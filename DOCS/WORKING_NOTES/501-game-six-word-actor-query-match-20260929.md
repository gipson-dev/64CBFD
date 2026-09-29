# Game six-word actor query byte match

Date: 2026-09-29

## Scope and behavior

`func_151420F8` in `conker/src/game_16EE20.c` occupies 34 words and 136 bytes
at `0x151420F8..0x15142180`. It copies the six-word template at `D_800A5200`
to a stack buffer, converts the incoming actor pointer to its zero-based
`D_800CC2D0` index, submits all six words through `func_150A2AEC`, and returns
whether the query result differs from `-1`.

## Source recovery

The previous C copied the six words through six array assignments. IDO loaded
all six source words before storing any of them, unlike retail's alternating
load/store schedule. Declaring a file-local six-word aggregate and assigning
`tmp = D_800A5200` restores the exact retail block-copy expansion, including
its `at`/`t9` temporary alternation and the final store in the call delay slot.

The previous index expression divided by unsigned `sizeof(struct127)`, which
selected `divu`. Casting the divisor to `s32` restores retail's signed `div`.
Expanding the final `!= -1` expression into an explicit failure branch restores
retail's two return paths instead of IDO's shorter add-and-`sltu` sequence.
The complete function then emits directly from C with no expected-word guards.

## Verification

- The focused `game_16EE20` object matches the complete 34-word retail stream
  with no guards.
- The authoritative linked matcher reports `3,005 / 5,463 (55.01%)` overall
  and `2,427 / 4,789 (50.68%)` in Game, with zero address-drift rows.
- Direct linked comparison reports zero differences across all 136 bytes.
- Both spans share SHA-256
  `4a242943a6ff310e5ae3c7004300f1cb55b84a08625c9b69fc6f668cc1481ec2`.
- `make tools-check`, all 10 tests under `tools/tests`,
  `make -C conker replace NON_MATCHING=1 -j4`, and the outer
  `make NON_MATCHING=1 -j4` build pass.

## Resume boundary

Recheck the 30-difference tier beginning at `func_1503F964`; most neighboring
entries may still be zero-return placeholders, so select the next candidate by
retail/source semantic quality rather than raw mismatch count alone. Keep Init
`func_1000FF90` parked at its measured compiler-allocation boundary.
