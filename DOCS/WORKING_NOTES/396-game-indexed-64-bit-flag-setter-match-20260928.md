# Game indexed 64-bit flag setter byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_1501D258` in
`conker/src/game/generated_49D30.c` with its semantic Game routine. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function accepts an array index and bit index. When global byte
`D_800C3670` is zero, it sets that bit in the indexed 64-bit row:

```c
D_800C3A60[index] |= 1LL << bit;
```

When `D_800C3670` is nonzero, it returns without changing the bitset. The
signed bit argument reproduces retail's sign extension into the second
64-bit `__ll_lshift` argument.

## Compiler result

IDO emits the complete retail routine directly from the typed expression. It
reproduces the 24-byte frame, argument spills, enable gate and delay slot,
`__ll_lshift` calling convention, eight-byte row indexing, paired loads and
OR operations, and high/low word stores. No expected-word guards are needed.

## Verification

- The focused `generated_49D30.c.o` build passed.
- Focused object disassembly matches all 27 retail instruction words.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_1501D258` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `d290ae23b10b11613cb5737ff78c3b7a462bf6cecf9b78b88af3c5501959bedb`.
- Fresh matcher totals are `2,898 / 5,466 (53.02%)` overall and
  `2,324 / 4,790 (48.52%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 26-word `func_15022754`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
