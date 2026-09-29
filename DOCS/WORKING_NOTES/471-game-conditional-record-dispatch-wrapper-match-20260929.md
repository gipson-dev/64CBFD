# Game conditional record-dispatch wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_15095A90` in `conker/src/game/generated_C1D70.c` spans 30 words and
120 bytes. It passes a record selector, three floating-point values, and a
scalar to `func_15095B08`, which writes an activity flag through a stack
pointer. When that flag is nonzero, the wrapper replaces its original result
through the five-argument `func_15095D34` dispatch; otherwise it returns the
original `arg0` value.

An initial separate result local produced 33 words by allocating another stack
slot and moving the value through `v1`. Reusing the homed `arg0` parameter as
the mutable result reproduces retail's `sp+0x28` lifetime and complete 30-word
schedule. No guarded words are required. The two callee bodies remain unchanged
placeholders; only their recovered argument contracts were made explicit.

## Verification

- The focused padded object reproduces the complete 30-word retail slot.
- The complete non-matching build and relink pass.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `d8ac1a75d5ffe67afa27db5b941e1061d2c9ae3710f844bdcbbe23ca36b5e28d`.
- The authoritative matcher reports `2,973 / 5,465 (54.40%)` overall and
  `2,399 / 4,789 (50.09%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary small Game placeholder. `func_15095B08` and
`func_15095D34` remain separate, larger restoration targets.
