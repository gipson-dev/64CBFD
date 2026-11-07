# Record damping and midpoint integration recovered and matched

Date: 2026-11-07. Continues [Note 2164](2164-game-record-vertex-callback-match-20261107.md)
from consumer `0ebea98caf9797ee34331d07fb90962cfe6607f3` and tools
`4a61cecb2284d0ce5757d8ce5488a47c6461a4d9`. One qualified Game recovery
advances the active 80% total goal. Host code and frozen Release are untouched.

## Recovered body and actual ABI

`s32 func_1513F728(u8 *actor)` replaces the false zero-return placeholder in
`conker/src/game_169510.c`. All **193 words / 772 bytes** match after the
explicit guarded scheduling step, at VA 0x1513F728..0x1513FA2C and
ROM 0x16CBD8..0x16CEDC. The existing O2/g3, MIPS2/O32 profile emits the
original **48-byte frame**, twelve-byte previous-velocity snapshot at
SP+0x20, unsigned decrement loop, remainder preloop and fourfold main loop.
The leaf makes no calls, touches no saved registers and returns one.

The local motion view at actor+0x110 contains velocity XYZ, vertical
acceleration, damping, and angular-rate XYZ. It snapshots velocity before
updating anything; applies the damping multiplier once per tick from
D_800BE9E4; then adds vertical acceleration times D_800BE9A4 to velocity Y.
Each acceleration is `(newVelocity - previousVelocity) * D_800BE9A8`.
Position XYZ receives `(previousVelocity + (0.5f * acceleration) * time) * time`.
Angles receive angular rate times the live time value. Separate float32
operations, multiplication grouping and reloads remain explicit in C.
No powf substitution, reassociation, iteration cap or fake return is used.

The full aligned-ROM census finds **zero direct JALs, one entry pointer at
ROM 0x22E7DC, and no interior pointers**. This is slot **25** of the
42-word D_80089CB8 first-update table. The complete **195-word
func_1513CFE4**, already exact in production, passes actor A0 and consumes
the s32 result to retain/remove the record. Other update/exit/release
services remain bounded providers; this does not claim live gameplay.

## Source screens and closed scheduling derivation

Unsigned for/do and signed for forms each emit 193 words / frame 48 with 57
differences. A named half constant adds 8 frame bytes; exhausted-count returns
and aggregate/local/block variants do not improve the selected shape.
A private half-acceleration regrouping is rejected because it changes
float32 arithmetic order, regardless of its smaller difference count.
Unsigned control is selected to avoid signed decrement overflow while
preserving the full 32-bit machine count. All screens remain ignored artifacts.

Raw body SHA-256: `b6876883069d491668f92385e325e1a1609fb451e25f2c9f5a2d4eee260cf757`.
Exactly **57 expected-word guards**, including four explicitly moved bindings,
derive the output from this complete semantic body:

* Raw word 40 is BEQ to 120 with a NOP delay. Retail word 40 is BEQL to 121
  with the half-constant LUI in delay 41. Retail 120 has the same LUI for
  initial zero and main-loop fallthrough. The nonzero BEQL edge annuls 41.
  No fallthrough loop instruction reads AT before 120; the two idempotent
  constant definitions dominate MTC1 at 122 on every exit. F18's earlier
  damping value is dead there. No float operation is swallowed by annulment.
* Words 120..175 are an explicit closed permutation of the raw post-loop
  instructions. The pure half-constant write is duplicated into 41 in place
  of a NOP. Gravity/time loads commute before the first velocity store;
  the remainder of the memory operations retain their store dependencies.
  Return-one materialization moves from 130 to 175 after V0's count use ends.
  Float operands and operation grouping are unchanged.
* Time HI/LO bindings move byte offsets 480/484 to 484/492. Inverse-time
  HI/LO move 516/536 to 508/532. Tick bindings at 16/40 stay fixed. No address
  is hard-coded in the output. Four independent GNU links cover raw and
  normalized bodies at retail and a second symbol layout with signed-LO carry.

Complete word/binding hashes, explicit branch/constant predicates, AT
fallthrough checks and a closed source-index permutation reject drift.
Removing the taken-edge constant produces an effective wrong-output control.
A raw-versus-retail access-cut counterexample records the limit:
**raw C output is qualified for ordinary mapped RAM public state/return;
raw private/fault-order identity is not claimed.** Normalized output is
separately qualified for full retail private state and access prefixes.

One packet-only Claude review was used for this branch-delay question,
with tools/customizations disabled and no second writer. Its useful condition
was the dead-until-merge AT lifetime and idempotent constant. Codex checked
the actual CFG and binding movement independently; the review's imprecise
merge label and load-order source suggestion were not treated as evidence.
Packet/response/reconciliation stay in the ignored private directory.

## Focused qualification

Seven checks pass before and after installation in both tools configurations:

* **523 guest cases per body** compare retail, normalized and raw output with
  an independent float32 damping/midpoint model. Cover zero, remainder and
  unrolled boundaries, negative multipliers, signed zero/subnormals,
  bounded nonfinite modeling, and time/inverse/tick aliases at four record
  positions. All 193 words execute. Normalized/retail full machine state agrees.
* **288 connected cases per body** execute the full original updater with the
  actual slot 25 callback, including disabled records, second-callback results,
  timer removal, exit veto and cursor mutation. Caller bytes are checked
  against ROM and the frozen production ELF. Three target forms agree.
* **577 fired access cuts**, including **3 delay cuts**, compare normalized/retail
  memory, GPR/FPR/HI/LO, PC, delay context and trace prefixes. The original
  twelve-byte stack snapshot and preserved saved registers agree. Six large
  unsigned counts cover bounded main-loop prefixes and exact count decrement;
  full multi-billion-iteration execution is not claimed.
* SDK native32 O0/O2/O3 each pass **171 finite cases** through the selected typed
  slot 25. Pointer32, symbol addresses, rounding mode, FTZ/DAZ clear and trapping
  UBSan are checked. Nine compiled negatives reject with exit 1: stub, skipped
  tick, wrong damping, vertical acceleration, inverse time, destination, time,
  half factor and return. Source ticks are never clamped for these tests.
* All 193 altered-word controls, six binding corruptions, pool/option/history
  corruptions and six strict whole-image corruptions reject. Four GNU links
  preserve all six bindings and their explicit moves.

Float modeling is bounded IEEE-single arithmetic, not hardware FCSR,
floating exception or NaN-payload emulation. Guest alias/nonfinite and
private/fault evidence are separate from finite native32 C evidence.
Actors are ordinary record memory, separate from the private stack;
volatile/MMIO, asynchronous mutation and hardware acceptance are not claimed.

## Production and progress

All **181 frozen inputs**, **58 raw/padded neighboring functions**, pools,
register metadata/options and **43 inherited warnings** are preserved.
Actual Make recompiles only game_169510.c and equals the independent
complete-image predictor: **571 changed bytes, zero exclusions**. This is
569 Game-body bytes and two target extent bytes; only the target's size
changes from 12 to 772. Symbol/string order and all other named definitions stay fixed.

All **6,052 function addresses** and **189,088 protected Game bytes across
720 owners** remain exact. Historical guards are unchanged and 57 rows
append; Makefile and progress CSV remain unchanged. Compilation/linking pass.
Whole-ROM checksum retains expected exit 2 and the inherited duplicate
generated_12D630 recipe warning. No whole-image checksum match is claimed.

Both tools copies pass fresh shared smoke checks. Three unchanged shared
regressions per copy are explicitly reused after exact fingerprints.
A disposable new-module overlay and an identified read-only missing-helper
fallback preserve all 2,434 inherited dirty sibling paths.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,235 / 5,512 | 76.83% | 0 | 1277 |
| Game | 3,562 / 4,839 | 73.61% | 0 | 1277 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

**175 more exact functions** remain to 4,410 / 80%. README gets aggregate rows
only; four concise index leads preserve historical text. Refresh Graphify
with scoped, fail-closed legacy-node retention, without a fresh full-corpus
claim; commit tools before consumer source/docs/pin, then check the fresh
hook terminal, clean trees and stable production artifacts.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `aa952c7bda6ac273beebf2bc9deda8231bbd13e7964e5fa7f77752d98293f88f` |
| Production binary | `9476f523487a74f05105b86c82a5ed117a40e03643841364012e9467e8943a4b` |
| Padded owner | `ffa463db798ac8dfd4f490838b193dd4c85e62ba8d54348efc6ee85d352723e4` |
| Guard manifest | `7d1ab46c6a902544af9086d2e3a0b1cabe5e0e467ba1c3f06be39b6f50d4fb9a` |

Ignored receipts: `conker/build/game-record-damping-update-1513F728-match/`;
screens/review: adjacent `game-record-damping-update-1513F728-private/`.

A live next-target audit found that func_1513F6E8 already matches all 16 words
in the production ELF; its NON-MATCHING source comment is stale. The private
source screen is retained without new adoption or match credit.

Next: **func_1513F4E4**, the 103-word combiner-state/display-list emitter at
VA 0x1513F4E4..0x1513F680, ROM 0x16C994..0x16CB30, frame 24. Its 12-byte
production placeholder is still unmatched. Recover the Gfx pointer return,
selector service, dirty-byte pipe sync, dynamic 16-byte combiner record and
signed 16-bit cache update; qualify actual callers and ordered aliases before
adoption. Keep the 80% goal active and all frozen/private/save/host boundaries.
