# Game outer/child pointer match - 2026-09-25

## Result

`func_15155EF8` is byte-exact across its complete 17-word linked extent
`0x15155EF8..0x15155F3C`. The fresh C-only matcher reports
`2565 / 5488 (46.74%)` overall and `1997 / 4799 (41.61%)` game. One init
function remains blocked by address drift; 2,922 total and 2,802 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The maintained wrapper already has retail's child-pointer load and null guard,
optional `func_1515F10C` call, outer-object `func_15169804` cleanup, final
`func_1518CA04(0xA6)` call, frame, and control flow. All three call
relocations matched before this pass.

Seven words differed because IDO kept the outer object in `a2` and its
`+0x14` child in `a1`; retail uses `a1` for the outer object and `a2` for the
child throughout the test, call, spill/reload, and cleanup. An explicit outer
pointer local was tested, but IDO optimized it back to the identical object,
so that inert source experiment was reverted. Seven expected-word-guarded,
non-relocating normalizations select the retail lifetimes without moving any
call relocation.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_182C30.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
make tools-check
```

The focused object contains all 17 retail words and the target is absent from
the non-exact list. The patch table has 557 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
68-byte linked ELF span at file offset `0x195EF8` and pristine extracted
retail span at `conker/conker.us.bin+0x1833A8` produced SHA-256
`c50b79d927b784631c6207992362051194d61b397ef57534ab57f716c9876140`
for both.

The `64CBFDOGL` sibling contains this symbol only in generated recomp output
and symbol configuration, with no hand-maintained implementation. This IDO
pointer-register normalization does not transfer to host source. Its dirty
tree was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 11-word `func_151D7770` with seven real
differences, followed by adjacent 11-word `func_151D779C`. Inspect the pair
together for a shared source or generated-slice pattern.
