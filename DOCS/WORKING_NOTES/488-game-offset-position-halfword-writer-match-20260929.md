# Game offset position halfword writer byte match

Date: 2026-09-29

## Scope and behavior

`func_150C7D7C` in `conker/src/game/generated_F4D20.c` has 32 executable
words and 128 bytes at `0x150C7D7C..0x150C7DFC`. The matcher tracks the
following zero word at `0x150C7DFC` as retail padding, making the complete
slot 33 words and 132 bytes through `0x150C7E00`.

Its recovered body queries `func_15083E90(0xC)`, then writes three signed
halfwords to the destination:

- Destination `0x10` receives source float `0x14` minus `30.0f`.
- Destination `0x12` receives source float `0x18` plus `50.0f`.
- Destination `0x14` receives source float `0x1C` plus `30.0f`.

Each floating-point result is truncated toward zero before the halfword store.

## Compiler shape

The pointer arguments and direct offset expressions reproduce retail's
24-byte frame, saved return-address lifetime, query-call delay slot, two float
constant materializations, three load/arithmetic/truncate sequences, required
`mfc1` hazard nops, and return delay slot.

All 32 executable instructions emit directly from semantic C. No
expected-word guards are needed, and the compiler-owned trailing zero padding
word also agrees with retail.

## Verification

- The focused `generated_F4D20` object builds with all 32 executable retail
  words and the following zero padding word.
- The complete ELF relink passes.
- Direct linked comparison reports zero differences across both the 128-byte
  executable body and the complete 132-byte tracked slot.
- The 128-byte bodies share SHA-256
  `18e3c934ee0783473d0aede4c877f66f969b43924fb18678f7210490066a8eb8`.
- The 132-byte tracked slots share SHA-256
  `c4ef61067900cb3ed96347ae8f10d7f584a99329af68d91fb82f84fc595df062`.
- The authoritative matcher omits `func_150C7D7C` from its non-exact list and
  reports `2,992 / 5,465 (54.75%)` overall and `2,417 / 4,789 (50.47%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. Keep this direct-C
match independent from the larger neighboring routines in `generated_F4D20`.
