# Complete Actor Animation Selector Byte Match

Date: 2026-10-10

Continue [Note 1229](1229-game-complete-tile-updater-and-special-helper-byte-match-20261010.md).
Install complete func_1502FBE8. The wider Game matching goal remains active;
this checkpoint is not whole-game or host-port completion.

## Scope And Baseline

- Consumer starts at clean bddc62b9; mounted tools starts at clean 041a6fa.
  Single Codex writer, zero Claude calls. User's keep-committed authorization
  applies: tools first, then consumer source/guards/docs/tools pin; no push.
- VA 0x1502FBE8..0x1502FD70, ROM 0x5D098..0x5D220, 98 words / 392 bytes,
  original 0x40 frame. Owner conker/src/game/generated_58F80.c.
  Graph query located the placeholder and typed direct dispatcher caller;
  complete assembly, actual compiler and live source govern the recovery.
- Five immutable before-* snapshots: current owner, ELF, guards, conversion
  progress and protected rodata. Their hashes are asserted on each test run.
  Never overwrite earlier tile/helper snapshots to accommodate another target.
- Older standalone tools stays at ddbdd16, independently dirty: native Windows
  entries 221 before, 224 after three new absent-path mirrors. Both tracked-dirty
  fingerprints remain unchanged. No older-tools commit/reset, OGL/Release,
  editor, save or private-input changes.

## Recovered Behavior

Return without resource reads when pending selector +0x1C9 is zero. Otherwise
capture D_800D1588[actor.id] before reset/bounds checks. Pending 255 clears
itself and selects index zero, bypassing count/current gates. Other selectors
use pending-1 and reject index >= unsigned count +0x2C9 or equal current +0x1C8.

Read the unsigned animation byte from pointer +0x2C4 at that index. Invoke
func_150837D4 with signed low-word actor-minus-D_800CC2D0 divided by 0x32C,
truncating toward zero, the captured animation and zero. Preserve index,
animation and original resource across the callback; do not reload changed
selector bytes, actor.id or pending/count. Write captured index to current.

Read mode D_800C35EA; mode one clears D_800C3638. Reread target resource using
captured animation. Equal resources skip phase/count reads and animation
restart, retaining the already captured mode. Unequal resources read unsigned
actor phase +0x84 and unsigned D_800C5A90[animation]. Replace phase with 0xFFFF;
call func_1505E650 with phase zero when phase >= length, otherwise the captured
phase. Both branches use the full seven-argument mixed O32 ABI:
actor, phase, 1.0f, 0.0f, 0.0f, 0.0f, zero. Reload mode only after an actual
animation callback. Mode one sets D_800C3638 to one, then func_1507EABC(actor).
The function is void; early V0 contents are not meaningful zero-return credit.

## Complete C And Guards

Thirty-two source shapes measured. Initial complete C emitted 96 words,
original frame, 44 differences. Word-width retained animation/phase and
explicit mode reads in both callback branches emit all 98 words, original
frame, zero diagnostics/pool and only 14 differences. Normal O2/g3 is retained.

Four pending-register words and three phase-register words form closed lives.
Four spill offsets move retained animation/resource to their retail homes.
Three words reorder one constant producer and existing stores around a
register-only MFC1. Store order is unchanged. Every producer emits from the
full semantic C; no insertion, omission, missing-body fill or ROM-loaded recipe.
Full 98-word input and all 22 relocation sites are validated before guard
emission; all 98 deliberately stale word inputs reject. Append exactly 14
expected-word rows; none of the changed sites has a relocation.

Raw C's retained spill homes differ from fitted/retail homes. Independent
ordered references explicitly account for each layout; raw private bytes are
not falsely called identical to retail. Fitted and retail complete private
memory/events/calls/access counts agree, including intentional spill mutations.

Authored tools: [candidates](../../tools/experiments/game_actor_animation_selector_candidates.py),
[checked recipe](../../tools/experiments/game_actor_animation_selector_matching.py),
[complete qualification and linked audit](../../tools/tests/test_game_actor_animation_selector_match.py).

## Fresh Qualification

- 982 cases / 2,946 original/fitted/raw executions match independent full
  private/public ordered references. Every one of 98 retail words executes.
  Cover all pending/identity/animation bytes in mapped fixtures, unsigned
  halfword boundaries, seven signed/wrapped distances, callback mutations,
  retained captures and mode reload gates. Callbacks clobber caller GP/FPR.
  Mapped out-of-range table-byte fixtures do not establish real asset validity.
- Eighteen private/public selector and retained-spill cases / 52 executions.
  Every selected memory ordinal fires: 456 full fault-prefix pairs / 912 failed
  executions. Missing fault is failure; compare full prefix bytes/events/calls.
  Seven-argument observation peeks at outgoing homes without inventing guest
  load instructions. Twenty additional live mode/current and flag/resource
  alias cases / 60 executions prove live ordering under stores.
- Fifteen independent original/fitted/raw links: nine under three symbol sets
  and six for the two live global-alias layouts. Signed HI/LO carries and actual
  JAL entries are checked. The main rebase matrix passes 135 cases / 405 runs.
- Copied owner compiles/posts/pads with zero diagnostics. All 37 neighbors,
  including the typed direct-caller cast, keep identical bodies/extents/relative
  relocations; pools exact. Actual target padding is 392 bytes, not missing-body
  credit. Only its bytes and 22 new target relocation sites change in the owner.
- Seven fresh complete IDO negatives and three native negatives are effective:
  reset, count boundary, retained index, phase comparison, mode reload, float ABI
  and unsigned phase. Source changes cannot pass only because guards hide them.
- Actual banked 88-word dispatcher and complete 98-word target execute in
  96 cases / 192 runs. Full private traces and ABI match. All other callbacks
  remain bounded, not claims of actual animation/hardware execution.
- Complete native32 C at O2/O0 passes 34,750 cases each, 69,500 executions:
  all 26 valid slots and byte domains, unsigned phase/length, equal/unequal
  resources, five callback plans and 30 live selector/actor-phase/flag aliases.
  Separate little-endian reference; actual seven-argument float ABI checked.
  Invalid wrapped guest distances are not native portable-pointer acceptance.

Fixture corrections were explicit: call observation uses peek, not guest reads;
owner comparison permits exactly the new target relocations; native reference
indentation is unambiguous and selector mutation uses the captured index after
reset, avoiding a fixture-only negative array index. The installation audit
also correctly rejected the stale ELF when run before the broad link finished.
No baseline, historical receipt or acceptance gate was weakened.

## Installation And Bank

Full linked rebuild/progress generation succeed. Shared manifest triggers a
broad rebuild; existing duplicate generated_12D630 recipe, unrelated C warnings
and MIPS3 warnings remain. Target owner is diagnostic-free, not the whole build.
All nine final post-install tests pass in 10.888s; root tools-check and the older
copy's standalone tool checks pass. All three exact new mirrors parse.

Whole ELF audit permits only this 392-byte instruction slot and its symbol-size
update. All other bytes/addresses/extents remain exact, apart from established
symbol/string-table ordering normalization after complete headers and symbol/name
multisets independently match. The original 1,862,498 guard bytes remain an
exact prefix; append 14 rows. Current guard file is 1,864,867 bytes; the existing
CRLF-to-LF Git warning is preserved, not a broad line-ending rewrite.
Conversion CSV and protected rodata are byte-identical.
Protected data: 189,088 bytes / 720 owners / zero differing bytes, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Current qualified ELF SHA-256:
6c0827ef087761597743303aed7ac8be12dc49b3f15799c4ca1b4b0aff90450b.

```sh
python3 -m tools.experiments.game_actor_animation_selector_candidates
python3 -m tools.experiments.game_actor_animation_selector_candidates --focused
python3 -m unittest tools.tests.test_game_actor_animation_selector_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Fresh matching credit: Game 2,765/4,816 (57.41%), total 3,438/5,489 (62.63%),
zero drift / 2,051 different. Both gain one; conversion counts/bytes unchanged.
Root README updates aggregate rows only. Tools 0474fdc is committed first;
consumer source/guards/docs pin that revision. Mirror only the three absent
authored paths, preserving older HEAD and dirty fingerprints; no push.
Refresh native Graphify after final code edits; preserve retention/version/
zero-node/unsafe-shrink warnings, no force/purge/install. Verify fresh consumer
hook log growth and absence of workers before finishing.

Fresh handoff validation passes nine documents / 4,138 relative links, zero
broken links; three exact new mirrors parse in both copies. All five current
and six historical snapshots, guard prefix, progress, rodata and qualified ELF
remain exact. Native Windows Git confirms mounted tools clean; WSL reports
five existing nested tools submodules dirty (asm-differ, asm-processor,
mips_to_c, texture2c, ultralib), not the three authored files. Preserve their
pins and use the native Git boundary for this Windows checkout; do not reset
them to make another platform's status clean.
Native graph refresh exits 1, refusing 39,472 to 17,699-node shrink; retain
19,398 nodes from 2,972 still-existing excluded files. Existing version mismatch
and devcontainer.json zero-node warnings remain explicit; no force/purge/install.

## Next Target

Recover complete func_150837D4, still false zero-return C in generated_AEB40.c:
VA 0x150837D4..0x150838EC, ROM 0xB0C84..0xB0D9C, 70 words / 280 bytes,
original 0x30 frame. It is this routine's first callback, already used by other
banked actor code. Read the complete body/callers and qualify actual selector
connections before claiming callback acceptance. The final 28-word helper
func_1507EABC remains original assembly in generated_AB760.c; animation helper,
FCSR/traps, hardware, live gameplay and host-port acceptance stay separate/open.
