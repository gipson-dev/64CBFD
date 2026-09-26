# Game optional-pointer call schedule match - 2026-09-26

## Result

All 18 words of `func_150E33CC` now match retail across
`0x150E33CC..0x150E3414`. The linked matcher reports `2605 / 5484 (47.50%)`
overall and `2037 / 4795 (42.48%)` game, with one address-drift blocker and
2,878 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine loads `*arg2`, returns one when it is zero, otherwise calls
`func_1000E7A0(2, value)` and returns zero. The original C emitted the same
behavior in a compact schedule: it kept the pointed value in `a1`, tested it
immediately, and materialized selector two in the call delay slot. Retail
keeps the value in `v0`, materializes selector two before the test, and moves
the value to `a1` in the call delay slot.

Directly dereferencing `arg2` in both expressions emitted the same compact
object. Reusing one result local for the null return and call path caused IDO
to coalesce the value into `a1` and add a final `move v0,a1`. Assigning the
selector through `arg0` before the test also optimized back to the original
schedule. These source probes were rejected and reverted.

Twelve expected-word guards cover the contiguous scheduling cluster at
relative offsets `0x14..0x40`. They select retail's pointed-value register,
selector placement, branches, call-delay move, and epilogue ordering. The
sole `R_MIPS_26` relocation for `func_1000E7A0` is explicitly moved from
relative offset `0x28` to `0x2C`. The five-word frame opening and final
padding `nop` were already exact and remain unguarded.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x11084C` and pristine
retail `conker/conker.us.bin+0x11087C` are byte-identical for 72 bytes and
share SHA-256
`4e11e68c67960b22b570a25feb7aaff4c509e19a21d120d7eb328c4e489d276a`.
The patch table contains 762 rows, zero duplicate keys, and twelve rows for
this function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 20-word `func_15131D4C`, now the first game row with twelve real
differences. It copies the three words at `D_800A37F0` into a stack record and
calls `func_15169260(record, 3, arg0, arg1)`. Retail establishes the outgoing
arguments first, retains the source base in `t6`, and interleaves each source
load with its store through local-record pointer `a0`. Current C retains the
source base in `v0`, batches the loads into `t6`, `t7`, and `t8`, then stores
them. Test aggregate-copy and explicit cursor forms before adding guards;
preserve the 20-word frame and sole call relocation exactly.
