# White Text Fade Candidate And Private Lifetime Gap

Date: 2026-10-17

Continue consumer **1d05536c**, tools **b3020e9**, after
[Note1494](1494-text-reveal-renderer-direct-restoration-and-match-20261017.md).
Investigate **func_150D0534**, VA **150D0534..150D0650**, ROM
**FD9E4..FDB00**: **70 body words plus one trailing slot nop**. The complete
addressed semantic candidate is **69 words / frame0x30**, with **62 full-slot
word differences**. It is **not installed** and earns no matching credit.
Tools **017c9c4** banks the new experiment and eight qualification tests first.

## Recovered Public Contract

Read the payload pointer at record0x48. Reset its signed byte to20 when
record0x30 bit0 is set. For a positive count, compute the old-buffer weight
as **count *12 modulo256**, current weight as255 minus that byte, then
subtract **D_800BE9E4** from the countdown with the original byte wrap.
Negative/zero counts leave the payload unchanged and draw only the current
buffer at full opacity. Count64 is a useful positive-count/zero-old-weight
case. The current weight cannot become zero from this multiplier, but the
original retains the conditional branch.

Draw each nonzero-weight buffer using white **255,255,255,weight**, position
**20,20**, flags **128**, and the selected index or index XOR1. Retain the
index/pointer reads after the relevant helper calls. Return1, so the actual
dispatcher keeps its cursor and clears the reset flag. This is callback
table slot2 at **D_800888A0+8**, unlike the earlier fade's slot0.

The real addressed parameter form, `*(u8 **)&record`, retains the retail
incoming record home at **SP+0x30**. Do not add a padding automatic or force
a physical register. Raw SHA-256:
`29756ae705f6061063b52afccdde45adc69960fae2844f6c6f99d6d723ad50be`.
Six relocation sites: one clock HI16/LO16 pair and four color/text calls.
Raw and actual padded slot bytes agree. All24 other raw/padded owner
functions and all constant/data pools remain unchanged.

## Unresolved Private Contract

Retail retains old weight in **S0**, saves S0 at **SP+0x18**, RA at
**SP+0x1C**, and state at **SP+0x20**. The addressed candidate spills old
weight at **SP+0x24**, saves RA at **SP+0x14**, and state at **SP+0x1C**,
without saving S0. Same frame size and the correct parameter home do not
establish the remaining lifetimes.

The actual22-word color setter and42-word variadic wrapper positively expose
different copied private words across **28 cases**, including both stack
phases and reset/non-reset paths. Compare all16 copied words per text call.
The raw/padded candidates agree with one another, and their visible call
arguments agree with retail, but their complete copied payload does not.
The installation gate rejects even retail words supplied without the missing
qualification; a byte list alone is not an acceptance receipt.

Eight source discriminators, without compiler-profile changes:

| Form | Body words | Frame | Measured limitation |
| --- | ---: | ---: | --- |
| Normal parameter | 66 | 0x30 | S0 holds record, not old weight |
| Addressed parameter | 69 | 0x30 | Correct P0 home, wrong old-weight lifetime |
| Staged mask/current byte | 68 | 0x30 | No S0 weight |
| Staged buffer-array accesses | 69 | 0x30 | No S0 weight |
| Explicit branch/staged arrays | 70 | 0x30 | Equal body length,65 slot differences |
| Byte old weight | 69 | 0x30 | No S0 weight |
| Both byte weights | 67 | 0x28 | Wrong frame and lifetime |
| Staged byte old weight | 69 | 0x28 | Wrong frame and lifetime |

The normal form's **move S0,A0** is a positive wrong-role discriminator,
not evidence that retail's S0 contract is recovered. The equal-length form
also remains non-matching. Earlier native allocation costs in Note1492
belong to func_150D01A0; this turn does not measure those costs for the white
fade or claim that the same numeric comparison has been observed here.

## Qualification And Unchanged Baseline

All **eight tests pass in39.443s**, without skips:

- **9,477 three-way public guest/reference cases**, all70 retail body words,
  every initial byte, signed boundaries, reset flags, nine payload aliases,
  full byte indices, three scripted callback mutation modes and two phases.
  The trailing slot nop is not executed.
- The **28 actual-helper private counterexamples** above, using direct
  snapshot reads rather than counted observer pseudo-instructions.
- **Nine independent original/raw/padded links**,180 three-way public cases,
  all six bindings and independent signed-low carry boundaries. Actual-helper
  private rebase parity is not claimed.
- Native32 **O2/O0 + UBSan**,6,144 cases/profile, a separately typed caller,
  and six effective compiled negatives for sign, factor and buffer selection.
  Native stubs do not read missing variadic arguments; guest-only aliases,
  extended indices and actual private wrapper reads are not portable C proof.
- **69 word / six binding /428 live-and-frozen corruptions** protect all
  **214 entries /197 distinct paths**. Replay all eight source discriminators.
- **256 actual35-word dispatcher cases** at slot2 retain the cursor and clear
  the flag, including the disabled `kind == -1` path. Only public caller parity.

Private/fault/full-image installation gates remain open. The unfinished text
consumer and presentation/gameplay are not executed. No new guards, compiler
penalty changes, parameter tricks, assembly rewrites or production body.

Fresh matching remains **Game2,955/4,828 (61.21%)**, total
**3,628/5,501 (65.95%)**, **1,873 different**, zero drift. Production source,
guard manifest, Makefile, layouts, nominal progress and root README retain
their exact fingerprints. The normal ELF remains
`9c99acc828faf468f59ae765bf58c849f1a5d1d0aaa254ed2d1ee09ac05c60f3`.
No new normal build is needed for this experiment-only checkpoint. Reuse
Note1494's unchanged installed reveal/constructor and complete image/data
receipts explicitly; they are not fresh test runs in this turn.

Twelve shared checks in each tools copy, both tool smoke checks, four
ASCII/AST parses and both task-file pairs pass fresh. Preserve every one of
the standalone mirror's **1,090 initial dirty hashes**, its **1,092 dirty
paths**, and HEAD **ddbdd16b**. No overwrite of existing mirror paths, mirror
commit/reset, push, dependency/provider/account change, Claude call, host-port
operation or frozen Release action. Verify the code-only post-commit Graphify
receipt before closing the checkpoint.

## Next

- [x] Recover and qualify the complete white-fade public candidate, real P0
  home, helper/caller/native/rebase boundaries and positive private rejection.
- [ ] Recover S0/RA/state lifetimes and private/fault/full-image gates before
  installing func_150D0534. Keep func_150D01A0's related issue open separately.
- [x] Continue ordinary C recovery at **func_150B9560**, now finished in
  [Note1496](1496-actor-counter-motion-direct-restoration-and-match-20261017.md), owner
  **generated_E5E90**, VA **150B9560..150B95FC**, ROM **E6A10..E6AAC**,
  **39 words**. Its former zero-return placeholder is now replaced with the
  complete counter-gated updates; see Note1496 for literal and normal-image
  qualification.
- [ ] Keep handwritten **func_150A76F0** in the separate assembly/register
  workstream. The fresh census ranks its32-word slot early, but its T4/T9/S6/S7
  inputs and **JR V0** are not an ordinary C ABI. Wider Game stays active.

```sh
python3 -m tools.experiments.game_white_text_fade
python3 -m unittest tools.tests.test_game_white_text_fade -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
