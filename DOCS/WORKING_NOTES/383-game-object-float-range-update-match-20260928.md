# Game object float-range update match - 2026-09-28

## Result

`func_15121C00` is byte-exact across its complete 25-word, 100-byte retail span
at `0x15121C00..0x15121C64`.

The fresh linked matcher reports 2,881 / 5,466 (52.71%) exact C functions
overall and 2,307 / 4,790 (48.16%) in Game, with one address-drift blocker and
2,584 genuinely different C rows overall.

## Recovery

The function forwards the object's float at offset `0x37C`, an embedded pointer
at `0x8C0`, two selected incoming floats, a fifth stack float, and the object's
float at `0x7B4` to `func_15049688`. The incoming middle float is intentionally
unused but remains part of the typed ABI and retail argument spill schedule.

After the call, the function multiplies the updated `0x37C` field by
`D_800A3430` and stores the result at object offset `0x39C`. The complete call
frame, floating-point transfers, constant relocation, multiply, and return
delay slot emit directly from semantic C. No expected-word guards or compiler
override are required.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x161C00` and the
pristine retail span at `conker/conker.us.bin` offset `0x14F0B0` compare equal
across all 100 bytes. Both have SHA-256:

`4870ffbcaf17797a8b7cbfa8aacaa74724de01c62edf8582634671fe365cae45`

## Validation

The focused replacement build, linked matcher, outer ROM build, project tool
checks, all nine focused Python tests, direct byte comparison, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 28-word Game `func_1512D2F8`, currently at 25
real differences. Keep the smaller documented special and near-match rows, the
Init SDK cache routines, address-drift-blocked `func_10012588`, and the larger
parked HUD renderers in their existing lanes.
