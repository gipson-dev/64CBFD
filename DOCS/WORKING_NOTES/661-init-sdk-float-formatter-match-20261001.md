# Init SDK float formatter match

Date: 2026-10-01

`func_10001550` occupies 296 words and 1,184 bytes at
`0x10001550..0x100019F0`. Its former C body was empty even though the retained
assembly implements the SDK `_Ldtob` conversion used by the repository's
`printf` family.

The recovered routine handles `%f`, `%e`, `%E`, `%g`, and `%G`. It normalizes
the requested precision, classifies zero and finite values through
`func_100019F0`, copies the existing `NaN` or `Inf` strings for special values,
and scales finite values with the decimal-power table at `D_8002BF20`.
Eight-digit chunks are generated through `ldiv`, leading zeroes are removed,
and the significant-digit pass applies retail's decimal rounding before
dispatching the final layout to `func_10001AA8`.

The implementation comes from the bundled SDK-family `xldtob.c` source and
the independently recovered debugger `_Ldtob` body. `struct246` now exposes
the formatter's double value, destination, count, precision, width, and flag
fields with their real scalar types. The existing Init read-only addresses are
declared as the powers table, `NaN` and `Inf` strings, zero digit, and `1e8`
constant used by the assembly.

The semantic body compiles to the exact 296-word extent and retains retail's
branches and calls. Its compact object emits 120 words directly. IDO keeps the
unsigned format code in a saved register and chooses a frame eight bytes
larger than the retail SDK object; 176 function-scoped expected-word guards
normalize that closed allocation and frame-layout schedule. Ten rows carry
both expected and replacement relocation metadata for the two helper calls,
`memcpy`, and moved read-only-data references. Plain signed `char`, volatile
parameter, and `-O3` experiments were rejected because they overflowed the
retail slot or changed the control flow and neighboring object profile.

The padded-object build accepts every row. The linked matcher no longer lists
`func_10001550`, while `func_100019F0` remains byte-exact and
`func_10001AA8` retains its previous non-matching status. Direct comparison of
`0x10001550..0x100019F0` reports zero different bytes, and both 1,184-byte
spans share SHA-256
`fade94f3c21abd93ef6e80ac921e889a4577d4e9cd7e0180f0c21dbf37bdcd2b`.

The matcher advances to `3,159 / 5,456 (57.90%)` byte-exact C functions
overall and `476 / 487 (97.74%)` in Init, with zero address drift and 11
different Init rows. The next smallest measured Init candidate is the
300-word `func_1000D96C`, currently different in 294 words.
