# Game two-event release callback match - 2026-09-26

## Result

`func_151D8D5C` is byte-exact across all 22 words and 88 bytes at
`0x151D8D5C..0x151D8DB4`. Fresh totals are 2,717 / 5,469 exact C functions
overall and 2,146 / 4,791 in Game.

## Recovery

The routine is a three-argument callback accepting an object pointer, an
unused float, and an event byte. Event `0x58` releases the object through
`func_1516972C`; event `0x47` performs the same release through a second call
site. Every other event returns without action.

Typing the callback as object/float/byte reproduces retail's stack home for the
unused middle `$a1` float bits and its incoming `$a2` home, byte mask, and
normalized event lifetime. Expressing the two accepted values as explicit
`if` and `else if` branches retains retail's separate call sites, branch over
the second comparison after `0x58`, and branch-likely epilogue for rejected
events.

## Evidence

Linked ELF offset `0x218D5C` and decompressed retail offset `0x20620C` compare
equal for 88 bytes, both with SHA-256
`dbb07e5309308e508f7a463a934b4a9c6499b6129bff1d6e74dbc0b015987aac`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,717 / 5,469 (49.68%) | 1 | 2,751 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,146 / 4,791 (44.79%) | 0 | 2,645 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object and link, full replacement build, fresh progress and
matcher, independent span comparison, project tool checks, all six padding
unit tests, outer build, and `git diff --check` pass. No retail-word patch is
used for this function.

## Next boundary

Continue with 20-word `func_15083FB0`, the smallest unparked Game candidate in
the fresh 19-real-difference tier. Keep the measured compiler boundaries for
`func_150721A4`, `func_150F1684`, `func_15155FD4`, and the
`func_151A8584`/`func_151A85D4` pair parked unless new evidence appears.
