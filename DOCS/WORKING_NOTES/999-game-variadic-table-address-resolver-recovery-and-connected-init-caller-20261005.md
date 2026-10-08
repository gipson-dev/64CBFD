# Game Variadic Table-Address Resolver And Connected Init Caller

Date: 2026-10-05. Starting HEAD: `339d56c0`.

Follow-up: [Note 1000](1000-game-caller-buffer-resource-loader-direct-recovery-and-syscall-boundary-20261005.md)
recovers the caller-buffer resource loader directly and distinguishes the real
syscall boundary from returning error-hook continuation tests. The next-target
statement below describes this historical checkpoint.

## Result And Scope

`func_1502B020`'s false zero-return placeholder is replaced with its recovered
SDK-varargs table-address resolver. Default IDO O2/g3 emits the complete
60-word / 240-byte body and original 0x48 frame. Two expected-word guards
normalize only independent loop stores. **This is a guarded match, not a
direct compiler match.** No profile override, insertion/omission, padding or
data-layout change is introduced.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502B020..0x1502B110`;
ROM `conker/conker.us.bin+0x584D0..0x585C0`.
Raw complete-slot SHA-256:
`541e2e7d512cda3d590e0773c06ab103954e1a87fbe38ab1e63a2ac1f835c8c3`.
Guarded/retail complete-slot SHA-256:
`b13bf05cd069a03869466184bab0f54b0fb2557bb744f1d334034496776b7844`.

The resolver and both maintained Init callers now declare the same
`u32 func_1502B020(u32 *size, u32 depth, ...)` interface. `init_8180.c`'s
old four-integer fixed-argument declaration is replaced; `init_12560.c`
receives the prototype and an unsigned size local. No sound/submission
behavior is changed. Full-slot checks cover both caller routines after
recompilation: `func_10008180` (214 words) and `func_1001263C` (43 words).

## Recovered Contract

Descriptor starts at one, base at D_AB1950. The SDK va_list begins immediately
after the depth argument. Every requested component is consumed, including
those after the descriptor becomes zero. Lookup runs only while descriptor
is nonzero; its returned offset is added to base with 32-bit wrap. Each loop
decrements depth and masks descriptor to 28 bits.

After traversal, a non-NULL size pointer receives the masked descriptor.
Only after that store does the emitted code reread descriptor for the return
gate. A zero descriptor returns zero; otherwise the resolved base is returned.
The final output must not be moved before traversal, and cache/clock outputs
must not cause a new lookup or late base recomputation. Tests preserve ordered
reads and all writes except the explicitly independent loop-store pair.

Depth zero consumes no varargs, makes no lookup, reports size one if requested
and returns D_AB1950. An explicit `func_1502B020(NULL, 0)` native control
supplies no trailing arguments. This differs from the range wrapper in
[Note 998](998-game-variadic-table-range-wrapper-recovery-and-guarded-loop-stores-20261005.md),
whose zero-depth path still consumes a final component.

An unwritten lookup descriptor retains the initialized/previous masked value.
High-only descriptor flags close the gate after masking, but all remaining
components are still consumed. Invalid pointers, insufficient varargs and
unbounded argument storage are not qualified or made safe by this recovery.

## Compiler Screen And Guards

The [108-form source screen](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_variadic_table_address_candidates.py)
uses the real SDK stdarg header and fixed retail relocations. All forms
compile without isolated diagnostics; best residual is two words, none is a
direct match. Ignored reports live in `conker/build/game-variadic-table-address/`.

The placeholder has three body words / no frame / 60 slot differences.
Initial semantic C with ternary return emits 61 words / frame 0x48 / 17
differences. Declaration order `path, component, base, descriptor` fixes
descriptor placement at sp+0x38, leaving 11 differences but still 61 words.
An explicit zero-descriptor early return recovers retail's 60-word return
shape and leaves only the two loop stores. Alternative declaration orders,
store order, predecrement, comma-update, explicit-mask, unsigned-component
and do/while controls reproduce the scheduling residual. These are compiler
controls, not semantic qualification of every alternate variadic type.

| Offset | Raw Expected | Retail Replacement | Effect |
| --- | --- | --- | --- |
| 0x94 | AFA80038 | AFA5004C | Store updated depth before branch instead of descriptor |
| 0x9C | AFA5004C | AFA80038 | Store masked descriptor in branch delay instead of depth |

Both stores complete before the next read/call, on both loop paths. Their
four-byte destinations are disjoint: entry SP+4 (depth home) and entry SP-16
(descriptor local). The branch at 0x98 and every other word are unchanged.
Qualification permits commutation only in a window containing exactly these
two destinations with equal values and an identical following event. All
other windows retain order, including repeated prologue writes and the final
optional output-store/descriptor-read pair. Guarded ordered events match retail.

There are exactly three unlinked object relocations: D_AB1950 HI16 at 0x30,
LO16 at 0x38, and cached-lookup R_MIPS_26 at 0x78. No guarded offset carries
a relocation; all three inputs remain intact. The
[patch table](../../conker/retail_word_patches.us.csv) has 10595 rows and zero
duplicate numeric owner/function/offset keys. Omitting either guard is rejected.

## Qualification

The [eleven-check module](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_variadic_table_address_match.py)
pins full raw/guarded hashes, complete linked identity, original frame,
compiler controls, SDK relocations, caller declarations and complete caller
slots, omitted-guard rejection and connected behavior.

- 2040 native boundary cases cover signed components, wrapping offset
  additions, depths 0..16, each missing-descriptor position, unwritten
  descriptors and optional size outputs. SDK host va_arg instrumentation
  verifies complete consumption; surrounding output words remain untouched.
- 4080 retail/raw/guarded boundary cases cover the same descriptor gates,
  component patterns and depths, both valid N64 stack phases, NULL/external/
  caller-stack outputs and output into the first consumed argument home.
  All 60 resolver words are visited in every form. Complete mapped memory,
  ordered reads, calls, return and saved-register restoration agree, with
  only the two independent raw stores permitted to commute.
- 84 three-way positive connected cases execute freshly compiled checked
  lookup/cache code, including depth 16 and outputs into cache address/offset
  state, the cache clock and caller-owned storage. SDK DMA/copy remain bounded
  hooks, not actual ROM transfers.
- 400 three-way connected hit/miss cases cover each missing-descriptor
  position, an initial cache hit or miss, cache-descriptor/clock outputs and
  both stack phases. Exact lookup and DMA counts remain pinned.
- 84 native actual-C cache/lookup/resolver cases cover depths 0..5, every
  missing position and NULL/local/cache-offset/clock outputs. Repeated calls
  with NULL/local outputs verify cache-hit reuse without additional DMA/copy.
  The actual current helper bodies are extracted; only SDK DMA/copy are hooks.
- 24 three-way connected cases execute retail Init `func_1001263C` with the
  raw/guarded/retail resolver and actual checked lookup/cache. They retain
  caller-owned size storage, the sound-ID halfword, rejection of missing
  descriptors, exact sound-command order/arguments and the special 0xD2 path.
  Sound functions are opaque hooks, not sound playback qualification.

Connected Init coverage is **42 of 43 caller words**. The unvisited word at
0x10012688 is the likely delay slot of the size-zero early exit after a
nonzero resolver return. With this actual callee, size zero always returns
address zero, so the caller exits before that branch. The test pins precisely
this unvisited word; it does not fake an impossible callee result for coverage.
All 60 resolver words remain covered by the separate boundary corpus.

The native compiler uses 32-bit GCC, warnings as errors and the existing
`-fno-strict-aliasing` byte-buffer convention. Neither these fixtures nor the
bounded low-word big-endian runner qualify hardware, real DMA, portable strict
aliasing, arbitrary stack alignment, invalid/private-frame output pointers,
real sound, PC runtime or rendering.

## Measured Progress

The full shared patch-table consumer rebuild reports:

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3295 / 5463 (60.31%) | 0 | 2168 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2622 / 4790 (54.74%) | 0 | 2168 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts remain unchanged because the old placeholder was already
counted as C. The 47 retained Init ASM functions are untouched. README changes
contain aggregate totals only; function-level narration stays in dedicated docs.
Existing unrelated build warnings remain; isolated candidate diagnostics are
empty. `make tools-check` passes. The follow-up build recompiles both Init
caller files and retains the same totals above.

The final combined suite passes **210 tests in 172.769 seconds, no skips**,
against that final ELF. Both Init caller slots remain byte-exact across all
214 and 43 words. Protected Init code (164048 bytes), Init data (17376 bytes),
Debugger code and Game data (189088 bytes / 720 owners) remain byte-exact.
Existing alias, resource-helper and connected-caller gates remain intact.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_variadic_table_address_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_variadic_table_address_match tools.tests.test_game_variadic_table_range_match tools.tests.test_game_table_range_loader tools.tests.test_game_cached_lookup_match tools.tests.test_game_cache_installer_match tools.tests.test_game_cache_installer_candidates tools.tests.test_game_block_loader_direct_match tools.tests.test_game_offset_relocator_match tools.tests.test_game_attachment_cursor_match tools.tests.test_game_resource_helper_schedule tools.tests.test_game_extended_child_constructor tools.tests.test_game_variadic_resource_loader tools.tests.test_game_asset_table_lookup_and_block_load tools.tests.test_game_texture_resource_setup tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_nullable_cleanup tools.tests.test_game_texture_metadata_and_maintenance tools.tests.test_game_queued_segment_writer tools.tests.test_match_progress tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout -q -f
wsl make tools-check
git diff --check
```

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502B020` in
`64CBFDOGL/recomp_out/.c`, with the original frame, SDK argument homes, loop
stores and final output-store/descriptor-read order already present. It also
contains an existing cadence probe; this audit does not qualify probe-free
runtime or change it. No maintained `src/pc` override/reference is found.
No sibling source, build, save or frozen Release artifact is modified.

Next connected source recovery: `func_1502B224`, still a zero-return
placeholder, 75 retail words / frame 0x30. Recover its descriptor-length
rounding/cap, raw DMA versus compressed allocation/decode/free paths and
size-mismatch error behavior without assuming the decoder or allocator is
already qualified for every extent.
