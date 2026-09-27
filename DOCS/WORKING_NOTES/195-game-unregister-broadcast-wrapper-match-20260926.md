# Game unregister-and-broadcast wrapper match - 2026-09-26

## Result

`func_15191B8C` is byte-exact across all 21 words and 84 bytes at
`0x15191B8C..0x15191BD8`. Fresh totals are 2,698 / 5,469 exact C functions
overall and 2,127 / 4,791 in Game.

## Recovery

The function snapshots the word at `D_800A8010`, unregisters the supplied
target and byte tag through `func_151494E0`, then broadcasts the snapshot as a
kind-1 record through `func_15169260` with the same target and tag.

A one-word local record reproduces retail's stack slot at `sp+0x1C` and the
global load stored in the first call's delay slot. Declaring the second formal
as `u8` reproduces both big-endian ABI reloads from `sp+0x27`. The complete
wrapper matches directly from typed C without guarded retail words or
compiler-steering expressions.

## Evidence

Linked ELF offset `0x1D1B8C` and decompressed retail offset `0x1BF03C` compare
equal for 84 bytes, both with SHA-256
`bf392e47a547c97973ce4acb9c2d4e4fb27927996a73ec68d090289742bfc0cc`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,698 / 5,469 (49.33%) | 1 | 2,770 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,127 / 4,791 (44.40%) | 0 | 2,664 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Sibling and validation

`64CBFDOGL/recomp_out/.c` already contains the complete generated recomp body,
so no sibling regeneration is needed. The sibling's 1,659 dirty entries and
frozen Release executable remain untouched.

The focused object, full replacement link, fresh progress and LIST matcher,
independent span comparison, tool checks, six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with 21-word `func_151A4F7C`, the next
nonblocked Game row at 18 differences. Init alternative `func_10001000`
remains at 14 differences; keep address-blocked `func_10012588` parked.
