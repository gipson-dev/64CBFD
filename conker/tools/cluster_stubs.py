#!/usr/bin/env python3
"""Cluster stub functions by retail instruction pattern.

For each stub (return-0 placeholder), extract retail words, build a
normalized opcode signature, and cluster. Big clusters = template-able
families for automated C generation.
"""
import csv
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, "../tools")
import match_progress as mp

segments = mp.load_segments("us", "progress.csv", "build/conker.us.elf", "conker.us.bin")
symbol_addrs = mp.load_symbol_addrs("symbol_addrs.us.txt")
with open("progress.csv", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r.get("version") == "us"]
mp.add_retail_lengths(rows, "us", segments, symbol_addrs)
row_by_name = {r["function"]: r for r in rows}

rom = open("conker.us.bin", "rb").read()

# find stubs: source file contains "return 0;" body per earlier scan
stubs = [l.strip() for l in open("stubs.txt") if l.strip()]
if not stubs:
    sys.exit("stubs.txt empty")

OPCODE_NAMES = {
    0x00: "SPECIAL", 0x01: "REGIMM", 0x02: "j", 0x03: "jal", 0x04: "beq",
    0x05: "bne", 0x06: "blez", 0x07: "bgtz", 0x08: "addiu", 0x09: "addiu",
    0x0A: "slti", 0x0B: "sltiu", 0x0C: "andi", 0x0D: "ori", 0x0E: "xori",
    0x0F: "lui", 0x1C: "SPECIAL2", 0x20: "lb", 0x21: "lh", 0x23: "lw",
    0x24: "lbu", 0x25: "lhu", 0x28: "sb", 0x29: "sh", 0x2B: "sw",
    0x31: "lwc1", 0x35: "ldc1", 0x39: "swc1", 0x3D: "sdc1",
    0x10: "cop0", 0x11: "cop1", 0x12: "cop2",
}

def sig(words):
    parts = []
    for w in words:
        op = w >> 26
        if op == 0:
            fn = w & 0x3F
            parts.append(f"S.{fn}")
        elif op in (0x02, 0x03):
            parts.append(OPCODE_NAMES[op])
        elif op in (4, 5):
            parts.append(OPCODE_NAMES[op])
        else:
            parts.append(OPCODE_NAMES.get(op, hex(op)))
    return " ".join(parts)

clusters = defaultdict(list)
for fn in stubs:
    row = row_by_name.get(fn)
    if not row:
        continue
    vaddr = mp.function_vram(row, symbol_addrs)
    vram, rom_start = segments[row["section"]]
    off = vaddr - vram + rom_start
    n = row["_retail_nwords"]
    words = [int.from_bytes(rom[off + i*4:off + i*4 + 4], "big") for i in range(n)]
    clusters[sig(words)].append(fn)

sizes = sorted(((len(v), k) for k, v in clusters.items()), reverse=True)
print(f"{len(stubs)} stubs in {len(clusters)} clusters")
for n, k in sizes[:25]:
    print(f"{n:4}x  {k[:110]}")
