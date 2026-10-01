# Init direct PI copy match

Date: 2026-10-01

`func_1000480C` occupies 117 words and 468 bytes at
`0x1000480C..0x100049E0`. The former source was an incomplete commented draft;
the recovered implementation performs the small-transfer direct PI read used
by `func_10004514` instead of falling back to the asynchronous DMA path.

The routine marks direct PI ownership through `D_8003A572`, rounds the byte
count up to an even value, waits for `D_8003A573` and both PI busy bits to
clear, and combines the device address with `D_80000308`. Aligned transfers
copy complete 32-bit words and retain the high halfword for a two-byte tail.
For a device address misaligned by two bytes, the routine first copies the low
half of the preceding word, then uses overlapping high/low halfword stores for
the bulk copy and preserves the final high halfword when required. It clears
the ownership flag on exit and restarts the PI manager thread when
`D_8003A575` is set.

The semantic C compiles to a 113-word body. Three tracked words already
coincide with retail at their final positions. The remaining compiler frame,
saved-register, allocation, relocation, branch, and scheduling displacement is
normalized by 112 stale-checked relocation-aware rows. Two of those rows insert
the missing saved-register reload and stack-frame restore, yielding retail's
115-word body followed by its two padding words.

The complete ELF link passed. The authoritative matcher no longer lists
`func_1000480C`; direct comparison of all 468 bytes reports zero differences,
and the linked and retail spans share SHA-256
`a34d2643235b5ceaf6120ddd09fbfc9b5ecb9f0ab34dcb09d55a081c90f1403e`.
The patch table contains 112 unique source offsets, no duplicate offsets, and
two insertions. Project tool checks pass. The focused unit suite passes all 10
tests, with 8 expected skips.

The matcher advances to `3,127 / 5,457 (57.30%)` overall and
`444 / 488 (90.98%)` in Init, with zero address drift and 44 genuinely
different Init C rows.
