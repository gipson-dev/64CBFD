# Game record-pointer repeated-field match - 2026-09-26

## Result

All 19 words of `func_150CFBEC` now match retail across
`0x150CFBEC..0x150CFC38`. The linked matcher reports `2616 / 5483 (47.71%)`
overall and `2048 / 4794 (42.72%)` game, with one address-drift blocker and
2,866 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

When `arg2` is `0x52`, the routine updates the record at `arg0 + 0x70`: it
sets flag bit zero, clears the first float, copies `arg0`'s float at `0x10`,
and stores the difference between `*arg1` and a fresh read of that source
field. The original source expressed the record pointer inside the condition,
so IDO folded every access back into `a0`. It also reused the first source
float load for both the copy and subtraction.

Declaring `temp_v0 = arg0 + 0x70` before the condition makes IDO materialize
the pointer in retail's conditional-branch delay slot and retain it in `v0`.
Qualifying the two source-field reads as volatile prevents common-subexpression
reuse. This reproduces retail's distinct `f6` copy load followed by the `f10`
subtraction load, with `*arg1` in `f8` and the result in `f16`.

The argument-byte narrowing, branch, pointer formation, byte flag update, FP
stores, repeated source loads, subtraction, and epilogue are all
source-emitted and exact. No guarded rows or relocations apply.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0xFD06C` and pristine
retail `conker/conker.us.bin+0xFD09C` are byte-identical for 76 bytes and share
SHA-256
`dbdf458a3a3766235455debb74b0a6ddaff00f12354927807aa5baec169d3870`.
The patch table remains at 808 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 16-word `func_15131918`, now the first game row with thirteen
real differences. Inspect its source, current object, and retail words for
ownership and lifetime structure before adding guarded scheduling words.
