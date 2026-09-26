# Game scaled table reader match - 2026-09-26

## Result

`func_150881CC` is byte-exact across its complete 19-word, 76-byte retail span
at `0x150881CC..0x15088214`. The fresh linked matcher reports 2,679 / 5,483
exact C functions overall and 2,111 / 4,794 in Game.

## Recovered behavior

The function reads the global table pointer `D_800872A0` and returns zero when
the table is absent. Otherwise it selects the `0x84`-byte record at the
caller's signed index, reads the record's leading float, multiplies it by
`256.0f`, and truncates the result to `s32`.

The existing C body already expressed that behavior correctly. Its unguarded
IDO output was 18 words and used the incoming argument and final pointer in
different registers from retail.

## Compiler boundary

Five relocation-aware guarded rows preserve retail's compiler shape: the
opening `a0`-to-`a1` index copy, both stride operations through `a1`, and the
final computed pointer and float load through `a0`. The first guard also moves
the `D_800872A0` high relocation one word later, so the inserted index copy
does not hard-code a linked address.

The resulting body reproduces retail's null path, `0x84` stride, float scale,
conversion, return schedule, and both trailing no-ops. The patch table now has
1,116 unique rows and zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The linked ELF `.game+0x881CC` span at ELF file offset `0xC81CC` and pristine
retail `conker.us.bin+0xB567C` span are both 76 bytes and compare equal. Both
hash to:

`227423c851572c4f05742c91087d60334e216d39e9efa44f811ad6dc6b3a92eb`

The focused generated-object build, full replacement relink, fresh matcher,
exact span comparison, patch-table duplicate audit, replacement/outer
non-matching build, `make tools-check`, all six project-tool unit tests, and
`git diff --check` pass. No gameplay runtime test was required for this
byte-matching change.

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

Continue with 30-word `func_15088780`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
