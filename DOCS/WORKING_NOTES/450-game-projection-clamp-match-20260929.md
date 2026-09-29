# Game projection clamp byte match

Date: 2026-09-29

## Scope

This pass completed `func_15145548` in `conker/src/game_16EE20.c`. The tracked
retail slot spans 61 words and 244 bytes at `0x15145548..0x1514563C`.

## Recovered behavior

The routine calls `func_1514563C` to calculate a projection scalar. When the
caller does not provide the optional fifth argument, it substitutes a local at
`sp+0x24`. A successful negative projection copies the first input vector to
the output. A projection above one writes the first vector plus the direction
vector. If the projection query fails, the first input vector is copied to the
output unchanged.

The existing component-wise float assignments described the same values but
compiled as floating-point loads and stores. Retail performs both fallback
copies as three raw words. Expressing those paths as whole-structure
assignments recovers the `lw`/`sw` copy sequences. It also restores the exact
floating-point temporary cycle used by the upper-clamp vector sums. The
retail `0x28` frame, fifth-argument stack handling, branch-likely bounds, and
helper-call relocation then all emit naturally. No expected-word guards are
needed.

## Verification

- The focused `game_16EE20.c.o` comparison matches all 61 retail words and the
  `R_MIPS_26` relocation for `func_1514563C`.
- `wsl make -C conker NON_MATCHING=1 -j1` relinked the ELF and binary
  successfully.
- The linked ELF and retail 244-byte spans share SHA-256
  `9c7a2fd3165ac85709a9677e3110a65943a5f92c9caa2cb1451fd8206fba2230`.
- Fresh matcher totals are `2,951 / 5,465 (54.00%)` overall and
  `2,377 / 4,789 (49.63%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 29-word `func_1503F5B8`,
currently at 28 real differences. It is a zero-return placeholder in
`conker/src/game/generated_6C960.c`; recover its semantics from the retail
`6C960` assembly slice before attempting compiler normalization. Keep
`func_15194320` and `func_15194394` parked behind generated-slice jump-table
and rodata ownership, `func_151F3D78` parked behind audio-object layout drift,
the tied Init SDK cache routines in their ownership lane, and
`func_10012588` parked on address drift.
