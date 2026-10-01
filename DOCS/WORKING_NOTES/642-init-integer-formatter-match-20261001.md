# Init integer formatter match

Date: 2026-10-01

`_Litob` occupies 168 words and 672 bytes at
`0x100230F0..0x10023390`. The existing C already expressed the broad SDK
algorithm, but the recovered wide format-code ABI and resulting compiler
schedule still left 158 of the retail words different.

The recovered routine selects the lowercase or uppercase digit table and the
octal, decimal, or hexadecimal radix from the format code. Signed decimal
formats convert a negative input to unsigned magnitude. The routine emits the
least-significant digit first into a 24-byte reverse buffer, repeatedly divides
the remaining 64-bit value with `lldiv`, copies the completed digit run to the
formatter destination, and derives precision and zero-padding widths.

Retail treats the incoming format code through its unsigned low byte while
retaining the wide ABI value. Expressing that behavior with an `int` parameter
and explicit unsigned-byte comparisons restores the correct semantics and the
168-word slot extent. The remaining mismatch is one closed IDO allocation and
scheduling cycle rooted in retail's compiler-generated parameter-home spill.

Ten linked words emit directly from semantic C. One hundred fifty-seven
stale-checked rows normalize the other 158 retail words; the final row uses a
guarded `insert_after` for retail's `jr` delay-slot stack restore. Relocation-
aware rows move both digit-table address pairs and the `__ull_rem`,
`__ull_div`, `lldiv`, and `memcpy` calls without embedding linked addresses.

An authoritative linked matcher pass classifies the complete function
byte-exact. The linked and retail 672-byte spans share SHA-256
`ec1902fca7a676159f2cd92ce58465dd9c03c1c0e0c7831d2301b6d2dfb09f04`.

The checkpoint is `3,141 / 5,457 (57.56%)` overall and
`458 / 488 (93.85%)` in Init, with zero address drift and 30 genuinely
different Init C rows. The next unparked Init candidate by size is
`func_1000C530` at 174 words, followed by the two 180-word rows
`func_100052A0` and `func_10011BB8`.
