# Game randomized burst direct match

Date: 2026-11-14. `func_1517AA20` is recovered as semantic C in
`conker/src/game/generated_1A7260.c`. All **87 words / 348 bytes** match
retail directly under the unchanged O2/g3 profile, with **zero guards**.
The routine occupies `0x1517AA20..0x1517AB7C`, ROM
`0x1A7ED0..0x1A802C`, with its original **0x50-byte frame**.

## Recovered behavior and ABI

The five arguments are size, X/Y/Z position and count. Size enters F12;
X/Y/Z enter A1/A2/A3, and count is the fifth stack argument. Sizes below
12 return immediately. Otherwise the routine truncates `size * 8` for an
unsigned remainder divisor, halves size, narrows Y to signed 16 bits and
emits `count` pieces when count is positive.

Each iteration consumes four random draws in their original order. The
first two supply X/Z offsets in `[-32,31]`. The third supplies the size
increment through unsigned remainder and a four-bit shift. The fourth's
low bit selects the variant. X is narrowed to signed 16 bits; Z addition
preserves 32-bit wraparound. Explicit unsigned additions avoid introducing
signed-overflow undefined behavior into the recovered C.

Splitting both mask operations from the subsequent subtractions reproduces
the retail random-call delay slots and register lifetimes directly. No
instruction replacements, assembly snippets, compiler-profile changes,
header changes or guard rows are introduced.

`func_150ADA20` retains its existing signed 32-bit return declaration; the
remainder expression explicitly converts that payload to unsigned. The
same-owner emitter `func_1517A644` gains its measured float-first signature,
including the byte variant and two signed 16-bit register coordinates.
Retail reads the variant with LBU and coordinates with LH. Its fifth
coordinate is passed as a 32-bit word and consumed through its low half.

**The emitter is still an unfinished zero-return placeholder.** Typing its
interface adds four ordinary argument-home stores, expanding the stub from
three to seven words. That entire change is included in the linked audit;
the emitter receives no matching credit. The other nine owner functions
and normalized pools remain unchanged.

## Focused qualification

- **832 guest cases** cover the size threshold, zero/negative/positive
  counts, four random patterns, all six-bit offset values, coordinate
  narrowing and wraparound, two stack phases and poisoned incoming homes.
  Helper hooks clobber volatile GPR/FPR and HI/LO state. Saved registers
  and the original stack pointer are preserved.
- **36 cases through the authentic caller window**
  `0x1518384C..0x15183884` validate float-to-coordinate truncation,
  fifth-argument placement and continuation after the call.
- **25 fired instruction-access boundaries** preserve the complete modeled
  register, FPR, memory, trace and helper-call state across retail, raw C
  and padded streams.
- **448 native 32-bit cases per O0/O2/O3 profile** pass with UBSan.
  Five effective native source controls reject wrong offset masking,
  size scaling, variant selection, Y coordinate or loop bound. Five guest
  instruction controls additionally check signed X submission.
- Both **complete-owner padders pass**, preserving all eleven proposed
  owner functions. Twelve independent GNU links across four code layouts
  compare the target's complete body and all five named call bindings.

The finite conversion domain includes sizes through `268435440.0f`, with
`size * 8` below signed 32-bit overflow. Four original instructions are
unreached in that domain: the divide-by-zero break and unsigned-float
sign-correction arm. **83 / 87 instructions execute**; all 87 match retail
statically. Nonfinite/FCSR behavior and invalid float-to-int conversions
are not claimed. Random and emitter implementations are modeled helper
boundaries; full handwritten 64-bit RNG, emitter lifecycle, parent lifecycle
and gameplay acceptance remain separate.

Fresh pre-install suite: **15.410 seconds**. Fresh installed suite:
**17.442 seconds**, with no skips. `make tools-check` and scoped whitespace
checks pass. A fresh installed suite using the sibling tools dependencies
passes in **31.859 seconds**. The overlay writes only to the consumer's
ignored build directory. Sibling HEAD remains
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; all 2,439 pre-existing dirty
paths are preserved, with before/after status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.

## Production and full-image evidence

The independent shadow executes the three actual Make object commands.
The production build produces the identical ELF, SHA-256:
`543b56ff67ccc293f565573e9f1ff86a5577947af8fa3fab4806a9bb6db1b705`.

Strict whole-image comparison accounts for **279 changed bytes**, with
zero exclusions and no metadata groups. Only the burst body and typed
emitter placeholder body/extents change. All **6,051 function addresses**
are fixed. Only `generated_1A7260.c.o` changes among **698 objects**, in its
text/relocation/symbol/string sections. All **189,088 protected data bytes**,
**82 headers**, existing guards and conversion CSV rows are unchanged;
**789 immutable input fingerprints** pass.

Actual recount: total **4,479 / 5,515 (81.21%)**, Game
**3,806 / 4,842 (78.60%)**, Init **492 / 492**, Debugger **181 / 181**;
zero drift and **1,036** different C functions. This is **one new exact C
function**. Converted function/byte percentages stay unchanged. At this
denominator, **209** additional matches reach 85%.

The scoped Graphify AST refresh covers this owner and five tools files.
All **60,251** previous node IDs are retained; **60,283 nodes / 113,568
links** result, with zero lost nodes. This is not a full-corpus extraction.
Private reports, sources and frozen inputs remain under
`conker/build/game-randomized-burst-1517aa20-screen/`.

## Resume boundary

Next target: **`func_1517A644`**, the same-owner **130-word** emitter with
its original **0x60-byte frame**. Recover allocation, initialization and
failure paths using the now-qualified burst interface; its typed stub is
not a recovery. Keep the wider 85% goal open.

`64CBFDOGL` has no host source checkout at the available path, so no host
source adoption, build or runtime verification is claimed. Frozen Release
artifacts are untouched. Bank the qualification tools before the consumer
source, aggregate README rows, note and concise indexes; do not push.
