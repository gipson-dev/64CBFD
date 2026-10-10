# Actor Counter-Updater Byte Match - 2026-10-10

## Scope And Baseline

Resume [Note 1213](1213-game-actor-attachment-updater-byte-match-20261010.md).
Target func_1502C608: VA 0x1502C608..0x1502C6E8, ROM 0x59AB8..0x59B98,
56 words / 224 bytes in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
Restore its complete void/slot interface and original 0x28 frame without
guards. Single Codex writer, zero Claude calls. No OGL, Release, saves,
editor, push or unrelated work; the wider Game matching goal stays active.

Consumer baseline 848e7d48c42ee6264ddf32d09292031830de7d1a; mounted tools
9f1e85e027d2294c5b5423fbfae3f46c7892cd98. Both start clean. New ignored
conker/build/game-actor-counter-update-match-test preserves source, ELF,
guards, conversion CSV and rodata baselines; historical receipts stay intact.

Source baseline SHA-256
aad32d41cf0c19f101403444b11bd4393ab6c415e6a0acde2b9484f7dfba63d3;
ELF 25dfb7f6cd6f59da92da7631098beadb7fafd65f823830a2ef4a51bc5cc4facf;
guards 25077ad5131a5888739c0653a2f29464e949d5e94bf6b7c3980515d9b56ec2c8.

## Recovered Semantics

Nonzero byte D_800BEAC0 skips every actor read. Otherwise actor is
D_800CC2D0 plus the unsigned low-word slot*0x32C product. Read byte +7,
signed halfword +0x60 and signed halfword +0x62 before the actor-byte gate;
zero +7 still performs the two halfword reads, but makes no call or update.
Narrow volatile halfword reads preserve those accesses in semantic C.

For nonzero +7, retain captured value and step in original private halfword
homes +0x22 and +0x20, actor pointer at +0x18, saved RA at +0x14. Call
func_1502C3BC with the original slot. The actual banked classifier is
19 words / 76 bytes, VA 0x1502C3BC..0x1502C408: read actor byte +0x136,
return it below 70, otherwise return 11. Do not include the first word of
the next routine when checking its size.

After the call read D_8008CA4C[result], reload the captured halves, read
configuration byte +4 and shift it eight bits, then reload the actor pointer.
Wrap the captured sum to s16. If that signed sum is at least the nonnegative
period, subtract once and wrap to s16; otherwise, if negative, add once and
wrap. This is not modulo, repeated correction or post-call actor-field reload.
Period zero and periods above 32767 retain these exact signed comparisons.

The complete banked 88-word func_1502BD84 dispatcher's state-2 path calls the
updater after clearing work. Its actor-ID-255 gate precedes this call; its
later active gate does not apply to state 2. The typed void prototype changes
no caller instructions. Hardware/live gameplay acceptance remains separate.

## Compiler Recovery

[Candidate driver](../../tools/experiments/game_actor_counter_update_candidates.py)
measures 49 complete/profile forms. The initial named actor gate emits
56 words / 0x30 frame / 24 differences. A direct actor-byte gate emits
56 / 0x30 / eight differences, solely frame and spill locations. Declaration
order can reduce this to six differences but cannot recover the frame.

Assign the classifier result to period, then use period for the configuration
lookup and shifted byte. This complete semantic form emits all 56 retail
words directly under production O2/g3, with the original 0x28 frame, seven
relocation sites, zero pools and zero diagnostics. No guards, insertions,
omissions or tail padding. O2 without g3 has seven differences; O1/g3 emits
65 words and O1 emits 64. No profile or shared helper changes.

## Fresh Qualification

[Focused suite](../../tools/tests/test_game_actor_counter_update_match.py):
ten tests pass before installation in 11.445s and after installation in
10.830s. Earlier fixture failures are excluded from acceptance.

- 4,330 guest cases / 12,990 original/raw/installed-or-candidate executions
  cover every period byte, all 26 valid slots, signed overflow, negative and
  zero boundaries, both byte gates and all 56 retail words. Complete memory,
  public/private access traces, saved-register lifetime and ABI agree with
  an independent reference. The reserved stack word +0x10 remains unmapped.
- 1,040 callee cases include all 256 actor identity bytes, two stack phases,
  both endpoint slots and the actual banked 19-word classifier. Bounded opaque
  callback cases mutate captured actor fields and replace the configuration
  table pointer: captured halves remain old, configuration reads are fresh.
- 32 alias/rebase cases cover configuration reads from saved RA, actor-pointer
  and halfword homes, plus the table cell aliasing the actor-pointer home.
  Five links include three independent symbol sets and signed-LO16 carries.
- 162 verified fault prefixes / 486 executions check each fired gate and the
  complete memory/trace prefix, including private accesses and both phases.
  These qualify emitted guest order, not portable C fault semantics.
- 1,992,704 native32 complete-C cases exhaust all 65,536 value bit patterns
  with six representative signed steps and five period bytes; also test all
  identity bytes, every bounded slot, both gates and a callback replacing the
  table entry and mutating actor halves. Native callbacks are bounded models,
  not a claim of executing banked MIPS instructions on the host.
- Six fresh compiled negative controls distinguish public results or public
  access traces: inverted gates, wrong period shift, missing negative
  correction, wrong destination and reloaded captured fields. Differences in
  private stack layout alone cannot qualify an effective negative control.
- 256 connected cases execute the complete actual banked 88-word dispatcher,
  19-word classifier and original versus candidate/installed 56-word updater.
  Full traces/memory/ABI agree, including actor-ID-255 and inactive state-2
  cases. Other dispatcher callbacks are explicitly bounded opaque.
- All 37 copied-owner neighbors retain complete bodies, relative relocations
  and decoded pools. Both owner compiles have zero diagnostics. Actual padder
  changes only the target 224-byte slot, using the unchanged guard manifest.

Fixture corrections: classifier extent is 19, not an assumed 20; state-2
dispatch does not use active; include early-return likely-delay coverage.
No failed setup or run is credited as a production match.

## Linked Checkpoint

Fresh build, match-progress and tools-check pass. The existing duplicate
generated_12D630 recipe warning remains; no warning-free-project claim.
Post-install audit permits only the target 224-byte slot and symbol extent,
normalizing symbol/string metadata for whole-ELF comparison. Guards, conversion
CSV and rodata assembly are byte-unchanged. Protected .game_data remains
189,088 bytes / 720 owners, zero byte or owner differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Final source SHA-256
6acffcb6caa5ca0fc5f6ff86ed99fe036182d448bc27a4dd1c8f215d51bac404;
ELF eb22ddc2bccd5794e668c27f3c3215b5ba5a69b82853f3f114adc8dfed4716d2;
guards 25077ad5131a5888739c0653a2f29464e949d5e94bf6b7c3980515d9b56ec2c8;
conversion CSV 5c104a10b09965a84863a7b353b1bfb1e49d3a56d0760cdba6383fa71fb92f24.

Fresh match-progress: Game 2,756/4,816 (57.23%), total 3,429/5,489 (62.47%),
Init 492/492 and Debugger 181/181 exact; zero drift / 2,060 different.
Conversion totals are unchanged because the replaced stub already counted
as C. Root README changes only two aggregate matching rows.

## Bank And Resume

Bank mounted tools 0483bc89649bcc696ceecff26afd26cd4be8b90e first, then
consumer source/docs/pin, without push. Only the two absent authored files
are mirrored to the older tools checkout. Preserve its HEAD ddbdd16 and
both tracked-dirty fingerprints; dirty entries rise from 186 to 188 solely
for the mirrors. No older commit, reset or conflicting overwrite.

Scoped validator passes: 36 documents / 4,182 relative links, zero broken
links and 60 exact authored-tool mirrors, both copies parsed, with old
HEAD/tracked-dirty fingerprints preserved.
Manual graphify update exits 1, refusing a 39,342 to 17,561-node shrink;
retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Existing
skill/package and zero-node devcontainer warnings remain. No force, purge,
installation or policy change. Verify the new consumer's detached hook using
fresh process/log evidence, not historical hook receipts.

1. Next: func_1502C6E8, VA 0x1502C6E8..0x1502C974, ROM 0x59B98..0x59E24,
   163 words / 652 bytes, frame 0x50; current source is a zero-return stub.
2. Recover slot plus signed-halfword second-argument ABI, actor +0x1C9/state-7
   gates, signed second-record lookup via D_800DBFF0, one-based actor +0x2C8
   selector and actual func_150849A0 callback result before distance tiers.
3. Preserve single-precision ordered squared distance and threshold compares,
   speed adjustment, callback/global byte overrides, signed clamp, unchanged
   tier early return, then func_150837D4 and final actor +0x1C8 store.
4. Qualify full callbacks, private lifetimes, float/NaN boundaries, owner/data
   audit and independent links before any installation or matching credit.

Preserve the separate uninstalled curve rejection in
[Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
The wider Game goal and full hardware/live acceptance remain open.
