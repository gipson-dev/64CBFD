# Game callback-table traversal match - 2026-09-26

## Result

`func_15167010` is byte-exact across all 23 words at
`0x15167010..0x1516706C`. The linked matcher reports 2,650 / 5,483 exact C
functions overall and 2,082 / 4,794 in Game.

## Source correction

The function walks the fixed `struct115` table rooted at `D_8008B4A8` through
the byte bound `D_8008B4A8 + 0x1484`. For every 52-byte record, it reads the
callback at offset `0x18` and invokes it when non-null.

The source now derives `end` from the initialized cursor rather than repeating
the global base expression. IDO still folds that bound into a second absolute
address and allocates only `s0`/`s1`, while retail derives it from `s0`, keeps
it in `s2`, and saves the contiguous `s0`-`s2` register set.

Fourteen guarded rows restore retail's 40-byte frame, saved-register offsets,
table-base `t6` materialization, explicit `s0 + 0x1484` bound in `s2`, loop
comparison register, and epilogue. The last guarded row replaces the compact
frame restore with `jr ra` and inserts retail's 40-byte frame restore in the
delay slot, so the rows affect fifteen words. Both moved `D_8008B4A8`
relocations and both removed relocations are explicit. The patch table now
contains 978 rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0x194490` and retail span
`conker.us.bin+0x1944C0` are both 92 bytes and compare equal. Both hash to:

`42399e3c663dbb084348a140d6b0a36bb3a672da3deade9e86222372154fa49b`

Changing the shared patch table triggered an exhaustive rebuild of its padded
consumers; the linked ELF and objcopy binary completed successfully. The fresh
linked matcher, exact span comparison, outer nonmatching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass.

## Sibling audit

`64CBFDOGL` contains `func_15167010` in generated recompilation outputs and
symbol declarations. The only documentation reference describes the same
callback slot; there is no separate maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Skip handwritten `func_151F892C` and `func_151F8960`. Continue with 34-word
`func_15167D84`, the first ordinary-C row in the fresh smallest-difference
queue. It selects record kind `5` or `0x42`, calls `func_15167A68` with a
payload size of `arg2 + 0x50`, copies `0x38` bytes into the returned record,
and writes the signed byte argument at offset `0x48`; the linked matcher
reports fifteen real differences.
