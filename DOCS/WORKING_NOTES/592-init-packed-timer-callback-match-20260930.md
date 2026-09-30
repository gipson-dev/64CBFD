# Init packed-timer callback match

Date: 2026-09-30

`func_1000EDA0` occupies 52 words and 208 bytes at
`0x1000EDA0..0x1000EE70`. Its recovered seven-argument callback signature
exposes the `u16` update/output pointer passed in the seventh ABI slot instead
of the former empty five-argument `void` placeholder.

The routine reads the packed value at record offset `0x18`, retaining its
signed low-half timer. A nonzero caller update replaces the packed high half,
clears the record and caller output halfwords, and reloads the packed value.
The low-half timer then decreases by `D_800BE9E4`. A positive result is merged
back into the packed word; an expired result copies the high half to both
outputs and calls `func_10010630` with the record's identifier, owner,
parameter, signed halfword, and unsigned halfword fields.

Forty-one of the 52 words emit directly from semantic C. Eleven stale-checked
guards preserve one closed temporary-register rotation across the high-half
mask, timer merge, expiry output stores, and final callback arguments. The
40-byte frame, saved-`s0` lifetime, seven-argument ABI, branches, delay slots,
call relocation, and return values require no normalization.

The focused object build, exhaustive guarded relink, authoritative matcher,
and direct section-span comparison pass. The linked Init section and pristine
image share SHA-256
`886bdb392b620bfbe0696c157098759fb4be73d307ceaabcf1ab4c3e9bd3f72b`
across all 208 bytes.

The matcher advances to `3,090 / 5,457 (56.62%)` overall and
`407 / 488 (83.40%)` in Init, with zero address drift and 81 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
