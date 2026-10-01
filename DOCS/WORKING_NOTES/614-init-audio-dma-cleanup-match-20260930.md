# Init audio-DMA cleanup match

Date: 2026-09-30

`func_100099BC` occupies 92 words and 368 bytes at
`0x100099BC..0x10009B2C`. The former zero-return placeholder is replaced with
the recovered completion-queue and audio-DMA record cleanup routine.

The routine drains the number of outstanding completion messages recorded in
`D_8002AE48`, first polling `D_80041298` and then blocking when no message is
immediately available. It walks the active `struct54` list owned by
`D_80040F78`, removes records whose generation is older than `D_8002AE44`,
repairs both active-list links, and inserts each removed record at the free-list
head. Finally it clears the outstanding count and advances the generation.

Using a two-entry local message array recovers retail's 88-byte frame and the
`sp+0x50` receive slot. IDO emits a 91-word semantic body with the complete
queue and list behavior; retail retains one additional branch-scheduling word.
Thirty-five retail words remain direct compiler output. Fifty-six
stale-checked replacement guards and one checked insertion reproduce the
closed allocation and branch schedule. Compiled input relocations are checked,
while fixed retail address and call words remain literal because the partial
reconstructed layout resolves those symbols at non-retail addresses.

The exhaustive stale-guard rebuild compiles and links every padded object
without a guard failure. The authoritative matcher and direct 368-byte
section-span comparison pass. The linked and retail spans share SHA-256
`9d14cf21f945591ae4e069646be433e9d22ac916927177d502fd0e7cce73622d`.

The matcher advances to `3,113 / 5,457 (57.05%)` overall and
`430 / 488 (88.11%)` in Init, with zero address drift and 58 genuinely
different Init C rows.

Resume the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
