# Paired float approach direct match

Date: 2026-11-10. `func_1505A250` replaces its empty C placeholder with all
**86 words / 344 bytes**, directly emitted by the existing compiler profile.
The original **0x10 frame** and two global relocations match without guards,
source padding, profile changes, or declaration changes.

Fresh production recount: **4,313 / 5,513 (78.23%)** total; Game **3,640 /
4,840 (75.21%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,200** different. **98 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion rows and converted-function/byte totals stay fixed.

Baseline consumer `9c4b0f938e16190a680d42de24e5294c75932a5d`; baseline tools
`b3eeee9fab7b7ce5621d4c20dbe69f244340e1bc`, from
[Note 2243](2243-game-recursive-actor-state-dispatch-guarded-match-20261110.md).
Eight qualification files are banked first in tools commit `f730e20b4fd3715f6bdf552f10e1c306f6afbbae`.
Local commits only.

## Recovered source and arithmetic

Owner `conker/src/game_83300.c`; original assembly retained at
`asm/nonmatchings/game_83300/func_1505A250.s`. Retail span: VA
**0x1505A250..0x1505A3A8**, ROM **0x87700..0x87858**. The linked placeholder
was 24 bytes and had 72 differing words across its retail slot. The existing
five-argument declaration already describes the recovered interface:

```c
void func_1505A250(f32 target_x, f32 target_z, f32 rate, f32 *x, f32 *z);
```

Snapshot both coordinate deltas. Return when both compare equal to zero.
Compute the single-precision vector length, scale the rate by `D_800D1550[0]`,
then derive each absolute normalized component step. Update the first output
in its original direction and clamp overshoot to its target. Update and clamp
the second output afterward, using its **live** value. The initial first value
is reused by the emitted code; the second pointer is reloaded after the first
store. This matters when outputs alias each other or the timestep global.

The first complete semantic source already emits the entire retail body.
Five descriptive float locals preserve the original operation order and
rounding. Moving the timestep multiplication ahead of the distance calculation
produces 88 words and 74 differences; reject that alternate schedule. No new
volatile declaration, dummy local, opaque word block, or normalization guard.

Raw target SHA256:
`8e12fbdcf9b2df5b3d7ab2bbdf679bfd309c69f8ecb416f6d05ea242b48d3782`.
Relocations at offsets **76 / 80** are the exact HI16/LO16 pair for
`D_800D1550`. All **88 non-target owner functions**, raw/padded relocations,
constant pools and register information remain equal. Eight inherited owner
diagnostics stay fixed. No header or other source owner is changed.

## Functional checks

- **1,479 guest cases per body / 2,958 executions** agree on complete memory,
  GPR/FPU state and instruction memory-access traces. Cover signed zeros,
  subnormals, overflowing norms, infinities, quiet NaNs, signs, clamp boundaries,
  ordinary outputs, shared outputs and output/timestep aliases. All **85
  reachable words** execute. Static control-flow analysis proves word **75**
  unreachable from entry; direct C still reproduces that redundant load.
- **1,443 native SDK32 cases at O0/O2/O3**, with strict aliasing and UBSan
  enabled: **4,329 total runs**, with **63,492 exact canonical output bytes
  per profile**.
  Finite and signed-zero bits agree. NaNs compare by class in the independent
  reference/native outputs. The guest raw/retail pairs compare all bits.
  Thirty-six physical argument-home alias cases remain guest-only.
- **17 effective compiled semantic controls** finish normally with observable
  output differences. Zero execution errors count as witnesses. Controls reject
  wrong deltas, the early-return conjunction, missing timestep/length/square
  root/normalization/absolute value, incorrect clamp/direction, cached second
  output, reversed stores, late timestep reload and a zero-rate shortcut.
  The latter is invalid for an underflowed norm, which can still produce NaNs.
- Raw, generic-padder, generated-padder and original-assembly target payloads
  and relocations agree. **88 word/binding corruptions** are rejected. **48
  executions across four independent symbol sets** cover low halves 0, 0x7FFC,
  0x8000 and 0xFFFC. **89 exact instruction-access cut pairs** preserve complete
  guest prefix state, including physical incoming-rate-home aliases.

These instruction models and native runs do not establish FCSR behavior,
signaling-NaN exceptions, portable C fault semantics, hardware execution or
live gameplay acceptance.

## All original direct caller windows

The aligned retail census finds **nine JAL sites**, no direct J, and no aligned
literal target pointer. Computed indirect calls are not excluded. The one
visible C call is in **`func_15059140`**, passing zero targets, its local rate,
and actor fields 0x164/0x168. Original argument setup uses F12/F14, A2/A3 and
the outgoing fifth-argument stack slot.

| Original parent | Window start..end, exclusive | Words |
| --- | --- | ---: |
| `func_150511E8` | 0x15051514..0x15051544 | 12 |
| `func_15051558` | 0x15051BD0..0x15051BF4 | 9 |
| `func_15051558` | 0x1505205C..0x150520E0 | 33 |
| `func_15056B08` | 0x1505823C..0x15058298 | 23 |
| `func_15059140` | 0x150592F4..0x15059324 | 12 |
| `func_150642AC` | 0x15064728..0x15064758 | 12 |
| `func_150C3574` | 0x150C35B0..0x150C35D0 | 8 |
| `func_150D942C` | 0x150D974C..0x150D97A8 | 23 |
| `func_150D942C` | 0x150D97EC..0x150D9848 | 23 |

Execute **162 cases per window / 2,916 executions / 1,458 complete state and
trace pairs**, covering all **155 window words**. Real branches, delay slots,
loads and float arithmetic feed the actual leaf body. Caller constants come
from the retained exact protected data. Inputs before each window are staged;
the complete parent algorithms remain unqualified.

## Actual Make and strict complete-image accounting

Freeze **2,194 input fingerprints** and retain exact mutable baseline files.
Five actual owner Make commands plus independent before/proposed compiles
reproduce the same raw/padded owner. Force the affected production owner,
link, emit the binary, regenerate progress and recount the actual ELF.
Every other fingerprinted input remains fixed.

Predict the entire ELF by replacing only the 344-byte target slot and updating
its symbol size **24 -> 344**. Exactly **211 bytes** change. There are no
metadata permutations and **zero exclusions**. Eight independent image
corruptions are rejected, including a dead target word, adjacent matched code,
protected data, symbol value/size/string and ELF header.

All **6,050 function addresses** remain fixed; only the target canonical body
changes. All **189,088 protected bytes / 720 data owners** remain exact,
SHA256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The conversion CSV, layout, headers, Makefile and complete guard manifest stay
byte-identical. Production completes in **194.43 seconds**. The existing
duplicate `generated_12D630` recipe warnings and expected full-ROM checksum
exit 2 remain; the owner, predicted binary, strict image and recount gates pass.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `7437f806f96c5f0beb77576a2a66a20df6daf3bc4e956c298d5a63c0bafecf57` |
| Built binary | `8e2a682f6b21fe3a79ebc599fa6708788d4eaf85f413c74e279facbe6f477eed` |
| Padded owner | `ea9baa64f1e7e3e7db5332589fb944b1187eef7d5b38dc0f04f1cfd456c92dde` |
| Guard manifest | `8d37e5d6a36e45fb20dceb5982c01f960ab1a6e71409ed501d009e45f45ec45e` |

## Tool copies, graph and next target

All **eight preinstall checks pass freshly per tools environment**: mounted
143.68 s, sibling 131.91 s. After adoption,
**two fresh installed checks per environment** requalify actual Make/full image
and complete guest behavior: mounted 77.76 s, sibling
80.75 s. Six other checks are explicit preinstall reuses,
with every tool and imported dependency fingerprint revalidated. Fresh shared
smoke checks pass; three unchanged pure-helper regression receipts per
environment are reused separately.

The sibling uses a private overlay for the eight new files. Explicit read-only
mounted fallbacks supply missing `diagnostic_rows`, `bound_blob` and
`reachable` helpers. Consumer Make invokes mounted CLI tools; independent
in-process padder checks use sibling helpers. Its **2,434 pre-existing dirty
paths** are preserved. Codex is the only writer; **zero Claude calls** are used.
No host-port source, saves or frozen Release artifact is touched.

The scoped code graph has **59,673 nodes / 113,059 links**.
All **59,673 old nodes** are retained or relocated, and definitions
outside changed paths remain equal apart from community metadata. Verify all
71 target-owner C positions and retain its 18 assembly pragmas. The eight new
tools still have **0 indexed nodes** under current submodule filters;
historical excluded nodes remain retained. This is a scoped refresh with a
recorded coverage gap. Private post-commit receipts also audit documentation
heading relocations.

Reproduce in the prepared consumer root under WSL PSBBN:

```sh
python3 -m unittest tools.tests.test_game_paired_float_approach_1505a250_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

The suite requires exact retained pre-adoption mutable inputs in
`conker/build/game-paired-float-approach-1505A250-match/frozen/`. No ROM or ELF
binary is committed; a clean clone without those inputs is not claimed to
reproduce the workspace image.

Next: investigate **`func_1505DDA8`**, 90 words/frame 0x70, in the
same owner. Its 12-byte zero-return placeholder still differs at
87 retail slot words and remains untouched/uncredited. The initial
assembly reading suggests active-slot search using scaled distance and a
wrapped heading interval. Verify its actor/u16/float ABI, original callers,
`func_1505DF10` result/output types, helper effects and loop bounds before
implementing or assigning any matching credit. Keep the wider 80% goal active.
