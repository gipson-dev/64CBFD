# Game display-list cursor expansion - 2026-09-25

## Result

All 15 words of `func_1510E634` now match retail across
`0x1510E634..0x1510E670`. The fresh linked matcher reports
`2573 / 5484 (46.92%)` overall and `2005 / 4795 (41.81%)` game. One init
function remains blocked by address drift; 2,910 total and 2,790 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Source and tool evidence

The routine emits the `0xDA380003` display-list command pointing at
`D_80089470` and returns the advanced command cursor. The typed source now
uses the established `Gfx *g = arg0++` idiom also present in
`func_15166FD8`. Under this generated slice's compiler profile, IDO still
folds the original cursor into `a0`, computes the return directly in `v0`, and
emits an 11-word body instead of retail's 13 meaningful words.

Eight guarded rows restore the retail schedule. One inserts `v1 = a0` after
the argument spills, one inserts the final return-delay `nop`, and the other
six reorder the address low half and command constant, store through `v1`,
advance `a0`, and copy it to `v0`. The moved `R_MIPS_LO16 D_80089470`
relocation is explicitly guarded.

`tools/pad_generated_object.py` now accepts the same non-relocated
`insert_after` field already supported for plain padded C objects. It counts
insertions before enforcing the retail slot, advances emitted jump-label
positions, and reports the expanded function size. A new assembler-backed
unit test verifies the inserted word and following function address.

## Verification

The current checkout passed:

```sh
python3 -m unittest discover -s tools/tests -p 'test_pad_*.py'
make build/src/game/generated_13AE20.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
```

An independent comparison of the complete 60-byte linked ELF span at file
offset `0x14E634` and pristine extracted retail span at
`conker/conker.us.bin+0x13BAE4` produced SHA-256
`28d8bacba51037d5bdf8db9e479119ce8122427682c41a509a427bc6079ec25e`
for both. The retail-word patch table has 590 rows, no duplicate
filename/function/offset keys, exactly eight rows for this function, and five
insertion-bearing rows project-wide.

The `64CBFDOGL` sibling has no hand-maintained implementation of
`func_1510E634`. This compiler-shape and padding-tool correction does not
require a host transplant. Its dirty tree was left untouched, and frozen
Release was not built or launched.

## Next boundary

Continue with 16-word `func_1512D6B0`, now the first game row with nine real
differences. Compare its C body, compact object, retail words, and relocations
before editing.
