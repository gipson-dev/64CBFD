# Game bounded table-buffer append byte match

Date: 2026-09-29

## Scope and behavior

`func_1507EBB8` in `conker/src/game/generated_AC030.c` occupies 32 words and
128 bytes at `0x1507EBB8..0x1507EC38`. It selects a source byte sequence from
`D_80086C24` and its length from `D_8009BBF0`, appends that sequence to a
caller-owned buffer only when the resulting count remains below 40 bytes, and
then advances the caller's count.

## Source recovery

The previous body was a false zero-return placeholder. The recovered table
types expose the selector-indexed source pointer and byte length. Keeping the
loaded byte in a full-width `s32` local is essential: it gives IDO retail's
`$a3` length lifetime, 32-byte frame, source spill at `0x1C`, and call-delay
length spill at `0x18`. Declaring that local as `u8` instead produced a
40-byte frame and `$v0` allocation. The final semantic body emits all retail
words directly with no expected-word guards.

## Verification

- The focused `generated_AC030` object reproduces all 32 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,028 / 5,463 (55.43%)` overall and
  `2,450 / 4,789 (51.16%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0x7EBB8` and retail ROM offset `0xAC068`.
- Both spans share SHA-256
  `6264e616750342b961bace698a74aa7a7f62df4dcba9df8a664422c21cee6499`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_150A32B4`, the next ordinary 31-word placeholder. Retail
constructs a large stack-local query record from four integer coordinates,
calls `func_150A1DA0`, and returns whether that call produced zero.
