# Game small record-copy allocator byte match

Date: 2026-09-29

## Scope and behavior

`func_1515FF74` in `conker/src/game/generated_18D250.c` spans 30 words and
120 bytes at `0x1515FF74..0x1515FFEC`. Its recovered body:

- Calls `func_15167A68` for a `0x34`-byte record.
- Forwards the fourth argument as the allocation category.
- Adds `0x18` to the second argument for the allocation offset.
- Narrows the third argument to the byte selector and passes final flag one.
- Returns explicit null when allocation fails.
- Copies eight bytes from the source into record offset `0xE` and returns the
  initialized record.

## Compiler shape

Declaring the selector as `u8` reproduces retail's byte reload from its stack
home at `sp + 0x33`; a full-width declaration would load the complete word.
The explicit `return NULL` is also material: retail writes zero to `v0` in the
null branch before joining the epilogue.

All 30 instructions emit directly from semantic C. The 40-byte frame, four
argument homes, allocator stack arguments, both call relocations and delay
slots, retained result spill around `memcpy`, and epilogue need no
expected-word guards.

## Verification

- The focused `generated_18D250` object builds with all 30 retail words.
- The complete ELF relink passes.
- Direct linked comparison reports zero differences across all 120 bytes.
- Both spans share SHA-256
  `9fa00267f5c4abdc9ea6b53cfb528fd6267781e75343bd4a68140e4daec73f9f`.
- The authoritative matcher omits `func_1515FF74` from its non-exact list and
  reports `2,991 / 5,465 (54.73%)` overall and `2,416 / 4,789 (50.45%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Keep this direct-C
match independent from the larger neighboring routines in `generated_18D250`.
