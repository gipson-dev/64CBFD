# Game packed descriptor builder byte match

Date: 2026-09-29

## Scope

This pass completed `func_15095060` in
`conker/src/game/generated_C1D70.c`. The tracked retail slot spans 29 words
and 116 bytes at `0x15095060..0x150950D4`.

## Recovered behavior

The routine constructs the 12-byte global descriptor `D_800D2C90`. When the
third argument is non-null, it first publishes the descriptor address at
offset `0x10` in that output object.

The first source word has two forms. Values below `0x10000000` are copied
directly into the descriptor. Larger values are treated as a `u32` table
address, with the selected word read at index `arg1 >> 8`. Source halfwords at
offsets `0x6` and `0x8` become descriptor halfwords at `0x4` and `0x6`.
Source bytes at `0xA`, `0xB`, and `0x4` become descriptor bytes at `0x8`,
`0x9`, and `0xA`. The corrected return type is `void`.

Typed source and descriptor structures preserve the recovered semantics, but
IDO 5.3 at this slice's `-O2 -g3` profile emits 34 words. It rematerializes the
absolute descriptor address before every store and hoists the table-index
calculation ahead of the range branch. Source-only pointer, cursor, register,
and opaque-array variants still emitted 32 or more words. A disposable `-O1`
probe retained the descriptor base but introduced a frame and different
register allocation, so changing the slice profile was not appropriate.

Thirty relocation-aware expected-word rows normalize that compiler artifact.
They retain the descriptor base in `v1`, defer the indexed lookup to the table
branch, and reproduce retail's field-load and store schedule. Six repeated
descriptor `lui` words are omitted, the final repeated address word is
repurposed for the second byte store, and one trailing `nop` is inserted after
the restored return. Every row verifies its expected instruction and
relocation before applying, so compiler drift fails closed.

## Verification

- The focused `generated_C1D70.c.o` comparison matches all 29 retail words,
  including both `D_800D2C90` relocation pairs and both branch targets.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and relinked the complete
  ELF and binary successfully after the shared patch table invalidated padded
  objects.
- The linked ELF and retail 116-byte spans share SHA-256
  `7e3c0b9009d0e83b9a405b6373de2aacc7545df9c12723db4fc78095317b0b55`.
- Fresh matcher totals are `2,954 / 5,465 (54.05%)` overall and
  `2,380 / 4,789 (49.70%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 28-word `func_15096D08`,
currently at 28 real differences. It is a zero-return placeholder in
`conker/src/game/generated_C3E20.c`; recover its loop from the retail `C3E20`
assembly slice before attempting compiler normalization. Keep
`func_15194320` and `func_15194394` parked behind generated-slice jump-table
and rodata ownership, `func_151F3D78` parked behind audio-object layout drift,
the tied Init SDK cache routines in their ownership lane, and
`func_10012588` parked on address drift.
