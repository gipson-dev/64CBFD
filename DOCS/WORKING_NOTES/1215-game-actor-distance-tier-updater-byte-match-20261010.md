# Actor Distance-Tier Updater Byte Match - 2026-10-10

## Scope And Baseline

Resume [Note 1214](1214-game-actor-counter-updater-byte-match-20261010.md).
Target func_1502C6E8: VA 0x1502C6E8..0x1502C974, ROM 0x59B98..0x59E24,
163 words / 652 bytes in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Restore the complete void (s32 slot, s16 view, s32 unused) interface,
original 0x50 frame and callback-sensitive tier computation.
Single Codex writer, zero Claude calls. No OGL, Release, saves, editor,
push or unrelated work. The wider Game matching goal stays active.

Consumer baseline 43ea1f1410995b097ebcad73f14fbf73a7ace9c4; mounted tools
0483bc89649bcc696ceecff26afd26cd4be8b90e. Both start clean.
Ignored conker/build/game-actor-distance-tier-match-test preserves source,
ELF, guard, conversion CSV and rodata baselines; historical receipts stay intact.
Source baseline SHA-256
6acffcb6caa5ca0fc5f6ff86ed99fe036182d448bc27a4dd1c8f215d51bac404;
ELF eb22ddc2bccd5794e668c27f3c3215b5ba5a69b82853f3f114adc8dfed4716d2;
guards 25077ad5131a5888739c0653a2f29464e949d5e94bf6b7c3980515d9b56ec2c8.

## Recovered Semantics

Actor is D_800CC2D0 plus the unsigned low-word slot*0x32C product.
The signed low halfword of view selects a 0x9A0-byte player record through
D_800DBFF0. Read actor +0x1C9 and the player-base global before the prepare
early return; state byte +5 equal to 7 is the second gate.

Capture four f32 thresholds in private homes +0x28..+0x34:
500, D_80096DE0, D_80096DE4, 2000. The two actual ELF globals contain
730 and 1500, not a new generated constant pool.
Actor byte +0x2C8 minus one is the selector; zero skips after those stores.
The selector, not view, caps the final tier. Initial wrong-view-cap
experiments are excluded and an effective compiled negative rejects that error.

Save actor at +0x1C, selector at +0x3C and player at +0x4C across
func_150849A0. The actual banked identity leaf is 11 words / 44 bytes,
VA 0x150849A0..0x150849CC, ROM 0xB1E50..0xB1E7C. Its ELF bytes equal
retail. The reachable normal path reads fresh actor +0x1C9, the table
pointer +0x2C4 and the first configuration byte. This is not a qualification
of every unrelated path through that leaf.

Read fresh player coordinates +0x2F8/+0x2FC/+0x300 and actor +0x14/+0x18/+0x1C.
Compute ordered single-precision dx*dx + dy*dy + dz*dz with rounding at each
operation. Strict threshold-square comparisons select tiers 0..4; NaN
comparisons fall through to 4. Preserve the early private threshold reads,
including the second threshold even when tier zero is selected.

For tier >=2, speed actor +0x3C below 3 decrements once.
Identity 90 raises tier zero to one. Identity zero reads fresh D_800BE616;
nonzero sets tier one. Fresh D_800C35EA equal to exactly one forces zero.
Clamp by the captured selector, retaining the emitted signed-negative clamp.
The ordinary selector range is 0..254; negative private selector mutation
is covered separately. The retained tier-minus-one check has no semantic
ordinary path.

Unchanged actor +0x1C8 tier returns. Otherwise read fresh actor +0x2C4,
reload the original inbound slot, read configuration[tier] and call
func_150837D4(slot, byte, 0). Save tier at +0x40 and actor at +0x1C,
then write the retained tier to actor +0x1C8 after the callback, overwriting
a callback change there. func_150837D4 remains a source placeholder and is
explicitly bounded opaque in this qualification.

## Compiler And Closed Layout

[Candidate driver](../../tools/experiments/game_actor_distance_tier_candidates.py)
measures 61 complete/profile forms. The nested baseline O2/g3 emits
162 words / 0x48 frame / 128 differences. Named deltas recover the frame
but leave 123 differences; early returns alone recover length but retain
0x48 / 44 differences. Twenty-four baseline declaration orders do not help.

Early returns plus an explicit squared temporary emit 163 words / 0x50
frame / 33 differences with no copied-owner diagnostics. O2 without g3
emits 162 / 0x50 / 162 differences; O1/g3 and O1 emit 198 / 0x48 / 188.
Keep the existing production O2/g3 profile; no shared compiler changes.

[Matching certificate](../../tools/experiments/game_actor_distance_tier_matching.py)
checks all 163 raw words and 14 relative relocations before any replacement.
Append 163 closed guard rows: 33 changed words, 130 unchanged dependencies.
Normalize only threshold/player/selector/tier private homes and the closed
floating-register/scheduling block, preserving coordinate read order and
every arithmetic rounding edge. Move one D_800BE616 HI16 producer from
offset 0x10C to 0x118 with its relocation; signed-LO16 carry cases qualify.
Frame, RA, actor home, inbound arguments, branches, calls and delay slots
already emit directly. No insertions, omissions, padding or new pools.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_actor_distance_tier_match.py):
11 tests pass before installation in 17.767s and after installation in
20.308s. Failed initial controls and setup runs receive no acceptance credit.

- 2,303 guest cases compare an independent reference against original and
  fitted full memory/public/private traces. Raw C is additionally checked
  for disjoint public results/access order, not private alias equivalence.
  Ordinary cases reach 161/163 words; the negative clamp is reached through
  private mutation. The tier-minus-one return remains semantically unreachable.
  Saved registers, RA/SP and unmapped reserved frame +0x10 are checked.
- 100 callee cases execute the actual banked identity leaf and bounded opaque
  mutation callbacks. Player/selector/threshold captures remain old while
  coordinates, override bytes and the final configuration pointer are fresh.
- 28 alias/rebase cases qualify original/fitted configuration reads from
  private homes and negative selector mutation. An explicit raw-C private-home
  counterexample proves the physical distinction rather than hiding it.
- 430 verified fault prefixes / 860 original-fitted executions check fired
  gates and complete public/private order. These are guest instruction-order
  claims, not portable C fault guarantees.
- 72 rebase cases use six independent links and three symbol sets. All 163
  stale words and 14 stale relocation sites are actually rejected, including
  the moved HI16 and signed-LO16 boundaries.
- 1,437,800 native32 complete-C cases cover 26 bounded slots, four views,
  all selector bytes, six distances, three speeds and three identity results,
  plus callback capture/final-store cases. Guest negative/wide views are
  separately mapped; no native out-of-range pointer claim.
- Seven fresh effective compiled negatives distinguish public results or
  access traces, including the wrong view clamp. NaN tier behavior and finite
  overflow are covered; raw NaN payloads/FP exception flags are not claimed.
- All 37 copied-owner neighbors retain bodies, relative relocations and
  decoded pools. Actual padder changes only the target 652-byte slot.
- 120 caller cases execute the exact four retail forwarding instructions at
  VA 0x1502CA9C / ROM 0x59F4C with a synthetic return boundary. They qualify
  slot, signed view and unused forwarding, not complete func_1502C974.

## Linked Checkpoint

Fresh build, match-progress and tools-check pass. Appending guards triggered
the manifest-dependent wider rebuild. Existing shared compiler warnings and
the duplicate generated_12D630 recipe warning remain; no warning-free claim.
Whole-ELF audit allows only the target 652-byte slot and symbol extent after
normalizing symbol/string metadata. The previous guard bytes remain an exact
prefix; conversion CSV and rodata assembly are byte-unchanged.
Protected .game_data is 189,088 bytes / 720 owners, zero byte/owner differences,
SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Final source SHA-256
65bd86e98d3df8536c883351dc4bd9ef98c1ed26372f17fccfc3c80fcce23b70;
ELF d5b9745d2361d77d2a5fb1a7a4a5d974bcf7f2b1104b003b1c02432cd2662e4a;
guards 865adc57371ae97c008f5b7fc394da116684e88272b76eba70052cc5174ea332;
conversion CSV 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Fresh match-progress: Game 2,757/4,816 (57.25%), total 3,430/5,489 (62.49%),
Init 492/492 and Debugger 181/181 exact; zero drift / 2,059 different.
Conversion totals stay unchanged because the replaced stub already counted
as C. Root README changes only two aggregate matching rows.

## Bank And Resume

Bank mounted tools 6c5b8a48f5d4aed18c7b92bf2ba385e2731e6927 first, then
consumer source/guards/docs/pin, without push. Mirror only three absent new
authored files to the older tools checkout, preserving HEAD ddbdd16 and both
tracked-dirty fingerprints. Dirty entries rise from 188 to 191 solely for
these mirrors; no older commit, reset or conflicting overwrite.

Scoped validator passes: 37 documents / 4,193 relative links, zero broken
links and 63 exact authored-tool mirrors, both copies parsed, with older
HEAD/tracked-dirty fingerprints preserved.

Manual graphify update exits 1, refusing a 39,352 to 17,571-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files.
Existing skill/package and zero-node devcontainer warnings remain.
No force, purge, installation or policy change. Verify the consumer's new
detached hook using fresh process/log evidence, not prior hook receipts.

1. Next: complete func_1502C974, VA 0x1502C974..0x1502CC34,
   ROM 0x59E24..0x5A0E4, 176 words / 704 bytes, frame 0x58.
   Current Gfx-pointer source is still a zero-return placeholder.
2. Recover the full cursor/slot/view/mode/stack-argument interface and
   visibility/work gates before connecting this updater. Retail mode values
   3, 4 and 5 bypass it; the third incoming argument selects view.
3. Preserve callback-sensitive actor reloads, alternate tier path,
   private parameter record, alpha/pointer selection and final cursor limit.
   Do not promote the four-instruction forwarding receipt to caller acceptance.
4. Qualify complete callback/private lifetimes, owner/data audit and
   independent links before installation or matching credit.

Preserve the separate uninstalled curve rejection in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and full hardware/live acceptance remain open.
