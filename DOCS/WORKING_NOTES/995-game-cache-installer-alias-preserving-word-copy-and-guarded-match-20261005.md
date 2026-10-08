# Game Cache Installer Alias-Preserving Word Copy And Guarded Match

Date: 2026-10-05. Starting HEAD: `7475566c`.

Follow-up: [Note 996](996-game-cached-lookup-frame-and-guarded-miss-path-match-20261005.md)
completes the next lookup match with twelve checked miss-path guards, retaining
this installer's alias gates and connected code. Counts below are this note's
historical checkpoint.

## Result And Scope

`func_1502AB04`'s complete 97-word / 388-byte linked slot now matches retail
using its recovered C body and 41 expected-word guards. **This is a guarded
match, not a direct compiler match.** Default IDO O2/g3 emits all 97 body
words with the original 0x28 frame and 41 raw differences. No padding,
instruction insertion/omission, profile override, ABI or data-layout change
is introduced. All branch/jump/call words are unchanged before guarding.

Source: `conker/src/game_57FA0.c`. Entry/end: `0x1502AB04..0x1502AC88`.
Retail ROM: `conker/conker.us.bin+0x57FB4..0x58138`.
Unguarded C slot SHA-256:
`a6bca817be8a9ee74df0bc7e91206bd401525478a5f4c39ffb832a9eed82a9bf`.
Guarded/retail slot SHA-256:
`5a09e7939b851c8e3d0a343734616143e0bf832772738360c854b73d30fdc22e`.

## Source And Alias Contract

[Note 994](994-game-cache-installer-frame-recovery-and-pair-copy-alias-gate-20261005.md)
recovered the frame/count lifetime but retained an 87-word scalar body with
74 differences. Its raw-exact two-word aggregate copy failed the native
partial-overlap witness: descriptor 215 instead of retail/scalar 115.
That rejected form remains a regression control, not the selected source.

The selected source uses a local four-byte `AssetTableWord57FA0` view for
the offset copy, followed by the separate scalar descriptor assignment.
On the qualified word-aligned inputs, each word copy is either disjoint
or fully overlapping; it does not combine the two live input reads into
one overlapping aggregate assignment. The explicit count local, generation
and address updates, sixteen-entry cache alias and original `bcopy` call
remain intact. Metadata assignment order is generation then address.

The one-word copy gives IDO the original memory-copy load/store shape and
separate offset-field induction pointers. The four-record unroll fits all
97 words naturally. All first 37 words and all final six words emit directly;
56 of the complete 97 words agree without guards. The 129-form source screen
reproduces the chosen body and immutable earlier controls with no diagnostics.
Its sole raw-exact aggregate trial is still rejected for alias behavior.

## Guard Classification

The [patch table](../../conker/retail_word_patches.us.csv) and independent
[match tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_cache_installer_match.py) pin every
expected and replacement word.

| Group | Guarded Words | Effect |
| --- | ---: | --- |
| Peeled iteration, 0x94..0xB0 | 7 | Descriptor temporary, pointer-update timing and independent descriptor/address/generation stores |
| Bulk address setup, 0xB8..0xC4 | 4 | Closed t6/t7 address/index temporary allocation |
| Bulk body, 0xF0..0x168 | 30 | Descriptor temporaries, induction update timing and independent stores |

The peel stores all three descriptor/address/generation fields before the next
offset read in both forms. Moving v0/v1 updates changes only the equivalent
base/displacement spelling of those field addresses. The bulk loop applies
the same reasoning to each of its four records: the offset store precedes
that record's descriptor read, then the remaining three field stores finish
before the next offset read. Every four-record iteration advances pairs by
0x20, each cache induction pointer by 0x40 and address by four additions of 8.
The final pointer/count comparisons and all delay-slot branches are retained.

This is broader than register renaming alone: independent stores and pointer
updates also move. Qualification therefore verifies disjoint write intervals
between identical read events, rather than falsely claiming raw ordered-store
identity. No call, branch, load count, field value or effective memory address
is replaced with different semantics.

Two guards preserve address relocations explicitly: offset 0xB8 retains
`R_MIPS_HI16:D_800C3D68`, and 0xBC retains `R_MIPS_LO16:D_800C3D68`.
Their expected/replacement words are unlinked words with zero low immediates;
the fixed-address linked check independently retains the resolved immediates.
All nine object relocations, including the bcopy call and cache end-pointer
addend, are pinned. Other guards require no relocations. The table contains
10579 rows with no duplicate owner/function/offset keys. All guards allow
neither insertion nor omission.

## Qualification

The new match module adds five checks: full raw/guarded slot identity and
unchanged control words; full-word read-window traces; every omitted-guard
rejection; all unlinked guard inputs/relocations; and production source/table/
linked identity. It reuses the bounded big-endian low-word runner and byte-copy
callback from Note 994. This is not an emulator/hardware or real SDK bcopy
qualification.

- 2550 three-way cases compare retail, freshly compiled raw C and guarded C:
  three data patterns, all 833 in-bounds cache input aliases per pattern and
  seventeen external/NULL-zero-count cases per pattern, for counts 0..16.
- All 97 words are visited in each form. Saved-register restoration, exact
  copy-call arguments, complete mapped memory including stack/fences, and
  ordered reads including values agree.
- The trace groups stores between successive reads. It asserts every pair
  of write intervals in a group is disjoint, then compares the identical
  address/size/value multiset and following read event. This permits only
  commuting stores, not overlapping writes or movement across a live read.
- Guarded ordered stores agree exactly with retail. Raw ordered stores can
  differ only inside those verified independent-write windows.
- Omitting each of the 41 guards is rejected by a mapped-access/instruction-
  budget check or complete memory/read/call/window comparison. External and
  aliased witness inputs exercise peel and bulk counts through sixteen.
- The native 833-alias matrix, partial-overlap rejection, earlier scalar/word
  compiler controls and previous 2550 scalar/word/retail traces remain intact.
  The actual lookup/block/variadic/relocator connection fixture uses the new
  production source and applies only the checked cache guards when comparing
  freshly compiled code to the linked production object.

Changing the shared patch table triggers a full consumer rebuild, which
succeeds. Production matches all 97 cache-installer words, while the block
and variadic loaders remain directly exact and the relocator retains its
existing seventeen-guard match. Existing source and duplicate generated-slice
recipe warnings remain; no new isolated compiler diagnostics are introduced.

**All 176 final combined checks pass in 70.002 seconds, no skips.** Complete
Init code (164048 bytes), Init data (17376 bytes), Debugger code and Game data
(189088 bytes / 720 owners) remain retail-exact. `make tools-check` and
`git diff --check` pass.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_cache_installer_candidates
python3 -m unittest tools.tests.test_game_cache_installer_match tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Progress And Next

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3291 / 5463 (60.24%) | 0 | 2172 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2618 / 4790 (54.66%) | 0 | 2172 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is a new guarded byte match, not a new C conversion or Init ASM reduction.
README edits contain aggregate totals only; detailed qualification stays here
and in the dedicated status/update/roadmap pages. The 47 retained Init assembly
functions are unchanged.

Read-only sibling audit finds translated retail `func_1502AB04` in
`64CBFDOGL/recomp_out/.c:202014`, including the frame and sequential pair
load/store sequence. No host synchronization is needed for this matching
change. No sibling source, build, save or frozen Release changes are made.
Real SDK copy, cache/DMA, PC runtime and rendering acceptance remain separate.
Counts outside 0..16, unaligned/invalid pointers and unsupported extents remain
unqualified; the supported partial-overlap domain is not narrowed.

Next connected target: cached lookup `func_1502AC88`, 158 / 159 body/slot words,
156 raw differences, frame 0xA0 in both forms. Begin with retail's cache-hit
record rotation and live generation/output-alias behavior; keep its miss-path
DMA alignment and the actual cache/block/variadic/relocator fixture intact.
