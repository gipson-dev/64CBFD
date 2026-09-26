# Game countdown register match - 2026-09-25

## Result

`func_15108B80` is byte-exact across its complete 16-word linked extent
`0x15108B80..0x15108BC0`. The fresh C-only matcher reports
`2562 / 5488 (46.68%)` overall and `1994 / 4799 (41.55%)` game. One init
function remains blocked by address drift; 2,925 total and 2,805 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained C already represents retail's terminal marker, object-relative
pointer, countdown subtraction, writeback, and negative-result state change.
Its control flow, function length, and `D_800BE9E4` relocation pair also
matched. Seven words differed because IDO assigned the terminal marker to
`a1` instead of retail's `v1`, assigned the countdown result to `v1` instead
of retail's `t0`, and encoded one commutative pointer addition as `t6+a0`
instead of `a0+t6`.

Moving the countdown declaration outside the conditional and reversing the
equivalent pointer-add expression were tested together; IDO emitted the same
object, so that source experiment was reverted. Seven expected-word-guarded,
non-relocating normalizations select retail's register lifetimes and operand
order. The global HI16/LO16 words remain untouched.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_135D00.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
make tools-check
```

The focused object contains all 16 retail words and the target is absent from
the non-exact list. The patch table has 540 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
64-byte linked ELF span at file offset `0x148B80` and pristine extracted
retail span at `conker/conker.us.bin+0x136030` produced SHA-256
`780f645debdf6325c966f3f00d0e78556835ec450895964b890d2c3eb2ddc8d5`
for both.

The `64CBFDOGL` sibling contains this symbol only in generated recomp output
and symbol configuration, with no hand-maintained implementation. This IDO
register normalization does not transfer to host source. Its dirty tree was
left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 19-word `func_1513A594` with seven real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
