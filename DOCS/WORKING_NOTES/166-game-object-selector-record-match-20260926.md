# Game object-selector record match - 2026-09-26

## Result

`func_1506AC0C` is converted from a zero-return placeholder and byte-exact
across its complete 19-word, 76-byte retail span at
`0x1506AC0C..0x1506AC58`. The fresh linked matcher reports 2,678 / 5,483
exact C functions overall and 2,110 / 4,794 in Game.

## Recovered behavior

The function builds an eight-byte local record containing the caller's object
pointer in word zero and the object's byte at offset `0x3B` in byte four. It
passes that record to `func_151B7328` with arguments `0`, `8`, `0xFF`, and
`1`.

The restored two-argument callback signature preserves retail's incoming
object and otherwise-unused second argument spills. A typed local structure
records the actual object/selector payload and gives IDO the retail stack
layout directly.

## Compiler boundary

The structure assignment emits retail's 40-byte frame, reloaded object
pointer, word and byte stores, five call arguments, delay slot, and epilogue.
Every instruction matches directly from C. No guarded word rows were needed,
and the patch table remains at 1,111 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x9808C` and pristine retail
`conker.us.bin+0x980BC` spans are both 76 bytes and compare equal. Both hash
to:

`d6b76d7ce1622ade285c6a6b5b364fd243ea0794725e02515fa4990891d223ae`

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

Continue with 19-word `func_150881CC`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
