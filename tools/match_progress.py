#!/usr/bin/env python3
"""Byte-matching progress for C-converted functions.

For every function that progress.py counts as converted to C, compare its
disassembly in the linked ELF (looked up by symbol name, so immune to
section-level layout drift) against ground-truth bytes read from the
pristine decompressed code image (conker.<version>.bin) at the function's
VRAM-derived file offset.

Each function is classified as:
  exact    - every instruction word matches retail
  blocked  - only external addresses differ (waiting on a callee/caller,
             literal pool, or shifted data symbol to be matched elsewhere;
             the function itself needs no edits)
  diff     - real instruction differences remain (or the length differs)

Usage:
  match_progress.py <progress.csv> <elf> <pristine.bin> [--version us]
                    [--objdump mips-linux-gnu-objdump] [--list]

progress.csv is the file `make -C conker progress` generates. --list prints
one line per non-exact function, smallest real diff first. --explain-blocks
adds short target summaries to blocked rows.
"""
import argparse
import csv
import os
import re
import signal
import subprocess
import sys
from collections import Counter, defaultdict

if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Fallback (vram_start, rom_start) per section, from conker/conker.*.yaml.
DEFAULT_SEGMENTS = {
    "us": {
        "init": (0x10001000, 0x1000),
        "game": (0x15000000, 0x2D4B0),
        "debugger": (0x16000000, 0x255880),
    },
    "eu": {
        "init": (0x10001000, 0x1000),
        "game": (0x15000000, 0x2D810),
        "debugger": (0x16000000, 0x256450),
    },
    "ects": {
        "init": (0x10001000, 0x1000),
        "game": (0x15000000, 0xCAF0),
        "debugger": (0x16000000, 0x224500),
    },
    "debug": {
        "init": (0x10001000, 0x1000),
        "game": (0x15000000, 0xD2B0),
        "debugger": (0x16000000, 0x248510),
    },
}


def load_elf_functions(elf_path, objdump):
    out = subprocess.run([objdump, "-d", elf_path],
                         capture_output=True, text=True, check=True).stdout
    funcs = {}
    func_addrs = {}
    symbols_by_addr = {}
    cur = None
    for line in out.splitlines():
        m = re.match(r"^([0-9a-f]+) <(\S+)>:", line)
        if m:
            addr = int(m.group(1), 16)
            cur = m.group(2)
            funcs[cur] = []
            func_addrs[cur] = addr
            symbols_by_addr[addr] = cur
            continue
        m = re.match(r"^\s*[0-9a-f]+:\s+([0-9a-f]{8})\s", line)
        if m and cur is not None:
            funcs[cur].append(int(m.group(1), 16))
    return funcs, symbols_by_addr, func_addrs


def is_jump(word_a, word_b):
    op_a, op_b = word_a >> 26, word_b >> 26
    return op_a == op_b and op_a in (2, 3)  # j, jal


def jump_target(word, pc):
    return ((pc + 4) & 0xF0000000) | ((word & 0x03FFFFFF) << 2)


def jump_name(word):
    return {2: "j", 3: "jal"}.get(word >> 26, "jump")


def name_implied_vram(name):
    m = re.fullmatch(r"(?:func|D)_([0-9A-Fa-f]{8})", name)
    if m:
        return int(m.group(1), 16)
    return None


def candidate_project_dirs(*paths):
    dirs = []
    for path in paths:
        if not path:
            continue
        path = os.path.abspath(path)
        if os.path.isdir(path):
            cur = path
        else:
            cur = os.path.dirname(path)
        while cur and cur not in dirs:
            dirs.append(cur)
            parent = os.path.dirname(cur)
            if parent == cur:
                break
            cur = parent
    cwd = os.getcwd()
    if cwd not in dirs:
        dirs.append(cwd)
    return dirs


def load_segments(version, *paths):
    yaml_name = f"conker.{version}.yaml"
    for directory in candidate_project_dirs(*paths):
        path = os.path.join(directory, yaml_name)
        if not os.path.exists(path):
            continue
        segments = {}
        current = None
        current_type = None
        current_start = None
        current_vram = None
        with open(path) as f:
            for line in f:
                m = re.match(r"\s*-\s+name:\s*(\w+)\s*(?:#.*)?$", line)
                if m:
                    if (current in ("init", "game", "debugger") and
                            current_type == "code" and
                            current_start is not None and
                            current_vram is not None):
                        segments[current] = (current_vram, current_start)
                    current = m.group(1)
                    current_type = None
                    current_start = None
                    current_vram = None
                    continue
                if current is None:
                    continue
                m = re.match(r"\s*type:\s*(\w+)", line)
                if m:
                    current_type = m.group(1)
                    continue
                m = re.match(r"\s*start:\s*(0x[0-9A-Fa-f]+)", line)
                if m:
                    current_start = int(m.group(1), 16)
                    continue
                m = re.match(r"\s*vram:\s*(0x[0-9A-Fa-f]+)", line)
                if m:
                    current_vram = int(m.group(1), 16)
                    continue
        if (current in ("init", "game", "debugger") and
                current_type == "code" and current_start is not None and
                current_vram is not None):
            segments[current] = (current_vram, current_start)
        if segments:
            return segments
    return DEFAULT_SEGMENTS.get(version)


def default_symbol_addrs_path(version, progress_csv, elf_path, pristine_bin):
    filename = f"symbol_addrs.{version}.txt"
    for directory in candidate_project_dirs(progress_csv, pristine_bin,
                                            elf_path):
        path = os.path.join(directory, filename)
        if os.path.exists(path):
            return path
    return os.path.join(os.path.dirname(progress_csv) or ".", filename)


def load_symbol_addrs(path):
    """Retail VRAM anchors for named (non-func_XXXXXXXX) symbols."""
    addrs = {}
    try:
        with open(path) as f:
            for line in f:
                m = re.match(r"^\s*(\w+)\s*=\s*0x([0-9A-Fa-f]+)\s*;", line)
                if m:
                    addrs[m.group(1)] = int(m.group(2), 16)
    except FileNotFoundError:
        pass
    return addrs


def decode_addr_pair(hi_word, lo_word):
    hi_op = hi_word >> 26
    lo_op = lo_word >> 26
    hi_rs = (hi_word >> 21) & 0x1F
    hi_rt = (hi_word >> 16) & 0x1F
    lo_rs = (lo_word >> 21) & 0x1F
    lo_rt = (lo_word >> 16) & 0x1F
    if hi_op != 0x0F or hi_rs != 0 or lo_rs != hi_rt:
        return None
    upper = (hi_word & 0xFFFF) << 16
    lower = lo_word & 0xFFFF
    if lo_op == 0x09 and lo_rt == hi_rt:  # addiu rt,rt,%lo(sym)
        if lower & 0x8000:
            lower -= 0x10000
        return (upper + lower) & 0xFFFFFFFF
    if lo_op == 0x0D and lo_rt == hi_rt:  # ori rt,rt,%lo(sym)
        return upper | lower
    return None


def is_symbol_addr_drift(ours, truth, i, symbols_by_addr, symbol_addrs):
    if i + 1 >= len(ours) or i + 1 >= len(truth):
        return 0
    if ours[i] == truth[i] and ours[i + 1] == truth[i + 1]:
        return 0
    ours_addr = decode_addr_pair(ours[i], ours[i + 1])
    truth_addr = decode_addr_pair(truth[i], truth[i + 1])
    if ours_addr is None or truth_addr is None:
        return 0
    target = symbols_by_addr.get(ours_addr)
    if target is None:
        return 0
    implied = name_implied_vram(target)
    if implied is None:
        implied = symbol_addrs.get(target)
    if implied != truth_addr:
        return 0
    return int(ours[i] != truth[i]) + int(ours[i + 1] != truth[i + 1])


def is_load_store(word):
    op = word >> 26
    return op in {
        0x20,  # lb
        0x21,  # lh
        0x23,  # lw
        0x24,  # lbu
        0x25,  # lhu
        0x28,  # sb
        0x29,  # sh
        0x2B,  # sw
        0x31,  # lwc1
        0x35,  # ldc1
        0x39,  # swc1
        0x3D,  # sdc1
    }


def is_external_load_drift(ours, truth, i):
    if (ours[i] & 0xFFFF0000) != (truth[i] & 0xFFFF0000):
        return False
    base = (ours[i] >> 21) & 0x1F
    if base in (0, 29, 30):
        return False
    start = max(0, i - 8)
    for j in range(i - 1, start - 1, -1):
        if ours[j] != truth[j]:
            continue
        if (ours[j] >> 26) == 0x0F and ((ours[j] >> 21) & 0x1F) == 0:
            if ((ours[j] >> 16) & 0x1F) == base:
                return True
    return False


def is_external_addr_drift(ours, truth, i):
    op = ours[i] >> 26
    rt = (ours[i] >> 16) & 0x1F
    rs = (ours[i] >> 21) & 0x1F
    if is_load_store(ours[i]):
        return is_external_load_drift(ours, truth, i)
    if op in (0x09, 0x0D) and rs == rt:  # addiu/ori rt,rt,%lo(sym)
        return is_external_load_drift(ours, truth, i)
    return False


def classify(ours, truth, symbols_by_addr, symbol_addrs):
    if len(ours) < len(truth) and all(w == 0 for w in truth[len(ours):]):
        # Trailing words are inter-function alignment nops that splat's
        # boundary detection folded into this symbol's declared length -
        # they aren't part of the function itself, so don't let them force
        # a "diff" verdict on an otherwise byte-exact function.
        truth = truth[:len(ours)]
    length_diff = abs(len(ours) - len(truth))
    real = jump = 0
    i = 0
    while i < min(len(ours), len(truth)):
        a, b = ours[i], truth[i]
        if a != b:
            if is_jump(a, b):
                jump += 1
            elif (drift := is_symbol_addr_drift(ours, truth, i,
                                                symbols_by_addr, symbol_addrs)):
                jump += drift
                i += 1
            elif i > 0 and is_symbol_addr_drift(ours, truth, i - 1,
                                                symbols_by_addr, symbol_addrs):
                jump += 1
            elif is_external_addr_drift(ours, truth, i):
                jump += 1
            else:
                real += 1
        i += 1
    real += length_diff
    if real:
        return "diff", real
    if jump:
        return "blocked", 0
    return "exact", 0


def target_label(addr, symbols_by_addr):
    name = symbols_by_addr.get(addr)
    if name:
        return f"{name}@0x{addr:08X}"
    return f"0x{addr:08X}"


def explain_block(ours, truth, ours_vaddr, retail_vaddr, current_symbols,
                  retail_symbols, symbol_addrs):
    if len(ours) < len(truth) and all(w == 0 for w in truth[len(ours):]):
        truth = truth[:len(ours)]
    reasons = Counter()
    i = 0
    while i < min(len(ours), len(truth)):
        a, b = ours[i], truth[i]
        if a != b:
            if is_jump(a, b):
                ours_target = jump_target(a, ours_vaddr + i * 4)
                truth_target = jump_target(b, retail_vaddr + i * 4)
                reasons[
                    f"{jump_name(a)} target "
                    f"{target_label(ours_target, current_symbols)} -> "
                    f"{target_label(truth_target, retail_symbols)}"
                ] += 1
            elif (drift := is_symbol_addr_drift(ours, truth, i,
                                                current_symbols,
                                                symbol_addrs)):
                ours_addr = decode_addr_pair(ours[i], ours[i + 1])
                truth_addr = decode_addr_pair(truth[i], truth[i + 1])
                reasons[
                    "addr pair "
                    f"{target_label(ours_addr, current_symbols)} -> "
                    f"{target_label(truth_addr, retail_symbols)}"
                ] += drift
                i += 1
            elif i > 0 and is_symbol_addr_drift(ours, truth, i - 1,
                                                current_symbols,
                                                symbol_addrs):
                pass
            elif is_external_addr_drift(ours, truth, i):
                reasons["external load/store immediate drift"] += 1
            else:
                reasons["unclassified drift"] += 1
        i += 1
    if len(ours) != len(truth):
        reasons[f"length drift {len(ours)} -> {len(truth)} words"] += abs(
            len(ours) - len(truth))
    return reasons


def function_vram(row, symbol_addrs):
    """Use name-implied VRAM (or symbol_addrs.<version>.txt for other
    named symbols) so upstream size drift is harmless. progress.csv's
    offset column reflects the *current build's* layout and is only a last
    resort."""
    name = row["function"]
    implied = name_implied_vram(name)
    if implied is not None:
        return implied
    if name in symbol_addrs:
        return symbol_addrs[name]
    return int(row["offset"])


def add_retail_lengths(rows, version, segments, symbol_addrs):
    by_section = defaultdict(list)
    for row in rows:
        if row.get("version") != version:
            continue
        section = row["section"]
        if section not in segments:
            continue
        vaddr = function_vram(row, symbol_addrs)
        by_section[section].append((vaddr, row))

    for entries in by_section.values():
        entries.sort(key=lambda t: t[0])
        for idx, (vaddr, row) in enumerate(entries):
            nwords = int(row["length"]) // 4
            if idx + 1 < len(entries):
                next_vaddr = entries[idx + 1][0]
                if next_vaddr > vaddr:
                    nwords = (next_vaddr - vaddr) // 4
            row["_retail_nwords"] = nwords


def retail_symbols_for_rows(rows, version, segments, symbol_addrs):
    symbols = {v: k for k, v in symbol_addrs.items()}
    for row in rows:
        if row.get("version") != version:
            continue
        if row.get("section") not in segments:
            continue
        try:
            symbols[function_vram(row, symbol_addrs)] = row["function"]
        except (KeyError, ValueError):
            pass
    return symbols


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("progress_csv")
    ap.add_argument("elf")
    ap.add_argument("pristine_bin")
    ap.add_argument("--version", default="us")
    ap.add_argument("--objdump", default="mips-linux-gnu-objdump")
    ap.add_argument("--symbol-addrs", default=None,
                    help="retail VRAM anchors for named symbols (default: "
                         "symbol_addrs.<version>.txt next to progress.csv)")
    ap.add_argument("--list", action="store_true",
                    help="list non-exact functions, smallest diff first")
    ap.add_argument("--explain-blocks", action="store_true",
                    help="with --list, show why blocked rows are classified "
                         "as address/callee drift")
    args = ap.parse_args()

    segments = load_segments(args.version, args.progress_csv, args.elf,
                             args.pristine_bin)
    if not segments:
        sys.exit(f"no segment table for version '{args.version}' - "
                 f"add it to DEFAULT_SEGMENTS or conker.{args.version}.yaml")

    rom = open(args.pristine_bin, "rb").read()
    elf, symbols_by_addr, func_addrs = load_elf_functions(args.elf,
                                                          args.objdump)

    symbol_addrs = load_symbol_addrs(args.symbol_addrs or
                                     default_symbol_addrs_path(
                                         args.version, args.progress_csv,
                                         args.elf, args.pristine_bin))

    with open(args.progress_csv, newline="") as f:
        rows = list(csv.DictReader(f))
    add_retail_lengths(rows, args.version, segments, symbol_addrs)
    retail_symbols = retail_symbols_for_rows(rows, args.version, segments,
                                             symbol_addrs)

    stats = defaultdict(lambda: defaultdict(int))  # section -> class -> n
    nonexact = []
    for row in rows:
        if row.get("version") != args.version or row["language"] != "c":
            continue
        section = row["section"]
        if section not in segments:
            continue
        name = row["function"]
        vaddr = function_vram(row, symbol_addrs)
        nwords = row.get("_retail_nwords", int(row["length"]) // 4)
        vram, rom_start = segments[section]
        off = vaddr - vram + rom_start
        truth = [int.from_bytes(rom[off + i*4: off + i*4 + 4], "big")
                 for i in range(nwords)]
        ours = elf.get(name)
        if ours is None:
            kind, ndiff = "diff", nwords
        else:
            kind, ndiff = classify(ours, truth, symbols_by_addr, symbol_addrs)
        stats[section][kind] += 1
        if kind != "exact":
            reasons = None
            if args.explain_blocks and kind == "blocked" and ours is not None:
                reasons = explain_block(
                    ours, truth, func_addrs.get(name, vaddr), vaddr,
                    symbols_by_addr, retail_symbols, symbol_addrs)
            nonexact.append((ndiff, kind, section, name, nwords, reasons))

    order = [s for s in ("init", "game", "debugger") if s in stats]
    print("| Section | Byte-exact | Blocked on address drift | Still differ |")
    print("| --- | --- | --- | --- |")

    def line(name, st):
        total = st["exact"] + st["blocked"] + st["diff"]
        pct = 100 * st["exact"] / total if total else 0.0
        print(f"| {name} | {st['exact']} / {total} ({pct:.2f}%) "
              f"| {st['blocked']} | {st['diff']} |")

    total = defaultdict(int)
    for s in order:
        for k, v in stats[s].items():
            total[k] += v
    line("total", total)
    for s in order:
        line(s, stats[s])

    if args.list and nonexact:
        print()
        nonexact.sort(key=lambda t: (t[1] != "blocked", t[0]))
        for ndiff, kind, section, name, nwords, reasons in nonexact:
            if kind == "blocked":
                print(f"BLOCK {name} ({section}, {nwords} words)")
                if args.explain_blocks and reasons:
                    for reason, count in reasons.most_common(4):
                        print(f"      {count}x {reason}")
            else:
                print(f"DIFF  {name} ({section}, {nwords} words): "
                      f"{ndiff} real diffs")


if __name__ == "__main__":
    main()
