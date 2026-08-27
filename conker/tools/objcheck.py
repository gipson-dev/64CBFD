#!/usr/bin/env python3
"""Compare functions in build/p2.o against a retail word list on stdin."""
import subprocess
import re
import sys

RETAIL = [l.strip().upper() for l in sys.stdin if l.strip()]
obj = sys.argv[1] if len(sys.argv) > 1 else "build/p2.o"
out = subprocess.run(["mips-linux-gnu-objdump", "-d", "-z", obj],
                     capture_output=True, text=True).stdout
words = {}
cur = None
for line in out.splitlines():
    m = re.match(r"^([0-9a-f]+) <(\S+)>:", line)
    if m:
        cur = m.group(2)
        words[cur] = []
        continue
    m = re.match(r"^\s*[0-9a-f]+:\s+([0-9a-f]{8})\s", line)
    if m and cur:
        words[cur].append(m.group(1).upper())
for k, v in words.items():
    if v == RETAIL:
        print("EXACT:", k)
    elif len(v) == len(RETAIL) and sum(1 for a, b in zip(v, RETAIL) if a == b) >= len(RETAIL) - 2:
        print("close:", k, [f"{i}:{a}" for i, (a, b) in enumerate(zip(v, RETAIL)) if a != b])
