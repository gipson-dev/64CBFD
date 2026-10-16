# Frame Timing Allocation And Signed-Zero Fit Boundary

Date: 2026-10-16. Consumer predecessor **9c646276**, tools predecessor
**511d98a**. The previous turn committed real semantic restoration in
[Note 1450](1450-frame-timing-state-semantic-restoration-20261016.md).
This turn qualifies compiler allocation evidence and rejects false fits.
**No production C, guest image, compiler profile or word guard changes.**
Continue the complete Game matching goal; this is not a byte-exact checkpoint.

## Target And Screens

```text
func_15019F20  VA 0x15019F20..0x1501A220  ROM 0x473D0..0x476D0
Production: 191 body words / frame 0x18 / one trailing NOP
141 actual slot-word differences / zero new guards
```

Thirty-one complete-owner screen outputs include one unchanged extent control.
They test separate byte gates and word divisors, real quotient/accumulator
lifetimes, named history ranges, chained zero stores, residual load types and
later integer-divisor captures. Reuse the normal O2/g3 compiler, existing
parsers, MIPS oracle and native32 harness. Do not repeat the previous thirty
screens or treat these new forms as semantically qualified as a group.

| Screen | Body Words | Slot Differences | Decision |
| --- | ---: | ---: | --- |
| Installed predecessor | 191 | 141 | Retain |
| Updated local total before residual store | 191 | 139 | Publicly equivalent, still wrong allocation |
| Branch-local byte divisor | 192 | 139 | Wrong body extent; consumes padding |
| Cached byte gate / word divisor | 192 | 142 | Wrong body extent |
| Named two-sample head / eight-sample tail | 190 | 159 | Signed-zero regression in emitted guest |
| Branch-local byte divisor + named history | 191 | 148 | No fit; do not adopt the history rewrite |
| Chained time-first zero assignments | 191 | 143 | No scheduling improvement |
| Signed residual / const unsigned load controls | 191 | 141 | No improvement |
| Explicit history extent 256 | 191 | 141 | Same raw object as predecessor |

The screens span 189..194 body words, always frame 0x18, with no private pools.
Differences compare the actual 192-word slot, including zero padding, not a
length-adjusted count that treats an un-emitted trailing NOP as different.
Only the updated-total form gets full public guest/native qualification here;
the named-history form is an effective emitted-code negative control.

```sh
python3 -m tools.experiments.game_frame_timing_fitting
python3 -m tools.experiments.game_frame_timing_fitting --history
python3 -m tools.experiments.game_frame_timing_fitting --combined
python3 -m tools.experiments.game_frame_timing_fitting --types
python3 -m tools.experiments.game_frame_timing_fitting --division-captures
python3 -m tools.experiments.game_frame_timing_fitting --accumulators
```

## Actual Compiler Observation

Four final, newly owned UOPT compiles cover the predecessor and updated-total
candidate in modes 5/6. The existing cc/uopt fingerprints must match; the
diagnostic stream-allocation and suppressed real-number printer gates fire.
Driver and children complete successfully. Complete parsed text, functions,
relocations and pools equal their normal compile. All 109 live input hashes
remain unchanged. Numeric diagnostic timings are not valid and are not used.

```sh
python3 -m tools.experiments.game_frame_timing_fitting --trace baseline --mode 5
python3 -m tools.experiments.game_frame_timing_fitting --trace baseline --mode 6
python3 -m tools.experiments.game_frame_timing_fitting --trace updated-total --mode 5
python3 -m tools.experiments.game_frame_timing_fitting --trace updated-total --mode 6
```

The source total is the virtual-register variable **M-8, expression 14**.
The updated-total spelling swaps its colour **2 -> 1** with the current-step
load's **1 -> 2**. Emitted instructions confirm that the incoming step moves
from V0 to V1, but the accumulator moves from V1 to V0, **not retail's A0**.
The smaller score does not restore the desired allocation.

Both forms keep the byte divisor at expression 0 / colour 5, its promoted
word at expression 6 / colour 3, and the residual address at expression
**158 / colour 8**. The actual linked words/bindings identify the residual's
LUI at +0x64 and ADDIU at +0x6C as the **T1** carrier for D_800BE610. Retail
instead loads that word through A0 at +0x5C/+0x60 and rematerializes its
store address separately in the quotient branches. This is observed emitted
code plus diagnostic constraints, not a claim about the unknown original C.

## Rejections And Qualification

All **seven final tests pass in 53.158s**:

```sh
python3 -m unittest tools.tests.test_game_frame_timing_fitting -v
```

Guest results use the existing emitted-MIPS instruction oracle and bounded
nearest-single floating model, not Ares, N64 hardware or gameplay execution.
Hardware FCSR, exception timing and NaN payloads are not qualified here.

- **6,908 three-way guest cases** compare retail, predecessor and the 139-
  difference candidate: 3,430 original fixtures plus 24 extra signed-zero/
  subnormal histories, each in two stack phases. All public memory, ordered
  callbacks and the hash of the full 1,104-byte callback region agree.
- Both C forms still have **1,662** public access-order differences over that
  expanded corpus. This includes the existing zero-reciprocal load/store gap;
  no complete fault-prefix or private-state equivalence is claimed.
- **24 actual opening access-fault cases** span two step values, three
  divisors, two stack phases and cuts 1/2. Exceptions fire at the actual LBU/
  LW dispatches +0x14/+0x18. Memory, FPRs, SP and RA agree, but GPRs differ in
  both C forms. Do not equate passing public output or two fewer differing
  words with a restored opening register contract.
- Native32 runs the actual updated-total C in separate O2/O0 units with UBSan,
  **3,430 cases each**, without -fwrapv. Ordinary remainder, wrong total-update
  sign and uncached history-index controls all fail with exit **22**, not a
  signal, undefined-behavior report or compile failure. The additional 24
  guest-only histories are not claimed as native coverage.
- All **15** owner neighbors retain raw words/bindings; the four prior warning
  sites retain their statements/carets/functions with actual source-line
  comparison. Fresh controls reject five altered immutable fixture inputs;
  all **109** live inputs remain byte-identical. Existing broad Note 1450
  installation/rebase/data-layout receipts are reused, not fresh runs.
- Four owned compiler observations complete with normal-object identity;
  the invalid trace mode/variant controls reject before invocation.

The named-history screen peels the first two samples before its eight-entry
loop. IDO removes the explicit opening +0 addition in that spelling. For ten
negative-zero history words, with a history write outside those ten entries,
retail completes with mean **0x00000000**, while the candidate completes with
**0x80000000**. Both reach the callback, whose observation also differs.
Retail actually visits the opening `add.s F0,F12,F10`, word **0x460A6000** at
**+0x260**. This is an effective guest execution counterexample, not a modeled
failure, crash or argument for changing the mean's intended sign semantics.
Do not adopt the peeled loop or force it into place with word guards.

## Bank And Resume

Tools **061bde1** commits the fitting experiment and regression suite first.
Both new files are identical in the active tools checkout and older mirror;
Windows AST passes for all four file copies. Eleven shared padder tests pass
in each checkout (0.053s active; 0.029s + 0.026s mirror), and make tools-check
passes. Preserve mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**,
all **883** initial dirty-file hashes and **885** final dirty paths. Do not
commit/reset that independently dirty checkout.

```text
Unchanged production ELF
44fa0f9f11ce36d6aad05a9214d8b025c687e54bb6dbf9e857386e2f47f3ebd3
Unchanged owner
d4884ed725cb96ba56e9a19ab0cb060682e527963579983a45b299a3e9383416
Unchanged guards
e09a6696c524fad38b6c2cbefdb4c8249e012efdd59b6a14cc51ac5958939239
```

Keep Game **2,930/4,828 (60.69%)**, total **3,603/5,501 (65.50%)**, different
**1,898**, zero drift. Production source, image, progress, guard history and
Makefile remain unchanged; no guest rebuild is required for this tools-only
investigation. Root README aggregates stay untouched. No push, Claude calls,
host-port changes or frozen Release action.

Next use the observed **byte-gate promotion / M-8 / residual-address expression
158** boundary to recover the opening roles and branch-local residual
addressing. Prefer a discriminating CFE/UGEN observation or narrowly justified
source lifetime experiment over repeating the 31 screens. Retain the signed-
zero counterexample when working on history address folding. Zero-reciprocal
access ordering, the actual instruction match and broader Game/additional-
source work remain open.
