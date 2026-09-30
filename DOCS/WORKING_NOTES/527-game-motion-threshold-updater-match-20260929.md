# Game motion-threshold updater byte match

Date: 2026-09-29

## Scope and behavior

`func_150CC638` in `conker/src/game/generated_F9430.c` occupies 32 words and
128 bytes at `0x150CC638..0x150CC6B8`. It always returns one. When object flag
bit zero is set, it reads the signed halfword at offset `0x1C`; values below
32 are scaled by eight and may lower the unsigned byte limit at offset `0x5C`.
It then compares that signed value with the threshold at object offset `0x128`.
When the threshold is lower, the float at `0x12C`, scaled by `D_800BE9A4`, is
added to both accumulators at offsets `0x2C` and `0x30`.

## Source recovery

The previous body was a false zero-return placeholder. Typed object and motion
record views recover the field widths, signed comparisons, flag gate, optional
byte update, and shared floating delta. Reloading the signed value only after
the byte store reproduces retail's path-sensitive semantics.

IDO folds the motion-record address into `$a0`, reuses `$v0` for the signed
value, and omits two repeated record-pointer materializations. Retail instead
keeps the signed value in `$v1`, uses `$v0` first for the scaled byte and then
for the record pointer, and places two address words in branch-likely delay
slots. Thirteen stale-checked expected-word guards normalize only that closed
register/address schedule. Two of those rows insert the retained address and
comparison words; all arithmetic, memory effects, control flow, and the global
relocation originate in semantic C.

## Verification

- The focused `generated_F9430` object reproduces all 32 retail words after
  the 13 expected-word guards are applied.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,031 / 5,463 (55.48%)` overall and
  `2,453 / 4,789 (51.22%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0xCC638` and retail ROM offset `0xF9AE8`.
- Both spans share SHA-256
  `f513b7f3c9bee8f04c2afe8007ea87e74d5ba3cd3a2c240639dcd9bc60eb3bfe`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_150D22F4`, the next ordinary 32-word placeholder. Keep
`func_15015F40`, `func_150A76F0`, `func_15106E78`, and Init `func_1000FF90`
parked at their documented special-case boundaries.
