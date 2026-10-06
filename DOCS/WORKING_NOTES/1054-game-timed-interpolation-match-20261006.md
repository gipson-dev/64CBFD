# Game Timed Interpolation Match

Date: 2026-10-06
Baseline: `f4f1d95d` ([Note 1053](1053-game-grid-channel-updater-match-20261006.md)).

## Recovered Contract

Replace the false zero-return `func_15141478` placeholder in
[`game_16DC80.c`](../../conker/src/game_16DC80.c), including its owner-local
prototype: **`s32 func_15141478(u8 *actor)`**. Complete slot **59 words / 236
bytes**, VA **0x15141478..0x15141564**, ROM **0x16E928..0x16EA14**, frame
**0x30**, existing **O2/g3**. No shared declaration/profile/data change.

Initialize payload **actor+0x110** and runtime **actor+0x170** before subtracting
live `D_800BE9A4` from timer **actor+0x180**. Only a strictly negative result
draws RNG values: float `func_150ADA68`, integer `func_150ADA20`, then another
float `func_150ADA68`. Reset timer using the first sample and the **live** scale
at runtime+0x14. Low two integer bits select the second sample's interval:
nonzero uses low+4/high+0; zero uses low+0/high+8. Store sampled target at+0xC.

Finally update current **payload+0x48** toward runtime+0xC using live smoothing
at+0x18; return1. Preserve subtraction, rounded multiplication and addition
order. No interval/timer/sample clamp or callback-value capture. Separate
sample-call statements explicitly sequence each RNG call before live field
loads; they emit the same candidate words as the earlier inline expressions.
Zero, negative zero and unordered timer comparisons bypass expiry.

## Compiler And Guard Evidence

[Persisted driver](../../tools/experiments/game_timed_interpolation_candidates.py):
eight pointer/sample/tail forms under four profiles, **32 controls**, no
installation. Actual SDK headers, fixed symbol anchors, empty diagnostics.
Selected explicit-sample form: **59 words/frame0x30/nine differences**;
**50 words compile directly**. Derive the remaining nine words without
instruction insertion/omission, branch/target/delay changes or call relocation:

- Six private runtime-pointer home stores/reloads, **SP+0x20 -> SP+0x24**,
  at offsets **0x58,0x64,0x6C,0x70,0x94,0x98**. Frame and saved-register slots
  remain unchanged; this is one consistent private-home move.
- Three commutative FPR operand swaps at **0x4C,0x84,0xAC**: timer-reset
  multiply and the two target additions. No other FPU field changes.

Derived words reproduce every retail word. The real object padder validates
all expected words and relocation metadata, assembles/links the result, and
checks a **236-byte symbol / complete59-word slot**, not a padded prefix.

## Qualification

[Nine focused tests](../../tools/tests/test_game_timed_interpolation_match.py):

- **8640 finite guest cases / three bodies** (raw, derived, retail): whole
  external storage, callback snapshots, ordered external accesses, V0=1,
  saved GPR/FPR/SP/RA, both SP phases and **all59 words reached**. Independent
  first/second samples, low-two-bit branches, timer/timestep boundaries,
  callback mutations and timestep/timer storage alias.
- **432 private-home redirection cases / three bodies**: the integer and
  second-float callbacks independently overwrite the saved pointer. Check
  intermediate pointer, final target store and tail rebase to original actor.
  Guest-only private-frame evidence, not a native stack-alias contract.
- **4320 native 32-bit actual-owner-body finite cases**: complete actor bytes
  and timestep, callback storage snapshots and independent shadow-state pass;
  callback mutations verify post-call live loads.
- **1008 special-float guest cases / three bodies**:432 field/timestep and576
  paired-sample cases. **504 native special-float cases**:216 field/timestep
  and288 paired samples. Signed zeros, subnormals, maximum finite values,
  infinities and quiet/signaling NaN encodings. Untouched storage is compared
  exactly; arithmetic NaN outputs may be compared by classification. Derived
  and retail guest bodies have identical modeled bytes and access traces.
  Python float conversion can quiet signaling NaNs; no N64 FCSR, exception,
  flush-mode or NaN-payload propagation claim follows from these fixtures.
- **Ten compiled negatives**, eight cases each: wrong expiry/mask/reset scale/
  endpoint/smoothing/return, omitted second sample, stale scale/endpoints across
  callbacks and the old stub. All distinguish actual storage/calls/return,
  without treating unsupported guest instructions as successful rejection.
- Production body/prototype, linked complete slot and all nine guard fields
  are bound explicitly. Thirty-two retained compiler controls also run.

Completed dependency rebuild and production audit against `f4f1d95d`:
only **`func_15141478`** changes across **6059 fixed slots**. Every function's
address/extent stays fixed. `.init`, `.init_data`, `.debugger`, `.game_data`
unchanged; **720 owners / 189088 Game-data bytes** remain retail-exact.
All **10738 old guards** preserved in order, plus nine: **10747 total**.
Owner warnings **0 -> 0**, zero new; shared headers unchanged.
Target SHA-256:
`be8bdc5b67968ac9bbba6a70ca0651a5e50a852b37032050a15cdc6d16cce681`.

Converted counts/bytes unchanged: **5464/6042**, Game **4791/5321**;
**85.57% total / 84.89% Game** converted bytes. Exact **3332/5464 (60.98%)**,
Game **2659/4791 (55.50%)**, **2132 different**, zero drift. Init492/492 and
Debugger181/181 unchanged. Root README updates aggregate statistics only.
All **18 focused post-link tests** pass in **55.115 seconds**, no skips:
the complete nine-test interpolation suite plus all nine retained production/
metadata tests whose total guard count changed. The full6059-slot audit also
binds every earlier function's unchanged words. This is not a rerun of all
101 previous tests. Documentation verification: **36 documents / 3401
relative links / zero broken**. `make tools-check`, compileall and diff checks
pass. All required build/test sessions completed; no runtime was launched.
The final rerun tightens NaN classification to calculated fields only;
bypassed target storage stays byte-for-byte checked, including NaN payloads.
Ignored receipts: `conker/build/game-timed-interpolation-test/`, including
`guards.csv`, `controls.json`, `behavior.json`, `negatives.json`, compiler
objects, padder fixture, build/regression/audit receipts and owner diagnostics.

## Cross-Project And Next Work

Read-only sibling `64CBFDOGL/recomp_out/.c` contains retail-translated
`func_15141478` at line975131; no source override found. No mechanical import,
regeneration, host/runtime adoption or gameplay acceptance claim. Sibling
source/build/save/frozen Release and runtime remain untouched; no push.

Next **`func_151415D4`**, **69 words / 276 bytes**, no frame, VA
0x151415D4..0x151416E8, ROM0x16EA84..0x16EB98. Piecewise envelope: initial
baseline, scaled rise, alternate plateau, scaled fall. Advance runtime+0xC by
live timestep, repeatedly subtract captured runtime+0x1C while it is smaller
than the new value. Preserve strict comparison and unchecked period behavior;
zero/negative/non-finite periods need bounded guest evidence, not a new clamp.

Ignored `next.py`, `next.log`, `next-piecewise/measurements.json`: **16 initial
controls**, four expression/pointer forms across four profiles, empty
diagnostics. O2/g3 emits **68 words/no frame/52 differences**; explicitly fresh
first-branch runtime emits68/no frame/54 differences. O2 emits67 words;
O1 variants emit85..88 with frames. No complete normalization, semantic tests,
native/padder/production qualification or installation for this next routine.
Large `func_151408A4` and other owner placeholders remain unrecovered.
