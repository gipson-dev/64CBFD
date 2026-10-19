# Actor State Tick Spill Ownership And Cached Timer

Date: 2026-10-19. Consumer predecessor: `78ae6221`; tools predecessor: `59b52f1`.
Tools checkpoint: `8a650a3`, committed before this consumer documentation/pin.

## Measured Boundary

Continue complete **func_1508A6FC**, VA `1508A6FC..1508B194`, ROM
`B7BAC..B8644`, from [Note 1617](1617-actor-state-tick-homes-and-ordered-reads-20261019.md).
This checkpoint qualifies an **experimental post-compile spill transform**.
It does not recover eleven additional homes directly from C, install a body,
add production guards or earn matching credit. Both raw and transformed bodies
retain **678 words/frame 288 and 600 real aligned word differences**.

[The experiment](../../tools/experiments/game_actor_state_tick_spills.py)
checks the complete source-word and binding fingerprints before changing any
words. Seventeen previously recovered scalar/table homes remain fixed. Eleven
cursor or call-save slots are mapped by their actual lifetimes:

| Role | Raw Source SP Offset | Retail SP Offset |
| --- | --- | --- |
| Reset cursor | A4 | 84 |
| Status cursor | A0 | 60 |
| Band cursor | 9C | 5C |
| Cached timer row | 74 | 7C |
| Cooldown row | 6C | 74 |
| State row | 60 | 6C |
| Event row | 5C | 68 |
| Action row | 50 | 54 |
| Event byte around SIGNAL | 58 | 64 |
| Cached actor action around ACTION | 80 | 104 |
| Draw actor around TEXT | 114 | 8C |

These are mappings of emitted operands, not a new source-debug home claim.
Saved GPR/FPR storage at SP+20..4C and outgoing stack arguments stay fixed.

## Timer And Pointer Origins

On the timer-reset path, raw source word 396 reloads the captured timer-table
base from SP+C4; word 399 rebuilds the row address with the current byte offset.
Retail instead reloads the cached current-row pointer from SP+7C. Those are not
equivalent if an opaque helper has changed the table-base home during this row.
The experimental transform loads the saved row pointer into T5 at source origin
396, omits the now-unneeded pure ADDU at 399, and retains the real public timer
read at source origin 401. It does not replace that read with a literal value.

The same transform materializes the folded other-actor bias after source origin
363. A derived ADDIU applies -0x658 to the actor address; the two coordinate
loads then use +14/+1C rather than -644/-63C. Their effective 32-bit guest
addresses are unchanged. This is a machine-address identity, not an assertion
about portable C pointer provenance or whole-function fault equivalence.

The complete checked origin map retains **677 unique source instructions**,
omits only source 399 and derives one pointer-bias instruction. Every original
memory-instruction origin survives once, although the private pointer load at
396 intentionally changes its source home. Relative branches are retargeted;
no branch/call/return is separated from its delay slot. All **62 relocation
entries** follow their retained source origins. Resolved binding fields are
copied only through their HI16/LO16/26 masks, never through unrelated opcode or
register bits. Stale input, bindings, linked fields and recipe output reject.
No retail instruction array is used as a transform input.

Three source-only cached-address alternatives are also retained in the screen:
byte pointer, pointer/integer roundtrip and word address. They emit 676 words
with frame 288 and the seventeen old homes. They are rejected, not selected;
the source candidate remains Note 1617's complete body and actual timer read.

## Fresh Qualification

[Nine tests](../../tools/tests/test_game_actor_state_tick_spills.py) pass with
no skips: **12.990s primary / 15.369s mirror**. Each copy compiles the complete
semantic source separately and derives its own experimental output.

- All 262 ordinary fixtures compare retail, raw source and transformed output
  against the independent state-machine model: calls/arguments, public stores,
  public memory, result, ordered public reads and restored saved GPR/FPR state.
  The corpus visits 660/678 retail words; it is not complete instruction coverage.
- All 56 effective alias pairs cover the seventeen existing homes and eleven
  mapped spills in both stack phases. Every requested mutation fires, and every
  retail alias changes the observed public behavior/read trace versus its plain
  fixture. Transformed output agrees with retail on these observations.
- All 22 old-layout negatives for the eleven new mappings reject raw output
  after the requested mutation fires. Unmapped guest accesses in a negative
  are not treated as hardware fault acceptance.
- Two timer-reset/table-home aliases distinguish the cached row from the
  rematerialized address. Both transformed runs match retail and both raw
  controls reject. The fixture explicitly requires the real timer-zero store.
  An initial negative timer did not enter reset and was an ineffective control;
  the final fixture starts current timer at 5 and alternate timer at 19.
- Two fired draw-index aliases deliberately still reject the transformed
  candidate. Retail saves/reloads the draw index at SP+A0 around TEXT; source
  keeps the reused slot in S0 and has no equivalent pair of private accesses.
- The zero-count path deliberately confirms another open boundary: transformed
  source stores reset/status/band cursor homes although retail skips those
  stores. Public observations agree, but private memory does not.
- Three synthetic resolved-field patterns retain every relocation's new
  position. These are mask/origin checks, not independent GNU rebase acceptance.

Both project-tools smoke checks and four-file Python syntax checks pass.
The seven pinned production inputs remain byte-identical. Note 1617's native32
and complete-owner/72-neighbor receipts are reused for the unchanged C, not
reported as freshly run or as native validation of the emitted transform.

## Still Open

Do not install this partial transform or generate broad production guards.
Missing draw-index accesses, count-branch store scheduling, saved-register role
lifetimes and whole-function scheduling remain unresolved. At a later STATUS
call, retail's S0/S2/S3 offset/slot/actor roles differ from source S3/S0/S2;
S6/S7 latch/elapsed roles are also exchanged. A global rename would corrupt the
already-correct physical save/restore interface; recovery must respect lifetimes.

Private-memory/PC/fault-prefix equivalence, remaining all-input aliases, FCSR,
complete instruction coverage, independent original-assembly/GNU maps, actual
padding/Make/strict first image and installation/recount gates remain open.
This checkpoint narrows spill ownership; it does not lower the 600 differences.

## Preservation And Resume

Only the two absent task files were copied into the independent tools mirror.
Its HEAD `ddbdd16b` and all **1,440 older dirty leaf hashes** remain unchanged.
No mirror commit/reset/stash/clean, push, dependency change, advisory-agent call,
host edit or frozen Release operation was performed.

An early absolute-path IDO invocation truncated an output path at its first
space and overwrote scratch `C:\Users\grego\OneDrive\Desktop\.vscode\Conkers`.
The user confirmed it was disposable scratch. No recovery is needed; subsequent
compiler inputs/outputs use the corrected relative-path invocation from conker.

Production C, retail assembly, guards, ELF, Makefile, progress and root README
are unchanged. Installed totals are the prior Note 1614 checkpoint, not a fresh
recount: Game **3,017/4,832**, overall **3,690/5,505**, 1,815 different/zero drift;
owner **69/73** exact. Production A6FC remains its 12-byte stub/665 classified
differences; do not confuse that with the experimental body's 600 differences.

```text
Raw source: 260a9fc2acbfa79a5348dda1a6589ca3ac73b81ea6aeda4c90798a4f9c52fb51
Transformed: 0752133c823e166b2ab230f03e59b5665d10ca099ccb676b93b0a8acd9f3f9d9
```

Ignored receipts live under
`conker/build/game-actor-state-tick/lifetimes/homes/spills/`, including source
controls, normalized words/bindings, primary and mirror tests, input snapshots
and tools-check logs. The consumer hook refreshes Graphify; preserve and audit
all prior excluded-but-existing nodes when closing this checkpoint.

Next: recover the draw-index spill and count-branch private store schedule,
then lifetime-scoped saved-register roles and complete instruction scheduling.
Keep the wider Game goal active and the production installation gated.
