#!/usr/bin/env python3
"""Batch-run perm.py --apply over the non-exact worklist.

usage: batch_perm.py [max_diffs]   (default 4)
"""
import re
import subprocess
import sys
from pathlib import Path

MAXD = int(sys.argv[1]) if len(sys.argv) > 1 else 4

# parse Makefile OPT_FLAGS/MIPSBIT overrides for files
mk = Path("Makefile").read_text()
overrides = {}
for m in re.finditer(r"build/src/([\w/]+)\.c\.o:\s*(OPT_FLAGS := [^\n]+|MIPSBIT := [^\n]+)", mk):
    f, val = m.group(1), m.group(2)
    overrides.setdefault(f, []).append(val)

# worklist
funcs = []
for line in Path("../nonexact.txt").read_text().splitlines():
    m = re.match(r"^DIFF\s+(\S+) \((\w+), (\d+) words\): (\d+) real diffs", line)
    if not m:
        continue
    fn, sec, words, diffs = m.group(1), m.group(2), int(m.group(3)), int(m.group(4))
    if diffs <= MAXD:
        funcs.append((diffs, fn))
funcs.sort()
print(f"{len(funcs)} functions with <= {MAXD} diffs")

# progress.csv filename mapping
import csv
srcfile = {}
with open("progress.csv", newline="") as f:
    for r in csv.DictReader(f):
        if r.get("version") == "us":
            srcfile[r["function"]] = r["filename"]

wins, fails = [], []
for diffs, fn in funcs:
    fname = srcfile.get(fn)
    if not fname:
        continue
    flags = None
    ovr = overrides.get(fname)
    if ovr:
        flagparts = []
        for o in ovr:
            v = o.split(":=", 1)[1].strip()
            flagparts.append(v)
        flags = " ".join(flagparts)
    cmd = ["python3", "tools/perm.py", fn, "--apply"]
    if flags:
        cmd += ["--flags", flags]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        fails.append(fn)
        continue
    if "EXACT VARIANT" in r.stdout and "applied to" in r.stdout:
        wins.append(fn)
        print(f"WIN {fn}")
    else:
        first = [l for l in r.stdout.splitlines() if l.strip().startswith(("0", "1", "2", "3", "4", "5"))][:1]
        fails.append(fn)
        print(f"--   {fn} {' '.join(first)}")

print(f"\nwins: {len(wins)}, fails: {len(fails)}")
for w in wins:
    print(" ", w)
