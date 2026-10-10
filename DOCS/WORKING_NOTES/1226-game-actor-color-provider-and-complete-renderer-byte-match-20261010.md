# Game Actor Color Provider And Complete Renderer Byte Match

Date: 2026-10-10. Continue the same renderer after
[Note 1225](1225-game-complete-actor-renderer-actual-color-and-matrix-connections-20261010.md).
Consumer baseline 11dbb224; mounted-tools baseline baacebd.
Codex single writer, zero Claude calls. Authorized tools-first commits, no push.
No host/Release builds, saves or editor changes.

## Installed Recovery

- func_1502CC34: VA 0x1502CC34, ROM 0x5A0E4; 50 words / 200 bytes,
  original 0x20 frame. All words emit directly from semantic C, no guards.
  Preserve unused s32 alpha's incoming argument home. Read primitive and
  environment palettes live, store all ten outputs in original order,
  re-read parameters[3], and conditionally invoke actual func_1502EC34.
  Plain alpha and volatile alpha produce identical words; select plain s32.
- func_1502CCFC: VA 0x1502CCFC..0x1502D54C, ROM 0x5A1AC..0x5A9FC;
  complete 532 words / 2,128 bytes, original 0x150 frame/private homes.
  Install the complete selected C body and certified recipe from Note 1223.
  531 guards: 122 normalizations, 409 unchanged dependencies, two existing
  instruction copies and one redundant-mask omission; no missing-body padding.

Source is [generated_58F80.c](../../conker/src/game/generated_58F80.c).
[Color candidate](../../tools/experiments/game_actor_color_provider_candidates.py)
installs both selected bodies into the same copied owner. Typed Gfx return
declarations preserve cursor use; func_1502F9FC remains a zero-return placeholder
with a corrected pointer return type. No behavior is recovered for it here.

## Fresh Qualification

[Eight-test suite](../../tools/tests/test_game_actor_renderer_install_match.py):

- 832 color cases / 1,664 original/compiled executions cover every color word,
  all 256 fog modes, signed/full-width views/alphas, live output/palette/actor/
  parameter aliases and finite pointed-opacity clamps. Complete private/public
  memory, events and calls agree; independent ordered public reference agrees.
- Two private output aliases and all 160 selected full fault-prefix pairs fire,
  320 failed executions. Absence of a requested fault is a failure.
- Three fresh complete IDO C negatives: wrong palette, alpha instead of
  parameter opacity, inverted fog gate. Check unmodified positives first.
- Combined copied owner has zero diagnostics; both bodies equal isolated
  candidates. All 36 other bodies, extents, relative relocations and pools
  remain exact. Actual postprocessing/assembly/padding changes only two slots.
- 224 full dispatcher/renderer cases / 672 original/raw/fitted executions
  connect compiled color/renderer to actual fog, RGB, shading and both matrix
  chains. Original/fitted private memory/order agree without adjustment.
  Raw comparisons retain Note 1225's proven saved-return-PC-only boundary.
- Actual native32 color plus fog C passes 648 cases at each of -O2/-O0:
  1,296 executions with separate little-endian independent reference.
  Three fresh native complete-body controls fail effectively at case/byte
  0/0, 0/36 and 1/24, all return code 5.

All 29 pre-install install/connected/native/schedule regressions passed.
After final guard-writer edits the eight-test pre-install suite passed again.
After installation, correct the linked test's reused symbol lookup: it had
asserted an unrelated function address. A local structured ELF lookup now
checks each requested name/address/type, with wrong-address and missing-symbol
rejections. No production or historical baseline is changed to resolve it.
Final post-install eight tests pass in 29.472s; make tools-check passes.

```sh
python3 -m unittest tools.tests.test_game_actor_renderer_install_match -v
make tools-check
make -C conker build/conker.us.elf NON_MATCHING=1 -j4
make -C conker match-progress NON_MATCHING=1
```

Historical pre-install suites intentionally assert unchanged production.
Do not rewrite their immutable baselines to pretend installation never occurred.

## Linked Audit And Credit

The build finishes and a repeat build confirms the ELF is up to date.
Known duplicate generated_12D630 recipe and outside-target compiler warnings
remain; isolated target/copied-owner diagnostics are zero, not the whole build.

Actual linked ELF equals the immutable before image with only the two target
instruction slots (2,328 bytes) and their two symbol-length fields updated.
All other linked bytes, addresses, extents, symbols and names remain exact.
Append exactly 531 renderer rows through structured CSV generation, preserving
the original guard bytes as a literal prefix, including mixed line endings.
Duplicate installation is rejected. No color rows. Progress and rodata exact.

Protected Game data: 189,088 bytes / 720 owners, zero differing bytes/owners.
SHA256: 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Fresh matching credit is +2: Game 2,762/4,816 (57.35%), total 3,435/5,489
(62.58%), zero drift / 2,054 different. Init 492/492 and Debugger 181/181
remain exact. Converted totals/bytes unchanged: both old placeholders already
counted as converted. Root README updates only the two aggregate matching rows.

Cosine and other callbacks remain explicitly bounded. No actual trigonometric,
complete callback-table, FCSR/trap, hardware or live-game acceptance claim.

## Bank And Resume

Tools f4e5f82 banks qualification; cc74178 banks corrected linked-symbol audit.
Consumer banks source/guards, this note, five concise indexes, README aggregate
rows and tools pin. No push. Mirror the two new authored paths and the verified
audit correction only. Older tools HEAD ddbdd16 and both tracked-dirty
fingerprints remain unchanged; native dirty entries rise 212 to 214.
No commit/reset in that independently dirty checkout.

Fresh handoff validation passes eight documents / 4,115 relative links,
zero broken links, two exact new mirrors parsed in both copies, older count
214, unchanged older HEAD and both tracked-dirty fingerprints.

Manual graphify update after final code edits exits 1, refusing unsafe
39,438 to 17,657-node shrink. Retain 19,398 nodes from 2,972 existing excluded
files. Version mismatch and zero-node devcontainer warning remain visible.
No force/purge/install. Verify fresh detached hook log growth and completion
after consumer commit.

1. Audit the renderer's remaining bounded production dependencies, starting
   with func_1502F9FC, before recovering the next complete semantic body.
   Use actual assembly, copied-owner layout and effective negative controls.
2. Keep native/guest byte-order proofs distinct, and saved-return-PC comparison
   limits explicit. Do not infer live rendering from byte matching.
3. Keep actual cosine/other callbacks, FCSR/traps, hardware/live and separate
   curve rejection gates from
   [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md)
   open. Wider Game matching goal remains active.

