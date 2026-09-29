# Game packed-byte submission wrapper byte match

Date: 2026-09-29

## Scope

This pass completed `func_150721A4` in `conker/src/game_981E0.c`. Its tracked
retail slot spans 17 words and 68 bytes at `0x150721A4..0x150721E8`.

## Recovered behavior

The existing C body passes the current object in `D_800D154C` to
`func_1506160C`. It extracts bits `16..23`, `0..7`, and `8..15` from the packed
word in `D_800D1580` as the next three arguments and supplies zero as the
fifth argument.

IDO emits the correct computation but stages the packed value and two masked
bytes through three redundant moves, producing a 20-word body. Retail keeps
the packed value in `v1`, extracts the middle and high bytes through `t6` and
`t7`, masks directly into the call registers, and computes the low byte in
the call delay slot.

Ordinary-object padding previously selected an overflow trampoline before it
could apply guarded omissions. `pad_c_object.py` now counts inserted and
omitted words before that decision and honors omission while emitting a body.
A focused unit test proves that a guarded omission contracts an otherwise
oversized ordinary function without creating an overflow symbol.

Three fail-closed omission guards remove only the redundant moves. Nine
additional expected-word guards normalize the equivalent register lifetimes
and schedule while preserving both global relocations and the call relocation.

## Verification

- The focused and normal padded objects reproduce all 17 retail instructions.
- The focused ordinary-object contraction unit test passes.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt every padded object and
  linked the complete ELF and binary successfully.
- The matcher classifies the function byte-exact. Direct comparison uses the
  decompressed US Game mapping (`0x15000000` to file offset `0x2D4B0`), not
  the assembly listing comment, and passes all 68 bytes. Both spans share
  SHA-256
  `23364d3eb1884f0df6cef21145f9029869c884555332de80fb722d6d2d36a2a0`.
- Fresh matcher totals are `2,963 / 5,465 (54.22%)` overall and
  `2,389 / 4,789 (49.89%)` in Game, with one address-drift row.

## Resume boundary

Resume ordinary Game matching with 31-word `func_1515B994`, at 28 real
differences. Keep `func_151A8584`/`func_151A85D4`, `func_1506EF5C`,
`func_1507A4D4`, `guMtxIdentF`, `func_150F1684`, and `func_15155FD4` parked at
their documented compiler boundaries. Keep the tied Init SDK cache routines
in their ownership lane and `func_10012588` parked on address drift.
