# Game current-record vector copy byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_1503A60C` in
`conker/src/game/generated_64120.c` with its semantic Game routine. The retail
slot spans 27 words and 108 bytes.

## Recovered behavior

The function selects the current `0x32C`-byte record using byte index
`D_800C3E78`. It reads the record's pointer at offset `0x1D4`, advances that
pointer by `0x40`, and writes three floating-point components at destination
offsets `0x30`, `0x34`, and `0x38`.

The corresponding source values come from current-record offsets `0x174`,
`0x18`, and `0x178`.

## Compiler result

The three source expressions intentionally repeat the global index and record
address calculation. Each preceding store uses an indirect destination
pointer that may alias global data, so IDO preserves retail's reload of
`D_800C3E78` and repeated multiply by `0x32C` before the next component.

The compiler emits all 27 retail words directly, including the retained base
address, index-byte address, record-size constant, destination pointer, three
multiply/address sequences, floating loads and stores, and leaf return. No
expected-word guards are required.

## Verification

- The focused `generated_64120.c.o` build passed.
- Focused object disassembly matches all 27 retail instruction words and
  relocations.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_1503A60C` as byte-exact.
- The linked and retail 108-byte spans share SHA-256
  `2cc7a51561b11b95abf5d25dc8ea767973ece17d01457d2d7e71933cd8efb466`.
- Fresh matcher totals are `2,901 / 5,466 (53.07%)` overall and
  `2,327 / 4,790 (48.58%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 28-word `func_1503D5F0`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
