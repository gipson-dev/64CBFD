# Game handwritten absolute-ordering helper restoration

Date: 2026-09-30

`func_150AD9A0` occupies 32 words and 128 bytes at
`0x150AD9A0..0x150ADA20`. It converts its three signed inputs to magnitudes,
orders those magnitudes with branch-delay XOR swaps, and combines them into
the integer approximation consumed by distance and spatial callers.

The routine was still represented by a zero-return C placeholder even though
the source already classified this slice and its three following math/PRNG
helpers as original handwritten assembly. Its strict source-order register
reuse, explicit trapping `sub`/`add`, filled branch and return delay slots,
and adjacency to the handwritten 64-bit PRNG routines support that ownership.
The existing retail assembly body is now included through `GLOBAL_ASM`.

The linked body matches all 32 retail words. Linked Game offset `0xAD9A0` has
SHA-256 `4a4f0a1e59e72bbf4c79d7209381c926f46563f59a94c9b2456f36e58382b620`.
Because this is an ownership correction rather than a C match, the exact
numerator remains 3,049 while the C denominator drops to 5,462; Game remains
2,470 exact with a denominator of 4,788. Address drift remains zero.

Keep the documented ownership/compiler-boundary rows parked. Resume with
35-word Game `func_150DEACC`, the next ordinary matcher row.
