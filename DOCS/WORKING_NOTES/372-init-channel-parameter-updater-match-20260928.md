# Init channel-parameter updater match - 2026-09-28

## Result

`func_1000CBF0` is byte-exact across the complete 25-word, 100-byte retail
span at `0x1000CBF0..0x1000CC54`.

The fresh linked matcher reports 2,870 / 5,466 (52.51%) exact C functions
overall and 393 / 495 (79.39%) in Init, with 2,595 genuinely different C rows
overall and 101 in Init.

## Recovery

The function walks the three entries in `D_800417B0` selected by `arg2`. For
each selected nonnull entry, it writes `arg0` to `unk5A` and `arg1` to
`unk5C`; when the full 32-bit `arg1` is zero, it also copies `arg0` to
`unk58`.

The placeholder used `s16` for the first two parameters. IDO therefore emitted
six entry words to truncate and sign-extend the ABI arguments, overflowing the
fixed retail slot and causing the padding tool to install a trampoline. Retail
uses the incoming 32-bit values directly and truncates only at each halfword
store. This also matters semantically: a nonzero `arg1` whose low 16 bits are
zero must not take the `unk58` update path.

The placeholder also cached `D_800417B0[i]`. Restoring direct table access for
each assignment reproduces retail's three pointer loads, register allocation,
branch-likely delay slots, and rolled loop. All 25 words compile directly with
no expected-word guards.

## Verification

The focused object build, complete link and fresh matcher pass succeed. The
refreshed rebuilt span at `build/conker.us.init.code.bin+0xBBF0` and pristine
retail span at `conker.us.bin+0xCBF0` compare equal across all 100 bytes. Both
have SHA-256:

`b05d76b390a3fd15235dbd4a530f255c0290734cae3ab4d4b20745179a6314a4`

The replacement build, outer-ROM build, project-tool checks, all nine focused
Python tests and whitespace validation also pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified or launched.

## Next boundary

Audit ordinary 28-word Init `func_10003BD0`, now the smallest unblocked
project-owned Init row at 25 real differences. The tied `osInvalICache` and
`osWritebackDCache` rows are SDK cache routines; the smaller 17-word
`func_10012588` remains blocked on address drift.
