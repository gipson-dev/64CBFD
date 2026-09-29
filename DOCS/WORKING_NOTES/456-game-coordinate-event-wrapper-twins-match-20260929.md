# Game coordinate-event wrapper twins byte match

Date: 2026-09-29

## Scope

This pass completed adjacent structural twins `func_150B3E74` and
`func_150B3EE8` in `conker/src/game/generated_E1280.c`. Each tracked retail
slot spans 29 words and 116 bytes. Their addresses are
`0x150B3E74..0x150B3EE8` and `0x150B3EE8..0x150B3F5C`.

## Recovered behavior

Both routines read the object's three position floats at offsets `0x10`,
`0x14`, and `0x18`, truncate them to signed 16-bit coordinates, and call
`func_1000FC18` with event `0x221` and duration `0xFA0`. The first wrapper
then invokes `func_151478F4`; the second invokes `func_15147928`.

The corrected return type is `void`. Direct casts from the three loaded
floats to `s16`, together with the complete `func_1000FC18` prototype,
reproduce retail's load order, FP truncations, halfword sign extensions,
stacked fifth argument, and both callback delay slots. Both complete routines
emit directly from semantic C. No expected-word guards or assembly fallback
are required.

## Verification

- The focused compact object matches all 29 words in each routine, including
  both call relocations and every delay slot.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and linked the complete ELF
  and binary successfully.
- The linked ELF span for `func_150B3E74` and pristine retail span share
  SHA-256
  `5d8fee60e1072f4d463b9ddb9aa49798d374ac0f46b921e80b13d684e0a013bc`.
- The linked ELF span for `func_150B3EE8` and pristine retail span share
  SHA-256
  `c509e2d4d06f21b27f1e0706ca67b87e692c894f3e7569f9cd29098c5c75d7c1`.
- Fresh matcher totals are `2,958 / 5,465 (54.13%)` overall and
  `2,384 / 4,789 (49.78%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked Game queue with 28-word `func_150E32D0`, at 28
real differences. Keep `func_15194320` and `func_15194394` parked behind
generated-slice jump-table and rodata ownership, `func_151F3D78` parked behind
audio-object layout drift, the tied Init SDK cache routines in their ownership
lane, and `func_10012588` parked on address drift.
