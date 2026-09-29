# Game packed indexed-byte updater byte match

Date: 2026-09-29

## Scope and behavior

`func_1506EF5C` in `conker/src/game_981E0.c` spans 22 words and 88 bytes at
`0x1506EF5C..0x1506EFB4`. It reads the packed global `D_800D1580` and updates
the active object referenced by `D_800D154C`:

- Field `0x282` receives the halfword sentinel `0xFFFF`.
- Byte `0x276` receives mode value five.
- Bits `16..23` select a two-byte slot beginning at object offset `0x284`.
- The selected bytes receive bits `8..15` and `0..7` of the packed value.

Retail reloads `D_800D154C` before each of the four stores. Expressing the two
indexed writes directly through repeated global reads, instead of caching one
object pointer, restores that behavior and the complete 22-word extent.

## Compiler shape

The semantic C produces the retail instruction skeleton, store ordering,
repeated root loads, packed shifts/masks, byte stride, and leaf return. IDO
chooses a different register assignment for every non-epilogue word and emits
the halfword sentinel with signed `addiu` instead of retail's equivalent
zero-based `ori`.

Twenty expected-word guards normalize those register lifetimes, instruction
schedule, and constant encoding. Four guards retain explicit relocation checks
for `D_800D154C` and `D_800D1580`. The final `jr ra` and delay-slot `nop` emit
directly from C, and no instruction is inserted or omitted.

## Verification

- The focused `game_981E0` object builds with all 22 retail words.
- The complete ELF relink passes.
- Direct linked comparison reports zero differences across all 88 bytes.
- Both spans share SHA-256
  `bb1533bcd2675ab5ab801d3148a589be179a3ce3d5e4a339f0def4f69c842d9a`.
- The authoritative matcher omits `func_1506EF5C` from its non-exact list and
  reports `2,987 / 5,465 (54.66%)` overall and `2,412 / 4,789 (50.37%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next small Game row. `guMtxIdentF` remains a canonical SDK
compiler-profile boundary, while `func_15155FD4` is the next 21-word Game
candidate at 19 real differences.
