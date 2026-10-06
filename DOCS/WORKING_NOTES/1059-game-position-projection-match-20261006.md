# Game Position Projection Match

Date: 2026-10-06
Baseline: `85aa7cab` ([Note 1058](1058-game-position-projection-investigation-20261006.md)).

## Source And Compiler Recovery

Replace the false zero-return projection helper and obsolete m2c comments in
[`game_16DC80.c`](../../conker/src/game_16DC80.c). Recovered effect-only ABI:
`void func_1514182C(u8 *actor, f32 *origin, f32 height, f32 scale, f32 angleX, f32 angleZ)`.
All **63 words / 252 bytes**, frame **0x80**, VA **0x1514182C..0x15141928**,
ROM **0x16ECDC..0x16EDD8**, compile directly under existing **O2/g3**.
No guards, assembly insertion, omission, profile or shared-header changes.

Build a local 4x4 rotation matrix using angleX, zero and angleZ. Read the live
origin after that callback into its translation row. Transform (zero,height,
zero) into actor+0x34/0x38/0x3C. Read all three live origin coordinates and
compute the three deltas/products before the first output store, preserving
aliases with actor positions or outputs. Store position + delta*500 at
actor+0x40/0x44/0x48. Retain separate subtraction, scale multiplication, then
500 multiplication and addition; factoring scale*500 changes rounded results.

Drop redundant position locals but keep the three delta locals. This yields
the right 63 words/frame 0x80 with five private-matrix-address differences.
Declaring delta floats **before** the matrix recovers its retail **SP+0x34**
base and removes all five differences. An equivalent nested matrix scope is
also exact. The SDK's shared actor type has unsuitable signed-halfword fields
at 0x40/0x44 and no named 0x48 field; retain owner-local byte-based float views.

The known caller `func_15141928` ignores the helper result. A void effect-only
C declaration emits the entire retail body directly; an explicit float return
does not fit. Retail's incidental F0 remains transformed X and is compared
in guest qualification. This does **not** conclusively establish the original
C return type or promise a native float return from a void function.

Update the local caller to load actor+0x170 as float bits, not numeric s32.
Angles come through the pointer at actor+0x178, offsets 0 and 8; scale comes
from actor+0x174 and origin from actor+0x17C. It still returns integer one.
All **18 slot words / 72 bytes** remain exact: **16 body words**, two zero pad
words, frame **0x20**, VA **0x15141928**, ROM **0x16EDD8**. Its linked bytes
are unchanged. Helper/caller ABI changes stay in this owner.

[Maintained driver](../../tools/experiments/game_position_projection_candidates.py):
eight matrix/product scopes and sum orders, four actual SDK profiles, plus
four caller profiles: **36 controls**, empty diagnostics. Exact main controls
are shape-000/001/100/101 under O2/g3; only O2/g3 is exact for the caller.
The driver writes ignored experiments, never installs production edits.
Prior 60 controls remain historical receipts; additional ignored position-local
and register/scope screens led to the direct declaration-order recovery.

## Qualification

[Nine maintained tests](../../tools/tests/test_game_position_projection_match.py):

- **15360 finite guest cases / two bodies**, actual compiled C and retail:
  eight origin aliases, four matrices, five heights, six scales, eight callback
  mutation modes, two SP phases. Independent full external storage, ordered
  access/call events, saved-register/SP/RA and incidental F0 agreement. All
  **63 words reached** in both bodies.
- **128 saved-height/scale-home mutation cases / two bodies**: live guest
  parameter-home reads survive callback changes. These are guest-only probes,
  not defined native aliases into a function's private frame. Combined finite
  and home-mutation receipt: **15488 cases**.
- **144 connected retail SDK cases / two bodies**: execute all **83 rotation
  words** and **40 coordinate-transform words**, with six bounded finite trig
  responses and an independent matrix/rounding reference. **141 helper words
  mapped / 123 reached**; the 18 tail/continuation words are mapped but unused
  on these normal calls. NEG.S sign-bit handling is exercised on finite values.
  The radian scale constant is read from verified Game data. This is not real
  N64 trig, exception or hardware acceptance.
- **360 connected typed-caller cases / two bodies**: float-bit arguments,
  live actor+0x17C origin, callback mutations, return integer one, incidental
  guest F0 and all 16 executable caller body words qualified.
- **9600 actual 32-bit native finite C executions**: 7680 full-storage alias/
  mutation cases and 1920 actor+0x17C direct/caller cases. Installed source,
  independent rounded reference, full actor/origin/coefficient storage and
  callback snapshots. No native scalar-return contract for the void helper.
- **720 special-float cases on each guest body and 720 native cases**: ten
  input locations, 12 encodings, three aliases, two mutation modes. Direct
  input/helper/matrix/untouched bits exact; only arithmetic NaNs compare by
  class. Angle boundaries use opaque helper providers, not real nonfinite
  rotation. No FCSR, flush mode, exceptions or arithmetic NaN-payload claim.
- **Ten compiled semantic negatives / 288 cases each**: placeholder, swapped
  angles, bad translation, integer height, zero height, wrong scale/output,
  stale or interleaved origin reads and reassociated scale*500. Real state,
  calls or strict mapped accesses distinguish each; unsupported ISA never
  counts as rejection. Differences: 288 each for the first seven, 96 each
  for stale/interleaved origins and 39 for factored multiplication.
- Production source/prototypes, full 63/18-word slots, unchanged **10760**
  guards and raw call relocations are bound: helper offsets 0x2C/0x74 to
  rotation/coordinate routines; caller offset 0x24 to projection. No rows
  target either function.

An initial three-method pre-install run passed saved-home and connected SDK
tests but failed the caller harness: it used the outer SP phase for nested
callee parameter-home writes. Correct only the harness to track callee SP
at entry. The subsequent caller/native/negative invocation passed in 77.656
seconds; controls/finite/special invocation passed in 44.054 seconds. The
original failed invocation is not claimed green. Post-build all-nine rerun
also qualifies installed source and production metadata.

## Rebuilt Audit And Progress

Explicit `make -j4 VERSION=us build/conker.us.elf` succeeds. Against banked
`85aa7cab`, only **func_1514182C** changes across **6059 fixed slots**, with
no address/extent changes. Typed caller bytes unchanged. `.init`, `.init_data`,
`.debugger` and `.game_data` unchanged; **720 Game-data owners / 189088 bytes**
remain retail-exact. All **10760 guards unchanged**. Owner warnings **0->0**,
zero new warnings. Target SHA-256:
`7e9720cc01b465122e02ff578745c5ba8c3132c41350ba01f995877d7cbf851b`.

Converted counts/bytes unchanged: **5464/6042**, Game **4791/5321**;
**85.57% total / 84.89% Game** converted bytes. Exact total **3335/5464
(61.04%)**, Game **2662/4791 (55.56%)**, **2129 different**, zero drift.
Init **492/492** and Debugger **181/181** exact unchanged. Root README changes
only the two aggregate matching rows; detailed function updates stay in DOCS.

Ignored build/audit/after and controls/behavior/SDK/negative/special/regression
receipts live under `conker/build/game-position-projection-test/`.

All **37 focused post-link tests pass in 206.840 seconds**, no skips, errors
or failures: nine new projection tests, complete nine-test actor-event and
nine-test envelope suites, and ten retained production/metadata methods.
This is not a rerun of every historical suite. The run finished while the
requested pause was in effect; its terminal successful receipt was inspected
on resume before checkpointing. **41 documents / 3453 relative links / zero
broken**; compileall, diff checks and `make tools-check` pass.

## Next Work And Boundaries

Next **func_15141A7C**, **100 words / 400 bytes**, frame **0x48**, VA
**0x15141A7C..0x15141C0C**, ROM **0x16EF2C..0x16F0BC**, owner
[`game_16EE20.c`](../../conker/src/game_16EE20.c). Global disable gate, two
classifiers, repeated callback-table reads, count-sensitive dispatch and live
linked-list cursor iteration need recovery. Inspect ABI and existing fixed
tables before compiling controls; do not introduce cached reads or bounds
checks absent from retail. Keep this next placeholder untouched until qualified.

The connected helper proof does not restore those helpers' own production C
or establish host adoption. No sibling source/build/save/frozen Release, runtime
launch, actual trig/hardware/FCSR/gameplay acceptance or push change. Continue
the Game matching goal.
