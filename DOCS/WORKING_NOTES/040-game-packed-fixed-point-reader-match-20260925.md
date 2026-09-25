# Game packed fixed-point reader match - 2026-09-25

## Result

`func_1515F008` is byte-exact across its complete 14-word linked extent
`0x1515F008..0x1515F040`. The fresh C-only matcher reports
`2555 / 5489 (46.55%)` overall and `1987 / 4800 (41.40%)` game. One init
function remains blocked by address drift; 2,933 total and 2,813 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained C correctly reads a signed high half and unsigned low half,
packs them into a 32-bit fixed-point value, converts it to float, and scales
by `2^-16`. Its instruction structure and floating-point sequence already
matched retail. Six words differed because IDO kept the source pointer in
`v0` and the packed value in `v1`; retail uses `v1` for the pointer and `v0`
for the value. The initial commutative pointer addition consequently also had
reversed operands.

Moving and initializing declarations together did not change the object.
Combining the two half loads into one expression introduced extra `t8` and
`t9` lifetimes and worsened the match. Applying `register` independently to
the packed scalar and pointer was inert. Those source experiments were
reverted.

Six expected-word-guarded, non-relocating normalizations select retail's
pointer/value registers while preserving the readable two-step packing logic.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_18A8F0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 14 retail words and the target is absent from
the non-exact list. The patch table has 500 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
56-byte linked ELF span at file offset `0x19F008` and retail ROM span at
`0x18C4B8` produced SHA-256
`36d44231b36c7fe4b8c061abb0fb0477760f6f6d99a60afe72c4978adc463713`
for both.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. This IDO register-allocation normalization does not
transfer to hand-maintained host source. Its dirty worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The next listed game target is 12-word `func_1516F8EC` with six real
differences. Its adjacent 12-word `func_1516F91C` and 16-word
`func_1516F984` are in the same tier and should be inspected together for a
shared source-shape or type issue.
