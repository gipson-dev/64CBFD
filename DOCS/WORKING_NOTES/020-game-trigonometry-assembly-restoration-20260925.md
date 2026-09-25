# Game trigonometry assembly restoration - 2026-09-25

## Result

The false C placeholders for `func_150AD780` and `func_150AD78C` are restored
to their original assembly ownership. Their complete contiguous extent
`0x150AD780..0x150AD8B0` is 304 bytes, or 76 words, and matches retail exactly.

This is a classification correction rather than two new C matches. The fresh
C-only matcher reports `2539 / 5493 (46.22%)` overall and
`1971 / 4804 (41.03%)` game. One init function remains blocked by address
drift; 2,953 total and 2,833 game C functions still differ.

## Classification evidence

Retail `func_150AD780` is the game's sine entry. Its three instructions load a
phase constant and add it to `$f12`; there is deliberately no `jr $ra`.
Execution falls directly into `func_150AD78C`, the cosine polynomial body.
That body branches and jumps to the shared return label `func_150AD89C`.

The placeholder source modeled all three labels as independent functions that
returned integer zero. Besides differing from retail, that erased the sine-to-
cosine fallthrough and the floating-point result in `$f0`. The sibling OGL
generated recomp already carries an explicit call from `func_150AD780` to
`func_150AD78C` to preserve this retail behavior.

The preserved `asm/DAC30.s` is the instruction authority. Three focused
`GLOBAL_ASM` fragments reproduce its retail symbol boundaries while allowing
the generated-slice padding validator to check each `glabel`: 12 bytes for
`func_150AD780`, 272 bytes for `func_150AD78C`, and 20 bytes for the shared
return and trailing padding at `func_150AD89C`.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_DAC30.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

The restored C rows are absent from `LIST=1`. An independent extraction of the
linked `.game` section compared all 304 bytes with `conker.us.bin+0xDAC30`;
both slices have SHA-256
`8d11bc80687c5c4bbf4dd3a814674a238008142d46badec1334a186ec6d1ba6d`.

The `64CBFDOGL` sibling already has generated recomp entries for both public
symbols and an explicit host-side fallthrough repair. No host source transfer
or build is required. Its unrelated worktree was left untouched, and its
frozen Release configuration was not built or launched.

## Next boundary

The remaining game queue begins with five three-difference C candidates.
Inspect 11-word `func_150849A0` next, followed by `func_150636A4` (19 words),
`func_1514672C` (30 words), `func_15199980` (36 words), and
`func_1505D024` (104 words).
