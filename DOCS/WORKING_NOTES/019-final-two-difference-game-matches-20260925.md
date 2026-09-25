# Final two-difference game matches - 2026-09-25

## Result

`func_1516968C` and `func_151696DC` are byte-exact across their contiguous
40-word linked extent `0x1516968C..0x1516972C`. The fresh C-only matcher reports
`2539 / 5495 (46.21%)` overall and `1971 / 4806 (41.01%)` game. One init
function remains blocked by address drift; 2,955 total and 2,835 game C
functions still differ. No two-difference game rows remain in `LIST=1`.

## Mismatches and resolution

The 20-word `func_1516968C` body already matched except for the order of two
independent byte loads at offsets `0x28` and `0x2C`. Retail loads `*arg1` into
`t7` before loading `arg0->unkC` into `t8`; IDO canonicalized both tested
comparison operand orders to the opposite schedule. Earlier one-local and
two-local source forms changed allocation and increased the mismatch count.
Two function- and offset-scoped guards now select the retail load order.

The 20-word `func_151696DC` body already matched except for two independent
loop-setup instructions around the positive-count branch. Retail materializes
the low half of `D_800DD198` at offset `0x0C` and initializes the loop index in
the branch delay slot at `0x14`. Source-order experiments changed register
allocation and regressed to 11 differences. Two guarded rows move the
`R_MIPS_LO16:D_800DD198` relocation with its `addiu` and place the zeroing move
in the retail delay slot.

## Verification

The current checkout passed:

```sh
make build/src/game_1944C0.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

Both targets are absent from the non-exact list. An independent extraction of
the linked `.game` section compared addresses `0x1516968C..0x1516972C` with
`conker.us.bin+0x196B3C`; all 160 bytes match and both slices have SHA-256
`ca16f7d8c8821d2c6269b0996afaae7e104035e3f29646ca1306c54976f16eb2`.
The debugger remains complete at 181 / 181 C rows, plus its independently
exact handwritten assembly row.

The `64CBFDOGL` sibling already carries both functions as generated recomp
entries with 0x50-byte extents. These IDO-only scheduling normalizations do not
transfer to host source. Its unrelated worktree was left untouched, and its
frozen Release configuration was not built or launched.

## Next boundary

The smallest remaining game rows each have three real differences. Inspect
three-word `func_150AD780` first to determine whether it is an ordinary C
function, a shared boundary, or handwritten code before changing source. The
other current three-difference game candidates are `func_150849A0` (11 words),
`func_150636A4` (19 words), `func_1514672C` (30 words), `func_15199980`
(36 words), and `func_1505D024` (104 words).
