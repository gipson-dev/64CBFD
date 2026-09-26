# Game translation matrix identity match - 2026-09-26

## Result

`func_150A7DA0` is byte-exact across its complete 20-word, 80-byte retail span
at `0x150A7DA0..0x150A7DEC`. The fresh linked matcher reports 2,684 / 5,483
exact C functions overall and 2,116 / 4,794 in Game.

## Recovered behavior

The function initializes a 4x4 matrix-like block. It stores floating-point
`1.0f` at diagonal offsets `0x00`, `0x14`, `0x28`, and `0x3C`, clears the
remaining rotation words, and copies the caller's three raw `u32` translation
values to offsets `0x30`, `0x34`, and `0x38`.

The previous C wrote `0x3F800000` through a `u32 *`. Although those bits are
the representation of `1.0f`, the integer type made IDO emit integer stores.
Using a 4x4 `f32` view for the diagonal restores retail's shared floating
constant and four `swc1` instructions without changing the raw translation
word contract.

## Compiler boundary

An empty constant-false branch and the label after the first diagonal store
are retained because they make IDO reproduce retail's interleaved store order.
The resulting unguarded object has the correct 20-word extent and store order,
but chooses `f0` instead of retail's `f4` for the shared constant and emits the
last float store before the return. Six guarded rows normalize those
independent choices: four `f0`/`f4` words and the final `swc1`/`jr ra` pair so
the last identity store occupies the return delay slot.

The stale commented non-matching alternative was removed. The patch table now
has 1,125 unique rows and zero duplicate `(filename,function,offset)` keys.

## Exact-byte evidence

The linked ELF `.game+0xA7DA0` span at ELF file offset `0xE7DA0` and pristine
retail `conker.us.bin+0xD5250` span are both 80 bytes and compare equal. Both
hash to:

`a0acd238bcbd6bedcd98c66c0eeb58fe64efddb28dd7aa1b179fecdc5dcc4e96`

The full replacement relink, fresh matcher, exact span comparison, patch-table
duplicate audit, `make tools-check`, all six pad-tool unit tests, outer
non-matching build, and `git diff --check` pass. No gameplay runtime test was
required for this byte-matching type and scheduling correction.

## Sibling audit

`64CBFDOGL` has generated/recompiler references for this function but no
separately maintained host implementation requiring a paired source change.
Its 1,659 existing scoped dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep 17-word `func_150721A4` parked as the known live-C compiler overflow,
keep probable handwritten `func_15125628` out of the ordinary C queue, and
keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership.

Continue with 18-word `func_150ADA20`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior and current object shape before changing source or adding guards.
