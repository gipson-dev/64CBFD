# Init dual-framebuffer clear match

Date: 2026-09-30

`func_10003ACC` occupies 65 words and 260 bytes at
`0x10003ACC..0x10003BD0`. The former empty placeholder is replaced with the
recovered dual-framebuffer RGBA5551 clear. It derives the pixel count from
`D_800BE620 * D_800BE624`, returns when framebuffer zero is null, fills the
first framebuffer with a scalar pointer loop, and fills the second with its
retail remainder loop and four-pixel bulk loop.

The recovered expression packs the three signed inputs as five red, five
green, five blue, and one alpha bit. The count retains retail's signed
multiply, double, and arithmetic-shift sequence. The first loop advances its
framebuffer cursor one halfword per pixel. The second loop first handles
`count & 3` pixels and then advances four halfwords per iteration.

The object uses `-O2 -g3 -Wo,-loopunroll,0`. Normal `-O2` unrolls both loops
and overflows the retail slot. Disabling automatic unrolling preserves the
scalar first loop, while the four-store second loop is expressed explicitly
in semantic C. Reusing the now-dead first argument for the second packed color
keeps the emitted function inside its retail extent without a stack frame.

Eight words emit at their retail offsets. Fifty-seven function- and
offset-scoped entries in `retail_word_patches.us.csv` normalize IDO's closed
register allocation and loop schedule, including the one-word displacement
through the second fill and the final return. The two framebuffer-table
address entries are relocation-aware, and every row fails if its expected
compiler word or relocation changes.

The focused object build, exhaustive stale-guard rebuild, authoritative
matcher, and direct section-span comparison pass. The linked Init section and
pristine image share SHA-256
`90aebf408fc334f16c47bd3141064d4bb1434fd80b2e9a8aa9581b524559822f`
for the complete function.

The matcher advances to `3,099 / 5,457 (56.79%)` overall and
`416 / 488 (85.25%)` in Init, with zero address drift and 72 genuinely
different Init C rows.

Resume with the remaining Init queue. Keep `func_1000FF90`,
`func_1000FEF0`, and `func_1000F85C` parked at their documented compiler
allocation boundaries.
