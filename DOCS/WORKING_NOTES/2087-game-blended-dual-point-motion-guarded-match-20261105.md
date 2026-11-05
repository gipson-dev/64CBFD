# Working Note 2087: Game blended dual-point motion guarded match

Date: 2026-11-05

## Recovered callback and fields

`func_1518EF54` occupies `0x1518EF54..0x1518F058`, ROM
`0x1BC404..0x1BC508`, in `generated_1BA1D0.c`: **65 words / 260 bytes**,
**frame zero**, and two timestep relocations. Its zero-return placeholder is
replaced by `s32 func_1518EF54(BlendedDualPointMotion1518EF54 *motion)`.
The local record view is `0x160` bytes; existing shared types and the adjacent
`DualPointMotion1BA1D0` view remain unchanged.

| Field | Offset | Recovered use |
| --- | --- | --- |
| Position XYZ | `+0x34` | First point advanced by captured displacement |
| Endpoint XYZ | `+0x40` | Second point advanced, then blended |
| Velocity XYZ | `+0x140` | X/Z damping, Y acceleration |
| Vertical acceleration | `+0x14C` | Multiplied by the early timestep read |
| Damping | `+0x150` | Captured once for X/Z velocity |
| Blend | `+0x15C` | Three component reads; payload-view offset `+0x4C` |

The payload view begins at record `+0x110`. The function captures damping,
updates X velocity, reads `D_800BE9A4` for vertical acceleration, and updates
Y/Z velocity. It reloads the timestep after the velocity stores, captures all
three velocity-times-step displacements, and adds them to both points. Each
endpoint component then becomes `position + (endpoint - position) * blend`.
Weights are not clamped, and values outside the unit interval extrapolate.
The full float32 expression also runs at zero and one, preserving cancellation
and nonfinite behavior rather than substituting an endpoint. Return is always one.

The sole aligned retail pointer is ROM `0x22E794`, VA `0x80089CD4`, slot
**D_80089CB8[7]** in the 42-entry callback table. No direct JAL references
exist. The original `func_1513CFE4` window at `0x1513D034..0x1513D074`
passes the record and consumes the return to force expiry one on zero.
The larger parent remains a C stub and receives no conversion credit here.

## Derived instruction permutation and register roles

The selected ordinary `-O2 -g3` C emits the complete **65-word**, frame-zero
kernel, with both HI16/LO16 bindings to `D_800BE9A4` at offsets zero/four.
**51 fail-closed, non-relocating replacement rows** normalize only FPR roles
and instruction order. No words are inserted or omitted, no profile changes,
and no assembly-body replacement is used.

The new `game_linear_float_dataflow` helper derives a bijection over all
65 input instructions. It labels loads by exact address and memory version,
stores by address and computed value, and arithmetic by its expression tree.
It permits operand exchange for add/multiply but never reassociation. The
fitter reorders the original words and changes only FPR operand/result bits;
opcode, format, address, immediate, GPR, and arithmetic-function bits already
match their corresponding original operations.

The inventory is **25 loads, 12 stores, 22 floating-point operations**, plus
six address/return/control words. The derivation verifies final dataflow,
read/write inventories and return one across **89 layouts**: disjoint storage
and every aligned timestep overlap within all `0x160` record bytes. The
unique return initializer moves from word 23 to word 22 without changing its
value. Relocation positions and bindings remain unchanged.

The entire raw body and both bindings are pinned before fitting. All 260 raw
byte corruptions, three missing/changed binding controls, a changed arithmetic
opcode, and a short instruction stream are rejected. Three actual padder
preimage corruptions fail closed. The derived result must equal every retail
word after relocation masking; the CSV rows are that checked difference set.

Earlier private source screens explain the chosen view: a single scalar
blend field lets IDO cache the factor and emits 62 words. Generic factor and
payload pointers emit 66; explicit position snapshots also emit 66. The
selected mixed record/payload access emits the original 65-operation inventory.
The nearby callback's prior normalization is documented separately in
[Note 1702](1702-dual-point-motion-match-20261024.md).

| Payload | SHA-256 |
| --- | --- |
| Natural before relocation | `372ead169d7ac00cc7e2b1f15ccd5bc63a347bc54bfd4d12c0faf0e860476183` |
| Fitted / retail | `70987c31e8415b3c9469f2d012e7688647d09a6f3325ae27619e9b06fd234b80` |

## Behavioral, caller and fault evidence

All **eight pre-install tests pass in 53.775 seconds** and all **eight
installed tests pass in 61.603 seconds**:

- **7,568 cases per body** cover signed zeros, denormals, small/large finite
  values, damping and vertical acceleration, both points, weight endpoints,
  extrapolation, and eight additional nonfinite model cases. Every word is
  visited. Original and fitted state agree literally. Raw-C comparison permits
  NaN value equivalence rather than specifying a payload; the present corpus
  observes zero payload differences. All other bytes compare exactly.
- **1,584 alias phases per body** execute every aligned timestep overlap,
  three velocity patterns, three blend values and both stack phases. They
  retain the early/late timestep reads and shared displacement capture.
- Native32 SSE O0/O2/O3 with trap UBSan passes **24,576 executions**: 4,096
  direct and 4,096 typed 42-entry-table calls per optimization. Full typed
  `0x160`-byte storage and reserved bytes are checked. All **16 defined wrong-C
  controls** are rejected.
- Two separately compiled timestep controls yield guest counterexamples:
  early capture with the timestep at velocity X, and a third read after the
  position update with the timestep at position X. They emit 65 and 81 words
  respectively and remain private, uninstalled controls.
- **288 phases** execute the actual 16-word return-sensitive caller window,
  including selector zero/seven, signed expiry bytes, stack phases, motion
  patterns, blend values and a fired controlled-zero return. The full parent
  and gameplay are not qualified by this bounded window.
- **185 fired root-access prefixes** preserve complete original/fitted
  private state. Raw access order and fault PCs differ and are not equated.
- **Nine independent GNU links / 45 rebased phases** compare original
  assembly, natural C and the fitted owner at three entry/timestep pairs,
  including HI/LO sign-carry edges. Original and fitted words remain identical.

The expression model does not establish NaN-payload selection, FCSR behavior,
MMIO or hardware execution of raw C. The fitted instructions are literally
retail, including their access order. Native fixtures use ordinary disjoint
storage; timestep-overlap and instruction-fault probes are guest ABI evidence,
not portable C alias/fault semantics. Routine work uses zero Claude calls.

Shared matcher, PC16, guarded-object and protected-data regressions pass
**19 tests in 10.616 seconds**; `make tools-check` passes. The standalone
tools checkout's pre-existing dirty work is preserved; fresh target receipts
belong to the mounted tools checkout.

## Whole-image and production audit

Independent compilation, real padding and linking preserve **60 neighboring
functions** and normalized pools, including the previously matched adjacent
motion callback. Across **6,052 linked functions**, only this target body
changes, with every address fixed. The full ELF is predicted by replacing
the target instructions and updating its named symbol extent from 12 to
260 bytes: **220 changed bytes**, **zero exclusions**. Three inside/outside
target image corruptions are rejected.

All **189,088 protected Game-data bytes / 720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Artifact | SHA-256 |
| --- | --- |
| Frozen predecessor ELF | `29005e48a1f51044750259749b5f066abcc3f85ba0c05cd3d58147a281df94de` |
| Qualified / production owner | `ee17b6ab74083d71fb241bcea9946cf83df282531bab57807afd60d9f453e812` |
| Qualified / production ELF | `b06f9a049b7b71c57625b6bc887eb75be0105090cb401be32323fda84cae9c2b` |
| Production code image | `df3735f9a9043e53626950fc43323ba265b7f6e45248737c1f17df736c2c1a84` |
| Production map, unchanged | `2ab021cc02cab424a5dae0e96a4ed5df1fe5f65ea58964f8e4e04b689771fbeb` |
| Guard registry after 51 rows | `e09c7ad43586de7a32ec698a050fc4661b4602d60e6b9f45becc2ca9441d7d50` |

The registry change triggers the full four-job production rebuild; all
applied preimages pass and linking succeeds. A blank-line correction makes
the installed source exactly equal to the independently qualified text; its
follow-up owner rebuild preserves the same object/image bytes. `make all`
generates the binary and stops only at the expected retail SHA-1 mismatch.
The inherited duplicate `generated_12D630` recipe warning and four unchanged
declaration warnings in this owner remain. No new target warning occurs.

The entire historical guard prefix remains byte-identical plus exactly 51
appended rows. Conversion CSV and Makefile remain byte-identical to their
frozen predecessors.

## Authoritative recount and continuation

| Section | Exact C functions | Address drift | Different |
| --- | ---: | ---: | ---: |
| Total | **4,158 / 5,512 (75.44%)** | 0 | 1,354 |
| Init | **492 / 492 (100.00%)** | 0 | 0 |
| Game | **3,485 / 4,839 (72.02%)** | 0 | 1,354 |
| Debugger | **181 / 181 (100.00%)** | 0 | 0 |

Converted inventory remains 5,512 / 6,046. The active 80% target requires
4,410 exact functions, **252 more**. Continue at ordinary candidate
`func_15191A84`; preserve the seven documented compiler/custom-ABI boundaries.
This checkpoint advances the active goal and does not complete it.

Reproduce under prepared WSL from the consumer root:

```sh
python3 -m tools.experiments.game_blended_dual_point_motion_match
python3 -m unittest tools.tests.test_game_blended_dual_point_motion_match -v
make -C conker -j4 build/conker.us.elf
make -C conker all
```

## Graph retention

The frozen graph has **58,613 nodes / 112,376 links / 5,119 communities**,
SHA-256 `a724cc8ed4f9a06ff49ba68b6cd484164659a77d76b4a85e0c609571e4152f43`.
The standard reduced update extracts eight uncached paths but proposes only
24,820 nodes and correctly refuses to overwrite the retained graph. Its
corpus warning retains 31,816 nodes from 3,754 still-present files outside
the reduced scan. An explicit eight-path refresh with `force=False` produces
**58,622 nodes / 112,384 links / 5,164 communities**, retaining **58,610 /
58,613** prior IDs with **zero removals outside changed paths**. Three
line-derived Update Log IDs relocate; twelve IDs are added, including eight
Note 2087 nodes and one additional reference node.

Qualified graph SHA-256:
`7112aea64df91f9143b068df755a8108bcd8e38ed6704e24c4f5b970c72e3d20`.
This is a scoped AST refresh with zero semantic LLM calls, not a fresh
full-corpus extraction. A final one-path note refresh checks stabilization.
