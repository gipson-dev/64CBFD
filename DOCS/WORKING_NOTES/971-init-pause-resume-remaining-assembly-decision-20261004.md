# Init Pause Resume: Remaining Assembly Decision

Date: 2026-10-04. Starting HEAD: `6a9c3a1e`.

## Result

**Some remaining Init assembly is C-expressible, but no remaining replacement
is currently ready for production adoption.** Resume from the banked exact
baseline, not a broad conversion batch. The supported compiler-generated Init
matching queue is complete; the remaining candidates are handwritten leaves
or connected routines with nonstandard entry/stack contracts.

Fresh inventory and ownership checks confirm:

| Representation | Entries | Bytes |
| --- | ---: | ---: |
| C | 492 / 539 (91.28%) | 151796 / 164048 (92.53%) |
| Assembly | 47 | 12252 |

All 492 C entries were exact at the previous matching checkpoint. This run
independently verifies every retained ASM slot and the complete existing linked
Init code/data against checksum-verified retail. Intentional assembly is not
missing original C, and complete restoration does not require 100% C.

## Conversion Decisions

| Group | Entries / bytes | Can convert? | Adoption blocker |
| --- | ---: | --- | --- |
| `func_10005BE0`, bitmap fill | 1 / 76 | Semantic C is qualified in bounded fixtures | Best freshly checked form is 20 words versus 19; complete retail loop/delay-slot shape unresolved |
| `func_100038E0`, MMIO setup | 1 / 44 | Ordered volatile accesses can be expressed in C | No complete 11-word match; register/address lifetime and return-delay differences remain |
| `func_10006240` through `func_1000709C`, decoder | 10 / 3984 | Connected experimental C exists | 4336 C bytes + 176 adapter bytes = 4512 executable, 528 over; private-stack and entry ownership unresolved |
| Cleanup/diagnostic/glyph path | 5 / 1308 | Partial connected C exists | Best formatter connection is 608 versus 412 bytes, 196 over; interior entry, caller stack and occupied placement remain |
| Boot/hardware/context/SDK | 30 / 6840 | Some algorithms are C-expressible, but retain their original ASM owners | Original provenance and machine/register interfaces; not an ordinary C-conversion backlog |
| Total | 47 / 12252 | 17 investigation targets, 30 intentional ASM owners | No approved replacement |

The complete per-function ownership map is in
[Note 947](947-init-remaining-assembly-conversion-map-20261004.md).
The last new bitmap hypothesis is
[Note 966](966-init-resume-preincrement-bitmap-and-conversion-decisions-20261004.md).
The last new decoder experiment is
[Note 967](967-init-decoder-entry-value-lifetime-fitting-trials-20261004.md):
one-word savings in a public unit were absorbed by final alignment, so the
complete executable did not shrink. Neither rejected shape should be repeated
unchanged as a supposed new conversion attempt.

## Fresh Verification

**110 focused tests pass in 64.829 seconds, no skips.** An initial 18-test
inventory/MMIO/bitmap smoke run also passed; those checks overlap the 110 and
are not additional distinct coverage. The larger run freshly compiles retained
bitmap shapes, formatter profiles and both decoder fitting profiles, reassembles
the MMIO leaf, and checks all source owners and linked raw slots.

Fresh bitmap controls remain:

| Shape | O2/g3 words | O2/g3 no-unroll words | O1 words | Retail words |
| --- | ---: | ---: | ---: | ---: |
| Preincrement cursor | 32 | 20 | 32 | 19 |
| Right-shift fill-value mask | 20 | 20 | 33 | 19 |
| Address-difference induction | 22 | 22 | 33 | 19 |

The preincrement form retains an extra initial bias and stores in the branch
delay slot; retail stores first and increments in that slot. Older 19-word
non-matching forms are not freshly recompiled here. MMIO's original three-store
contract is rechecked, but historical MMIO C matrices are not rerun:
word `0xBC000C02` to `0x80038070`, halfword `0x4040` to `0x80038074`, then
halfword `0x4040` to `0xBC000C02`. An extra global read or invented return
contract is not an acceptable way to force compiler register allocation.

Existing linked artifact checks, without instruction normalization:

| Section | Bytes / owners | Different bytes | SHA-256 |
| --- | ---: | ---: | --- |
| Init code | 164048 | 0 | `34372ebc8b2e56b5b6c02c8b88ce33a1558d5d329397fdc6e9e984333df6d4bf` |
| Init data | 17376 | 0 | `a3d3d56157fd9f9feb00a48a526c50ec51227b5a5afc277aa9a4b765c8fc6239` |
| Game data | 189088 / 720 | 0 | `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670` |

No fresh production relink or complete guarded decoder corpus run is claimed.
Bounded instruction models and native fixtures are not hardware/gameplay proof.

```sh
python3 -m unittest tools.tests.test_init_bitmap_preincrement tools.tests.test_init_bitmap_fill_value_mask tools.tests.test_init_bitmap_address_difference tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_equality_exit tools.tests.test_init_bitmap_exit_edge tools.tests.test_init_bitmap_unsigned_induction tools.tests.test_init_mmio_assembly tools.tests.test_init_bitmap_assembly tools.tests.test_init_bitmap_allocator_contract tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_decompressor_storage_boundaries tools.tests.test_init_startup_thread_contract tools.tests.test_init_glyph_formatter_semantic tools.tests.test_init_glyph_adoption_boundaries tools.tests.test_init_glyph_adapter tools.tests.test_init_decompressor_distance_operation_local.InitDecompressorDistanceOperationLocalTests.test_packed_profile_size_reduction -q -f
```

## Where To Continue

1. For the nearest small conversion, investigate `func_10005BE0` only with a
   new hypothesis for the captured-endpoint branch and increment delay slot.
   Preserve inclusive filling, wrapping address arithmetic, aliases and the
   late signed count reload. Require all 19 retail words before adoption.
2. Keep `func_100038E0` second. Seek source/provenance evidence for address
   lifetime and scheduling while retaining exactly the three ordered stores,
   their widths, and the void interface. Prior pointer/volatility/address-read
   matrices are already negative evidence, not new work.
3. For sustained Init work, prioritize complete decoder fitting. Reduce at
   least 528 executable bytes, counting every adapter and actual allocation.
   Measure direct-call units separately from public symbol regions, which can
   contain unnamed helpers. Resolve private-stack reservation and shared-entry
   ownership, then rerun both complete guarded CU1 corpora before placement.
4. Treat glyph/formatter recovery as its own connected task. Close the 196-byte
   gap and prove interior-entry/caller-stack ownership and nonoverlapping
   placement; a fitted glyph leaf is insufficient.
5. Adopt only a fully qualified owner, relink, regenerate progress, and compare
   adjacent slots plus complete Init code/data and Game data against retail.
   Only then update README aggregate totals.

## Interrupted Work Boundary

Two Game paths were already modified at resume:
`conker/src/game/generated_139FC0.c` and
`tools/tests/test_game_queued_segment_writer.py`. They contain the pending
`func_1510CDB8` color-emitter recovery and incomplete test extensions. They are
preserved unchanged and excluded from this Init assessment. Do not describe
that Game recovery as banked or completely qualified by these Init checks.

- [x] Resume from the actual banked HEAD and preserve interrupted edits.
- [x] Recount/classify all 47 Init ASM owners and verify every raw slot.
- [x] Freshly rerun 110 focused checks without skips.
- [x] Verify complete existing Init code/data and Game data against retail.
- [x] Separate semantic candidates, adoption blockers and intentional ASM.
- [ ] Qualify a complete small-leaf replacement before changing ownership.
- [ ] Fit and qualify connected decoder/glyph entry and stack ownership.
- [ ] Finish the separately pending Game color-emitter tests and checkpoint.

Only working documentation changes in this assessment. Production Init owners,
compiler profiles, word guards and README aggregates remain unchanged. No sibling
source/build, frozen Release, saves, ROM promotion or push is included.
