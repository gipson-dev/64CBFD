# Game matrix identity element match - 2026-09-26

## Result

`func_150A7CB0` is byte-exact across its complete 20-word, 80-byte retail span
at `0x150A7CB0..0x150A7CFC`. The fresh linked matcher reports 2,683 / 5,483
exact C functions overall and 2,115 / 4,794 in Game.

## Recovered behavior

The function builds a 4x4 matrix-like word block. It places the three caller
values on the first three diagonal positions, clears every other word except
the final diagonal element, and stores floating-point `1.0f` at offset
`0x3C`.

The previous C used integer constant `0x3F800000` for that final element. The
bits were numerically identical in memory, but the type was wrong: IDO emitted
an integer `lui` and `sw` instead of retail's `lui`, `mtc1`, and `swc1`.

## Compiler boundary

Casting the final element to `f32 *` restores retail's genuine floating-point
constant and store. IDO then reproduces the first 17 words directly but moves
the final zero store before the float store. Three guarded rows rotate those
independent words into retail order: float store at `0x40`, `jr ra` at `0x44`,
and the zero store at offset `0x38` in the return delay slot.

The obsolete commented non-matching alternative and fake-label experiment
were removed. The patch table now has 1,119 unique rows and zero duplicate
`(filename,function,offset)` keys.

## Exact-byte evidence

The linked ELF `.game+0xA7CB0` span at ELF file offset `0xE7CB0` and pristine
retail `conker.us.bin+0xD5160` span are both 80 bytes and compare equal. Both
hash to:

`d6a1e950c51300de8a005337398173f3f308e6b4b263fcbaebab1267f8ce93b2`

The focused object build, full replacement relink, fresh matcher, exact span
comparison, patch-table duplicate audit, replacement/outer non-matching build,
`make tools-check`, all six project-tool unit tests, and `git diff --check`
pass. No gameplay runtime test was required for this byte-matching type and
scheduling correction.

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

Continue with 20-word `func_150A7DA0`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
