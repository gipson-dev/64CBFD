# Game indexed-slot clear match - 2026-09-25

## Result

`func_150F02A0` is byte-exact across its complete eight-word linked extent
`0x150F02A0..0x150F02C0`. The fresh C-only matcher reports
`2552 / 5490 (46.48%)` overall and `1984 / 4801 (41.32%)` game. One init
function remains blocked by address drift; 2,937 total and 2,817 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The original compact expression compiled to the correct operations but used
the temporary chain `t7`, `t6`, `t8`, and `t9` where retail used `t6`, `v1`,
`t7`, and `t8`. It differed in five of eight words.

Making the slot-table base pointer and byte index explicit, with the base
declared first, gave the base load its retail `v1` register and reduced the
mismatch to four words. Declaring the index before the base instead allocated
`v1` to the index and `a1` to the base; widening the index from `u8` to `s32`
did not improve allocation. Those alternatives were rejected.

Four expected-word-guarded, non-relocating normalizations select retail's
`t6` index load, `t7` shift, `t8` address, and final store base. The maintained
C now exposes the meaningful base and index lifetimes while the guards isolate
the remaining IDO temporary-allocation differences.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_11C2B0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The focused object contains all eight retail words and the target is absent
from the non-exact list. The generated patch table has 494 rows and no
duplicate filename/function/offset keys.

The linked ELF `.game` section starts at file offset `0x40000`; therefore the
function's section-relative offset `0xF02A0` maps to ELF file offset
`0x1302A0`. An independent comparison of that complete 32-byte linked span
with retail ROM offset `0x11D750` produced SHA-256
`88702e620c68fd1e29b4ba1ede612864ee03fdc06a41eddb8eefcda46250e665`
for both. The older standalone `build/conker.us.game.code.bin` was not used as
evidence because it predates the fresh link.

The `64CBFDOGL` sibling contains this function only in generated recomp output
and symbol configuration. This IDO register-allocation normalization does not
transfer to host source. Its dirty worktree was left untouched, and its frozen
Release configuration was not built or launched.

## Next boundary

The next listed game target is 12-word `func_151B2FA0` with five real
differences. Re-establish its source ownership, linked words, and relocation
context before editing. The following candidates have six or more real
differences.
