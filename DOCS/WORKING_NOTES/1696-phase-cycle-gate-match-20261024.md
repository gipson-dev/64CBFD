# Phase Cycle Callback Direct C Match

Date: 2026-10-24. Consumer predecessor `f8332af0`; tools predecessor
`f5559d5a`. Qualification tools committed first as
`5a4c1944cf28dff31f4a9dfca7869ae93c2024cb`. No push requested/performed.
Routine work, zero Claude calls; no providers or dependencies changed.

## Recovered Routine

`func_150D21CC`, `conker/src/game/generated_FF5C0.c`, replaces a three-word
zero-return placeholder with its complete phase-cycle update. VA
`0x150D21CC..0x150D227C`, ROM `0xFF67C..0xFF72C`, exclusive ends:
176 bytes / 44 body words, frame 24, three bindings, no alignment tail.
All words emit directly from normal IDO O2/g3 C without guards.

Recover `void(struct260 *owner)`, matching the real typed update table.
The common actor header is followed at +0x28 by a local `PhaseCycle` view:
active byte, three preserved bytes, phase +0x2C, threshold +0x30,
unused float +0x34 and period +0x38. Keep the existing `D_800BE9A4`
float timestep symbol. Local names describe observed operations, not an
unverified specific visual effect or actor identity.

1. Add the timestep to phase with a single-precision store.
2. While phase is strictly greater than period, subtract period and store
   each single-precision result. Exact-period phase remains period, not zero.
3. When the resulting phase is less than or equal to threshold, set the
   active byte to one before submitting `(255,255,255,255)` to the color
   helper. Otherwise clear the byte and make no call.

Do not substitute modulo/fmod, a greater-or-equal loop, a zero-period
bailout or a single algebraic reduction. Zero/negative periods, Infinity
and finite precision stalls can retain the original nonprogress loop.
Production behavior is preserved; malformed tests use bounded guest
execution and never invoke a nonterminating native case.

Raw object body SHA-256:
`9a5c82301428b1b96389fa9bf7663bdab3256498c555432c290c98befd456a4f`.
Resolved retail body SHA-256:
`1b864e9b56b8989a78c6c602b08cc71aaf60ce8260927c3a9c337e73c4686f15`.
Bindings: timestep HI16 +0x08, timestep LO16 +0x0C, color JAL +0x8C.
Independently assembled original and isolated/whole-owner C have identical
raw payloads and symbolic bindings, not just the same resolved addresses.

The unreachable duplicate byte clear at +0x9C is emitted by the compiler
and retained literally. Coverage visits all 43 executable root words;
the unreachable store is explicitly accounted for, not counted as visited
or excluded from the 44-word matching extent.

## Caller And Helper Boundaries

An aligned full-ROM scan finds no direct JAL sites and exactly one literal
function pointer at ROM `0x22F064`, slot 47 of the 98-entry update table
`D_8008A4E8` (VA `0x8008A4E8`, ROM `0x22EFA8`). The existing callback
declaration is `void (*)(struct260 *)`; no incompatible function-pointer
cast or guessed integer-return ABI is introduced.

Execute the complete 45-word `func_15149264` parent in 432 phases:
selectors -1/0/47/97, destructor -1/0/9, both tick flags, lifetime -1/0/32767,
ticks 0/1/30 and active/inactive color paths. Check signed disable sentinel,
lifetime narrowing, callback ordering, destructor and final release.
All parent words are visited. Other update/destructor callbacks and
`func_1516972C` remain bounded providers in this test, not newly recovered C.

The retained 19-word `func_1515D4D4` helper is already byte-exact and
unchanged. The root passes all 255 values, so the helper accepts priority,
stores the three low RGB bytes, writes dirty word one and priority 255.
Visit all 19 helper words in connected guest execution; compile its actual
C body together with the root and actual parent for the native chain.

Its defining source and retail ABI use `void(s32,s32,s32,u8)`. Add that
correct local declaration rather than the stale shared `functions.h`
declaration `void(u8,u8,u8,s32)`. Do not broaden this change into a shared
prototype repair/recompile of unrelated users. Root constant 255 arguments
are qualified across the actual interface; no wider caller repair is claimed.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips, zero reused checks. Pre-install primary/mirror:
9.454s / 9.656s; installed: 10.752s / 10.439s. Both shared tools checks
exit zero. Reuse existing MIPS, float32, frame/fault, native32, source-span,
object/pool, relocation and normal generated-padder helpers.

- 4,560 terminating finite guest phases cover signed zero, denormals,
  negative phase/timestep, exact period, adjacent ULP boundaries, repeated
  wraps and inclusive threshold equality. Five normal/global-overlapping
  layouts and two stack phases preserve complete original guest state,
  calls and external bytes. Another 390 generated alias cases exceed the
  reference loop budget and are not mislabeled as finite acceptance.
- Four dedicated zero-period, negative-period, Infinity and finite-stall
  probes compare literal/fitted complete prefixes at the same execution
  budget. Three quiet-NaN cases exercise ordered comparison behavior in
  the model only. This is not N64 FCSR/exceptions or hardware emulation.
- Twenty-six fired root-access fault prefixes preserve complete private
  state, saved-register/return lifetime, PC and delay origin. Correctness
  is not reduced to output-only comparison.
- Native32 O0/O2/O3 with trap UBSan executes 1,980 connected actual
  parent/root/color-helper cases per optimization. Python independently
  generates expected little-endian byte-image hashes and call order.
  Use full 64-byte typed owner backing with a separate header/tail, proper
  callback types and declared storage for the dirty word. Native overlap
  and malformed-loop behavior are not claimed from these finite fixtures.
- Six effective defined wrong-C controls reject equality wrapping, missing
  timestep, strict-only threshold, wrong flag, wrong RGB and omitted call.
  Fresh native actual-parent boundary tests cover all 98 update slots,
  disable/destructor paths and three effective parent controls.
- Four strict-image controls reject unrelated header/trailing/code changes
  or a different retail body. All guard CSV bytes remain identical.

The first native fixture emitted flat initializers for a nested trace array,
triggering compiler diagnostics. Correct the fixture braces and bound
diagnostic reporting before the fresh passing runs; no production semantics
or compiler warning settings were changed to mask the error.

## Production And Preservation

Advance the previous sealed baseline only for its four already-qualified
overrides. Seal 15,950 initial files, then add the two owned tools files in
both copies: 15,954 files / 31 focused inputs / all 1,454 linker objects.
Use checked native stdin/tar streams and the verified Linux cache, without
DrvFS project reads.

Actual shadow Make uses three ordinary commands, IDO O2/g3 and the normal
generated-slice padder. Its complete padded object equals qualification.
Preserve all six raw/padded neighbors and pools. Isolated diagnostics are
empty; whole-owner diagnostics remain unchanged. Production Make exits
zero in 21.061s. Its broader dependency rebuild retains all non-target
object bytes. Inherited compiler/libultra and duplicate generated_12D630
recipe warnings remain; no warning-free build claim.

Independent and production links agree on exactly 126 changed ELF bytes:
125 target-code bytes and one target symbol-size byte, 12 to 176.
No metadata exclusions, reordering or unrelated changes. Preserve all
other 6,054 bodies, all 6,055 addresses and protected Game data:
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Audit all 15,954 native entries before/after adoption with exactly three
overrides: target source, target object and ELF. Recapture the live adopted
ELF and independently recount that actual stream, not an inferred +1.

Installed ELF SHA-256:
`ab07cb5ca8e137c6e9a9c25b6e8b874ec2ed95131b279cced742b90f68f949cc`.
Installed target object SHA-256:
`ca0be42e1afd82098eb956039d5b0266878185d86ea9e310a01776d0d4980c09`.
Unchanged guard CSV SHA-256:
`3a5b68d16b833e8b1e1c054f492606354062658a3bfa01cd520b97f9f29a5d1c`.

Preserve all 1,604 pre-existing older-mirror dirty paths/statuses/hashes/HEAD;
add only the two owned tools files, leaving 1,606 dirty paths. Do not reset
or commit the independent mirror. Host Release, saves, configuration,
private inputs, providers and dependencies are untouched.

## Measured Progress And Resume

| Section | Byte-Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,773 / 5,505 (68.54%) | 0 | 1,732 |
| Game | 3,100 / 4,832 (64.16%) | 0 | 1,732 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove only `func_150D21CC` from the live-ELF-pinned queue. Remaining
source screens: 1,603 simple placeholders, 120 semantic/other and nine
unlocated entries. `func_1510D8C0` already has `Gfx *` C missed by the
parser; its private screen and `func_1518C850` remain uncredited. Continue
the remaining 44-word candidates, keeping the 92-word `func_1509E730`
and 862-word `func_1508CAD8` stubs separate. Target 4,129 exact C functions:
356 more, goal incomplete.

Root README changes only its two aggregate matching rows. Retain normal
post-commit Graphify worker receipts and verify all eight changed-file
hashes/mtimes/memberships plus all 43,953 prior nodes. The retained-corpus
warning remains; do not claim full-corpus re-extraction or old-edge retention,
and do not forge a missing commit stamp. No rendering/gameplay/hardware
acceptance is inferred from this C recovery.

Ignored evidence: `conker/build/game-phase-cycle-gate/qualified/`.
Tools: `tools/experiments/game_phase_cycle_gate.py` and
`tools/tests/test_game_phase_cycle_gate.py`.
