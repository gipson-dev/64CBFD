# Game Record Allocation And Player Registration Conversion

Date: 2026-10-08

## Result

Continue [Note 1129](1129-game-selected-player-state-direct-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert retained
`func_151D8868` to complete semantic C in
[generated_205C90.c](../../conker/src/game/generated_205C90.c).
All **111 words /444 bytes**, frame **0x30**, match retail after **two
strict scheduling guards**; **109 words emit directly** under existing
IDO 5.3 O2/g3. No filler, pools, new data, profiles or Makefile changes.
Local SDK string declaration and callee/global prototypes are recovered.
Reference [205C90.s](../../conker/asm/205C90.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_205C90/func_151D8868.s)
remain untouched. VA0x151D8868..0x151D8A24, ROM0x205D18..0x205ED4.

Already exact assembly becomes semantic C. All linked instructions remain
unchanged; only this444-byte conversion row and exact two-row guard append
change from the previous selected-player baseline.

## Recovered Contract

`u8 *func_151D8868(u8 *owner, s32 payloadBytes, u8 slot, s32 context)`:

- Reject nonzero D_800E0B94, then failed func_151D87E0(owner[5]), then any
  nonzero byte among D_800BEAC0..D_800BEAC3, in that order.
- Scan unsigned byte validation indices through the live signed D_80082FA0
  inclusive. Reload owner[5] each iteration. A selected player must pass
  func_15181CC8 first and have func_1517EF00 return zero; failure skips all
  subsequent checks/allocation. Limit reloads survive callback mutations.
- Allocate with func_15167A68(0x3F, context, payloadBytes+0x18,1,slot,1).
  NULL returns immediately. Copy exactly eight owner bytes to record+0xE.
- Scan four unsigned byte players. Reload copied record[0x13] each iteration;
  selected players call func_1501C010(player,live owner[4]). Finally store
  fresh owner[4] to record[0x16] and return the allocated record.

Owner stays captured across callbacks. The emitted routine reloads its other
three allocator arguments from incoming homes after callbacks. Real allocator
and caller declarations/assembly confirm argument widths and allocation layout;
real callers include func_151C1FB8 and func_151D5404. Their complete caller bodies
and all later callee implementations are not qualified here.

## Source Fit And Guards

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_player_registration_candidates.py)
retains complete source alternatives and executable negatives. A shared byte
counter emits111 words/17 differences; separate byte counters recover the
frame/lifetimes and leave only two differences. Other shapes retain the two
or worsen fitting: int registration counter109/26, wide slot111/3, separate
validation failures113/65, separate global gates117/94, explicit final-positive
gate112/22 and enclosing-positive flow111/79. Zero diagnostics/pools.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 111 | 0x30 | 2 |
| O2 | 110 | 0x30 | 110 |
| O1/g3 | 117 | 0x28 | 112 |
| O1 | 116 | 0x28 | 111 |

At+0x94/+0x98, IDO emits `beqzl t0,+0xA8; lw t1,0(s2)`.
Retail uses `beqz t0,+0xA4; nop`, executing the existing+0xA4 load on the
zero path. Neither loads the limit after a nonzero final gate. Raw's+0xA4
duplicate is unreachable. The two expected-word guards normalize this closed
conditional branch/load schedule, not missing semantic logic. Normalization
also checks the adjacent branch and duplicate load; four stale schedule
mutations are rejected. No relocations are patched at these two locations.

Unsigned shifts define validation indices0..31. Explicitly masking the shift
count emits112 words/71 differences and is retained as a source control, not
selected. No artificial validation cap is added. Native cases use limits-1..4;
guest cases additionally cover31. No portable C claim for limits>=32, signed
payload-add overflow, arbitrary private-home aliases or overlapping memcpy.
Nonoverlapping allocation aliases are RECORD, OWNER-5 and OWNER+16.
Guest fault prefixes do not model CP0 BD/EPC metadata or hardware faults.

## Qualification

[Nine target tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_player_registration_match.py)
reuse strict TriangleOracle, native32, owner/parser/padder helpers and add an
independent public construction reference. Shared domain oracle is unchanged.

- **110,604 guest cases** cover low masks/check bitsets, all byte masks,
  signed limits, allocation outcomes and two SP phases. Every reachable raw/
  retail word is reached; only dead duplicate loads remain. Full GP/FP,
  ordered trace/memory and independent public flow/results agree.
- **2,056 lazy-gate cases** cover all disable/four-gate byte values and
  predicate failures with unnecessary globals/limit unmapped. **68 required
  fault prefixes** cover saved registers, homes, fields and copy boundary.
  Copy fault ordering uses a controlled boundary, not actual SDK memcpy.
- **2,256 public mutation/alias/raw-argument cases** and eight private-home
  cases establish live masks/limit/level, failure ordering and captured owner
  versus allocator argument reloads. Raw wrapping payloads/home aliases are
  emitted-instruction evidence, not extra portable C range.
- **2,163,968 actual native32 C executions** through a volatile function
  pointer assert pointer/int sizes4, all masks/check bitsets/failure paths,
  all slot bytes, seven mutation modes, three nonoverlapping aliases and
  defined signed payload range. Compare all160 storage/canary bytes, globals
  and ordered calls with independent expected flow.
- **34 source/profile forms /208 ordinary executions /eight effective
  compiled negatives** cover exclusive validation bound, owner registration
  mask, cached limit/owner mask/record mask, seven-byte copy, wrong allocation
  size and shifted return. All controls compile and execute successfully;
  exceptions never count as behavioral negative passes.
- Copied complete owner has **zero diagnostics**, ten unchanged neighbors,
  identical pools/relative relocations. Real padder emits444 bytes without
  filler/data. **Six independent links /576 rebased executions** check all
  **18 symbolic relocations**, including signed-LO carries/high addresses.
- **9,216 complete connections** execute the actual34-word predicate with
  the complete111-word constructor, not the prior synthetic continuation.
  Both installed bodies match retail. Later checks, allocator, SDK copy and
  registration remain controlled interfaces, not full gameplay/hardware.
- Historical guard assertion retains every original hash/exact-row check,
  accepts only original11,146 rows or those rows plus the exact two new ones,
  and rejects eight corrupt manifests. This is the sole shared helper change.

Prequalification is a union of focused passes, not one claimed full run:
tests01/04/06 pass in26.584s;03/05 pass before07's fixture warning-type failure;
07/08 pass after replacing the expected empty string with the actual empty
warning list. Test02's110,592 outcomes pass before its reachability assertion
finds omitted early gates. Add twelve early-gate cases; corrected02 passes
in87.891s. Rerun09/06 passes in55.283s after correcting a no-op source-control
replacement. No production failure or compiler warning is hidden by these
fixture corrections. The latest additional shift control passes post-install.

Fresh installed **all41 constructor/four-neighbor tests pass in601.805s**,
zero skips/errors/failures. This reruns the selected-player, player-mask,
distance-level and embedded-callback suites because the shared guard checker
changed. Ten shared padder checks pass in0.044s. Both tools project checks,
profile driver, CLI help, and syntax checks in both mirrors pass.
Older wider suites remain explicitly reused receipts, not fresh claims.

Reproduce the expanded suite from the source repository in WSL:

```sh
python3 -m unittest -v \
  tools.tests.test_game_record_player_registration_match \
  tools.tests.test_game_selected_player_state_match \
  tools.tests.test_game_record_player_mask_match \
  tools.tests.test_game_record_distance_level_match \
  tools.tests.test_game_record_embedded_callback_match
make -C conker -j4 build/conker.us.elf progress.csv
```

## Linked Audit And Progress

Build succeeds. The global CSV dependency triggers broad recompilation:
existing duplicate generated_12D630 recipe warnings and diagnostics in unchanged
Game/Debugger sources remain. The strict new owner compile has zero diagnostics;
the full build is not claimed warning-free.

Audit against game-selected-player-state-test/after.json preserves all
**6,058 bodies/addresses/extents**,6,042 retail slots/16 overflow symbols,
protected sections and prior **11,146 guards**, then adds exactly two.
Actual linked callback table/dispatcher prefix remain retail-exact.
All720 Game-data owners /189,088 bytes retain SHA256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Exactly one conversion-row change: func_151D8868, asm -> c,444 bytes.

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,474/6,042 (90.60%) | 1,933,408/2,256,728 (85.67%) | 3,385/5,474 (61.84%) | 2,089 /0 |
| Game | 4,801/5,321 (90.23%) | 1,761,972/2,072,880 (85.00%) | 2,712/4,801 (56.49%) | 2,089 /0 |

Init492/492 and Debugger181/181 converted routines remain exact.
New ignored baseline: conker/build/game-record-player-registration-test/after.json.
Compare the previous selected-player baseline, not this target's own after.
Root README changes aggregates only; detailed updates remain here.

Final source SHA256:
029b0e8633d649a137a91682fe444bd13719650b46b31146a83d478180b6c0c8.
Final progress SHA256:
8d69c9b60b3c36744b687cc3d144fae3140e56591209c3e0c1d9ae1d7a7e9f9e.
Guard CSV SHA256:
5f86176c588376fd2dd528dee562722d32765ab120b8cee6ffd9fe9321833823.
Original owner/progress and complete receipts remain in the ignored test folder.

## Authorized Checkpoint

Continue the user's "Keep commited" instruction. Commit tools first:
**6e2e24d56248309a8be2b98b7d135d4b8544775c**, complete driver/test and strict
guard-history extension. Parent checkpoint groups only this constructor,
two CSV guards, Note1130/progress docs and that exact tools pin. No push
requested or performed. Publish tools before publishing the referring parent.

Preserve the independently dirty older standalone tools checkout at ddbdd16;
mirror fixture contents without resetting, stashing or duplicating divergent
history. Canonical mounted tools is the committed consumer. Zero Claude calls;
no OGL Release, saves/configuration, runtime, accounts or bridge changes.

Validate116 documents /3,962 relative links /zero broken. Twenty-one relevant
tools policy/fixture files are byte-identical between mounted and standalone
checkouts. Tools staged whitespace checks pass and mounted tools is clean.
Parent records the exact tools revision; remote publication is not verified.

Graphify query finds no target node. Full refresh refuses to replace38,504
nodes with16,716; fail-closed retention preserves19,398 nodes from2,972
excluded existing files. Do not force overwrite or undo existing ignore edits.
Graph refresh remains incomplete, separately from matching qualification.

## Next Function

[func_151D8A24.s](../../conker/asm/nonmatchings/generated_205C90/func_151D8A24.s)
is the owner's sole remaining retained assembly: **64 words /256 bytes**,
frame **0x28**, VA0x151D8A24..0x151D8B24, ROM0x205ED4..0x205FD4.

Ignored next-state-screen.py and next-state-update-measurements.json retain
complete natural, explicit unsigned wrapping-subtraction and int-expiry forms:
each64 words/frame0x28/**four raw differences**, zero diagnostics/pools.
Int player instead emits66 words/frame0x30/63 differences. These are fitting
measurements only; no behavior qualification or production conversion yet.

Recover optional timer decrement with signed-halfword truncation/reload,
expiry captured before callbacks, signed callback selector with -1 skip,
live record mask/level after callback, clear-before-register calls, fresh
level mirror and final expiry/free lifetime. Actual index0 table entry is
the already-qualified embedded-record callback; other three are zero.
Full pointer/index domains, callback mutations, faults, native32, copied-owner,
rebases and connected paths remain future gates. Wider Game/hardware/gameplay
and PC-port work remains open.
