# Init object-aware audio dispatch match

Date: 2026-10-01

`func_10010FFC` occupies 115 words and 460 bytes at
`0x10010FFC..0x100111C8`. Its former zero-return placeholder discarded an
object-aware audio request used by the adjacent Init audio interface.

The restored function first narrows the incoming handle to 16 bits and rejects
a null object or an object whose `interaction_state` is zero. When the object
has a camera, it forwards the original volume directly to `func_10010BE8` with
mode `0x40`, the caller's signed and byte parameters, and `D_80041FD9`.

The non-camera path reduces the requested volume to three quarters. For an
object ID other than `0xFF`, it multiplies the unsigned `unkE` field from
`D_800D1C90[id]` by the object's `xz_scale`; ID `0xFF` starts from zero. Values
above 256 map to `1.0`, values below 80 map to `0.3125`, and intermediate
values are divided by 256. The function then calls `func_10010E78` with the
reduced volume, the object's three truncated position coordinates, a fixed
lower range of 500, and an upper range of `trunc(2000 * scale) + 501`.

The semantic C recovers the complete 115-word extent, 0x40-byte frame, saved
register set, branch topology, constants, unsigned integer-to-float sequence,
and both call contracts. IDO retains the narrowed handle through a stack home
instead of retail's opening register lifetime. That one scheduling distinction
displaces most subsequent integer allocation even though the floating-point
sequence and control-flow boundaries remain equivalent. One hundred four
relocation-aware, stale-checked guard rows normalize those compiler-only words,
including movement of the two calls and the `D_800D1C90` address pair. Eleven
words emit directly from semantic C.

The exhaustive padded-object rebuild and complete ELF link passed. The
authoritative matcher no longer lists `func_10010FFC`; a direct comparison of
all 460 bytes reports zero differences, and the linked and retail spans share
SHA-256
`f082d41b929c07fc57b6645669c3e923b7ff3a20be2696b0d2379e0a26ffce7d`.
The project test suite also passes all 10 tests, with 8 expected skips.

The matcher advances to `3,123 / 5,457 (57.23%)` overall and
`440 / 488 (90.16%)` in Init, with zero address drift and 48 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
