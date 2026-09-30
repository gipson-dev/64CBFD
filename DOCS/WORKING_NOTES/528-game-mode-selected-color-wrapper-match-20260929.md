# Game mode-selected color wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_150D22F4` in `conker/src/game/generated_FF5C0.c` occupies 32 words and
128 bytes at `0x150D22F4..0x150D2374`. It accepts an existing handle, a record
pointer, and a signed 16-bit selector. When record byte `0x28` equals one, it
calls `func_1517F08C` with record byte `0x3C` and three `0xFF` channel values.
Otherwise it uses record byte `0x3D` and three zero channel values. Both paths
forward the selector as the sixth argument and return the updated handle.

## Source recovery

The previous body was a false zero-return placeholder. The neighboring matched
callback `func_15182768`, which appears in the same retail function table,
establishes the three-argument callback ABI and the six-argument
`func_1517F08C` contract. Expressing the two modes as a direct `if`/`else`
restores retail's `0x20` frame, incoming argument spills, mode-byte test,
path-specific record loads, five register/stack arguments, shared return
handle, and epilogue. All 32 words emit directly from C with no expected-word
guards.

## Verification

- The focused `generated_FF5C0` object reproduces all 32 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,032 / 5,463 (55.50%)` overall and
  `2,454 / 4,789 (51.24%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0xD22F4` and retail ROM offset `0xFF7A4`.
- Both spans share SHA-256
  `7bb68200536b66166927c2070077dbc5ac251147b697bc66c064635dd18c443c`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_150DEB58`, the next ordinary 34-word placeholder. Keep
`func_15015F40`, `func_150A76F0`, `func_15106E78`, and Init `func_1000FF90`
parked at their documented special-case boundaries.
