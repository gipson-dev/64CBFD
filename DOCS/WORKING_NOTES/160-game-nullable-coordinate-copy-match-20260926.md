# Game nullable coordinate-copy match - 2026-09-26

## Result

`func_1511F92C` is converted from a zero-return placeholder and byte-exact
across its complete 21-word, 84-byte retail span at
`0x1511F92C..0x1511F980`. The fresh linked matcher reports 2,672 / 5,483
exact C functions overall and 2,104 / 4,794 in Game.

## Recovered behavior

The function passes the destination object's byte at offset `0x3F` to
`func_151149AC`. A null lookup result leaves the destination unchanged. A
nonnull result supplies three signed halfwords at offsets `0x10`, `0x12`, and
`0x14`, which are copied to the same offsets in the destination object.

The local declaration of `func_151149AC` now records the pointer return used
by this generated slice instead of relying on the placeholder's implicit
integer contract.

## Compiler boundary

An explicit retained destination pointer gives IDO retail's `a1` lifetime.
The compiler spills `a1` to its argument-home slot in the call delay slot,
reloads it in the null-test delay slot, then emits all three `lh`/`sh` pairs
and the exact frame teardown. The generated-slice padder retains the three
authored trailing nops inside the retail span.

Every instruction matches directly from C. No guarded word rows were needed,
and the patch table remains at 1,111 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x14CDAC` and pristine retail
`conker.us.bin+0x14CDDC` spans are both 84 bytes and compare equal. Both hash
to:

`8640e14c5975fc467cd18311e1eb4d66accd1db351c5dad86efe81635ba5440b`

The focused object build, non-matching relink and objcopy binary, fresh
matcher, exact span comparison, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching change.

## Sibling audit

`64CBFDOGL` references `func_1511F92C` through generated recompilation,
symbol, and animation-configuration artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and
size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 18-word `func_15130374`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
