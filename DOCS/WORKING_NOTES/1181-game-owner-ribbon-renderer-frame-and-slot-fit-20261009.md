# Game Owner Ribbon Renderer Frame And Slot Fit

Date: 2026-10-09

## Result And Boundary

Continue the same complete func_151B32C8 from
[Note 1180](1180-game-owner-ribbon-renderer-recovery-checkpoint-20261009.md).
The [fitting driver](../../tools/experiments/game_owner_ribbon_renderer_fitting.py)
now emits the full semantic renderer in475 words/1,900 bytes with its original
0x148/328-byte frame. It has243 real word differences, down from432.

This is still an uninstalled fitting checkpoint, not a byte match.
The production zero-return placeholder in
[generated_1E0560.c](../../conker/src/game/generated_1E0560.c) is unchanged.
Source, ELF, guards, progress and README aggregate rows are unchanged.
No matching/conversion credit and no new literal-word guards.

Baseline parent c6236066696fc5e6f8efbd9b0cc7895f062d1bde,
mounted tools5a824845eec6506127e518fdd48cd3595482710a; both clean before edits.
One Codex writer, zero Claude calls. No OGL/Release/save/editor work.

## Real Source Fit

- Enclose work in the successful vertex-allocation branch, retaining the common
  return. This removes the extra early-return branch/delay pair without changing
  lazy failure exits, callback ABI or public writes.
- Retain distinct ray, tangent, raw normal and scaled-offset values. Add the three
  actual squared-normal components, not unused locals or artificial stack arrays.
- Place the texture accumulator before the vertex cursor; the real induction
  local separates copied points from the origin pointer.
- Keep sync above the eleven material words, with bank/combine below them.
  Squared components and the magnitude/scale locals follow the material outputs.
- Use explicit independent zero-offset assignments and tangent-before-ray source
  assignments in the selected form. Preserve every floating multiply/subtract,
  squared-sum grouping, sqrt/division and truncated coordinate store.
- All nine segments,20 vertices,40 untouched vertex-flag bytes,27 own commands,
  fresh per-segment texture-step reads and unsigned wrapping remain qualified.

Selected form: retail-inputs-dx-dy-dz-rx-ry-rz, O2/g3.

| Private home | Retail and selected |
| --- | ---: |
| Vertex cursor |0x140|
| First copied point |0x134|
| Second copied point |0x128|
| Retained origin |0x120|
| Sync byte |0xEF|
| Material words |0xE8..0xC0|
| Bank / combine bytes |0xBF /0xBE|
| Saved S0..S4 / RA |0x70..0x84|
| Saved F20..F30 pairs |0x40..0x68|

The complete copied owner compiles with no new/preexisting warnings and target
output equals the isolated object. The actual existing padder now accepts the
1,900-byte target and emits it unchanged, without target padding or new guards.
This proves slot fit only; it does not authorize installing nonmatching output.

## Bounded Screen

43 complete source forms,46 profile/control rows;32 public-contract fixtures
per row (1,472 candidate executions). Zero compiler diagnostics and pool bytes
in all rows. No row matches retail.

| Candidate/profile | Words | Frame bytes | Differences | Contract failures /32 |
| --- | ---: | ---: | ---: | ---: |
| Prior recovery O2/g3 |477|304|432|Not this screen|
| Distinct offsets, allocated scope |475|312|301|0|
| Squared components, allocated scope |475|328|298|0|
| Top texture/induction homes |475|328|277|0|
| Material homes, low magnitude/scale |475|328|259|0|
| Explicit zero offsets |475|328|252|0|
| Selected tangent-before-ray O2/g3 |475|328|243|0|
| Selected O2 |475|328|335|8|
| Selected O1/g3 |605|248|597|0|
| Selected O1 |605|248|597|0|

The O2 row reorders triangle command writes on all eight rendering fixtures.
Reject that profile under the ordered public-write contract, even though terminal
memory alone could agree. Other measured forms are controls, not installation
candidates merely because their slot fits or bounded contract samples pass.

## Qualification

The [fitting suite](../../tools/tests/test_game_owner_ribbon_renderer_fitting.py)
reuses the full recovery contract with the selected complete C body, not a
geometry-only substitute. Final twelve-test run passes55.814s, zero skips.

- 512 guest cases/1,024 original/candidate executions: all original words,
 lazy allocation/material exits, flags, widths and texture-step aliasing.
- 385 mutation cases/770 executions: signed view boundaries, unsigned selector,
 retained origin, live material output widths and helper mutations.
- 7,680 actual native32 C cases: full actor, vertex and command bytes, ABI,
 finite binary32 geometry, UV wrap and aliases.
- Four independent symbol sets/eight links;64 cases/128 executions and all17
 original relocation uses preserved.
- 32 actual34-word installed material callback cases/64 executions;32 complete
 original348-word graphics walker cases/64 executions. Second callback/helper
 bodies and caller overflow/rollback remain outside this bounded qualification.
- Six effective semantic negatives,12 missing-byte fault cases/24 executions
 and three lazy fixtures. Guest fault prefixes are not portable hardware/FCSR claims.
- 16 owner neighbors, relative relocations and pools remain preserved. Actual
 padder emits475 raw target words unchanged.
- Final added coverage/preservation test:64 cases/128 executions, reaches all475
 words of each body and all12 incoming callee-saved FP words restored.
  Raw callback argument addresses also agree, directly qualifying all private
  material word/byte output pointers and the sync/resource cursor homes.

Initial harness failures: candidate generator saw a patched recovery seed,
then the profile screen correctly rejected reordered O2 writes; the added
seeded-FP check initially left the oracle's incoming preservation snapshot stale.
Correct setup and record rejected profiles; do not weaken preservation/write
checks or count failed suite runs as acceptance.

## Remaining Fit

Same-index differences by retail phase boundaries, not a semantic equivalence
proof or a license to replace words:

| Retail offsets | Phase | Differing / words |
| --- | --- | ---: |
|0x000..0x26C|Resource/material/graphics setup|30 /155|
|0x26C..0x380|Initial copies and geometry|67 /69|
|0x380..0x4CC|Initial vertex pair|64 /83|
|0x4CC..0x5D4|Loop copies and geometry|29 /66|
|0x5D4..0x730|Loop vertices and commands|53 /87|
|0x730..0x76C|Return/restore epilogue|0 /15|

Remaining differences include FP/GPR allocation, independent scheduling and
the original byte-offset plus two-pointer induction. Current source still
strength-reduces the loop differently. Same length/frame/homes alone cannot
certify those changes as closed allocation cycles.

Continue this same renderer:

1. Fit the initial shared actor+0x48 copy base and original loop induction.
2. Fit real FP normal/scale/offset lifetimes, retaining arithmetic operand order
   and exact public memory/callback/vertex/command order.
3. Prove any residual closed compiler allocation/scheduling changes before
   adding relocation-aware guards; do not synthesize retail instructions.
4. Install only after all475 linked words, owner/pool/relocation/protected data,
   guard history and full selected-body qualifications pass.

## Preservation And Checkpoint

Unchanged measured hashes:
source33a6690f6229713ead48a1ba2fb2d826cb268a28c889671d378b4a1e94e1179b;
ELF952b3100768e9ef8f6ff029c29bcfe1bba3bda03d66d6b97769b02313b77eac8;
guards6dd23d98d3c335a91a185500d9336765fe2e3966f00f74b166e8dce9bfa15d9b;
progress5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Protected Game data189,088 bytes/720 owners remains exact.
Game2,742/4,816 exact,total3,415/5,489,zero drift/2,074 differences remain the
unchanged Note1179 linked baseline, not a fresh matching increase.

Tools1b0e63354e21c088d586e6a0bb408f0707b97009 commits fitting and qualification
before the parent consumer pin.
Preserve all114 existing older standalone dirty entries and HEADddbdd16.
Mirror only two absent authored fitting files, yielding116; no older checkout
commit/reset/push. Existing tracked dirty-file hashes must remain unchanged.
Root README aggregates unchanged; detail belongs in this note and indexes.

Documentation validation:167 documents/4,498 relative links/zero broken.
All81 authored tooling files parse and have exact mounted/older mirror bytes.
The graph query still identifies the unchanged production placeholder at line75;
it does not prove installation. Explicit graphify update . exits1: it refuses
to replace the39,022-node existing corpus with a17,249-node extraction. Preserve
that fail-closed decision; no force/purge/install. Wait for the separate parent
post-commit hook and retain excluded nodes/local version/scan warnings.

Ignored receipts: conker/build/game-owner-ribbon-renderer-fitting/ and
conker/build/game-owner-ribbon-renderer-fitting-test/. Wider Game goal active.
