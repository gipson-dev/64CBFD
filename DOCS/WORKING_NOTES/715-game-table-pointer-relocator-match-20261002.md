# Game table-pointer relocator match

Date: 2026-10-02

`func_1503D484` replaces its zero-return placeholder with the 35-word retail
routine at `0x1503D484..0x1503D510`. Its input is a sentinel-terminated table
of eight-byte records.

The function advances until the unsigned halfword at the start of a record is
`999`. For every preceding record whose word at offset `0x4` is nonzero, it
passes that word to `func_1503D438` with the table base. The already-matched
helper adds the base only when the stored value is nonzero and has a clear top
nibble, preserving values that are already absolute or otherwise tagged.

After reaching the sentinel, the routine divides the nonnegative byte distance
from the table base by eight and writes the resulting record count to
`D_800C5A90[arg1]`. Advancing the incoming pointer directly preserves retail's
`s0` cursor and `s1` base lifetimes; expressing the division as an arithmetic
right shift preserves its known nonnegative count calculation without IDO's
general signed-division correction.

The complete function emits directly from semantic C with no expected-word
guards, checked insertions or omissions, relocations, or compiler-profile
override. The exhaustive `NON_MATCHING=1` rebuild and linked matcher pass with
zero address drift. The linked and retail 140-byte spans are identical, with
SHA-256:

```text
4714bad5a07ebceff4a37418ab06e7739eaf2877c1024ac67e4676d55baa79a1
```

Game advances to `2,555 / 4,788 (53.36%)`, with 2,233 different C rows;
overall byte-exact C progress is `3,223 / 5,456 (59.07%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`.
`make tools-check` also passes. No fresh gameplay run was performed.

Resume the ordinary small-Game queue with adjacent 36-word `func_1503D774`,
currently at 35 real differences. Keep `func_15015F40` parked behind unresolved
indirect-table ownership and `func_150A76F0` in the handwritten
register-contract workstream.
