# Game slot-cursor allocation match - 2026-09-26

## Result

All 19 words of `func_150356C8` now match retail across
`0x150356C8..0x15035714`. The linked matcher reports `2611 / 5484 (47.61%)`
overall and `2043 / 4795 (42.61%)` game, with one address-drift blocker and
2,872 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine rejects slot count fifteen, increments `D_800C3F00`, and returns
the previous 12-byte record in `D_800C3F08`. Reusing the loaded `val` local
with `val++` makes IDO keep the cursor in retail's `a0` and restores the final
byte store. This reduced the mismatch from thirteen to nine words while
preserving the 19-word extent, zero-return path, and branch structure.

Explicit cursor-pointer locals, including `register` spelling, made IDO
rematerialize the cursor for the store and grew the function to 20 words. A
`volatile` cursor also overflowed the slot. A `register` next-value local and
declaration reordering reproduced the original object. `next = ++val`
reproduced the accepted `val++` object but added no useful source clarity, so
it was rejected.

Nine expected-word guards restore the remaining independent register and
scheduling choices. Retail increments in the branch delay slot through `t6`,
narrows through `t7`, forms the 12-byte stride in `t8`, selects the previous
record offset in `t9`, and retains the table address in `t0`. The
`D_800C3F08` `R_MIPS_HI16` stays at relative `0x10` while changing from `t9`
to `t0`; the paired `R_MIPS_LO16` moves from relative `0x18` to `0x38`. All
other words are source-emitted and exact.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x62B48` and pristine
retail `conker/conker.us.bin+0x62B78` are byte-identical for 76 bytes and share
SHA-256
`ce94daa79799e73dfcc4b67025fc8e51fcb016d97ee6964f07a39a20f6c3b44c`.
The patch table contains 790 rows, zero duplicate keys, and nine rows for this
function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 18-word `func_15043B70`, now the first game row with thirteen
real differences. It consumes a remaining count in chunks capped by the gap
between `arg1` and `arg2`, advances `arg2`, and returns zero once the boundary
is reached. Compare its loop branch direction, selected-chunk lifetime, and
zeroing path against retail before introducing guarded words.
