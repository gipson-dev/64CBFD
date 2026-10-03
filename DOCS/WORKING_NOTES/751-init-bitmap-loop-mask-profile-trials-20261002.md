# Init Bitmap Loop, Mask, and Profile Trials

Date: 2026-10-02

## Result

`func_10005BE0` remains in its original assembly owner after a final matrix of
55 shape/profile combinations. None emits its complete nineteen-word retail
body. All eleven source shapes pass 65 host behavior cases, with two calls
per case. These validate candidate behavior for positive counts, not a
production conversion, guest execution, or recovery of original C provenance.

The first pass compiled eight shapes under four profiles. Those 32 combinations
were rerun in the final matrix, so they are not counted as additional distinct
combinations. Two shapes reproduce the earlier loop/mask controls from
[Note 738](738-init-bitmap-leaf-contract-and-compiler-experiment-20261002.md).
The new evidence is the extended loop forms, integer comparison, postdecrement
mask, and profile matrix, including no-unroll behavior.

No production source, shared declarations, assembly ownership, compiler profile,
word guards, README totals, or linked project artifact changed. No full project
build or gameplay test was performed. Diagnostic files remain under ignored
`conker/build/`.

## Source Shapes

The fixture `conker/build/init-bitmap-resume-experiment.c` declares the two
globals as byte pointers and the count as `s16`, as in the isolated prior
experiment. Every shape loads the start and inclusive end once before filling.

| Shape | Fill loop | Final mask when low-three-bit count is nonzero |
| --- | --- | --- |
| 1 | Store, compare `cursor++ != end` | `(2 << (bits - 1)) - 1` |
| 2 | Same loop | `(1 << bits) - 1` |
| 3 | Store, conditional increment and explicit `goto` back edge | Two-based mask |
| 4 | Same explicit back edge | One-based mask |
| 5 | Store through `cursor++`, compare with `end + 1` | Two-based mask |
| 6 | Same one-past-end loop | One-based mask |
| 7 | Initial store, then `while (cursor != end) *++cursor = 0xFF` | Two-based mask |
| 8 | Same initial-store loop | One-based mask |
| 9 | Shape 1 loop | `if (bits--) *end = (2 << bits) - 1` |
| 11 | Shape 1 loop with both compared pointers cast to `unsigned long` | Two-based mask |
| 12 | Same integer-comparison loop | One-based mask |

Shape 10 is not run: it duplicates Shape 9. The integer type in Shapes 11/12
can represent pointers on the tested WSL host and the guest o32 target; this
is not a claim of portability to every host data model.

## Reproduction

Driver: `conker/build/init-bitmap-resume-experiment.py`, run from `conker/`:

```sh
python3 build/init-bitmap-resume-experiment.py
```

Common IDO options are `-c -32 -G 0 -Xfullwarn -Xcpluscomm -signed
-nostdinc -non_shared -Wab,-r4300_mul -mips2 -o32`. The driver compiles
each shape using `-DSHAPE=<number>` with the five profiles below.

Each object is linked independently using `mips-linux-gnu-ld -m elf32btsmip`,
text start/entry `0x10005BE0`, and absolute global definitions:
`D_8003BE70=0x8003BE70`, `D_8003BE7C=0x8003BE7C`, and
`D_8003BE78=0x8003BE78`. `objdump -d -z` output is retained beside each object.
Words through the final return delay slot are compared against ROM bytes
`0x5BE0..0x5C2C`, excluding subsequent object alignment nops.

The host fixture is built from that same source with `cc -O2 -std=c99
-DHOST_TEST -DSHAPE=<number>`. It tests counts 1 through 64 and 32,767,
all eight remainder classes, single-byte and multi-byte ranges, the inclusive
last-byte mask, surrounding-byte preservation in a 4,104-byte buffer, and
repeat calls. All 715 shape/case combinations pass twice. Zero counts,
reversed ranges, global/data aliasing, and execution of guest assembly are
not covered. No defensive early-return behavior was added.

## Measurements

Each cell is **body words / differing word positions**, including missing or
extra body words as differences. This is not an instruction edit distance.
Retail has nineteen words. `No unroll` means `-O2 -g3 -Wo,-loopunroll,0`.

| Shape | `-O2 -g3` | `-O2` | `-O1` | `-g` | No unroll |
| --- | ---: | ---: | ---: | ---: | ---: |
| 1 | 20 / 19 | 20 / 19 | 30 / 30 | 35 / 35 | 20 / 19 |
| 2 | 19 / 16 | 19 / 16 | 29 / 29 | 34 / 34 | 19 / 16 |
| 3 | 20 / 19 | 20 / 19 | 30 / 30 | 37 / 36 | 20 / 19 |
| 4 | 19 / 16 | 19 / 16 | 29 / 29 | 36 / 35 | 19 / 16 |
| 5 | 20 / 19 | 20 / 19 | 31 / 31 | 36 / 36 | 20 / 19 |
| 6 | 19 / 15 | 19 / 15 | 30 / 30 | 35 / 35 | 19 / 15 |
| 7 | 32 / 28 | 32 / 32 | 35 / 35 | 41 / 41 | 21 / 19 |
| 8 | 31 / 27 | 31 / 31 | 34 / 34 | 40 / 40 | 20 / 18 |
| 9 | 22 / 21 | 22 / 21 | 32 / 32 | 36 / 36 | 22 / 21 |
| 11 | 20 / 19 | 20 / 19 | 30 / 30 | 35 / 35 | 20 / 19 |
| 12 | 19 / 16 | 19 / 16 | 29 / 29 | 34 / 34 | 19 / 16 |

The explicit conditional back edge is optimized to the same XOR-temporary
comparison as the postincrement control. Integer pointer comparisons do not
remove it. Shape 6 instead compares the advanced cursor with `end + 1`, but
adds endpoint arithmetic and stores at `-1(cursor)` in the loop branch delay
slot. Its tail uses `1 << bits` and a different mask schedule, rather than
retail's branch-delay decrement followed by `2 << (bits - 1)`.

The initial-store/while form is unrolled under the default optimized profiles.
Disabling unrolling reduces its size but still does not fit the nineteen-word
slot. Postdecrement in the mask condition increases the optimized body to
22 words. None establishes a register-only or independent-scheduling repair;
do not normalize a large fraction of this handwritten loop into retail words
just because some candidate has the right total length.

## Handoff

The two small retained Init candidates have now had renewed bounded trials:
MMIO results are in
[Note 750](750-init-mmio-pointer-lifetime-profile-trials-20261002.md), and
bitmap results are above. Both remain deferred; future experiments need a new
source/compiler/dataflow rationale rather than rerunning these same shapes.
The inventory and production acceptance gates remain in
[Note 749](749-init-remaining-assembly-resume-assessment-20261002.md).

Init stays at 492 C / 47 assembly rows. Retain the proven assembly baseline
and do not extract this unmatched leaf from the shared owner. Ordinary decomp
work can resume at Game `func_15040CC8`, the untouched 38-word callback
dispatcher target. Broader decompressor or nonstandard-register rewrites
remain separate whole-contract work, not missing small C conversions.
