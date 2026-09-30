# Game resource slot-array teardown byte match

Date: 2026-09-29

## Scope and behavior

`func_150B6D78` in `conker/src/game/generated_E4070.c` occupies 33 words and
132 bytes at `0x150B6D78..0x150B6DFC`. It releases the standalone allocation
in `D_800D9894`, then scans the ten pointer slots from `D_800D9898` through
`D_800D98BC`. Every non-null allocation is passed to `func_1516972C`, and
each released owner is cleared. The routine finishes by setting
`D_800D9890` to state 3.

## Source recovery

The previous body was a false zero-return placeholder. The recovered C uses
the exclusive `D_800D98C0` end symbol to preserve retail's do-while scan and
the existing no-loop-unroll profile for `generated_E4070`.

IDO directly reproduces 31 of the 33 retail words, including the 32-byte
frame, saved `$s0`/`$s1` lifetimes, standalone release, branch-likely loop,
per-slot clears, and epilogue. Two relocation-aware expected-word guards
exchange only the independent low-half address resolutions for the cursor
and exclusive end pointer.

## Verification

- The focused `generated_E4070` object reproduces all 33 retail words.
- The full replacement build, outer non-matching build, and ELF relink pass.
- The authoritative matcher reports `3,017 / 5,463 (55.23%)` overall and
  `2,439 / 4,789 (50.93%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 132 linked bytes.
- Both spans share SHA-256
  `c9f16b9bdec0d5a3f4a6f2778cd94a59aad0204e99ea73f300251dbcaa83423d`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_150BDE90` as the next ordinary 31-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
