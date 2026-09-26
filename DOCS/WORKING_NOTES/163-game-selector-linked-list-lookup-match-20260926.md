# Game selector linked-list lookup match - 2026-09-26

## Result

`func_15178B98` is converted from a zero-return placeholder and byte-exact
across its complete 19-word, 76-byte retail span at
`0x15178B98..0x15178BE4`. The fresh linked matcher reports 2,675 / 5,483
exact C functions overall and 2,107 / 4,794 in Game.

## Recovered behavior

The function starts at the linked-list head stored in `D_800DCF38`, compares
the caller's byte selector with each node's byte at offset `0x34`, and follows
the next pointer at offset `0x08`. It returns the first matching node pointer
or zero when the list is empty or exhausted.

The existing integer return contract is retained because adjacent generated
wrappers consume the pointer-sized result as an integer. A typed local node
pointer records the actual traversal and memory layout without changing that
ABI.

## Compiler boundary

The direct `while` loop emits retail's two branch-likely instructions, null
head path, matching-node early return, duplicated next-pointer load, and final
zero return exactly. Every instruction matches directly from C. No guarded
word rows were needed, and the patch table remains at 1,111 unique rows with
zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x1A6018` and pristine retail
`conker.us.bin+0x1A6048` spans are both 76 bytes and compare equal. Both hash
to:

`c90feae04990328b11469fe19f238fd17925d37dd5be53fc0c9df139b6c63333`

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

Continue with 18-word `func_1519257C`, the next ordinary Game C row with
seventeen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
