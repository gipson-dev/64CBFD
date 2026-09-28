# Game state-transition dispatch match - 2026-09-28

## Result

`func_151E4E00` is byte-exact across all 25 words and 100 bytes at
`0x151E4E00..0x151E4E64`. Fresh linked totals are 2,858 / 5,468 (52.27%)
overall and 2,286 / 4,790 (47.72%) in Game.

## Recovered behavior

The function clears `D_8008FDCC`, calls `func_151E557C`, selects mode `3`
through `D_800E0B94`, and clears `D_8008FDA4`, `D_8008FD80`, and
`D_800D2E40`. It then calls `func_1501C730(6, 0x1D, 0, 0, 1)`.

The old body was a false zero-return placeholder. The recovered function is
`void`, matching its state-transition-only behavior.

## Compiler boundary

The literal global-write sequence emits the complete 25-word routine directly.
IDO places the initial halfword clear in `func_151E557C`'s delay slot, retains
the independent mode and clear relocations, writes the fifth dispatch argument
at `sp+0x10`, and emits retail's argument setup and epilogue. No guarded retail
words or relocation substitutions are needed.

The guard table remains at 1,487 rows with zero duplicate
`(filename, function, offset)` keys. No rows belong to this function.

## Exact-byte evidence

The rebuilt span at `build/conker.us.bin+0x212280` and pristine retail span at
`conker.us.bin+0x2122B0` compare equal for all 100 bytes. Both have SHA-256:

`b9e858200c78ed83eab87512429e3b959bd15e9e51b833ce8c5d90ce4e593b74`

The focused object build, exhaustive relink, fresh linked matcher, direct span
comparison, and guard-table integrity audit pass. The broader replacement and
outer-ROM builds, project-tool checks, all unit tests, and the whitespace check
also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Keep the documented smaller compiler and SDK cases parked. Classify 26-word
Game `func_151E7EF8`, the next unparked compact Game row in the fresh linked
queue with 24 real differences, before changing its implementation.
