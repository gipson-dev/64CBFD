# 1993 - Angular-trail factory recovered as guarded C

Verified 2026-11-02. Production **4,060/5,507 (73.72%)**; Game
**3,387/4,834 (70.07%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,447 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **346 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15153F18(AngularTrailInput *angles, LocalizedTrailInput *input,
s32 category, s32 channel, s32 owner)` replaces the zero-return placeholder in
`conker/src/game/generated_17CAF0.c`. Original `17CAF0.s`:
VA15153F18..151541B8, ROM1813C8, 672 bytes, 168 words, 184-byte frame and
fourteen relocation bindings. The caller-qualified input is one natural
76-byte descriptor: an 8-byte angular prefix followed by the existing 68-byte
localized-trail configuration. Seventy-three bytes are required by every
caller; root offsets 0x3D..0x3F remain private padding. All twelve bytes of the
local velocity vector are observable.

The factory chooses a randomized request count. For each request it draws two
unsigned random values, constrains them by the two signed angle ranges and
passes the resulting angles, a randomized radius and the velocity output to
`func_15143794`. Four further integer/float draws select scale, duration, mode,
time and request-selector values. The eighteen-argument provider
`func_151DA6F8` receives those values, the localized configuration, category,
owner, the low big-endian byte of `channel`, two copies of the recovered
constant and the opacity comparison. The return contract is `void`.

The complete linked-image census finds exactly five aligned JAL sites:
VA151422A8 in `func_15142180`, VA151AEDD0 in `func_151AECA0`, VA151B04FC in
`func_151B03B8`, VA151DC374 in `func_151DC260` and VA151DC594 in
`func_151DC484`. All five establish every required descriptor byte. The exact
C caller at VA15142180 independently confirms that argument 0 is the angular
prefix and argument 1 is the overlapping root-plus-eight localized view. No
aligned jump site exists and conservative return-value taint reaches no
post-call read.

## Closed compiler words

The semantic C emits the retail 168-word extent, fourteen bindings, unrolled
random sequence and loop shape. Its natural compiler frame is 200 bytes;
sixteen checked expected-word normalizations close the remaining independent
layout choices:

- six frame/home/scratch words at offsets 0x000, 0x044, 0x078, 0x080, 0x22C
  and 0x29C;
- eight saved-register allocation words around the integer random values at
  offsets 0x094, 0x09C, 0x0B0, 0x0C0, 0x12C, 0x144, 0x158 and 0x1E0;
- two commutative floating-multiply operand orders at offsets 0x180 and
  0x190.

No relocation word is guarded. Three independently shifted GNU layouts agree
after those sixteen closed words. Raw semantic payload SHA256:
`842db97e986a881744d8c94aa402debbcabcfade28518ece6246a2a35c7e8d9b`.
Normalized payload SHA256:
`820ec0ad3cdc593311eb877d8f12192740dd57f49c5127d91ee81e98b71ed161`.

## Fresh qualification

- Guest execution covers 256 cases at each of three independent links and
  three images, for 2,304 executions. All 162 reachable non-trap words execute;
  six positive-divisor trap words remain unreachable under the qualified
  ranges. Zero/one/two-request paths and all 256 channel bytes execute.
- Original, normalized and raw C agree in public memory, register, FP, call and
  complete provider-payload state. The comparison records 1,008 payloads,
  every one of the eighteen provider arguments and complete descriptor and
  scratch snapshots. Live mutations after count RNG, direction generation and
  provider calls prove the recovered read timing.
- Native O0/O2/O3 runs 256 cases per profile, 768 total, with warnings treated
  as errors and UBSan stopping at the first error. All profiles pass without a
  warning or sanitizer finding. Whole-descriptor fences remain intact.
- The caller census proves all five original JALs, five unique parents, the
  O32 fifth-argument stack slot, the overlapping descriptor views and all 73
  required bytes. Complete parent gameplay execution is not claimed.

The permanent five-method suite reproduces raw/binding, guest, caller, native
and complete-image gates from retained receipts. It passes after installation
against the actual production object and ELF. The bounded Graphify refresh is
structural AST only, retains every prior node and every still-valid prior edge
occurrence, archives the obsolete `s32` placeholder return edge and uses zero
LLM tokens. No full-corpus extraction, global reclustering or gameplay
acceptance is claimed.

## Owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 30,288-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The strict complete-image predictor replaces only the 672-byte target. It has
zero exclusions: all 6,052 function addresses, 6,051 other bodies and the
complete named-definition multiset remain fixed. The installed production
object equals the qualified five-command Make object, and the production ELF
equals the independent strict whole-image prediction exactly.

Installed object SHA256:
`ffaf0f20cc7855202ae7605709136fa6735012908d5832b30fb6b86b3d5fe143`.
Linked ELF SHA256:
`17ad20e1a039f88b9008b1b694447978cc68502dab29f74a51d17d47b5401c4c`.
Production linker-map SHA256:
`ebb679dbafe5095950abc7ea997853701ce7cf975c8529cf54230dc13f2f0b51`.

The public qualification tools were committed first at `431ab8f`. The retained
stage is `conker/build/game-angular-trail-factory-15153F18-match/`; it contains
the layout, guest, native, caller, owner, whole-image and installed receipts.
The root README changes only aggregate rows; detailed recovery stays here and
in the five concise indexes. No Claude call was needed.

## Next step

Privately audit `func_15154684`, the next zero-return C placeholder in this
owner. Its retail slot is VA15154684..15154884, 512 bytes and 128 words. Keep
it uncredited until ABI/caller, semantic runtime, owner/actual-Make,
strict-image, installed recount, documentation and bounded Graphify-retention
gates pass.
