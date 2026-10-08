# Game Table-Range Loader Direct Recovery And Caller Qualification

Date: 2026-10-05. Starting HEAD: `14c48459`.

Follow-up: [Note 998](998-game-variadic-table-range-wrapper-recovery-and-guarded-loop-stores-20261005.md)
recovers this loader's variadic caller with two checked loop-store guards and
actual-source connected fixtures. The unrecovered-caller statements and counts
below describe this note's historical checkpoint.

## Result And Scope

`func_1502AF04` is recovered from its false zero-return C placeholder as the
resource table-range DMA loader and in-place offset adjuster. All 71 words /
284 bytes emit **directly from default IDO O2/g3**, including retail's 0x40
frame. No new word guards, padding, insertion/omission or compiler-profile
override is needed. The real four-argument pointer-returning interface replaces
the empty-argument integer placeholder declaration in the same source file.
The two known retail callers already consume v0 as a pointer; no unrelated
source interface or data-layout edits are made.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502AF04..0x1502B020`;
ROM `conker/conker.us.bin+0x583B4..0x584D0`.
Raw compiler / linked production / retail SHA-256:
`aefe486d405c79f8b2c99f848b7f96fddfb3de3b7f41985a940671bd70aa7ce5`.

## Recovered Contract

- Multiply the 32-bit component by eight with unsigned wrap, then add the
  original base. Preserve all high source-address bits: DMA uses address
  masked with `~0xF`, not the cached lookup's `0x7FFFFFF0` mask.
- Align caller storage using `(buffer + 8) & ~0xF`. This is **not** ordinary
  +15 roundup: it can select storage before the supplied pointer. Caller
  ownership must include the selected aligned interval; tests use a larger
  allocation and verify surrounding bytes.
- DMA length is `((address & 0xE) + count * 8 + 15) & ~0xF`, with mode one.
  Count zero still makes the DMA call, with length zero or sixteen for the
  qualified address lows. The SDK return value is ignored, as in retail.
- Return `aligned + (address & 0xF)` as the first pair pointer. Rebase the
  offset word of each eight-byte pair by the original base, with unsigned
  wrap. Descriptor words and all other bytes remain untouched after DMA.
  There is no sentinel/zero-offset exception or descriptor mask in this loop.

Two retail callers are identified in the ignored disassembly tree:
`func_1502B110.s:62` (variadic table-range wrapper) and
`game_83300/func_1505E0C4.s:218` (actor/resource constructor, stack buffer).
The latter supplies two pairs. Neither caller's C placeholder is changed in
this checkpoint. Caller qualification below uses the real retail wrapper
instructions, not a claimed recovery of that wrapper's source.

## Compiler Evidence And Rejected Exact Form

The [77-form source screen](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_table_range_candidates.py)
uses only the existing default profile and fixed retail call relocation.
Ignored artifacts are under `conker/build/game-table-range/`. All forms compile
without isolated diagnostics; source-shape controls are retained in tests.

| Form | Body Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Previous false zero-return placeholder | 3 / 71 slot | 0 | 71 |
| Initial semantic word-indexed loop | 75 / 71 slot | 0x40 | 46, including overflow |
| Eight-byte pair struct indexing | 71 | 0x40 | 5 |
| Integer-address pair-pointer sums | 71 | 0x40 | 2 |
| Separate captured DMA length | 71 | 0x48 | 9 |
| Selected safe argument-address assignment | 71 | 0x40 | 0 |

Pair-struct indexing restores the original peeled and four-record unrolled
loop without the word-index conversion moves. Integer-address sums recover
retail's operand ordering directly. Capturing the address in the DMA source
argument recovers its sp+0x28 spill and reload instead of sp+0x2C. Recomputing
`base + component` in the independent length argument lets IDO share the
arithmetic while keeping the C expression correctly sequenced.

One screen form also emits exact words but is **rejected**: it assigns
`address` in the first DMA argument while reading `address` in the length
argument. Those call arguments are unsequenced in C, so a matching binary
does not qualify that source. The screen flags this form explicitly; the
test pins the selection's absence of any other address reference in that call.
The two safe exact forms independently recompute the length address, differing
only by a redundant earlier assignment. Production selects the one without
that redundant assignment and includes a short sequencing comment. This
rejection remains a source-language gate, not a machine-word mismatch claim.

## Qualification

[The new seven-check module](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_table_range_loader.py)
pins the raw full slot/hash, source-shape controls, safe call-argument shape,
native semantics, full instruction corpus, connected retail caller, production
source and guard-free linked identity. The unlinked object has exactly one
relocation: offset 0x64, `R_MIPS_26:func_10004514`.

- 6336 native actual-source cases: three data patterns, counts 0..32, all
  sixteen buffer pointer lows and address lows 0/4/8/12. Independent byte
  expectations verify DMA arguments, returned pointer, rebased offsets,
  untouched descriptors, and every allocation/fence byte.
- Seven native base/component vectors per data pattern cover 32-bit address
  wrap, negative component bit patterns, signed extremes and preservation of
  high DMA source bits. Offset words include overflow-prone values. The DMA
  fixture returns -1 after filling, proving the source ignores that return.
- 12672 two-way retail/fresh-C instruction cases repeat the count/buffer/
  address/data matrix with both valid N64 stack phases. Independent expected
  public memory/calls/returns agree. Complete mapped memory including private
  stack and ordered read/write/call events agree between retail and C; all
  71 words are visited. Caller-saved integer registers are clobbered by DMA;
  saved-register and stack restoration are checked at final return.
- 60 connected retail `func_1502B110` wrapper cases: explicit/default base,
  depths 1/2/3, counts 0/1/2/5/16 and both stack phases. They execute the real
  wrapper and the freshly compiled range loader, checked cached lookup and
  checked cache installer together. Nested lookup offsets produce the expected
  resolved base and final range output; all 71 range-loader words are visited.
  The wrapper itself remains unrecovered C, and skipped/invalid descriptor
  paths are not claimed as new caller acceptance.

The bounded big-endian low-word runner models only SDK DMA and byte copy;
it is not emulator/hardware or real ROM DMA qualification. Native fixtures
use 32-bit GCC with warnings treated as errors and the existing
`-fno-strict-aliasing` byte-buffer convention; this is not a claim of portable
strict-aliasing acceptance. Invalid/unaligned pair
accesses, insufficient caller storage, actual ROM validity, arbitrary stack
alignment and unsupported count/extent domains remain unqualified.

## Measured Progress

The production rebuild succeeds and freshly reports:

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3293 / 5463 (60.28%) | 0 | 2170 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2620 / 4790 (54.70%) | 0 | 2170 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

This is a semantic placeholder recovery and new direct byte match. Conversion
counts do not change because the old placeholder was already counted as C.
The 47 retained Init ASM functions and existing 10591 patch-table rows are
unchanged. README edits contain aggregate totals only; detailed recovery stays
in dedicated documentation. Existing duplicate generated-slice recipe
warnings remain; the new isolated compiler and production source have no
new diagnostics. `make tools-check` passes.

**All 190 final combined checks pass in 135.010 seconds, no skips.** Complete
Init code (164048 bytes), Init data (17376 bytes), Debugger code and Game data
(189088 bytes / 720 owners) remain retail-exact. Neighboring cached lookup,
cache installer, block loader, variadic loader and relocator match checkpoints
hold. The command adds this module's seven checks to Note 996's complete suite.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m tools.experiments.game_table_range_candidates
python3 -m unittest tools.tests.test_game_table_range_loader tools.tests.test_game_cached_lookup_match tools.tests.test_game_cache_installer_match tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
make tools-check
git diff --check
```

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502AF04` at
`64CBFDOGL/recomp_out/.c:202652`, including the original +8 alignment, full
source-address mask, sp+0x28 saved address, pair fixup loop and pointer return.
No maintained `src/pc` reference/override is found for this function. No host
synchronization is needed for this guest recovery. No sibling source, build,
save or frozen Release artifact is modified. Real SDK DMA/copy, PC runtime
and rendering acceptance remain separate and open.

Next connected source recovery: `func_1502B110`, still a zero-return
placeholder, 69 retail words with frame 0x48. Recover its default-root choice,
SDK varargs traversal, intermediate cached lookups, descriptor-length gate
and final call to this range loader. Keep zero/one-depth behavior and undefined
caller inputs faithful; do not synthesize a safer path that changes retail.
