# Game current-player threshold dispatch byte match

Date: 2026-09-29

## Scope and behavior

`func_150DEB58` in `conker/src/game/generated_10B7D0.c` occupies 34 words and
136 bytes at `0x150DEB58..0x150DEBE0`. It indexes `D_800DBFF0` with the current
player index `D_80082FA0`. When float field `0x388` of that `0x9A0`-byte record
is below `5.0f`, it returns zero. Otherwise it calls `func_15140410` with the
incoming object, embedded records at offsets `0x120` and `0x12C`, and the
incoming signed 16-bit mode, returning the callee result.

## Source recovery

The previous body was a false zero-return placeholder. Existing `struct108`
layout evidence establishes the player-record stride and threshold field, and
the matched wrappers `func_150F337C` and `func_150F7F58` establish the embedded
record call idiom. A focused local player-record view preserves only the
measured field and size needed by this generated slice.

The typed array access emits retail's complete multiply-by-`0x9A0` shift/add
chain, both global relocation pairs, and the field load. A direct early return
followed by the four-argument call reproduces the float branch, argument
addresses, signed mode lifetime, result, and epilogue. All 34 words emit
directly from C with no expected-word guards.

## Verification

- The focused `generated_10B7D0` object reproduces all 34 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,033 / 5,463 (55.52%)` overall and
  `2,455 / 4,789 (51.26%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 136 linked bytes at
  Game offset `0xDEB58` and retail ROM offset `0x10C008`.
- Both spans share SHA-256
  `f6c3bce2d227ddb0b50324b277e7367e65edae74debfba82802ec09ceada3973`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_1514DBB8`, the next ordinary 32-word placeholder. Keep
`func_15015F40`, `func_150A76F0`, `func_15106E78`, and Init `func_1000FF90`
parked at their documented special-case boundaries.
