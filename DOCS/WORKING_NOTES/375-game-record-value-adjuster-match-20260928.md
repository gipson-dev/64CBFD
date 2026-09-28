# Game record-value adjuster match - 2026-09-28

## Result

`func_15034EB4` is byte-exact across its complete 27-word, 108-byte retail
span at `0x15034EB4..0x15034F20`.

The fresh linked matcher reports 2,873 / 5,466 (52.56%) exact C functions
overall and 2,299 / 4,790 (48.00%) in Game, with one address-drift blocker and
2,592 genuinely different C rows overall.

## Recovery

The routine returns without changing records when signed global
`D_800C3EF0` is zero. Otherwise it converts that scale to `f32`, multiplies it
by `D_80097D60` and the owner multiplier at offset `0x14C`, then subtracts the
result from field `0x34` of a 0x40-byte indexed record reached through owner
offset `0x1D4`. It repeats the subtraction for the second index unless that
index is `-1`.

The previous body was a zero-return placeholder. The recovered semantic C
emits 26 of the 27 retail words directly. At function offset `0x48`, IDO emits
`mul.s f0,f16,f10` (`0x460A8002`) while retail uses the mathematically
equivalent `mul.s f0,f10,f16` (`0x46105002`). A single expected-word guard
records and normalizes only that commutative operand order. The guard table now
contains 1,661 rows with zero duplicate keys.

## Verification

The linked span at `build/conker.us.elf` file offset `0x74EB4` and pristine
retail span at `conker.us.bin` offset `0x62364` compare equal across all 108
bytes. Both have SHA-256:

`01814b1b5a158ba63f14570ed41dfa6bd164582897d02ecc8122135d4342f716`

The focused object build, linked matcher scan, replacement build, outer-ROM
build, project tool checks, all nine focused Python tests, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Audit ordinary unparked 27-word Game `func_1507F454`, now the first ordinary
candidate in the 25-real-difference tier. `func_10003BD0` remains open after a
source-shape audit whose experiments were removed. Keep `osInvalICache` and
`osWritebackDCache` in the Init SDK ownership lane and keep smaller documented
special cases in their existing lanes.
