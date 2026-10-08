# Game Offset Relocator Typed Scan And Guarded Bulk Match

Date: 2026-10-05. Starting HEAD: `a9513a7d`.

Follow-up: [Note 993](993-game-block-loader-direct-output-size-and-frame-match-20261005.md)
completes the next block-loader target directly across all 86 words. The
relocator's guarded match and this checkpoint's measurements remain unchanged.

## Result And Scope

`func_1502B4A8`'s complete 72-word / 288-byte slot matches retail using its
recovered C body and seventeen expected-word guards. **This is a guarded
match, not a direct compiler match.** Default IDO O2/g3 emits all 72 body
words with no frame and seventeen raw differences. The guards normalize
only the closed temporary-register allocation in the two-record bulk loop.
No instruction insertion/omission, profile, public interface or data change
is introduced. The now-direct variadic loader is retained unchanged.

Entry/end: `0x1502B4A8..0x1502B5C8`. Retail ROM:
`conker/conker.us.bin+0x58958..0x58A78`.
Unguarded C slot SHA-256:
`1174f22c712142aeaec1cd146c214088942d94898c0a3d1a6a0a867ea121a96d`.
Guarded/retail slot SHA-256:
`a07f71a50c44c47daf0edd894105db8a482bf2e3ff105109148e8c807164944f`.

## Source Recovery

The [Note 962](962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md)
checkpoint used a 65-word C body plus seven padding words, with 71 differences.
The current scan uses a named local two-word offset/length record view and
tests `records[count++].length` until the terminal bit appears. That preserves
terminal-entry inclusion and the complete scan before relocation writes.
It naturally emits retail's peeled first scan iteration and its boolean
`sltiu` tests. The original indexed raw-word relocation loop stays intact.
The compiler still supplies the odd-entry peel and two-record unroll.

All first forty words, including the complete scan and odd-entry peel, now
emit directly from C. Fifty-five of the full 72 words match without guards.
The remaining seventeen words form one closed allocation over non-overlapping
temporary lifetimes: initial index/end scale, first length/mask/relocation,
second length/mask/relocation, and the next-iteration prefetch. All operations,
addresses, memory offsets, comparison kinds, branches and delay updates agree.
No opaque call or shared state is involved in the normalization.

| Offset | Expected C | Retail Replacement |
| --- | --- | --- |
| 0xA0 | `000278C0` | `000270C0` |
| 0xA4 | `0005C0C0` | `000578C0` |
| 0xA8 | `03043021` | `01E43021` |
| 0xAC | `008F1821` | `008E1821` |
| 0xB8 | `8C790004` | `8C780004` |
| 0xC0 | `03274824` | `0307C824` |
| 0xC8 | `AC690004` | `AC790004` |
| 0xCC | `15200003` | `17200003` |
| 0xD0 | `00445821` | `00445021` |
| 0xDC | `AC6B0000` | `AC6A0000` |
| 0xE0 | `8C6C000C` | `8C6B000C` |
| 0xE8 | `01876824` | `01676024` |
| 0xF0 | `AC6D000C` | `AC6C000C` |
| 0xF4 | `15A00003` | `15800003` |
| 0xF8 | `00447821` | `00447021` |
| 0x104 | `AC6F0008` | `AC6E0008` |
| 0x110 | `8C790004` | `8C780004` |

Every row is owned by `game_57FA0`, requires no relocations (`-`/`-`) and
permits neither insertion nor omission. The shared table has 10538 rows and
zero duplicate owner/function/offset keys. Each guard checks actual compiled
input, both independently and through the production padder.

## Source Screen

[game_offset_relocator_candidates.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_offset_relocator_candidates.py)
retains the original source fixture and screens 186 named forms. None matches
directly; all isolated compilations have no diagnostics. It tests scan flags,
pre/post-increment and comma conditions, cursor/index/address forms, integer
types, declaration order, typed record views, and indexed/captured relocation
forms. Reports live under ignored `conker/build/game-offset-relocator/`.

Ordinary scalar boolean scans emit 66 words. Raw-word post-increment scans
emit 73 words and exceed the slot. A manually peeled address-word screen fits
72 words but retains 22 differences; it is not adopted. The named typed scan
fits naturally and leaves only the seventeen bulk temporary differences.
The full-record-view trial also has seventeen differences, but they describe
a different cursor/end allocation. It is not the selected guard source;
the raw digest and expected-word checks distinguish the two allocations.
The unsigned-index screen changes the unroll shape and is not adopted.
Screened shapes are compiler evidence, not blanket semantic qualifications;
in particular, hoisted pointer arithmetic is not credited for the NULL/
negative-count domain. Production keeps the signed count and local typed
scan strictly inside `count == 0`.

## Qualification

[test_game_offset_relocator_match.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_offset_relocator_match.py)
adds six independent checks. The bounded big-endian low-word oracle reuses
the existing leaf/delay-slot runner and adds only AND and unsigned immediate
comparison support. This is not a full emulator or hardware acceptance.

- 4665 three-way cases compare retail, freshly compiled unguarded C and guarded
  C: fixed counts 1..17, twenty auto-count terminal positions, seven offset
  words, six length words, three base addresses and negative-count NULL calls.
  Return values, complete memory, ordered reads/stores and saved registers agree.
- The corpus visits all 71 reachable words in each form, including annulled
  and executed branch-likely delays. The duplicated odd-peel store at
  `0x1502B538` is unreachable after the preceding unconditional branch. Static
  full-slot equality still covers that word as well.
- 448 additional mixed-record three-way cases cover counts 1..32, fixed/auto
  modes and staggered sentinel/zero/nonzero fields. Independently calculated
  masked lengths and wrapping output addresses agree for each record.
- Omitting any one guard fails mapped-memory/instruction-budget or ordered
  trace/output comparisons. Zero-length records and multiple bulk iterations
  are required witnesses; a single nonzero pair alone does not reject all
  incomplete allocations.
- Original 65-word and oversized 73-word source controls remain reproducible.
  Production source, all seventeen guard rows and complete linked identity
  are pinned independently.

The existing variadic-loader fixture still compiles the actual loader and
relocator together. It pins the raw relocator before applying checked guards,
then demands production/retail identity. Loader remains raw-exact across all
77 words with no guards. Existing native count/sentinel/mask tests and actual
constructor/helper/loader/relocator connections remain in the combined suite.

The shared patch-table edit triggers a full consumer rebuild, which succeeds
before the final regression suite. Fresh production matches all 72 relocator
words, and the 77-word loader remains directly exact. Existing source and
duplicate `generated_12D630` recipe warnings remain. **All 161 final combined
checks pass in 86.318 seconds, no skips.** Complete Init code (164048 bytes),
Init data (17376 bytes), Debugger code and Game data (189088 bytes / 720 owners)
remain retail-exact. The existing attachment guarded match, helper/release
direct matches and connected native resource fixtures are retained.
`make tools-check` and `git diff --check` pass.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_offset_relocator_candidates
python3 -m unittest tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Progress And Next

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3289 / 5463 (60.21%) | 0 | 2174 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2616 / 4790 (54.61%) | 0 | 2174 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is a new guarded byte match, not a new C conversion or Init ASM reduction.
README changes are aggregate-only; detailed recovery stays in this note and
the dedicated status/update/roadmap pages. Negative counts do not dereference
the input. Missing terminals, NULL with nonnegative count, invalid or
unbounded tables and real allocator/DMA/decode behavior remain unqualified.

Read-only sibling audit finds the translated retail relocator in
`64CBFDOGL/recomp_out/.c:204006`, including the original bulk register
allocation at line 204199. Existing default-off host diagnostics remain.
No maintained named override is found in scoped `src`/CMake inputs. No host
source, build, save or frozen Release change is made; this is not PC runtime
or final-pixel qualification.

Next local target: the connected 86-word block loader `func_1502B350`, whose
77-word semantic body still has 78 raw slot differences. Preserve raw and
compressed paths, failure cleanup, size-output writes and existing actual
resource connections. Keep both newly matched loader/relocator slots pinned.
The unrelated light-selector stack-seed and `func_150E6FAC` return-tail gates
remain open.
