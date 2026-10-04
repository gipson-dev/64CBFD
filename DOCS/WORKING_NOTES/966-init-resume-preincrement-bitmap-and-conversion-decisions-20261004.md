# Init Resume: Preincrement Bitmap and Conversion Decisions

Date: 2026-10-04. Starting HEAD: `dc61e219`.

Subsequent Game checkpoint: [Note 968](968-game-texture-metadata-and-cache-maintenance-recovery-20261004.md)
qualifies and banks the separate metadata/maintenance edits described here as
pending. This note's Init measurements and rejected conversion decision stand.

## Answer

**Some remaining Init assembly can be expressed in C, but no remaining
replacement is ready to adopt.** Init remains 492 / 539 C functions (91.28%)
and 151796 / 164048 C bytes (92.53%). The 47 assembly entries total 12252
bytes. All 47 retained owners and raw slots, complete Init code/data and
Game data remain retail-exact after the resumed production build.

This assessment follows [Note 964](964-init-remaining-assembly-current-conversion-decisions-20261004.md).
The complete function-by-function classification remains
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md).

| Group | Entries / bytes | Decision |
| --- | ---: | --- |
| Bitmap `func_10005BE0` | 1 / 76 | C-expressible; full nineteen-word replacement remains unresolved |
| MMIO `func_100038E0` | 1 / 44 | C-expressible ordered volatile accesses; full eleven-word match remains unresolved |
| Decoder `func_10006240`..`func_1000709C` | 10 / 3984 | Connected C candidate exists; 4512 executable bytes including adapter, 528 over; stack/entry ownership unresolved |
| Cleanup/diagnostic/glyph path | 5 / 1308 | Partial C exists; best connected formatter is 608 versus 412 bytes, 196 over; caller/interior-entry/placement unresolved |
| Boot/hardware/context/SDK | 30 / 6840 | Retain original assembly and actual machine/register interfaces |
| Total | 47 / 12252 | Seventeen investigation targets, thirty intentional assembly owners |

Retention is a provenance and machine-interface decision, not a claim that
every SDK algorithm is impossible in C. Complete restoration need not mean
removing all intentional assembly.

## New Bitmap Hypothesis

Shape 20 in `tools/experiments/init_bitmap_ordered.c` biases the captured
unsigned address cursor down once, then increments before each byte store.
The loop compares the updated cursor directly with the captured endpoint.
This tests whether eliminating the saved old-cursor comparison can recover
retail's direct endpoint branch. It retains inclusive filling, wrapping o32
address arithmetic, captured endpoints and the signed count reload after
filling. The function remains void; no return contract or global read is
invented to force register allocation.

Fresh isolated IDO compilation and linking produce:

| Profile | Body words / retail | Different aligned positions | Frame bytes |
| --- | ---: | ---: | ---: |
| O2/g3 | 32 / 19 | 32 | 0 |
| O2/g3, no unroll | 20 / 19 | 20 | 0 |
| O1 | 32 / 19 | 32 | 16 |

The no-unroll form now uses `bne v0,v1`, but keeps an extra initial cursor
decrement and places the byte store in the branch delay slot. Retail instead
stores first and increments in the delay slot. Default O2 unrolls the fill
loop and grows to 32 words. **Reject production adoption.** This is a newly
measured rejected source shape, not an additional converted function.

Eight new tests freshly compile all three profiles. They qualify 501 completed
retail/C model pairs and six bounded reversed-range prefixes, covering counts,
remainders, sentinels, repeats, pointer/count storage aliases and wrapping
addresses. The alias oracle rejects an incorrectly hoisted count read; output
fences reject unauthorized stores. Each profile also passes 79 strict host
fixture cases. These are bounded model/fixture results, not hardware execution.

## Fresh Verification

The interrupted production build was resumed to terminal success rather than
restarted. Its command was:

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
```

The generated matcher reports Init 492 / 492 byte-exact C functions, zero
address drift and zero differing C functions. Inventory tests independently
verify all 539 entries, 47 ASM owners and every retained ASM slot. Raw full
section checks, without instruction normalization, report:

| Section | Bytes / owners | Different bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Init code | 164048 | 0 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| Init data | 17376 | 0 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |
| Game data | 189088 / 720 | 0 | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

**110 focused tests pass in 76.355 seconds, no skips.** This includes the eight
new bitmap checks and the 102-check Init assessment command from Note 964.
Retained bitmap controls and connected formatter profiles are freshly compiled,
MMIO is reassembled, and the decoder fitting check freshly confirms 4336 C
bytes plus 176 adapter bytes = 4512 executable bytes. Neither full guarded
decoder corpus is rerun. Older nineteen-word non-matching bitmap forms and
the historical MMIO C trial are not freshly recompiled in this assessment.

```sh
python3 -m unittest tools.tests.test_init_bitmap_preincrement tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -q -f
```

## Next Init Steps

1. Keep the proven assembly baseline. Do not run a broad conversion batch or
   change totals merely because a semantic experiment passes its fixtures.
2. For bitmap work, require a source hypothesis that explains both the direct
   endpoint branch and increment delay slot without shape 20's initial bias.
   Do not repeat this preincrement form unchanged. Older nineteen-word forms
   fit but still lack a complete match.
3. Keep MMIO as the second small candidate. Preserve its three ordered stores:
   word `0xBC000C02` to `0x80038070`, halfword `0x4040` to `0x80038074`, then
   halfword `0x4040` to `0xBC000C02`. Require the full eleven-word slot and
   access contract together; no extra reads or invented return interface.
4. For sustained connected recovery, reduce the existing decoder by at least
   528 executable bytes, including adapters. Then resolve private-stack and
   entry/frame ownership and rerun both complete guarded CU1 corpora.
5. Keep glyph/formatter fitting separate: close the 196-byte connected gap,
   interior-entry/caller-stack gates and occupied production placement.
6. Adopt only a completely qualified owner, relink, regenerate aggregates and
   verify neighbors plus complete Init code/data and Game data against retail.

## Interrupted Game Boundary

Three edits already existed when this Init assessment resumed:
`conker/include/variables.h`, `conker/src/game_305D0.c` and
`conker/src/game/generated_139FC0.c`. They correct two table widths and add
the metadata loader/cache-maintainer bodies requested by Note 965. The resumed
build succeeds with these edits, but their dedicated behavior and connected
cache-lifecycle tests are still pending. They are preserved and excluded from
this Init checkpoint; do not describe them as adopted or qualified recoveries.

## Checkpoint

- [x] Resume the production build to terminal success and preserve pending work.
- [x] Recount and classify every remaining Init assembly entry.
- [x] Verify every retained owner/raw slot and full Init code/data plus Game data.
- [x] Test a new preincrement compiler-shape hypothesis and record its rejection.
- [x] Pass 110 focused checks without skips.
- [ ] Qualify a complete small-leaf replacement before production adoption.
- [ ] Fit and qualify connected decoder/glyph ownership before conversion.
- [ ] Finish separate Game metadata/maintenance behavior and lifecycle tests.

Only isolated Init experiments, tests and working documentation are changed
by this assessment. No production Init owner, compiler override, word guard or
README aggregate changes. No sibling source/build, frozen Release, save, ROM
promotion, hardware/gameplay acceptance or push is included.
