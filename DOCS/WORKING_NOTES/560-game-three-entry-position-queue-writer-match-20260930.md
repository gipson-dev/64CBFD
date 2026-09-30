# Game three-entry position queue writer byte match

Date: 2026-09-30

`func_1517D578` occupies 33 words and 132 bytes at
`0x1517D578..0x1517D5FC`. It reads the byte count at `D_8008CEB0` and does
nothing once three records are present. Otherwise it selects one 16-byte entry
from `D_800DDD28`, stores three signed coordinates, a byte selector, two
trailing halfwords, and one float, then increments the count.

The recovered seven-argument contract preserves the three signed-coordinate
narrowings and the seventh argument's big-endian byte home at `sp+0x1B`.
Explicit coordinate lifetimes make IDO emit the correct 33-word extent and
retail control flow. The remaining difference is one closed compiler
allocation cycle: retail moves the float first, retains the count address in
`a3`, and forms the selected entry in `v1`; IDO schedules the narrowings first
and rotates those pointers and dependent temporaries through `t0`, `t3`,
`t4`, and `a3`.

Four words emit unchanged from semantic C. Twenty-nine stale-checked guards
normalize that schedule and allocation cycle. The two moved relocations retain
their original `D_8008CEB0` and `D_800DDD28` targets, and no branch target,
predicate, loaded argument, record offset, value, or side effect is changed.

The focused object, complete relink, outer ROM build, and authoritative matcher
pass. The linked ELF and pristine decompressed retail spans share SHA-256
`71f575144e94e2e3cac83b62e3e197e36edfa34d7c1ad864f439cb942be99e01`.
The matcher advances exactly one row to `3,063 / 5,462 (56.08%)` overall and
`2,484 / 4,788 (51.88%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_15183BA4`, the next ordinary matcher row.
