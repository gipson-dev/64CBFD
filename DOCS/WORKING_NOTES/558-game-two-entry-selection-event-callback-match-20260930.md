# Game two-entry selection event callback byte match

Date: 2026-09-30

`func_15158B3C` occupies 37 words and 148 bytes at
`0x15158B3C..0x15158BD0`. Its byte-typed operation selects one of two records
or clears the current selection. Operation `0x2D` compares the current pointer
at object offset `0x40` with both record pointers, switches to the other
pointer, and copies the corresponding selector byte to offset `0x44`.
Operation zero clears the pointer and selector when either the first record
pointer or the byte at record offset `0x4` identifies the current selection.
Other operations and unrelated records leave the selection unchanged.

The recovered callback signature preserves the byte argument's retail entry
spill and truncation while making the routine's non-value-returning contract
explicit.
Twenty-six words emit directly from semantic C. Ten expected-word guards
normalize an 11-word closed compiler difference: retail leaves the successful
second-record return delay slot empty, shifting the zero-operation block by
one word, and uses a `v0`/`t1`/`t2`/`t3` temporary cycle where IDO chooses
`t1`/`t2`/`t3`/`t4`. No data access, predicate, or side effect is synthesized
by the guards.

The matcher advances by exactly one row to `3,061 / 5,462 (56.04%)` overall
and `2,482 / 4,788 (51.84%)` in Game with no address drift. The linked
148-byte Game span has SHA-256
`f6f19275e72e485804598ba595d662c7522ed0f876312a865749ff013dad34e5`.

Keep the documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_1516441C`, the next ordinary matcher row.
