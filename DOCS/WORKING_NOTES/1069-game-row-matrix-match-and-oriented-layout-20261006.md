# Game Row Matrix Match And Oriented Layout

Date: 2026-10-06. Baseline: `6c1d385f`
([Note1068](1068-game-oriented-matrix-recovery-20261006.md)).
This checkpoint installs the adjacent row-scaled matrix builder while banking
further oriented-layout recovery. Only `func_15142838` changes production bytes.

## Recovered Row Matrix

`func_15142838`:55 words/220 bytes, frame0x58,
VA15142838..15142914, ROM16FCE8..16FDC4. Nine inputs:output Mtx pointer,
two row factors, three rotation inputs and three translations.
[Semantic implementation](../../conker/src/game_16EE20.c) calls
func_150A8050(matrix,rx,ry,rz), stores translation in matrix[3][0..2],
then multiplies the first three columns of rows0/2 by row0 and row1 by row1.
All provider fourth-column fields, including matrix[3][3], remain untouched.
Finally call guMtxF2L(matrix,output). No scalar return is consumed.
After the rotation provider, output, scales and translations reload live
argument homes; rotation inputs have already been consumed.

Provider call offset2C, converter call offsetC4; the last matrix element is
stored in the converter call delay. The existing O2/g3 profile emits all55
retail words directly. No new guards, compiler/profile changes, frame/stack
rewriting, shared-header changes or padder changes.

[Original caller func_15133760](../../conker/src/game/generated_15F680.c)
is24 words/96 bytes, VA15133760..151337C0, ROM160C10..160C70.
It loads eight floats from source+18/+1C/+20/+24/+28/+38/+3C/+40 and returns1.
Correct the local callee declaration to void/Mtx* and explicitly cast the
generic u8* output; no numeric conversion or caller-instruction changes.
All31 raw functions/relative relocations/pools in the caller owner remain
unchanged. Both production owners retain their two existing warnings.

## Maintained Controls And Qualification

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_row_matrix_candidates.py):four store-order
forms across four SDK profiles,16 controls, empty standalone diagnostics.
Translation-first/row-order/O2g3 is the unique exact control. Its non-g3 O2
counterpart differs in four words; translation-last O2g3 differs in37, column
ordering in19. O1 controls grow to72 words.

[Eleven tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_row_matrix_match.py):

- 2160 paired guest cases:five first-row/four second-row scales, three translation
  sets, three provider patterns, aliases, source mutations and two stack phases.
  All55 words covered; full ordered trace and storage identity, preserved saved
  state despite poisoned volatile registers.
- 192 every-float-input special-bit cases and36 guest-only argument-home probes.
  Output/scales/translations remain live; consumed rotation inputs do not.
- 288 connected cases execute every original24 caller/55 builder/115 converter
  word. Conversion is restricted to finite, exactly integral, signed32-bit
  representable results after multiplication by65536.
- 1176 actual freestanding32-bit native typed-caller cases:1080 finite plus96
  special-bit cases. Compare full external bytes; arithmetic NaNs only by
  classification. Provider and converter are bounded payload-capture helpers.
- Nine compiled semantic negatives alter mapped, meaningful fields/calls:
  placeholder, missing provider/converter, wrong row/translation/rotation/output,
  premature translation, and overwriting a retained provider field.
- Strict missing-source/private-matrix/output checks; actual padder preserves220
  symbol bytes, excludes the four-byte text alignment tail, retargets both calls.
- Copied builder owner preserves92 neighbors/pools/relocations/two warnings;
  copied caller preserves all31 functions/pools/relocations/two warnings.
  Production binds exact target/caller/eight neighbors and unchanged guard hash.

The first ten-test pre-install run failed a native harness compile because
`-Werror` rejected misleading indentation. Splitting count++ onto its own line
fixed the harness, not production behavior; all ten then passed in26.230s.
The final production gate is part of the40-test post-link regression below.
No original rotation-helper C restoration, general rounding/FCSR flags,
NaN/out-of-range fixed conversion or gameplay acceptance is claimed.

## Oriented Layout Follow-Up

`func_15142600` still remains a zero-return production placeholder. Its retail
142 words/frame0xB8 are not yet recovered from legitimate C.
[Maintained driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_oriented_matrix_candidates.py)
now has64 controls:the prior32 plus32 direction-order/captured-start controls.

| Maintained O2/g3 Control | Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Frame-fitting array-up |142|0xB8|84|
| Prior reversed up-vector |142|0xC8|57|
| Ordered locals, reversed direction |142|0xC8|47|
| Ordered locals, reversed direction, captured start |142|0xD0|44|

Every differing word of the last three candidates is still only a stack
immediate; non-stack instruction order, arithmetic, register allocation,
saved-register lifetime and helper-call position agree.
The47-difference form recovers direction at SP68/6C/70; its matrix is SP74
instead of retail78. The44-difference captured-start form recovers deltaZ
at SP3C, horizontalZ at44 and upZ/Y/X at48/4C/50; direction moves to70/74/78,
matrix to7C. Neither recovers the frame0xB8 allocation.

[Twelve maintained tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_oriented_matrix_recovery.py)
passed in69.874s before the production regression:2448 five-body guest cases,
1224 native caller cases per candidate across four candidates,144 original
caller/builder/converter cases per body, nine semantic negatives, native
integer-load rejection, padder and copied owners. Every candidate covers all142
words. These tests qualify known external behavior, not private-trace identity
across different stack layouts. All previous provider/native-NaN/FCSR/converter
bounds from Note1068 remain.

Ignored exploration covered48 struct orders,32 scalar-vector forms,60 scalar
orders,16 capture forms,16 scopes,16 normalized-component forms,16 union views,
64 mixed struct/array norms and16 reciprocal/sqrt staging forms. No exact
candidate emerged. Nine g1/g2/O3 attempts were diagnostic-gate rejections,
not passing controls; no maintained profile changed.
Debugger local records are frontend declaration offsets, not proof of optimized
physical stack allocation. Do not use them to justify an allocation claim.
A final12-control three-component horizontal-vector scratch screen found
142/frameC8/44; this extra candidate is not maintained or behavior-qualified.

Next:qualify that horizontal-vector shape if promising, then recover the
original142/frameB8 layout. Do not normalize oversized frames or install guards
that merely rewrite private offsets. Install oriented builder/typed caller only
after direct-layout, behavior, copied-owner and post-link gates.

## Production Receipts

Explicit US ELF build passed. Audit against the Note1067 production manifest:
6059 slots, only func_15142838 changes; all addresses/extents stable.
Protected init164048/init_data17376/debugger19800/game_data189088 bytes unchanged.
All720 Game-data owners/189088 bytes exact; all10809 existing guard rows unchanged.
Guard canonical SHA256:
`e021c108eef6c84112743955be809d3bdf4ce4e1de0cba474897ed3b0bcabb8a`.
Target SHA256:
`13078cff7fb5863a11a215fc6165df412afb33b9de61abc8601785e4ac5cf998`.
Original608-byte builder private pool and owner diagnostics unchanged.

All40 focused post-link tests pass in119.063s, zero skips/errors/failures:
11 row matrix,12 oriented,12 scaled matrix,5 padder tests.
Project tool checks, scoped Python compilation and git diff whitespace checks
pass. Documentation verification covers51 documents/3575 relative links,
zero broken links.
Refreshed actual progress.csv and matching report:

| Section | Converted | Converted Bytes | Byte-Exact | Different | Drift |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total |5464/6042 (90.43%)|85.57%|3343/5464 (61.18%)|2121|0|
| Init |492/539 (91.28%)|92.53%|492/492 (100%)|0|0|
| Game |4791/5321 (90.04%)|84.89%|2670/4791 (55.73%)|2121|0|
| Debugger |181/182 (99.45%)|99.19%|181/181 (100%)|0|0|

Converted totals do not rise:replacing an existing C placeholder adds semantics
and an exact match, not a newly converted slot. Root README updates aggregate
matching rows only. Detailed status stays in DOCS.
Ignored audit/regression/build/progress receipts are under
`conker/build/game-row-matrix-test/`; compiler controls under
`conker/build/game-row-matrix/` and `conker/build/game-oriented-matrix/`.
No sibling source/build/save/runtime, frozen Release, host adoption or push.
Game matching goal stays active.
