# Game record gate wrapper match - 2026-09-26

## Result

`func_150A34B0` is converted from a zero-return placeholder and byte-exact
directly from C across its complete 21-word, 84-byte retail span at
`0x150A34B0..0x150A3500`. The fresh linked matcher reports 2,682 / 5,483 exact
C functions overall and 2,114 / 4,794 in Game.

## Recovered behavior

The function accepts a byte-addressed record and returns zero immediately when
record byte `0x14` equals `1`. Otherwise it inspects the low two bits of record
byte `0x15`: when either bit is set it returns zero, and when both are clear it
forwards the original record pointer to `func_150A3504` and returns that
callee's result.

An old-style forward declaration for `func_150A3504` permits the recovered
pointer call while preserving that large function's existing zero-return
placeholder body and codegen. Reconstructing `func_150A3504` remains separate
work.

## Source reconstruction

A combined short-circuit condition moved the zero result before the first
branch, while two negative early returns added an extra branch. The matching
shape uses the first early return followed by a positive call condition and a
final zero return. IDO then emits retail's branch-likely duplicated load of
byte `0x15`, preloaded `v0 = 0`, low-bit rejection branch, direct call, and
shared epilogue.

All 21 words match directly from C. No guarded word rows were added; the patch
table remains at 1,116 unique rows with zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The linked ELF `.game+0xA34B0` span at ELF file offset `0xE34B0` and pristine
retail `conker.us.bin+0xD0960` span are both 84 bytes and compare equal. Both
hash to:

`fb9edd181a18b5c89565ce4898cf3549dc72d810b57d7f04578cb572abaddeef`

The focused generated-object build, full replacement relink, fresh matcher,
exact span comparison, patch-table duplicate audit, replacement/outer
non-matching build, `make tools-check`, all six project-tool unit tests, and
`git diff --check` pass. No gameplay runtime test was required for this
byte-matching wrapper restoration.

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

Continue with 20-word `func_150A7CB0`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
