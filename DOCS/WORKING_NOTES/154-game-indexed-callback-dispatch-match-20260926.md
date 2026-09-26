# Game indexed callback dispatch match - 2026-09-26

## Result

`func_151635A8` is byte-exact across all 23 words, or 92 bytes, at
`0x151635A8..0x15163604`. The fresh linked matcher reports 2,666 / 5,483
exact C functions overall and 2,098 / 4,794 in Game.

## Recovered behavior

The function uses `arg0->unk25` to select an entry from `D_8008B370`. It
returns immediately when the selected callback is null. Otherwise, it calls
the selected function with `arg0`, `arg1`, and `arg2`; the byte argument is
normalized before dispatch.

The previous declaration described the callback as taking only one `s32`, and
the source cached that pointer in a local before calling it with only `arg2`.
The corrected declaration is a three-argument callback taking
`(struct225 *, s32, u8)`. Direct table expressions restore the null test and
the full call boundary. Qualifying the table entries as volatile preserves
the retail behavior of reading the callback pointer once for the null test
and again for dispatch.

## Compiler boundary

The compact C object emits 20 words in the 23-word retail slot. It keeps the
table base and first indexed slot in different registers, reuses the first
slot address for the second callback-pointer read, and emits a shorter shared
epilogue. Retail loads the table base into `v0`, independently reloads and
scales `arg0->unk25` for dispatch, and schedules its shared epilogue across
the branch-likely and post-call paths.

Fifteen guarded rows in `retail_word_patches.us.csv` normalize seventeen
persistent compiler words. Four rows explicitly move and verify the existing
HI/LO relocation pair, and two rows use checked `insert_after` words to extend
the compact epilogue without patching anonymous padding. Every row verifies
its compiled input and relocation state. The patch table now contains 1,092
unique rows with zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The rebuilt `build/conker.us.bin+0x190A28` and pristine retail
`conker.us.bin+0x190A58` spans are both 92 bytes and compare equal. Both hash
to:

`dc380763ac394a43b8fe7d813d940059454fb61662872bd1514a10c05734eb27`

The focused guarded object build, all-consumer non-matching ELF rebuild,
objcopy binary, fresh matcher, exact span comparison, `make tools-check`, all
six project-tool unit tests, and `git diff --check` pass.

## Sibling audit

`64CBFDOGL` references `func_151635A8` through generated recompilation,
symbol, and configuration artifacts; no separate maintained hand
implementation was found. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow.
Keep probable handwritten `func_15125628` out of the ordinary C matching
queue; raw-assembly ownership remains a separate workstream.

Continue with 20-word `func_15168A4C`, the next ordinary Game C row with
sixteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
