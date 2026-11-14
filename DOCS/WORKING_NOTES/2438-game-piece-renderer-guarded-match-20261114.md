# Game piece renderer guarded match

Date: 2026-11-14. `func_1517A3A0` is recovered in
`conker/src/game/generated_1A7260.c`. Its complete **169-word / 676-byte**
body occupies `0x1517A3A0..0x1517A644`, ROM `0x1A7850..0x1A7AF4`, with
the original **0x58-byte frame**. **131 words emit directly from C;
38 expected-word guards restore alpha-cache addressing and tail scheduling.**
The first 109 instructions match directly. All ten other owner functions
and normalized pools remain unchanged.

## Recovered renderer and interface

The routine takes a display-list cursor, the existing 184-byte piece record,
and a signed-halfword view index, and returns the advanced cursor. Header
byte zero is the descriptor category; the record's two matrix banks start
at offset 0x10. The existing shared record layout is preserved.

Categories 12 and 89 bypass the view test. Other categories pass the selected
view matrix, float-converted position and four camera globals to
`func_1510AEE0`. Inspecting that complete helper confirms its final two
arguments are optional float-output pointers; both are null here. A nonzero
result rejects the draw. Rejected category 8 records set the view's high
retirement bit only if the corresponding low bit was already set. Other
rejected categories return the original cursor without emitting a packet.

The draw path sets the low view bit except for category 9. It calls the
already-matched variant-state helper, builds the selected matrix from the
three signed angles, repeated scale and position, then emits `gSPMatrix`.
The current matrix bank is reloaded after the transform helper. If opacity
differs from the signed-halfword cache, the routine emits pipe sync and a
black primitive color with that alpha, then updates the cache. A zero local
sync byte is passed to the material-state helper. Categories 8/9 select
`0x5049D8`; other categories use `0x504240`. The mode combines
`D_800D2C9C | 0x80000 | 0x2CA0`. A final display-list call targets
`D_8008CDF0`, and its eight bytes advance the returned cursor.

Portable native qualification uses the actual four-view domain 0..3.
Ten additional guest-only signed-view cases check the emitted N64 shifts'
masked counts and address arithmetic; they are not claims about portable C
shifts outside the valid view range or out-of-array native pointers.

## Guard derivation and named bindings

The compiler reuses one alpha-cache address through LUI/ADDIU/LH/SH. Retail
uses two direct symbolic LUI+access pairs. The normalization splits only that
address materialization, reschedules the matrix packet and alpha comparison,
preserves the comparison branch's target, relocates the private sync byte
from SP+0x57 to SP+0x43, and closes the dead temporary-register substitutions
in the material mode and terminal display-list command. Frame, saved S0/S1/RA,
incoming homes, all calls and all C-level reads/writes remain represented.
There are no inserted or omitted instruction slots, profile changes or
shared-header changes. The record, command buffer and BSS cache are disjoint.

The raw 169-word body is pinned by SHA-256:
`27ceee2eaaddc6b7785ebda289d4ee96e80cc7ce584ff471c2603d26f0e1218c`.
All 169 individual word-corruption controls and one actual JAL-binding
corruption control reject altered input. Twenty-four raw named bindings
become 26 after splitting the cache address pairs. The already-defined
`D_800D35E4` is the named alias of retail's `D_800D35E0 + 4`; independent
data-address rebases verify this equivalence rather than assuming one link
address is sufficient. Expected and replacement relocation fields are pinned.

Raw C has a different private sync address and a reordered ordinary-RAM
access sequence. Its public packet/provider/final-memory agreement is kept
separate from retail/guarded full-state and fault-boundary identity.

## Focused validation

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_piece_renderer_1517a3a0_match -v
```

- **3,082 guest cases** cover all category, packed-retirement and opacity
  byte values, culling outcomes, both matrix banks, matching/missing alpha
  cache states, signed coordinates/angles, scale payloads including signed
  zero and quiet NaN, two stack phases, volatile-register and outgoing-home
  clobbers, record/global mutations and guest-only incoming-home mutation.
- **32 real dispatcher-window cases** qualify all four callback slots:
  descriptors 8, 9, 12 and 89 in `D_8008B4A8`, stride 0x34. The aligned ROM
  pointers are `0x230110`, `0x230144`, `0x2301E0` and `0x231184`; there are
  no direct JAL callers. The original eight-word window
  `0x15167898..0x151678B8` forwards cursor/record/signed view through JALR,
  saves the next-record link in its delay slot and reaches the continuation.
  This is a call-boundary check, not complete dispatcher acceptance.
- **134 fired memory boundaries** preserve complete modeled state between
  retail and guarded code. Five effective instruction controls reject wrong
  bypass category, retirement nibble, matrix opcode, alpha field or terminal
  opcode. The retirement control distinguishes required 0x02 -> 0x22 from
  the incorrect 0x02 -> 0x12 update.
- **1,536 native 32-bit cases per O0/O2/O3**, with UBSan, compare all 184
  canonical record bytes, 128 command words, provider arguments/observations,
  globals and the returned cursor. Five effective source controls reject the
  wrong category, retirement shift, matrix bank, alpha field or material
  mode. Native cases exclude incoming-home mutation and invalid view shifts.
- Both **complete-owner padders** preserve all eleven functions and pools.
  Twelve GNU links across four independently moved code/data layouts retain
  the complete target and symbolic address relationships.

**168 / 169 words execute**; the unreachable address-load word at index 150
is a static byte match. Fresh pre-install integrated suite passes in
**27.732 seconds**. The fresh installed suite passes in **26.682 seconds**;
the sibling-dependency overlay suite passes in **33.321 seconds**, with no
skips. Culling, matrix generation, variant and material helpers are modeled
provider boundaries here; this does not claim
complete graphics hardware, full provider-chain or gameplay acceptance.
`make tools-check` and scoped whitespace checks pass.

The overlay writes only inside the consumer's ignored build directory and
falls back to mounted dependencies for absent sibling modules. Sibling HEAD
stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, preserving all **2,439** dirty paths;
before/after status SHA-256 is `a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.

## Whole-image audit and progress

The shadow executes the three actual Make object commands. The production
ELF is identical to that prediction, SHA-256:
`48e306d9d3efc311e83b4dcdfa74effe217d76f1915fcc33343ea6b028952d55`.

Strict delta is **599 bytes**, with zero exclusions: target body/extent plus
one exactly reconstructed closed permutation of symbol/string entries
`func_151C71A0`, `func_151BD7F4` and `D_80098D10`. All named definitions are
preserved, apart from the declared target extent. There is no blanket
metadata exclusion. All **6,051 function addresses** stay fixed, and only
the target body differs. Only `generated_1A7260.c.o` changes among **698
objects**, in text/relocation/symbol/string sections. All **189,088 protected
data bytes**, **82 headers**, prior guard rows and conversion CSV rows are
unchanged. Exactly **38** guards append, and **795 immutable fingerprints**
pass, including the complete view-test helper and dispatcher assembly.

Actual recount: total **4,483 / 5,515 (81.29%)**, Game **3,810 / 4,842
(78.69%)**, Init **492 / 492**, Debugger **181 / 181**; zero drift and
**1,032** different C functions. One new exact C function is credited;
converted function/byte totals are unchanged. **205** further matches reach
85% at the current denominator.

Scoped Graphify AST refresh covers the owner and five tools files, retaining
all **60,433** old node IDs: **60,469 nodes / 113,860 links**,
with zero lost nodes. This is not a full-corpus extraction. Private evidence
and frozen inputs are under `conker/build/game-piece-renderer-1517a3a0-screen/`.

## Resume boundary

Next: **`func_15179DB0`**, the owner's last stub: **140 words**, original
**0x80-byte frame**, `0x15179DB0..0x15179FE0`. Recover its indexed source
tables, two-element trigonometric update and signed vertex narrowing before
credit. Ten of the owner's eleven functions now match retail.

Tools commit `bc583c8` banks the five qualification files before the consumer
source, 38 guards, README aggregate rows, this note and concise indexes.
Keep the 85% goal active;
do not push. The available `64CBFDOGL` path has no host source checkout.
There is no host adoption/runtime claim, and Release remains frozen.
