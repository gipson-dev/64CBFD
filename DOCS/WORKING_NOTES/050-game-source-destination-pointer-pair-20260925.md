# Game source/destination pointer pair - 2026-09-25

## Result

`func_151D7770` and `func_151D779C` are byte-exact across their complete
11-word linked extents `0x151D7770..0x151D779C` and
`0x151D779C..0x151D77C8`. The fresh C-only matcher reports
`2567 / 5488 (46.77%)` overall and `1999 / 4799 (41.65%)` game. One init
function remains blocked by address drift; 2,920 total and 2,800 game C
functions still differ. Debugger remains complete at `181 / 181`.

These two source-level matches complete the seven-difference game tier.

## Mismatch and resolution

Both maintained functions declared the `arg0+0x28` destination first and
inlined the `arg0+0x40` child lookup into the condition. IDO consequently
computed the destination before reading the child field and advanced every
temporary register relative to retail. Both functions also spelled the byte
clear as `&= 0xFE`; retail uses the equivalent wider immediate `0xFFFE`
before storing the low byte.

The adjacent matching `func_151D7724` supplies the source pattern. Each
function now declares the child pointer first, then the destination pointer,
tests the child field through the named pointer, and applies `0xFFFE` to the
destination byte. IDO emits both retail bodies directly. No guarded word
normalization is required.

## Verification

The current checkout passed:

```sh
make build/src/game/generated_204660.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
make tools-check
```

Both targets are absent from the non-exact list. The patch table remains at
557 rows with no duplicate filename/function/offset keys and contains no rows
for either function. Independent complete-span comparisons produced:

| Function | Bytes | Linked ELF offset | Retail offset | SHA-256 |
| --- | ---: | ---: | ---: | --- |
| `func_151D7770` | 44 | `0x217770` | `0x204C20` | `d517ddfff457357c5fcbcfa85ccd2493e2b651ac6088cb1ca9b538689af6874a` |
| `func_151D779C` | 44 | `0x21779C` | `0x204C4C` | `713f78d536b61397b41dda9342268622278371abbb291bb872f8967c97c2c2db` |

The `64CBFDOGL` sibling contains generated recomp metadata and a host smoke
test referencing `func_151D7770`, but no hand-maintained implementation for
either function. The source-order recovery does not transfer to host source.
Its dirty tree was left untouched, and frozen Release was not built or
launched.

## Next boundary

The next listed game target is 15-word `func_1509F248` with eight real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
