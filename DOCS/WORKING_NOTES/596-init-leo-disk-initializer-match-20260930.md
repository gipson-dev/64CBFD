# Init Leo disk initializer match

Date: 2026-09-30

`osLeoDiskInit` occupies 60 words and 240 bytes at
`0x10027820..0x10027910`. Its recovered libultra body initializes the 64DD PI
handle type, base address, and domain-two timing fields; writes those timings
to the PI registers; clears the 96-byte transfer record; and installs the
handle into the PI table and disk-handle global while interrupts are disabled.

The body is based on the repository-local `tools/ultralib` implementation and
uses the SDK `-O1` profile. This retail revision does not emit the reference
source's `domain` or `speed` stores. Removing those revision-mismatched writes
restores the correct 60-word semantic body.

IDO still materializes the handle address twice for the adjacent `pageSize`
and `relDuration` stores, while retail shares one high-address load. Seven
function- and offset-scoped entries in `retail_word_patches.us.csv` normalize
that bounded cluster: five scheduling substitutions, one relocation-checked
omission, and one trailing zero-word insertion that preserves the retail
extent. All later instructions and relocations then retain their compiler
output unchanged.

The focused object build, exhaustive stale-guard rebuild, authoritative
matcher, and direct section-span comparison pass. The linked Init section and
pristine image share SHA-256
`7d204edfe2419d1dc472aaba89b7665d3ca50a8969dc9c573e26338dceb566bc`
for the complete function.

The matcher advances to `3,095 / 5,457 (56.72%)` overall and
`412 / 488 (84.43%)` in Init, with zero address drift and 76 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
