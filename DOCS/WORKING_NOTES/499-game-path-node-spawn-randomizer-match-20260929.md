# Game path-node spawn randomizer byte match

Date: 2026-09-29

## Scope and behavior

`func_15079790` in `conker/src/game_A28B0.c` occupies 60 words and 240 bytes
at `0x15079790..0x15079880`. When `D_800D1892` is set, it assigns identifier
`0xFF` to the current actor. Otherwise it assigns identifier `0x3A`, generates
two random signed offsets in `[-250, 249]`, finds the actor's indexed
`PathNode8`, and writes randomized X and Z positions around that node.

## Source recovery

The previous C cached the indexed `PathNode8 *` and reused it for both
coordinates. That shortened the emitted body by five words: retail reloads
the current actor, path-table base, actor node index, and indexed node pointer
for the Z update. The cached pointer also moved the first signed random offset
from retail's `30(sp)` slot to `26(sp)`.

Expressing the X and Z assignments with independent indexed lookups restores
the repeated loads and moves the signed offset back to `30(sp)`. IDO then
emits the complete retail frame, random modulo operations, sign extension,
integer-to-float conversions, stores, branches, and delay slots directly from
C.

## Verification

- The focused `game_A28B0` object matches the complete 60-word retail shape
  with no expected-word guards.
- The authoritative linked matcher reports `3,003 / 5,463 (54.97%)` overall
  and `2,425 / 4,789 (50.64%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 240 bytes.
- Both spans share SHA-256
  `17a05b13fc4c788386d4fe5f06b22abd7c5fb77eb5a898f1ec0d7fe121570def`.

## Resume boundary

Re-run the authoritative mismatch queue and inspect the remaining
30-difference semantic bodies before choosing the next function. Keep
`func_15015F40` parked behind unresolved indirect-table ownership,
`func_15022640` parked at its measured IDO scheduling boundary, and
handwritten `func_150A76F0` in the assembly lane.
