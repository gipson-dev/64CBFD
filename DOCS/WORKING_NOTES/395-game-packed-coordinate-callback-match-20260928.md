# Game packed-coordinate callback byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_1518CCA8` in
`conker/src/game/generated_1B9F30.c` with its semantic Game routine. The
retail slot spans 30 words and 120 bytes, including three trailing padding
words.

## Recovered behavior

The routine loads a packed 32-bit coordinate offset from record offset
`0x14`. It adds the packed upper half to signed halfword X at `0x34` and adds
the packed value, truncated by the halfword store, to Y at `0x36`.

When signed halfword Z at `0x38` is zero, the routine extracts the low nibble
of the callback byte at `0x3B`. A nonzero nibble indexes the function-pointer
table `D_8008D5D0` and invokes that callback with the record pointer. A zero Z
gate or zero callback index returns without dispatch.

## Compiler normalization

The explicit `0xFFFF0000` mask is required for IDO to reproduce retail's
upper-half extraction shape. The semantic compile otherwise emits the full
frame, branches, delay slots, indirect call, and data accesses at their retail
positions.

Ten function- and offset-scoped expected-word guards normalize one closed
temporary-register allocation cycle: the packed offset uses retail `t1`, the
Z gate uses `t3`, the low-coordinate sum uses `t2`, and the callback index and
scaled table offset use `t4` and `t5`. No relocation guards or control-flow
replacement are required. The guard manifest has no duplicate
`(filename, function, offset)` keys.

## Verification

- The focused `generated_1B9F30.c.o` build passed with every expected word
  validated by `pad_generated_object.py`.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_1518CCA8` as byte-exact.
- The linked and retail 120-byte spans share SHA-256
  `11ea57903c0bc7e72ed5d68b72e52c9b0ee5039ab8344aa6068a6b527125e3e6`.
- Fresh matcher totals are `2,897 / 5,466 (53.00%)` overall and
  `2,323 / 4,790 (48.50%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_1501D258`, currently at
26 real differences. The lower-difference Game rows are documented compiler
boundaries; keep them parked. Also keep `func_151F3D78` parked behind the
pre-existing audio-object layout drift, keep the tied Init SDK cache routines
in their ownership lane, and keep address-drift row `func_10012588` parked.
