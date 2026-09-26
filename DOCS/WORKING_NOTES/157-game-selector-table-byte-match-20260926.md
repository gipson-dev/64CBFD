# Game selector-table byte match - 2026-09-26

## Result

`func_150849CC` is converted from a zero-return placeholder and byte-exact
across all 19 words, or 76 bytes, at `0x150849CC..0x15084A18`. The fresh
linked matcher reports 2,669 / 5,483 exact C functions overall and
2,101 / 4,794 in Game.

## Recovered behavior

The function derives a zero-based table index from two object bytes. A
nonzero byte at offset `0x1C9` selects `value - 1`. When that byte is zero,
the function falls back to offset `0x2C8`; a zero fallback selects index zero,
and a nonzero fallback selects `value - 1`.

When `arg1` is nonnull, the selected index is written through it. The function
then loads the byte-table pointer at object offset `0x2C4` and returns the
byte at the selected index. This recovers actual behavior where the previous
placeholder returned zero without reading the object, table, or output
pointer.

## Compiler boundary

The recovered source emits every retail operation, register choice, delay
slot, and memory access directly. IDO simplifies the fallback control flow to
18 words by letting `index = value - 1` fall through. Retail retains a
redundant unconditional branch to the common continuation, producing 19
words.

Three guarded rows in `retail_word_patches.us.csv` extend the two affected
branch distances and insert the retained unconditional branch after the
fallback null-test delay slot. Every row verifies its compiled input. No
register, data access, relocation, or behavior changes. The patch table now
contains 1,109 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0xB1E4C` and pristine retail
`conker.us.bin+0xB1E7C` spans are both 76 bytes and compare equal. Both hash
to:

`69dd64e52454a5db16aa031021fd5e6ee7c1a1a0140673367baad3924113ab24`

The focused guarded object build, all-object non-matching ELF rebuild,
objcopy binary, fresh matcher, exact span comparison, `make tools-check`, all
six project-tool unit tests, and `git diff --check` pass.

## Sibling audit

`64CBFDOGL` references `func_150849CC` through generated recompilation,
symbol, animation-configuration, and staging artifacts; no separate
maintained hand implementation was found. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow and
keep probable handwritten `func_15125628` out of the ordinary C queue.
Generated 13-word `func_151F892C` and `func_151F8960` use unaligned
`lwl`/`lwr` bitstream loads and remain raw-assembly ownership work.

Continue with 20-word `func_1508CA88`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
