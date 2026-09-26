# Game callback selector register match - 2026-09-25

## Result

All 33 words of `func_15196330` now match retail across
`0x15196330..0x151963B4`. The fresh linked matcher reports
`2576 / 5484 (46.97%)` overall and `2008 / 4795 (41.88%)` game. One init
function remains blocked by address drift; 2,907 total and 2,787 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Register evidence

The function reads a callback record through `arg0+0x98`, dispatches signed
selectors at record offsets `0x65` and `0x62` through `D_8008F898` and
`D_8008F88C`, then calls `func_151478F4`. Its 32-byte frame, argument spill,
branches, selector scales, indirect calls, pointer spill/reload, direct call,
epilogue, and all five relocations already matched retail.

All nine differences were one closed `v0`/`v1` rotation. Retail keeps the
record pointer in `v0` across the first callback and uses `v1` for both signed
selectors; IDO chose the reverse. Nine expected-word guards restore those
lifetimes without altering relocations or control flow.

Three source experiments were rejected. Separating declarations and widening
the selector from `s8` to `s32` left codegen unchanged. Declaring the selector
before the pointer also left the register rotation intact while moving the
pointer spill from `sp+0x1C` to `sp+0x18`.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_1C2C60.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 132-byte linked ELF span at file
offset `0x1D6330` and pristine extracted retail span at
`conker/conker.us.bin+0x1C37E0` produced SHA-256
`8661611d0a0313dbe6f9307ad9d011fdeda11efe9b9a69fd63b2fefd45d67efb`
for both. The retail-word patch table has 616 rows, no duplicate
filename/function/offset keys, and exactly nine rows for this function.

The `64CBFDOGL` sibling has symbol metadata for `func_15196330` but no
hand-maintained implementation to transplant. Its dirty tree was left
untouched, and frozen Release was not built or launched.

## Next boundary

Continue with adjacent 33-word `func_151963B4`, which has the same nine-word
register rotation and differs only in its final direct callee. Verify its
retail span, relocation set, and complete linked hash independently.
