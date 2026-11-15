# Game projection bounds guarded match

Date: 2026-11-14. `func_1510AEE0` now replaces its zero-return placeholder
with the recovered ordered projection/depth predicate and optional output
ratios. All **97 body words**, plus **three alignment words**, match retail
after **82 checked guard rows**. Owner `generated_137ED0` advances from
**2 / 4** to **3 / 4 exact**. This completes the private screen in
[Note 2406](2406-game-projection-bounds-private-screen-20261114.md).

The actual production ELF recount is **4,494 / 5,515 (81.49%)** total and
**3,821 / 4,842 (78.91%)** Game, zero address drift, **1,021** still different.
Init remains **492 / 492**, Debugger **181 / 181**. **194 more matches** reach
the active 85% total goal. Converted counts/bytes remain **5,515 / 6,048
(91.19%) / 86.17%**; the root README changes only aggregate figures.

## Source and instruction contract

Owner: `conker/src/game/generated_137ED0.c`; original assembly remains
`conker/asm/137ED0.s`. Body VA **0x1510AEE0..0x1510B064**, ROM
**0x138390..0x138514**; its aligned slot ends at VA **0x1510B070** / ROM
**0x138520**. The original leaf frame is **0x10**. Baseline consumer
`6fec71d3f43e2762651b3ed7e8c561428378f0e6`, tools
`635058a13192e74c31f5cacdb7c2022d61b29957`.

The ten-argument interface takes a 4x4 float matrix, X/Y/Z, near/far planes,
two projection scales and two optional output pointers. It computes the
three ordered dot products, rejects depth and scaled horizontal/vertical
bounds, then writes `1 - component / depth` to each non-null output.
The second pointer is read after the first output store; the private vertical
value is also reloaded for that second output. These matter when the first
output aliases an incoming parameter home or the private vertical home.

Explicit statement staging preserves the original floating-point operand
order, including translation plus accumulated products. The value-parameter
and private-local `volatile` qualifiers enforce the observed stack-home
reads/writes in this implementation. They do **not** establish that the
original source used those qualifiers; matrix elements and output pointees
are ordinary float objects.

Raw IDO C emits **93 words**, frame **0x10**, no target relocations, SHA-256
`5e16ac6bf09f1d80c3a699f5b2f61e17b42d1fbf620813804c781226c6f884f5`.
The checked normalizer consumes every raw word exactly once. Its explicit
ledger changes 70 register fields across **45 words**, maps **ten branch
edges**, changes **two false-likely branches** to ordinary false branches,
replaces two unreachable duplicate lowering words at raw +0x60/+0xC8 with
NOPs, and inserts **four pipeline NOPs** at normalized
+0x11C/+0x124/+0x144/+0x16C. The four insertions produce the original 97-word
body; the existing three alignment NOPs complete its 100-word slot. There
are no omitted manifest rows. All **three neighboring functions** and owner
pools remain unchanged in raw and padded checks.

Normalization reads no retail ROM bytes. It requires the exact raw hash and
empty binding map, then independently proves the ordered symbolic behavior
before checking its result against retail. **94 corruption controls** reject
all 93 changed raw words and an unexpected binding. This is a guarded match,
not a claim that the compiler directly emits all retail words.

## Qualification

- [x] Ordered symbolic FP expression trees, full symbolic memory, saved
  registers, restored SP/RA and final condition agree across **300 alias
  layouts / 2,235 terminal paths**. Matrix/parameter/private/output overlap
  includes the first output overwriting the later pointer home. Three valid
  instruction controls reject a near comparison, matrix column and premature
  pointer cache. The cache control agrees for ordinary separate outputs and
  fails specifically for the pointer-home alias.
- [x] **2,598 guest cases** compare retail, raw C and normalized instructions
  with an independent ordered finite model and complete memory maps. These
  visit **96 / 97** retail body words. Near/far/scale boundaries, null/shared
  and matrix outputs, and incoming/private stack-home aliases are included.
  Three effective emitted controls change the near boundary, matrix column
  and output subtraction. **205 memory-access prefixes** compare complete
  retail/normalized machine state, PC and branch-delay ownership.
- [x] **96 quiet-NaN cases** preserve payload/operand behavior under two
  explicitly assumed left/right preferred quiet-payload rules. Actual hardware
  NaN selection and FCSR exception behavior remain unverified. The raw C
  instruction schedule has no precise fault-order claim.
- [x] **2,577 native32 cases per O0/O2/O3**, with undefined-behavior traps,
  compare all 16 matrix words and four output words. Finite cases cover null,
  shared and matrix outputs; output divisions use nonzero depth. Five
  effective source controls reject near/far comparisons, both output signs
  and the vertical matrix column. Guest parameter/private-home aliases are
  separate from this portable native contract.
- [x] All **four authentic JAL/delay-slot windows** execute **256 caller
  cases** with all three streams. Sites are VA **0x151767CC**, **0x15176830**,
  **0x15177138**, **0x1517A448**. Their real SWC1 delay slots transport the
  final scale word; all ten argument words are checked. An aligned full-input
  scan finds those four literal JALs and no literal function pointer. This
  does not exclude computed/external calls or qualify full parent gameplay.
- [x] Both **complete-owner padders**, all four owner functions, four
  independent code/data layouts and **12 GNU links** pass, including the
  unchanged neighbors' relocated bindings.
- [x] Mounted pre-install suite passes in **24.566 s**, isolated sibling suite
  in **25.711 s**, and installed mounted suite in **21.656 s**. Fresh
  `make tools-check` passes. An earlier negative-control interpreter lacked
  C.LE and OR-with-zero move support; those fixture instructions are now
  implemented, and controls fail through behavior differences rather than
  unsupported-instruction errors.

Reproduce using the prepared consumer:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_projection_bounds_1510aee0_match -v
make tools-check
```

Seven byte-identical task files were qualified in an ignored overlay using
sibling dependencies with mounted fallback. Sibling HEAD remains
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all **2,439 dirty paths** and
status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
are unchanged. No sibling files were replaced.

## Production image and handoff

All **809 frozen inputs** were checked before installation. The actual Make
recipe's three owner commands were independently exercised before linking;
the scoped production Make then rebuilt and recounted the actual ELF.
The existing duplicate `generated_12D630` Make recipe warning remains.

The entire production ELF equals the independently predicted image:
**268 changed bytes**, solely the target body and its size, with **zero
metadata permutations / zero exclusions**. All **6,051 function addresses**
remain fixed. Only the intended object changes among **698 objects**;
its changed sections are `.text`/`.symtab`. All **82 headers**, conversion
rows, three owner neighbors and **805 immutable inputs** remain fixed. The
guard CSV retains its complete old byte prefix and appends exactly 82 target
rows, including four inserted NOPs.

Protected data is exact across **189,088 bytes / 720 owners**, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Production ELF SHA-256:
`a68b4f502f52e0d5e796d535f40cfc6fb1b84873dba0203a76c22d32da4df5f1`.
Ignored qualification artifacts are under
`conker/build/game-projection-bounds-1510aee0-match/`.

Scoped Graphify AST refresh covers **eight files**, retaining all **61,016
old IDs** with zero loss: **61,053 nodes / 114,751 links**, zero LLM tokens.
This is a scoped merge, not full-corpus re-extraction. Routine Claude calls:
zero. Tools commit `4992782c21befe37073c751fe7874c39af9a49ee` precedes the consumer pin/source/
documentation commit. No push; the sibling host has no applicable source
checkout here and its Release remains frozen.

Next screen: the owner's remaining **229-word `func_1510AA44`**. The separate
961-word common particle updater remains private at
[Note 2452](2452-game-common-particle-frame-native-and-callers-20261114.md), with
no installation or credit. Its old frozen baseline must be retained; any
future installation prediction needs the newly adopted production baseline.
