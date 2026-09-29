# Game active-object state updater byte match

Date: 2026-09-29

## Scope

This pass completed `func_1507C370` in
`conker/src/game/generated_A9260.c`. The tracked retail slot spans 28 words
and 112 bytes at `0x1507C370..0x1507C3E0`.

## Recovered behavior

The routine starts at `D_800CC2D0` and traverses the signed active-object
count in `D_8008FD8C`. For each `0x32C`-byte object, it reads the state pointer
at offset `0x31C`. Null states are skipped. Every non-null state is passed to
`func_1507C3E0` together with pointers to the three adjacent unsigned
halfwords at state offsets `0x114`, `0x116`, and `0x118`.

Using typed `struct127` and `struct126` pointers recovers retail's retained
object and state-pointer lifetimes. The source-level `object++` update emits as
the `0x32C` pointer advance in the loop branch delay slot. Correcting the
wrapper and callee declaration to `void` also records their actual return
contract. The complete function emits directly from C without expected-word
guards.

## Verification

- The focused `generated_A9260.c.o` comparison matches all 28 retail words,
  the `R_MIPS_26` relocation for `func_1507C3E0`, two `HI16`/`LO16` pairs for
  `D_8008FD8C`, and one pair for `D_800CC2D0`.
- `wsl make -C conker NON_MATCHING=1 -j1` relinked the ELF and binary
  successfully.
- The linked ELF and retail 112-byte spans share SHA-256
  `f76ebf3e5c54848c244a826c349a9b156683e93f088e363b88d3e31ccab607af`.
- Fresh matcher totals are `2,953 / 5,465 (54.03%)` overall and
  `2,379 / 4,789 (49.68%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 29-word `func_15095060`,
currently at 28 real differences. It is a zero-return placeholder in
`conker/src/game/generated_C1D70.c`; recover its semantics from the retail
`C1D70` assembly slice before attempting compiler normalization. Keep
`func_15194320` and `func_15194394` parked behind generated-slice jump-table
and rodata ownership, `func_151F3D78` parked behind audio-object layout drift,
the tied Init SDK cache routines in their ownership lane, and
`func_10012588` parked on address drift.
