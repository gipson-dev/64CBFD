# Game Attachment Walker Guarded Register Match

Date: 2026-10-05. Starting HEAD: `9d9abff9`.

## Result And Boundary

The complete linked `func_15168E54` slot now matches all 45 words / 180 bytes
at retail address `0x15168E54`, with its original 0x38 frame. **This is a
guarded match, not a direct compiler match.** Unguarded semantic C remains
45 words with nine raw differences. Nine expected-word guards close the
cursor/opcode register allocation and commute equality operands only.
No insertion, omission, relocation, algorithm replacement, public interface,
profile or data change is introduced. Final production C is unchanged.

Retail uses `v1` for the current command and `v0` for its signed opcode;
IDO instead uses `a2` and `v1`. All addresses, memory offsets, branch kinds,
branch displacements, call target, delay-slot updates and saved-register
lifetimes already agree. The three differing comparisons merely reverse
equal/not-equal operands while applying the same allocation.

| Offset | Expected C Word | Retail Replacement |
| --- | --- | --- |
| 0x38 | `02203025` | `02201825` |
| 0x44 | `82230000` | `82220000` |
| 0x50 | `10740006` | `12820006` |
| 0x54 | `24C40004` | `24640004` |
| 0x58 | `54750007` | `56A20007` |
| 0x60 | `90CF0003` | `906F0003` |
| 0x7C | `03113021` | `03111821` |
| 0x80 | `80C30000` | `80620000` |
| 0x84 | `1473FFF2` | `1662FFF2` |

All rows explicitly require no relocations (`-`/`-`), no insertion and no
omission. The table contains 10521 rows with zero duplicate owner/function/
offset keys. Guard offsets are all inside this routine, and both the
independent fixture and production padder verify compiled input words.

Raw C slot SHA-256:
`958dcb84bbf375ebdd6c9170744538d8a59afb5385c31977ab50158843aca792`.
Guarded production and pristine ROM `conker/conker.us.bin+0x196304` SHA-256:
`157c0f41f4c9b1ec4468044fd64cf52dbd88b33f189424160d1b97959f78e210`.

## Source Investigation

[game_attachment_cursor_candidates.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_attachment_cursor_candidates.py)
reproduces 36 named source forms under default IDO 5.3 O2/g3 in ignored
`conker/build/game-attachment-cursor/`. No form matches directly. Trials cover
opcode width, pointer/signed/unsigned address cursors, declaration order,
initializer/scope, operand order, register qualifiers, cursor expressions,
line layout and neutral expressions. Alternate signed/unsigned leaf result
declarations also retain nine differences, so no return interface is changed.

Most forms preserve the 45-word/0x38 body and nine differences. Declaration
initialization differs at ten positions. Two cursor arithmetic forms emit
41 words/0x30 and differ at all 45 slot positions. They are screen results,
not adopted semantic alternatives. The widened opcode trial was reverted:
the original signed-byte local remains in production.

## Qualification

[test_game_attachment_cursor_match.py](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_attachment_cursor_match.py)
adds five checks: reproduce the screen; pin raw input and all nine guard
rows; compare whole instruction traces; reject partial allocations; retain
four neighboring byte hashes and addresses. The trace runner extends the
existing bounded low-word oracle locally with signed byte loads. It is not
a full hardware emulator or FCSR model.

- 1427 three-way cases run retail, independently compiled unguarded C and
  guarded C, including every opcode byte, subtype boundaries, seven word
  patterns and seven base words. All memory, calls, ordered reads and stores
  agree. They execute the actual retail-exact eight-word address-adjuster leaf.
- The corpus visits every one of the 45 walker and eight leaf words in all
  three forms, including taken/annulled branch-likely delay paths.
- Twenty additional three-way cases use an explicitly opaque leaf with
  caller-register clobbering and next-command mutations, or change the first
  opcode between its two volatile reads. Their ordered traces agree.
- Omitting any one guard from the closed allocation is rejected by bounded
  trace/output comparison or mapped-memory/instruction-budget checks. These
  intentionally broken inputs are negative controls, not valid retail cases.
- A new actual-body native fixture qualifies all 256 opcode bytes, 256 subtype
  bytes and seven word patterns: **458752 cases**, using the actual adjuster.
  Commands after the terminator remain untouched.

The existing independent texture fixture retains nine raw compiler differences
and the raw digest, then checks each guard input before demanding complete
guarded/production/retail equality. Setup and resolver remain unguarded and
non-matching. Existing actual constructor/helper/loader/setup/resolver/attachment
connections rerun; no mock is silently credited as a real allocator or decoder.

**All 154 final combined checks pass in 67.116 seconds, no skips.** The shared
patch-table change triggers a full consumer rebuild, which completes before
the final suite. Complete Init code/data, Debugger code and Game data stay
raw retail-exact. The recent nullable cleanup, immediate release and resource
helper direct matches remain exact. Existing source warnings and duplicate
`generated_12D630` recipe warnings remain; isolated screen compiler diagnostics
are recorded separately. `make tools-check` and `git diff --check` pass.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

This does not qualify malformed unterminated streams, real guest allocation/
DMA/decode, natural PC gameplay or final pixels. Synthetic callback mutations
are explicitly separate from the actual connected leaf corpus.

## Progress And Next

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3287 / 5463 (60.17%) | 0 | 2176 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2614 / 4790 (54.57%) | 0 | 2176 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is one additional guarded byte match, not a new C conversion. Conversion
counts and the 47 Init ASM entries are unchanged. README remains aggregate-only.

Read-only sibling audit finds the full retail attachment sequence in
`64CBFDOGL/recomp_out/.c:1081473`, including the same `v1`/`v0` cursor/opcode
allocation. No named maintained override is found in scoped `src`/CMake input
search. No synchronization is needed for this function, and no host source,
build, save or frozen Release changes are made. This is not runtime parity
qualification for the sibling's downstream resource/rendering pipeline.

Next matching target: the complete 77-word variadic resource loader
`func_1502B6BC` from [Note 962](962-game-variadic-resource-loader-and-offset-relocation-recovery-20261004.md).
It has seventeen raw differences but fits the slot and retail 0x50 frame.
Preserve the actual `stdarg.h` interface and connected loader tests while
investigating its register/stack schedule. `func_150E6FAC` remains a separate
fifteen-word return-tail gate; do not repeat Note 921's failed return/goto/profile
matrix. The light-selector connected stack-seed gate remains open.
