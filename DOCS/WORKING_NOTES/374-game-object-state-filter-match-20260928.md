# Game object-state filter match - 2026-09-28

## Result

`func_15033F70` is byte-exact across its complete 28-word, 112-byte retail
span at `0x15033F70..0x15033FE0`.

The fresh linked matcher reports 2,872 / 5,466 (52.54%) exact C functions
overall and 2,298 / 4,790 (47.97%) in Game, with one address-drift blocker and
2,593 genuinely different C rows overall.

## Recovery

The routine first rejects all work while `D_800C35EA` equals one. Otherwise it
loads the attached-object pointer at caller offset `0x31C` and returns zero for
a null attachment. Attached-object types `0x0C` and `0x16` are excluded. For
all other types, state byte `0x11A` equal to three is also excluded; the
accepted path clears that state byte and returns one.

The previous body was a zero-return placeholder. A local pointer and a single
type-byte lifetime reproduce retail's branch-likely layout, delay-slot loads,
and final state-byte store. IDO also emits retail's unused `arg0` stack spill
naturally. All 28 words compile directly from semantic C; no expected-word
guards or assembly restoration are involved.

## Verification

The linked span at `build/conker.us.elf` file offset `0x73F70` and pristine
retail span at `conker.us.bin` offset `0x61420` compare equal across all 112
bytes. Both have SHA-256:

`52e7d0b4c187ce6e9967c12143188bf08fcaf5788e2587cb3b7c11d133c58b61`

The focused object build, linked matcher scan, replacement build, outer-ROM
build, project tool checks, all nine focused Python tests, and whitespace
validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Audit ordinary unparked 27-word Game `func_15034EB4`, now the first unparked
row in the 25-real-difference tier. `func_10003BD0` remains open at 25 real
differences after a source-shape audit whose experiments were removed. Keep
the tied Init SDK cache rows and smaller documented special cases in their
existing ownership lanes.
