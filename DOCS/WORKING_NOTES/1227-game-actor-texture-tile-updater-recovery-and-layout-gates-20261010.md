# Complete Game Actor Texture Tile Updater Recovery And Layout Gates

Date: 2026-10-10. Continue the same renderer dependency after
[Note 1226](1226-game-actor-color-provider-and-complete-renderer-byte-match-20261010.md).
Consumer baseline 3a571bfd; mounted-tools baseline cc74178.
Previous goal turn is progress: two complete bodies installed and byte-exact.
Codex single writer, zero Claude calls. Authorized tools-first commits, no push.
No host/Release builds, saves or editor changes.

## Complete Retail Contract

func_1502F9FC: VA 0x1502F9FC..0x1502FBE8, ROM 0x5CEAC..0x5D098,
**123 words / 492 bytes**, original 0x20 frame, saved s0/RA.
Initial 124-word arithmetic included the next function's first instruction;
correct it from actual assembly boundaries before accepting coverage/layout.

[Complete candidate](../../tools/experiments/game_actor_tile_updater_candidates.py)
returns a Gfx cursor and receives signed slot. Actor stride is 0x32C.

- Actor types 0x89 and 0xBA delegate commands and actor pointer to
  func_150C3160, then preserve its returned cursor.
- Select texture row 14 for type 0, 7 for 0x96, 4 for 0x28,
  5 for types 1..4, otherwise 0.
- If D_800C5338[type] is null, return the original cursor without commands.
- Otherwise emit two SDK gDPSetTileSize commands, tiles 5 and 4.
  Read live actor coordinate pairs at 0x27A/0x27E, then advance two bytes.
  Add two to each signed coordinate. Read unsigned width/height at
  row offsets 8/10 of a 12-byte record, multiply by four and subtract two.
  Preserve 16-bit conversions and final 12-bit/3-bit command fields.
- Re-read the table root and actor/record fields for each iteration.
  Earlier command stores can change later inputs when output overlaps them.

Reuse the owner's existing ActorDisplay58F80 and ActorSegmentRow58F80
definitions in isolated compilation. The copied owner needs only its typed
function prototype, special helper prototype and complete body.
Production [generated_58F80.c](../../conker/src/game/generated_58F80.c)
still has the zero-return placeholder. No guards, source, ELF, progress or
rodata are installed/modified in this checkpoint.

## Physical Layout Boundary

Selected O2/g3 emits 111 complete words / 444 bytes, frame 0x20, no data pool,
zero diagnostics, 118 actual word differences against the 123-word retail body.
The complete behavior is present; this is not a byte match.

IDO reuses the first actor-address calculation instead of retail's second
calculation. Register allocation, signed-halfword versus equivalent truncated
unsigned-halfword loads and scheduling also differ. Do not describe the gap
as only two independent scheduling words or fill it with opaque retail words.

Measure nineteen full-body source forms at O2/g3 and O1/g3: 38 forms,
none byte-exact. Additional exploratory profiles are not final match proof.
Structured indexing, signed second index, coordinate-base placement, local
widths and count forms do not close the layout. Candidate records are retained
under conker/build/game-actor-tile-updater-test/shapes.json.

Actual copied-owner padding preserves the 492-byte address window but exposes
a 444-byte function symbol plus 12 trailing zero words. Those zeros are ordinary
slot padding, not recovered behavior or matching credit. Recover/certify the
original instruction length and register/schedule shape before installation.

## Final Qualification

[Nine new tests](../../tools/tests/test_game_actor_tile_updater_recovery.py):

- 1,024 primary cases / 2,048 original/compiled executions: all 256 types,
  null/non-null roots, both O32 stack phases, every original 123 and compiled
  111 instruction reached. Full private/public memory, events, access counts,
  calls and callee-saved lifetime agree; independent ordered public reference.
- 548 boundary/callback cases / 1,096 executions: signed/full-width wrapped
  slots, signed-coordinate and dimension wrap, zero/changed special cursors
  and live callback mutations.
- 85 aliases / 170 executions: live actor coordinates, texture rows, public
  output and table-root replacement; map the resulting guest root explicitly.
  Two private output-buffer cases additionally check actual command bytes.
- All 518 selected full fault-prefix pairs fire: 1,036 failed executions.
  Compare full private/public prefix bytes/events/calls; missing fault fails.
- Seven freshly compiled complete IDO negatives are effective: row, type gate,
  inset, width, tile index, count and null gate. Check unmodified positives first.
- Complete native32 C with actual SDK macros passes 20,480 cases at each of
  O2/O0, 40,960 executions. All types, null roots, slots 0/25, four coordinate/
  dimension patterns and five live actor/texture/output alias layouts.
  Separate explicit little-endian reference; native pointers/actor width checked.
  Three fresh complete native negatives return 5 at case 40, bytes 196/193/199.
  Guest table-pointer replacement and wrapped invalid slots are not native proof.
- Copied-owner before/after compile and actual postprocess/padding have zero
  diagnostics. Target equals isolated body; all 37 neighbors, extents,
  relative relocations and pools remain exact. Only copied target window changes.
- 88 full dispatcher/renderer cases / 176 executions use actual banked
  dispatcher, renderer, color, RGB, shading and identity matrix bodies.
  Original/compiled tile executions agree in full connected private/public
  bytes/events/calls, without saved-PC adjustment. Independently check the
  tile routine at its captured call/return boundary. Reject modeled tile substitute.

The full final new/recent-install regression run passes all 17 tests in 66.202s,
and make tools-check passes. The previous renderer's actual linked audit is
freshly rerun, not merely reused.

```sh
python3 -m unittest tools.tests.test_game_actor_tile_updater_recovery tools.tests.test_game_actor_renderer_install_match -v
make tools-check
```

Fixture corrections: off-by-one retail length/coverage; distinct texture rows
for effective wrong-row control; actual padded symbol/window distinction;
missing SDK macro dependency and C token spacing; width assertion scope;
reference filtering for private output events. An imported TestCase alias
initially caused unintended duplicate tests; use its module instead.

A receipt initially collided with baseline.json after checking all five hashes.
Recover the original manifest from verified untouched before-* copies, matching
the original captured hashes exactly. Rename the receipt unchanged-production,
reject baseline as a receipt name, and check all five snapshot/live hashes.
No historical snapshot or production bytes are changed to accommodate tests.

Special func_150C3160, cosine and other callbacks remain explicitly bounded.
No actual special-helper, full callback-table, trigonometric, FCSR/trap,
hardware or live-game acceptance claim. Connected proof checks complete tile
semantics and its boundary, not an independent whole-renderer replacement oracle.

## Bank And Resume

Tools c5df5cc commits both new authored files before consumer docs/tools pin.
Mirror only those previously absent paths into older tools. Preserve older HEAD
ddbdd16 and both tracked-dirty fingerprints; native dirty entries 214 to 216.
No older-tools commit/reset, no push. Root README aggregate rows are unchanged:
Game 2,762/4,816 (57.35%), total 3,435/5,489 (62.58%), zero drift / 2,054 different.

Fresh validation passes eight documents / 4,121 relative links, zero broken
links, both exact new mirrors parsed in both copies, older count 216 and
unchanged HEAD/tracked-dirty fingerprints. All five original snapshots and
production artifact hashes remain exact.

Local graph lookup confirms the production placeholder at generated_58F80.c:1201.
Graph is navigation only; actual assembly/compiler/snapshot evidence governs.
Refresh native graphify after final code edits, preserving unsafe-shrink refusal,
retention, version and zero-node warnings. No force/purge/install.
Manual update exits 1, refusing 39,446 to 17,665-node shrink and retaining
19,398 nodes from 2,972 still-existing excluded files. Keep the original graph.
Verify fresh detached consumer hook completion/log growth before finishing.

1. Continue this complete 123-word updater, not only its special/empty gates.
   Close original actor-address recalculation, LH/LHU selection, register cycles
   and instruction schedule with a complete compiler form or certified emitted
   producer/relocation recipe. Do not insert missing semantic behavior.
2. Qualify original/raw/fitted private memory/order, aliases, fired faults,
   independently rebased links and every stale recipe dependency. Connect actual
   special helper separately rather than assume its bounded model is complete.
3. Only then install, rebuild/audit the whole linked ELF against these immutable
   snapshots and measure fresh matching credit. Keep hardware/live and separate
   curve gates from [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
   open. The wider Game matching goal remains active.

