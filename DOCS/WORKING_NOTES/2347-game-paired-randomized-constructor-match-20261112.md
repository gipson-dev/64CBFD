# Paired Game randomized effect constructor matches

Date: 2026-11-12. `func_150C60D8` (`generated_F3270`) and
`func_150C6A08` (`generated_F3BA0`) replace zero-return placeholders with
semantic C. Each matches all **197 retail words** using 62 checked,
relocation-aware scheduling guards. Retail `func_151342BC` calls these
through entries 4 and 5 of the `0x80089A70` dispatch table.

The routines construct a randomized effect descriptor from position and
velocity arguments, read a floating-point owner field, make eight integer and
six floating-point random draws, and call `func_151303BC`. The factory reads
112 bytes from the descriptor; on success, the constructor copies its 40-byte
payload into the returned effect. The descriptor's intentionally untouched
gap and tail are preserved.

The earlier candidate in Note 2346 used a `0xC0` frame and differed from retail
for constructed owner/stack overlaps. Eliminating a redundant scalar and
reusing the owner parameter after its final owner read yields the retail
`0xB8` frame and the original descriptor, payload and saved-return addresses.
Both independent padders reproduce the complete retail instructions and
relocation bindings. Nine other functions and the constant pools remain
unchanged in each owner.

Tools commit `d9f89d0` provides the qualification packet:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_random_paired_constructor_match -v
```

All eight checks passed with mounted tools and staged sibling dependencies,
before and after installation. Per function, the guest checks include 20
ordinary cases against an independent descriptor model, 452 stack-overlap
cases, 48 cases through the original dispatch window, 48 connected to both
original RNG bodies, and 48 through the original RNG/factory/copy chain. The
latter visits 125 of 145 instructions in the connected helpers. Native 32-bit
builds at `-O0`, `-O2` and `-O3` each pass 16 cases with UBSan and six
effective negative controls. Twelve GNU links per function exercise three
independent symbol bases.

For each function, 912 modeled access cuts agree on public memory and helper
calls; the retail and padded programs additionally agree on full modeled
memory and access traces. The unguarded compiler body differs in private
frame state at 396 cuts because of instruction scheduling. These modeled
fault prefixes do not establish portable C fault semantics, hardware or
gameplay behavior.

The actual Make build matches the independent shadow ELF, binary and owner
objects. The strict image audit accounts for all **1,720** changed bytes with
zero exclusions; only the two target function bodies changed, all **6,050**
function addresses stayed fixed, and all **189,088** protected Game-data
bytes were unchanged. The remaining 1,452 linked objects and the conversion
rows were preserved. A fresh linked recount reports Game **3,736 / 4,842
(77.16%)**, total **4,409 / 5,515 (79.95%)**, zero drift and **138** more
Game matches needed to reach 80%.

Next inspect the related `func_150C6460` and `func_150C6D90` routines. Their
retail bodies have 163 words each and similar structure; their descriptors,
ABI and callers still require qualification.

The scoped Graphify refresh retained or relocated all 59,955 previous nodes,
with 59,959 afterward and no out-of-scope changes. It retained 31,816 nodes
fail-closed; it was not a full-corpus extraction.
