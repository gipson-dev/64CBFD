# Init sound-slot dispatcher match

Date: 2026-10-01

`func_10010BE8` occupies 164 words and 656 bytes at
`0x10010BE8..0x10010E78`. Its former C body returned zero for every request,
leaving the original sound-handle allocation path unavailable to C callers.

The recovered routine first narrows the incoming handle to 16 bits and uses
its low nibble as the preferred entry in the 16-slot `D_800425E0` table. A
matching nonzero handle reuses that slot, stopping and clearing an active
sound first. A new or stale handle uses the preferred slot when it is inactive
and unreserved; otherwise the routine checks slot zero and then scans slots
one through fifteen for the first inactive entry whose sound flags do not set
bit `0x8000`.

Requests below volume 100, with no available slot, with sound ID zero, or with
a masked sound index at or above `0x6E3` are rejected. A successful allocation
returns the slot's current generation handle, advances that generation by
`0x10` while skipping wrapped values below `0x10`, records the requested sound
flags, and marks an existing sound state with value 5 before replacement.

The effect mix adds unsigned `D_80041FD8` when the low-seven-bit sum remains
below `0x80`; otherwise it saturates those bits through `| 0x7F`. The routine
converts the signed cents argument through `alCents2Ratio` and calls
`func_10017438` with the current bank, masked sound index, volume, pan, pitch,
mix, bus, and the selected slot's sound-state pointer.

The semantic source has the exact 164-word extent. Seventy-nine linked words
emit directly from C. Eighty-five stale-checked rows normalize IDO's remaining
frame layout, register allocation, loop induction, and scheduling differences;
relocation-aware rows preserve the table and sound-state query references.
Six alternate relocation spellings already resolve to the correct linked
bytes and therefore need no guards.

A repository-wide stale-check rebuild and authoritative linked matcher pass
classify the function byte-exact. The linked and retail 656-byte spans share
SHA-256
`3e184b650c03d5c5992a6ac1877b3246acd1a5c3a0a77807fcc6ab86dfdb7d4d`.

The checkpoint is `3,139 / 5,457 (57.52%)` overall and
`456 / 488 (93.44%)` in Init, with zero address drift and 32 genuinely
different Init C rows. The three smaller rows remain parked:
`func_1000FF90` (35 words), `func_1000FEF0` (40), and `func_1000F85C` (48).
The next unparked Init candidates by size are `__osInitialize_common` and
`_Litob`, both at 168 words.
