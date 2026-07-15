#!/usr/bin/env python3
"""Byte-matching progress for C-converted functions.

For every function that progress.py counts as converted to C, compare its
disassembly in the linked ELF (looked up by symbol name, so immune to
section-level layout drift) against ground-truth bytes read from the
pristine decompressed code image (conker.<version>.bin) at the function's
VRAM-derived file offset.

Each function is classified as:
  exact    - every instruction word matches retail
  blocked  - only j/jal target addresses differ (waiting on a callee/caller
             elsewhere to be matched; the function itself needs no edits)
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
import subprocess
import sys
from collections import defaultdict

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
    cur = None
    for line in out.splitlines():
        m = re.match(r"^[0-9a-f]+ <(\S+)>:", line)
        if m:
            cur = m.group(1)
            funcs[cur] = []
            continue
        m = re.match(r"^\s*[0-9a-f]+:\s+([0-9a-f]{8})\s", line)
        if m and cur is not None:
            funcs[cur].append(int(m.group(1), 16))
    return funcs


def is_jump(word_a, word_b):
    op_a, op_b = word_a >> 26, word_b >> 26
    return op_a == op_b and op_a in (2, 3)  # j, jal


def classify(ours, truth):
    if len(ours) < len(truth) and all(w == 0 for w in truth[len(ours):]):
        # Trailing words are inter-function alignment nops that splat's
        # boundary detection folded into this symbol's declared length -
        # they aren't part of the function itself, so don't let them force
        # a "diff" verdict on an otherwise byte-exact function.
        truth = truth[:len(ours)]
    if len(ours) != len(truth):
        return "diff", max(abs(len(ours) - len(truth)), 1)
    real = jump = 0
    for a, b in zip(ours, truth):
        if a != b:
            if is_jump(a, b):
                jump += 1
            else:
                real += 1
    if real:
        return "diff", real
    if jump:
        return "blocked", 0
    return "exact", 0


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
    elf = load_elf_functions(args.elf, args.objdump)

    stats = defaultdict(lambda: defaultdict(int))  # section -> class -> n
    nonexact = []
    with open(args.progress_csv, newline="") as f:
        for row in csv.DictReader(f):
            if row.get("version") != args.version or row["language"] != "c":
                continue
            section = row["section"]
            if section not in segments:
                continue
            name = row["function"]
            vaddr = int(row["offset"])
            nwords = int(row["length"]) // 4
            vram, rom_start = segments[section]
            off = vaddr - vram + rom_start
            truth = [int.from_bytes(rom[off + i*4: off + i*4 + 4], "big")
                     for i in range(nwords)]
            ours = elf.get(name)
            if ours is None:
                kind, ndiff = "diff", nwords
            else:
                kind, ndiff = classify(ours, truth)
            stats[section][kind] += 1
            if kind != "exact":
                nonexact.append((ndiff, kind, section, name, nwords))

    order = [s for s in ("init", "game", "debugger") if s in stats]
    print("| Section | Byte-exact | Blocked on callees | Still differ |")
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
