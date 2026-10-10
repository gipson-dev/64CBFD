# Complete Game Actor Renderer Actual Color And Matrix Connections

Date: 2026-10-10. Continue the same complete renderer after
[Note 1224](1224-game-complete-actor-renderer-native32-sdk-qualification-20261010.md).
Consumer baseline f996409b; mounted-tools baseline e5f59e3.
Previous goal turn is progress: complete native SDK qualification was banked.
Codex is the single writer, zero Claude calls. Tools-first authorized commits,
no push. No host/Release builds, saves or editor changes.

## Actual Connected Bodies

func_1502CCFC: VA 0x1502CCFC..0x1502D54C, ROM 0x5A1AC..0x5A9FC,
532 words / 2,128 bytes; original 0x150 frame and all ten private color homes.
Complete portable C, matching recipe and production are unchanged.

[Connected fixture](../../tools/experiments/game_actor_renderer_connected.py)
executes the complete renderer with eleven actual bodies / 726 helper words:

| Function | Words | Provenance |
| --- | ---: | --- |
| func_1502CC34 | 50 | Complete original retail body; production is still a placeholder |
| func_1502EC34 | 150 | Banked ELF equals retail, including protected table/constants |
| func_1502C974 | 176 | Banked complete dispatcher |
| func_1502D54C | 57 | Banked complete RGB provider |
| func_1502D630 | 125 | Banked complete shading provider |
| func_150A7960 / func_150A7A00 / func_150A7A14 | 40 / 5 / 13 | Banked actual point-transform chain |
| guMtxF2L2 / func_151EFE00 / func_151EFE88 | 64 / 34 / 12 | Banked actual identity/fixed-matrix chain |

All ten non-placeholder helper bodies are checked against the actual ELF and
retail ROM, as are the fog helper's 36 table/constant bytes. The color helper
is deliberately not represented by its zero-return production placeholder.
Missing color, fog or identity helper bodies are rejected, not replaced by hooks.

The independent public reference derives colors from live view palettes,
parameters and the separately recovered fog semantics. Capture its active
memory through the structured read API so preceding bounded callback mutations
remain visible. Use a semantic packed-identity reference instead of the old
dummy matrix fill. Check all ten actual color output homes independently.
The original big-endian proof and native little-endian proof remain separate.

## Return-PC Qualification Boundary

Real helpers save their caller return PC, unlike the earlier bounded models.
Raw C call scheduling changes some return addresses by one word. This is a
real raw-body difference; do not describe raw private bytes as retail-exact.

Original and fitted executions remain exactly equal in complete private/
public memory, events, calls and access counts, without any adjustment.
For raw comparisons only, derive return-PC mappings from the already certified
emitted-word provenance in recipe_items. Adjust comparison copies only at
actual private SP-relative LW/SW of RA. Execution and original memory/events
are never rewritten. Retire a saved-home adjustment on any overlapping write.
All other private/public values and all event ordering remain strict.

A dedicated control observes eight changed saved-return access values in its
connected case, checks exact original/fitted bytes/events, writes identical
return-PC bits as an ordinary public scalar and proves that scalar is not
adjusted. The unrelated public change still fails the comparison.
This is not arbitrary private-memory masking or a byte-match claim for raw C.

## Fresh Qualification

[Connected suite](../../tools/tests/test_game_actor_renderer_connected.py)
adds eight tests. The final combined connected/native/schedule run passes
all 21 tests in 81.365s after final code edits; make tools-check also passes:

```sh
python3 -m unittest tools.tests.test_game_actor_renderer_connected tools.tests.test_game_actor_renderer_native32 tools.tests.test_game_actor_renderer_schedule -v
make tools-check
```

- 326 renderer cases / 978 original/raw/fitted executions. Exercise all 256
  fog modes, direct opacity 0/1/254/255, finite pointed-opacity clamps,
  signed/full-width views, two actor slots/pages and wrapped count 33.
  Check independent commands/cursor/public state and all ten private colors.
- 168 complete dispatcher/RGB/shading/renderer cases / 504 executions.
  Independently check caller RGB/alpha parameters, then renderer public state
  from its actual call-boundary snapshot. Both actual matrix chains execute.
- 18 private-parameter alias and live bounded-callback mutation cases.
  Mutate fog mode, palette, part mask or configuration before real color code.
- All 758 selected full connected fault-prefix triples fire: 2,274 failed
  executions across three complete renderer/caller paths. Complete original/
  fitted prefix bytes/events/calls agree; raw differs only at proven saved PCs.
- Three freshly compiled complete renderer negatives are effective: wrong
  color view, primitive control and actor tail state. Their unmodified positive
  case is checked against the same independent reference first.
- Five missing-real-helper controls reject modeled substitutes. The return-PC
  control also rejects ordinary scalar/public changes.
- Source, linked ELF, guards, progress and rodata remain exactly equal to the
  original recovery/schedule/native immutable baselines. No matching credit.

Initial fixture failures included a wrong aggregate helper-word expectation
and omission of shared helper rodata from one public reference input. Correct
those test inputs/arithmetic; rerun all positives and negatives. No renderer
source, fitting recipe or historical baseline is changed.

Other callbacks, including cosine, remain explicitly bounded. These tests do
not claim actual trigonometric execution, complete callback-table recovery,
FCSR/traps, hardware, native actual-helper execution or live gameplay.
Matching remains Game 2,760/4,816 (57.31%), total 3,433/5,489 (62.54%),
zero drift / 2,056 different. Root README aggregate rows are unchanged.

## Bank And Resume

Tools baacebd commits the two new authored paths first. Mirror only those
previously absent paths into older tools; native Git dirty entries rise
210 to 212. Preserve older HEAD ddbdd16 and both tracked-dirty fingerprints,
no independent older-tools commit/reset. Consumer banks this note, five concise
indexes and the tools pin; no push.

Before mirroring, the preceding native handoff validator passes seven documents,
4,086 relative links and its two exact mirrors, older count 210 and unchanged
tracked fingerprints. Fresh validation of this note/index set passes seven
documents / 4,091 relative links with zero broken links, both exact new mirrors
parsed in both copies, older count 212 and unchanged tracked fingerprints.
Manual graphify update refuses unsafe 39,430 to 17,649-node shrink, exit 1;
retention preserves 19,398 nodes from 2,972 existing excluded files.
Keep version and zero-node warnings, no force/purge/install. Verify fresh
detached hook completion and log growth after the consumer commit.

Continue the same renderer, including its required production dependency:

1. Recover the full semantic C body of the 50-word func_1502CC34 color provider.
   Qualify its original frame, argument spill, aliased outputs, conditional fog
   path, emitted layout and effective negatives against the complete body.
   Its production placeholder cannot remain beneath an installed renderer.
2. Qualify the combined copied owner with both recovered bodies and existing
   guard history, then install, rebuild and audit the entire linked ELF,
   neighbors/data/relocations against the preserved baseline.
3. Measure fresh matching credit only from that build. Keep cosine/other
   callback, FCSR/trap, hardware/live and separate curve rejection gates from
   [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
   open. The wider Game matching goal remains active.
