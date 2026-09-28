# Game sequence-state advance match - 2026-09-28

## Result

`func_1507F454` is byte-exact across its complete 27-word, 108-byte retail
span at `0x1507F454..0x1507F4C0`.

The fresh linked matcher reports 2,874 / 5,466 (52.58%) exact C functions
overall and 2,300 / 4,790 (48.02%) in Game, with one address-drift blocker and
2,591 genuinely different C rows overall.

## Recovery

The routine follows the current player pointer `D_800D154C` to its attached
object at offset `0x31C`, then treats bytes `0x5C` and `0x5D` as a sequence ID
and cursor. A zero sequence ID returns success immediately. Otherwise the
cursor advances, selects a byte from `D_80086BA0[sequence]`, and returns zero
while that byte is nonzero. Reaching the sequence's zero terminator clears
both state bytes and returns success.

The previous body was a zero-return placeholder. The semantic C reproduces
the retail control flow, memory accesses, increment, resets, and delay slots.
IDO assigns three short-lived integer registers in a cycle different from
retail. Six expected-word guards preserve retail's equivalent allocation; the
table `lui` and `lw` guards retain their `R_MIPS_HI16` and `R_MIPS_LO16`
relocations for `D_80086BA0`. The guard table now contains 1,667 rows with zero
duplicate keys.

## Verification

The linked span at `build/conker.us.elf` file offset `0xBF454` and pristine
retail span at `conker.us.bin` offset `0xAC904` compare equal across all 108
bytes. Both have SHA-256:

`ea3ed1e81ea5cb90d4a8d41ecdf8d9cf2542fa75a939ab385b3fbcbf32d6820b`

The focused object build, linked matcher scan, replacement build, outer-ROM
build, project tool checks, all nine focused Python tests, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Audit ordinary unparked 27-word Game `func_1509CB68`, now the first ordinary
candidate in the 25-real-difference tier. `func_10003BD0` remains open after a
source-shape audit whose experiments were removed. Keep `osInvalICache` and
`osWritebackDCache` in the Init SDK ownership lane and keep smaller documented
special cases in their existing lanes.
