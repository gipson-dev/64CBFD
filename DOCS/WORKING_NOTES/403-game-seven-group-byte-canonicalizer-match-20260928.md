# Game seven-group byte canonicalizer byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_15084D00` in
`conker/src/game/generated_B21B0.c` with its semantic Game routine. The retail
slot spans 28 words and 112 bytes.

## Recovered behavior

The function reads the byte at offset four from its input record and searches
seven byte-table groups. `D_8009D954[group]` supplies each table's entry count,
while `D_80087240[group]` points to its entries. A match returns the first byte
of that group; if every group misses, the original record byte is returned.

The source uses direct indexed nested loops. The cached input byte is held in
an `s32`, while its load remains unsigned. That width gives IDO retail's `v1`
allocation, leaving `v0`, `a2`, and `a0` for the group index, group count, and
entry index. All 28 words emit directly from C under the slice's existing
compiler profile; no expected-word guards are required.

## Verification

- The focused `generated_B21B0.c.o` build passed under the existing profile.
- Focused object disassembly matches all 28 retail instruction words and
  relocations.
- The full `wsl make -C conker NON_MATCHING=1` rebuild and relink passed.
- `match_progress.py` classifies `func_15084D00` as byte-exact.
- The linked and retail 112-byte spans share SHA-256
  `3b3e792efd6c29d299a34033d671ade846af96083c28773f36a40ab1e1006588`.
- Fresh matcher totals are `2,905 / 5,466 (53.15%)` overall and
  `2,331 / 4,790 (48.66%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_1509F5F4`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
