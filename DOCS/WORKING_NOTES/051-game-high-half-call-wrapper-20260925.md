# Game high-half call wrapper - 2026-09-25

## Result

`func_1509F248` is byte-exact across its complete 15-word linked extent
`0x1509F248..0x1509F284`. The fresh C-only matcher reports
`2568 / 5488 (46.79%)` overall and `2000 / 4799 (41.68%)` game. One init
function remains blocked by address drift; 2,919 total and 2,799 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained wrapper already had retail's frame, null guard, source load,
high-half mask, call relocation, return value, and epilogue. Eight words
differed because the signed expression let IDO shift directly into `a0` in
the call delay slot. Retail shifts into `t7`, then narrows through
`andi a0,t7,0xFFFF` in that delay slot. The missing narrowing also shortened
the taken path and changed the branch displacement.

Casting the existing high-half expression to `u16` expresses the original
argument width. IDO now emits retail's separate `srl`, call, and delay-slot
`andi` directly, including the corrected branch displacement. No guarded word
normalization is required.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_CBDB0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 15 retail words and the target is absent from
the non-exact list. The patch table remains at 557 rows with no duplicate
filename/function/offset keys and contains no row for this function. An
independent comparison of the complete 60-byte linked ELF span at file offset
`0xDF248` and pristine extracted retail span at
`conker/conker.us.bin+0xCC6F8` produced SHA-256
`2196a6a2a0d16a73686d717c9024d3309d592849ea32d10c2b2e11abd07e5b82`
for both.

The `64CBFDOGL` sibling contains the symbol in generated recomp output and
symbol/staging configuration, but no hand-maintained implementation. The IDO
source-width recovery does not transfer to host source. Its dirty tree was
left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 17-word `func_150C5EFC` with eight real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
