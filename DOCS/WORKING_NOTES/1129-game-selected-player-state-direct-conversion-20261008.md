# Game Selected-Player State Direct Conversion

Date: 2026-10-08

## Result

Continue [Note 1128](1128-game-record-player-mask-direct-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
func_151D87E0 to complete C in
[generated_205C90.c](../../conker/src/game/generated_205C90.c).
All **34 words /136 bytes**, frame **0**, emit directly under existing
IDO 5.3 O2/g3. No guards, filler, pools, data, profiles, headers or Makefile
changes. Reference [205C90.s](../../conker/asm/205C90.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_205C90/func_151D87E0.s)
remain untouched. VA0x151D87E0..0x151D8868, ROM0x205C90..0x205D18.

Already exact assembly becomes semantic C; every linked instruction remains
unchanged. Only this 136-byte conversion row changes from the prior baseline.

## Recovered Contract

s32 func_151D87E0(u8 mask) scans four unsigned byte player indices in order.
Only selected bits read D_80084060[player]. A selected mapping>=4 returns0
immediately. A valid selected D_800BE944[index] nonzero returns1 immediately.
Otherwise continue and return0. Invalid-first and ready-first outcomes differ;
ignoring invalid entries is not equivalent. Nonselected and later entries
remain unread after an early return.

The routine is leaf/frame0, with a byte mask and byte counter/index.
Retail writes the raw incoming A0 word to its argument home before masking
to eight bits. This is an emitted-instruction contract, not permission to
access arbitrary stack or invalid C pointers. Globals are read-only, and
the semantic result is normalized integer0/1. Preserve four symbolic
HI16/LO16 global relocations.

Actual retained func_151D8868 passes owner+5 in the JAL delay slot, after
D_800E0B94's disable gate. It branches on the predicate result. No production
caller change is needed.

## Source Fit And Qualification

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_selected_player_state_candidates.py)
retains thirteen complete forms. Selected byte prototype, old-style byte
argument and int mapped-index local all match. Int player emits67 words/
63 differences; wide mask30 words/33 differences; explicit byte increment
34 words/two differences. Zero compiler diagnostics in every retained form.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 34 | 0 | 0 |
| O2 | 32 | 0 | 33 |
| O1/g3 | 34 | 0x8 | 32 |
| O1 | 34 | 0x8 | 32 |

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_selected_player_state_match.py)
reuse existing Triangle/ProgressReference, strict native32, owner, parser,
relocation and padder helpers. No shared helper change.

- **173,184 guest cases**:65,536 mapping-byte cases,40,960 full-byte-mask
  cases,65,536 flag-byte cases and1,152 explicit raw-A0 cases. All34 words
  reached; two SP phases and four upper-register patterns. Compare the
  independent ordered result/trace/memory reference and complete selected/
  retail GP/FP equality. Raw upper patterns are instruction evidence, not
  additional C-parameter range.
- Six lazy cases prove empty-mask, invalid-first and ready-first exits without
  mapping future entries or unnecessary state bytes. Twenty-four required
  fault prefixes compare the argument-home write and selected map/flag reads
  against the independent reference, in two SP phases. These are bounded
  instruction-order tests, not portable C-fault claims.
- **3,608,576 actual native32 executions** through a volatile function pointer:
  all256 masks, all625 mappings from0/1/2/3/255, all16 state bitsets, plus
  every flag-byte value at every selected/mapped slot. Assert four-byte
  pointer/int, exact return, first four map/state bytes after every call and
  remaining504 global canary bytes after every configuration. Defined
  byte conversions and valid arrays only.
- Sixteen source/profile forms,72 ordinary executions, seven effective
  compiled negatives: invalid-continue, threshold-five, narrowed mapping,
  reversed bits, flag-one-only, shifted flag and return-two. Every control
  executes successfully; compiler/oracle exceptions never count as negatives.
- Copied owner has zero diagnostics, **ten unchanged neighbors**, identical
  pools/relative relocations. Actual padder emits136 bytes, no filler/data.
  Eight independent links execute32 cases: moved entry, independently rebased
  globals across signed-LO carry/high addresses, global/global aliases and
  argument-home aliases. Exact symbolic HI16/LO16 carry checked. Home aliases
  are emitted-instruction evidence, not ordinary portable C.
- **24,576 bounded actual caller executions** use the real22-word prefix,
  complete34-word predicate and real7-word epilogue. Cover256 masks, four
  mappings, four state patterns, three disable values and two SP phases.
  Disabled fixtures leave owner+5 unmapped, proving it is skipped. Compare
  ordered public reads/results, complete selected/retail state and restored
  ABI. Actual linked prefix/epilogue match retail.

Only the caller's positive continuation is replaced by a two-word jump to
its actual epilogue. The complete111-word caller, later callees, hardware
and gameplay are **not** qualified by that bounded connection.

First prequalification run: seven tests pass, one controls fixture fails,
67.662s. Alternate source/profile code spills below SP, outside the fixture's
original mapped home. Map private SP-0x100..SP+0x100 for controls only;
keep strict selected/reference/fault cases unchanged. Corrected focused
control test passes in13.481s. Explicitly reuse the seven unchanged pre
receipts instead of repeating exhaustive cases before installation.

Fresh installed **all eight tests pass in102.672s**, zero skips/errors/failures.
Ten shared padder checks pass in0.053s. Both tools project checks, source/
profile driver, CLI help and syntax checks pass. Prior unchanged helper suites
from Notes1126-1128 are reused receipts, not claimed freshly rerun. Remove
trailing empty EOF lines from five new tools files in both mirrors before
committing; no executable code or qualification behavior changes.

## Linked Audit And Progress

Build succeeds with existing duplicate generated_12D630 recipe warnings;
actual owner compile has zero diagnostics. Audit against
game-record-player-mask-test/after.json preserves all **6,058
bodies/addresses/extents**,6,042 retail slots/16 overflow symbols,
protected sections and **11,146 guards**. Actual linked callback table/
dispatch prefix remain retail-exact. All720 Game-data owners /189,088 bytes
retain SHA256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Exactly one conversion-row change: func_151D87E0, asm -> c,136 bytes.

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,473/6,042 (90.58%) | 1,932,964/2,256,728 (85.65%) | 3,384/5,473 (61.83%) | 2,089 /0 |
| Game | 4,800/5,321 (90.21%) | 1,761,528/2,072,880 (84.98%) | 2,711/4,800 (56.48%) | 2,089 /0 |

Init492/492 and Debugger181/181 converted routines remain exact.
New ignored baseline: conker/build/game-selected-player-state-test/after.json.
Always compare the previous player-mask baseline, not this target's own after.
Root README changes aggregates only; detailed updates remain here.

Source-before SHA256:
1b88c25b732795af584427280cae903f5c8ca3d3248230444d5a6b96a023c90b.
Final source SHA256:
913927183374a9ef297fd176f8879d33a4872ddf0d7295bbdcbeb01ac18bfb54.
Final progress SHA256:
2e4c98158538e268c453f818c51b80ce74d658db9b08079b746ccd7817d2c221.
Guard CSV SHA256:
5f029ab9d10ca4a13d8ad7b3b045c8fcf5f73592a67c10471d7ef738b2ed0d78.
Reference205C90.s SHA256:
1486d7fdf9a87e5aff20f0dfc427862fd4a55a322990f7e95e082a9666994ff2.
Original owner and before-progress rows are retained with ignored receipts.

## Authorized Commit Checkpoint

The user's later "Keep commited" request authorizes banking completed work.
Earlier notes' no-commit statements describe their matching-time checkpoints,
not this later authorized commit. Tools are committed first:

- 7f3c323: qualified embedded-record, distance-level and player-mask fixtures.
- fbd3fd8: qualified selected-player predicate driver/test.

The source checkpoint groups four directly exact conversions in this one
owner, Notes1126-1129, concise progress docs and the tools pin at
fbd3fd8dec103d434c42b2f39b37885186cc4db0. No push requested or performed.
Publish tools before publishing a parent commit that references them.

Preserve the older independently dirty standalone tools mirror at ddbdd16;
do not reset, stash or overwrite its unrelated changes. The canonical mounted
tools checkout is the committed consumer dependency. New fixture contents are
mirrored byte-for-byte locally, but the standalone checkout's older branch is
not silently reconciled or separately duplicated into divergent history.

Claude budget0 /attempted0 /completed0. No OGL Release, real saves/configuration,
live runtime, accounts, bridge installation or billing changes.

Graphify query finds no target node. Fresh update refuses to replace38,459
nodes with16,705 after the existing ignore changes reduced its corpus.
Keep old graph and ignore edits; no forced overwrite. Graph refresh remains
incomplete, separately from matching qualification.

Documentation validation:115 documents /3,950 relative links /zero broken.
Nineteen relevant tools policy/fixture files are byte-identical between the
mounted checkout and older standalone mirror. Staged whitespace checks pass;
mounted tools is clean after both commits. Parent commit records the exact
tools revision, not a moving branch.

## Next Function

[func_151D8868.s](../../conker/asm/nonmatchings/generated_205C90/func_151D8868.s)
remains retained assembly: **111 words /444 bytes**, frame **0x30**,
VA0x151D8868..0x151D8A24, ROM0x205D18..0x205ED4.

Static audit identifies ordered disable/predicate/four-byte global gates,
a byte-player loop bounded by live signed D_80082FA0, two selected-player
checks, six-argument allocator call, eight-byte owner copy, four-player
registration loop and final live owner byte store. Recover the complete
contract before fitting: parameter widths, allocator failure, mask mutation/
reloads, callback ordering, copy aliases and saved-register lifetime.
Its full positive continuation is not covered by this note's caller-prefix
fixture. No complete candidate or production conversion claimed yet.

Adjacent64-word func_151D8A24 is also retained. Wider Game matching/full
callee/hardware/gameplay/PC-port work remains open.
