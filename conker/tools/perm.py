#!/usr/bin/env python3
"""Micro-permuter: apply transforms to one function's C source, compile all
variants in one object, score against retail bytes.

Usage (from conker/): python3 tools/perm.py <func_name> [--show N]
Pulls the function's C body from its source file (progress.csv mapping),
extracts retail words from conker.us.bin, generates variants, compiles with
project flags, and reports any byte-exact variant.

Variant strategies (applied combinatorially, capped):
 - swap operands of == and != comparisons
 - (a - b) == 0 / (b - a) == 0 subtraction idioms
 - swap operands of + * | & ^ (int and float)
 - parenthesize a+b+c right/left
 - reorder sequential loads/statements (swap independent statements)
"""
import argparse
import csv
import itertools
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, "../tools")
import match_progress as mp

CC = "../ido/ido5.3_recomp/cc"
CFLAGS = ("-c -32 -G 0 -Xfullwarn -Xcpluscomm -signed -nostdinc -non_shared "
          "-Wab,-r4300_mul -D_LANGUAGE_C -D_FINALROM -DF3DEX_GBI_2 "
          "-D_MIPS_SZLONG=32 -w -I . -I include -I include/2.0L "
          "-I include/2.0L/PR -I include/libc -I src/libultra/os "
          "-I src/libultra/audio -I src/libultra/io").split()
OPT = "-O2 -g3 -mips2 -o32".split()


def find_function(name):
    with open("progress.csv", newline="") as f:
        for r in csv.DictReader(f):
            if r["function"] == name and r.get("version") == "us":
                return r["filename"], r["language"]
    return None, None


def extract_body(src_path, name):
    text = Path(src_path).read_text()
    # find definition: name( ... ) { ... } (not a ;-terminated declaration)
    pat = re.compile(r"^[^\n]*\b" + re.escape(name) + r"\s*\(", re.M)
    for m in pat.finditer(text):
        brace = text.find("{", m.end())
        semi = text.find(";", m.end())
        if brace == -1 or (semi != -1 and semi < brace):
            continue
        depth = 0
        for i in range(brace, len(text)):
            if text[i] == "{":
                depth += 1
            elif text[i] == "}":
                depth -= 1
                if depth == 0:
                    return text[m.start():i + 1], (m.start(), i + 1)
    return None, None


def retail_words(name):
    segments = mp.load_segments("us", "progress.csv", "build/conker.us.elf", "conker.us.bin")
    symbol_addrs = mp.load_symbol_addrs("symbol_addrs.us.txt")
    with open("progress.csv", newline="") as f:
        rows = [r for r in csv.DictReader(f) if r.get("version") == "us"]
    mp.add_retail_lengths(rows, "us", segments, symbol_addrs)
    row = next(r for r in rows if r["function"] == name)
    vaddr = mp.function_vram(row, symbol_addrs)
    vram, rom_start = segments[row["section"]]
    off = vaddr - vram + rom_start
    rom = open("conker.us.bin", "rb").read()
    n = row["_retail_nwords"]
    return [int.from_bytes(rom[off + i * 4:off + i * 4 + 4], "big") for i in range(n)]


def variants_of(body):
    """Generate transformed bodies. Keep it bounded and semantically safe."""
    outs = []

    # atom: identifier with optional member/index chains and leading stars
    atom = r"(\*{0,2}\s*[\w]+(?:(?:->|\.)(?:\w+))*(?:\[[^\]]+\])*)"
    cmp_pat = re.compile(atom + r"\s*(==|!=)\s*" + atom)
    or_pat = re.compile(atom + r"\s*(\||&|\^)\s*" + atom)

    def swap_cmps(text, flip):
        def repl(m):
            a, op, b = m.group(1), m.group(2), m.group(3)
            if flip:
                return f"{b.strip()} {op} {a.strip()}"
            return m.group(0)
        return cmp_pat.sub(repl, text)

    def swap_or(text):
        return or_pat.sub(lambda m: f"{m.group(3)} {m.group(2)} {m.group(1)}", text)

    # 2. subtraction idiom: a == b -> (a - b) == 0 or (b - a) == 0
    def sub_idiom(text, direction):
        def repl(m):
            a, op, b = m.group(1).strip(), m.group(2), m.group(3).strip()
            if op == "==":
                if direction:
                    return f"({a} - {b}) == 0"
                return f"({b} - {a}) == 0"
            return m.group(0)
        return cmp_pat.sub(repl, text)

    outs.append(("base", body))
    outs.append(("swapcmp", swap_cmps(body, True)))
    for d in (True, False):
        outs.append((f"sub{int(d)}", sub_idiom(body, d)))
    outs.append(("swapcmp+sub1", sub_idiom(swap_cmps(body, True), True)))
    outs.append(("swapcmp+sub0", sub_idiom(swap_cmps(body, True), False)))
    outs.append(("swapor", swap_or(body)))
    outs.append(("swapcmp+or", swap_or(swap_cmps(body, True))))

    # 3. plus-operand swap: a + b -> b + a (top-level in return/assign lines)
    plus_pat = re.compile(r"(\b[\w.\[\]]+)\s*\+\s*([\w.\[\]]+)")
    def swap_plus(text):
        return plus_pat.sub(lambda m: f"{m.group(2)} + {m.group(1)}", text)
    outs.append(("swapplus", swap_plus(body)))

    # 4. right-parenthesize a + b + c chains
    chain_pat = re.compile(r"(\b[\w.\[\]]+)\s*\+\s*([\w.\[\]]+)\s*\+\s*([\w.\[\]]+)")
    def rparen(text):
        return chain_pat.sub(lambda m: f"{m.group(1)} + ({m.group(2)} + {m.group(3)})", text)
    outs.append(("rparen", rparen(body)))

    # 5. swap adjacent independent statements (lines ending with ;)
    lines = body.split("\n")
    decl_pat = re.compile(r"^\s*(?:u8|s8|u16|s16|u32|s32|u64|s64|f32|f64|void|char|int|short|long|float|double|struct|static|extern|const|volatile)\b")
    for i in range(len(lines) - 1):
        a, b = lines[i].strip(), lines[i + 1].strip()
        if a.endswith(";") and b.endswith(";") and not decl_pat.match(a) and not decl_pat.match(b) \
           and not a.startswith(("if", "}", "else", "do", "while", "for", "switch", "return")) \
           and not b.startswith(("if", "else", "do", "while", "for", "switch", "return", "}")):
            new = lines[:]
            new[i], new[i + 1] = lines[i + 1], lines[i]
            outs.append((f"swpline{i}", "\n".join(new)))

    # dedupe
    seen = {}
    for tag, b in outs:
        if b not in seen:
            seen[b] = tag
    return [(tag, b) for b, tag in seen.items()]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("func")
    ap.add_argument("--flags", default=None, help="extra flags: e.g. -O1")
    ap.add_argument("--show", type=int, default=3)
    args = ap.parse_args()

    fname, lang = find_function(args.func)
    if not fname:
        sys.exit("function not found")
    # source file search
    cands = list(Path("src").rglob(fname + ".c"))
    if not cands:
        sys.exit(f"source file for {fname} not found")
    body, span = extract_body(cands[0], args.func)
    if not body:
        sys.exit("function body not found")
    preamble = cands[0].read_text()[:span[0]]

    truth = retail_words(args.func)
    vs = variants_of(body)
    print(f"{args.func}: {len(vs)} variants, retail {len(truth)} words, src {cands[0]}")

    def nlcount(seq):
        return sum(s.count("\n") for s in seq)

    lines = [preamble, "\n"]
    ranges = []
    for i, (tag, b) in enumerate(vs):
        b2 = re.sub(r"\b" + re.escape(args.func) + r"\b", f"permfn_{i}", b)
        start_line = nlcount(lines)
        lines.append(b2 + "\n")
        ranges.append((start_line, nlcount(lines)))

    while True:
        Path("build/perm_test.c").write_text("".join(lines))
        cmd = [CC] + CFLAGS + (args.flags.split() if args.flags else OPT) + ["-o", "build/perm_test.o", "build/perm_test.c"]
        r = subprocess.run(cmd, capture_output=True, text=True)
        if r.returncode == 0:
            break
        # drop variants on failing lines
        bad = set()
        for em in re.finditer(r"perm_test\.c, line (\d+):", r.stderr):
            ln = int(em.group(1))
            for idx, (a, b) in enumerate(ranges):
                if a <= ln <= b:
                    bad.add(idx)
        if not bad:
            print(r.stderr[:2000])
            sys.exit("compile failed, cannot localize errors")
        for idx in sorted(bad, reverse=True):
            vs.pop(idx)
            ranges.pop(idx)
        lines = [preamble, "\n"]
        ranges = []
        for i, (tag, b) in enumerate(vs):
            b2 = re.sub(r"\b" + re.escape(args.func) + r"\b", f"permfn_{i}", b)
            start_line = nlcount(lines)
            lines.append(b2 + "\n")
            ranges.append((start_line, nlcount(lines)))
        if not vs:
            sys.exit("all variants failed to compile")

    out = subprocess.run(["mips-linux-gnu-objdump", "-d", "-z", "build/perm_test.o"],
                         capture_output=True, text=True).stdout
    relocs = subprocess.run(["mips-linux-gnu-objdump", "-r", "build/perm_test.o"],
                            capture_output=True, text=True).stdout
    reloc_by_func = {}
    cur = None
    for line in relocs.splitlines():
        m = re.match(r"^RELOCATION RECORDS FOR \[(.+)\]:", line)
        if m:
            cur = m.group(1)
            continue
        m = re.match(r"^([0-9a-f]+)\s+R_MIPS", line)
        if m and cur:
            reloc_by_func.setdefault(cur, set()).add(int(m.group(1), 16))

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
            words[cur].append(int(m.group(1), 16))

    scored = []
    for i, (tag, b) in enumerate(vs):
        w = words.get(f"permfn_{i}")
        if not w:
            continue
        rset = reloc_by_func.get(f".text.permfn_{i}", set()) | reloc_by_func.get(".text", set())
        # compare ignoring jal/j targets (unresolved in object): compare all
        # words but skip differences on j/jal encodings and relocated words
        diffs = 0
        for j, (a, t) in enumerate(itertools.zip_longest(w, truth, fillvalue=None)):
            if a == t:
                continue
            if a is not None and t is not None and (a >> 26) in (2, 3) and (t >> 26) in (2, 3):
                continue
            if j * 4 in rset:
                continue
            diffs += 1
        scored.append((diffs, tag, i))
    scored.sort()
    winner = None
    for d, tag, i in scored:
        if d == 0:
            winner = i
            break
    if winner is not None:
        tag, body = vs[winner]
        print(f"=== EXACT VARIANT [{tag}] ===")
        print(body)
        if args.apply:
            src = cands[0].read_text()
            # replace the original function definition with the variant body
            # (rename permfn back)
            new_body = body
            orig = src[span[0]:span[1]]
            assert orig.strip(), "empty original span"
            src2 = src[:span[0]] + new_body + src[span[1]:]
            cands[0].write_text(src2)
            print(f"applied to {cands[0]}")
    else:
        for d, tag, i in scored[:args.show]:
            print(f"  {d:3} diffs  [{tag}]")


if __name__ == "__main__":
    main()
