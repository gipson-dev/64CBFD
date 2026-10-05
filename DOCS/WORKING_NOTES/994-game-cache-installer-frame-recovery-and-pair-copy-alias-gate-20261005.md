# Game Cache Installer Frame Recovery And Pair-Copy Alias Gate

Date: 2026-10-05. Starting HEAD: `1c640686`.

## Adopted Progress

`func_1502AB04` now emits retail's complete first 19 words, including the
0x28 frame, saved s0/s1/s2/ra, count preserved in s2 across `bcopy`, and address
saved/restored at sp+0x34. The source copies the first argument into an explicit
local `count`; the existing scalar offset/descriptor assignments and loop stay
intact. This recovers the original lifetime without changing the ABI, data
layout, calls, profile or patch table.

**Production remains non-matching:** 87 body words in the 97-word slot,
74 raw differences, down from 93. No new exact function or C conversion is
claimed. Entry/end: `0x1502AB04..0x1502AC88`. Retail ROM:
`conker/conker.us.bin+0x57FB4..0x58138`.

| Source | Body / Slot Words | Frame | Differing Words |
| --- | ---: | ---: | ---: |
| Previous scalar source | 87 / 97 | 0x20 | 93 |
| Adopted scalar source with count local | 87 / 97 | 0x28 | 74 |
| Two-word pair copy with count local | 97 / 97 | 0x28 | 6 |
| Pair copy, generation assignment first | 97 / 97 | 0x28 | 0; rejected |
| One-word offset copy, scalar descriptor | 97 / 97 | 0x28 | 41; experimental |

Previous padded C slot SHA-256:
`9411056ee2483732bfd3b404b7ab27b514a0af4c614b62c554dbe125f1b0719a`.
Adopted padded C slot SHA-256:
`6acec640d1eb26a525a32a799d53abb2effeb9336ed73ec7fb4bc931e32ebad0`.
Retail slot SHA-256:
`5a09e7939b851c8e3d0a343734616143e0bf832772738360c854b73d30fdc22e`.

## Compiler Screen

[game_cache_installer_candidates.py](../../tools/experiments/game_cache_installer_candidates.py)
screens 128 named forms under the existing default IDO O2/g3 profile. All
compile without diagnostics. The immutable baseline is retained independently
of the current production source. The driver checks both the selected count-local
source and the unchanged cache layout before writing reports under ignored
`conker/build/game-cache-installer/`.

Forms cover scalar versus aggregate copies, pair/index types, local versus
parameter count lifetimes, declaration/tag order, typed input/destination
cursors, address update placement, metadata assignment order and volatile
trials. The parameter `register` hint alone does not recover s2. The explicit
count local does. A two-word offset/descriptor view produces retail's separate
field induction pointers and four-record unroll; generation-first assignment
resolves its last three pairs of independent metadata-store scheduling words.

Exactly one named form, `local-generation-first`, emits all 97 words directly.
**It is not adopted**, because compiler identity alone does not preserve the
already-supported native alias behavior described below. This is not a claim
that every experimental form is semantically qualified. Volatile and oversized
trials are likewise not production changes.

## Partial-Overlap Rejection

The cache is sixteen 16-byte records. Existing tests already permit input
word pairs to alias that cache and require reads after the initial shift.
Expanded tests cover every in-bounds word-aligned cache input span for counts
0..16: 833 cases. The scalar source and the one-word-copy trial agree throughout.

Concrete witness: count 1, input `((u32 *)D_800C3D68) + 61`, generation 41,
address `0xFFFFFFF8`. With the existing fixture, entry 15 starts with generation
115 and offset 215. The input pair is its generation followed by its offset;
the destination pair is its offset followed by its descriptor.

Retail and scalar code load 115, store it into the offset, then read the
now-overwritten offset as the descriptor. Final offset/descriptor: **115/115**.
The native aggregate assignment captures both input words before writing
either destination word. Final offset/descriptor: **115/215**. Partial aggregate
assignment overlap is not a portable C contract; the observed native result
is a concrete rejection witness, not a guarantee for all compilers.

The freshly linked IDO aggregate candidate is statically retail-exact. That
does not establish equivalent source behavior on the native compiler. The
expanded alias gate is retained instead of excluding the failing input case
or treating an exact-match counter as acceptance. No host transplant is made.

## Qualification

[test_game_cache_installer_candidates.py](../../tools/tests/test_game_cache_installer_candidates.py)
adds five checks: fresh compiler controls and prologue identity; the partial
overlap rejection; all 833 native one-word-copy aliases; production source
selection; and complete three-way instruction traces.

The latter reuses the existing bounded big-endian low-word runner and models
only the byte-copy callback. It clobbers caller-saved integer registers, checks
mapped loads/stores and relies on the runner's saved-register checks. It does
not execute the real SDK `bcopy` or claim hardware/runtime acceptance.

2550 three-way cases compare retail, adopted scalar C and the experimental
one-word-copy C: three distinct data patterns, all 833 cache aliases per pattern
and seventeen external/NULL-zero-count cases per pattern. Copy-call arguments,
ordered non-stack reads including values, and complete non-stack memory agree.
All 97 retail words, all 87 scalar body words and all 97 word-copy words are
visited. Stack scratch bytes and void-return temporaries are not compared;
callee-saved register restoration is checked in each run.

Metadata/descriptor store schedules can differ between reads. The test does
not mislabel them as ordered-store identity: it checks actual subsequent read
values and complete final mapped memory. No scheduling guards are introduced.
The one-word candidate's 41 remaining differences are not yet independently
qualified as a closed guarded normalization and remain experimental.

The actual-source cache/lookup/block fixture also adds an independent native
833-case scalar simulation. Connected cache/lookup/block/variadic/relocator
fixtures remain intact. Fresh production rebuild succeeds and confirms
unchanged exact totals and neighboring matches. **All 171 final combined checks
pass in 88.369 seconds, no skips.** Complete Init code (164048 bytes), Init data
(17376 bytes), Debugger code and Game data (189088 bytes / 720 owners) remain
retail-exact. The block and variadic loaders remain directly exact, and the
relocator keeps its existing guarded match. `make tools-check` and
`git diff --check` pass. The existing duplicate generated-slice recipe warning
is unchanged.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_cache_installer_candidates
python3 -m unittest tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Counts And Next

Exact totals remain 3290 / 5463 (60.22%) overall and 2617 / 4790 (54.63%) Game,
with zero address drift and 2173 still-different functions. Converted counts,
all 492 exact Init C functions, all 181 exact Debugger C functions, and the
47 retained Init assembly functions are unchanged. README aggregates were
already correct and need no counter edit for this partial matching progress.

Read-only sibling audit finds translated retail `func_1502AB04` in
`64CBFDOGL/recomp_out/.c:202014`, its 0x28 frame at line 202023, s2 count at
line 202035, and sequential offset-store/descriptor-load sequence around
lines 202107..202115. No sibling source, build, save or frozen Release changes
are made. This is not PC runtime or rendering acceptance.

Next: pursue the alias-preserving one-word-copy shape or an equivalent scalar
source that emits the same induction/unroll. If considering guards, first
classify all 41 differences, prove the closed allocation and independent-store
schedule, and retain full alias/read-value traces and omitted-guard controls.
Do not re-adopt the raw-exact two-word aggregate by dropping partial overlap.
Counts outside 0..16, invalid pointers and unsupported buffer extents remain
unqualified. The connected cached lookup `func_1502AC88` is still 158 / 159
body/slot words, 156 differences, frame 0xA0, and can be pursued independently.
