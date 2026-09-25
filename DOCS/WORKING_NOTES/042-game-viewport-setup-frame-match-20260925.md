# Game viewport setup frame match - 2026-09-25

## Result

`func_15019BB8` is byte-exact across its complete 68-word linked extent
`0x15019BB8..0x15019CC8`. The fresh C-only matcher reports
`2559 / 5489 (46.62%)` overall and `1991 / 4800 (41.48%)` game. One init
function remains blocked by address drift; 2,929 total and 2,809 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained C already matched 61 of 68 words. IDO reserved a `0x38`-byte
frame while retail uses `0x30`. All actual stack accesses already use retail
offsets: saved `s0` and `ra` are at `0x20` and `0x24`, the sign-extended local
is at `0x28`/`0x2A`, and outgoing arguments occupy `0x10` and `0x14`. No
instruction references the compiler-only `0x30..0x37` area.

That unused frame-size choice also exchanged `t7` and `t8` in five words of
the `D_800BE628 + arg1 * 0x180 + D_800BE9C0 * 0x10 + 0x40` viewport-address
calculation. Earlier attempts to introduce or remove named locals either left
the 56-byte frame unchanged or grew it by another eight-byte chunk, so those
experiments were reverted.

Seven expected-word guards normalize the frame open/close and five affected
address words. The `R_MIPS_HI16:D_800BE628` and
`R_MIPS_LO16:D_800BE628` relocations remain attached to their normalized
instructions.

## Verification

The current checkout passed:

```sh
make build/src/game_45B80.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all 68 retail words and the target is absent from
the non-exact list. The patch table has 519 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
272-byte linked ELF span at file offset `0x59BB8` and retail ROM span at
`0x47068` produced SHA-256
`e5b5db6ffd379981dedd07db51eb68b92bf6fa81490c6ef281c01a3b68c28bb0`
for both.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. This IDO frame/register normalization does not
transfer to hand-maintained host source. Its dirty worktree was left
untouched, and its frozen Release configuration was not built or launched.

## Next boundary

The next listed game target is 14-word `func_1509F6B0` with seven real
differences, followed by 14-word `func_150C7930` and 17-word `func_150CDB6C`
in the same tier.
