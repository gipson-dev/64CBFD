# Game selector display-list appender byte match

Date: 2026-09-30

`func_15183BA4` occupies 33 words and 132 bytes at
`0x15183BA4..0x15183C28`. It scans the 11 selector bytes at `D_800A72D0`,
retains `-1` when no selector matches, and uses a successful index to read the
corresponding display-list pointer from `D_800DDF78`. A null pointer leaves the
output cursor unchanged; a non-null pointer appends one `G_DL` command and
returns the advanced cursor.

The recovered fixed four-argument contract types the unused third and fourth
arguments as signed halfwords. IDO therefore emits their required o32 argument
home stores at `sp+0x08` and `sp+0x0C` without allocating a frame. The bounded
selector loop then emits directly from the indexed C scan, including retail's
branch-likely increment and early-exit schedule.

Using the SDK's original `gSPDisplayList(dl++, *entry)` macro is the final
source-level match. Its post-increment expansion snapshots the output cursor in
`v0`, writes command `0xDE000000`, rereads the selected pointer, advances `a0`,
and writes the pointer through the retained cursor exactly as retail does.

All 33 words emit directly from semantic C with no expected-word guards or
compiler-profile override. The focused object, complete relink, outer ROM
build, and authoritative matcher pass. The linked ELF and pristine
decompressed retail spans share SHA-256
`0eb643956a1f00342d1e746734b5b8127d7b84832163a0a6c9e3a90250dcb046`.
The matcher advances exactly one row to `3,064 / 5,462 (56.10%)` overall and
`2,485 / 4,788 (51.90%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_1518AADC`, the next ordinary matcher row.
