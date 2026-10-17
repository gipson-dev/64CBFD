# Actor Scale Timer Restoration And Match

Verified 2026-10-17. Consumer predecessor `402afd3f`; tools predecessor
`9a968aa`. Both active trees began clean. Note 1506's 42-word direct match
remains installed. This checkpoint restores the next 90-word routine in the
same owner; the broader Game goal and previously recorded matching gaps remain
open.

## Restored Function

`func_150F3214`, owner `generated_11FF10`, original `asm/11FF10.s`:
VA `150F3214..150F337C`, ROM `1206C4..12082C`, 90 words / 360 bytes,
frame `0x28`, five relocations.

- Validate the linked owner at actor offset `0x110`: active word, matching
  **byte** epochs, then non-null model pointer at owner offset `0x1D4`.
- Call `func_15143134` with the original point, actor position output, and
  model matrix at `0x3C0`. Its established interface has three arguments.
- Compute scale from the square root of the float timer and its multiplier;
  preserve the `0x30` then `0x2C` store order.
- Store the low byte of the original unsigned conversion of
  `base - decay * time * time`, preserving ordered float32 operations.
- Reload and advance the timer by `D_800BE9A4`; return zero only when the
  limit is ordered-less-than the updated timer. Unordered comparison returns
  one, unlike a rewritten `time <= limit` predicate.

The alternate draft was a reference, not an accepted donor: it contains word
loads for byte epochs, integer accesses for floats, and an extra call argument.
The restoration retains the original symbol and a concise purpose comment;
the byte field is not given an unproven subsystem name.

The semantic C emits 90 words under the existing O2/g3 profile. **88 words are
literal retail words**; two exact expected-word guards preserve commutative
`MUL.S` operand order at `0x78` and `0x98`. No frame, home, load/store order,
branch, conversion sequence or relocation is patched. Raw SHA-256:
`3efe468b63f0a9436c368dacf6e7bf31fa889355cf20c0f965d8efcfa68a42e9`.
The padded routine matches all 90 words. All 11 raw/padded neighboring
functions and normalized owner pools remain unchanged.

The rejected initial source had frame `0x38` and 15 differences. Direct
returns and repeated owner/model expressions recover the retail frame and
private homes. Redundant pointer locals, alternate declarations, typed-record
forms, and reversed multiply expressions did not improve the complete match.
Their bounded screens remain reproducible in the candidate tool.

## Qualification

Seven pre-install tests pass in 13.367s. Seven final installed tests pass in
16.170s, including the separate historical-test followup described below.

- 2,688 core guest cases, 36 modeled FP-edge cases, and 50 alias/provider-home
  mutation cases reach **all 90 retail words**. Rejection gates leave later
  inputs unmapped to prove lazy access.
- 820 selected access-fault prefixes compare retail, raw and padded complete
  modeled private/public state. Opaque provider accesses are excluded.
- Three independent rebased links pass 48 cases, varying high/low address
  halves across signed HI16 carry boundaries and rebinding the call target.
- Native32 O2/O0 each pass 1,536 typed-object cases with UBSan, byte canaries,
  call-argument checks, and six effective timer/width/decay negative controls.
- A signed-cast native negative was ineffective after final byte truncation
  on the valid domain; it was rejected and replaced, not counted as a control.
  The initial native case-count assertion was likewise corrected to the actual
  loop product, rather than changing production code.
- The callback table at `0x80089D50` / ROM `0x22E810` points to this routine
  and is a protected input. No complete dispatcher or transform-callee
  qualification is claimed. The transform is an explicitly opaque provider.

The existing bounded conversion model supplies CFC1/CTC1/CVT.W.S behavior;
a local square-root instruction handler is exercised across the corpus.
FCSR save/restore is checked in the model. Hardware exceptions, general FCSR
fidelity, NaN payload propagation, and portable C semantics for invalid FP
conversions or private-stack mutation are not claimed. Native tests use only
defined finite conversions and typed objects.

## Complete First Image

The code-only metadata proposal was rejected before any accepted initial
prediction existed. Its private-link witness is archived in
`game-actor-scale-timer-install/rejected-code-only-metadata.elf`.
The link revealed two exact symbol serialization swaps:
`D_8008CC0C/D_800A1260` and `D_800A1950/D_800A1580`.
The predictor checks exact names, definitions, attributes and pair permutations;
there is no blanket metadata exclusion.

The accepted initial prediction accounts for **267 changed ELF bytes**:
**237 code + 2 target-extent + 28 metadata**, zero exclusions. The normal
production build matches that complete prediction byte-for-byte:
`5efb8a9f598af0712d97eaf4d0f2ab2df134e349ad16eddfeb0f75e74128b7d4`.
The immutable `initial-prediction.json` SHA-256 remains
`45f26931531c47054386dc061e13cc31d7cf3fadc78ccf0e8561fde0e855a822`.

All 6,057 bodies and addresses are audited: only this target body/extent
changes; every address remains fixed. All 189,088 Game-data bytes / 720 owners
remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
All predecessor guard bytes, including existing mixed line endings, remain
unchanged; exactly two rows are appended mechanically. Compiler profiles,
conversion rows and all other protected inputs remain unchanged.
The freeze protects 261 entries / 240 distinct paths.

The first prediction has six exact before/after members. A later older
actor-state test exposed a raw guard-manifest comparison that also needed the
historical view. Its one-line test-only successor is stored separately in
`FOLLOWUP`, with exact before/after hashes; the six-member first prediction
and production image were **not rewritten**. Fourteen effective fixture
corruption controls cover both records. All nine affected historical checks
pass freshly in 35.937s. Earlier broader receipts are reused, not called fresh.

## Bank And Resume

Tools **e033fe7** banks the candidate, image predictor, checkpoint and tests,
plus narrow historical adapters, before the consumer source/docs/pin.
Both tools copies pass their 12 shared checks and smoke checks; 16 ASCII/AST
parses and eight byte-identical task pairs pass. Copying verifies exact
predecessor hashes first. Preserve 1,124 unrelated mirror hashes, 1,132 dirty
paths, and mirror HEAD `ddbdd16b`. No mirror commit/reset, push, Claude call,
host-port or frozen Release action. Finish the owned post-commit Graphify
worker before closing.

Fresh matching: Game **2,964 / 4,828 (61.39%)**; total
**3,637 / 5,501 (66.12%)**; 1,864 different, zero address drift.
Nominal conversion counts remain unchanged because the old placeholder was
already represented as C. Root README changes only aggregate matching rows.

- [x] Restore all 90 words with the original frame and two multiply guards.
- [x] Pass full target, affected historical, first-image and tools-copy checks.
- [x] Preserve neighbors, data, guard history, immutable predictions and mirror.
- [ ] Recover `func_150F2D14`: 288 words, frame `0x150`, same owner,
  VA `150F2D14..150F3194` / ROM `1201C4..120644`. Start with the complete
  owner-epoch gate and state-triggered record emission. The draft contains
  wrong-width accesses and explicit conversion artifacts; do not import it as
  a qualified match. Preserve the halfword invalidation store at actor `0xE`.
- [ ] Keep the 139-word `func_150F2A60` gap, both fade lifetime gaps and wider
  Game goal open. No host/gameplay completion follows from this checkpoint.

```sh
python3 -m tools.experiments.game_actor_scale_timer
python3 -m unittest tools.tests.test_game_actor_scale_timer -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
