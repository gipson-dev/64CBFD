# Complete Actor Texture Tile Updater Qualified Schedule And Padding

Date: 2026-10-10

Target: func_1502F9FC, VA 0x1502F9FC..0x1502FBE8, ROM 0x5CEAC..0x5D098.
Continue [Note 1227](1227-game-actor-texture-tile-updater-recovery-and-layout-gates-20261010.md).
This is an isolated/copy-owner qualification, not production installation or
new matching credit. The wider Game matching goal remains active.

## Complete Compiler Form And Recipe

The halfword-indexed coordinate pointer retains the original second actor
stride calculation. Complete normal O2/g3 C now emits 120 words / 480 bytes,
the original 0x20 frame, no pool and no diagnostics; 120 real word differences.
The earlier 111-word recovery remains a historical semantic baseline.

The recipe retains every one of those 120 emitted producers exactly once and
copies three existing producers: the slot move and global-base HI/LO address
pair. It reorders independent instructions, renames closed register lifetimes,
and resolves branch destinations from producer labels. No memory-access
producer is copied, no producer omitted and no missing semantics supplied.
The coordinate LHU-to-LH promotion is exhaustively checked for all 65,536
halfwords through its modulo-16 addition before modulo-12 graphics fields.
This limited certificate alone is not an all-state instruction proof; the
independent ordered references, aliases, fault and rebase tests below are
required. The finite qualification is not hardware/trap acceptance.

All 120 input words and five input relocation dependencies are checked before
fitting. The 120 guarded rows use three physical insert-after positions to emit
123 words; these physical CSV positions are not the logical copied-producer
labels. Seven output relocation sites are derived from emitted provenance.
Actual padding, assembly and linking produce all 123 retail words byte-exact.
The copied symbol and slot are both 492 bytes, with no missing-body zero fill.

Authored tools:

- [layout forms](../../tools/experiments/game_actor_tile_updater_layout.py)
- [complete scheduling recipe](../../tools/experiments/game_actor_tile_updater_matching.py)
- [qualification suite](../../tools/tests/test_game_actor_tile_updater_match.py)

## Measured Qualification

- 1,024 cases / 3,072 executions compare complete original/raw/fitted bodies.
  Cover every word of the 123/120/123-word forms, every actor type, null roots
  and both stack phases. Independent ordered public reference; full private/
  public bytes, events, calls and access counts agree without normalization.
- 548 boundary cases / 1,644 executions cover signed/wrapped slots, coordinate/
  dimension wrap and bounded special-helper mutations/returned cursors.
- 85 unique alias cases cover live actor/texture/output/table-root replacement
  and private command buffers. Every one of 518 selected fault prefixes fires
  in each original/raw and original/fitted comparison, 2,072 failed executions.
  Compare full private/public prefix memory, events and calls. Missing fault
  fails; do not interpret absent output as a passed fault test.
- Twelve independent links over four entry/global/helper address sets pass
  1,056 cases / 3,168 executions, including both signed HI/LO carry directions.
  Rebased fitted/original words and full private memory/order agree.
- All 120 changed-word controls fail both recipe and actual padder guards.
  All five changed CSV relocation dependencies fail; mutate each actual object
  relocation too, rejected by both guard-row generator and actual padder.
- Complete native32 C using actual SDK macros passes 20,480 cases at each of
  O2/O0, 40,960 executions. All types/null roots, valid slots 0/25, four patterns
  and five alias layouts; independent little-endian reference. Three fresh
  native negatives fail at case 40 with code 5, bytes 196/193/199. Seven fresh
  complete IDO negatives are semantically effective and recipe-rejected.
  Wrapped invalid slots/table-pointer replacement remain guest-only evidence.
- Copied owner has zero diagnostics; all 37 neighbors, extents, relative
  relocations and pools remain exact. Isolated/owner target producers and guards
  agree. Actual padded owner changes only the 492-byte target; every relocation
  outside it remains exact, and all seven target sites match the recipe.
- Each original/raw and original/fitted pair passes 88 actual banked dispatcher/
  renderer/color/RGB/shading/identity-matrix cases, 352 connected executions
  across both pairs. Full connected private/public bytes/events/calls agree;
  independently check the updater's captured call/return boundary and reject
  a modeled updater substitute. Other callbacks, including the special helper,
  are still bounded here.
- All five original Note 1227 snapshots and corresponding production artifact
  hashes remain exact. Immutable baseline receipts and stale owner reject.

The scheduling suite and recent installation regressions pass 17 tests in
44.016s; make tools-check passes from the repository root. Invoking that target
inside conker was a command-scope error, corrected without editing its Makefile.
Initial fixture fixes were classmethod rebinding, assembler label/prelude
conversion and excluding the new target's seven relocations from the unchanged
neighbor-relocation comparison. No production bytes or snapshots were changed.

Final broader recovery/scheduling/install regression passes all 26 tests in
178.786s after the authored EOF cleanup. Nine documents / 4,131 relative links
validate with zero broken links. All three mirrors are exact and both copies
parse; older count 219/HEAD/fingerprints and all five snapshots/artifacts pass.

```sh
python3 -m unittest tools.tests.test_game_actor_tile_updater_recovery tools.tests.test_game_actor_tile_updater_match tools.tests.test_game_actor_renderer_install_match -v
make tools-check
```

## Bank And Resume

Tools f2dd1c3 commits the three new authored files before the consumer docs/pin.
Mirror only their previously absent paths into older tools, then remove the two
authored trailing blank lines identically in both copies. Older HEAD ddbdd16
and both tracked-dirty fingerprints stay unchanged; native dirty entries
216 to 219. No older-tools commit/reset, no push. Root README aggregate rows
remain unchanged: Game 2,762/4,816 (57.35%), total 3,435/5,489 (62.58%),
zero drift and 2,054 different.

Refresh native graphify after final code edits; preserve unsafe-shrink refusal,
retention, version and zero-node warnings. No force/purge/install. Check fresh
consumer-hook log growth and absence of workers before finishing.
Final native refresh exits 1, refusing 39,454 to 17,680-node shrink and retaining
19,398 nodes from 2,972 still-existing excluded files. Version mismatch and
devcontainer.json zero-node warnings remain explicit; no force/purge/install.

1. Connect the actual 52-word / 208-byte func_150C3160 body at ROM 0xF0610..0xF06E0.
   Count the instruction-comment lines, not labels/source lines; the initial
   56-word handoff estimate was corrected before banking.
   It performs floating division/conversion, integer division, actor-state write
   and one graphics command. Qualify both special types, zero/nonzero divisor,
   wrap loop, aliases and fired prefixes against an independent reference.
   Do not treat the current arbitrary cursor/mutation callback model as its
   semantics. Preserve explicit finite-value/FCSR/trap boundaries.
2. Only after that gate, install the complete selected body and all qualified
   guards, rebuild and audit the whole linked ELF against the unchanged five
   original snapshots. Measure fresh progress before giving matching credit.
3. Keep other callbacks, trigonometric/FCSR/trap/hardware/live acceptance and
   the separate threshold-curve gates from
   [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
   open. No OGL/Release/save/editor changes.
