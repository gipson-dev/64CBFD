# Game two-owner linked-list lookup byte match

Date: 2026-09-29

## Scope and behavior

`func_15155FD4` in `conker/src/game/generated_182C30.c` spans 21 words and
84 bytes at `0x15155FD4..0x15156028`. It searches two owner records beginning
at `D_800DCE50` and ending at `D_800DD190`:

- Each owner is `0x1A0` bytes and holds its list head at offset `0x140`.
- Each node holds its next pointer at offset eight and key byte at offset
  `0x10`.
- The first node whose key equals the signed integer argument is returned.
- A null result is returned only after both lists are exhausted.

Typed owner and node structures recover the nested owner/list traversal,
branch-likely updates, successful pointer return, and null fallthrough.

## Compiler shape

Using a signed 32-bit key argument produces retail's complete 21-word
instruction skeleton. A byte argument instead adds an argument mask and
register moves, expanding the function to 25 words.

IDO assigns the owner cursor and end pointer to the opposite registers from
retail while preserving the same control flow. Eight expected-word guards
normalize that closed register-allocation cycle. Four retain explicit
relocation checks for `D_800DCE50` and `D_800DD190`; the remaining four cover
the owner-head load, owner increment, and final loop branch. The node walk,
key comparison, returns, and all delay slots emit directly from C.

## Verification

- The focused `generated_182C30` object builds with all 21 retail words.
- The complete ELF relink passes.
- Direct linked comparison reports zero differences across all 84 bytes.
- Both spans share SHA-256
  `321b9b3da9418278f6de2c2970961e4df0babf026867ae99d5f8f30473d11094`.
- The authoritative matcher omits `func_15155FD4` from its non-exact list and
  reports `2,988 / 5,465 (54.68%)` overall and `2,413 / 4,789 (50.39%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Keep `guMtxIdentF`
parked at its measured SDK compiler-profile boundary, and keep the documented
generated-slice ownership cases out of the ordinary C queue.
