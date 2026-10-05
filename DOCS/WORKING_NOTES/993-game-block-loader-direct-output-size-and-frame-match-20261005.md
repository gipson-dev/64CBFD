# Game Block Loader Direct Output-Size And Frame Match

Date: 2026-10-05. Starting HEAD: `2fe135b4`.

Follow-up: [Note 994](994-game-cache-installer-frame-recovery-and-pair-copy-alias-gate-20261005.md)
recovers the next cache installer's retail frame and rejects an overlap-sensitive
raw-exact candidate. The block loader remains directly exact.

## Result And Scope

`func_1502B350` now emits its complete 86-word / 344-byte retail slot directly
from semantic C under the existing default IDO `-O2 -g3` profile. The original
0x30 frame, saved-register lifetime, argument spills, calls, branches, delay
slots and output stores all agree. No guards, compiler override, padding,
assembly restoration, interface change or data change is needed.

Source: `conker/src/game_57FA0.c`. Entry/end: `0x1502B350..0x1502B4A8`.
Retail ROM: `conker/conker.us.bin+0x58800..0x58958`.
Direct/production/retail slot SHA-256:
`f176b2891cb5a8aa6f60461047ea78f4b4e7958fcaef18fb41b9d0c1ccdc31ae`.

## Recovery

[Note 963](963-game-asset-table-cache-lookup-and-block-load-recovery-20261004.md)
recovered the full loader contract but emitted 77 body words in its 86-word
slot, with a 0x38 frame and 78 differences. Its source kept a separate expanded
size local and combined the zero/upper-limit tests, with early common failure
initialization. The matching shape instead stores the masked header through
the output pointer and tests that value directly. It retains explicit separate
zero-size, oversize and second-allocation-failure branches.

One `amount` local supplies the initial even allocation size, the independently
16-rounded DMA size, and the eventual decoder return or failure zero. A
separate aligned-size local creates an extra stack slot even when the rest
of the control flow agrees. Removing that local changes the frame from 0x38
to retail's 0x30 and resolves the last 22 stack-address/frame differences.
The chosen source does not need any `register` declaration.

The original behavior remains:

- Initial allocation failure returns NULL without writing the output or
  performing DMA, decode or free.
- Plain modes return the first allocation and write its even-rounded size;
  DMA has separate 16-byte rounding.
- Compressed mode masks the header's high bit and writes its expanded size
  before the second allocation. Only sizes 1..999999 request that allocation.
- Zero/oversize/second-allocation failure returns NULL and writes zero after
  freeing the compressed buffer.
- Successful allocation preserves its returned pointer even when the decoder
  returns zero or a negative count. Scratch is read at the original call site.
- Compressed input is freed before the final output store; cleanup mutations
  of the output cannot replace the preserved decoder count.

## Reproducible Screen

[game_block_loader_candidates.py](../../tools/experiments/game_block_loader_candidates.py)
retains the immutable pre-match baseline and screens 37 source forms across
eight profiles: 296 trials. Exactly two trials match directly, both using
`-O2 -g3`: the single-size form with and without a result register hint.
Only the latter is adopted. Lower optimization was an initial hypothesis,
not a production change. Default-profile candidates emit no diagnostics.
The 74 `-O2 -g1`/`-O2 -g2` trials emit IDO's expected warning that debug
disables optimization; the report retains that evidence rather than treating
those profile labels as fully optimized results.

| Source / Profile | Body Words | Frame | Differing Words |
| --- | ---: | ---: | ---: |
| Original baseline / O2 g3 | 77 | 0x38 | 78 |
| Nested failures, output-size test, two sizes / O2 g3 | 86 | 0x38 | 22 |
| Adopted single-size source / O2 g3 | 86 | 0x30 | 0 |
| Adopted single-size source / O2 without g3 | 85 | 0x30 | 83 |

Ignored reports and independently linked objects live under
`conker/build/game-block-loader/`. Screening is compiler evidence, not a
semantic endorsement of every experimental form.

## Qualification

[test_game_block_loader_direct_match.py](../../tools/tests/test_game_block_loader_direct_match.py)
adds four checks: fresh default-profile full-slot identity; original and
extra-local rejection controls; register-hint equivalence; and independently
pinned production/neighbor identity with no block-loader guards.

The existing actual-source cache/lookup/block fixture keeps its native tests
for all plain flag modes and rounding boundaries, first/second allocation
failures, header limits, decoder zero/negative returns, output/header aliasing,
scratch mutation and free-before-final-store behavior. Its connected fixture
compiles actual lookup, block loader, variadic loader and relocator bodies
together, with opaque allocation/DMA/decode callbacks. These callbacks are
contract tests, not qualification of the real callee implementations.

Production rebuild succeeds. **All 165 final combined checks pass in 54.613
seconds, no skips.** The full linked relocator stays exact with its existing
seventeen checked guards; the variadic loader stays directly exact across all
77 words. The cache installer remains 87 / 97 body/slot words with 93
differences and a 0x20 / 0x28 C/retail frame. The cached lookup remains
158 / 159 words, 156 differences and a 0xA0 frame in both forms.

Complete Init code (164048 bytes), Init data (17376 bytes), Debugger code and
Game data (189088 bytes / 720 owners) remain retail-exact. This source-only
module edit does not change the shared patch table. `make tools-check` and
`git diff --check` pass. The existing duplicate `generated_12D630` recipe
warning remains unrelated.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_block_loader_candidates
python3 -m unittest tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Progress And Next

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3290 / 5463 (60.22%) | 0 | 2173 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2617 / 4790 (54.63%) | 0 | 2173 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is a new direct byte match, not a new C conversion or Init ASM reduction.
The 47 retained Init assembly functions are unchanged. README edits contain
aggregate totals only; recovery detail stays in the dedicated docs.

Read-only sibling audit finds the translated `func_1502B350` in
`64CBFDOGL/recomp_out/.c`, including the original 0x30 frame, output-size
loads, separate failure branches, decoder result preservation and
free-before-final-store sequence. Scoped maintained `src` and CMake searches
find no named loader override. Existing default-off diagnostics remain
separate. No host source, build, save or frozen Release changes are made.
This is not real allocator/DMA/decode, PC runtime or final-pixel acceptance.
NULL output pointers and invalid compressed buffers remain unqualified.

Next connected target: cache installer `func_1502AB04`, retail slot 97 words.
Begin with the 0x20 / 0x28 frame and copy/loop lifetime differences before
attempting a broad register normalization. Retain its sixteen-entry cache
alias and live-copy/read-order behavior. The cached lookup `func_1502AC88`
follows, with the real cache/block/variadic/relocator connection tests intact.
