# Game float-record update match - 2026-09-26

## Result

`func_1518F89C` is byte-exact across all seventeen words at
`0x1518F89C..0x1518F8E0`. The linked matcher reports
`2631 / 5483 (47.98%)` overall and `2063 / 4794 (43.03%)` game, with one
address-drift blocker and 2,851 total differing C functions. Debugger remains
complete at `181 / 181`.

## Source and schedule

The function samples `func_150ADA68`, computes
`object[0x30] = sample * object[0x40] + object[0x3C]`, then calls
`func_1518F8E0(object)`. The byte-pointer source expressed that behavior but
let IDO dissolve the common `object + 0x30` pointer and select a different
floating-point register and operand schedule.

A `FloatUpdate1BA1D0` record names the value, base, and scale fields. That
source shape recovers retail's `f4` scale, `f8` base, `f6` product, and `f10`
result allocation. A pointer-to-volatile probe produced the same object and
was rejected in favor of the ordinary typed pointer.

IDO still stores the object in the first call delay slot, dissolves the record
base, commutes the multiply operands, and schedules the second call too early.
Twelve stale-guarded rows move both call relocations, retain the field base in
`v0`, restore the FP operations, and shift the epilogue. One guarded insertion
after compact offset `0x0C` restores retail's explicit first-call delay `nop`;
the final retail delay `nop` comes from the existing slot padding.

## Evidence

The final linked and pristine 68-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1BCD1C`
- retail `conker/conker.us.bin+0x1BCD4C`
- SHA-256 `5f7e34a4ac1ba1b56e1d13de47a39512e6935234606e7a12141f5aeb301270f5`

The patch table contains 879 rows, twelve for this function, and no duplicate
`(filename, function, offset)` keys. The focused object build, exhaustive
nonmatching rebuild, fresh direct matcher, outer build, and project tool checks
passed.

The `64CBFDOGL` sibling contains only generated recompilation declarations for
this function, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 17-word `func_151A561C`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It is the same one-word aggregate
forwarder shape already solved for `func_1518F45C`, but sources its record from
`D_800A8D70`; test the aggregate local and `void *` callee contract first.
