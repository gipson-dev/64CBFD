# Game Optional-Size Loader And Live Output Aliases

Date: 2026-10-05. Starting HEAD: `9ea429a8`.

Follow-up: [Note 1003](1003-game-counted-pointer-loader-direct-match-and-full-caller-20261005.md)
completes the next pointer-output/returned-size wrapper and its full caller.
The results and next-target description below are this note's historical
checkpoint, not the latest resume boundary.

## Result And Scope

`func_1502B5C8`'s zero-return placeholder is replaced with semantic SDK-varargs
resource-path traversal and optional size-output loading. All **61 words /
244 bytes and the original 0x50 frame emit directly from default IDO O2/g3**.
No word guards, compiler-profile overrides, inserted/omitted instructions or
data-layout changes are introduced. The full linked slot is retail-exact.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502B5C8..0x1502B6BC`;
ROM `conker/conker.us.bin+0x58A78..0x58B6C`.
Complete raw/linked/retail SHA-256:
`3e5a7f5d2eb6e43e30fefad7ef24f5cb4f7880de2bb8040cf05e4c437e8f0568`.

The owner and all six maintained caller owners now use the same pointer-return,
two-named-argument variadic declaration. Required pointer/address and signed-
size-cell casts retain existing caller/global types and behavior rather than
refactoring their structures. Every complete caller slot remains unchanged
and retail-exact. Init, Debugger and sibling PC source are untouched.
The shared patch table is unchanged: 10595 rows, no duplicates/wrapper rows.

## Recovered Contract

The wrapper selects the supplied size pointer, or an independent private
fallback when NULL, and writes one to that target. The descriptor is a
separate local, not initialized by that output-one store. Traversal starts
at D_AB1950 and consumes all signed 32-bit components using SDK stdarg.

For each component, a live nonzero size target permits `func_1502AC88` to
write the descriptor. The returned offset is added modulo 2^32. The full
descriptor is then masked to 28 bits and written to the size target before
decrementing depth. Missing descriptors stop lookups but not remaining
argument consumption. Callback writes to the size target during lookup are
overwritten by this descriptor-derived update.

After traversal, another live size read gates `func_1502B350`. That helper
receives the resolved base, freshly read full descriptor and the same size
target. The wrapper returns the helper's pointer independently of the final
size; NULL/nonzero-size and non-NULL/zero-size results are not collapsed.
A missing path returns NULL without loading, with size zero. There is no
new relocation, caller-buffer argument, output allocation or error helper.

The real block helper's first allocation failure returns NULL without writing
size: ordinarily the masked descriptor count remains, not its even allocation
rounding. At zero depth, that untouched size is the initialized one. Second
allocation failure instead reaches the helper's final size-zero store. Opaque
callback writes can still affect an aliased output: for example, the explicit
allocation hook's scratch mutation remains when size aliases scratch and
the first allocation fails. Tests preserve this effect, not an invented
guarantee that all failed loads leave output memory unchanged.

## Physical Frame And Aliases

Retail's descriptor is at callee SP+0x38, equivalently **entry SP-0x18**.
The fallback size is at SP+0x40, equivalently **entry SP-0x10**. Zero depth
still calls the loader because size is initialized to one, forwarding the
unwritten descriptor seed. The recovered IDO instructions retain both exact
cells and the original seed-sensitive behavior. Zero/one descriptor
initialization controls fail the physical-seed witness.

This is target-instruction preservation, **not defined portable native C**:
the unwritten local is indeterminate at zero depth or with an unwritten
lookup result. Native fixtures execute only positive depths with lookup
writing the descriptor. Their narrowly scoped GCC maybe-uninitialized warning
exclusion surrounds only the recovered wrapper. No native zero-depth or
unwritten-result acceptance is claimed.

Output/descriptor overlap is deliberately different from an ordinary output:
the initial output-one writes descriptor one, and each output mask removes
the descriptor's high flags in-place. The final loader must reread that cell.
A non-production stale-read instruction control passes the old high flags
instead and fails the witness. The production function has no such control
or patch.

Mapped caller argument-home aliases also preserve their ordered effects:
an output at the first component home changes that component to one; at the
second/third home it changes the future component to the prior descriptor
mask. One bounded depth-home witness initializes depth to one and then
decrements the same cell to zero, suppressing the final load. This does not
claim arbitrary depth/output overlap terminates: other values can underflow
or prolong the retail loop. Saved-register overlap and arbitrary invalid
output addresses are not qualified.

The complete maintained caller frames remain retail-exact:

| Caller | Words | Frame |
| --- | ---: | ---: |
| `func_151D2AB0` | 39 | 0x20 |
| `func_1509B8FC` | 21 | 0x20 |
| `func_15017578` | 26 | 0x28 |
| `func_151F2960` | 146 | 0x18 |
| `func_15085B70` | 30 | 0x18 |
| `func_150025FC` | 50 | 0x28 |

All full slots, original frames and pre-edit hashes are pinned. The complete
`func_15085B70` caller is additionally executed with actual wrapper/cache/
lookup/block instructions: its physical descriptor and fallback remain at
caller-entry SP-0x30 and SP-0x28, respectively. Other caller checks are
static full-slot preservation, not full audio/script/scene execution.

## Compiler Screen

The [128-form screen](../../tools/experiments/game_optional_size_loader_candidates.py)
uses SDK stdarg, default IDO O2/g3 and fixed retail relocations. It includes
all 120 permutations of the five central locals, target/loop/return controls
and zero/one descriptor-initialization negatives. All isolated candidates
compile without diagnostics. Production-source identity is asserted.

| Form | Body Words | Frame | Real Word Differences |
| --- | ---: | ---: | ---: |
| Placeholder | 3 | 0 | 61 |
| Baseline | 61 | 0x50 | 1 |
| Selected layout 6 | 61 | 0x50 | 0 |
| Ternary target | 62 | 0x50 | 51 |
| Inverted target | 61 | 0x50 | 3 |
| Default result before branch | 60 | 0x50 | 17 |
| Descriptor zero | 62 | 0x50 | 49 |
| Descriptor one | 63 | 0x50 | 49 |

Swapping the baseline component/fallback declarations resolves the last
word without changing the frame or semantic operations. Layouts 6, 12, 48,
62, 72 and 86 all match directly; layout 6 is selected. Four unlinked
relocations remain: D_AB1950 HI16/LO16 at 0x44/0x48, lookup at 0x80 and
block-loader call at 0xBC.

## Qualification

The [fifteen-check module](../../tools/tests/test_game_optional_size_loader_match.py)
passes against the rebuilt ELF, pinning compiler/source controls, complete
direct/linked identity and hash, relocations, no guards and all caller slots.

- 14592 native positive-depth boundary cases cover depths 1..16, all missing
  positions, all 16 high-flag combinations, optional/external size outputs,
  signed extremes/repeated components, unsigned base wrap, pointer failure
  and zero/negative final sizes. Lookup counts, full argument consumption,
  descriptor forwarding, pointer/size independence and storage fences are
  checked independently.
- Four native lookup-output-mutation cases preserve descriptor-derived
  output updates and all combinations of NULL/non-NULL pointer with zero/
  nonzero final size.
- 2940 two-way target boundary cases cover depths 0..6, seven incoming
  descriptor seeds, both N64 stack phases, every missing position,
  unwritten lookup callbacks and optional/external output targets. All 61
  words are visited. Full mapped memory including private frames, ordered
  reads/stores/events, calls, return and saved-register lifetime agree
  exactly; no event commutation is used.
- Six descriptor/output overlap cases, eight bounded argument-home alias
  cases, two descriptor-initialization negative controls and a stale final
  reread control witness the physical-cell/order dependencies explicitly.
- 324 connected cases execute freshly compiled block-loader and checked
  lookup/cache source bodies at depths 1..3, every missing position, raw/
  compressed/bit-31 flags, optional output and both allocation failures.
  Independent expected pointer, output size, allocation/free and lookup
  counts agree, including the distinct first/second-failure contracts.
- Seventy-two connected output aliases to cache offset, cache clock and live
  scratch preserve complete memory/call/event effects under explicit callback
  mutations. This is not an allocator ownership or hardware alias guarantee.
- Fifty-six connected zero-depth target cases forward original descriptor
  seeds into the actual block loader with optional output and first-allocation
  failure controls; failure leaves the initialized-one ordinary/fallback size.
- Eight native actual-C wrapper/cache/lookup/block cases cover cache hit/miss,
  optional size and first-allocation failure. SDK DMA/copy/allocation effects
  remain bounded hooks.
- 108 cases execute the complete 30-word Game caller with both wrapper forms
  and actual cache/lookup/block instructions. Path 0x19/component, physical
  descriptor/fallback cells, missing/failure gates and first two header
  halfwords/payload-pointer globals are checked. All 30 caller words are
  covered across the corpus. The downstream `func_15085BE8` is an explicit
  opaque returning boundary, not its original float-heavy body or current
  placeholder; no post-helper state/runtime acceptance is claimed.

Large allocation/transfer amounts qualify call arguments/control, not actual
buffer extents. Synthetic DMA payloads are complete only up to 64 bytes.
Zero-length compressed fixtures supply initialized mapped temporary memory,
not proof of zero-byte allocator behavior or valid asset headers. Native uses
the existing 32-bit freestanding/no-strict-aliasing convention. Real SDK,
allocator/decoder behavior, audio, gameplay and rendering remain separate.

## Measured Progress

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3298 / 5463 (60.37%) | 0 | 2165 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2625 / 4790 (54.80%) | 0 | 2165 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The owner and six caller owners rebuild successfully. Existing unrelated
pointer/integer caller warnings and duplicate generated-slice recipe warnings
remain; the recovered owner and isolated candidates compile without diagnostics.
`make tools-check` passes. Direct full-section comparison confirms Init code
(164048 bytes), Init data (17376 bytes), Debugger code (19800 bytes) and Game
data (189088 bytes / 720 owners) remain retail-exact. Conversion totals and
the 47 retained Init ASM functions are unchanged. README changes contain
aggregate counts only; recovery narration stays in dedicated DOCS.
The final combined resource/matching/tool regression suite passes **247 tests
in 246.404 seconds, no skips**, against the rebuilt ELF. Tools, whitespace,
relative links and the unchanged 10595-row patch-table audit pass.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_optional_size_loader_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_optional_size_loader_match -q -f
wsl make tools-check
git diff --check
```

For the combined suite, use [Note 1000's module list](1000-game-caller-buffer-resource-loader-direct-recovery-and-syscall-boundary-20261005.md)
with `tools.tests.test_game_optional_size_loader_match` and
`tools.tests.test_game_buffer_variadic_loader_match` prepended.

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502B5C8` at
`64CBFDOGL/recomp_out/.c:204311`, with its original frame, separate size/
descriptor cells and live output/descriptor reads already present. No maintained
`src/pc` override/reference is found. No host transplant, build, save or frozen
Release change is made.

Next bounded target: `func_1502B7F0`, still a zero-return placeholder, 60
words / 0x48 frame, ROM 0x58CA0. Unlike the obsolete commented approximation,
retail stores the block pointer through its first argument and **returns the
separate size**, not void or the pointer. Its active caller divides that
count by 24. Recover the SDK variadic signature, size/result-output aliases,
retained incoming zero-depth descriptor and caller frame before adoption.
