# Game byte-table index lookup match

Date: 2026-09-30

`func_15041480` occupies 34 words and 136 bytes at
`0x15041480..0x15041508`. It narrows its argument to an unsigned byte and scans
the 80-byte table at `D_800848D0`, returning the first matching index. When no
entry matches, it returns the table bound, 80.

Retail checks four adjacent bytes per iteration. Expressing those four checks
explicitly recovers the branch-likely chain, early-return delay slots, running
index, advancing table pointer, and four-byte loop stride. Default IDO
`-O2 -g3` recognizes and doubles that source loop into eight checks, expanding
the body from 34 to 54 words. The object-specific `-Wo,-loopunroll,0` profile
preserves retail's four-way form.

All 34 words emit directly from semantic C. The unsigned argument
normalization, table relocation, four byte loads, four immediate returns,
80-entry bound, pointer update, absent-value return, and trailing return delay
slot match without expected-word guards.

The focused object, exhaustive profile-dependent object rebuild, complete
relink, authoritative matcher, direct span comparison, outer `NON_MATCHING=1`
build, project tool checks, and whitespace check pass. The linked ELF and
pristine decompressed retail spans share SHA-256
`dffbcfa8fd45b23a77815de868084b779498276451ac20ede147c70a42466fc1`.
The matcher advances exactly one row to `3,072 / 5,461 (56.25%)` overall and
`2,493 / 4,788 (52.07%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_15076768`, the next ordinary matcher row.
