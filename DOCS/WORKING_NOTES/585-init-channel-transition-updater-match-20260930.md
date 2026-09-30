# Init channel-transition updater match

Date: 2026-09-30

`func_1000DF68` occupies 59 words and 236 bytes at
`0x1000DF68..0x1000E054`. It finds the requested channel record through
`func_1000B1FC`, installs the new 16-bit target, and optionally snaps the
current value and refreshes an active channel through `func_1000CC54`. For
multi-step transitions it stores the absolute current-to-target difference
divided by the requested step count, preserving retail's zero-to-two and
`0x8000`-to-`0x7FFF` clamps. Short transitions use the fixed `0x200` step.

Recovering the function's `void` ABI, record type, signed absolute difference,
integer division, and clamp order reproduces its frame, argument spills,
calls, division traps, and first 47 words. IDO emits the final clamp,
fixed-step store, and epilogue one word shorter than retail. Twelve
stale-checked, relocation-free guards normalize that closed tail schedule,
including the two branch displacements that cross it. No data or call
relocation is replaced.

The focused compact-object inspection, exhaustive guard-dependent rebuild,
complete relink, authoritative matcher, and direct section-span comparison
pass. The linked ELF and retail spans share SHA-256
`e3f6789eb12fdf89b984522ef3520b5996babbbae4f94646ea8610ff45011f9a`.
The matcher advances to `3,084 / 5,458 (56.50%)` overall and
`401 / 489 (82.00%)` in Init, with zero address drift and 88 genuinely
different Init C rows.

Resume with the remaining Init queue after the parked `func_1000FF90`.
