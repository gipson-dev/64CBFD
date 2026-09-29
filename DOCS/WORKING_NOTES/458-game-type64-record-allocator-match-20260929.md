# Game type-0x64 record allocator byte match

Date: 2026-09-29

## Scope

This pass completed `func_15104170` in
`conker/src/game/generated_131620.c`. Its tracked retail slot spans 29 words
and 116 bytes at `0x15104170..0x151041E4`.

## Recovered behavior

The routine requests a `0x20`-byte type-`0x64` record through
`func_15167A68(0x64, 0, 0x20, 0, 0xFF, 1)`. Allocation failure leaves the
record untouched. On success it writes timer `0xF` at offset `0x18`, clears
state bytes `0x1A` and `0x1B`, stores the second and third arguments at
offsets `0x10` and `0x14`, and narrows the first argument into selector byte
`0x1C`.

The corrected return type is `void`. An `s32` return model preserved the
allocator pointer explicitly, adding one copy after the call and another in
the epilogue. Retail merely leaves that pointer incidentally in `v0`; the
known caller ignores it. With the `void` contract, the complete frame,
argument spills, allocator call, null branch, stores, and epilogue emit
directly from semantic C. No expected-word guards are required.

## Verification

- The focused compact object matches all 29 retail words and the
  `func_15167A68` call relocation.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and linked the complete ELF
  and binary successfully.
- The linked ELF and pristine retail 116-byte spans share SHA-256
  `31cd26b3f8dc9d4dad65be176cb2da0a5c555d08a8d1db15f85f1df654543519`.
- Fresh matcher totals are `2,960 / 5,465 (54.16%)` overall and
  `2,386 / 4,789 (49.82%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 30-word `func_1511A7C0`, at 28
real differences. Keep `func_15194320` and `func_15194394` parked behind
generated-slice jump-table and rodata ownership, `func_151F3D78` parked behind
audio-object layout drift, the tied Init SDK cache routines in their ownership
lane, and `func_10012588` parked on address drift.
