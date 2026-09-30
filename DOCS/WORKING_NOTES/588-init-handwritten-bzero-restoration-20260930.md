# Init handwritten bzero restoration

Date: 2026-09-30

`bzero` occupies 40 words and 160 bytes at `0x100226F0..0x10022790`.
The previous C body was a simple byte-at-a-time loop, but retail uses the
handwritten libultra implementation. It handles an initial unaligned prefix,
clears aligned 32-byte blocks with eight word stores, clears remaining words,
and finishes with a byte loop.

The authoritative body from `asm/libultra/libc/bzero.s` now also lives behind
the function-only
`asm/nonmatchings/libultra/libc/bzero/bzero.s` `GLOBAL_ASM` boundary. The
former C approximation remains disabled under `#if 0` to document the removed
implementation. This routine is intentionally assembly-owned and uses no
expected-word guards.

The focused generated-assembly build, complete relink, refreshed progress
inventory, authoritative matcher, and direct span comparison pass. The linked
Init section and pristine image share SHA-256
`6cb49ba97859396e62e39990cd9a31a7a775d8e8b5618695b03027823a7b2863`
across all 160 bytes.

The row is now correctly classified as assembly. The matcher reports
`3,086 / 5,457 (56.55%)` exact C rows overall and
`403 / 488 (82.58%)` in Init, with zero address drift and 85 genuinely
different Init C rows. Including `bzero`, 50 Init rows are now raw assembly.

Resume with the remaining Init queue. Keep `func_1000FF90` and
`func_1000FEF0` parked at their documented saved-register allocation
boundaries.
