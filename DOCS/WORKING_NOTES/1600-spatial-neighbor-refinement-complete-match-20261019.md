# Spatial Neighbor Refinement Complete Match

Verified: 2026-10-19. **func_15086098 is installed and all179 linked words
are byte-exact**, including its112-byte frame and716-byte slot.
VA15086098..15086364, ROM B3548..B3814, generated_B3020.
Consumer predecessor ebfaf5ac; tools predecessor94acbb1. Tools checkpoint
**342de47** banks the four new qualification files before the consumer
source/guards/docs/tools-pin commit.
No push. This supersedes [Note1599's experimental boundary](1599-spatial-neighbor-refinement-semantic-recovery-and-matching-boundary-20261019.md).

This is a **guarded match, not direct compiler identity**. The selected complete
C retains index S0 but emits176 words/frame120 with139 differences. Both owner
profiles emit identical target words/bindings. The real padder applies176
expected-word/relocation guards, retaining174 unique source origins, omitting
two dead/redundant words and inserting five explicitly derived words. All11
relocation bindings survive. No compiler profile, Makefile, original assembly,
literal pool, volatile declaration or physical-register C binding changes.

## Behavior And Live Return

The C uses descriptive position, node, coordinate, projection, minimum and
selection names while retaining the address-based export and a concise purpose
comment. Its seven-argument interface is verified from the full routine and
three actual callers. Count/option are signed low bytes; the selected/refined
index remains a full32-bit result, with255 as the sentinel.

Always call the height-band and closest-node helpers. For positive count and
a non-sentinel index, try record containment with truncated integer XYZ. A
contained record, or squared doubled radius above the loaded threshold, uses
the direct refinement/override path. Otherwise cache the post-helper node
table/threshold and scan all five neighbor bytes.255 skips one entry, not the
whole scan. Signed16 X/Z deltas define a normalized forward line, with no
segment-end clamp. Retain the first strictly positive projection/strict distance
minimum. Refine the original index and accept that result only when it equals
the selected neighbor. Preserve helper effects and list/state store order/alias.

The directly used **func_15086C70** now returns `s32` and explicitly returns
func_150A3194's live V0. Its old `void` declaration discarded an actual observed
result. The corrected wrapper still emits the same20 words under both owner
profiles; its complete80-byte slot and every other owner body stay fixed.
No implementation/credit is claimed for the still-unfinished refinement/FIND
providers. Opaque-provider fixtures are contracts, not full-engine execution.

## Source-Derived Recipe

The selected source is Note1599's outer-object form. Moving that real temporary
to the function scope recovers index S0; it does not introduce a dummy effect.
The normalizer rejects any change to the704-byte raw body or its11 bindings.

1. Restore frame112, original incoming count/option/list/state homes, refined
   home60 and selected home58. Keep RA54/S050, the six FP pair homes20..48,
   matching save/restore order and actual register lifetimes. A frame-only
   control overwrites the caller's incoming list word, even on count0.
2. Recover X/Z F28/F30, minimum F26, projection F24, original F22 preservation,
   and Y/base-Z's nonoverlapping F20 reuse. Restore the signed-coordinate
   access schedule and closed GP/temporary-FP roles, including the two
   commutative residual additions and node-address operand order.
3. Move the threshold load to its original lifetime, use F12 for the radius
   comparison, and insert the two original minimum copies into F26, including
   the unreachable duplicate. Rematerialize the source's1.0 LUI/MTC locally
   into F8 for each valid neighbor instead of retaining a saved F30 constant.
4. Omit the dead duplicate coefficient MTC and the hoisted integer5 load.
   The counter is explicitly initialized0, incremented once per neighbor,
   runs through1..5 and has no loop helper. Its strength-reduced `!=5` test
   therefore permits the original SLTI/backedge. Reuse one source delay NOP
   for the test and insert its branch-likely/join copy, preserving both paths.
5. Split the rounded projection SUB into base-dot NEG plus current-dot ADD,
   retain the operand/multiplication schedule and insert the extra R4300
   multiplication hazard NOP. Together with the two minimum copies and extra
   loop-test copy these are exactly five inserted words:176-2+5=179.

All source origins are unique except the explicitly named inserted operations.
No runtime ROM read or literal179-word replacement body is used by the recipe.
Guard rows preserve the historical CSV prefix and check every original source
word and relocation before emitting the qualified result.

```text
Raw:        42926261351a97b64a3293f7f2e93db283fe1db84c512b9cf1a9e70549321c85
Normalized: 2a5e43a59df60d6015c1653cebc7cb0842f641681c3a2d3db3a23eb0d218620a
```

## Fresh Qualification

**Eight installed tests pass in37.435 seconds**, without skips. Pre-install
qualification also passed all eight in33.085 seconds:

- 103 fixtures/two stack phases produce206 completed retail/normalized/raw
  triples. Retail and normalized agree in every GP/FP/LO value, condition,
  complete private/public memory, ordered accesses/stores, physical/logical
  helper calls and visited PCs. All three agree with an independent public
  reference. Raw agreement is not a raw private-state claim.
- 572 fired own-access cuts compare the same complete retail/normalized
  states before the requested access. Each gate is confirmed fired at its
  requested count. Include early exits, no neighbors, geometric selection,
  contained/aliased state, direct-radius/full-word result and mutated helpers.
- Fixtures visit175/179 retail words. The unsigned-byte conversion correction
  at150861A0/A4/A8 and dead minimum copy at150861F0 remain present but unvisited.
  Frozen threshold100,000,000 cannot be exceeded by a byte's squared doubled
  radius; controlled threshold fixtures exercise that branch without changing
  production data. Do not claim all179 words were executed.
- Native32 O0, O2 and O2+UBSan pass all103 fixtures without sanitizer
  diagnostics. Thirteen compiling behavioral negatives exit21..25 for width/
  sign, equality/tie, stop-on255, four-neighbor, signed-coordinate, refinement
  acceptance, dropped record-return and stale-table errors. Integer casts use
  finite bounded inputs; nonfinite geometry fixtures avoid the integer-cast
  path. Arbitrary invalid node indices are not a native backing guarantee.
- 187 stale raw-word/binding controls reject every changed raw word and all11
  changed relocation specifications. The explicit five-counter-value proof
  qualifies the loop condition. The frame-only negative returns but overwrites
  incomingSP+14, the caller's list word; it is not accepted as a matching fix.
- 24 connected runs execute71 actual words across the height, live record
  wrapper and containment wrapper. Check bands2/128/255, live V0 and all seven
  float query-packet fields. The deeper FIND/query providers remain opaque.
- 96 runs execute the real22-word1509A6A8..1509A6FC seven-argument caller/
  result-consumer window and its five-word epilogue, with the480-byte caller
  frame as an explicit live-in. Check cached-byte setup, stack argument words,
  result publication and fresh post-helper category lookup. This caller
  supplies count0; do not claim full-script or positive-count caller coverage.
- Three independent GNU maps give30 rebased raw/normalized pairs and literal
  equality to independently assembled retail. Move code, all five helpers,
  both globals and backing; retain all11 bindings, including HI/LO carries.
- Completed list/state and list/global-pointer-byte alias triples preserve
  public helper/store order. Both whole-owner profiles preserve72 neighbors,
  all pools and all73 addresses. The real padder and seven-command Make shadow
  emit the same qualified object. Its existing normal-profile override still
  supplies only func_150891E8; no new override is added.
- Four strict complete-image corruption controls and two actual padder stale
  CSV controls reject changes. The installed image equals the independently
  predicted first link, not merely an image with selected sections excluded.

An initial test incorrectly inspected fixture memory before the model
initialized incoming argument words. Correcting that setup confirms the
frame-only corruption; the fixture error was not a production defect. The
initial failed receipt was not counted as a passing suite.

Shared tools checks and syntax checks in both tools copies pass. The older
standalone mirror HEAD ddbdd16 and all1,383 pre-existing dirty leaf hashes are
preserved. Only four absent task files were copied; no mirror commit, reset,
stash or clean. Prior unchanged neighbor-suite receipts are reused, not reported
as freshly rerun. No Claude call, REA setup, dependency change, hardware/FCSR
execution, real-save operation or frozen host Release operation was involved.

## Exact Production Image

The initial target-only prediction exposed one closed symbol/string ordering
change: adjacent `D_8009D9D0` and `func_150A3FC4` records exchange order. The
existing serialization helper validates the exact contiguous original records,
strings and field definitions before performing that single declared swap.
Canonical named symbols change only func_15086098's size12->716. No entire
metadata section is ignored and no other symbol value/type/size changes.

The **578 changed bytes** close exactly:537 target-code bytes, two target-size
bytes,17 symbol-order bytes and22 string-order bytes. The actual production
Make build reproduces the predicted3,257,636-byte ELF. Every one of6,056 other
bodies and all6,057 addresses are fixed, including the corrected wrapper.
Protected Game data remains189,088 exact bytes across720 owners, zero changes.
Original assembly, data, Makefile and conversion CSV remain unchanged.

```text
Source: 1ea8523c2148a3603e5fb04c2699952822166a403a4568c2228d74153e3fcbf1
Guards: 754763e55d3731701d31c0b53fc3f672b366bde617412ebf38872c77625c79d1
ELF:    e8d1f53395dcf4b35dc4eb38b49b019a00bb11443694e3e6b0604deb67026e24
```

Fresh matching: **Game3,010/4,832 (62.29%)**, **total3,683/5,505 (66.90%)**,
**1,822 different/zero drift**. Init492/492 and Debugger181/181 remain exact.
Owner **62/73 exact,11 remaining**. Conversion stays5,505/6,044 (91.08%) and
86.08% bytes. Root README changes only the two matching aggregate rows;
function narratives remain in docs. Commit tools first, then consumer source/
guards/docs/pin. No push.

## Resume

Next: **func_1508BC20**, the shortest remaining owner nonmatch:189 words,
frame136,184 differences, VA1508BC20..1508BF14, ROM B90D0..B93C4. Freeze this
installed baseline, inspect its full assembly and actual callers, and recover
the complete interface before another qualified match. The other ten owner
nonmatches, including func_15086364, remain separate unfinished work. Keep
the wider Game goal active, not complete after this individual match.

```sh
python3 -m unittest tools.tests.test_game_spatial_neighbor_refinement_match -v
python3 -m tools.experiments.game_spatial_neighbor_refinement_integration --audit
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
make tools-check
```

Ignored frozen inputs, compiler objects, original padded owner, source-origin/
private/native/caller/GNU receipts, Make shadow, initial serialization diagnosis,
first link, installed build/audit/test log, remaining-owner inventory and graph
before/after audit live under `conker/build/game-spatial-neighbor-refinement/matching/`.
