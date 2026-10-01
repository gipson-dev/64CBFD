# Init common system initializer match

Date: 2026-10-01

`__osInitialize_common` occupies 168 words and 672 bytes at
`0x10022790..0x10022A30`. Its former C body was empty, omitting the platform
setup performed before the rest of libultra and the game begin normal work.

The recovered routine enables the final-ROM state, enables the CPU coprocessor
bit, and configures the floating-point control/status register. It polls the
PIF RAM word until it can read and rewrite the initialization flag, preserving
the retail call to `__osSpRawWriteIo`.

The routine installs the 16-byte exception preamble at the four standard N64
exception-vector addresses, writes back and invalidates the corresponding
cache range, and installs the RDB TLB mapping. It then reads and aligns the
hardware clock rate, applies libultra's three-quarters adjustment using the
canonical unsigned `osClockRate` type, and clears the application NMI buffer
on a cold reset.

Finally, it waits for the PI interface to become idle and probes the 64DD Leo
status register. A present interface sets `D_8002BD20` and installs
`__osLeoInterrupt`; an absent interface clears the flag.

The semantic source uses the retail SDK's `-O1` profile and has the exact
168-word extent. Sixty-nine linked words emit directly from C. Ninety-nine
stale-checked, relocation-aware rows normalize the remaining IDO frame,
register-allocation, exception-copy, clock-store, and MMIO scheduling
differences. The guards preserve calls and all moved global references rather
than embedding linked addresses.

A repository-wide stale-check rebuild and authoritative linked matcher pass
classify the complete function byte-exact. The linked and retail 672-byte spans
share SHA-256
`853e38c0f3d587f1f6e1f70d7fb0c4b640fbfcaf314727d7975b757c1b8dc4e4`.

The checkpoint is `3,140 / 5,457 (57.54%)` overall and
`457 / 488 (93.65%)` in Init, with zero address drift and 31 genuinely
different Init C rows. The next unparked Init candidate is `_Litob`, also 168
words. The smaller `func_1000FF90`, `func_1000FEF0`, and `func_1000F85C`
rows remain parked at their previously documented blockers.
