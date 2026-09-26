# Game linked-node reset match - 2026-09-26

## Result

`func_1515C158` is byte-exact across all 18 words, or 72 bytes, at
`0x1515C158..0x1515C1A0`. The fresh linked matcher reports 2,664 / 5,483
exact C functions overall and 2,096 / 4,794 in Game.

## Recovered behavior

The function visits the two `0x1A0`-byte rows spanning `D_800DCE50` through
`D_800DD190`. Each row owns a linked-list head at offset `0xC8`. For every
node, the function clears the word at offset `0x44`, writes `-1` at offset
`0x48`, and follows the next pointer at offset `0x08`.

Typed local `ResetRow` and `ResetNode` layouts make that ownership explicit.
The resulting C reproduces the retail 18-word length, null-row path, inner
loop, duplicated clear in the inner branch-likely delay slot, and next-row
head load in the outer branch-likely delay slot.

## Compiler boundary

IDO 5.3 consistently keeps the row cursor in `v0` and each node in `v1`;
retail uses `v1` for the row and `v0` for the node. Equivalent raw-pointer,
typed-structure, declaration-order, loop-form, and optimized-away-expression
spellings retained that coloring once the control flow had reached the exact
18-word shape.

Thirteen guarded rows in `retail_word_patches.us.csv` normalize this
compiler-only register assignment. Two rows also move checked `R_MIPS_LO16`
relocations so the global address low halves retain retail order. Every row
checks its compiled input word, and the relocation rows check both old and new
relocation ownership. The table now contains 1,073 unique rows with zero
duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x1895D8` and pristine retail
`conker.us.bin+0x189608` spans are both 72 bytes and compare equal. Both hash
to:

`766f008ab39ae3a2a267b0c789c7b65a48c6307d0de4f1bf78fc4831dbc01c25`

The focused object build, full non-matching ELF and binary build, fresh
matcher, relocation-aware disassembly, exact span comparison, `make
tools-check`, all six project-tool unit tests, and `git diff --check` pass.

## Sibling audit

`64CBFDOGL` contains `func_1515C158` in generated recompilation, symbol,
configuration, and historical documentation artifacts; no separate
maintained hand implementation was found. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Keep probable handwritten `func_15125628` out of the ordinary C
matching queue; raw-assembly ownership remains a separate workstream.

Continue with 35-word `func_1515D520`, the next ordinary Game C row with
sixteen real differences. Its existing C already describes allocation,
zeroing, tail insertion into `D_800DCD78`, and null termination; begin by
measuring its current stack-slot and list-cursor lifetime differences.
