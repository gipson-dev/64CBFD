# Game Buffer Variadic Wrapper And Incoming Descriptor Frame

Date: 2026-10-05. Starting HEAD: `16975bfd`.

## Result And Scope

`func_1502B8E0`'s false zero-return placeholder is replaced with its semantic
SDK-varargs resource-path traversal and caller-buffer loader wrapper. All
**53 words / 212 bytes and the original 0x48 frame emit directly from default
IDO O2/g3**, without word guards, compiler-profile overrides or inserted/
omitted instructions. The complete linked slot is also retail-exact.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502B8E0..0x1502B9B4`;
ROM `conker/conker.us.bin+0x58D90..0x58E64`.
Complete raw/linked/retail SHA-256:
`2212c3662f9ec8a1cd54a8a6b594e65e25d31294efb74d9580842c5901633fbd`.

Declarations in the owner, Game caller `game_36680.c` and Init caller
`init_8180.c` now use the same three-named-argument variadic prototype and
32-bit returned count. Caller bodies are unchanged. The patch table is
unchanged, with no wrapper rows; conversion counts and the 47 retained Init
ASM routines are unchanged. No sibling source/build/save/Release changes.

## Recovered Contract

The wrapper starts at D_AB1950 with a separate gate initialized to one.
Each signed 32-bit path component is consumed using the actual SDK stdarg
header. While the gate is nonzero, `func_1502AC88` receives the current base,
component and descriptor address. Its returned offset is added modulo 2^32.
The depth is decremented and the full descriptor's low 28 bits become the
next gate. A missing descriptor stops subsequent lookups but does not stop
consumption of the remaining arguments.

If the final gate is nonzero, `func_1502B224` receives the resolved address,
original caller buffer, full descriptor (including high flags), and cap.
The wrapper returns that loader's low 32-bit count, including zero or
0xFFFFFFFF. A missing path returns zero without touching the caller buffer.
There is no output allocation, extra size pointer, fallback or synthesized
descriptor initialization.

## Incoming Frame Boundary

Retail writes no descriptor before entering the path loop. At zero depth,
the initial gate remains one and the loader is still called with the word
read from callee SP+0x34, equivalently **wrapper-entry SP-0x14**. A lookup
boundary that leaves the descriptor unwritten retains the same incoming
bytes; their low 28 bits govern subsequent lookup/loading gates.

The recovered IDO code preserves this exact 0x48 frame, slot, uninitialized
load and seed-sensitive behavior. Zero/one initialization controls change
both loader arguments and physical memory and are explicitly rejected.
This is **target-instruction preservation, not portable defined C behavior**:
the unwritten C local remains indeterminate. Native tests execute only
positive depths whose lookup writes the descriptor; they do not qualify
native zero-depth or unwritten-lookup behavior. A narrowly scoped
GCC maybe-uninitialized warning exclusion surrounds only this recovered body
in the native fixture, not production or unrelated code.

This frame audit follows the distinction in [Note 986](986-game-light-selector-candidate-fitting-and-connected-frame-witness-20261005.md):
a nominal callee-relative match alone is insufficient if a connected caller
has changed its physical stack frame. Here the complete maintained Game
caller `func_1500ABA0` (29 words / 0x20 frame) and Init caller `func_10008180`
(214 words / 0xF0 frame) remain retail-exact after the prototype edits.
The Game caller's lookup descriptor pointer is observed at caller-entry
SP-0x34 in every connected case. Init's unchanged frame composes to SP-0x104;
its full slot/frame is statically checked, not executed as a full audio-init
routine by this module. Both natural callers use positive depths (3 and 2),
so standalone zero-depth seed tests are not described as natural caller runs.

Original assembly `conker/asm/43D00.s` also shows `func_150169A0` calling the
wrapper with depth two, cap zero, a 0x58 frame and components 0xE/category.
However, current `conker/src/game/generated_43D00.c` still contains its
zero-return placeholder, and the linked slot is not retail-exact. This is
reference-only caller evidence, not retained working assembly or connected
runtime qualification. It is untouched by this recovery.

## Compiler Screen

The [133-form screen](../../tools/experiments/game_buffer_variadic_loader_candidates.py)
uses SDK stdarg, default IDO O2/g3 and fixed retail relocations. It includes
all 120 local-declaration permutations, ordering/register/control variants
and zero/one descriptor-initialization negative controls. All isolated forms
compile without diagnostics.

| Form | Body Words | Frame | Real Word Differences |
| --- | ---: | ---: | ---: |
| Placeholder | 3 | 0 | 53 |
| Baseline | 53 | 0x48 | 5 |
| Layout 1 | 53 | 0x48 | 2 |
| Baseline gate-first | 53 | 0x48 | 3 |
| Selected gate-first | 53 | 0x48 | 0 |
| Selected descriptor zero | 54 | 0x48 | 41 |
| Selected descriptor one | 55 | 0x48 | 44 |

The selected local order is path, component, base, gate, descriptor. Gate-
first initialization resolves the two independent opening words at 0x30/
0x34 without guards. The driver asserts production-source identity. Four
unlinked relocations are pinned: D_AB1950 HI16/LO16 at 0x2C/0x34, lookup
call at 0x70 and buffer-loader call at 0xA4.

## Qualification

The [eleven-check module](../../tools/tests/test_game_buffer_variadic_loader_match.py)
passes against the rebuilt ELF and pins source, compiler controls, full
retail identity, caller frames, relocations and absence of guards.

- 21888 native positive-depth boundary cases cover depths 1..16, every
  missing-path position, all 16 flag combinations, three caps, signed
  extremes/repeated components, unsigned base wrap and zero/0xFFFFFFFF
  loader returns. Full argument consumption, lookup counts, full descriptor
  forwarding and destination fences are checked independently.
- One native NULL-buffer missing-path case requires no loader/destination
  access while all four path arguments are still consumed.
- 2268 two-way target boundary cases cover depths 0..8, both valid N64
  stack phases, seven physical descriptor seeds, every missing position,
  descriptor-writing/unwritten callbacks and signed/wrapping components.
  All 53 words are visited. Complete mapped memory including private frames,
  ordered reads/stores/events, call arguments, return and saved-register
  lifetime agree exactly, with no event commutation.
- Both zero/one initialization controls fail a zero-depth seed witness at
  entry SP-0x14. The descriptor is not initialized to make tests convenient.
- 600 connected cases execute freshly compiled `func_1502B224`, checked
  lookup/cache source bodies and retail/recovered wrapper instructions.
  Depths 1..5, all missing positions, raw/compressed/bit-31 flags, five caps
  and both stack phases preserve resolved addresses/counts and all effects.
- Fourteen connected zero-depth cases execute the actual buffer loader with
  all seven incoming seeds at both stack phases. No lookup runs. Original
  raw/compressed length and return selection remain seed-sensitive.
- Four connected compressed allocation failures stop after allocation and
  return zero. Eight decode-mismatch prefixes stop before the original
  handwritten syscall helper; error word, retained decoded count, return
  address and full memory/event prefix agree, with no cleanup yet executed.
- Forty-eight cases execute all 29 Game caller words, both wrapper forms
  and actual lookup/cache/loader bodies. They check the 12/component/10
  path, SP-0x34 descriptor address, missing gates and all three bzero calls.
  The two later arrays are adjacent, so fences surround their combined
  1800-byte cleared extent rather than falsely treating the shared boundary
  as untouched memory.

SDK DMA/bcopy/bzero, allocation and decoder effects are explicit bounded
hooks, not hardware or real-asset acceptance. Transfers up to 64 bytes have
synthetic complete payloads; large seeded lengths qualify call arguments/
control only, not actual transfer/buffer extents. Zero-length compressed
fixtures have mapped initialized temporary storage, not proof of actual
zero-byte allocator behavior. Trap prefixes do not qualify exception
recovery, actual post-trap cleanup or return. Native uses the existing
32-bit freestanding GCC/no-strict-aliasing convention. No general native
portability, full Init sound setup, gameplay or rendering claim is made.

## Measured Progress

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3297 / 5463 (60.35%) | 0 | 2166 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2624 / 4790 (54.78%) | 0 | 2166 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The owner and both caller owners rebuild successfully. Existing unrelated
pointer/integer caller warnings and duplicate generated-slice recipe warnings
remain; the recovered owner and isolated candidates compile without
diagnostics. `make tools-check` passes. Direct full-section comparison
confirms Init code (164048 bytes), Init data (17376 bytes), Debugger code
(19800 bytes) and Game data (189088 bytes / 720 owners) remain retail-exact.
The final combined resource/matching/tool regression suite passes **232 tests
in 178.769 seconds, no skips**, against the rebuilt ELF. Patch-table audit
confirms 10595 rows with no duplicates or wrapper rows; whitespace checks pass.
README edits contain aggregate counts only; narration stays in DOCS.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_buffer_variadic_loader_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_buffer_variadic_loader_match -q -f
wsl make tools-check
git diff --check
```

## Host Boundary And Next

Read-only sibling inspection finds translated retail `func_1502B8E0` at
`64CBFDOGL/recomp_out/.c:204981`, retaining the original frame and SP+0x34
descriptor load. No maintained `src/pc` override/reference is found. This
does not authorize source transplantation or a host build; sibling source,
build, saves and frozen Release remain untouched.

Next bounded target: `func_1502B5C8`, still a zero-return placeholder,
61 words / 0x50 frame, ROM 0x58A78. Recover its optional size-output/fallback,
SDK varargs, descriptor gates and connected `func_1502B350` contract. Audit
its unwritten zero-depth descriptor and output aliases before adopting any
nominal byte match; do not initialize away incoming state or discard seeds.
Its retail descriptor is SP+0x38 (entry SP-0x18), distinct from the fallback
size at SP+0x40 (entry SP-0x10). Size starts at one, is read live as the gate
and receives masked descriptor updates before the final loader call. Preserve
that distinction and the final descriptor reread when qualifying output aliases.
