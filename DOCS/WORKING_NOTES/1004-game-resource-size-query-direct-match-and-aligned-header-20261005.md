# Game Resource Size Query And Aligned Header

Date: 2026-10-05. Starting HEAD: `4d6ffa72`.

Followup: [Note 1005](1005-game-actor-display-list-scan-match-and-live-callback-state-20261005.md)
recovers the next actor display-list scan. Counts and next-target statements
below remain the historical size-query checkpoint.

## Result And Scope

`func_1502B9B4`'s false zero-return placeholder and obsolete commented
approximation are replaced with SDK-varargs path traversal, rounded raw-size
query and compressed-header size read. All **69 body words / 276 bytes and
the 0x68 frame emit directly under default IDO O2/g3**. The full **71-word /
284-byte slot**, including two trailing zero words, matches retail. No word
guards, profile overrides, inserted/omitted instructions or data-layout changes.

Source: `conker/src/game_57FA0.c`; entry/body-end/slot-end
`0x1502B9B4..0x1502BAC8..0x1502BAD0`; ROM `0x58E64..0x58F78..0x58F80`.
Raw/linked/retail full-slot SHA-256:
`500d45ee24f019fae523dd0626a65273beb0905731a0f6d2b2c7a31e42124d0f`.
Body-only SHA-256:
`5bcb8acf6539ffc03ad0e2dfda8700dfbba780e6da82756871ba90f64e0afa64`.

The owner and sole active C caller owner, `conker/src/init_8180.c`, now use
`u32 func_1502B9B4(u32 depth, ...);`. Its audio bootstrap caller
`func_10008180` remains unchanged and retail-exact across **214 words /
0xF0 frame**. Caller SHA-256:
`e5edcb6039f9b8e816dacd1dea8996ed458a81fa7a68f9f342ef13de781a5dbf`.
Existing caller/local types, allocation parameters and later audio setup are
not refactored. The patch table remains unchanged: 10595 rows, zero duplicates,
zero target rows. Other matching resource helpers are untouched.

## Recovered Contract

Traversal starts at D_AB1950 with gate one. Every signed 32-bit component is
consumed with SDK stdarg; while gate is nonzero, lookup writes the descriptor
and its returned offset is added modulo 2^32. The descriptor's low 28 bits
become the next gate. A missing descriptor stops lookups but still consumes
the remaining components.

Nonzero final gate returns the low 28-bit size rounded up to even. The rounded
maximum 0x0FFFFFFF becomes 0x10000000; there is no extra 28-bit mask after
rounding. When `(descriptor & 0x70000000) == 0x10000000`, the query instead
reads **16 bytes** at the resolved base into its aligned private header and
returns the header's complete first word. Bit 31 does not alter that compressed
flag test. The returned header is not masked, rounded or derived from the DMA
helper's return value. No allocation, decode, free, output pointer or error
helper is introduced.

Positive-depth zero/missing size returns zero with no header DMA. Zero depth
is deliberately different: gate is still one, so a compressed incoming seed
with zero low size still causes the 16-byte header read. Descriptor initialization
would erase this original target behavior and is rejected.

## Physical Frame And Alignment

Descriptor: SP+0x54, **entry SP-0x14**. The three-u64 scratch area is 24 bytes,
starting at SP+0x38. Header selects SP+0x38 when address bit 3 is clear, or
SP+0x40 otherwise. For the two N64 eight-byte stack phases this yields a
16-byte-aligned, fully in-bounds 16-byte destination:

| Entry Stack Phase | Header Relative To Entry | Descriptor Relative To Entry |
| --- | ---: | ---: |
| 0 | -0x30 | -0x14 |
| 8 | -0x28 | -0x14 |

The descriptor is not initialized on entry. Zero-depth and unwritten-result
instruction cases retain the incoming seed. This is **target preservation,
not defined portable native C** for indeterminate-local reads. Native fixtures
use positive depth with a descriptor-writing lookup only. Their narrow
maybe-uninitialized exclusion surrounds only the recovered query.

Native GCC i386 naturally differs from MIPS o32 in u64 alignment. The native
fixture explicitly aligns its u64 typedef to eight bytes to state the target
ABI premise, rather than claim this scratch rule is portable to arbitrary
native stack alignment. Actual SDK stdarg and the existing 32-bit freestanding/
no-strict-aliasing test convention are used. Target tests independently exercise
both real stack phases and full private memory/events.

The final header load executes after DMA. Explicit DMA callbacks overwrite
the descriptor and caller-saved registers, and return values distinct from
the header; the query still returns the live header word. A stale instruction
control substituting the DMA return fails this witness. Production has no
instruction controls or patches. Arbitrary pointer/saved-frame corruption
and hardware DMA semantics are not qualified.

## Compiler Screen

The [136-form screen](../../tools/experiments/game_resource_size_query_candidates.py)
uses default IDO O2/g3, actual SDK stdarg and fixed retail relocations. It
includes all 120 central-local permutations, u32/u64/byte scratch forms,
initialization/update controls and zero/one descriptor-initialization negatives.
Production-source identity is asserted.

| Form | Body Words | Frame | Real Word Differences |
| --- | ---: | ---: | ---: |
| Placeholder | 3 | 0 | 69 |
| Baseline u32 scratch | 69 | 0x68 | 7 |
| u64 scratch only | 69 | 0x68 | 5 |
| Layout 1, u32 scratch | 69 | 0x68 | 4 |
| Selected layout/u64 scratch | 69 | 0x68 | 2 |
| Selected size-first initialization | 69 | 0x68 | 0 |
| Selected comma initialization | 69 | 0x68 | 2 |
| Selected descriptor zero/one | 71 | 0x68 | 58 |

Layout 1 places size before descriptor, recovering descriptor SP+0x54.
Three u64 words recover scratch SP+0x38 and alternate pointer SP+0x40.
Initializing size before base produces retail's interleaved root-high,
size-one, root-low schedule and eliminates the final two differences.
All 136 isolated candidates compile without diagnostics. Four unlinked
relocations: D_AB1950 HI16/LO16 at 0x2C/0x34, lookup call at 0x70 and
header-DMA call at 0xE4.

## Qualification

The [eleven-check module](../../tools/tests/test_game_resource_size_query_match.py)
passes against the rebuilt ELF, pinning complete raw/linked/retail words,
frame/padding, controls, source/prototypes, no guards, relocations and full
Init caller slot/hash.

- 7296 native boundary cases cover depths 1..16, all missing positions, all
  16 high-flag combinations, signed extremes/repeated components, unsigned
  base wrap and zero/high-bit/all-one header words. Lookup counts, complete
  component consumption, rounded raw size and header-vs-DMA-return behavior
  are checked independently. No native zero-depth acceptance is claimed.
- 5670 two-way target boundary cases cover depths 0..6, nine incoming seeds,
  both stack phases, all missing positions, unwritten callbacks, raw/compressed/
  bit-31 flags and three header words. All 69 body words are visited; the two
  padding words are pinned statically. Full mapped/private memory, ordered
  reads/stores/events, call arguments, return and saved-register lifetime
  agree exactly without commuting events. Independent expectations check
  lookup count, resolved base, rounded size and physical header destination.
- Eighteen live-header cases use DMA returns 0/1/0xFFFFFFFF while overwriting
  the descriptor and caller-saved registers. Two descriptor initializer
  controls and a wrong u32-scratch layout fail the physical witnesses;
  a stale final-load control returns DMA status instead of header size.
- 972 cases execute freshly compiled actual lookup and checked cache-installer
  bodies at depths 1..3, all missing positions, three flag forms, six lengths
  including 0x0FFFFFFE/0x0FFFFFFF, three headers and both stack phases.
  The query makes no allocation/decode/free calls. Expected lookup/header
  counts and returned sizes are independent of the comparison model.
- Fifty-four connected zero-depth cases forward incoming seeds directly,
  including compressed zero-length seeds that still read the header.
- 384 native actual-C query/lookup/cache cases cover cache hit/miss, all
  16 high flags, lengths 0..3 and three header words. Modeled SDK DMA/copy
  effects and expected call counts remain explicit bounded hooks.
- Seventy-two original Init caller prefixes execute its first **66 words**
  through actual query/lookup/cache instructions and opaque earlier setup/
  resolver/allocation calls. Depth/components are 2/0x17/0. Query descriptor
  is physically at caller-entry SP-0x104; header is SP-0x120 or SP-0x118.
  Returned zero/rounded/high-bit/all-one sizes pass unchanged into the bank
  allocation `(size,0xFF,2,0)` and pending load `(bank,size,2,0x17,0)`.
  There is no added failure guard, cap conversion or extra size mask.

The Init prefix stops before `func_1502B8E0` at the pending bank-load call.
It does not execute the later bank patcher, sequence setup, players, sound
manager or full audio startup. The complete 214-word caller is separately
static-verified; this is not claimed as full caller execution. Returning mapped
opaque allocations qualify argument transport, not real allocation success or
large/high-bit requested buffer extents. Header DMA writes exactly 16 mapped
bytes. Real SDK/hardware, allocator, audio, gameplay, rendering and PC runtime
acceptance remain separate.

## Measured Progress

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3300 / 5463 (60.41%) | 0 | 2163 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2627 / 4790 (54.84%) | 0 | 2163 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The owner and Init caller owner rebuild successfully. Existing unrelated
Init pointer/integer and duplicate generated-recipe warnings remain; isolated
recovered candidates have none. A pre-edit address/length/SHA-256 snapshot of
all **6060 function slots** compared with the rebuilt ELF confirms only
`func_1502B9B4` changes, with no added/deleted slots. The caller and other
resource helpers stay unchanged.

Full protected sections remain retail-exact: Init code 164048 bytes, Init
data/rodata 17376 bytes, Debugger section 19800 bytes, Game data 189088 bytes /
720 owners. Conversion totals and 47 retained Init ASM functions are unchanged.
The 10595-row patch table is unchanged. `make tools-check` passes. README
changes contain aggregate counts only; function detail stays in DOCS.

The combined resource/matching/tool regression suite passes **272 tests in
239.593 seconds, no skips**, against the rebuilt ELF. Tools, whitespace and
relative links pass. The patch-table SHA-256 remains:
`131118dfc98562a5608c9f3a40e29ec75a5ceb712c629f02880b2c126ce9c5c8`.

## Reproduction

Run from the `64CBFD` root in PowerShell:

```powershell
wsl python3 -m tools.experiments.game_resource_size_query_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_resource_size_query_match -q -f
wsl make tools-check
git diff --check
```

For the combined regression use [Note 1003's modules](1003-game-counted-pointer-loader-direct-match-and-full-caller-20261005.md)
and prepend `tools.tests.test_game_resource_size_query_match`.

## Host Boundary And Next

Read-only sibling inspection finds translated `func_1502B9B4` at
`64CBFDOGL/recomp_out/.c:205123`, with the original cursor, incoming descriptor,
scratch-alignment branch and live header read already present, plus a
preexisting cadence diagnostic. The translated category caller also records
an earlier explicit vararg correction; this is not a new PC-port fix.
No maintained `src/pc` reference/override is found. No host transplant, build,
save or frozen Release change is made.

Next bounded target: adjacent `func_1502BAD0`, **173 words / frame 0x48**,
ROM 0x58F80, currently a zero-return placeholder in
`conker/src/game/generated_58F80.c` and differing at 169 linked words.
Retail scans **25 actors at stride 0x32C**, emits opening/closing display-list
references, maintains tagged diagnostic slot state and invokes mode-specific
actor render helpers. Recover its Gfx pointer return, signed 16-bit argument,
actor/state exclusions, live helper reads and cleanup before matching its
register/save schedule. Reference: `conker/asm/58F80.s`.
