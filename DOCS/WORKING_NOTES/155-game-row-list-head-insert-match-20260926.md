# Game row-list head insert match - 2026-09-26

## Result

`func_15168A4C` is byte-exact across all 20 words, or 80 bytes, at
`0x15168A4C..0x15168A9C`. The fresh linked matcher reports 2,667 / 5,483
exact C functions overall and 2,099 / 4,794 in Game.

## Recovered behavior

The function inserts a node at the head of a row/column list rooted in
`D_800DCE50`. The node's byte at offset `0x01` selects one of two
`0x1A0`-byte rows, and `arg1` selects a four-byte pointer slot within that
row. The old slot head becomes the node's next link. When an old head exists,
its previous link is changed to the new node. The function then records
`arg1` in the node's byte at offset `0x00`, clears the new node's previous
link, and stores the node as the slot head.

A local `ListNode` type names the index, row, previous, and next fields.
Separating `row = node->row` and `column = arg1 * 4` before forming the slot
recovers retail's complete address calculation: the row remains in `v0`, the
column offset in `t7`, the global base in `t9`, and the final slot in `v1`.
Writing the old-head assignment directly in the `if` condition explains the
branch schedule that stores `node->next` in the delay slot.

## Compiler boundary

The recovered source emits sixteen of the twenty retail words directly.
Across the remaining four words, IDO keeps the old list head in unused
argument register `a2`; retail keeps the same value in `t0`. The load, null
test, delay-slot next-link store, and old-head previous-link store are
otherwise identical.

Four guarded rows in `retail_word_patches.us.csv` normalize only that register
choice. Every row verifies its compiled input word; no relocation, branch
target, instruction order, or function length changes. The patch table now
contains 1,096 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x195ECC` and pristine retail
`conker.us.bin+0x195EFC` spans are both 80 bytes and compare equal. Both hash
to:

`8cd11f1a0d4f89be63b6bb67883a21cd18de7edfdc8011d2c194dbbf096ea697`

The focused guarded object build, all-object non-matching ELF rebuild,
objcopy binary, fresh matcher, exact span comparison, `make tools-check`, all
six project-tool unit tests, and `git diff --check` pass.

## Sibling audit

`64CBFDOGL` references `func_15168A4C` through generated recompilation,
symbol, configuration, and diagnostic artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow and
keep probable handwritten `func_15125628` out of the ordinary C queue.
Generated 13-word `func_151F892C` and `func_151F8960` use unaligned
`lwl`/`lwr` bitstream loads and remain raw-assembly ownership work rather than
ordinary IDO C matching targets.

Continue with 23-word `func_150747E4`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
