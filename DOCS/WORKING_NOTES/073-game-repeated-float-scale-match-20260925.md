# Game repeated float-scale match - 2026-09-25

## Result

All 12 words of `func_151318E8` now match retail across
`0x151318E8..0x15131918`. The linked matcher reports `2586 / 5484 (47.16%)`
overall and `2018 / 4795 (42.09%)` game, with one address-drift blocker and
2,897 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The former zero-return placeholder is now the retail repeated float-scale
loop. It loads `D_800BE9E4` as the iteration count and multiplies `arg0[1]`
by the supplied scalar once per iteration. A typed `(f32 *, f32)` boundary
preserves the mixed pointer/float ABI: IDO carries the scalar bits in `a1`
and emits the retail `mtc1 a1,f12` entry word.

The sole in-file caller, `func_151316AC`, now expresses both operands as
floats and remains independently byte-exact. No guarded words were added.
The complete 48-byte target spans at linked `0x15ED68` and retail `0x15ED98`
share SHA-256
`dd1732f04e8fad0d5daed64f7a9833097445188e8d285d53da86220914bb350b`.
The complete 48-byte caller spans at linked `0x15EB2C` and retail `0x15EB5C`
share SHA-256
`22cb90341b57ea50023850f7cab38aaca0afbf2da61e0637c62336feffc0198e`.
The patch table remains at 659 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling uses the ROM-generated recomp body and exposes its
generated declaration and symbol-table entry. It has no hand-maintained
implementation requiring a transplant. Its dirty tree was left untouched,
and frozen Release was not built or launched.

## Next boundary

Continue with 17-word `func_15133A50`, now the first game row with ten real
differences. Compare its placeholder/source model, compact object, retail
words, and relocations before editing.
