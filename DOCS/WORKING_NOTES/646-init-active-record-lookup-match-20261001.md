# Init active-record lookup match

Date: 2026-10-01

`func_1000FF90` occupies 35 words and 140 bytes at
`0x1000FF90..0x1001001C`. It searches the active portion of the 0x30-byte
`D_80041FE0` record array and returns the first matching zero-based index.

The recovered predicate requires `unk14` to equal the primary selector.
`unk18` and `unk1C` each accept either an exact selector match or the wildcard
value `-1`, independently. Records carrying bit `0x80` in `unk10` are skipped.
The function returns `-1` when the active count is non-positive or no enabled
record satisfies all three selectors.

The third selector is typed `u32`. Its `0xFFFFFFFFU` wildcard comparison is
bit-equivalent to the retail `-1` test and causes IDO to retain the two
independent sentinel constants visible in the original function. This yields
the exact 35-word branch-likely loop, delay-slot increments, record stride,
and return paths.

Twenty-two words emit unchanged from semantic C. Thirteen stale-checked rows
normalize one closed compiler allocation cycle: the compact object assigns
the record cursor and first two selectors to `a0`, `a3`, and `a1`, while
retail uses `a1`, `a0`, and `a3`. Two guarded rows preserve the HI/LO
relocations for `D_80041FE0`; no instruction is inserted or omitted.

The authoritative linked matcher no longer lists `func_1000FF90`. The linked
and retail 140-byte spans share SHA-256
`eb36532b03f324f494ecc9c6cf7753c062f747d46e2de603413d378c6d5a72d4`.
The repository-wide stale-check build and final link pass. Project tool checks
pass, all 10 focused tool tests pass, and `git diff --check` is clean.

The measured checkpoint is `3,145 / 5,457 (57.63%)` overall and
`462 / 488 (94.67%)` in Init, with zero address drift and 26 genuinely
different Init C rows. The next Init candidate is `func_1000FEF0`, a 40-word
active-record lookup with 40 real linked-word differences.
