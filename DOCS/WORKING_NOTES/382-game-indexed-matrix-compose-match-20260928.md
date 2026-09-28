# Game indexed matrix compose match - 2026-09-28

## Result

`func_15110360` is byte-exact across its complete 26-word, 104-byte retail span
at `0x15110360..0x151103C8`.

The fresh linked matcher reports 2,880 / 5,466 (52.69%) exact C functions
overall and 2,306 / 4,790 (48.14%) in Game, with one address-drift blocker and
2,585 genuinely different C rows overall.

## Recovery

The function forwards its output matrix and three floating-point arguments to
`func_151102CC`. It then selects a `0x180`-byte record from the allocation at
`D_800BE628` and calls `func_150A7A48` with the matrix at record offset `0xBC`,
composing the result in place.

A typed record with an embedded `f32[4][4]` at offset `0xBC` reproduces retail's
base, index, and scaled-offset lifetimes in `t6`, `t7`, and `t8`. Raw integer
pointer arithmetic was semantically equivalent but rotated that three-register
allocation and left seven differing words. The typed array access emits all 26
retail words directly, with no expected-word guards or compiler override.

The empty placeholder for adjacent `func_151102CC` now carries its recovered
matrix-and-three-floats signature so this wrapper uses the retail float ABI. Its
body remains unrecovered and is still independently reported as different.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x150360` and the
pristine retail span at `conker/conker.us.bin` offset `0x13D810` compare equal
across all 104 bytes. Both have SHA-256:

`f4c281be9de95e3c11d54064497fb0852eaf1803bbef9fd39f1afa1ec6685184`

## Validation

The focused replacement build, linked matcher, outer ROM build, project tool
checks, all nine focused Python tests, direct byte comparison, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 25-word Game `func_15121C00`, currently at 25
real differences. Keep the smaller documented special and near-match rows, the
Init SDK cache routines, address-drift-blocked `func_10012588`, and the larger
parked HUD renderers in their existing lanes.
