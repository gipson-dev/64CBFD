# Game secondary collision-classifier wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_15046F84` in `conker/src/game/generated_71820.c` occupies 32 words and
128 bytes at `0x15046F84..0x15047004`. It classifies an input position and
collision record through `func_15047004`. Classification zero delegates to
`func_15046D00` with the original 16-bit selector, class one returns false,
and class two returns true.

## Source recovery

The previous body was a false zero-return placeholder. Retail uses the same
four-argument classifier-switch scaffold as adjacent `func_15046C80`, changing
only the class-zero handler. The recovered semantic switch and observed
`func_15046D00` ABI reproduce the complete frame, argument home stores and
reloads, dispatch branches, branch-likely return, and epilogue directly from
C. No expected-word guards are used.

## Verification

- The focused `generated_71820` object reproduces all 32 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,027 / 5,463 (55.41%)` overall and
  `2,449 / 4,789 (51.14%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0x46F84` and retail ROM offset `0x74434`.
- Both spans share SHA-256
  `70ad2ec1ad364a1b82e41a9c63b2116dea4702ff54c0833feeb3c4e930559646`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Recover Game `func_1507EBB8`, the next ordinary 32-word placeholder. Retail
shows a bounded copy from the selector-indexed `D_80086C24` source table into
an output buffer using the selector-indexed byte length in `D_8009BBF0`.
