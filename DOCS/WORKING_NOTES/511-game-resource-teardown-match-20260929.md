# Game resource teardown byte match

Date: 2026-09-29

## Scope and behavior

`func_15080BE8` in `conker/src/game/generated_AD9B0.c` occupies 31 words and
124 bytes at `0x15080BE8..0x15080C64`. It clears active byte `D_800D1941`,
releases the primary object in `D_800D1950`, and frees the allocation in
`D_800D1944`. When optional owner slot `D_800D1948` is nonzero, it frees that
allocation plus `D_800D194C` and `D_800D1998`, then clears `D_800D1948`.
Finally it invokes `func_151F2D6C(0, 0x5622)`.

## Source recovery

The previous body was a false zero-return placeholder. The recovered `void`
routine expresses the release order, optional cleanup gate, owner-slot clear,
and final tagged teardown directly. It reproduces the complete 24-byte frame,
all six calls, branch-likely exit, delay slots, and epilogue.

IDO allocates the optional allocation directly to `a0`; retail first keeps it
in `v0`, tests that register, and moves it to `a0` in the free-call delay slot.
Four relocation-aware stale checks normalize only that closed load/test/move
window. No instruction is inserted or omitted.

## Verification

- The focused `generated_AD9B0` object accepts all four stale checks.
- The full guard-table rebuild, replacement build, outer non-matching build,
  and ELF relink pass.
- The authoritative matcher reports `3,015 / 5,463 (55.19%)` overall and
  `2,437 / 4,789 (50.89%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes.
- Both spans share SHA-256
  `cd3ecd60f04fee86983201b3860e4136788407f2e8ee6b6919b8b0ad28bf0294`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_150A0D14` as the next ordinary 30-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
