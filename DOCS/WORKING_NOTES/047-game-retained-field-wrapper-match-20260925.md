# Game retained-field wrapper match - 2026-09-25

## Result

`func_1513A594` is byte-exact across its complete 19-word linked extent
`0x1513A594..0x1513A5E0`. The fresh C-only matcher reports
`2563 / 5488 (46.70%)` overall and `1995 / 4799 (41.57%)` game. One init
function remains blocked by address drift; 2,924 total and 2,804 game C
functions still differ. Debugger remains complete at `181 / 181`.

## Mismatch and resolution

The wrapper already forwarded the correct values to `func_1513A5E0`, but its
local declaration incorrectly described the second parameter as `s32`.
Retail masks the incoming byte once when receiving it and again when
forwarding it. Correcting the callee declaration to `u8` recovers the second
mask directly from C.

Retail then reloads the original object and reads `arg0->unk1D4`, followed by
a branch whose target is the immediately following epilogue. A volatile field
read preserves the meaningful object and field loads without inventing a
side effect. IDO assigns different registers to those loads and cannot retain
the behaviorally empty branch by itself, so three expected-word-guarded,
non-relocating rows select the retail pointer registers and insert the branch
plus its delay-slot `nop`. The existing call relocation remains untouched.

## Verification

The current checkout passed:

```sh
make build/src/game_161520.c.o
make -j8 build/conker.us.elf
make match-progress NON_MATCHING=1
make match-progress NON_MATCHING=1 LIST=1
make tools-check
```

The focused object contains all 19 retail words and the target is absent from
the non-exact list. The patch table has 543 rows and no duplicate
filename/function/offset keys. An independent comparison of the complete
76-byte linked ELF span at file offset `0x17A594` and pristine extracted
retail span at `conker/conker.us.bin+0x167A44` produced SHA-256
`92d868e180951fab17cafdf85fa155bed52a369b34a935ae5223fc765d7b40b0`
for both.

The `64CBFDOGL` sibling has generated recomp metadata and a host-side lethal
impact test for these symbols, but no hand-maintained implementation. The
IDO-facing prototype/read recovery does not transfer to host source. Its
dirty tree was left untouched, and frozen Release was not built or launched.

## Next boundary

The next listed game target is 27-word `func_151423D8` with seven real
differences. Inspect its source, retail words, relocations, and compiler
schedule before editing.
