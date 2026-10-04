# Game Physical Data Order And Literal Pool Restoration

Date: 2026-10-04. Starting HEAD: `3c193f44`.

## Result

The Game-data placement gate from
[Note 939](939-game-curve-update-direct-match-and-data-placement-gate-20261004.md)
is resolved in a freshly rebuilt production ELF. The complete physical
`.game_data` image at **0x80082B20**, **189,088 bytes / 0x2E2A0**, equals
checksum-verified retail with **zero different bytes across all 720 owners**.
No relocation normalization or expected-word replacement is used for this
data comparison. This is static linked-image acceptance, not guest gameplay.

The pan coefficient at **0x800A1350 is now 0x3EDCEE77**, not 0x4675E800.
The curve builder/update remain directly exact across 194/212 words, with
unchanged addresses and no new instruction guards. A fresh full link succeeds.

## Cause And Repair

Splat's generated linker script groups all `.data` owners before all `.rodata`
owners. Retail interleaves these owners. Absolute symbol aliases did not fix
the physical data displacement. `restore_game_data_order` now follows the
tracked YAML's ROM order, anchors each owner's physical address and checks
that its linked contents do not exceed the declared retail span.

The repair validates the complete owner inventory, rejects missing/extra/
duplicate and unrecognized selectors, rejects malformed or overlapping YAML
spans, and changes only `.game_data` input subalignment to four bytes. Explicit
anchors preserve retail's eight-byte boundary at ROM 0x236578. It is idempotent
and leaves unrelated linker sections unchanged.

The first strict link exposed these five input-size discrepancies:

| ROM owner | Retail bytes | Previous input bytes | Resolution |
| --- | ---: | ---: | --- |
| 0x236578 table | 56 | 64 | Target-specific assembler `-no-pad-sections` |
| 0x23D870 perspective pool | 16 | 0 | Restore standalone original rodata owner |
| 0x23D880 rotation pool | 16 | 0 | Restore standalone original rodata owner |
| 0x23D890 angle conversion pool | 16 | 0 | Restore standalone original rodata owner |
| 0x23D8A0 angle result pool | 32 | 0 | Restore standalone original rodata owner |

The table contains fourteen actual source words. Ordinary MIPS assembly pads
its `.data` section to 64 bytes; omitting the targeted flag reproduces exactly
eight trailing zeros outside its retail span. The flag changes padding, not
table contents, symbols or instruction generation. Other objects keep their
existing assembler flags.

The four recovered C owners read fixed external data symbols and emit no
`.rodata` sections. The YAML now assigns the original 80 pool bytes to generated
assembly data owners. Their C bodies are untouched. A stale ignored generated
linker script still selecting the empty C pools is repaired to the same new
selectors, with duplicate/missing-owner checks retained. The linker target now
depends on the YAML as well as the patch tool.

Generated `conker.ld` and assembly data remain ignored under the repository's
existing convention. The committed YAML and tool/Makefile changes are the
authoritative repair. A disposable full Game-data extraction recreates all four
pools and the table, then independently assembles and compares all five spans
against retail. No manual generated-file edits are required to reproduce them.

DATA/RODATA linker markers now describe the initial data prefix and the mixed
remainder in retail order, not totals of all scattered section types. No source
consumer of these markers was found; the build extracts the complete output
section rather than using those markers as a split boundary.

## Full Comparison And Text Effects

The preserved pre-edit artifact `game-data-before-6b5593d7.elf` fails the new
auditor: **189,024 versus 189,088 bytes**, **146,080 different byte positions**
(including the absent 64-byte tail), and all 720 owner spans differ. This is
a measured artifact comparison, not a claim about when the grouping bug began.

The rebuilt data SHA-256 is:

```text
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670
```

Five Game instruction words change through corrected data relocations; all
five now equal their raw retail words. They account for six changed code bytes:

| Instruction address | Before | Rebuilt / retail |
| --- | --- | --- |
| 0x15001074 | 0x3C018008 | 0x3C018009 |
| 0x1500107C | 0x8C2E6010 | 0x8C2E1AB8 |
| 0x150A8454 | 0xAC29CC7C | 0xAC29857C |
| 0x150A9028 | 0xAC29CC7C | 0xAC29857C |
| 0x150A9754 | 0x2631CC7C | 0x2631857C |

Complete Init code (164,048 bytes), Init initialized data (17,376 bytes), and
Debugger code (19,800 bytes) remain byte-identical to the preserved baseline.
Both current Init sections are also directly compared with retail and exact.
Game code keeps its original 2,072,880-byte extent; only the five words above
differ from the preserved code image. No broad text conversion or guard change.

## Verification

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 tools/check_game_data_layout.py conker/build/conker.us.elf
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
make tools-check
```

All **53 focused tests pass in 12.141 seconds, no skips**. Layout/auditor coverage
includes a real synthetic MIPS link at the eight-byte boundary; a deliberate
oversized owner that fails linking; duplicate/missing/unknown owners; malformed
YAML and ELF rejection; checksum rejection; complete byte/length/address checks;
CLI success/failure receipts; display limits that do not reduce comparisons;
padding-flag negative control; and fresh disposable extraction. The existing
32 curve/emitter/helper tests also pass. Project tool checks pass.

Fresh instruction classifier: total 3278 / 5463 exact, Init 492 / 492, Game
2605 / 4790 and Debugger 181 / 181; zero instruction-address drift and 2185
different Game rows. These counts and source-representation totals are
unchanged. README aggregate rows were checked and already agree, so no edit.
The existing duplicate-recipe and compiler warnings remain; the full build
finishes successfully despite them.

Both before and repaired ELF/map evidence are preserved under ignored build
storage. Repaired checkpoint: `conker/build/game-data-fixed-20261004.elf` and
`.map`; copying refused to overwrite a different existing checkpoint.

## Next Work

- [x] Audit owner ordering and exact object spans before another conversion.
- [x] Qualify the table's padding and restore all four missing literal pools.
- [x] Rebuild, check every physical Game-data byte, and retain rejecting tests.
- [x] Confirm Init preservation, both curve matches and fresh aggregate counts.
- [ ] Resume semantic Game recovery at `func_150E81A8`, the next verified
  zero-return placeholder in `generated_113D60.c`; preserve neighboring
  assembly owners `func_150E7FEC` and `func_150E83AC`.
- [ ] Qualify actual guest execution separately before claiming gameplay or
  hardware acceptance for the restored curve/dispatch path.

No guest launch, compressed-ROM promotion, sibling-port build, Release change
or push. Init conversion gates from Notes 940/941 are unchanged; the prior
missing-production-ELF boundary is superseded by this successful repair.
