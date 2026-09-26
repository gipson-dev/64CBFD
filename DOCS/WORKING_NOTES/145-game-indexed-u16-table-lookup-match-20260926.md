# Game indexed u16 table lookup match - 2026-09-26

## Result

`func_15084CB0` is byte-exact across all 20 words, or 80 bytes, at
`0x15084CB0..0x15084D00`. The fresh linked matcher reports 2,657 / 5,483 exact
C functions overall and 2,089 / 4,794 in Game.

## Recovered behavior

The function searches the `u16` table at `D_800BE598`, bounded by the byte
count in `D_800BE590`. It returns the first index whose entry equals `arg0`,
or zero when the count is non-positive or no entry matches.

Reordering the explicit result, index, and count locals gives retail's `v1`,
`v0`, and `a1` lifetimes. Replacing the separate cursor with
`D_800BE598[i]` lets IDO derive the cursor in `a2` while retaining `arg0` in
`a0`; this removes the surplus argument copy and directly recovers both
global relocation pairs, the branch-likely match path, and the cursor advance.

IDO proves that the guarded unit-step loop can use `i != count`, while retail
retains an explicit signed `i < count` comparison. Seven guarded rows restore
that `slt`/`bnez` backedge, adjust the two exit branches, and move the cursor
advance and epilogue one word later. The patch table now contains 1,053 rows
with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt linked span `build/conker.us.bin+0xB2130` and pristine retail span
`conker.us.bin+0xB2160` are both 80 bytes and compare equal. Both hash to:

`a9ddf6d16d75ad40e7d6a0c112b0bd26ccb05e909e66a23aa428d897fef6ebe8`

Changing the shared patch table triggered an exhaustive rebuild of every
padded consumer. The linked ELF, objcopy binary, fresh matcher, and exact span
comparison pass. The outer nonmatching build, `make tools-check`, all project
tool unit tests, and `git diff --check` also pass.

## Sibling audit

`64CBFDOGL` contains `func_15084CB0` in generated recompilation/configuration
artifacts and symbol references, but no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known three-word live-C compiler
overflow. Continue with 19-word `func_15086D48`, the next ordinary Game C row
with sixteen real differences. It searches the 16-byte records at
`D_800D2350`, using the signed halfword count at `D_80087290`, and returns the
first index whose byte at record offset seven equals `arg0`, or `0xFF` when no
record matches.
