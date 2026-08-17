#!/usr/bin/env python3
"""Verify one function in a compiled object against retail bytes.

Usage (from conker/): python3 tools/fcheck.py FUNC OBJ
Prints diff count and inline word diffs. Exit 0 when all words match
(jumps/relocated words tolerated).
"""
import re
import subprocess
import sys

sys.path.insert(0, "../tools")
import match_progress as mp

name, obj = sys.argv[1], sys.argv[2]

segments = mp.load_segments("us", "progress.csv", "build/conker.us.elf", "conker.us.bin")
symbol_addrs = mp.load_symbol_addrs("symbol_addrs.us.txt")
import csv
with open("progress.csv", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r.get("version") == "us"]
mp.add_retail_lengths(rows, "us", segments, symbol_addrs)
row = next((r for r in rows if r["function"] == name), None)
if row is None:
    sys.exit(f"{name} not in progress.csv")
vaddr = mp.function_vram(row, symbol_addrs)
vram, rom_start = segments[row["section"]]
off = vaddr - vram + rom_start
rom = open("conker.us.bin", "rb").read()
n = row["_retail_nwords"]
truth = [int.from_bytes(rom[off + i * 4:off + i * 4 + 4], "big") for i in range(n)]

out = subprocess.run(["mips-linux-gnu-objdump", "-d", "-z", obj],
                     capture_output=True, text=True).stdout
rout = subprocess.run(["mips-linux-gnu-objdump", "-r", obj],
                      capture_output=True, text=True).stdout

words = None
cur = None
cur_base = 0
base = 0
rel_offs = set()
for line in out.splitlines():
    m = re.match(r"^([0-9a-f]+) <(\S+)>:", line)
    if m:
        cur = m.group(2)
        cur_base = int(m.group(1), 16)
        if cur == name:
            words = []
            base = cur_base
        continue
    m = re.match(r"^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s", line)
    if m and cur == name:
        words.append(int(m.group(2), 16))
for line in rout.splitlines():
    m = re.match(r"^([0-9a-f]+)\s+R_MIPS", line)
    if m:
        rel_offs.add(int(m.group(1), 16))

if not words:
    sys.exit(f"{name} not found in {obj}")

diffs = []
for i in range(max(len(words), n)):
    a = words[i] if i < len(words) else None
    t = truth[i] if i < n else None
    if a == t:
        continue
    if a is not None and t is not None and (a >> 26) in (2, 3) and (t >> 26) in (2, 3):
        continue
    if base + i * 4 in rel_offs:
        continue
    diffs.append((i, a, t))

print(f"{name}: {len(diffs)} word diffs ({len(words)} vs {n} words)")
for i, a, t in diffs[:12]:
    print(f"** [{i:3}] obj    {a:08X}" if a is not None else f"** [{i:3}] obj    --")
    print(f"**       retail {t:08X}" if t is not None else "**       retail --")
if len(diffs) > 12:
    print(f"... {len(diffs) - 12} more")
sys.exit(0 if not diffs else 1)
