# Game Counted Pointer Loader And Full Caller

Date: 2026-10-05. Starting HEAD: `4a798e79`.

Follow-up: [Note 1004](1004-game-resource-size-query-direct-match-and-aligned-header-20261005.md)
completes the next size-query wrapper and qualifies its Init caller prefix.
Results and next-target description below remain this note's historical
checkpoint, not the latest resume boundary.

## Result And Scope

`func_1502B7F0`'s false zero-return placeholder is replaced with semantic
SDK-varargs traversal, pointer-output loading and a separate unsigned returned
size. All **60 words / 240 bytes and the 0x48 frame emit directly under
default IDO O2/g3**. No word guards, profile overrides, inserted/omitted
instructions or data-layout changes. The obsolete commented void approximation
is removed; it did not express the retail return contract.

Source: `conker/src/game_57FA0.c`; entry/end `0x1502B7F0..0x1502B8E0`;
ROM `conker/conker.us.bin+0x58CA0..0x58D90`.
Complete raw/linked/retail SHA-256:
`e88dfdc70feb02075b447f087746999e1077f259047c8f4c20482f6be3f156f6`.

The shared declaration is now `u32 func_1502B7F0(void **output, u32 depth, ...);`.
Its sole active C caller, `func_15016690`, explicitly casts the existing
struct-pointer output cell to `void **`. The original unsigned division by
24 and record layout remain unchanged. Its complete 112-word slot / 0x28
frame is still retail-exact; SHA-256:
`723d1caa2c30b4efcba8eab56eb2533207c0dd09cf358d5b9227e14ed0a19804`.
Other references in commented unrecovered handlers are not active caller
qualification. The shared patch table remains unchanged: 10595 rows, zero
duplicate keys, zero target rows.

## Recovered Contract

Traversal starts at D_AB1950 with private size one. All signed 32-bit path
components are consumed with SDK stdarg. While size is nonzero, lookup writes
the descriptor and returns an offset added modulo 2^32. Each iteration masks
the descriptor to 28 bits and decrements depth. A missing descriptor stops
lookups, not remaining argument consumption. The output pointer cell is not
written during traversal.

After traversal, nonzero size calls `func_1502B350(base, descriptor, &size)`
and stores the returned pointer through the live output argument. Zero size
stores NULL without calling the block helper. The final size is reread after
that pointer store and returned as all 32 unsigned bits. There is no NULL
output-cell check: the first argument must address a writable pointer cell.

Pointer and size are independent. First allocation failure returns NULL
without replacing the masked size; at zero depth that retained size is one.
Second allocation failure writes size zero. A successful decoder may return
zero with a non-NULL pointer. None of these combinations is collapsed or
"fixed" into a pointer-validity test.

## Physical Frame And Aliases

Retail descriptor: SP+0x34, **entry SP-0x14**. Private initialized-one size:
SP+0x38, **entry SP-0x10**. Incoming output/depth homes: SP+0x48/SP+0x4C;
first two component homes: SP+0x50/SP+0x54. Descriptor is not initialized on
entry. Zero depth still invokes the block loader with the original incoming
descriptor seed. Zero/one initializer controls fail the physical seed witness.

This preserves target instructions, **not defined portable native C** for
indeterminate descriptor reads. Native cases use positive depth and a
descriptor-writing lookup only. The narrow native warning exclusion surrounds
only this wrapper. Saved-register overlap, invalid output addresses and
arbitrary callback corruption are not qualified.

Bounded output aliases to descriptor, size and incoming argument homes retain
their ordered effects. Unlike the optional-size wrapper, there is no initial
output-one store to alter upcoming components. An output alias to private size
receives the final pointer word, and that same word becomes the returned count
because the size reload follows the pointer store. Descriptor overlap does not
retroactively change the already completed load.

The output home is reread at `0x1502B8AC` after the block call. An opaque
callback that redirects this home causes the final pointer store to use the
new mapped cell. A stale-load negative instruction control fails that witness.
The production function has no instruction controls or patches.

A connected fixture initially allocated its expanded buffer at the stack entry
address inherited from a previous wrapper's tests. Decode then overwrote this
wrapper's output home and the real reread attempted an unmapped pointer store.
The fixture now allocates expanded storage separately at 0x70000. Explicit
argument-home/private-cell witnesses remain; no production behavior was changed
to accommodate the invalid ordinary-allocation fixture.

## Compiler Screen

The [132-form screen](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_counted_pointer_loader_candidates.py)
uses default IDO O2/g3, actual SDK stdarg and fixed retail relocations. The
initial 127 forms include 120 local-declaration permutations; five additional
loop/update variants pursue the best two-word result. Production identity is
asserted. All 132 isolated candidates compile without diagnostics.

| Form | Body Words | Frame | Real Word Differences |
| --- | ---: | ---: | ---: |
| Old five-argument placeholder | 7 | 0 | 60 |
| Baseline | 60 | 0x48 | 10 |
| Layout 1 | 60 | 0x48 | 2 |
| Selected size-first update | 60 | 0x48 | 2 |
| Selected for-loop update | 60 | 0x48 | 0 |
| Descriptor zero | 61 | 0x48 | 48 |
| Descriptor one | 62 | 0x48 | 50 |

Layout 1 puts size before descriptor in local declarations. Moving depth's
decrement into the `for` update resolves the independent stores at offsets
0x94/0x9C: depth stores before the branch, size in the branch delay slot.
Both source assignment orders in the while loop leave those two differences.
Four unlinked relocations remain: D_AB1950 HI16/LO16 at 0x30/0x38, lookup
call at 0x78, block call at 0xB4.

## Qualification

The [fourteen-check module](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_counted_pointer_loader_match.py)
passes against the rebuilt ELF. It pins complete raw/linked/retail identity,
frame/hash, source/prototype, caller slot, relocations and absence of guards.

- 7296 native positive-depth cases cover depths 1..16, every missing position,
  all 16 high-flag combinations, signed extremes/repeated components, unsigned
  base wrap and independent NULL/non-NULL pointer with zero/negative size.
  Lookup counts, all argument consumption and output/storage fences are
  checked independently. No native zero-depth acceptance is claimed.
- 1470 two-way target boundary cases cover depths 0..6, seven incoming seeds,
  both N64 stack phases, all missing positions and unwritten lookup callbacks.
  All 60 words are visited; full mapped memory, ordered reads/stores/events,
  call arguments, return and saved-register lifetime agree without commuting
  events. Independent expectations check base, descriptor, size and pointer.
- 84 private-size/descriptor/argument-home output cases preserve physical
  store/reload order; two redirected output-home cases, a stale-load control
  and two descriptor-initialization controls witness the live dependencies.
- 162 cases execute freshly compiled actual block-loader and checked
  lookup/cache bodies with raw/compressed/bit-31 flags, missing paths, depths
  1..3 and both allocation failures. Expected sizes, pointers, lookup counts
  and allocation counts are independent of the comparison model.
- 72 connected pointer outputs alias actual cache offset, clock and live
  scratch under explicit callback mutations. The final pointer store and
  returned private size stay distinct. These are bounded effects, not an
  allocator ownership or hardware alias guarantee.
- 28 connected zero-depth seed cases execute the actual block loader. First
  allocation failure leaves size one and stores NULL to output.
- Four native actual-C wrapper/cache/lookup/block cases cover hit/miss and
  first-allocation failure. Failure stores NULL but retains returned size 16.
- 432 cases execute the complete Game caller with actual wrapper/cache/lookup/
  block instructions, both stack phases, scene-present/default fallback,
  components 1..3, every missing position, raw lengths 16/48 and compressed
  decode, plus both allocation failures. Components are 12/component/6;
  descriptor/size are physically at caller-entry SP-0x3C/SP-0x38.
  All **108 reachable caller words** are covered. The compiler's unreachable
  duplicate load at 0x150167D0 and three trailing padding words are pinned by
  full-slot identity, not artificially executed for coverage.
- Sixteen isolated caller-boundary cases qualify unsigned counts
  0/1/23/24/25/0x7FFFFFFF/0x80000000/0xFFFFFFFF and NULL/non-NULL outputs.
  The original `divu` word 0x0041001B is pinned. Only its nonzero-divisor,
  low-word quotient is added to the scoped oracle; no generic MIPS/FCSR
  emulation claim is made.

The caller writes both state globals -1 and count `size / 24`. Only zero
quotient invokes `allocate_memory(24,1,0,0)` and replaces count with one.
A NULL pointer with size 48 therefore remains NULL with count two; no new
fallback gate is introduced. Mapped fallback storage is checked independently:
scene-present signed halfwords, float coordinates plus 100, scene byte at +7,
or default halfwords 3600/-3200/-2200 and float 1000; zero bytes at +6/+0x15
and untouched record bytes/fences. Fallback allocation failure is not safely
handled by the original caller and is not claimed as qualified continuation.

SDK DMA/copy/allocation/decoder effects remain bounded hooks. Synthetic DMA
payloads are complete only up to 64 bytes; larger counts qualify arguments and
control, not physical buffer extents. Initialized mapped zero-length header
fixtures are not proof of allocator or asset validity. Native uses the existing
32-bit freestanding/no-strict-aliasing convention. Actual SDK, hardware, runtime,
gameplay and rendering remain separate acceptance tasks.

## Measured Progress

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3299 / 5463 (60.39%) | 0 | 2164 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2626 / 4790 (54.82%) | 0 | 2164 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The shared-header rebuild succeeds. A pre-edit SHA-256/address/length snapshot
of **all 6060 function slots** compared against the rebuilt ELF confirms only
`func_1502B7F0` changes, with no added/deleted function slots. Its sole active
caller remains unchanged. Existing unrelated pointer/integer and duplicate
generated-recipe warnings remain; isolated recovered candidates have none.

Complete protected sections remain retail-exact: Init code 164048 bytes,
Init data/rodata 17376 bytes, Debugger section 19800 bytes, Game data
189088 bytes / 720 owners. Conversion totals and the 47 retained Init ASM
functions are unchanged. README edits are aggregate counts only; narration
stays in DOCS. `make tools-check` passes.

The combined resource/matching/tool regression suite passes **261 tests in
217.336 seconds, no skips**, against the rebuilt ELF. Tools, whitespace and
relative links pass. The shared patch table is unchanged, SHA-256:
`131118dfc98562a5608c9f3a40e29ec75a5ceb712c629f02880b2c126ce9c5c8`.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_counted_pointer_loader_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_counted_pointer_loader_match -q -f
wsl make tools-check
git diff --check
```

For the combined suite, use [Note 1002's modules](1002-game-optional-size-loader-direct-match-and-live-output-aliases-20261005.md)
and prepend `tools.tests.test_game_counted_pointer_loader_match`.

## Host Boundary And Next

Read-only sibling inspection finds translated `func_1502B7F0` in
`64CBFDOGL/recomp_out/.c:204822`. Its original frame, separate descriptor/size,
post-block output-home reread and final size return are already present.
No maintained `src/pc` reference/override is found. No host transplant,
build, save or frozen Release change is made.

Next bounded target: `func_1502B9B4`, still a zero-return placeholder,
**69 body words / 71 slot words, frame 0x68**, ROM 0x58E64. It traverses
SDK-varargs paths but returns the rounded resource size, reading a 16-byte
compressed header into a stack-phase-dependent aligned buffer instead of
allocating/decompressing a resource. Preserve its incoming descriptor at
entry SP-0x14, zero-depth seed dependency, both header-buffer choices and
live DMA result before adopting a size-query C body.
