# Game indexed record lookup match - 2026-09-26

## Result

`func_15086D48` is byte-exact across all 19 words, or 76 bytes, at
`0x15086D48..0x15086D94`. The fresh linked matcher reports 2,658 / 5,483 exact
C functions overall and 2,090 / 4,794 in Game.

## Recovered behavior

The function searches the 16-byte records reached through `D_800D2350`,
bounded by the signed halfword count at `D_80087290`. It returns the first
index whose byte at record offset seven equals `arg0`, or `0xFF` when the count
is non-positive or no record matches.

Replacing the separate byte cursor with
`D_800D2350[(i * 0x10) + 7]` lets IDO preserve the search key in incoming
`a0` and derive the record cursor in `a1`. This removes the surplus argument
copy and directly recovers both global relocation pairs, the branch-likely
match path, and the 16-byte cursor induction.

IDO proves that the guarded unit-step loop can use `i != count`, while retail
retains an explicit signed `i < count` comparison. Six guarded rows restore
that `slt`/`bnez` backedge, extend the empty-record branch, and move the cursor
advance plus `0xFF` fallback epilogue one word later. The patch table now
contains 1,059 rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0xB41C8` and pristine retail span
`conker.us.bin+0xB41F8` are both 76 bytes and compare equal. Both hash to:

`1052c36b9456acec6421f1c3b878089012ad40b723db196c0d41e2d744e785f1`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all project
tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_15086D48` only in generated recompilation and
configuration artifacts, symbol references, and existing investigation notes;
no separate maintained hand implementation was found. Its 1,659 existing
dirty entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Continue with 19-word `func_150F631C`, the next ordinary Game C row
with sixteen real differences. It conditionally passes each non-null pointer
at object offsets `0x30` and `0x34` to `func_1516972C`.
