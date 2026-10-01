# Init audio-record cleanup and dispatch match

Date: 2026-09-30

`func_1000E17C` occupies 94 words and 376 bytes at
`0x1000E17C..0x1000E2F4`. Its zero-return placeholder is replaced with the
recovered three-pass maintenance routine for the twelve-record audio pool.

The first pass checks records with positive identifiers. Definition types one
and three are selected after clearing flag bits `0xF0`; selected records whose
primary runtime slot is already `-1` are invalidated. The second pass clears
each record's links at offsets `0x60` and `0x10` when the linked record has
been invalidated. The final pass selects the same definition types and sends
active identifiers through `func_1000DE1C` with operation four.

Pointer-based `do/while` loops reproduce retail's unconditional twelve-record
passes and exact branch topology. If all three passes reference the same C
symbols, IDO common-subexpresses the pool start and end addresses across the
function, producing an 89-word body instead of retail's 94 words. Distinct
compile-time aliases preserve the three independent materialization
lifetimes. The aliases are fully consumed by stale-checked relocation guards;
the linked object references only `D_800419A8` and `D_80041E58`.

The recovered body has the exact 94-word extent and 56-byte frame. Seventy-six
opcodes emit directly from C. Eighteen stale-checked replacements normalize
one closed `s3`/`s4`/`s5` allocation rotation and three address-completion
schedules. Five additional guards change only alias relocation symbols. No
instruction is inserted or omitted.

The exhaustive shared-guard rebuild compiles every padded object and links
the complete ELF without a stale-guard failure. The expected whole-ROM
checksum remains incomplete, while the authoritative matcher and direct
376-byte section-span comparison pass. The linked and retail spans share
SHA-256
`a3fd280d56d3bd1bdabfb0dd492979c232b8fc91404eca3957b50a24d81bfdc5`.

The matcher advances to `3,118 / 5,457 (57.14%)` overall and
`435 / 488 (89.14%)` in Init, with zero address drift and 53 genuinely
different Init C rows.

Continue the remaining Init queue. Keep `func_1000FF90`, `func_1000FEF0`, and
`func_1000F85C` parked at their documented compiler-allocation boundaries.
