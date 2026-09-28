# Game byte-timer state match - 2026-09-28

## Result

`func_1512D2F8` is byte-exact across its complete 28-word, 112-byte retail span
at `0x1512D2F8..0x1512D368`.

The fresh linked matcher reports 2,882 / 5,466 (52.73%) exact C functions
overall and 2,308 / 4,790 (48.18%) in Game, with one address-drift blocker and
2,583 genuinely different C rows overall.

## Recovery

The function dispatches on the byte state at object offset `0x84D`. State `1`
clears the timer byte at `0x84E` and advances to state `2`. State `2` adds the
global tick delta `D_800BE9E4` to that byte and clears the state when the
truncated timer reaches `D_800DC290[index]`, where the index is the word at
offset `0x850`. Other states return unchanged.

An explicit `switch` reproduces retail's two forward equality branches and
immediate default return. Expressing the timer update as compound assignment to
the `u8` field preserves the promoted sum through its byte store and unsigned
comparison, yielding retail's `t7/t8/t9` lifetime. All 28 words emit directly
from semantic C, with no expected-word guards or compiler override.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x16D2F8` and the
pristine retail span at `conker/conker.us.bin` offset `0x15A7A8` compare equal
across all 112 bytes. Both have SHA-256:

`7c7474bd53426dc3bd1b762af24722efa1c56b155158869c3545ce71d1a451f5`

## Validation

The focused replacement build, linked matcher, outer ROM build, project tool
checks, all nine focused Python tests, direct byte comparison, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_1512D604`, currently at 25
real differences. Keep the smaller documented special and near-match rows, the
Init SDK cache routines, address-drift-blocked `func_10012588`, and the larger
parked HUD renderers in their existing lanes.
