# Game display-list cursor twin match - 2026-09-25

## Result

All 14 words of `func_15166FD8` now match retail across
`0x15166FD8..0x15167010`. The fresh linked matcher reports
`2575 / 5484 (46.95%)` overall and `2007 / 4795 (41.86%)` game. One init
function remains blocked by address drift; 2,908 total and 2,788 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Source and schedule evidence

The routine emits the `0xDA380003` display-list command pointing at
`D_80089470` and returns the advanced command cursor. Its source already uses
the typed `Gfx *g = arg0++` idiom established for `func_1510E634`.

IDO emitted the same compact 11-instruction schedule: it folded the original
cursor into `a0`, computed the return directly in `v0`, and left three padding
words. Retail retains the original cursor in `v1`, resolves the address low
half before the command constant, stores through `v1`, advances `a0`, and
copies it to `v0` before returning.

Eight function-specific guarded rows restore that schedule. Two rows insert
the retained-cursor move and final return-delay `nop`; six reorder the low-half
address calculation, command constant, stores, cursor advance, and return
copy. The moved `R_MIPS_LO16 D_80089470` relocation is explicitly guarded.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_193E50.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 56-byte linked ELF span at file
offset `0x1A6FD8` and pristine extracted retail span at
`conker/conker.us.bin+0x194488` produced SHA-256
`4905a240f582ba884f83a2b6ab96c6f6109fbf5a5d54ce9e50a382b3f95c8ef3`
for both. The retail-word patch table has 607 rows, no duplicate
filename/function/offset keys, exactly eight rows for this function, and seven
insertion-bearing rows project-wide.

The `64CBFDOGL` sibling has symbol metadata for `func_15166FD8` but no
hand-maintained implementation to transplant. Its dirty tree was left
untouched, and frozen Release was not built or launched.

## Next boundary

Continue with 33-word `func_15196330`, now the first game row with nine real
differences. Compare its source, compact object, retail words, and relocations
before editing; do not assume it shares this cursor-writer pattern.
