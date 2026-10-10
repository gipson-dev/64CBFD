# Object Color-Mode Semantic Recovery And Table Gates

Date: 2026-10-10. Diagnostic progress only; not installed or byte-matching.
Continue [Note 1206](1206-game-owner-captured-object-metadata-adapter-byte-match-20261010.md).

## Target And Workflow

func_1502EC34: VA 0x1502EC34..0x1502EE8C, ROM 0x5C0E4..0x5C33C,
150 words / 600 bytes, frame 0x28. The production zero-return stub remains in
[generated_58F80.c](../../conker/src/game/generated_58F80.c).
The recovered signature is void(object, red, green, blue, opacity), with four
32-bit output pointers. Return-register value is not a contract.

Single Codex writer, zero Claude calls. Reuse the existing compiler, section
parser, strict guest interpreter, copied-owner asm processor, actual padder,
linked ELF slot parser and protected-data audit. No unrelated broad reruns,
OGL, Release, save/editor work, memory updates or push.

New authored tools:

- [Complete candidate driver](../../tools/experiments/game_object_color_mode_candidates.py).
- [Focused recovery suite](../../tools/tests/test_game_object_color_mode_recovery.py).

Reproduce from the repository root under WSL:

```sh
python3 -m tools.experiments.game_object_color_mode_candidates
python3 -m unittest tools.tests.test_game_object_color_mode_recovery -v
make tools-check
make -C conker match-progress NON_MATCHING=1
```

Ignored receipts live under conker/build/game-object-color-mode{-test}/.
The fresh immutable baseline is baseline.json plus before-0..before-4 in the
test directory. Historical adapter and curve baselines are not overwritten.

## Semantic Contract

- Mode 0 and modes above 7 leave outputs untouched, including invalid pointers.
- Mode 1 writes three object bytes in order, then reads word +0xA0. Unsigned
  values below 256 are direct opacity; larger values are float pointers.
  Preserve clamp comparisons, binary32 multiplication by protected 2.55f and
  truncation. Tests use finite, in-range conversion inputs, not NaN/FCSR claims.
- Modes 2/3 zero RGB, read +0xA5, store opacity, then reload mode +0xA4.
  An output alias can change that mode; caching it is observably wrong.
- Modes 4/5 capture the high packed byte once, reload packed RGB between
  preceding output stores, then load phase +0xA5. Call cosf with rounded
  phase * pi/128; preserve each rounded addition/multiply. Store first opacity
  before reloading blend byte +0xA7. The final product uses low 32 bits and an
  arithmetic right shift, including when first opacity exceeds 255.
- Modes 6/7 retain the first high byte but reload RGB and later phase under
  aliases. Opacity is 255 - ((phase * high) >> 8).

Cosine results are bounded callbacks with hostile caller-register clobbers,
not actual cosf implementation, native32, hardware, live rendering or FCSR
qualification. Valid byte phase inputs cannot reach the unsigned conversion
fixup; unreachable instructions are not counted as covered.

## Measurements And Qualification

Twenty complete/profile forms measured. Selected O2/g3 and O2 bodies emit
148 words / 592 bytes with frame 0x28, zero diagnostics and 32 new pool bytes.
Selected O1/g3 and O1 bodies emit 200 words / frame 0x38. Compact and clamp-if
forms lose the physical frame/shape. The selected isolated link has 77 word
differences against retail, including table-address and extent differences;
this is not a relocation-normalized remaining-scheduling count.

Seven tests pass in the final strengthened run: 7.039 seconds.

- 1,697 cases / 3,394 executions compare actual compiled C instructions and
  retail against an independent reference: all 256 modes, all 256 direct
  opacities, nine finite float samples, two stack phases and output/object
  aliases. Complete public memory and ordered public accesses/calls agree.
  Coverage reaches 139/150 retail and 137/148 compiled instruction addresses.
- Four actual compiled semantic negatives fail independently: cached mode,
  cached packed RGB, byte-truncated scaled opacity and unsigned blend shift.
- Retail private store homes are preserved: RA at SP+0x14, high byte at +0x1C,
  object home at +0x28. Modes 4/5 preserve all original input bytes, including
  private stack bytes, and ordered stack writes. Independent private read
  scheduling outside these claims remains unqualified.
- 65 public-access fault prefixes / 130 executions check the fault gate fired,
  ordered prefix and exact partial public memory. Four invalid-output-pointer
  cases prove no-output modes remain lazy. This is not an all-private fault audit.
- 144 cases / 288 executions connect the actual compiled helper to the banked
  linked 89-word adapter and 34-word fallback. Both are read from the current
  production ELF and verified against retail. Full original input memory,
  nested call arguments and adapter return agree. The helper runs in the
  diagnostic map; the production helper remains a stub.
- Actual copied-owner preprocess/compile/postprocess has zero diagnostics and
  preserves all 37 neighbor bodies and relative relocations, existing pool
  prefix, and every other actual padded owner byte.

## Installation Gates

Do not install this candidate or manufacture matching credit.

The isolated seven-entry table has case offsets 0x30, 0xD0, 0xD0, 0x108,
0x108, 0x1EC, 0x1EC. Retail's last pair is 0x1F0, 0x1F0. Fixed retail table
labels therefore enter modes 6/7 four bytes into the candidate case. The raw
body is also eight bytes shorter than the complete retail slot.

The actual copied owner relocates the new table through .rodata with addend
0x100. The preserved jtbl_80096DF8_game anchor requires 0x124 to address
jtbl_80096F1C. Blindly replacing the section symbol with the existing anchor
would read 36 bytes before the correct protected table. The actual padder
accepts the 592-byte body and emits fixed labels, but does not certify table
contents or case entry semantics. Padder success alone is not installation
acceptance. No recipe, inserted/omitted words or guard rows are authored here.

Protected seven-entry table remains at ROM 0x23B9DC; adjacent constants remain
D_80096F38 = 0x40233333 and D_80096F3C = 0x3CC90FDB. Do not rewrite protected
data or shift neighbors to accommodate compiler pools.

## Production And Bank

Source, whole ELF, guard manifest, conversion CSV and original rodata assembly
remain byte-identical to the fresh baseline. Source SHA-256:
c6bbcfe40be1b6d35f63bc839f306b17024835106691871e468eee1b42eeba54.
ELF SHA-256: 50b9240b6119092fed41e254f70be3a05346266151c5b77e337583eb7bcb1bd0.
Protected Game data remains exact: 189,088 bytes / 720 owners, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Fresh matcher confirms Game 2,750/4,816 (57.10%), total 3,423/5,489 (62.36%), zero address
drift / 2,066 different. Root README aggregate rows need no change.

Fresh tools-check passes. The scoped documentation/mirror validator checks
29 documents / 4,108 relative links with zero broken links, plus 42 authored
tools with byte-identical older mirrors and successful AST parsing in both
copies. Older HEAD and both tracked-dirty fingerprints remain unchanged.

Bank tools 64139c2bdd85a9127ded540b45fe53ef47e61322 first, then documentation
and consumer pin. Mirror only the two absent authored files to the older
checkout. Preserve its HEAD ddbdd16 and both tracked-dirty fingerprints;
its independent dirty work remains uncommitted. No push.

Manual graphify update exits 1, refusing shrink from 39,273 to 17,492 nodes.
Retention keeps 19,398 nodes from 2,972 excluded-but-existing files. Existing
0.9.20/0.9.26 and zero-node devcontainer.json warnings remain; no force, purge,
install or policy changes. Check the fresh consumer post-commit hook separately.

## Resume

1. Recover one complete form with the original frame/homes, case starts and
   150-word extent. Inspect mode 4/5 exit scheduling and mode 6/7 captured-high
   producer lifetime; preserve all qualified public ordering under aliases.
2. Qualify actual copied-owner pool relocation/addends at independent rebases.
   Normalize only certified scheduling/register choices with complete expected
   words and relocation guards; never copy a retail body as a generic recipe.
3. Qualify full private accesses/lifetimes and stale-word/relocation failures,
   then whole linked ELF target-only changes and protected data. Requalify the
   adapter and complete renderer against the actual installed helper.
4. Preserve the separate uninstalled curve handoff in
   [Note 1202](1202-game-owner-threshold-curve-squared-copy-and-physical-frame-gates-20261010.md).
   Its frame/private/slot gates and historical receipts remain unchanged.

The wider Game matching goal remains active.
