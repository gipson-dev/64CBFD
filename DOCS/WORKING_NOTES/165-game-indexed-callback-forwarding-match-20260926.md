# Game indexed callback forwarding match - 2026-09-26

## Result

`func_151B82CC` is byte-exact across its complete 19-word, 76-byte retail span
at `0x151B82CC..0x151B8318`. The fresh linked matcher reports
2,677 / 5,483 exact C functions overall and 2,109 / 4,794 in Game.

## Recovered behavior

The function loads a child pointer from `arg0 + 0x98`, reads its selector byte
at offset `0x08`, and selects a callback from `D_8008FB98`. A nonnull callback
receives the original object pointer, integer argument, and byte argument.

The previous C selected and invoked the callback without arguments. Correcting
the callback-table type and forwarding all three inputs restores the actual
contract. Retaining the child pointer in a separate local recovers retail's
`v0` child-pointer and `v1` callback lifetimes.

## Compiler boundary

The corrected callback prototype forces IDO to spill and zero-extend the byte
argument while leaving all three argument registers live for `jalr`. The split
child pointer then emits the exact selector load, table indexing, null branch,
indirect call, and epilogue. Every instruction matches directly from C. No
guarded word rows were needed, and the patch table remains at 1,111 unique
rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x1E574C` and pristine retail
`conker.us.bin+0x1E577C` spans are both 76 bytes and compare equal. Both hash
to:

`e8095c4ad32badb28ba75115586cce130c72a73b44a9c39a00c22ec7f7389baf`

The focused object build, non-matching relink and objcopy binary, fresh
matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` uses generated recompilation artifacts for this guest function;
no separately maintained hand implementation needs a paired change. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 19-word `func_1506AC0C`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
