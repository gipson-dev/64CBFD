# Game randomized RGBA initializer byte match

Date: 2026-09-29

## Scope and behavior

`func_15152ABC` in `conker/src/game/generated_17CAF0.c` occupies 31 words and
124 bytes at `0x15152ABC..0x15152B38`. It uses the first
`func_150ADA20` result to select one of five three-byte RGB entries from
`D_800A5FE0`. A second result sets the output alpha byte to an inclusive value
from 155 through 255. The selected RGB bytes are then copied to output offsets
zero through two.

## Source recovery

The previous body was a false zero-return placeholder. Both random remainders
must use unsigned divisors. Retaining the five-entry result in a `u8` restores
retail's explicit narrowing before the multiply-by-three table index. Declaring
that byte before the selected-color pointer also restores the pointer's
`sp+0x18` lifetime across the second RNG call. All 31 words emit directly from
C with no expected-word guards.

## Verification

- The focused `generated_17CAF0` object reproduces all 31 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,036 / 5,463 (55.57%)` overall and
  `2,458 / 4,789 (51.33%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes at
  Game offset `0x152ABC` and retail ROM offset `0x17FF6C`.
- Both spans share SHA-256
  `88d2149442bf8daa04fcfad60211c9ac28fe73d3f87a481e14acbb788959d265`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_15157898`, the next ordinary 32-word row reported by the
matcher. Keep `func_15015F40`, `func_150A76F0`, `func_15106E78`, and Init
`func_1000FF90` parked at their documented special-case boundaries.
