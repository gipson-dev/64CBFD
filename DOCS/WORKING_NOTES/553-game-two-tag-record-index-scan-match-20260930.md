# Game two-tag record index scan byte match

Date: 2026-09-30

`func_1511A410` occupies 33 words and 132 bytes at
`0x1511A410..0x1511A494`. It scans signed tags at the start of eight-byte
records, stopping at sentinel `-0x21` or after finding two records tagged
`-3`. It returns the first matching record index and writes the second index
through its output pointer. Both results remain zero when their corresponding
match is absent.

Retail reserves three local scratch words although the scan retains at most
two indices; preserving that object reproduces the `sp+0x0C` and `sp+0x10`
slots and the complete 24-byte frame. Twenty words emit directly from the
semantic C. Thirteen stale-checked guards move IDO's loop-invariant scratch
base into retail's match-only schedule and normalize the resulting closed
temporary-register chain and retry-branch target. They do not alter the scan,
sentinel, stores, result values, or function extent.

The matcher advances by exactly one row to `3,056 / 5,462 (55.95%)` overall
and `2,477 / 4,788 (51.73%)` in Game with no address drift. The linked
132-byte Game span has SHA-256
`c9f324d509e8a4e3282456e941568a37a88c4b1e6dc32ae7d04bbe8c52384c67`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
34-word Game `func_1511A738`, the next ordinary matcher row.
