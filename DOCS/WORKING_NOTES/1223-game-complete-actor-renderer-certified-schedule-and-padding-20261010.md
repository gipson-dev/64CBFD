# Complete Game Actor Renderer Certified Schedule And Padding

Date: 2026-10-10. Continue the same complete renderer after
[Note 1222](1222-game-complete-actor-renderer-original-private-layout-20261010.md).
Consumer baseline dd3e6f12; mounted-tools baseline 755a04d.
Codex is the single writer, zero Claude calls. Keep tools-first authorized
commits, no push, no host/Release builds, saves or editor changes.
Previous goal turn is progress: original frame/private layout qualified and banked.

## Complete Emitted Schedule

func_1502CCFC: VA 0x1502CCFC..0x1502D54C, ROM 0x5A1AC..0x5A9FC,
532 words / 2,128 bytes; eight arguments and original 0x150 frame.
The complete portable C from Note 1222 still emits 531 words. Its original
frame, ten private colors, identity/tier/configuration/state homes and
saved-register lifetime remain unchanged.

[Certified recipe](../../tools/experiments/game_actor_renderer_matching.py)
uses only the complete compiler-emitted body and guarded relocation metadata:

- Close the count-pointer/fog-opcode/fog-global register cycle t2->t0,
  t0->t1, t1->t2 over its producers, consumers and callback spill/reload.
- Close the transient register cycle t6->t7, t7->t9, t9->t6 from the loop
  through tail producers. Preserve earlier live identity/table intermediates.
- Hoist the already-emitted custom-geometry LUI/ORI to their original positions.
  Their register's configuration-pointer use is finished before the hoist;
  no memory access is reordered.
- Omit only the emitted ANDI part-mask producer and bypass it at SLLV, which
  inherently masks to five bits. Keep part & 31 in portable C. Preserve the
  separate bit-one producer and all later transient uses.
- Duplicate the existing common B/LHU live-count exit into retail's separate
  null/non-null mode-3 arms. Both inserted words come from existing emitted
  branch/count-read producers; redirect the null edge to its own exit.
- Restore the independent count-pointer reload/fog-opcode schedule. Recompute
  all branch displacements and relocation positions after movement and edits.

531 complete expected-word guards normalize 122 words, omit one redundant
mask and insert two branch/read copies. The remaining 409 rows are unchanged
dependencies, including the omitted producer. No frame adjustment, missing
semantic body, ROM-word body replacement, unexplained padding or pool is used.
All 532 fitted words and all original relocation positions match exactly.

This is an isolated/copy-qualified byte match. Production still contains the
zero-return placeholder: no source, guard, linked ELF or progress installation
is claimed before native32 and actual-helper qualification.

## Fresh Qualification

[Schedule suite](../../tools/tests/test_game_actor_renderer_schedule.py):

```sh
python3 -m unittest tools.tests.test_game_actor_renderer_schedule -v
make tools-check
```

All eight tests pass in 32.405s after final code edits. Fresh tool checks pass.
An earlier complete run passed in 58.862s; the final run also fixes the new
three-body receipt arithmetic without changing historical receipts.

- Actual isolated padder and assembler emit exactly 532 words / 2,128 bytes,
  original frame, all original relocations and zero missing-body padding.
- 273 primary cases / 819 complete original/raw/fitted executions exercise
  all 532 original words. Independent public reference, full private/public
  memory and complete access events agree for all three bodies.
- The fitted body also passes all 16 incoming/private/public alias and mode
  mutation cases, and all 1,963 requested full fault-prefix pairs fire and
  agree in memory, events and calls. Guest prefixes are not portable C faults.
- Both full owner copies compile with zero diagnostics. All 37 neighbor
  bodies/relative relocations and normalized pools are exact; owner target
  instructions/guards equal the isolated candidate.
- Run actual owner asm postprocessing, pad the whole owner with the preserved
  guard prefix plus candidate rows, and assemble both copies. Only the target
  2,128-byte slot changes; complete text before and after it stays exact.
- Nine independent original/raw/fitted links and nine behavioral
  cases preserve all 532 fitted words, complete private memory/order, signed
  LO16 carries and separate virtual/physical matrix aliases.
- All 531 individually damaged words are rejected by the recipe and actual
  padder; all 47 damaged relocation dependencies are rejected by the padder.
- Three freshly compiled complete negatives are effective and rejected by
  the recipe: wrong custom fog bit, wrong primitive control and missing actor
  tail state. Earlier eight recovery negatives are unchanged prior evidence.
- Immutable production source/ELF/guards/progress/rodata baseline remains
  exactly equal to the previous recovery and private-layout baselines.

The first test setup lacked the existing CSV writer's fieldnames; add its
normal before-guards header initialization. A measurement snippet also shadowed
its function metadata variable. These were private fixture/measurement errors,
not production edits or grounds to weaken gates. The final focused run passes.

Renderer callbacks still use explicit bounded ABI/effect models. No complete
actual color/lighting/matrix helper execution, native32 SDK renderer,
FCSR/trap, hardware or live acceptance is claimed by these tests.
Matching remains Game 2,760/4,816 (57.31%), total 3,433/5,489 (62.54%),
zero drift / 2,056 different. Root README aggregate rows stay unchanged.

## Bank And Resume

Tools e59626e commits the two new authored files first. Mirror only their
previously absent paths to older tools. Older HEAD ddbdd16 and both tracked-dirty
fingerprints remain unchanged; native Git dirty entries rise 206 to 208 only
for those mirrors. Consumer commit banks this note, five concise indexes and
the new tools pin. No push or independent older-tools commit.

Before mirroring, the preceding scoped validator freshly passes seven documents,
4,075 relative links and both preceding authored mirrors with older count 206.
Fresh validation afterward passes seven documents / 4,080 relative links and
both exact new mirrors parsed in both copies; older count 208 and tracked-dirty
fingerprints remain exact. Old validators, baselines and receipts are not rewritten.
Manual graphify update refuses 39,417 to 17,636-node shrink, exit 1; retention
preserves 19,398 nodes from 2,972 excluded-but-existing files. Preserve version
and zero-node warnings; no force/purge/install. Verify fresh detached hook
completion and log growth after the consumer commit.

Continue this same full renderer:

1. Qualify complete portable C on native32 with the actual SDK graphics macros,
   exact command words/cursor/callback ABI, boundary shifts and effective negatives.
2. Connect the complete actual dispatcher/RGB/shading/renderer chain. Use the
   full original func_1502CC34 color-helper body/contract and actual matrix
   helper bodies; no bounded hook may stand in for a claimed recovered helper.
3. Install only afterward. Rebuild, audit the whole linked ELF/neighbor/data/
   guard history against this immutable baseline and measure fresh credit.

Keep the separate curve rejection gates from
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
and the wider Game goal open.
