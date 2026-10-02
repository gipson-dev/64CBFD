# Game resource-release family and height predicate match

Date: 2026-10-02

Three related Game resource-release placeholders are now restored and
byte-exact. `func_1514795C` occupies 33 words at
`0x1514795C..0x151479E0`, scans the resource slots at object offsets
`0x3C..0x48`, and releases the trailing slot at `0x4C`.
`func_151571C4` occupies 33 words at `0x151571C4..0x15157248`, scans
`0x104..0x110`, and releases the trailing slot at `0x114`.
`func_15158A20` occupies 33 words at `0x15158A20..0x15158AA4`, scans
`0xE0..0xEC`, and releases the trailing slot at `0xF0`.

Each routine iterates from zero through the inclusive global limit
`D_80082FA0`, calls `func_100043B4(entry, 4)` for each nonzero indexed entry,
and applies the same release to its trailing slot. Their retail frames,
saved-register lifetimes, loop branches, and delay slots all emit directly
from semantic C without expected-word guards or compiler-profile overrides.

`func_15159084` occupies 39 words at `0x15159084..0x15159120`. It masks the
state word at object offset `0x184` to five bits and rejects modes 2 and 3.
For other modes, it returns true when the height at `0x118` equals
`D_800A63A0` and flags at `0x184` contain neither bit `0x02` nor `0x08`.
Otherwise it returns true when that height is below the comparison height at
offset `0x18` or when byte `0x137` is nonzero. A shared result lifetime
reproduces retail's common return path. Thirty-eight words emit directly from
semantic C; one stale-checked expected-word guard preserves only retail's
commutative `c.eq.s` operand order.

The full linked matcher completes with zero address drift and advances Game to
`2,518 / 4,788 (52.59%)`, with 2,270 different C rows. Overall byte-exact C
progress is `3,186 / 5,456 (58.39%)`. Init remains
`487 / 487 (100.00%)` and Debugger remains `181 / 181 (100.00%)`. No fresh
gameplay run was performed; this checkpoint is compiler, link, and linked-word
comparison evidence.

Resume the ordinary small-Game queue with 34-word `func_1516F864`. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten register-contract workstream.
