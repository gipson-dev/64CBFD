# Game Owner Ribbon Renderer Induction And FP Proof

Date: 2026-10-09

## Result And Boundary

Continue complete func_151B32C8 from
[Note 1181](1181-game-owner-ribbon-renderer-frame-and-slot-fit-20261009.md).
The [induction driver](../../tools/experiments/game_owner_ribbon_renderer_induction.py)
retains 475 words /1,900 bytes, frame 0x148 /328 bytes and all recovered private
homes. Its selected O2/g3 form scale-reuse-dz has 163 raw word differences,
down from 243. A separately certified 13-word FP-field-only remap leaves 151.

Neither body is installed or byte-exact. The false zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.
No new literal-word guards or matching/conversion credit. Source, ELF, guard
manifest, progress and README aggregate rows remain unchanged.

Baseline parent d017a31fbcd8d43e8078289ddcdfe69ce12bfcee,
mounted tools 1b0e63354e21c088d586e6a0bb408f0707b97009; clean before edits.
Single Codex writer, zero Claude calls. No OGL/Release/save/editor work.

## Source Recovery

- Replace two squared-normal temporaries with a real actor+0x48 point-base
  pointer. Inline the same squared products, preserving arithmetic operand order
  and grouping. The remaining squared-Z temporary is actually used.
- Reuse the dead tangent-Z local for the scale after computing the cross product.
  Preserve distinct raw/scaled normal values, magnitude/sqrt/division and stores.
- All geometry/resource/material/helper logic and ordered public writes remain
  intact: nine quads, 20 vertices, 40 untouched flag bytes and 27 own commands.
- Initial T0=0x18 and S2=0xF0, byte-offset counter and two advancing pointers now
  emit directly from C. Loop opens with lw at,0(t1), then increments T0 and A3
  by 0x18; closes with bne t0,s2,loop and T1+=0x18 in its delay slot.
- Full target length/frame, cursor/point/origin/sync/material homes, saved
  S0..S4/RA and FP20..31 lifetimes remain qualified.

45 complete source forms, 32 ordered public-contract fixtures each: 1,440
candidate executions, zero failures, zero compiler diagnostics and pool bytes.
No screened form matches retail. This screen is bounded evidence, not exhaustive
behavioral acceptance or a reason to install another nonmatching form.

| Representative form | Words | Frame bytes | Raw differences |
| --- | ---: | ---: | ---: |
| Prior fitted body |475|328|243|
| One squared temporary replaced, loop base |475|336|238|
| Two squared temporaries replaced, shared base |475|328|189|
| Scale reuses dead tangent X/Y |475|328|200|
| Selected scale reuses dead tangent Z |475|328|163|
| Selected with ray-first assignments |475|328|187|

Typed m2c output is reference-only. It still has unresolved types, pointer-unit
increments and bitwise struct casts; it is not an installed or qualified C body.
One initial generator assertion expected the old ray-first source layout; fix
the transformer for the current tangent-first seed, without changing the contract.

## Closed FP Allocation Certificate

Normalize only architectural FP operand fields, not operation bits, GPR fields,
immediates, memory addresses, branch targets or ordered arithmetic operands.
The initial lease permutes F26/F28/F30 over offsets 0x288..0x380; the loop lease
exchanges F28/F30 over 0x4CC..0x5D4. Exactly 13 instruction words change.
No retail instruction constants are used to generate the remapped instructions.
Shape/zero/induction checks reject stale compiler output before certification.

Paired symbolic provenance checks every ordered FP input before assigning fresh
result tokens. FP-to-GPR and FP-store inputs must agree, keeping GPR/public memory
equality inductive. Explore both FP-branch paths over the fixed nine-iteration
loop; reject unexpected calls, control flow or counter/limit changes. The unchanged
restore tail must close every FP register lifetime.

Measured certificate: 1,024 paths, 313 reached words, 260,868 symbolic steps,
13 changed words. It closes 12 retail differences; zero initialization still
differs in scheduling. The certificate proves raw-to-normalized allocation
equivalence for the checked body, not full retail equivalence or hardware/FCSR
and gameplay acceptance.

An unsafe alternative initial permutation changes the same 13 words and passes
the shape gate but fails on a live FP operand mismatch. Three additional stale
frame/zero/counter mutations also fail. Do not count a no-op negative as detection.

## Full Qualification

The [induction suite](../../tools/tests/test_game_owner_ribbon_renderer_induction.py)
passes all fourteen tests in 62.407s, zero skips. It reuses the complete recovery
contract with the new selected full C body, not a geometry-only substitute.

- Raw guest: 512 cases /1,024 original-candidate executions; all 475 words reached,
  flags/lazy exits/texture-step aliases and hostile volatile/outgoing-home clobbers.
- Raw mutations: 385 cases /770 executions; signed view boundaries, retained
  origin, unsigned selector, live geometry/width/step and full-width helper outputs.
- Actual native32 C: 7,680 cases, full actor/vertex/command bytes, ABI, aliases,
  untouched flag bytes, finite binary32 geometry and wrapping texture coordinates.
- Independently assemble original and link both objects under four symbol sets:
  eight links, 64 cases /192 original-raw-normalized executions; all 17 relocation
  uses retained. The remap works on independently rebased candidate instructions.
- Raw actual installed 34-word material callback: 32 cases /64 executions.
  Raw complete original 348-word graphics walker: 32 cases /64 executions.
- Six effective compiled semantic negatives. Adapt late-origin injection to the
  new points-base assignment and assert every control actually changes source.
- Raw missing-byte faults: 12 cases /24 executions and three lazy fixtures.
  These compare public call/write prefixes, not portable C fault semantics.
- Raw all-word/private-home/saved-FP check: 64 cases /128 executions. Every one
  of the 12 seeded incoming callee-saved FP words is restored; raw callback
  argument addresses agree for every resource/sync/material output home.
- Repeat guest, mutation, actual material/walker, faults and all-word/saved-FP
  qualification with the entire normalized 475-word body and identical case
  counts. Native32 qualifies the source body, not a separate normalized C source.
- Copied actual owner: 16 neighbors, relative relocations and pools preserved;
  zero existing/new warnings. Raw target equals isolated output. Actual padder
  accepts 1,900 bytes and emits the target unchanged, without padding/new guards.

Second material callback body, full helper implementations, caller overflow/
rollback, SDK/FCSR/hardware/live rendering/gameplay remain separate open gates.

## Remaining Fit

Same-index differences at retail phase boundaries are diagnostic counts only,
not proof that corresponding words can be substituted:

| Retail offsets | Phase | Raw | FP-normalized | Words |
| --- | --- | ---: | ---: | ---: |
|0x000..0x26C|Resource/material/graphics setup|30|30|155|
|0x26C..0x380|Initial copies and geometry|24|18|69|
|0x380..0x4CC|Initial vertex pair|47|47|83|
|0x4CC..0x5D4|Loop copies and geometry|10|4|66|
|0x5D4..0x730|Loop vertices and commands|52|52|87|
|0x730..0x76C|Return/restore|0|0|15|

Continue this same renderer:

1. Fit the initial second-point loads to retail's shared actor+0x48 base rather
   than the current actor-relative +0x60/+0x64/+0x68 loads.
2. Fit remaining initial-copy/zero and geometry scheduling, helper setup and
   vertex/command GPR allocation without changing ordered public effects.
3. Certify any residual closed transformations before relocation-aware guards;
   never synthesize whole retail words or weaken the qualified contract.
4. Install only after all 475 linked words and full owner/pool/relocation/data/
   guard-history/source qualifications pass. No match credit before that point.

## Preservation And Commits

Unchanged SHA-256:
source 33a6690f6229713ead48a1ba2fb2d826cb268a28c889671d378b4a1e94e1179b;
ELF 952b3100768e9ef8f6ff029c29bcfe1bba3bda03d66d6b97769b02313b77eac8;
guards 6dd23d98d3c335a91a185500d9336765fe2e3966f00f74b166e8dce9bfa15d9b;
progress 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.
Protected Game data remains exact: 189,088 bytes /720 owners,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Game 2,742 /4,816 exact; total 3,415 /5,489, zero drift /2,074 different remain
the unchanged installed baseline, not a new matching increase.

Mounted tools 5a069ec8192680c4ba41c745640742db9ab5426d commits driver and suite
before the parent documentation/tools pin. No push requested/performed.
Preserve older standalone HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a
and all 116 preexisting dirty entries. Mirror only the two absent authored files;
118 entries result. No older-checkout commit/reset/push; tracked dirty hashes
must remain unchanged. README aggregate rows stay unchanged; detail lives here.

Ignored receipts: conker/build/game-owner-ribbon-renderer-induction/ and
conker/build/game-owner-ribbon-renderer-induction-test/. Documentation/link,
authored-file parse/mirror and scoped Git checks accompany the consumer commit.
Validation passes: 168 documents /4,509 relative links /zero broken; all 83
authored tooling files parse and match the older mirror byte-for-byte. Older
HEAD and both tracked dirty-file hashes remain unchanged; all 116 original
dirty entries are preserved, with only the two intended new files added.
Graph query still sees the production placeholder; retain existing corpus and
wait for the incremental post-commit refresh rather than forcing a shrink.
Wider Game matching goal remains active.
