# Game floor-threshold state trigger byte match

Date: 2026-09-28

## Scope

This pass completed `func_1506D6B4` in `conker/src/game_981E0.c`. The retail
slot spans 38 words and 152 bytes at `0x1506D6B4..0x1506D748`.

## Recovered behavior

The routine reads the active actor's floor value at offset `0x118`. It returns
when that value equals sentinel `D_80099D4C` or lies below the actor's signed
threshold at offset `0x1A6`. Otherwise it selects packed state byte `0x29` for
health below two or `0x2C` for health of at least two.

The selected byte becomes the high byte of `D_800D1580`; the previous low 16
bits are retained and bits 16 through 23 are cleared. The routine then calls
`func_1506D584` to process the selected state.

Expressing the comparisons as early returns and the health selection as a
conditional expression reproduces retail's frame, branch-likely exits, global
address lifetime, two-arm selector branch, packed update, call, and delay-slot
store. Thirty-two words emit directly from semantic C. Six guarded words
normalize one commutative FP comparison operand order and the closed temporary
cycle used by the final load, shift, mask, merge, and store.

## Verification

- The focused `game_981E0.c.o` build passed under the existing `-O2 -g3`
  profile; all 38 words match retail after the six guarded allocation words.
- The full `wsl make NON_MATCHING=1 -j1` rebuild and relink passed from
  `conker`; the shared patch-table dependency regenerated all padded objects.
- `match_progress.py` classifies `func_1506D6B4` as byte-exact.
- The linked ELF and retail 152-byte spans share SHA-256
  `690e50073ee7d0d285273ab36186c7fea022fabf86b1a9ce25c9f2ee82b69a9c`.
- Fresh matcher totals are `2,931 / 5,466 (53.62%)` overall and
  `2,357 / 4,790 (49.21%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_15080784`, currently at
27 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
