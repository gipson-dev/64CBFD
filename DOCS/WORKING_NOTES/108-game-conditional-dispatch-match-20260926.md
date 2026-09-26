# Game conditional dispatch match - 2026-09-26

## Result

`func_1518F858` is byte-exact across all seventeen words at
`0x1518F858..0x1518F89C`. The linked matcher reports
`2620 / 5483 (47.78%)` overall and `2052 / 4794 (42.80%)` game, with one
address-drift blocker and 2,862 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

The function reads the signed byte at object offset `0x89`. A value of `-1`
returns immediately; every other value indexes the callback table at
`D_8008D680` and invokes the selected function.

The generated C originally expressed the operation as a positive `if` and
read through an ordinary pointer. IDO reused one load in `v0`, formed the table
address before the branch, and emitted a normal branch into a shared epilogue.
An explicit early return through a volatile signed-byte pointer reproduces
retail directly: `t6` holds the first test, `t7` receives the second load,
`t8` holds the scaled index, and the early `$ra` restore fills the `beql` delay
slot. The table relocation sequence, indirect call, and common epilogue then
match without guarded word patches.

The object build, full non-matching link, fresh matcher, outer build, and
project tool checks passed. Linked `conker/build/conker.us.bin+0x1BCCD8` and
pristine retail `conker/conker.us.bin+0x1BCD08` are byte-identical for 68 bytes
and share SHA-256
`3e7c845da43fd38459e5396305f94fc0425fb79a84c1e68d2d98228cbc382587`.
The patch table remains at 823 rows with zero duplicate keys and no rows for
this function.

The `64CBFDOGL` sibling contains recompilation metadata and a stub declaration
for this address, but no maintained host implementation to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 17-word `func_1519072C`, now the first game row with thirteen
real differences. Its generated C builds a stack record containing the input
pointer and byte `0x3B`, then passes that record to `func_151D343C` and
`func_1518F45C`. Compare the current object against retail's retained `a2`
lifetime, local-pointer spill at `sp + 0x1C`, and call scheduling.
