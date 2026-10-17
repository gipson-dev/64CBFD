# Dual Fade Native Caller-Save Selection

Date: 2026-10-17

Continue consumer **81132e68**, tools **0a0712a**, from
[Note 1491](1491-dual-fade-argument-home-and-allocation-trace-20261017.md).
Target **func_150D01A0**, VA **150D01A0..150D02B4**, ROM **FD650..FD764**,
**69 retail words / frame0x30**. The addressed candidate is still **68 words**,
with **61 full-slot word differences**, wrong S0/RA/state homes, and no
installation, new guards or matching credit. This checkpoint explains its
remaining caller-save decision; it does not change the candidate or production.

## Native Evidence

Use the existing fingerprint-locked owned UOPT driver and full normal-object
comparison. The new adapter adds read-only native breakpoints to the prepared
compiler only, with finish breakpoints for cupcosts and globalcolor. Remove
all four new address breakpoints before the driver continues into UGEN/AS1.
Both complete drivers exit successfully and preserve all emitted text,
function, relocation and pool inventories against their normal compiles.

The earlier real-number diagnostic printer remains suppressed. **No printed
numeric cost or timing is evidence.** Instead, read the actual IEEE-754 words
from the compiler's return storage and native XMM compare operands, then read
the flags immediately after the real COMISS instruction at **0x481500**.
The next JA tests **CF=0 and ZF=0**. Record final colors independently at
globalcolor return and cross-check them with the procedure-scoped mode5 table.

| Source / role | Caller-cost bits | Callee base bits | Compared S0 cost bits | Best bits | Post-COMISS CF/ZF/PF | Final color |
| --- | --- | --- | --- | --- | --- | ---: |
| Addressed / old weight | 0x40000000 (2) | 0 | 0x40800000 (4) | 0x40000000 (2) | 1/0/0 | 8, actual T1 |
| Normal / old weight | 0x40000000 (2) | 0 | Not compared: color14 forbidden | N/A | N/A | 8, actual T1 |
| Normal / record control | 0x60AD78EC | 0x3DCCCCCD | 0x40833333 | 0x60AD78EC | 0/0/0 | 14, actual S0 |

The first-use penalty is **0x40800000 (4)** with **13 static nodes** in both
fixed source forms. Caller probes include internal registers2 and13; callee
probe uses14. These are fixed-capture internal colors, not a universal hardware
mapping. The addressed weight really reaches the S0 comparison but loses it:
the candidate's caller-save cost2 is less than the first-use S0 cost4. The
normal record positively exercises the opposite decision and emits S0.

Match each native variable by its complete IChain header, table/chain identity,
procedure, storage and offset, then join subsequent cost/compare/final events
by its actual live-range pointer. Weight is **373|0 / expression0 / M-12**;
record is **1589|0 / expression8 / P0**, both procedure882. Independently
check the same identities, final colors and color14 availability in mode5.

The prepared **5.3** binary's native location word has **16/8/8-bit**
block/storage/level fields. Do not copy the different 21/3/8-bit layout in
the [upstream reference header](https://github.com/n64decomp/ido/blob/master/src/uopt/uoptdata.h).
An initial ignored scratch probe used that wrong block shift and fired no
target events; it established no absence claim. Correct the native layout and
require all exact events. The [upstream allocator](https://github.com/n64decomp/ido/blob/master/src/uopt/uoptreg2.c)
helps locate cupcosts, first-use penalties and selection comparisons, but is
reference material, not proof of this binary's offsets or original game flags.

## Qualification And Bank

Three focused tests pass in **20.913s**, no skips. They run two fresh owned
drivers, require the normal65/addressed68 raw fingerprints, real opposite
selection controls, and complete code identity. **162 effective negative
controls** reject missing/duplicate events, wrong identities, costs, flags,
registers, boundaries and absent gates. Compiler identity and source-label
checks reject unsupported probes before launch. An initial qualification run
caught a transcription error in the record control's raw best-cost constant;
correct it to the captured **0x60AD78EC**, without removing a gate or case.

All **210 protected entries / 193 paths** retain their live/frozen fingerprints.
Reuse Note1491's unchanged ten-test public/native/caller/helper/rebase receipts
explicitly; this turn does not claim fresh execution of those corpora or full
private/fault/gameplay parity. No semantic source or compiler-profile sweep.

Tools **59d8398** banks the adapter and tests first. Twelve shared checks pass
in the active checkout (one progress, six word-patch, five PC16); the mirror's
six word-patch and five PC16 checks pass. Tools-check and four ASCII/AST parses
pass; both new task-file pairs are exact. Preserve standalone mirror HEAD
**ddbdd16b** and all **1,080 initial dirty hashes**, now **1,082 dirty paths**.
No mirror commit/reset, push, Claude call, dependency/provider/account change,
host-port operation or frozen Release action.

Fresh official matching remains **Game2,953/4,828 (61.16%)**, total
**3,626/5,501 (65.92%)**, **1,875 different**, zero address drift. Init492/492
and Debugger181/181 remain exact. The existing duplicate generated_12D630
recipe warning is unchanged. Production C, guard CSV, Makefile, normal ELF,
progress CSV and root README retain their fingerprints; no aggregate edits.

## Next

- [x] Observe old-weight caller/callee costs, actual comparison flags and final
  colors, with opposite-direction positive control and unchanged full code.
- [ ] Recover the source's block/live-unit topology or establish a supported
  original compiler-profile difference that explains retail's S0 selection.
  Availability, source register hints and equal word counts are insufficient;
  do not lower the compiler penalty or force its registers to manufacture a fit.
- [ ] Recover S0, RA and state homes; close complete private/helper/fault and
  immutable linked-image gates before installation. Wider Game matching stays open.

```sh
python3 -m tools.experiments.game_dual_fade_allocation_choice --source home
python3 -m unittest tools.tests.test_game_dual_fade_allocation_choice -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
