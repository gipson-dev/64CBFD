# Game angle normalization match - 2026-09-26

## Result

`func_15144B68` is byte-exact across all twenty-four words at
`0x15144B68..0x15144BC8`. The linked matcher reports
`2619 / 5483 (47.77%)` overall and `2051 / 4794 (42.78%)` game, with one
address-drift blocker and 2,863 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

The function normalizes an input float into the range beginning at zero and
bounded by `D_800A56A4`. Retail copies the input from `f12` into `f2`, keeps
zero in `f12`, repeatedly subtracts the period while the value is above it,
then repeatedly adds the period while the value is negative.

The original C updated `arg0` directly, causing IDO to keep the evolving value
in `f12` and zero in `f2`. Introducing a named `ret` local reproduced retail's
register allocation, loop structure, branch-likely instructions, and both
branch-delay updates. An explicit `if`/`do`/`else` probe exceeded the fixed
retail span and was rejected. Compact source forms consistently left only the
same independent opening compare and move in the opposite order.

Two expected-word-guarded replacements at offsets `0x008` and `0x00C` swap
those independent scheduling words. They do not change control flow or move a
relocation. The exhaustive non-matching rebuild, link, fresh matcher, outer
build, and project tool checks passed. Linked
`conker/build/conker.us.bin+0x171FE8` and pristine retail
`conker/conker.us.bin+0x172018` are byte-identical for 96 bytes and share
SHA-256
`3092544aa3402e37d36842a0d1fec70e2bb75c61795fef11a33a3c7e0aefc9f2`.
The patch table contains 823 rows, zero duplicate keys, and two rows for this
function.

The `64CBFDOGL` sibling contains recompilation metadata and a stub declaration
for this address, but no maintained host implementation to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 17-word `func_1518F858`, now the first game row with thirteen
real differences. Its generated C conditionally dispatches through
`D_8008D680` using the signed byte at object offset `0x89`; compare that source,
the retained slice assembly, current padded object, and linked retail words
before deciding whether the mismatch is structural or scheduling-only.
