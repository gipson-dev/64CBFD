# Game zero-payload record dispatch byte match

Date: 2026-09-29

## Scope

This pass completed `func_1514DAA4` in
`conker/src/game/generated_179F30.c`. Its tracked retail slot spans 29 words
and 116 bytes at `0x1514DAA4..0x1514DB18`.

## Recovered behavior

The routine sets bit 1 in the object word at offset `0x94`, prepares a local
two-word payload containing zeroes, and requests an eight-byte record through
`func_15158BD0(arg0, 1, 8)`. If allocation succeeds, it copies the payload to
record offset `0x58` and dispatches the new record with the original object
and event selector `0x13` through `func_1514EC1C`.

The corrected return type is `void`. Twenty-seven of the 29 words emit from
the semantic C body. IDO independently schedules the payload-size load and
retained-object spill on the opposite sides of the allocator call, so two
fail-closed expected-word guards reproduce retail's order. They do not replace
control flow, data access, call targets, or recovered behavior.

## Verification

- The focused padded object matches all 29 retail words, including the two
  guarded scheduling positions and the allocator relocation.
- `wsl make -C conker NON_MATCHING=1 -j1` rebuilt and linked the complete ELF
  and binary successfully.
- Direct comparison of the linked ELF and pristine retail 116-byte spans
  passed. Both spans share SHA-256
  `86252aec5532b02318f5211fd7a49240a496794ab58da9d4a86654495738b51b`.
- Fresh matcher totals are `2,962 / 5,465 (54.20%)` overall and
  `2,388 / 4,789 (49.86%)` in Game, with one address-drift row.

## Resume boundary

Resume the fresh ordinary Game queue with 17-word `func_150721A4`, at 16 real
differences. Keep `func_15194320` and `func_15194394` parked behind generated-
slice jump-table and rodata ownership, `func_151F3D78` parked behind
audio-object layout drift, the tied Init SDK cache routines in their ownership
lane, and `func_10012588` parked on address drift.
