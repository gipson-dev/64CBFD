# Init arena-anchor initializer byte match

Date: 2026-09-29

## Scope and behavior

`func_10003BD0` in `conker/src/init_3BD0.c` occupies 28 words and 112 bytes at
`0x10003BD0..0x10003C40`. Its recovered C body:

- Installs arena base `D_800E9D10` as the head in `D_800380B4`.
- Clears node fields `0x0`, `0x4`, `0xC`, and `0x10`.
- Stores `D_80038098 - D_800E9D10 - 0x14` in field `0x8`.
- Loads the initialized head once and installs it in `D_800380BC`,
  `D_800380B8`, and `D_800380B0`.

## Compiler shape

The repeated global-head accesses are significant: replacing them with local
arena and node pointers lets IDO collapse the body from 27 compiler words to
22 and loses retail's repeated loads. The accepted semantic C keeps those
accesses explicit and emits the correct field initialization and final anchor
stores in a 27-word compiler body.

Retail retains three opening addresses in `$v1`, `$a0`, and `$a1`. IDO instead
finishes the first two addresses immediately and materializes `D_800380BC`
through `$at` near the final stores. Twenty stale-checked guards normalize
that one closed schedule. The first guard inserts the sole additional word,
the `R_MIPS_LO16:D_800380BC` address completion through `$a1`; subsequent
guards preserve the corresponding independent instruction order and moved
relocations. Once that cycle closes, the final `D_800380B8` and `D_800380B0`
stores and the epilogue emit directly from C.

## Verification

- The focused `init_3BD0` object matches all 28 retail words and all symbol
  relocations.
- The shared guard manifest passed a complete Makefile-driven object rebuild
  and ELF relink with every existing stale check active.
- Direct linked comparison reports zero differences across all 112 bytes.
- Both spans share SHA-256
  `daff5038fcc53e085d9b5dd4c1683c53f53e11a74ff73ea438b7edca3336bffc`.
- The authoritative matcher omits `func_10003BD0` from its non-exact list and
  reports `2,996 / 5,465 (54.82%)` overall and `395 / 495 (79.80%)` in Init,
  with zero address-drift rows.

## Resume boundary

The next measured Init rows were SDK cache-maintenance routines
`osInvalICache` and `osWritebackDCache`. They have since been restored to
their original handwritten assembly ownership in Working Note 492. Continue
with an ordinary small Game or Init candidate.
