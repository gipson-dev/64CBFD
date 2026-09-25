# Game Event Handler Byte Match - 2026-09-25

## Result

`func_15135480` is byte-exact across its 55-word extent
`0x15135480..0x1513555C`. Full linked progress is 2528 / 5497 (45.99%); game
is 1960 / 4808 (40.77%), with 2848 game C functions still different.

## Mismatch and resolution

The maintained C body was behaviorally correct and 53 of 55 words already
matched retail. The only differences were commuted equality operands:

- offset `0x48`: compiled `bnel v0,t9`; retail `bnel t9,v0`;
- offset `0xAC`: compiled `beq v0,t1`; retail `beq t1,v0`.

Unsigned subtraction-to-zero expressions produced the desired branch order
but extended temporary lifetimes and changed later registers. Those source
experiments were reverted. `retail_word_patches.us.csv` now carries two
function- and offset-scoped expected-word guards that normalize only the two
independent branch words.

## Verification

The current checkout passed:

```sh
make -j4 build/src/game_161520.c.o
make -j8 build/conker.us.elf
python3 ../tools/match_progress.py progress.csv build/conker.us.elf \
  conker.us.bin --version us --objdump mips-linux-gnu-objdump
```

The sibling `64CBFDOGL` consumes the original function through generated
N64Recomp output, so this IDO-only operand normalization does not transfer.
Its frozen Release configuration was not built or launched.

## Next boundary

The current one-difference game rows are `func_150AF2E0`, `func_151061EC`,
`func_15144A74`, and `func_151ACB60`. Existing notes park the first three
pending recovered signature/type information and identify `func_151ACB60` as
an argument-homing timing wall. Re-audit those prerequisites before another
source-shape experiment rather than repeating blind operand swaps.
