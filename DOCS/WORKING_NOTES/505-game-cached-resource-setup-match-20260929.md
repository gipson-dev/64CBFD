# Game cached resource setup byte match

Date: 2026-09-29

## Scope and behavior

`func_1517A9A8` in `conker/src/game/generated_1A7260.c` occupies 30 words and
120 bytes at `0x1517A9A8..0x1517AA20`. It accepts a running display-list
cursor and a resource selector. When the selector equals cached
`D_800DD1B0`, the cursor is returned unchanged. Otherwise the routine passes
the cursor, resource source `D_80090614`, selector shifted by eight, and a
20-byte local output record to `func_15094F70`, then caches the selector and
returns the updated cursor.

## Source recovery

The previous body was a false zero-return placeholder. The recovered C
restores the cache gate, the local record required by `func_15095060`'s write
at output offset `0x10`, and the full nine-argument setup call. Keeping the
selector parameter volatile reproduces retail's incoming argument spill and
two independent reloads, restoring the complete 30-word extent.

IDO reproduces the frame, cache branch, local address, constants, call,
cache update, and shared return path. Six stale-checked guards normalize one
closed scheduling permutation among the selector reload/shift, two outgoing
constant stores, shifted-index move, and local-record address calculation.
The guarded words contain no relocations and do not add or remove code.

## Verification

- The focused `generated_1A7260` object emits the complete retail stream after
  the six expected-word guards are applied.
- A full guard-table rebuild and the outer non-matching ROM build pass.
- The authoritative linked matcher reports `3,009 / 5,463 (55.08%)` overall
  and `2,431 / 4,789 (50.76%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 120 bytes.
- Both spans share SHA-256
  `096d913e68b8486c3adef397b4f0076b0c2948e4bd0ffa13139747bada4a89dd`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_15182F58` as the next ordinary 29-difference Game candidate.
Keep `func_15015F40` parked behind its unresolved indirect-table ownership,
`func_150A76F0` in the handwritten-assembly queue, and Init `func_1000FF90`
parked at its measured compiler-allocation boundary.
