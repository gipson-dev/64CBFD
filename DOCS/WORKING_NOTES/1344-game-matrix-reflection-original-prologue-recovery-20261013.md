# Matrix Reflection Original Prologue Recovery

Date: 2026-10-13. Continue
[Note 1343](1343-game-matrix-reflection-sdk-typed-saved-index-recovery-20261013.md)
on `func_15034F30`: VA `0x15034F30..0x150356C8`, ROM `0x623E0..0x62B78`,
486 words / 1,944 bytes, original frame `0x190`.

## Scope And Baseline

Consumer baseline: `a0ef72a8778a2d022b5e6dabc9685aa3f31392bf`.
Tools baseline: `4efe06f102df0369df332e166dc790afc88b40b3`.
Production remains the zero-return placeholder in
`conker/src/game/generated_61D10.c`. Candidate work is uninstalled; no guard,
profile, production source, linked image, progress or root README edit.
The wider Game matching goal stays active. This checkpoint is not a whole
function match, conversion credit, SDK execution or host/gameplay acceptance.

New experiment and qualification:

- `tools/experiments/game_matrix_reflection_register_schedule.py`
- `tools/tests/test_game_matrix_reflection_register_schedule.py`

## Original Opening Recovered

The old source temporarily assigns the input formal to the reflection buffer,
calls identity through that value, then restores the input from a `saved` local.
That extra source-level assignment prevents the original opening schedule.
Use the direct `guMtxIdentF(reflection)` call instead, leaving the input formal
unchanged and removing the now-unused real temporary.

Under the existing O2/g3 profile, the complete **first22 words are retail-exact**.
The key beginning is now:

```text
27BDFE70  addiu sp,sp,-0x190
AFB60058  sw    s6,0x58(sp)
00E0B025  move  s6,a3
AFBF0064  sw    ra,0x64(sp)
```

All other saved stores, three incoming argument stores, the identity call and
its direct SP+0x150 argument also match. The recovered four s2 shifts and later
instruction stream from Note1343 remain unchanged.

| Measurement | Result |
| --- | --- |
| Selected complete words / frame | 486 / 400 (`0x190`) |
| Literal differences | 240, versus banked259 |
| Emitted words changed | 19 |
| Words22..485 versus banked259 | Identical |
| Compiler diagnostics / extra pools | Empty / 0 bytes |
| Source guards / installation | None / no |

Word22 is still different: the source reads the first mode into v0 rather than
retail t6. The s4/s5 conversion-buffer/offset roles, later floating registers and
caller temporaries remain unresolved. Fixed-input return GPR9/14 are still
different. Do not infer a whole function match from the exact opening.

## Compiler And Profile Evidence

Twenty-three named complete source forms produce eight extent/frame-valid
literal arrays. Compare full words to establish that plain/cast/address direct
identity forms emit the same selected body. Integer-address formals produce263
differences, without the recovered opening. Reusing another opening pointer
temporary produces488 words and is rejected. Other pointer views, flat conversion
storage, meaningful translation-value locals and unsigned snapshot/offset forms
do not improve the selected score. No artificial masks, padding or fixed-register
bindings are introduced.

Profile evidence is specific to this complete body:

| Profile | Words | Frame | Differences | Exact Opening Prefix |
| --- | --- | --- | --- | --- |
| O2/g3 | 486 | 400 | 240 | 22 words |
| O2 without g3 | 486 | 400 | 257 | 1 word |
| O1/g3 | 556 | 312 (`0x138`) | 539 | 0 |
| O1 without g3 | 556 | 312 (`0x138`) | 539 | 0 |

The bare-O2 form is an effective opening-fault negative despite matching the
extent/frame. O1 variants fail both gates. Production continues using its
existing O2/g3 settings; no profile change or compiler installation is needed.

The fingerprint-locked owned capture fires, exits successfully, and preserves
the whole normal/traced object and pools. Frame transitions stay88 ->104 ->400;
physical locals296 / saved88 / outgoing16 remain unchanged. Removing the real
temporary changes frontend M288 ->284 and optimizer M296 ->292, with P76 fixed.
This is a logical stream-definition change, not a changed physical frame.

All four matrix addresses remain SP+0x84,0xD0,0x110,0x150, with optimized offsets
-268,-192,-128,-64. Both streams retain five direct P+16 output loads and three
direct P+8 mode reads, no output-address materialization and no P+12 input-formal
assignment. Reflection's fp cache stays removed. The two conversion-buffer
rlda M-268/raw register20 records remain; the s4 versus retail s5 cache role is
not recovered. Raw records are retained without undocumented flag-bit inference.

## Qualification And Strict Controls

Four focused opening/frame/fault/profile checks pass in5.562 seconds. The
complete suite passes **all26 checks in75.233 seconds**, including24 target
checks and two protected text/data checks. The full output is retained under
`conker/build/game-matrix-reflection-register-schedule-test/full-suite.log`.

The existing4,800 sampled guest cases, aliases, live homes, native32 O2/O0 with
four effective negatives, actual19-slot caller windows, both complete owner
padders, independent rebases and wrong-index control remain enabled and pass.
The mixed-format alias still reaches its original bounded provider rejection;
no final result or actual SDK implementation execution is claimed.

Across192 domains, **10,260 common fault triplets actually fire** against259.
Full modeled agreements rise **192 ->3,648**, with no prior agreement lost.
Output-home counts still match retail, and own-access-count distance never
worsens. The focused original/selected comparison is equal at cuts0..18 in both
stack phases; first difference moves **cut1 ->cut19**. The old259 opening remains
an effective cut1 negative, as does the bare-O2 profile.

Historical count controls now explicitly compile333,331 and259 references:
their bad329 rejection counts remain8,48,48. Preserve all eight historical
domains, all48 newer domains, the21 older forms, the11/15-word distinctions and
the old407 indirect-load diagnostic. Check selected count distance over all192
domains. No banked test, assertion implementation or acceptance gate is weakened.

These are bounded complete modeled states, not hardware PC/BD/full FCSR/HI,
arbitrary-input, complete parent execution or gameplay proof. Routine work uses
zero additional Claude calls. The full Game objective is not complete.

## Frozen Production And Banking

All seven target inputs, protected text/data, guards, progress and root README
remain fixed. Counts stay Game2,824/4,823, total3,497/5,496, different1,999, drift0,
converted5,496/6,044. There is no production rebuild or aggregate credit change.

Both tools copies pass ROM-free wrapper and Windows syntax checks. Older tools
HEAD ddbdd16 and all440 initial dirty-path fingerprints remain fixed; only two
absent, byte-identical files are added. Tools
**579be6c075871007ec300c8f2e3862729ab28821** banks those two files first; the
consumer records its exact pin/docs. No push, duplicate mirror history,
dependency install, real-save changes or frozen Release work.

Direct graph update refuses18,765 proposed versus40,545 existing nodes. Retain
19,398 nodes from2,972 excluded-but-existing files, the skill0.9.20/package0.9.26
warning, zero-node devcontainer and oversized-HTML limitations. Do not force a
shrink. Record the incremental hook and post-bank receipts after completion.

Reproduction from the prepared consumer root under WSL:

```sh
python3 -m tools.experiments.game_matrix_reflection_register_schedule --filter identity-direct-plain --profiles
python3 -m tools.experiments.game_matrix_reflection_register_schedule --probe
python3 -m unittest tools.tests.test_game_matrix_reflection_register_schedule \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls -v
make tools-check
```

## Next Work

Keep this same routine active. Restore the s4/s5 byte-offset/conversion-cache
roles and remaining mode/floating/temporary schedules while preserving the
retail-exact22-word opening, four exact shifts, matrix addresses and3,648 modeled
agreements. Finish all240 differences and private/fault/linked-image qualification
before installing or claiming a byte-exact function.

## Post-Bank Verification

Consumer **5be301e11162bbc90931da9b833b905d78f7e910** records the exact tools
**579be6c075871007ec300c8f2e3862729ab28821** pin and linked documentation.
Both active checkouts are clean. Older tools retains HEAD ddbdd16 and all440
initial fingerprints, with only two absent additions (442 dirty paths).

Eight fresh post-bank checks pass **in10.018 seconds**: all seven frozen target
inputs, private RAM/return boundary, owned compiler capture, recovered fault
prefix, four exact shifted-index words, effective profile negatives and both
protected text/data checks. Cuts0..18 still agree in both phases; cut19 and
returnGPR9/14 remain unresolved. The full26-check receipt remains separate.

The incremental hook completes at **40,555 nodes / 81,041 edges**, with zero
live graph workers and retained history intact. The direct shrink refusal and
oversized-HTML limitation are not bypassed. The new note link resolves; root
README SHA256 remains
`640d27f289d843d625eabd94f747b399fc31105726db2a78ab245962ac885e8c`.
No push, production rebuild, dependency installation or host Release work.
The wider Game goal remains active on this routine's remaining240 differences.
