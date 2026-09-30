# Init handwritten osSetIntMask restoration

Date: 2026-09-30

`osSetIntMask` occupies 40 words and 160 bytes at
`0x10024880..0x10024920`. The previous source was a zero-return C placeholder
even though the retail routine is handwritten assembly. It reads CP0 Status,
combines the current CPU and MI masks, translates the requested RCP mask
through `D_8002C850`, writes `D_A430000C`, installs the requested CPU mask in
CP0 Status, observes the original hazard nops, and returns the previous mask.

The authoritative body from `asm/libultra/os/setintmask.s` now lives behind
the dedicated `asm/nonmatchings/generated_setintmask/osSetIntMask.s` boundary.
The false C body remains disabled under `#if 0` only to document the removed
placeholder. The CP0 access and hardware-register sequence are intentionally
handwritten and are not modeled through synthetic C or expected-word guards.

The focused generated-slice build, complete relink, refreshed progress
inventory, authoritative matcher, and direct span comparison pass. The built
Init section and pristine image share SHA-256
`4f77fb7a5c63f84cc4f19456f3608deb338d495a7c560abf9cb4a8548f7275b1`
across all 160 bytes, including the retail data relocations.

The row is now correctly classified as assembly. The matcher reports
`3,081 / 5,458 (56.45%)` exact C rows overall and
`398 / 489 (81.39%)` in Init, with zero address drift and 91 genuinely
different Init C rows.

Resume with the remaining Init queue after the parked `func_1000FF90`.
