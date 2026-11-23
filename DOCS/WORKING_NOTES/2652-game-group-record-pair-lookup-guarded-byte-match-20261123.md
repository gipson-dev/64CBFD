# 2652 - Group record pair lookup guarded byte match

Date: 2026-11-23. The 85% total matching goal remains active.

`func_15022024` is installed as a complete semantic C lookup and matches
all **91 retail words / 364 bytes / frame 16** through a closed, checked
allocation and control-flow normalization. It replaces the zero-return stub
in `conker/src/game/generated_49D30.c`. The original remains at
`conker/asm/49D30.s:6044`, VA `15022024..15022190`, ROM `4F4D4..4F640`.

Fresh production recount: **4,632 / 5,528 (83.79%) total**, Game
**3,959 / 4,855 (81.54%)**, Init **492 / 492**, Debugger **181 / 181**,
zero drift, **896 different**. **67 more matches** reach at least 85% at
this denominator. Conversion rows and the denominator do not change: the
previous stub already counted as C. This checkpoint earns one exact match.

## Recovered interface and behavior

```c
s32 func_15022024(f32 *first, f32 *second, s32 actorIndex, s32 group);
```

The routine requires `D_800C35EA[group] == 1`, reads the unsigned byte
count from `D_800C363A`, scans active u16 entries through `D_800C35C8`,
and matches each eight-byte tag's type 2 and actor unique-ID byte. The
actor stride is 0x32C and unique ID is at +0x3B. The first match selects
a 0x44-byte record through `D_800C3958`; optional floats +0x3C and +0x40
fill the second and first output pairs respectively. A matched record
returns 1 even if both optional values are the sentinel; no match returns
0 and leaves outputs untouched.

The C retains retail's alias-sensitive access order: cache the sentinel
bits `C61C3C00` before clearing first[1], second[1], first[0], second[0];
reload each output's first float before duplicating it; reload the global
record pointer only after the first optional field's stores. That final
pointer-table read has a narrow volatile view. Shared global declarations
and the compiler profile stay fixed. The literal caller at `1503B204`
passes output pairs at caller SP+0xD0/SP+0xC8, actor from SP+0x40 and group
zero; its real 15-word window verifies the bypass and boolean-result flags.
The complete large caller is not claimed recovered.

## Derived normalization, separate from raw compiler output

The actual owner profile is `-O2 -g3 -Wo,-loopunroll,0`. Raw C emits
**87 words / frame 8 / 90 raw word differences**, not a direct byte match.
The normalizer preserves all **79 core operations** and their relocation
bindings, using explicit operand roles for separate live intervals.

- Allocate the two output pointers to S1/S2, add their two saves, two copies
  and two restores, and extend/release the real frame from 8 to 16.
- Fold the two-word zero-count early return into the shared zero exit and
  invert/retarget the count guard. Six additions minus two omissions give
  the four-word extent difference.
- Move the active-table LW after two independent address-low calculations.
- Translate the loop index/count/cursor, tag/record and temporary GPR roles,
  plus zero/sentinel/value FPR roles, without changing public access order.

The symbolic decoder fails on unknown instructions. It compares all three
entry paths and ten one-iteration paths with fresh symbolic public reads,
32-bit modular address expressions, ordered writes, return values and o32
saved registers. Equal loop-carried roles establish induction from index 0
through termination. Twelve effective source-register mutations reject.
Public aliasing is covered outside the function's private frame; FP equality
is symmetric and uninterpreted, without an FCSR/trap claim.

`87` expected-word/binding rows encode this derived result; every input
word is guarded, including unchanged words. Both padders produce all 91
original words and bindings. Every one of the 87 changed-word controls and
all 14 changed-binding controls reject through both padders: **202** actual
rejections. Both reject this guarded body when oversized; the generic
padder's insertion/trampoline rejection is recorded rather than described
as an ordinary unguarded overflow pass. Four independent global/code
arrangements give **12 GNU links**, including HI16/LO16 carry cases.

Original word 81 (`15022168`) is unreachable from normal entry and remains
present in the exact body. The earlier inventory-only result in Note 2651
is superseded for this function by these completed proofs and adoption gates.
`func_15195AA8` remains private/uncredited; no pair-lookup proof applies to it.

## Fresh focused checks

The versioned packet and helpers are
`tools/experiments/game_group_record_pairs_15022024_{match,manifest,objects,make,image,qualification}`
and `tools/tests/game_group_record_pairs_15022024_{normalizer,symbolic,guest,native}`.
Run under WSL from the decomp root:

```sh
python3 -m unittest tools.tests.test_game_group_record_pairs_15022024_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

| Tools phase | Elapsed | Tests |
| --- | ---: | --- |
| preinstall-primary | 90.403s | 4 fresh / 0 reused |
| preinstall-sibling | 97.124s | 4 fresh / 0 reused |
| installed-primary | 89.024s | 4 fresh / 0 reused |
| installed-sibling | 87.305s | 4 fresh / 0 reused |

Each fresh suite verifies 728 guest cases per raw/generic/generated/retail
stream, including count 255 and actor 25; 170 actual caller windows; 206
full-state, dispatched-word and access fault prefixes; and 524 valid SDK32
native cases at each O0/O2/O3 with UBSan and strict aliasing. Five semantic
controls cover gate, tag type, record field, return and uncached sentinel.
The sentinel-region and cross-record aliases are guest-only; 204 cases are
excluded from the portable native vectors. All 90 reachable retail words
execute. No arbitrary-pointer, FCSR/hardware or gameplay acceptance is claimed.

The second tools run uses a disposable overlay of 1,677 files: 349 identical
sibling files, 1,316 explicit primary fallbacks, 11 task files and one
bootstrap. This is not a standalone-clean-sibling claim. The real sibling
HEAD, dirty state and dependency hashes are unchanged. `make tools-check`
passes. Codex is the only writer; Claude calls: zero.

## Strict production/image boundary

Both full-owner padders and the real Make recipe match the same complete
object, preserving all 56 neighbors, pools and diagnostic sets. A separate
reference compiles frozen before-C with frozen before-guards, reproduces
the original whole owner, then substitutes only independent original ASM.
The entire actual linked ELF equals the baseline plus that target and its
size update, with closed named-symbol/string ordering reconstruction:
**277 changed bytes, zero exclusions**. The protected 189,088-byte Game data
region and all 720 data owners remain exact. All 3,014 frozen production
and workflow inputs are audited against the explicit change plan.

```text
before ELF: 370aca4f81e5197454282894dae2680d22f39bb10b442396fab8277cec9c5927
after ELF:  1ad1e388f0d80ae610987531978597e680975ba404688cd144d5166485448fd2
owner:      4b8b72727f876fbdc89cc7c9429dd47f972526a9897d515c86903cd44651096f
```

The production Make build retains the known duplicate generated_12D630
recipe warning. No shared Makefile/profile, header, layout or historical
guard bytes change. The 87 rows are an exact append to the prior CSV.
Root README changes only the two aggregate matching rows; detailed recovery
history stays here and in concise documentation indexes.

The existing `64CBFDOGL` scene configurations were audited. They consume a
binary artifact, not this C owner; the selected scene still lists this
function as a stub. No applicable direct C consumer or complete host build
root exists at that path. No host edits, binary refresh, Release action or
runtime acceptance is claimed. Tools are committed first, then the consumer
pin/source/guards/docs. Nothing is pushed. Graphify refresh retains every
prior node ID and qualification, and marks the actual C definition installed
and guarded-exact after observed post-commit producers finish; a fail-closed
scoped refresh is not called a full-corpus extraction.

Continue with the banked `func_15195AA8` recovery: prove its removed incoming
argument lifetime and closed normalization before any install or matching
credit. Its 147/150-word mismatch and 96-byte frame are retained in Note 2651.
