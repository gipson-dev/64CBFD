#!/usr/bin/env python3
"""Find functions with jal + delay-slot 'sw a0,0x18(sp)' homing that are EXACT."""
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
    if "sw\ta0,24(sp)" in line and "jal" in prev:
        hits.append(cur)
    prev = line

exact_hits = [h for h in hits if h not in nonexact]
print(f"{len(hits)} total, {len(exact_hits)} exact")
for h in exact_hits[:10]:
    print(h)
