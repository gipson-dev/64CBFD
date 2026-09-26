# Game float threshold mapper match - 2026-09-26

## Result

`func_150F34A0` is converted from a zero-return placeholder and byte-exact
across its complete 21-word, 84-byte extent `0x150F34A0..0x150F34F0`. The
fresh matcher reports 2,686 / 5,482 exact functions overall and
2,118 / 4,793 in Game.

## Recovered behavior

The routine accepts an owner pointer followed by a floating-point input. For
inputs below `-5.0f`, it returns:

`arg1 * D_800A1980 + D_800A1984`

For all other inputs it returns `0.75f`. Its sole retail caller passes the
float from stack offset `0x6C` while retaining its owner pointer in `a0`, then
uses the returned `f0` value as a local scalar.

## Source and ABI evidence

The old `s32 func_150F34A0(void)` declaration could only emit a three-word
zero-return placeholder. The retail entry moves `a1` into `f12`, homes `a0`
at `0(sp)`, and returns through `f0`, proving the mixed pointer/float argument
ABI and floating-point result.

A local `f32 result` with an `if`/`else` reproduces the complete retail body
directly. IDO emits the same argument home store, `-5.0f` and `0.75f`
constants, `bc1fl` delay-slot assignment, independent `D_800A1980` and
`D_800A1984` relocations, multiply/add schedule, shared `f2` result, and final
`mov.s f0,f2`. No guarded patch rows are required.

## Exact-byte evidence

The linked ELF `.game+0xF34A0` span at ELF file offset `0x1334A0` and pristine
retail `conker.us.bin+0x120950` span are both 84 bytes and compare equal. Both
hash to:

`6d6c36748842f9c5cbab4fb19be66043bbefb79055a5b5e4cfe1625bcda8dd9d`

The focused object build, complete replacement link, fresh matcher, exact-span
comparison, outer build, project-tool checks, six pad-tool unit tests, and
whitespace audit pass.

## Sibling audit

`64CBFDOGL` has no separately maintained host implementation. Its already
dirty generated `recomp_out/.c` currently reflects the old three-word
zero-return placeholder for this routine, so host parity is not yet implied by
the decomp match. That generated output was left untouched for a later
controlled regeneration from the corrected guest input. The sibling's 1,659
existing dirty entries were preserved. Frozen Release was not built, modified,
or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership,
keep 17-word `func_150721A4` parked as the known live-C compiler overflow, and
keep probable handwritten `func_15125628` outside the ordinary C queue.

Continue with 20-word `func_150FADC8`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior, relocations, and current object shape before editing source.
