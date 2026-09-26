# Game delimiter-split match - 2026-09-26

## Result

`func_1516A770` is byte-exact across all sixteen words at
`0x1516A770..0x1516A7B0`. The linked matcher reports
`2627 / 5483 (47.91%)` overall and `2059 / 4794 (42.95%)` game, with one
address-drift blocker and 2,855 total differing C functions. Debugger remains
complete at `181 / 181`.

## Recovered behavior

The former C body returned zero. Retail instead scans a zero-terminated byte
string and replaces every `0xBD` delimiter with zero in place. The return
value begins at one and increments only when a delimiter is replaced, so it
reports the number of resulting fields rather than the number of traversed
bytes.

Expressing the scan through repeated `*arg0` reads gives IDO the retail
register lifetimes: the current byte remains in `v0`, the `0xBD` constant in
`a1`, and the field count in `v1`. The compiler also reproduces both
branch-likely next-byte loads, the conditional count update, pointer advance,
and shared return epilogue directly. No guarded word rows are required.

## Evidence

The final linked and pristine 64-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x197BF0`
- retail `conker/conker.us.bin+0x197C20`
- SHA-256 `059a7d6e9e7166f4c154face31ebe5ddfbbfb064c34253e110bafa6ea0bf10d2`

The focused generated object build, full nonmatching link, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation declarations and
calls for this function, with no separately maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 16-word `func_1518F45C`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It builds a one-word stack record
from `D_800A74D4` and forwards that record, a count of one, and its narrowed
arguments to `func_15169260`; its current C body is behaviorally complete but
does not yet preserve retail's argument-home and call schedule.
