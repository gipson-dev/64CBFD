# Game volatile callback dispatch match - 2026-09-26

## Result

`func_151D73A8` is byte-exact across all 23 words and 92 bytes at
`0x151D73A8..0x151D7404`. Fresh totals are 2,701 / 5,469 exact C functions
overall and 2,130 / 4,791 in Game.

## Recovery

The function narrows its third argument to a byte, uses the object's byte at
offset `0x2C` to select a callback from `D_8008FCA4`, and invokes a non-null
entry with the original three arguments.

The previous C body was behaviorally correct but IDO common-subexpression
reduced the table access to one index load and one entry load, producing only
18 instructions. Retail intentionally loads the index and callback entry
twice while retaining the table base in `v0`. A local table-base pointer whose
entries are volatile, combined with explicit volatile byte reads for each
index expression, reproduces both accesses and all 23 retail words. The
callback itself remains fully typed.

## Evidence

Linked ELF offset `0x2173A8` and decompressed retail offset `0x204858` compare
equal for 92 bytes, both with SHA-256
`57531c17795eef924bf98ddf2b9a699f1dac86900db25b0a68b855dada588fee`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,701 / 5,469 (49.39%) | 1 | 2,767 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,130 / 4,791 (44.46%) | 0 | 2,661 |
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

Continue ordinary Game matching with 20-word `func_1502E474`, the next
unparked nonblocked Game row at 19 differences. Keep the measured
`func_151A8584`/`func_151A85D4` callback-scheduling pair parked. Init
alternative `func_10001000` remains at 14 differences; keep address-blocked
`func_10012588` parked.
