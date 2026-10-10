# Game Actor Render-Dispatch Byte Match

Date: 2026-10-10. Continue and finish the same complete func_1502C974
investigated in [Note 1216](1216-game-actor-render-dispatch-recovery-and-layout-gates-20261010.md)
and [Note 1217](1217-game-actor-render-dispatch-lifetime-and-private-counterexamples-20261010.md).
Codex is the single writer; zero Claude calls. Keep commits tools-first;
no push, host build, Release, saves, editor or older-tools commit/reset.

## Installed Routine

VA 0x1502C974..0x1502CC34, ROM 0x59E24..0x5A0E4:
all 176 words / 704 bytes now match retail in the actual linked ELF.
[Production owner](../../conker/src/game/generated_58F80.c) replaces the
zero-return placeholder with the full five-argument semantic routine.
Preserve early visibility/mask/alpha/matrix gates, two separate alpha queries,
distance/alternate-tier callbacks, RGB/shading, owner override, mode-four
signed low-word factor product, all eight renderer arguments and fresh
post-render index/base/limit lookup with strict signed cursor rollback.

Original frame 0x58, RA +0x24, actor +0x2C, original cursor +0x34,
matrix +0x38, parameters +0x40 (alpha +0x4C), tier +0x54;
incoming arguments start +0x58, outgoing arguments +0x10..+0x1C.
The ordinary unreachable retail move at index 171 is retained, not padded.
Adjacent RGB/shading/render placeholder bodies stay intact with their existing
O32 v0 contracts; explicit owner casts keep their neighbors unchanged.

## Closed Normalization

[Matching helper](../../tools/experiments/game_actor_render_dispatch_matching.py)
uses the complete ternary-overflow semantic C from Note 1217.
IDO O2/g3 emits 177 words / 0x60 frame, zero diagnostics and new pools.
All 177 raw words and 28 relocation entries are closed dependencies.
The recipe does not read the ROM to generate replacement instructions.

- Remap the complete private and inbound homes to the original frame.
- Close the temporary-register rotation after visibility, including the
  separate mode-four factor/matrix/product cycle.
- Exchange the independent base low-half and saved-view read before actor
  construction, carrying the low relocation to its new instruction.
- Remove exactly one emitted ANDI count mask: MIPS sllv itself uses the low
  five bits. The portable semantic C retains explicit masking, including
  negative/wide views. Retarget the count operand and crossing branch.
- Invert the final likely branch, exchange the existing return producers
  into their corresponding delay slots, and retain the unreachable move.

177 guards: 111 changed replacement words, 65 unchanged dependency rows and
one omitted-mask dependency. One omission, zero insertions, zero missing-body
padding. Recovered frame/home/schedule qualification closes the installation
gates from Note 1217; its raw private counterexamples remain valid historical
evidence, not claims of raw private equivalence.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_actor_render_dispatch_match.py)
passes all 15 tests before and after installation: pre-install 29.664s,
first post-install 35.876s, final clarified-receipt rerun 29.168s.

- 2,160 guest cases compare independent semantic reference, complete original,
  raw C and fitted instructions on public behavior. Original/fitted memory
  and full private/public events agree. Raw/fitted are two emissions of one
  complete semantic C form, not independent C recoveries.
- 2,228 factor/cursor cases exercise all 256 factors, eight signed alpha
  boundaries, pointer-wrap, negative count, equality and strict overflow.
- 64 callback-mutation cases preserve the two alpha queries, captured actor,
  fresh owner/matrix/configuration/factor and post-render cursor globals.
- 60 connected cases execute actual banked 19-word alternate selector,
  163-word distance updater and 11-word identity leaf with the complete caller.
- 112 complete-parent cases verify ELF == ROM for the banked 173-word
  func_1502BAD0, then execute it connected to both original and fitted
  176-word dispatch bodies. Cover first/last parent slots, two views, all
  seven modes, two stack phases and alpha gates. Other parent/render
  callbacks remain explicitly bounded opaque, not whole-game acceptance.
- 1,491,048 actual native32 cases execute this selected complete C, with
  bounded callbacks, valid slot/view bounds and callback-sensitive rollback.
- Seven fresh effective compiled negative controls distinguish public
  return/traces. Existing public-fault probes also pass: 63 fired prefixes /
  189 original/raw/fitted executions; raw private order is not claimed.
- 144 private alias/mutation cases check full memory/events and actual
  callback pointer homes. Include owner-kind reads aliasing the frame and
  callback writes to original cursor, RGB/alpha and tier homes.
- 590 verified full private/public fault prefixes / 1,180 executions:
  every requested gate fires and complete original/fitted prefixes agree.
- Six independently assembled links / 96 cases retain exact instructions
  and complete physical behavior under three symbol sets and signed-LO16
  carries. Two additional raw-C links / 64 cases qualify public semantics.
- All 177 damaged raw words and 28 stale expected relocation entries are
  rejected by the actual padder; complete recipe stale-word checks also fire.
- All 37 copied-owner neighbor bodies, relative relocations and decoded
  pools agree. Copied target guards equal the isolated guards. Actual owner
  padding changes only the target 704-byte slot.

The linked-only audit after the successful full build allows only the target
704 bytes and target symbol extent to change, apart from regenerated debug
metadata. Every other protected linked byte/address/extent is preserved.
The prior guard file is an exact byte prefix; conversion CSV and retained
rodata are unchanged. Protected .game_data remains exact: 189,088 bytes /
720 owners, zero byte/owner differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Fresh matching: Game 2,758/4,816 (57.27%), total 3,431/5,489 (62.51%),
zero address drift / 2,058 different. Converted counts/bytes stay unchanged;
root README updates only aggregate matching rows.
The full build retains the known duplicate generated_12D630 recipe warning
and legacy pointer/type/long-double warnings outside this target. Isolated
and copied-owner target compilation has no diagnostics. No warning-free
full-build or host/gameplay acceptance claim.

## Bank And Resume

Tools 6ad7714 banks the matching helper/suite; 2136f14 clarifies that raw and
fitted are emissions of one C form. Commit qualified tools first, then source,
generated guard rows, concise
indexes, aggregate README rows and consumer pin. Mirror only two absent new
authored files to older tools; verify an exact existing authored mirror before
updating its receipt wording. Preserve older HEAD ddbdd16 and tracked-dirty
fingerprints; dirty entries rise 195 to 197 solely for the two new mirrors.
Keep all prior baselines/candidate receipts separate from this target's
ignored conker/build/game-actor-render-dispatch-match-test outputs.

Scoped validator passes: 40 documents / 4,224 relative links, zero broken
links and 69 exact authored-tool mirrors parsed in both copies. Older HEAD
and tracked-dirty fingerprints remain exact; fresh tools-check passes.

Native graphify update after final code edits exits 1, refusing a 39,379 to
17,606-node shrink. Retention preserves 19,398 nodes from 2,972 excluded-but-
existing files. Preserve existing version/zero-node warnings; no force, purge or install.
Verify the fresh consumer hook's workers and log growth after commit.

Next full target: func_1502D54C, VA 0x1502D54C..0x1502D630,
ROM 0x5A9FC..0x5AAE0, 57 words / 228 bytes, frame-free RGB parameter callback.
Recover its flag-selected averaged/inverted actor colors or white output,
including ordered output reloads/aliases, then qualify the real dispatcher
connection. Do not broaden to the 125-word shading callback or 532-word
renderer until their complete contracts are recovered and qualified.
Preserve the separate curve rejection in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and hardware/live acceptance remain open.
