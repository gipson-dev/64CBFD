# Game selector init wrapper match - 2026-09-26

## Result

`func_1509E8A0` is converted from a zero-return placeholder and byte-exact
directly from C across its complete 24-word, 96-byte padded retail span at
`0x1509E8A0..0x1509E8FC`. The fresh linked matcher reports 2,681 / 5,483 exact
C functions overall and 2,113 / 4,794 in Game.

## Recovered behavior

The function is a three-argument callback wrapper. It dispatches selector
value `7` to `func_1000E0F8(arg0)`, selector value `8` to
`func_1000E8F0(arg0)`, and returns zero for every other selector. The third
argument is not read by the C behavior but is part of the callback contract.

Retail spills incoming `a2` above its 24-byte frame, proving that third
argument even though the selected initializer calls only consume `arg0`.

## Source reconstruction

Two independent `if` returns recovered the calls and frame but made IDO invert
the first comparison. Expressing the selector as a two-case `switch` produces
retail's two forward equality branches, default zero path, direct calls, and
shared epilogue. All 22 executable words and the two trailing padded no-ops
match directly from C.

No guarded word rows were added. The patch table remains at 1,116 unique rows
with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The linked ELF `.game+0x9E8A0` span at ELF file offset `0xDE8A0` and pristine
retail `conker.us.bin+0xCBD50` span are both 96 bytes and compare equal. Both
hash to:

`6cb20288b9c0d04cb6020064f8ce112235044f1ac1eff97063a03cdad6d33617`

The focused generated-object build, full replacement relink, fresh matcher,
exact span comparison, patch-table duplicate audit, replacement/outer
non-matching build, `make tools-check`, all six project-tool unit tests, and
`git diff --check` pass. No gameplay runtime test was required for this
byte-matching callback restoration.

## Sibling audit

`64CBFDOGL` contains this function only in generated `recomp_out/.c`; no
separately maintained host implementation needs a paired change. Its 1,659
existing scoped dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 21-word `func_150A34B0`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
