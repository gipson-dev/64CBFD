# Init virtual task-address converter match

Date: 2026-09-30

`_VirtualToPhysicalTask` occupies 68 words and 272 bytes at
`0x10003220..0x10003330`. The former zero-return placeholder is replaced with
the repository-local libultra implementation. It copies the incoming 64-byte
`OSTask` into the fixed temporary task at `D_80036B60`, then converts each
non-null ucode, ucode-data, DRAM-stack, output-buffer, output-size, data, and
yield-data pointer through `osVirtualToPhysical`.

The function's real ABI is `OSTask *` in and `OSTask *` out. The fixed retail
BSS symbol remains externally owned, so this recovery does not introduce a
new object-local BSS allocation or shift surrounding data. The existing
`sptask.c` `-O2 -g3` profile emits the complete retail routine directly from
semantic C. No expected-word guards or compiler-profile changes are needed,
and sibling `osSpTaskLoad` and `osSpTaskStartGo` remain byte-exact.

The focused object build, linked rebuild, authoritative matcher, and direct
section-span comparison pass. The linked Init section and pristine image
share SHA-256
`39bdaef9aafe9186372b8b1b14301f33e467f2108ea4521d3e140aad7d45306f`
for the complete function.

The matcher advances to `3,096 / 5,457 (56.73%)` overall and
`413 / 488 (84.63%)` in Init, with zero address drift and 75 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
