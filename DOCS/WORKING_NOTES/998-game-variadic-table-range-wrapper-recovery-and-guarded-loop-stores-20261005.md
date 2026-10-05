# Game Variadic Table-Range Wrapper Recovery And Guarded Loop Stores

Date: 2026-10-05. Starting HEAD: `b4db5527`.

## Recovery And Scope

`func_1502B110`'s false zero-return placeholder is replaced with the recovered
SDK-varargs table-range wrapper. Default IDO O2/g3 emits its full 69-word /
276-byte body and original 0x48 frame, with two raw scheduling differences.
Two expected-word guards make the complete linked slot byte-exact. **This is
a guarded match, not a direct compiler match.** No profile override, padding,
instruction insertion/omission or data-layout change is introduced. The
four-named-argument variadic pointer-returning declaration replaces the
empty-argument integer placeholder in the same file.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502B110..0x1502B224`;
ROM `conker/conker.us.bin+0x585C0..0x586D4`.
Raw full-slot SHA-256:
`b249fec226d56f27cdf2471a0a1b283cacde2654b3befa32a1bf03364511f08d`.
Guarded/retail full-slot SHA-256:
`d2a96c6abbb8424685a7350199fa6fb7e1c2d6ef9c4b3c3fd7004f41ec548a4f`.

## Recovered Contract

The wrapper initializes descriptor to one and result to NULL. A zero base
selects `D_AB1950`; a supplied base is retained. For each component before
the last, it consumes the SDK vararg even after the descriptor gate closes.
If descriptor is nonzero, it calls the actual cached lookup, adds its returned
offset to the base with 32-bit wrap, then masks the descriptor to 28 bits.
Depth decreases in place, preserving its original argument home slot.

One final component is consumed unconditionally. If the descriptor remains
nonzero, the wrapper calls `func_1502AF04` with resolved base, original caller
buffer, final component and original count, then returns that pointer. A NULL
range result remains NULL without a fallback. A descriptor with only high flag
bits closes the gate after masking; subsequent varargs still advance but
neither lookup nor range loading occurs.

Depth zero and one both consume one final component and can call the range
loader. Tests supply that component explicitly; insufficient varargs are
undefined caller input, not a reason to synthesize a new zero-depth guard.
An unwritten lookup descriptor retains the initialized or previous masked
value, unlike the other resource loader's uninitialized descriptor local.
Counts are delegated unchanged; large boundary-test counts do not qualify
the range loader's corresponding memory extents or actual DMA requests.

The known actor/resource-constructor caller is
`game_83300/func_1505E0C4.s:230`. Its instructions remain outside this source
recovery; no new constructor/runtime acceptance is claimed.

## Compiler Screen And Guards

The [67-form screen](../../tools/experiments/game_variadic_table_range_candidates.py)
uses the real `conker/include/libc/stdarg.h`, default IDO O2/g3 and fixed retail
relocations. All forms compile without isolated diagnostics; none is directly
exact. Ignored reports live under `conker/build/game-variadic-table-range/`.

The original placeholder has three body words, 69 slot differences and no
frame. Initial semantic C fits 69 words / frame 0x48 with ten differences.
Declaration order `path, component, descriptor, result` recovers the exact
sp+0x3C descriptor and sp+0x38 result placement. This leaves only two stores
different. Unsigned-component, alternate declaration order, predecrement,
comma-update, explicit descriptor assignment and do/while trials reproduce
the same two-word scheduling residual. These are compiler controls, not a
claim that every alternate variadic type has been semantically qualified.

| Offset | Raw Expected | Retail Replacement | Effect |
| --- | --- | --- | --- |
| 0xAC | AFA8003C | AFA70054 | Store updated depth before loop branch instead of descriptor |
| 0xB4 | AFA70054 | AFA8003C | Store masked descriptor in branch delay instead of depth |

The branch at offset 0xB0, all call/branch conditions and all other 67 words
are unchanged. Both forms complete the same two stores before any subsequent
read or call, on both taken and fallthrough paths. The four-byte destinations
are disjoint: entry SP+0x0C (depth argument home) and entry SP-0x0C
(descriptor local). There is no movement across a live read or callback.
Raw ordered stores differ, so qualification checks commuting stores between
identical reads rather than falsely asserting raw ordered-event identity.

Neither guarded offset carries a relocation. The unlinked object has exactly
four relocations, all retained: D_AB1950 HI16 at 0x40 / LO16 at 0x44, cached
lookup call at 0x8C and range-loader call at 0xE0. The
[patch table](../../conker/retail_word_patches.us.csv) contains 10593 rows
with zero duplicate numeric owner/function/offset keys.

## Qualification

[The new nine-check module](../../tools/tests/test_game_variadic_table_range_match.py)
pins complete raw/guarded slots and hashes, compiler/source controls, SDK
relocations, every omitted-guard rejection, production source/table identity,
and boundary/native/actual-callee behavior.

- 1386 native boundary cases cover three roots, three signed-component/data
  patterns, depths 0..16, each intermediate missing-descriptor position,
  unwritten descriptor callbacks, original count delegation and NULL results.
  Instrumented builtin va_arg checks complete argument consumption; the
  fixture uses the actual SDK header's host branch.
- Explicit native controls cover an unwritten descriptor through wrapping
  base additions and a missing descriptor with a NULL buffer that must never
  reach range loading. No missing-buffer safety claim is made for open gates.
- 8316 three-way retail/raw/guarded boundary cases cover the same descriptor
  gates and argument patterns, three roots, depths 0..16, counts 0/5/FFFFFFFF
  and both valid N64 stack phases. All 69 words are visited in each form.
- Complete mapped memory including private stack, ordered reads and call
  arguments, final return and saved-register restoration agree. Every changed
  write window is restricted to exactly the two disjoint four-byte stores
  above, with equal values and an identical following read/call event. Other
  windows retain their original order, including repeated prologue writes.
  Guarded ordered events agree exactly with retail.
- Removing either guard is rejected by a bounded-access/control failure or
  full memory/event comparison. The witnesses include a zero-length
  descriptor that must stop subsequent lookups.
- 200 three-way connected cases execute the actual wrapper, newly recovered
  range loader, checked cached lookup and checked cache installer together.
  They cover explicit/default roots, depths 0/1/2/3/5, counts 0/1/2/5/16,
  both stack phases and external/caller-owned stack buffers. All wrapper and
  range-loader words are visited; depth-zero cases provide one component.
- 544 native connected cases use the actual C cache installer, lookup, range
  loader and new wrapper, with only SDK DMA and byte-copy fixtures. Default/
  explicit roots, depths 0..5, counts 0..16 and every missing-descriptor gate
  preserve resolved bases, complete call counts, rebased offset words and
  unchanged descriptors. This is no longer merely a retail-only caller test.

The low-word big-endian runner and bounded DMA/copy fixtures are not hardware,
real ROM DMA or rendering qualification. Native GCC is 32-bit with warnings
treated as errors and the existing `-fno-strict-aliasing` byte-buffer convention.
Insufficient varargs, unsupported count/extent combinations, unaligned/invalid
pointers, buffers outside caller-owned storage and arbitrary stack alignment
remain unqualified. Earlier alias and resource-helper gates remain intact.

## Measured Progress

The full shared patch-table consumer rebuild succeeds and freshly reports:

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3294 / 5463 (60.30%) | 0 | 2169 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2621 / 4790 (54.72%) | 0 | 2169 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion totals remain unchanged because the old placeholder was already
counted as C. The 47 retained Init ASM functions are untouched. README edits
contain aggregate totals only; recovery narration stays in dedicated docs.
Existing duplicate generated-slice recipe/unrelated source warnings remain;
isolated candidate diagnostics are empty. `make tools-check` passes.

The final combined suite passes **199 tests in 148.664 seconds, no skips**,
against the freshly rebuilt ELF. Protected Init code (164048 bytes), Init
data (17376 bytes), Debugger code and Game data (189088 bytes / 720 owners)
remain byte-exact. Existing connected resource and alias gates also pass.

## Reproduction

Run from the `64CBFD` root in PowerShell; the compiler driver uses relative
source/output paths to avoid IDO's space-containing-path limitation.

```powershell
wsl python3 -m tools.experiments.game_variadic_table_range_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_variadic_table_range_match tools.tests.test_game_table_range_loader tools.tests.test_game_cached_lookup_match tools.tests.test_game_cache_installer_match tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
wsl make tools-check
git diff --check
```

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502B110` at
`64CBFDOGL/recomp_out/.c:202995`, already containing the 0x48 frame, original
loop stores and unconditional final component load. No maintained `src/pc`
reference/override is found. No host synchronization is needed for this
matching change. No sibling source, build, save or frozen Release artifact
is modified. Real SDK DMA/copy, PC runtime and rendering acceptance remain
separate and open.

Next connected source recovery: `func_1502B020`, still a zero-return
placeholder, 60 retail words with frame 0x48. It traverses from D_AB1950 using
SDK varargs, optionally writes the masked final size and returns the resolved
table address only while the descriptor gate remains open. Preserve its
zero-depth initialized-one behavior, continued argument consumption after a
missing component, and output-store-before-final-descriptor-read alias gate.
