# Game variable-tail descriptor wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_15094FE8` in `conker/src/game/generated_C1D70.c` spans 30 words and
120 bytes. Like adjacent `func_15094F70`, it first normalizes a source
descriptor into `D_800D2C90` through `func_15095060`, then dispatches through
`func_150950D4` with a zero fifth argument.

This variant accepts eleven inputs and forwards all five incoming tail values
to the final call. Expressing that complete ABI directly reproduces retail's
incoming loads and outgoing stack stores. All 30 words emit from semantic C
without guards.

## Verification

- The focused padded object fits the complete 30-word retail slot.
- The complete non-matching build and relink pass.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `552edff8f4df1216c778a7dfc877db65bce0f6d25ec744671c9b1f6dec7f41eb`.
- The authoritative matcher reports `2,972 / 5,465 (54.38%)` overall and
  `2,398 / 4,789 (50.07%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary small Game placeholder. The shared
`func_150950D4` implementation remains a separate, larger restoration target.
