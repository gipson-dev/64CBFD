# Game burst-piece factory guarded match

Date: 2026-11-14. `func_1517A644` is now recovered in
`conker/src/game/generated_1A7260.c`. Its complete **130-word / 520-byte**
routine occupies `0x1517A644..0x1517A84C`, ROM `0x1A7AF4..0x1A7CFC`,
with the original **0x60-byte frame**. **129 words emit directly from C;
one expected-word guard preserves the original low-half stack load.**

This replaces the typed placeholder documented in
[Note 2434](2434-game-randomized-burst-direct-match-20261114.md). The
matched 87-word burst caller remains unchanged. All ten other owner
functions, including the settle/fade callback, and all normalized pools
are preserved.

## Recovered routine and record view

The factory truncates size to a signed 32-bit range. A zero range returns
without allocation. Otherwise it requests category 9, group 0, 184 bytes,
mode 1, priority 255 and flag 1 from `func_15167A68`; allocation failure
returns without a floor query or random draws.

On success, `func_1510E82C` receives the signed low halves of X/Y/Z, with Y
also supplied as its second height input. The returned floor plus three
sets both the record's floor and current Y. The factory writes X/Z, pitch
90, random yaw, zero roll and horizontal speeds, the variant byte, random
scale, vertical speed, three random signed-byte spins, timer zero and
opacity 255. Five random draws occur in their original order.

The shared record view now names `variant` at `0x9F` and `scale` at `0xA8`,
while retaining unknown bytes at `0xAC..0xAF` and `0xB4..0xB7`. Its size is
184 bytes. These type changes do not change the existing callback's code.
Floor/velocity conversion explicitly truncates through signed 32 bits
before signed 16-bit narrowing, preserving wrapping without relying on
an out-of-range direct float-to-short conversion.

## Single low-half load guard

The unchanged 32-bit fifth-argument interface preserves the matched caller.
At word 58 / byte `0xE8`, IDO emits `lw t5,0x70(sp)` before storing T5's low
half to record Z. Retail instead uses `lh t5,0x72(sp)`. The sole guard pins
`0x8FAD0070 -> 0x87AD0072`, with no relocation on that instruction.

The loaded value is consumed by the signed-halfword store at word 61.
Its extra high bits are dead; T5 is overwritten before its next read.
Both streams require an ordinary mapped four-byte o32 incoming argument
home. This is a measured load-width normalization, not a claim that the
raw and retail memory-access widths are identical. Raw register/trace
state inside that lifetime and arbitrary per-byte memory-fault equivalence
are not claimed.

The normalizer pins the complete raw body SHA-256
`afc60ae7eb1e5888a8387fdd138857ec6b6c5c38948892dc914ab6b20281dbb5`
and all eleven named bindings. All 130 individual raw-word corruption
controls and one binding corruption control reject changed input. No
operations, compiler flags, headers or existing guard rows change.

## Qualification

The integrated command is:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_burst_piece_1517a644_match -v
```

- **880 guest cases** cover zero, fractional, positive and negative size;
  allocation success/failure; signed coordinate narrowing and poisoned
  upper argument bits; three random patterns; two stack phases; constant
  changes and incoming-home mutations across helper calls. Record bytes,
  helper arguments/observations and preserved registers match an
  independent model.
- **108 connected cases** execute the real matched burst loop and this
  factory together, including zero/negative count, the size gate, two-piece
  loops and allocation failure. This checks the caller's saved loop and
  floating-register lifetimes across the recovered callee.
- **52 fired instruction-access boundaries** compare complete modeled
  retail/guarded state. Raw C preserves public memory, helper calls and
  observations at those same boundaries with the required argument home
  mapped; its private load-width difference remains explicit.
- **304 native 32-bit cases per O0/O2/O3 profile** pass with UBSan. All 184
  record bytes are checked after serialization to N64 byte order, together
  with helper observations. Six effective controls reject wrong category,
  allocation size, pitch, yaw modulus, floor offset or timer. Guest-only
  incoming-home mutations are excluded from portable native claims.
- Both **complete-owner padders** pass, with twelve GNU links across four
  code layouts. All 130 guarded words and eleven bindings match retail.
  A full retail census finds one direct JAL at ROM `0x1A7FE4` and no literal
  pointers to this factory.

**127 / 130 instructions execute** in the valid finite conversion corpus;
the three original divide-by-zero breaks are unreachable after the saved
nonzero-range gate. All 130 words match statically. Nonfinite/FCSR and
invalid float-to-int behavior, full handwritten 64-bit RNG execution,
complete allocator/ground-provider lifecycle and gameplay acceptance
remain separate. Helper effects are modeled.

Fresh pre-install suite: **18.234 seconds**. Fresh installed suite:
**25.839 seconds**, no skips. `make tools-check` and whitespace checks pass.
A fresh installed suite using sibling tools dependencies passes in
**25.148 seconds**. Its overlay writes only to the consumer's ignored build
directory. Sibling HEAD stays
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with all **2,439** pre-existing
dirty paths preserved. Before/after status SHA-256 is
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`.

## Production image and progress

The independent shadow executes the three actual Make object commands.
Production ELF matches it exactly, SHA-256:
`4a59ed1c77fcd34c456a1fbd0ecd25e3c7fa1284164cf283b6602cb2d8d336be`.

The strict whole-image audit accounts for **438 changed bytes**, with zero
exclusions. Only this factory's body and symbol extent change. It also
accounts exactly for the symbol/string-table serialization of
`func_151420F8`, `func_1518EB10` and `D_80098D1C` changing from that order
to `D_80098D1C`, `func_151420F8`, `func_1518EB10`. Their named definitions
and values do not change; this is not an unexplained metadata exclusion.

All **6,051 function addresses** are fixed. Only `generated_1A7260.c.o`
changes among **698 objects**, in text/relocation/symbol/string sections.
All **189,088 protected data bytes**, **82 headers**, previous guards and
conversion CSV rows are preserved. Exactly one guard row is appended;
**788 immutable input fingerprints** pass.

Actual recount: total **4,480 / 5,515 (81.23%)**, Game
**3,807 / 4,842 (78.62%)**, Init **492 / 492**, Debugger **181 / 181**;
zero drift and **1,035** different C functions. This is **one new exact C
function**, with converted function/byte totals unchanged. **208** further
matches reach the 85% goal at the current denominator.

The scoped Graphify refresh covers this owner and six tools files. All
**60,289** previous node IDs are retained; **60,332 nodes / 113,642 links**
result, with no lost nodes. This is not a full-corpus extraction. Frozen
inputs, receipts and private fixtures remain in
`conker/build/game-burst-piece-1517a644-screen/`.

## Resume boundary

Next: **`func_1517A1EC`**, a same-owner **106-word** callback with the normal
**0x18-byte frame**. Its retail body updates position/spin and lifetime,
fades opacity, and conditionally retires the record. Recover its extra
record fields and state transitions before claiming another match.

Bank tools before the consumer source, one guard, README aggregate rows,
note and concise indexes. Keep the 85% goal active; do not push.
`64CBFDOGL` has no host source checkout at the available path, so no host
build/runtime adoption is claimed. Frozen Release artifacts are untouched.
