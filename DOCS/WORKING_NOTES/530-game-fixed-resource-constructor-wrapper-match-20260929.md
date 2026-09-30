# Game fixed resource-constructor wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_1514DBB8` in `conker/src/game/generated_179F30.c` occupies 32 words and
128 bytes at `0x1514DBB8..0x1514DC38`. It forwards the incoming owner to
`func_15160A58` with mode two, resource `D_800A58A0`, subtype two, and twelve
fixed stack arguments: `0x12C`, `0x28`, four `0xFF` values, zero, `-1`, two
zeros, `0xFF`, and one. The callee result remains the wrapper result.

## Source recovery

The previous body was a false zero-return placeholder. Other retail calls to
`func_15160A58` establish its wide constructor ABI and the correspondence
between stack offsets `0x10..0x3C` and arguments four through fifteen.
Expressing the complete 16-argument call directly restores retail's `0x48`
frame, constant preload registers, reverse stack-store schedule, resource
relocation pair, call, delay slot, and epilogue. All 32 words emit directly
from C with no expected-word guards.

## Verification

- The focused `generated_179F30` object reproduces all 32 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,034 / 5,463 (55.54%)` overall and
  `2,456 / 4,789 (51.28%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0x14DBB8` and retail ROM offset `0x17B068`.
- Both spans share SHA-256
  `87d5dcc1c3831a00b3ddcd3a65994a1b55e497ccc924c820ed8cafd6e055a110`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_1514F3CC`, the next ordinary 32-word placeholder. Keep
`func_15015F40`, `func_150A76F0`, `func_15106E78`, and Init `func_1000FF90`
parked at their documented special-case boundaries.
