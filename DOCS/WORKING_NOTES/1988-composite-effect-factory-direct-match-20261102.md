# 1988 - Composite-effect factory recovered directly from C

Verified 2026-11-02. Production **4,055/5,507 (73.63%)**; Game
**3,382/4,834 (69.96%)**, Init 492/492 and Debugger 181/181. Zero address
drift, 1,452 different; one new installed match and unchanged C inventory.
The active 80% target remains **4,406/5,507**, requiring **351 more**. This is
progress toward that goal, not completion.

## Interface and recovered behavior

`void func_15152B38(CompositeEffectInput *input, u8 mode, s32 extra)` replaces
the zero-return placeholder in `conker/src/game/generated_17CAF0.c`. Original
`17CAF0.s`: VA15152B38..15152F70, ROM17FFE8..180420, 270 words, 176-byte
frame and nineteen relocation bindings. The 116-byte input record controls a
randomized count, fixed packet/header fields, two scalar ranges, two angular
ranges, a radius range, one header-byte range, one signed header-short range
and nine packet-byte ranges.

The routine draws the count first and keeps the live input pointer across every
provider and submission call. Each iteration fills a header and packet, obtains
the two direction angles and radius, asks `func_15143794` for the direction
vector, fills the nine randomized byte channels, and submits the pair through
`func_1515C2F0`. Mode is an unsigned byte; `extra` remains a full signed
32-bit argument. Unknown field meanings stay offset-based rather than receiving
speculative names. The draft in the adjacent alternate-source checkout was
used only as a recovery lead; all credited types, extents and behavior were
qualified against this repository's retail image and callers.

## Complete private scratch extent and direct bytes

The helper-visible packet ends at byte 58 but occupies a **60-byte** private
extent. The helper-visible header ends at byte 22 but occupies a **24-byte**
private extent. Four additional top-level tail bytes make the complete scratch
object **88 bytes**. Six total private tail bytes are untouched and are not
read by the qualified submission interface. Keeping those extents explicitly
preserves the retail stack layout without inventing scalar meanings.

The selected C emits all **270 retail words directly**, frame176, with every
relocation binding equal and **zero expected-word guards**. Raw payload SHA256:
`e0ec9c03e53dc37933fde31f8724b5903fc59e07babeab64894005606090736e`.
Original and C objects also agree after three independent GNU links with
shifted code and provider layouts. Fourteen divisor-trap words are unreachable
when the qualified range divisors are nonzero; all other 256 words execute in
the guest corpus.

## Fresh qualification

- Guest execution covers 256 cases / 512 original-versus-C runs, all 256
  reachable nontrap words, all 256 mode bytes, full 32-bit `extra` values and
  live input mutation after the first RNG call and after submission. Full
  memory/register/FP/call/payload/trace state agrees. The fired accesses yield
  261 equal access-prefix pairs; three independent GNU links separately prove
  relocation equality.
- Native32 runs 256 cases under each of O0/O2/O3 with UBSan. Eleven effective
  controls per profile reject altered unsigned RNG/count handling, header-byte,
  signed header-short, scalar, angle, random-byte, mode, extra, cached-input
  timing and scratch-extent behavior. The 116/60/24/88-byte extents and the
  untouched private tails are asserted.
- The aligned-ROM census finds exactly thirteen JALs in thirteen unique parent
  functions, with no aligned jump or literal target pointer. Every one of the
  110 bytes actually read has pre-call store evidence. Six callers supply
  `extra` with `LW`; seven use zero-extended byte or constant values. A
  conservative post-call V0 taint walk finds no return-value read, proving the
  recovered `void` contract. Complete parent execution is explicitly not
  claimed or credited.

Both tools copies contain byte-identical five-module qualification suites. The
shared suite passes all five methods against the installed production source,
object and image from the primary tools submodule and again after validating
the older mirror hashes. No gameplay or portable-uninitialized-byte acceptance
is inferred.

## Actual owner, image and production result

All 40 raw and padded `generated_17CAF0` neighbors and normalized pools remain
identical; owner compilation has zero diagnostics. The real owner recipe uses
five commands and produces the qualified 29,576-byte object. Protected Game
data remains exactly 189,088 bytes across 720 owners.

The strict complete-image predictor replaces the 12-byte placeholder slot and
symbol extent with the 1,080-byte target. It has zero exclusions and requires
no metadata reorder closure. All 6,052 addresses, 6,051 other bodies and the
complete named-definition multiset stay fixed. The production ELF equals the
independent prediction exactly.

Linked ELF SHA256:
`c3ac9a148dfa49ed6fae2cd5c04a37eed443128c4250acf69aa102511233bde3`.

The public qualification tools were committed first at
`5f21a43e1d4c03620965ade05207555d0f489295`. The retained stage is
`conker/build/game-composite-effect-factory-15152B38-match/`; it contains the
layout, guest, native, caller, owner, complete-image, installed and transfer
receipts. The root README changes only aggregate status rows; detailed recovery
stays here and in the five concise indexes. The scoped Graphify refresh is
structural AST only, retains all prior nodes and valid edge occurrences,
archives the obsolete s32 placeholder-return edge, and makes no full-corpus or
global-reclustering claim. No Claude call was needed.

## Next step

Audit adjacent `func_15152F70`, still a zero-return placeholder in the same
owner. Qualify its real ABI, callers, complete private extents and provider
ordering before attempting source fitting. Keep private candidates uncredited
until guest/native/caller, owner/actual-Make, strict-image, installed recount
and documentation gates pass.
