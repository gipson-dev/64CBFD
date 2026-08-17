#!/usr/bin/env python3
"""Side-by-side word diff: linked ELF vs retail bytes, with disasm text.

Usage: fdiff.py <func> [more funcs...]      (run from conker/)
Options via env: SHOW=max diffs per func (default 10)
"""
import sys, os, re, csv, subprocess, glob

sys.path.insert(0, "../tools")
import match_progress as mp

elf_path = "build/conker.us.elf"
bin_path = "conker.us.bin"
SHOW = int(os.environ.get("SHOW", "10"))

names = sys.argv[1:]
if not names:
    sys.exit("usage: fdiff.py FUNC [FUNC...]")

segments = mp.load_segments("us", "progress.csv", elf_path, bin_path)
symbol_addrs = mp.load_symbol_addrs("symbol_addrs.us.txt")
rom = open(bin_path, "rb").read()
funcs, symbols_by_addr, func_addrs = mp.load_elf_functions(elf_path, "mips-linux-gnu-objdump")

with open("progress.csv", newline="") as f:
    rows = [r for r in csv.DictReader(f) if r.get("version") == "us"]
mp.add_retail_lengths(rows, "us", segments, symbol_addrs)
row_by_name = {r["function"]: r for r in rows}

# full disasm text for ours (single pass): addr -> text
disasm_text = {}
out = subprocess.run(["mips-linux-gnu-objdump", "-d", "-z", elf_path],
                     capture_output=True, text=True).stdout
for line in out.splitlines():
    m = re.match(r"^\s*([0-9a-f]+):\s+([0-9a-f]{8})\s+(.*)", line)
    if m:
        disasm_text[int(m.group(1), 16)] = m.group(3).strip()

# retail asm text: addr -> text (parse all asm/*.s once, cache by vram)
retail_text = {}
for path in glob.glob("asm/**/*.s", recursive=True):
    try:
        txt = open(path).read()
    except OSError:
        continue
    for line in txt.splitlines():
        m = re.match(r"\s*/\*\s*[0-9A-Fa-f]+\s+([0-9A-Fa-f]{8})\s+[0-9A-Fa-f]{8}\s*\*/\s+(.*)", line)
        if m:
            retail_text[int(m.group(1), 16)] = m.group(2).strip()

tot_exact = 0
for name in names:
    row = row_by_name.get(name)
    if row is None:
        print(f"{name}: NOT FOUND in progress.csv")
        continue
    section = row["section"]
    vaddr = mp.function_vram(row, symbol_addrs)
    nwords = row["_retail_nwords"]
    vram, rom_start = segments[section]
    off = vaddr - vram + rom_start
    truth = [int.from_bytes(rom[off + i*4: off + i*4 + 4], "big") for i in range(nwords)]
    ours = funcs.get(name)
    if ours is None:
        print(f"{name}: NOT IN ELF")
        continue
    kind, ndiff = mp.classify(ours, truth, symbols_by_addr, symbol_addrs)
    print(f"{name}: {kind}, {ndiff} real diffs, ours {len(ours)} vs retail {nwords} words @ {vaddr:08X}")
    if kind == "exact":
        tot_exact += 1
        continue
    our_base = func_addrs.get(name, vaddr)
    shown = 0
    for i in range(max(len(ours), nwords)):
        w_ours = ours[i] if i < len(ours) else None
        w_true = truth[i] if i < nwords else None
        if w_ours == w_true:
            continue
        shown += 1
        t1 = disasm_text.get(our_base + i*4, "")
        t2 = retail_text.get(vaddr + i*4, "")
        a = f"{w_ours:08X} {t1}" if w_ours is not None else "--"
        b = f"{w_true:08X} {t2}" if w_true is not None else "--"
        print(f"** [{i:3}] ours   {a}")
        print(f"**       retail {b}")
        if shown >= SHOW:
            print("   ...")
            break
print(f"\n{tot_exact}/{len(names)} exact")
