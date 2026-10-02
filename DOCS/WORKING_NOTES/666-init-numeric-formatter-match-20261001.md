# Init numeric formatter match

Date: 2026-10-01

`func_10001AA8` occupies 370 words and 1,480 bytes at
`0x10001AA8..0x10002070`. Its former C placeholder returned zero and omitted
the numeric layout stage called by `func_10001550` after digit generation and
rounding.

The recovered routine emits fixed notation for `%f` and for `%g`/`%G` values
whose exponent falls in the retail fixed-format window. It adjusts precision,
places leading zeroes and the decimal point, copies available significant
digits, and records deferred leading or trailing zero counts in the formatter
state. Retail's unusual decimal bookkeeping in the short-digit branch is
preserved exactly.

Outside that window, the routine converts general format to `%e` or `%E`,
emits the first significant digit and optional fractional digits, then writes
the exponent marker, sign, and a two-to-four-digit decimal exponent. Its final
path computes deferred field-width padding when the relevant alignment flags
are active. The old-style declaration is retained because the matched caller
uses the original default argument promotions; changing it to a modern narrow
prototype perturbs the already matched caller.

IDO emits a 365-word compact body from the semantic C. Eighty-seven words
already match retail directly. The remaining closed frame, allocation,
branch-shape, and scheduling difference is represented by 278 function-scoped,
stale-checked rows. Thirteen rows insert retail scheduling words, eight omit
compact-only words, and three validate relocation movement.

The padded-object and linked builds pass, and the matcher no longer lists
`func_10001AA8`. Direct comparison of `0x10001AA8..0x10002070` reports zero
different bytes. Both 1,480-byte spans share SHA-256
`d34588b845730b80b2a13a9bdaf75c284a2ad8f0bb718fb73cbc08fb1968243e`.

The matcher advances to `3,164 / 5,456 (57.99%)` byte-exact C functions
overall and `481 / 487 (98.77%)` in Init, with zero address drift and six
different Init rows. The next smallest measured Init candidate is the
402-word `func_100020D0`, currently different in 399 words.
