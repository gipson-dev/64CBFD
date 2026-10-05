# Init Pause-Resume Current Conversion Readiness

Date: 2026-10-05. Starting HEAD: `3b672c6f`.

## Decision

Resume the user's remaining-Init assessment, not the interrupted Game light
selector experiment. **Some remaining Init assembly can be expressed in C,
but none of the retained replacements is ready for production adoption.**
The ordinary compiler-generated Init recovery queue is finished. Remaining
work involves handwritten leaves, connected shared-entry routines and
intentional machine-level implementations. Do not start a broad conversion
batch or count experimental C as completed production ownership.

This refresh supersedes the conversion shortlist in
[Note 976](976-init-remaining-conversion-decision-and-decoder-cache-matrix-20261004.md)
with the bitmap and MMIO evidence from
[Note 981](981-init-bitmap-record-view-fitting-and-ordered-read-qualification-20261005.md)
and [Note 978](978-init-mmio-record-view-fitting-and-ordered-access-qualification-20261005.md).
The complete retained-function map is in
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md); its older
528-byte decoder gap is superseded by the current **512-byte** gap below.

## Fresh Inventory

Structured parsing of `conker/progress.init.csv` and the retained-owner audit
confirm all 539 unique, contiguous entries and every selected assembly owner.

| Representation | Functions | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151796 / 164048 (92.53%) |
| Assembly | 47 | 12252 |

| Remaining group | Entries / bytes | Current decision |
| --- | ---: | --- |
| Bitmap `func_10005BE0` | 1 / 76 | C-expressible; optimized record-view body fits 19 words but differs at 17 positions |
| MMIO `func_100038E0` | 1 / 44 | Volatile C preserves access order; direct record body fits 11 words but differs at 9 O2/g3 or 8 O1 positions |
| Connected decoder | 10 / 3984 | Semantic C exists; complete C plus adapter is 4496 bytes, 512 over |
| Cleanup/debug/glyph | 5 / 1308 | Partly recovered connected C; best formatter connection is 608 versus 412 bytes, 196 over |
| Intentional boot/SDK/hardware/context | 30 / 6840 | Keep original assembly provenance and machine interfaces |
| Total | 47 / 12252 | 17 investigation targets, 30 intentional assembly entries; no newly adopted conversion |

The ten decoder entries are `func_10006240`, `func_1000625C`,
`func_1000632C`, `func_10006380`, `func_10006424`, `func_10006828`,
`func_1000692C`, `func_1000696C`, `func_10006E00` and `func_1000709C`.
They share entry/register/frame contracts and are not independent ordinary
C functions that can be promoted one at a time.

The five cleanup/debug/glyph entries are `__osCleanupThread`,
`func_10007C74`, `func_10007CC4`, `func_10007D28` and `func_10007DAC`.
The 608-byte figure describes the experimental formatter/writer connection,
not a replacement for all 1308 bytes of this group. The fitted 29-word glyph
writer alone does not close adapter, interior-entry or caller-stack gates.

Intentional assembly includes the boot clear-and-jump entry, CP0/FPU/cache/TLB
operations, exception and thread-context machinery, and original SDK leaves.
Some SDK algorithms are C-expressible; retaining their proven handwritten
implementations is a provenance/interface decision, not a claim of impossibility.
Complete restoration does not require artificial 100% C representation.

## Pick Up Here

1. **Bitmap first: recover the loop and tail, not merely size.** The current
   grouped view fits the body but still emits an XOR comparison, pre-branch
   increment and delay-slot store. Retail stores first, compares the captured
   pointers directly, then increments in the branch delay slot. A new isolated
   compiler-shape trial must explain that difference while retaining inclusive
   filling, captured endpoints, wrapping arithmetic, aliases, late signed-count
   reload and the two-based partial-byte mask. Do not repeat existing qualifier,
   equality/countdown, all-ones-mask or grouped-field trials unchanged. Require
   the complete nineteen-word schedule and existing contract tests before
   replacing its owner inside `conker/asm/init_5AB0.s`; preserve the exception
   entry at `0x10005C2C`. Standalone text is still 80 bytes after alignment,
   so a 76-byte body is not a complete allocation saving by itself.
2. **MMIO second: require a new address-lifetime/provenance hypothesis.** Keep
   exactly three stores: word `0xBC000C02` to `0x80038070`, halfword `0x4040`
   to `0x80038074`, then halfword `0x4040` to `0xBC000C02`. Grouped addressing
   currently rematerializes the hardware destination and changes the schedule;
   it is not only a register rename. Keep the void interface, add no reads and
   do not invent a return contract to force V0. Require all eleven words and
   ordered-access checks before changing `conker/src/init_38E0.c`'s ASM owner.
3. **Decoder is sustained connected work.** Freshly reproduce the byte-depth
   lead: O2/g3 C text 4320 plus actual adapter 176 equals 4496 executable bytes.
   Remove another 512 complete bytes, counting helpers, padding and adapter.
   O1 is 5792 plus 176 equals 5968 bytes and is not a fitting alternative.
   Original entry/frame/placement and complete private-stack reservation remain
   open. [Note 979](979-init-byte-depth-full-masked-cu1-corpus-qualification-20261005.md)
   records 507 retail pages in each masked CU1 mode for the unchanged lead;
   those full corpora were not rerun here. Requalify both after a candidate change.
4. **Formatter is a separate connected conversion.** Close the 196-byte gap
   and prove nonstandard registers, interior entry, caller-stack regimes and
   nonoverlapping production placement. Experimental address `0x10009000`
   is occupied by production `func_10008F90`; it is not free space. A semantic
   leaf that fits cannot bypass these connection gates.
5. **Only then adopt.** Change the established source owner, rebuild/link
   production, regenerate progress and compare adjacent slots plus complete
   Init code/data and Game data. Update README aggregate rows only after an
   actual conversion. No broad instruction normalization replaces these gates.

- [x] Recount and classify all 47 retained assembly entries.
- [x] Verify actual source owners, all raw slots and complete existing Init/data.
- [x] Recompile bitmap/MMIO and connected formatter fixtures and rerun contracts.
- [x] Freshly reproduce current byte-depth sizes and pinned instruction hashes.
- [ ] Recover and qualify a complete bitmap or MMIO replacement before adoption.
- [ ] Close decoder/formatter size, entry, placement and stack ownership gates.

## Fresh Verification

**138 focused checks pass in 68.289 seconds; two additional byte-depth size
and disabled-option identity checks pass in 2.070 seconds. Both exit zero,
with no skips: 140 passing checks total.** These rerun existing tests; no new
test coverage or conversion is claimed.

The focused run freshly compiles the grouped bitmap views and all twelve MMIO
shape/profile images. Their retained receipts report 1002 completed ordered
bitmap pairs plus twelve bounded prefixes, and sixty ordered MMIO pairs.
The six formatter profiles freshly reproduce allocated text sizes of
624/704, shared 608/688, and split 624/720 bytes for O2/O1 respectively.
The separate byte-depth checks compile current connected shapes in both
profiles, include the actual adapter and pin the retained instruction hashes.
The focused run also checks the earlier distance-operation control separately;
its 4512-byte image is not confused with the best 4496-byte byte-depth lead.

The retained-owner tests validate the pristine ROM checksum, source ownership
and all 47 raw slots. Against the existing linked `conker/build/conker.us.elf`:

| Section | Bytes | Different bytes |
| --- | ---: | ---: |
| Init code | 164048 | 0 |
| Init data | 17376 | 0 |
| Game data, 720 owners | 189088 | 0 |

These are existing-artifact checks and bounded instruction/model fixtures,
not a fresh production relink, full decoder corpus, real-hardware or gameplay
acceptance. Detailed commands and fixture boundaries for the 138-check run
are the combined command in Note 981. Additional command:

```sh
python3 -m unittest tools.tests.test_init_decompressor_builder_byte_level.InitDecompressorBuilderByteLevelTests.test_packed_profile_size_reduction tools.tests.test_init_decompressor_builder_byte_level.InitDecompressorBuilderByteLevelTests.test_disabled_option_keeps_banked_packed_instruction_images -q -f
```

## Preserved Work

The starting dirty scope is the paused Game experiment:
`tools/experiments/game_light_selector_candidate.c`,
`tools/tests/test_game_light_selector_candidate.py`, and
`tools/tests/test_game_viewport_renderer.py`. All three remain untouched and
excluded from this documentation checkpoint. Its production owner remains a
placeholder; this Init assessment does not qualify or adopt that experiment.

Only working documentation changes. Production Init sources, profiles,
guards, README aggregates, sibling sources/builds, frozen Release and saves
remain unchanged. No ROM promotion or push is included.
