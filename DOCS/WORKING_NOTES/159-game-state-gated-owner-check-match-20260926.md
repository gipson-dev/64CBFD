# Game state-gated owner check match - 2026-09-26

## Result

`func_15116930` is converted from a zero-return placeholder and byte-exact
across all 21 words, or 84 bytes, at `0x15116930..0x15116984`. The fresh
linked matcher reports 2,671 / 5,483 exact C functions overall and
2,103 / 4,794 in Game.

## Recovered behavior

The function first requires bit `0x04` in the object's byte at offset `0x4F`.
It then reads the state byte at offset `0x73` and exits when either low state
bit or bit `0x04` is already set. For a clear state, it follows the pointer at
`arg1 + 0x31C` and requires that owner's byte at offset `0x57` to equal one.

When every gate passes, the function clears the low two state bits and then
sets bit `0x02` through the same two consecutive byte stores found in retail.
No null check is present in the original code, so the recovered C retains the
authored assumption that the owner pointer is valid on this path.

## Compiler boundary

The decisive source shape retains `arg1 + 0x31C` as an `u8 **` owner-slot
address and dereferences it only in the final condition. Loading the owner
into a local `u8 *` made IDO overwrite `v0` and emit an extra preservation
move. Retaining the slot address lets IDO keep the state byte in `v0`, emit
the late owner load into `t0`, and reproduce all retail registers, branch
distances, delay slots, masks, and stores directly from C.

No guarded word rows were needed. The patch table remains at 1,111 unique
rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x143DB0` and pristine retail
`conker.us.bin+0x143DE0` spans are both 84 bytes and compare equal. Both hash
to:

`c5c323dece9963de7032c222fae4dbd364fe18d5a94e0da60766d8cf3e62566a`

The focused object build, non-matching relink and objcopy binary, fresh
matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` references `func_15116930` through generated recompilation,
symbol, and animation-configuration artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and
size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 21-word `func_1511F92C`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
