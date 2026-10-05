# Game Variadic Resource Loader Direct Stack Match

Date: 2026-10-05. Starting HEAD: `59f26b8e`.

## Result And Scope

`func_1502B6BC` now matches its complete 77-word / 308-byte retail slot
directly from semantic C, including the original 0x50 frame. No expected-word
guards, compiler overrides, inserted/omitted instructions, interface changes
or data edits are needed. The production change is confined to this function
in `conker/src/game_57FA0.c`.

Entry/end: `0x1502B6BC..0x1502B7F0`. Retail ROM:
`conker/conker.us.bin+0x58B6C..0x58CA0`.
Independent freshly compiled C, linked production and pristine ROM all have
SHA-256 `40ead79430624c623749d0a0b9319470f3c925d306da179f6eb908c4828b3fe1`.

The earlier [Note 962](962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md)
recovery fit the same body/frame but differed at seventeen words. A distinct
local output pointer, defaulted to `&fallbackSize` and replaced only when
the caller's size pointer is nonnull, recovers the complete saved-register
prologue and nullable-output branch/delay schedule. It leaves three differences:
the compiler places the descriptor at `sp+0x40` instead of retail's `sp+0x38`.
Moving its declaration after the component and offset locals resolves those
three words without extra variables or operations. The fallback stays at
`sp+0x44`, and all remaining words match unchanged.

| Source Form | Body Words | Frame | Raw Slot Differences |
| --- | ---: | ---: | ---: |
| Previous production | 77 | 0x50 | 17 |
| Separate output pointer, explicit if/else | 78 | 0x50 | 67 |
| Separate output pointer, fallback default | 77 | 0x50 | 3 |
| Fallback default, descriptor/component declaration swap | 77 | 0x50 | 0 |

The three formerly differing descriptor words are now direct compiler output:
`0x5C: 27B40038`, `0x8C: 8FA80038`, `0xB0: 8FA50038`.
The nullable fallback address at `0x30` is `27B20044`.

## Preserved Contract

Keep the actual four-fixed-argument plus variadic interface and local
`stdarg.h` macros. Every positive-depth path component is consumed, even
after size/status becomes zero and suppresses later lookups. The offset delta
still wraps as an unsigned address word; the descriptor mask is unchanged.
The block loader's pointer result and post-call size/status remain independent
gates. Size and relocation outputs may be null or alias; the final count wins
when aliased. A missing path leaves the relocation output untouched.

The descriptor remains intentionally uninitialized for zero depth or an
unwritten lookup result. No initializer, depth clamp, fixed-arity substitute,
stack-address cast or invented scratch padding was added. Exact instructions
do not extend the C qualification domain to those undefined inputs, negative
depth, absent variadic arguments or arbitrary invalid pointers.

## Source Screen And Regression

[game_variadic_loader_stack_candidates.py](../../tools/experiments/game_variadic_loader_stack_candidates.py)
retains the pre-match source as an explicit fixture and reproduces 83 named
forms with default IDO 5.3 O2/g3. It screens nullable selection, separate output
pointers, declaration permutations, loop-local component scope and offset/result
reuse. Only the adopted descriptor/component swap matches directly. Each form
records complete differences, body length, frame and compiler diagnostics in
ignored `conker/build/game-variadic-loader-stack/screen.json`.

All isolated screen compilations emit no diagnostics. Reusing the offset as
the result either changes the frame or retains additional differences; it is
not adopted. Plain permutations of the path/fallback/descriptor group do not
match. The experiment asserts that production is exactly the winning source
form, so future screens cannot silently redefine the earlier baseline.

[test_game_variadic_resource_loader.py](../../tools/tests/test_game_variadic_resource_loader.py)
now has fifteen checks. A new source-screen identity check retains the baseline
and real variadic macros. Its independent IDO fixture demands full raw C =
production = ROM identity, pins all four stack-address words, and still checks
the unchanged relocator and three exact callers. Existing native fixtures
retain depth 1..16, signed components, wrapping offsets, all-component
consumption, nullable/aliased outputs, callback mutations, actual offset
relocation and connected constructor/helper/loader callers. All fifteen pass.

The production rebuild passes. **All 155 final combined checks pass in
66.630 seconds, no skips.** They retain the previous attachment guarded match,
resource helper/immediate release direct matches, connected resource/texture
fixtures and complete Init code (164048 bytes), Init data (17376 bytes),
Debugger code and Game data (189088 bytes / 720 owners) retail identity.
`make tools-check` and `git diff --check` pass. No patch-table or header change
requires another all-consumer rebuild. Existing duplicate `generated_12D630`
recipe warnings remain; the changed production source compiles without
diagnostics under its existing profile.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_variadic_loader_stack_candidates
python3 -m unittest tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Progress And Next

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3288 / 5463 (60.19%) | 0 | 2175 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2615 / 4790 (54.59%) | 0 | 2175 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is one new direct match, not a new C conversion. Conversion counts,
47 remaining Init ASM entries and the shared 10521-row word-patch table are
unchanged. README contains only updated aggregate measurements.

The read-only sibling audit finds retail's original frame, nullable-output
prologue and all three `sp+0x38` descriptor accesses in
`64CBFDOGL/recomp_out/.c:204551`. The translated loader also contains existing
host diagnostics; no definition override is found in maintained `src` inputs.
No sibling source, build, save or frozen Release changes are made. This is
not a PC allocator/DMA/decode, natural gameplay or pixel qualification.

Next local matching target: `func_1502B4A8`, the same pipeline's 72-word offset
relocator. Its semantic body remains 65 words plus seven slot padding words,
with 71 raw differences. Investigate the auto-count scan and indexed relocation
loop shape against retail's odd-entry peel and two-record unroll. Preserve
unsigned address wrapping, sentinel/length handling, terminal inclusion and
negative-count no-dereference behavior; keep the now-exact variadic loader and
connected fixtures pinned. The unrelated light-selector stack-seed and
`func_150E6FAC` return-tail gates remain open.
