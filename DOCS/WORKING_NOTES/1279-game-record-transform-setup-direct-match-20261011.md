# Game Record Transform Setup Direct Match

Date: 2026-10-11. Recover complete func_1503E3C4 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503E3C4..0x1503E5F8, ROM 0x6B874..0x6BAA8: 141 words / 564 bytes.
All 141 words emit directly under the existing O2/g3 owner profile, frame
0xD8. No guards, instruction drops, handwritten replacement, caller body,
header or compiler-recipe changes. Matching +1 only; conversion counts and
bytes unchanged. The full Game goal stays active.

## Baseline And Contract

Consumer f2326a2e954a173b50a60ee4a8dc4965a7266664 and mounted tools
1c81a02fb4d6aaf3b1133017b4631002c467f0b9 were committed at entry.
[Note 1278](1278-game-record-mask-teardown-guarded-match-20261011.md)
left this 141-word / 136-difference target. Inspect the complete retail body,
sole 171-word dispatcher caller, real types and owner profile after the
scoped Graphify query. Reuse IDO, structured ELF/object/pool parsers, existing
MIPS/native32 fixtures, GLOBAL_ASM post-processing and both production
padders. Codex is the sole writer; zero Claude calls, no bridge or installs.

Recover void func_1503E3C4(s32 slot, s32 index, s32 offset,
struct04 *record, s32 absolute). Retail establishes no status result. The
existing dispatcher already passes struct04 *, so its body needs no edit.
Keep the existing 104-byte struct04, 812-byte struct127 and 16-byte struct106.
Use a local float view of the record without redefining shared structures.

- Cache the original actor and record pointers. Add index + offset before
  the 64-byte stride and copy that actor-bank matrix into private +0x94.
- After bcopy, reread the full-width fifth argument from its incoming home.
  Any nonzero value skips the relative transform. Otherwise reread slot and
  index homes, live unsigned group +0xE and signed type byte. Only -1 skips;
  -2 is not this routine's sentinel. Invalid indices/slots are guest-only.
- On a relative transform, reread the bank on the cached actor. Invert the
  selected matrix into private +0x54; clear primary [1][3], [0][3], [2][3]
  and set [3][3] to one. Multiply primary * inverse into primary in place.
- Pass the matrix and nine output pointers to func_1503E5F8 using the full
  ten-argument O32 interface, including six stack arguments. Copy the first
  nine float fields to record +0x24..+0x44 in retail order.
- Read live actor coordinates after decomposition and the snapshot stores.
  Subtract actor x/y/z, then 30.0f from y. Preserve single-precision order
  ((x*x + y*y) + z*z), sqrt, zero-length fallback to one, reciprocal and
  direction stores +0x48/+0x4C/+0x50. Do not rewrite this as double math.

The adjacent 141-word func_1503E5F8 GLOBAL_ASM implementation stays intact.
func_150499A0 and func_150A7A48 remain separate C placeholders; executing
their retail instruction references in a test is not conversion credit or
qualification of those current C stubs.

## Direct Source Recovery

Initial semantic source emits 142 words / 126 differences, frame 0xD8.
Combining index + offset before pointer scaling recovers 141 words with nine
private matrix-address differences, all a four-byte local-home displacement.
Putting the meaningful type local before the matrix locals removes all nine.
No unused padding, artificial volatile, dead local or word normalization.
The typed struct04 * interface is also 141/zero/frame 0xD8. The compact
no-unroll diagnostic matches identically; O1/g3 and O1 do not match and are
not installed. This is a bounded candidate screen, not an exhaustive search.

## Fresh Qualification

New tools: experiments/game_record_transform_setup_candidates.py and
tests/test_game_record_transform_setup_match.py. Immutable before-inputs and
receipts: conker/build/game-record-transform-setup-match-test/.

- Thirteen complete pre-install tests pass in 43.380 seconds. All thirteen
  installed tests pass in 23.854 seconds. A final two-test literal-audit and
  integrity-control rerun passes in 7.971 seconds after documentation edits.
  All 4,372 relative links across seven checkpoint docs pass. Prior unchanged neighbor-suite
  receipts are historical, not described as freshly rerun.
- The 212-case retail/raw/padded matrix reaches all 141 target words. It
  covers full-width absolute values 0/1/-1/256/0x80000000, signed types
  -128/-2/-1/0/1/2/127, index/offset addition, groups, stack phases and zero
  length. Invalid slots/indices/type banks are explicitly mapped guest-only.
- Twenty-two callback/lifetime/public-alias cases distinguish live incoming
  homes, bank/group/index/absolute reads from cached actor/record identity.
  Position callbacks and all caller-saved GPR/FPR clobbers are qualified.
  Public aliases and two private matrix/record overlaps are guest evidence,
  not portable native alias or stack-home mutation claims.
- Two independent placements rebase seven symbols with HI16/LO16 carries;
  24 cases preserve all linked forms and private +0x94/+0x54 pointer shapes.
  The retail byte-field alias is relational D_800C666E = D_800C6660 + 14,
  not an independently fixed address.
- All 493 fired fault triplets preserve private/public memory, events and
  registers exactly. This qualifies emitted instruction order, not portable
  C fault semantics, hardware traps or FCSR behavior.
- Eight freshly compiled semantic controls fail on public results/call
  arguments: unsigned type, wrong sentinel, truncated absolute, cached bank,
  reversed multiplication, missing snapshot, missing height and missing zero
  fallback. Relocate longer controls away from real callee addresses; private
  frame differences alone cannot pass the effectiveness gate. Two stale
  installs and source/target/neighbor/extent/guard corruptions are rejected
  without mutating production inputs.
- Both copied owners pass GLOBAL_ASM post-processing and both real padders.
  All 21 neighbors, normalized pools, other slots/relocations, the 171-word
  caller and 141-word assembly decomposer remain unchanged.
- Native32 O2 and O0 each pass 1,728 bounded finite cases, checking all 26
  record words, nine output-pointer identities, bank/group/position callbacks,
  full absolute width and zero fallback. Three controls fail with actual
  mismatch receipts, not just a reduced-case-count exit. Callees are bounded
  diagonal-affine/decomposition models; no generic decomposition claim.
- Twelve cases execute linked retail bcopy plus original 166-word inverse
  and 76-word multiply instructions, with those hooks removed. All three
  target forms and the finite diagonal-affine reference agree. The remaining
  decomposition hook is a boundary model, not the full Euler implementation.
- Sixty-four cases execute the actual 171-word dispatcher, 27-word predicate
  and 141-word setup against an independent composed reference. Counts
  0/1/3/4, states 2/3, stack phases, position mutation, allocation, skipped -2
  elements, element flags and final state publication agree. Other callbacks
  and tail routines remain models, not complete gameplay acceptance.
- Twenty payload cases preserve all nine backup words, including signed zero,
  subnormal, infinity and NaN payloads. Finite/overflow directions compare to
  the ordered float reference. NaN directions compare emitted machine forms
  only: the host model canonicalizes sqrt NaNs, so no independent payload
  propagation or hardware/FCSR claim is made.

Initial harness issues were resolved before installation: missing relational
byte-field alias, negative-body/callee overlap, native warning/receipt shape,
incorrect assumed caller frame, fixture bank/type-table overlap, and NaN
reference versus oracle canonicalization. No production workaround, baseline
refresh or generic metadata exception was used to pass the checks.

```sh
python3 -m tools.experiments.game_record_transform_setup_candidates --profiles
python3 -m unittest tools.tests.test_game_record_transform_setup_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Linked Audit

Rebuild exits zero, retaining the existing duplicate generated_12D630 recipe
warning. Literal whole-ELF comparison changes exactly 445 bytes: 443 in this
target's slot and two function-size bytes, 12 -> 564. Every other byte,
function body/address/extent and metadata entry remains exact; no projection
or permitted permutation. All seven other inputs remain byte-identical:
guards, progress CSV, rodata assembly, symbols, undefined functions, layout
and Makefile. All old guard history, including the preceding spill pair,
is unchanged.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | f9e9a919dfbae01d337e9a7c5130e52d5f6f518070f8822f2dd72247535150ef |
| Source after | 7eb13c78160b463708784daeca18041496c8f48939092ce55c3636b93d86324f |
| ELF before | 25dd5c57a0dfcffa127574c1a9402176167c67cfe3b4ef1b74e93d5066b46d54 |
| ELF after | f464f3d3e466ee2be9c4a2b012d21475c48d2676f9e556823d109adc9d17ebf8 |
| Guards, unchanged | 75a00e8d566bd1f737d2d4bd2bbbc5c01eb7ec6c33f9789a422b5aa73bc1d5ed |

Fresh progress: Game 2,800/4,822 (58.07%), total 3,473/5,495 (63.20%),
Init 492/492 and Debugger 181/181. Zero drift / 2,022 still different.
Matching +1 only; root README gets aggregate rows, no recovery narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools 036e55c first, then this source, note, five current indexes,
aggregate README and exact consumer gitlink. No push. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 49 recorded fingerprints
stay unchanged. Only two absent files are copied with identical hashes;
dirty count 326 -> 328. Do not commit/reset its independent dirty history.
The target suite runs in the mounted consumer, not the standalone mirror.

Native graphify update . exits one on protective shrink refusal: 18,152
candidate nodes versus 39,931 saved. Preserve 19,398 nodes from 2,972 excluded
but still existing files; no force/purge/install. Version and empty-source
warnings are separate from compiler diagnostics. After consumer commit
require a fresh terminal Rebuilt, advanced log
bytes/UTC and zero rebuild workers, not just a hook-launch message.
Precommit hook-log baseline: 535,098 bytes.

Fresh live recheck: setup 141/zero and adjacent assembly decomposer 141/zero.
Next genuine placeholder: func_1503E82C, 138 words / 138 differences,
VA 0x1503E82C..0x1503EA54, ROM 0x6BCDC..0x6BF04, same owner. Inspect its
complete record transform/update contract and actual caller before recovery.
Keep the decomposer, earlier guards, inverse/multiply recoveries and deeper
callback/allocator/hardware/renderer/gameplay qualification separate and open.
No OGL Release build/change, private input/save or active editor/debugger
mutation. Keep the full Game goal active; no completion claim.
