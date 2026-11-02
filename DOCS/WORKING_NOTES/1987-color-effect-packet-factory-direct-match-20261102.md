# 1987 - Color-effect packet factory recovered directly from C

Verified 2026-11-02. Production **4,054/5,507 (73.62%)**; Game
**3,381/4,834 (69.94%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,453 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **352 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15152874(ColorEffectInput *input, u8 mode, s32 extra)` replaces the
zero-return placeholder in `conker/src/game/generated_17CAF0.c`. Original
`17CAF0.s`: VA15152874..15152ABC, ROM17FD24..17FF6C, 146 words, 144-byte
frame and twelve relocation bindings. The caller supplies a 76-byte input
record. The factory chooses an unsigned count from `baseCount + RNG %
(countRange + 1)`, copies position and two scalar fields, then builds one
52-byte visible packet for each iteration.

Every packet uses two integer draws for signed-halfword vector angles, one
float draw for radius, another for scale, one integer lifetime draw and two
more float draws for scalar fields. Input fields stay live across providers.
A signed color selector of -1 writes opaque white; other selectors dispatch
through `D_8008AC60`. Submission receives the low bytes of mode and extra.
The submission result is ignored and does not stop later iterations. Unknown
field meanings remain offset-based rather than receiving speculative names.

## Complete private packet extent and direct bytes

The helper-visible packet fields end at byte 52. Retail nevertheless allocates
a complete **56-byte** private packet object: four trailing bytes are untouched
by this function and are not read by the qualified submission interface.
Declaring `privateTail34[4]` preserves that compiler layout without inventing
a scalar meaning. A 52-byte declaration moved thirteen stack-address words by
four bytes; the complete extent naturally restores retail SP+0x58.

The selected C emits all **146 retail words directly**, frame144, with every
relocation binding equal and **zero expected-word guards**. Raw payload SHA256:
`cfcd734f0d79c98d7874b2f9b24d5eb39629d15db87ed3a9efc7831ff8c5f4f4`.
Original and C objects also agree after three independent GNU links with
shifted code, helper and global layouts. The four retained divisor traps are
unreachable when the qualified range divisors are nonzero.

## Fresh qualification

- Guest execution covers 256 cases / 512 original-versus-C runs, all 142
  reachable words, all 256 mode bytes, both color routes and live input
  mutation after the first RNG and after submission. Full memory/register/FP/
  call/packet/trace state agrees. Two fired access-prefix cases produce 129
  equal prefix pairs. Semantic execution uses the authentic layout; the three
  independent GNU links separately prove relocation equality.
- Native32 runs 256 cases under each of O0/O2/O3 with UBSan. Eleven effective
  controls per profile reject altered RNG sign handling, count, angle,
  lifetime, scale, color, mode, extra, radius, cached-input timing and packet
  extent. The 76-byte input, 52 visible bytes and 56-byte private extent are
  asserted without reading the untouched tail.
- The aligned-ROM census finds exactly one JAL, ROMFAFA4 / VA150CDAF4, and no
  aligned jump or literal target pointer. The actual four-word call window
  executes 256 cases: input is SP+0xA0 from the JAL delay slot, mode is LBU
  owner+0x0C and extra is LBU owner+0x01. Twenty descriptor-write sites span
  SP+0xA0..SP+0xE8. The return is not consumed before the parent returns.
  The complete 221-word parent `func_150CD7F8` remains retained assembly and
  is explicitly not claimed or credited.

Both tools copies contain byte-identical five-module qualification suites.
Five fresh pre-install methods pass against each copy; the primary suite then
passes all five again against the installed production source/object/image.
No gameplay or portable-uninitialized-byte acceptance is inferred.

## Actual owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 29,396-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners.

The strict complete-image predictor replaces the 584-byte target slot and
symbol extent 12->584, then closes one existing named metadata exchange between
`D_8008AC60` and `D_8009EE78`. It has zero exclusions. All 6,052 addresses,
6,051 other bodies and the complete named-definition multiset stay fixed.
The production ELF equals the independent prediction exactly.

Linked ELF SHA256:
`f459bd92845118fe65e9615347275c6b6a08821b21558c9546b87922a6e88b20`.

The stage is
`conker/build/game-color-effect-factory-15152874-match/`. It retains guest,
native, caller, owner, full-image, installed and transfer receipts. The root
README changes only aggregate status rows; detailed recovery stays here and in
the five concise indexes. The scoped Graphify refresh is structural AST only,
retains prior nodes and valid edge occurrences, archives the obsolete s32
placeholder return, and makes no full-corpus or global-reclustering claim.
No Claude call was needed.

## Next step

Audit adjacent `func_15152B38`, still a zero-return placeholder in the same
owner: VA15152B38..15152F70, ROM17FFE8..180420, 270 words and frame176. Screen
its complete interface, callers and helper/provider ordering before attempting
a broad recovery. Keep private candidates uncredited until guest/native/caller,
owner/actual-Make, strict-image, installed recount and documentation gates pass.
