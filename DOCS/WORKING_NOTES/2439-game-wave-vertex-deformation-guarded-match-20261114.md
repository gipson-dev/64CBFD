# Game wave vertex deformation guarded match

Date: 2026-11-14. `func_15179DB0` is recovered in
`conker/src/game/generated_1A7260.c`. The complete **140-word / 560-byte**
routine occupies `0x15179DB0..0x15179FE0`, ROM `0x1A7260..0x1A7490`.
**68 words emit directly from C; 72 expected-word guards restore the retail
private frame, pointer-array homes, scheduling and integer temporary roles.**
Raw C uses a **0x90-byte frame**; the qualified guarded body restores the
original **0x80-byte frame**.

All ten neighboring functions and normalized pools remain unchanged. The
owner now has **11 / 11 retail-matching C routines**, with no zero-return
placeholders. Its obsolete placeholder heading is replaced by a recovered
routines heading. Converted function/byte totals are unchanged.

## Recovered behavior and ABI

The routine has a void interface with one unsigned-byte table index. The
only direct JAL is at ROM `0x1B1410`, inside `func_15183D28`; that caller
already declares the correct interface and supplies slots 8 and 9. There
are no aligned literal pointers to the routine.

A 20-byte resource record supplies two vertex pointers, both captured
before the first helper. The second bank is processed first, then the
first bank. A separate 0x38-byte configuration row supplies two phase-step
values at 0x18/0x1C, two phases at 0x20/0x24 and amplitude at 0x28.
The seven retail edge indices are **4, 9, 13, 14, 15, 17 and 19**.
`D_800A7218` is snapshotted once as the degree-to-radian multiplier.

For each bank the routine calls `sinf(phase * factor)`, reloads amplitude,
truncates the product to signed 32 bits, then narrows to signed 16 bits.
It writes this displacement to the X coordinates of vertices 2 and 3.
The edge value is the negative of the arithmetic-right-shifted signed
displacement, preserving the negative-odd rounding behavior. Seven indexed
vertices receive that edge value; vertex 6 then receives edge + 18, and
vertex 8 receives edge - 18. Later stores retain their overwrite order when
indices repeat or select center/offset vertices.

The current phase adds its current step with single-precision rounding.
When the updated phase is at least 360, exactly one subtraction of 360
occurs. A value such as 1080 is not fully reduced in one call. The helper
can change live amplitude, phases, steps or indices; the snapshotted bank
pointers and factor stay fixed across both iterations.

## Qualified normalization

The normalization pins the entire raw body and all fifteen named bindings.
Raw SHA-256:
`a54e86df64bbb89c3cb903f2d95b71f26c75b3156690c32d91b934c188507894`.
All 140 individual raw-word corruption controls and one actual JAL-binding
corruption control reject altered input. All fifteen bindings survive,
including the relocated index-table references and the `sinf` call.

Frame allocation/deallocation move from 0x90 to 0x80, and the incoming
argument remains at the same absolute caller-home address. The three private
two-element pointer arrays move from SP+0x78/+0x80/+0x88 to retail
SP+0x5C/+0x64/+0x6C. Saved S0..S5/RA and paired F20/F22 offsets remain fixed;
outgoing homes stay at SP+0..0x0F. The arrays never escape to the helper,
which takes a float value. Unused compiler stack space is removed without
overlapping the arrays, saved state or outgoing homes.

One independent index-tail address calculation moves before integer
conversion. Closed GPR-role substitutions preserve every opcode, arithmetic
operation, memory width, field offset and branch target. No instruction
slots are inserted or omitted, and no profile/shared-header changes occur.
An independent symbolic check proves the **67-instruction post-sine block**
has the same **35 ordered memory events**, alias-aware memory expression and
live values. Its effective control changes an edge offset and must fail.

Raw C's larger private frame and temporary state differ from retail.
Public memory/provider agreement is kept separate from exact retail/guarded
machine-state and fired-boundary agreement. Input vertex objects are distinct
from the unescaped private frame; the three tested bank-overlap layouts do
not authorize arbitrary pointers into a callee's private stack.

## Focused validation

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_wave_vertices_15179db0_match -v
```

- **2,672 valid guest cases** cover signed displacement/narrowing, zero and
  negative amplitude, negative-odd halving, single-wrap boundaries, all 256
  argument/index byte values, repeated indices, separate/identical/overlapping
  banks, provider mutations, incoming-home mutation and two stack phases.
  Extended table/index addresses are guest-only synthetic mappings.
- **Eight prefixes** stop immediately before an invalid float-to-integer
  conversion, checking prior memory effects and helper observations. Native
  cases exclude these inputs. Hardware indefinite results and FCSR exception
  behavior after that boundary are not claimed.
- **24 authentic caller-window cases** execute the original seven words
  `0x15183F4C..0x15183F68`, including the signed flag gate, unsigned-byte
  argument mask, JAL and its delay slot. Both real slots and skipped calls
  reach their measured continuations; the full caller is not requalified here.
- **216 fired memory boundaries** preserve complete state between retail
  and guarded streams. Four effective instruction controls reject wrong bank
  selection, wrap bound, seventh index or positive edge offset.
- **84 connected cases** execute both iterations together with the original
  complete **104-word `sinf` body**, freshly verified in the production ELF
  against the ROM. Its results agree with the independent single-precision
  reference. This does not claim physical hardware/FCSR acceptance.
- **742 native 32-bit cases per O0/O2/O3 profile**, with UBSan, check all
  **1,536 vertex backing bytes**, 56 configuration bytes, 20 resource bytes,
  index/factor state and provider observations. Six effective source controls
  reject wrong bank, center vertex, negative halving, index count, wrap
  equality or factor reload. Native table slots are 8 and 9; extended guest
  indices and invalid conversions are excluded.
- Both **complete-owner padders** agree on all eleven routines and pools.
  Twelve GNU links across four independently moved code/data layouts preserve
  all 140 words and symbolic address relationships.

All **140 words execute** in the valid corpus. The pre-install integrated
suite passes in **49.546 seconds**. The fresh installed suite passes in **48.129 seconds**, and the
sibling-dependency overlay passes in **56.398 seconds**, with no skips. `make tools-check` and scoped
whitespace checks pass. Provider-mutation fixtures are modeled boundaries;
the separate connected cases execute the real sine helper.

The overlay writes only under the consumer's ignored build directory.
Sibling HEAD stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all **2,439** dirty
paths; before/after status SHA-256 is `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.

## Production audit and progress

The shadow executes the three actual Make object commands. Production ELF
matches that prediction exactly, SHA-256:
`d26eb6ae82ab3852d0b67c1e0fdf891bc5d89cdc58f97082993743afd8e8e592`.

The **437-byte** strict delta contains this body/extent and one explicitly
reconstructed closed symbol/string permutation involving `D_800A7210`,
`D_80090D34` and `D_8008FE2C`. All named definitions remain identical except
the declared target extent. There are **zero exclusions**. All **6,051
function addresses** stay fixed. Only the target body and its owner object
change among **698 objects**, in text/relocation/symbol/string sections.
All **189,088 protected data bytes**, **82 headers**, existing guards and
conversion CSV rows stay fixed. Exactly 72 guard rows append, and
**794 immutable input fingerprints** pass.

Actual recount: total **4,484 / 5,515 (81.31%)**, Game **3,811 / 4,842
(78.71%)**, Init **492 / 492**, Debugger **181 / 181**; zero drift and
**1,031** different C functions. This is one new exact C function. **204**
more matches reach 85% at the current denominator.

Scoped Graphify AST refresh covers the owner and six tools files, retaining
all **60,476** old node IDs: **60,523 nodes / 113,955 links**,
with zero lost nodes. This is not a full-corpus extraction. Private evidence
is under `conker/build/game-wave-vertices-15179db0-screen/`.

## Resume boundary

Next: **`func_15183290`**, the remaining stub in the related caller owner
`generated_1B0740.c`: **392 words**, original **0x68-byte frame**, spanning
`0x15183290..0x151838B0`. Recover its parameter widths, resource setup and
provider sequencing before another adoption. All eleven functions in
`generated_1A7260.c` are now recovered and verified.

Tools commit `dbd3367` banks the six qualification files before the consumer
source, 72 guards, README aggregate rows, this note and concise indexes.
Keep the 85% goal
active; do not push. No host source checkout is available under `64CBFDOGL`,
so there is no host adoption/runtime claim. Release remains frozen.
