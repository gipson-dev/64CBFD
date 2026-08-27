#!/usr/bin/env python3
"""Find EXACT functions with 'jal; or a0,v0,zero' delay-slot move."""
import subprocess, re

out = subprocess.run(["mips-linux-gnu-objdump", "-d", "-z", "build/conker.us.elf"],
                     capture_output=True, text=True).stdout
nonexact = set()
for l in open("../nonexact.txt"):
    m = re.match(r"^(?:DIFF|BLOCK)\s+(\S+)", l)
    if m:
        nonexact.add(m.group(1))

cur = None
hits = []
prev = ""
for line in out.splitlines():
    m = re.match(r"^([0-9a-f]+) <(\S+)>:", line)
    if m:
        cur = m.group(2)
        continue
    if "or\ta0,v0,zero" in line and "jal" in prev:
        hits.append(cur)
    prev = line

exact_hits = [h for h in hits if h not in nonexact]
print(f"{len(hits)} total, {len(exact_hits)} exact")
for h in exact_hits[:6]:
    print(h)
