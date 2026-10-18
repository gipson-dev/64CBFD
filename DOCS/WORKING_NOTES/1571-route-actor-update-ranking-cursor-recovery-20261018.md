# Route Actor Update Ranking Cursor Recovery

Date: 2026-10-18. **Private source recovery; not installed; zero matching credit.**

## Result

Continue the same `func_15087350` from
[Note 1570](1570-route-actor-update-frame-and-save-layout-recovery-20261018.md).
Consumer baseline is `b7d97e6a`; tools baseline is `c767262`. Bank the new
tools first in **21db626**, then the consumer pin and this handoff. No push.

Target: generated_B3020, VA `15087350..15087CC0`, ROM `B4800..B5170`.
Retail requires **604 words / frame 456 (0x1C8)**, with the recovered interface:

```c
void func_15087350(s32 recordIndex, s32 active, f32 lookAhead);
```

The new selected complete C emits **594 words / frame 456**. A separate
score cursor, an explicit current-score capture and the indexed next-score
read recover **five words in the ranking tail only**. All earlier call-anchored
block lengths remain unchanged. Original GP/FP save slots and incoming homes,
the first 15 literal words and final 11 literal words remain intact.

It is still **10 words short / 481 positional word differences**, including
the missing words. The difference count has not improved: do not describe the
five-word extent gain as five newly byte-exact instructions. There is no
normalizer, instruction insertion, frame guard, padding or installation.

The selected source is `game_route_actor_update_extent.selected()`, named
`rank-cursor-current`. It reuses the dead record-bank cursor for the later
score-array pass, retaining the full-width modular offset gate, signed bound,
stable strict-less-than ordering and all three explicit float-to-s32 casts.
It introduces no volatile qualifier or narrower conversion domain.

Raw SHA-256:
`423ef8706eab06a130de88369c7b23596c1bf9e62f3da6caa915a7a6a0600320`.
The 70 relative bindings have canonical SHA-256:
`76dd7ba3dc3e16f662369c343b107ae67f362ae608efa54848615712a3e3721a`.

## Extent Diagnosis

Anchor the complete body at its 20 actual static helper calls and the tail.
The static call sequence must agree before comparing blocks; a changed-call
control rejects the comparison. Shape alignment omits physical registers and
private offsets for diagnosis only. It is not matching or instruction rewriting.

| Block | Retail Words | Old Raw | New Raw | Remaining Extent Difference |
| --- | ---: | ---: | ---: | ---: |
| 3: correction through advance | 83 | 82 | 82 | +1 |
| 4: through event submission | 14 | 15 | 15 | -1 |
| 13: coordinate conversion / static-branch join | 81 | 74 | 74 | +7 |
| 19: projection / state / finalizer gate | 75 | 73 | 73 | +2 |
| 20: ranking through return | 114 | 108 | 113 | +1 |

All other block lengths agree. Blocks 3 and 4 cancel; calls through the first
306 words retain their offsets. Equal lengths do not establish equal words,
registers, local homes, access order or branch-delay behavior.

Retail's three moving-coordinate conversions each store and reload a shared
private s32 word at SP+0x48 before the halfword output. The selected raw C still
omits those six accesses. They explain six of block 13's seven missing words;
the join schedule also differs. The shared spill's original source cause is
not established. Do not invent a volatile original type to force it.

Nineteen bounded source screens preserve all 72 other owner bodies and pools:
four conversion forms, four spill controls, four explicit-ranking forms, four
cursor forms and three typed-cursor forms. The diagnostic volatile ID/word
union reaches 597 words / frame 456, but is not selected. Direct float-to-short
emits the old 589 words yet narrows C's defined conversion domain, so is also
not selected. The explicitly captured two-value / independent-index forms
grow the frame or change the original save layout. Typed separate-cursor,
record-reuse and actor-reuse forms remain distinct controls, not installation
candidates. Full source/object/command receipts remain in the ignored build.

## Fresh Qualification

**All 15 tests pass in 58.419 seconds, no skips.**

- Re-run 703 paired complete-routine cases with 494 actual helper words and
  the independent ordered-binary32 reference. Compare complete public RAM,
  canonical provider calls and saved ABI: 216 core, 80 effectful-provider,
  319 signed-lap/ranking, 16 index/actor and 72 active/tick cases.
- Add 12 wide-coordinate cases outside signed-16 range but inside the finite
  signed-32 conversion domain, in both stack phases. Retain the explicit
  conversion before narrowing; this is guest evidence, not native32/UBSan.
- Pass six bounded numeric-provider error-limit witnesses and 16 actual retail
  caller windows, including real argument/delay words and poisoned-V0 consumers.
  Complete callers and unknown indirect interfaces remain outside the proof.
- Run 228 additional paired guest cases over all 19 source screens. Keep these
  separate from the selected-point cases and older Note 1570 screen receipts.
- Seven newly compiled semantic negatives produce ordinary wrong results or
  call contracts, not crashes or exhausted execution budgets.
- All 594 raw-word and 70 binding mutations fail the selected fingerprint gate.
  A normal-profile before/after compile preserves 72 neighbors, pools and the
  strict projection override; existing primary/normal flags remain unchanged.
- Re-fire 34 opening access prefixes: 28 agree / six reject. Both phases still
  first reject at cut 14 / PC `150873A4`, with GPR14/GPR24 different while RAM,
  FPRs and accesses agree there. Full private-state or hardware-trap equality
  is not claimed. Original local array/scalar homes are still not restored.

A repeated-run bookkeeping failure was caught before banking: the test summary
used the same `cursor-screens.json` name as a source-screen bank. Regenerate that
bank with unchanged source, rename summaries to `selected-cursor-*.json`, and
assert all five screen-bank byte strings remain unchanged after qualification.
The 15-test result above is after this fix. The earlier 14-test pass alone was
not sufficient repeatability evidence. A separate repeat of the 19-screen
test also passes in 23.695 seconds, with all five input banks preserved.

## Bank And Resume

Tools **21db626** first. The two new files are byte-identical, ASCII and
AST-valid in both tools copies. Both copies pass three repository-setup tests
and project-tool smoke checks; consumer `make tools-check` passes. Preserve all
1,284 previous dirty mirror leaf hashes and its `ddbdd16` HEAD. Add only the
two absent task files: 1,286 dirty paths, no mirror commit or reset.

All 23 protected production/reference inputs remain frozen. The installed
Note 1568 whole-ELF audit is freshly rechecked and passes. The completed older
588-word compiler capture is audited, not repeated; no debugger launch or
new capture is needed. No production Make/build, guard, source, progress or
root-README change. Carry forward Note 1568's installed **Game 2991/4828**,
**total 3664/5501**, **1,837 different / zero drift**; no fresh recount or credit.
No Claude call, emulator, host edit or frozen Release action.

```sh
python3 -m tools.experiments.game_route_actor_update_extent
python3 -m tools.experiments.game_route_actor_update_extent --qualify
python3 -m unittest tools.tests.test_game_route_actor_update_extent -v
python3 -m tools.experiments.game_route_actor_update_frame --audit
python3 -m tools.experiments.game_route_record_integration --audit
```

The suite reuses the screen artifacts. Regenerate them separately with
`--conversions`, `--spills`, `--ranking`, `--cursors` and `--typed` when needed.
Keep these sources and the qualified594 point separate from Note 1570's
strict589 point. Never rerun the completed `--capture`.

Next continue **this same function**: establish the source cause of the shared
conversion word, restore the remaining projection/join and ranking extent,
then repair argument temporary roles and private homes/access order. Finish
native32/UBSan, aliases/private prefixes, all-word/binding proof, actual mixed
padding/Make, independent GNU rebases, first whole-ELF prediction, installation,
protected-body/data/address audit and fresh recount before claiming a match.
Preserve the installed setup/vector/spline/dispatcher baseline. Game stays open.
