# Init active entry mode dispatcher match

Date: 2026-09-30

`func_1000E2F4` occupies 70 words and 280 bytes at
`0x1000E2F4..0x1000E40C`. The former zero-return placeholder is replaced with
the recovered three-entry sound-state scan and mode update.

The routine visits each non-null `D_800417B0` entry whose identifier is
positive and whose state byte is zero. In nonzero mode it clears the entry's
channel value through `func_10008EE0` and conditionally calls
`func_10008F58` when metadata flag `0x10` is clear. In zero mode it
conditionally calls `func_100084D8`, sets the entry's cached value to `-1`,
and recomputes the channel through `func_1000CC54`. It finishes by storing the
mode byte in `D_80041F00`.

The metadata flag uses retail's 32-bit read at offset four of the 16-byte
`D_8002B074` record. The recovered C preserves that width explicitly instead
of changing the shared placeholder struct, whose fields are currently split
into halfwords.

Fifty-eight of 70 words emit directly from semantic C, including the complete
frame, branch-likely loop, all four call relocations, delay slots, and global
relocations. Twelve function- and offset-scoped guards normalize one closed,
non-relocating temporary-register allocation cycle across the two metadata
tests. No words are inserted or removed.

The exhaustive stale-guard rebuild, authoritative matcher, and direct
section-span comparison pass. The linked Init section and pristine image
share SHA-256
`9c7c8f921694c0fed12dc7ca5c311ccc242df93cb2ad3d55e9ad76300ff911d0`
for the complete function.

The matcher advances to `3,102 / 5,457 (56.84%)` overall and
`419 / 488 (85.86%)` in Init, with zero address drift and 69 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
