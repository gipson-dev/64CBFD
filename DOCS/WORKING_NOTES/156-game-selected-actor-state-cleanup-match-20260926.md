# Game selected actor-state cleanup match - 2026-09-26

## Result

`func_150747E4` is byte-exact across all 23 words, or 92 bytes, at
`0x150747E4..0x15074840`. The fresh linked matcher reports 2,668 / 5,483
exact C functions overall and 2,100 / 4,794 in Game.

## Recovered behavior

The function reads the active object's byte at offset `0x65`. Zero leaves all
actor state unchanged. A nonzero value selects
`D_800CC2D0[active->unk65 - 1]`, clears the selected actor's pointer at offset
`0x218`, and stores the low byte of `D_800D1580` at actor offset `0x232`.

The previous source embedded `active->unk65 - 1` directly in the array index
and read `D_800D1580` only at the final field assignment. IDO distributed the
subtraction into a late `-0x32C` pointer adjustment and scheduled the update
load between the two stores. Explicit `index` and full-width `value` locals
recover the retail structure: test the original slot, decrement it, multiply
that index by `sizeof(struct127)`, load the update value before the final
stride shift, form the actor pointer in `a0`, then perform both stores.

## Compiler boundary

The recovered source emits thirteen of the twenty-three retail words
directly, including the complete control flow, stride sequence, update-load
timing, final pointer and stores, and function length. IDO still assigns the
decremented index to `v0` instead of retail's `v1`, keeps the update value in
`v1` instead of `t9`, and exchanges the positions of the actor-array low
relocation and update-value high relocation.

Ten guarded rows in `retail_word_patches.us.csv` normalize those persistent
compiler choices. Two rows explicitly verify and exchange the relocation
types and symbols; the other eight change only index/value registers. No
branch target, memory offset, instruction count, or behavior changes. The
patch table now contains 1,106 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0xA1C64` and pristine retail
`conker.us.bin+0xA1C94` spans are both 92 bytes and compare equal. Both hash
to:

`e55e08ffb3090ae280fa188c1f8d04a0896849388ab6ef9c6ed04b7cac1774e0`

The focused guarded object build, all-object non-matching ELF rebuild,
objcopy binary, fresh matcher, exact span comparison, `make tools-check`, all
six project-tool unit tests, and `git diff --check` pass.

## Sibling audit

`64CBFDOGL` references `func_150747E4` through generated recompilation,
symbol, configuration, and staging artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow and
keep probable handwritten `func_15125628` out of the ordinary C queue.
Generated 13-word `func_151F892C` and `func_151F8960` use unaligned
`lwl`/`lwr` bitstream loads and remain raw-assembly ownership work.

Continue with 19-word `func_150849CC`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
