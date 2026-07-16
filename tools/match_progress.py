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
one line per non-exact function, smallest real diff first.
"""
import argparse
import csv
import re
import signal
import subprocess
import sys
from collections import defaultdict

if hasattr(signal, "SIGPIPE"):
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# (vram_start, rom_start) per section, from conker/conker.us.yaml.
SEGMENTS = {
    "us": {
        "init": (0x10001000, 0x1000),
        "game": (0x15000000, 0x2D4B0),
        "debugger": (0x16000000, 0x255880),
    },
}


def load_elf_functions(elf_path, objdump):
    out = subprocess.run([objdump, "-d", elf_path],
                         capture_output=True, text=True, check=True).stdout
    funcs = {}
    symbols_by_addr = {}
    cur = None
    for line in out.splitlines():
        m = re.match(r"^([0-9a-f]+) <(\S+)>:", line)
        if m:
            addr = int(m.group(1), 16)
            cur = m.group(2)
            funcs[cur] = []
            symbols_by_addr[addr] = cur
            continue
        m = re.match(r"^\s*[0-9a-f]+:\s+([0-9a-f]{8})\s", line)
        if m and cur is not None:
            funcs[cur].append(int(m.group(1), 16))
    return funcs, symbols_by_addr


def is_jump(word_a, word_b):
    op_a, op_b = word_a >> 26, word_b >> 26
    return op_a == op_b and op_a in (2, 3)  # j, jal


def name_implied_vram(name):
    m = re.fullmatch(r"func_([0-9A-Fa-f]{8})", name)
    if m:
        return int(m.group(1), 16)
    return None


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


def is_symbol_addr_drift(ours, truth, i, symbols_by_addr):
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


def classify(ours, truth, symbols_by_addr):
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
            elif (drift := is_symbol_addr_drift(ours, truth, i, symbols_by_addr)):
                jump += drift
                i += 1
            elif i > 0 and is_symbol_addr_drift(ours, truth, i - 1, symbols_by_addr):
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


def function_vram(row):
    """Use name-implied VRAM when possible so upstream size drift is harmless."""
    name = row["function"]
    m = re.fullmatch(r"func_([0-9A-Fa-f]{8})", name)
    if m:
        return int(m.group(1), 16)
    return int(row["offset"])


def add_retail_lengths(rows, version):
    by_section = defaultdict(list)
    for row in rows:
        if row.get("version") != version:
            continue
        section = row["section"]
        if section not in SEGMENTS[version]:
            continue
        vaddr = function_vram(row)
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("progress_csv")
    ap.add_argument("elf")
    ap.add_argument("pristine_bin")
    ap.add_argument("--version", default="us")
    ap.add_argument("--objdump", default="mips-linux-gnu-objdump")
    ap.add_argument("--list", action="store_true",
                    help="list non-exact functions, smallest diff first")
    args = ap.parse_args()

    if args.version not in SEGMENTS:
        sys.exit(f"no segment table for version '{args.version}' - "
                 f"add it to SEGMENTS in {sys.argv[0]}")
    segments = SEGMENTS[args.version]

    rom = open(args.pristine_bin, "rb").read()
    elf, symbols_by_addr = load_elf_functions(args.elf, args.objdump)

    with open(args.progress_csv, newline="") as f:
        rows = list(csv.DictReader(f))
    add_retail_lengths(rows, args.version)

    stats = defaultdict(lambda: defaultdict(int))  # section -> class -> n
    nonexact = []
    for row in rows:
        if row.get("version") != args.version or row["language"] != "c":
            continue
        section = row["section"]
        if section not in segments:
            continue
        name = row["function"]
        vaddr = function_vram(row)
        nwords = row.get("_retail_nwords", int(row["length"]) // 4)
        vram, rom_start = segments[section]
        off = vaddr - vram + rom_start
        truth = [int.from_bytes(rom[off + i*4: off + i*4 + 4], "big")
                 for i in range(nwords)]
        ours = elf.get(name)
        if ours is None:
            kind, ndiff = "diff", nwords
        else:
            kind, ndiff = classify(ours, truth, symbols_by_addr)
        stats[section][kind] += 1
        if kind != "exact":
            nonexact.append((ndiff, kind, section, name, nwords))

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
        for ndiff, kind, section, name, nwords in nonexact:
            if kind == "blocked":
                print(f"BLOCK {name} ({section}, {nwords} words)")
            else:
                print(f"DIFF  {name} ({section}, {nwords} words): "
                      f"{ndiff} real diffs")


if __name__ == "__main__":
    main()
