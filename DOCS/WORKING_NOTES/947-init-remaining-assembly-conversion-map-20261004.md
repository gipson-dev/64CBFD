# Init Remaining Assembly Conversion Map

Date: 2026-10-04. Starting HEAD: `b287786f`.

## Decision

Resume the requested Init assessment. **Some of the remaining assembly is
C-expressible, but no remaining replacement is ready for production adoption.**
The supported compiler-generated Init recovery queue is complete; the remaining
work is behavioral rewriting of custom leaves or connected assembly contracts,
not another broad batch of ordinary C recoveries.

The two small targets remain `func_10005BE0` and `func_100038E0`. The decoder
and glyph/formatter paths have experimental semantic C, but fitting and ownership
gates remain. Keep the handwritten boot, SDK and privileged/context owners.
Retaining intentional assembly is compatible with completing the decompilation;
100% C representation is not the same as complete or correct restoration.

Two pre-existing Game edits are preserved and excluded from this assessment:
`conker/src/game/generated_113D60.c` and
`tools/tests/test_game_event_sound_dispatch.py`. Their creator changes are
unfinished work, not newly qualified conversions in this note. No production
relink or aggregate regeneration was performed here.

## Current Inventory

Structured parsing of `conker/progress.init.csv` confirms 539 distinct entries:

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151,796 / 164,048 (92.53%) |
| Assembly | 47 | 12,252 |

| Group | Functions | Bytes | Conversion decision |
| --- | ---: | ---: | --- |
| Bitmap leaf | 1 | 76 | Small semantic-C candidate; full-slot match unresolved |
| MMIO leaf | 1 | 44 | Ordered volatile-C candidate; full-slot match unresolved |
| Connected decoder | 10 | 3,984 | Whole-chain conversion project; not independent helper replacements |
| Cleanup/debug/glyph | 5 | 1,308 | Connected interface, placement and stack work required |
| SDK thread queue leaves | 2 | 96 | Algorithms are C-expressible; retain SDK assembly and actual register interfaces |
| Hardware/context/setup | 8 | 4,376 | Retain machine-level operations and context contracts |
| Separated SDK assembly | 19 | 2,288 | Retain original SDK implementations; not a missing original-C queue |
| Boot entry | 1 | 80 | Retain handwritten clear-and-jump entry |
| Total | 47 | 12,252 | No newly adopted conversion |

SDK provenance is not a claim that every SDK algorithm is impossible in C.
For example, memory-copy/clear and thread-queue behavior can be expressed in C.
That alone does not preserve retail instruction behavior, privileged operations,
or nonstandard register interfaces, and does not justify replacing proven owners.

## Complete Remaining Map

Each row's address, extent, assembly source ownership and raw linked retail bytes
were checked in this assessment. The decisions use the established contract and
compiler evidence linked below, not a new compilation of every candidate.

| Entry | Bytes | Group |
| --- | ---: | --- |
| `func_10001000` | 80 | Boot |
| `func_100038E0` | 44 | MMIO candidate |
| `func_10005AB0` | 84 | Hardware/context |
| `func_10005B04` | 220 | Hardware/context |
| `func_10005BE0` | 76 | Bitmap candidate |
| `func_10005C2C` | 1,484 | Hardware/context |
| `func_100061F8` | 72 | Hardware/context |
| `func_10006240` | 28 | Decoder |
| `func_1000625C` | 208 | Decoder |
| `func_1000632C` | 84 | Decoder |
| `func_10006380` | 164 | Decoder |
| `func_10006424` | 1,028 | Decoder |
| `func_10006828` | 260 | Decoder |
| `func_1000692C` | 64 | Decoder |
| `func_1000696C` | 1,172 | Decoder |
| `func_10006E00` | 668 | Decoder |
| `func_1000709C` | 308 | Decoder |
| `func_100071D0` | 1,512 | Hardware/context |
| `func_100077B8` | 544 | Hardware/context |
| `func_100079D8` | 76 | SDK thread queue |
| `func_10007A24` | 20 | SDK thread queue |
| `func_10007A38` | 448 | Hardware/context |
| `__osCleanupThread` | 124 | Cleanup/debug/glyph, including interior entry |
| `func_10007C74` | 80 | Cleanup/debug/glyph |
| `func_10007CC4` | 100 | Cleanup/debug/glyph |
| `func_10007D28` | 120 | Cleanup/debug/glyph |
| `func_10007DA0` | 12 | Hardware/context |
| `func_10007DAC` | 884 | Cleanup/debug/glyph |
| `osMapTLBRdb` | 96 | Separated SDK |
| `bzero` | 160 | Separated SDK |
| `__osSetSR` | 16 | Separated SDK |
| `__osGetSR` | 16 | Separated SDK |
| `__osSetFpcCsr` | 16 | Separated SDK |
| `osInvalICache` | 128 | Separated SDK |
| `osInvalDCache` | 176 | Separated SDK |
| `__osDisableInt` | 32 | Separated SDK |
| `__osRestoreInt` | 32 | Separated SDK |
| `bcopy` | 784 | Separated SDK |
| `osWritebackDCache` | 128 | Separated SDK |
| `osGetCount` | 16 | Separated SDK |
| `osSetIntMask` | 160 | Separated SDK |
| `osWritebackDCacheAll` | 48 | Separated SDK |
| `osUnmapTLB` | 64 | Separated SDK |
| `osMapTLB` | 192 | Separated SDK |
| `sqrtf` | 16 | Separated SDK |
| `__osProbeTLB` | 192 | Separated SDK |
| `__osSetCompare` | 16 | Separated SDK |

The YAML directly owns `init_5AB0`, `bcopy` and `sqrtf` assembly. Other rows
resolve through their C owner's `GLOBAL_ASM` pragma. Do not assume every CSV
assembly row has a corresponding C wrapper or a separate nonmatchings file.

## Next Init Steps

1. **Bitmap `func_10005BE0`: best small fitting target.** Preserve captured
   start/end pointers, inclusive byte filling, the signed count reload after
   filling, partial-byte masking and alias timing. Require the complete
   nineteen-word slot, including the direct endpoint branch and increment delay
   slot. The taken-edge trial is twenty O2 words; the separate-final-store
   trial is thirty-four, or twenty-two with unrolling disabled. Neither fits.
   Develop a new compiler-shape hypothesis before running more
   variants; do not repeat equality, countdown or exit-edge forms unchanged.
   See [Note 944](944-init-bitmap-exit-edge-control-flow-trials-20261004.md).
2. **MMIO `func_100038E0`: second small target.** Preserve the ordered word
   publication of `0xBC000C02` to `0x80038070`, halfword publication of `0x4040`
   to `0x80038074`, then halfword write to `0xBC000C02`. Require all eleven
   words and exact access widths/order. Prior pointer-lifetime, volatility and
   published-address trials do not match. Do not invent a return type simply
   to force `$v0`; use a justified address-lifetime/scheduling hypothesis.
   See [Note 885](885-init-mmio-published-address-dataflow-trial-20261004.md)
   and [Note 919](919-game-linked-record-position-semantic-recovery-20261004.md).
3. **Decoder: reduce the complete connected image.** Its last qualified
   candidate is 4,512 executable bytes against 3,984 retail: 528 bytes excess.
   This is prior candidate-specific evidence, not a fresh size measurement.
   Shared registers and inherited stack slots prohibit treating the ten
   assembly entries as ordinary standalone helpers. Continue the existing
   candidate, then rerun both full guarded CU1 corpora after changes. Prove
   private-stack reservation and entry/frame ownership before adoption.
   See [Note 911](911-init-distance-operation-local-fitting-20261004.md)
   and [Note 943](943-init-resume-linked-baseline-and-conversion-shortlist-20261004.md).
4. **Glyph/formatters: qualify the whole calling path.** The 29-word C leaf
   fits its thirty-word body, but adapter/caller costs remain. The connected
   controls are 624 bytes / 48 stack, 608 / 80, and 624 / 64 against 412 retail
   bytes. The experimental address is occupied; inherited registers, interior
   entry and stack ownership remain gates. Fresh formatter tests below rerun
   the retained profiles; a fitted leaf alone is not a production conversion.
   See [Notes 933](933-init-glyph-adapter-production-placement-and-stack-boundaries-20261004.md),
   [935](935-init-shared-formatter-setup-text-stack-tradeoff-20261004.md) and
   [936](936-init-split-destination-validation-interface-trial-20261004.md).
5. **Adopt only after proof.** Change only the established source owner,
   preserve adjacent entries and addresses, perform a production relink,
   regenerate progress, and compare full Init code/data and Game data against
   checksum-verified retail. Change README aggregates only after an achieved
   conversion. Do not replace broad unmatched flow with instruction guards.

If both small leaves are eventually adopted, the conditional target is
494 / 539 C functions (91.65%) and 151,916 / 164,048 C bytes (92.60%), leaving
45 assembly entries / 12,132 bytes. These are prospective, not achieved totals.

## Fresh Verification

The existing linked ELF was independently parsed as ELF32 big-endian MIPS and
compared with pristine ROM after validating its SHA-1 against `conker.us.yaml`.
This is an existing-artifact check, **not a fresh production rebuild** and not
qualification of the pending Game source edits.

| Section | Address | Bytes | Different bytes |
| --- | --- | ---: | ---: |
| `.init` | `0x10001000` | 164,048 | 0 |
| `.init_data` | `0x800290D0` | 17,376 | 0 |

```text
.init       34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf
.init_data  a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239
```

All 47 retained slots match their raw retail bytes, without normalization,
and all 47 source owners resolve. The complete 189,088-byte Game-data section
also remains retail-exact across all 720 owners, verified by
`tools/check_game_data_layout.py` against the same existing ELF.

```sh
python3 -m unittest tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter -q -f
python3 tools/check_game_data_layout.py conker/build/conker.us.elf
```

**70 tests pass in 55.349 seconds, no skips.** Each freshly compiled bitmap
suite records 1,002 completed retail/C pairs and twelve bounded prefixes.
These and the connected formatter fixtures are bounded contract/model tests,
not whole-decoder corpus reruns, hardware execution or gameplay acceptance.

## Checkpoint

- [x] Recount 492 C / 47 assembly entries and classify every remaining row.
- [x] Resolve all retained source owners and compare all retained linked slots.
- [x] Verify complete existing Init code/data and Game data against retail.
- [x] Rerun seventy focused contract and retained compiler-profile tests.
- [x] Record which candidates are C-expressible versus production-ready.
- [ ] Establish a new bitmap fitting hypothesis and qualify all nineteen words.
- [ ] Establish a new MMIO hypothesis and qualify all eleven words.
- [ ] Resolve connected decoder/glyph fitting and ownership before adoption.

Only working documentation changes. Init source, compiler profiles, word
guards and README aggregates remain unchanged. The two pending Game edits
are untouched. No compressed-ROM promotion, sibling build, Release change,
hardware/gameplay acceptance or push is claimed.
