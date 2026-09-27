# Game embedded-owner release handler match - 2026-09-26

## Result

`func_151A4F7C` is byte-exact across all 21 words and 84 bytes at
`0x151A4F7C..0x151A4FD0`. Fresh totals are 2,699 / 5,469 exact C functions
overall and 2,128 / 4,791 in Game.

## Recovery

The function handles event byte zero by comparing the embedded record at
object offset `0x28` against the incoming record. It compares the leading
32-bit owner first, then compares the byte discriminator at offset 4 only if
the owners differ. A match in either field releases the object through
`func_1516972C`.

Initializing the embedded-record pointer directly from `arg0 + 0x28` places
that address calculation in retail's opening branch delay slot. A direct
short-circuit `||` reproduces the word loads, first equality branch, deferred
byte loads, and branch-likely cleanup path. All words compile directly from
typed C without guarded retail words or compiler-steering expressions.

## Evidence

Linked ELF offset `0x1E4F7C` and decompressed retail offset `0x1D242C` compare
equal for 84 bytes, both with SHA-256
`0bd405af9a6aebab3730df73a5236f99bdc9e8078ae9b36038f9554135498794`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,699 / 5,469 (49.35%) | 1 | 2,769 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,128 / 4,791 (44.42%) | 0 | 2,663 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling and validation

`64CBFDOGL/recomp_out/.c` still contains the old two-instruction zero-return
generated body; a future controlled regeneration must consume this restored
guest function. The sibling's 1,659 dirty entries and frozen Release
executable remain untouched.

The focused object, full replacement link, fresh progress and LIST matcher,
independent span comparison, tool checks, six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with 20-word `func_151A8584`, the next
nonblocked Game row at 18 differences. Its adjacent 20-word partner
`func_151A85D4` has the same current score. Init alternative `func_10001000`
remains at 14 differences; keep address-blocked `func_10012588` parked.
