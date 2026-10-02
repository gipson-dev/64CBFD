# Init 64DD interrupt handler match

Date: 2026-10-01

`__osLeoInterrupt` occupies 441 words and 1,764 bytes at
`0x10026B10..0x100271F4`. Its former C placeholder returned zero and omitted
the 64DD PI/Leo interrupt state machine installed by `__osInitialize_common`
when the disk interface is present.

The recovered routine is grounded in the bundled libultra `leointerrupt.c`
reference and the retained retail assembly. The retail revision first checks
the disk-presence flag. Its DMA-busy path resets the PI interface, clears a
pending mechanical interrupt when necessary, records error `0x4B`, and uses
the existing abnormal-resume helper.

The main path handles mechanical and buffer-manager interrupts, write-sector
progression, read-sector and track modes, C1 error-sector collection, C2 DMA,
two-block track transitions, completion queue notification, and all abnormal
resume conditions. Retail uses interrupt error values `3`, `6`, and `17` in
places where the newer bundled SDK headers name `22`, `24`, and `23`; local
constants preserve the measured retail semantics explicitly.

IDO emits a 440-word compact body. Of those words, 323 match retail directly.
The remaining closed register allocation, scheduling, branch-target, and
relocation layout is represented by 117 function-scoped, stale-checked rows,
including 52 relocation-aware rows. No insertion or omission guards are used;
the existing generated-object layout supplies the retail slot's final `nop`.

The padded object and linked ELF build successfully, and the matcher no longer
lists `__osLeoInterrupt`. Direct comparison of
`0x10026B10..0x100271F4` reports zero different bytes. Both 1,764-byte spans
share SHA-256
`2c73138bf3c4ec93d256f0014f9526852817bf7460b691ea4fac3a36f140e695`.

The matcher advances to `3,167 / 5,456 (58.05%)` byte-exact C functions
overall and `484 / 487 (99.38%)` in Init, with zero address drift and three
different Init rows. The next smallest remaining Init target is the 580-word
`func_1000A750`, currently different in 507 words.
