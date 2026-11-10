# Actor-slot sector search direct match

Date: 2026-11-10. `func_1505DDA8` replaces its zero-return placeholder with
the complete **90-word / 360-byte** active-slot search. All words, the original
**0x70 frame**, saved-register lifetimes and seven relocation sites match
directly from C under the unchanged compiler profile. **No guards** are added.

Fresh production recount: **4,314 / 5,513 (78.25%)** total; Game **3,641 /
4,840 (75.23%)**; Init **492/492**; Debugger **181/181**. Zero address drift,
**1,199** different. **97 more** accepted matches reach 4,411/5,513 and the
active 80% goal. Conversion rows and converted-function/byte totals stay fixed.

Baseline consumer `8aa94f7b2cabad2d83753669d8e19d12a7521306`; baseline tools
`f730e20b4fd3715f6bdf552f10e1c306f6afbbae`, from
[Note 2244](2244-game-paired-float-approach-direct-match-20261110.md).
Eight qualification files are banked first in tools commit `12448af5469002ba3d942c4f68ddb65db6d8838c`.
Local commits only.

## Source, types and loop behavior

Owner `conker/src/game_83300.c`; original assembly retained in
`asm/nonmatchings/game_83300/func_1505DDA8.s`. Retail span: VA
**0x1505DDA8..0x1505DF10**, ROM **0x8B258..0x8B3C0**. The 12-byte placeholder
had 87 differing words across its retail slot. Recover consistent local types:

```c
s8 func_1505DDA8(struct127 *actor, u8 unused, u16 angle_range, f32 scale);
f32 func_1505DF10(struct127 *, u8, u16 *, f32 *, f32 *, s32);
```

Scan unsigned-byte slot indices from zero through the inclusive signed global
last-slot index `D_80082FA0`. Skip table entries whose complete interaction-state
word is zero. Any nonzero state, including negative values, is active. The
table stride is 0x32C and the actual declared table contains 26 entries.

For each active slot, snapshot `actor->xz_velocity * scale * 0.5f` before the
helper. The helper returns squared 3D distance in F0 and writes heading,
horizontal squared distance and vertical delta through three typed pointers.
When distance is strictly below squared radius, read the actor's **live**
moving angle, wrap its difference plus half the unsigned range to u16, and
require it to be strictly below the range. Return the slot sign-extended from
s8, or -1 after exhaustion. The incoming second argument is unused in retail;
do not add an exclusion for that slot value.

The initial nested-if source emits 92 words/frame 0x78. Declaring the u8 index
first restores frame 0x70 but still emits 92 words. An explicit `continue` for
inactive entries recovers all 90 words: the compiler retains the loaded limit
on that path and reloads it after an active helper/failed selection. Named
locals remain meaningful; no extra lexical block, padding local, volatile
declaration, opaque instruction block or normalization guard is needed.

The recovered helper declaration agrees with its original **51-word assembly**,
which remains intact and receives no C-conversion credit. F0 is a float return;
the three output pointers are heading u16, horizontal distance f32 and height
delta f32. Both original call sites supply the unused sixth word as zero.
No C caller outside this owner uses either repaired declaration.

Raw target SHA256:
`2cf85beab984bd928109f18e69537a656b5abee363fc8f83e79973b972cfc2e8`.
Relocations: HI16/LO16 `D_80082FA0` at offsets **72/76 and 272/276**,
HI16/LO16 `D_800CC2D0` at **96/104**, and R_MIPS_26 `func_1505DF10` at **180**.
All **88 non-target owner functions**, raw/padded relocations, constant pools
and register information remain equal. Eight inherited owner diagnostics stay
fixed. No shared header, other owner, Makefile or compiler option is changed.

## Functional and instruction qualification

- **886 guest cases per body / 1,772 executions** agree on complete memory,
  GPR/FPU state, calls and instruction memory-access traces. Cover empty/negative
  limits, first/last slots, full nonzero state words, wrapped heading edges,
  strict radius boundaries, signed zeros, subnormals, overflow, infinities and
  quiet NaNs. Helper effects change actor heading/speed, the global limit and
  later active slots. Actor/table aliases and physical incoming-home changes
  verify snapshot versus live behavior.
- **846 native SDK32 cases at O0/O2/O3**, strict aliasing and UBSan enabled:
  **2,538 total runs**, with **817,492 exact public-state/call bytes per
  profile**. Use the real struct layout and 26-slot table. Forty extended-table,
  wrap or physical argument-home cases remain guest-only. The wrap fixture
  terminates through a helper limit change after 260 calls; the original u8
  loop can otherwise cycle at a limit of 255 without a match.
- All **88 reachable words** execute. Words **58/59** are the compiler's
  unreachable negative-division correction. Word 6 masks the width into saved
  S2; word 54 copies it to V0; the intervening code does not redefine S2 and
  the helper preserves it under O32. Word 56's nonnegative branch is therefore
  always taken. A CFG-only reduction proves the two dead words; production C
  still emits both literally.
- **17 effective compiled semantic controls** finish normally and produce
  observable disagreements. Cover loop bounds/start, active-state gates,
  radius factor/scale, strict distance/sector edges, signed wrapping, heading
  field, half-range offset, signed result, index width, unused-slot exclusion,
  and cached heading/speed/limit. Longer mutants execute at a private rebased
  entry to avoid overlapping the adjacent real helper; no execution error
  counts as a semantic witness.
- Raw, generic-padder, generated-padder and original-assembly payloads and
  bindings agree. **97 word/binding corruptions** are rejected. **48 executions
  across four independent symbol sets** cover low halves 0, 0x7FFC, 0x8000 and
  0xFFFC. **216 exact instruction-access cut pairs** preserve complete guest
  prefix state, including helper effects and argument homes.

These model/native checks do not establish FCSR behavior, signaling-NaN
exceptions, portable C fault semantics, hardware or live gameplay acceptance.

## Original callers and real helper integration

The complete aligned retail code-image census finds one JAL to the target and
two to its helper, with no direct J or aligned literal pointers to either.
Computed indirect calls remain unexcluded.

| Parent / callee | Original JAL | Qualified setup/continuation window | Words |
| --- | --- | --- | ---: |
| `func_150538CC` / target | 0x15054100 | 0x150540F4..0x15054114 | 8 |
| `func_1505DADC` / helper | 0x1505DC10 | 0x1505DBF8..0x1505DC28 | 12 |
| Target / helper | 0x1505DE5C | 0x1505DE38..0x1505DE7C | 17 |

The first caller supplies actor+0x124 as the unused byte, range **0x200** and
scale **15.0f**, then compares the signed result with -1. Its branch-taken
continuation at 0x1505415C is also recorded. The target/helper setup includes
the original radius calculation and both outgoing stack arguments.

Execute **648 cases in each connected target/caller mode / 2,592 executions /
1,296 complete state-and-trace pairs**. Connect the actual 51-word helper and
cover every helper word. Its heading provider `func_1505A630` is an explicit
opaque fixture that clobbers caller-saved registers and can change actor
coordinates/angle. The helper's snapshotted deltas, three stores and float
return agree with an independent arithmetic model. Another **216 executions**
cover both original helper caller windows. All **37 window words** execute.
Inputs outside the windows are staged; complete parent algorithms and the
heading provider's actual algorithm remain unqualified.

## Complete image, tool copies and next target

Freeze **2,205 input fingerprints**, retaining the exact mutable baseline.
Five actual owner Make commands and independent before/proposed compiles agree.
Production forces the affected owner, links, emits the binary and recounts the
actual ELF. Predict the entire image by replacing only the 360-byte target and
updating its symbol size **12 -> 360**: exactly **282 changed bytes**, no
metadata permutations and **zero exclusions**. Eight independent image
corruptions are rejected, including a dead target word and adjacent helper.

All **6,050 function addresses** remain fixed. All **189,088 protected bytes /
720 data owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Conversion CSV, layout and the complete guard manifest stay byte-identical.
Production completes in **63.54 seconds**. Existing duplicate
`generated_12D630` recipe warnings and the expected whole-ROM checksum exit 2
remain; the owner, predicted binary, strict image and recount gates pass.

| Artifact | SHA256 |
| --- | --- |
| Production ELF | `a424a1f821f7c979e36a77c51dbe231346edfa1c1f48e78181beea6ad3cd98e5` |
| Built binary | `c09a4b03e52bf228475e2dc519b5cfbe72a948940f47ef707edced11e30a04a9` |
| Padded owner | `4a809ece5be0c6c9e816e9244c10cc1dba33594008358ab1a70c8e7e71f9f6ba` |
| Guard manifest | `8d37e5d6a36e45fb20dceb5982c01f960ab1a6e71409ed501d009e45f45ec45e` |

Eight fresh preinstall checks per tools environment pass: mounted
**144.71 s**, sibling **128.96 s**. Two fresh
installed checks per environment requalify actual Make/full image and complete
guest behavior: mounted **44.62 s**, sibling
**30.98 s**. Six other checks are explicit preinstall reuses,
with every tool/imported dependency fingerprint revalidated. Fresh shared
smoke checks pass; three unchanged pure-helper regression receipts per
environment are reused separately.

The sibling uses a private overlay for eight new files. Explicit read-only
mounted fallbacks provide missing diagnostic/binding/CFG helpers and the prior
float-instruction oracle. Consumer Make invokes mounted CLI tools; independent
in-process padder checks use sibling helpers. Its **2,434 pre-existing dirty
paths** are preserved. Codex is the only writer; **zero Claude calls** are used.
No host-port source, saves or frozen Release artifact is touched.

The scoped code graph has **59,680 nodes / 113,069 links**.
All **59,680 old nodes** are retained or relocated; definitions outside
changed paths remain equal apart from community metadata. Verify 71 owner C
positions and retain 18 assembly pragmas. The new tools have
**0 indexed nodes** under existing submodule filters. Historical
excluded nodes remain retained; this is a scoped refresh with a recorded
coverage gap. Private post-commit receipts also audit heading relocations.

Reproduce in the prepared consumer root under WSL PSBBN:

```sh
python3 -m unittest tools.tests.test_game_slot_sector_search_1505dda8_match -v
python3 tools/match_progress.py conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

The suite requires exact retained pre-adoption mutable inputs in
`conker/build/game-slot-sector-search-1505DDA8-match/frozen/`. No ROM or ELF
binary is committed; a clean clone without those inputs is not claimed to
reproduce the workspace image.

Next: investigate **`func_15060BE0`**, 93 words/frame 0x18, in the
same owner. Its 12-byte zero-return placeholder still differs at
80 retail words and remains untouched/uncredited. Initial assembly
reading suggests an actor anchor-coordinate updater: a metadata-selected
0x40-byte transform, scaled normalized vector, truncated halfword outputs and
actor-position fallback. Verify types, caller interface, alias/access order and
valid versus invalid float-conversion domains before implementation. Keep the
wider 80% goal active.
