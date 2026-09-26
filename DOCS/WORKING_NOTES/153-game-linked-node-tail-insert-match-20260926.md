# Game linked-node tail insert match - 2026-09-26

## Result

`func_1515D520` is byte-exact across all 35 words, or 140 bytes, at
`0x1515D520..0x1515D5AC`. The fresh linked matcher reports 2,665 / 5,483
exact C functions overall and 2,097 / 4,794 in Game.

## Recovered behavior

The function allocates a `0x34`-byte node with allocation arguments
`(0x34, 1, 2, 2)`. A successful allocation is cleared with `bzero`. If
`D_800DCD78` is null, the new node becomes the list head. Otherwise, the
function follows each node's first-word next pointer, appends the allocation
after the current tail, and clears the new node's next pointer. It returns the
new node, or null when allocation fails.

A local `LinkedNode` type makes the 0x34-byte object and its first-word link
explicit. Testing `D_800DCD78` through a separate head lifetime, rather than
first reusing the traversal cursor, recovers retail's empty-list
branch-likely, loop entry, branch delay slots, and otherwise unreachable
layout store. An explicit saved allocation lifetime prevents IDO from keeping
the node in `a2` across `bzero`, recovering retail's `a0` node and `a1` head
register assignments.

## Compiler boundary

The recovered source emits 31 of the 35 retail words directly. IDO assigns a
48-byte debug frame instead of retail's 32-byte frame and independently
schedules the saved-node store before `bzero` while retail schedules the
`0x34` size there and places the store in the call delay slot.

Four guarded rows in `retail_word_patches.us.csv` normalize the frame
allocation/restoration and those two independent words. Every row checks its
compiled input word. No relocations or branches are changed. The patch table
now contains 1,077 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x18A9A0` and pristine retail
`conker.us.bin+0x18A9D0` spans are both 140 bytes and compare equal. Both hash
to:

`733ee62073dc69ffbb2b236538fc66d6723f7b8e4375b011ab98d10982b35504`

The focused guarded object build, all-consumer non-matching ELF rebuild,
objcopy binary, fresh matcher, exact span comparison, `make tools-check`, all
six project-tool unit tests, and `git diff --check` pass.

## Sibling audit

`64CBFDOGL` contains `func_1515D520` only in generated recompilation, symbol,
and configuration artifacts; no separate maintained hand implementation was
found. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow.
Keep probable handwritten `func_15125628` out of the ordinary C matching
queue; raw-assembly ownership remains a separate workstream.

Continue with 23-word `func_151635A8`, the next ordinary Game C row with
sixteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
