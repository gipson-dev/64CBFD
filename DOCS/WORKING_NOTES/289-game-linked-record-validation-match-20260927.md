# Game linked-record validation match - 2026-09-27

## Result

`func_151002BC` is byte-exact across all 29 tracked words and 116 bytes at
`0x151002BC..0x15100330`. The span contains 26 executable words and three
trailing layout nops. Fresh totals are 2,793 / 5,469 (51.07%) exact C
functions overall and 2,222 / 4,791 (46.38%) in Game.

## Recovery

The false zero-return placeholder now reads the linked entry through the
object state at offset `0x28`. It marks object halfword `0x0E` as `-1` when
the entry is inactive, has type `0xFF`, or does not match the state's selector
against entry byte `0x3B`. A valid matching entry with a non-null pointer at
offset `0x318` subtracts `D_800BE9E4` from the state halfword at offset `0x06`.

Direct C recovered the behavior and register ownership, but IDO emitted only
25 executable words: it rematerialized the invalid sentinel on each failure,
selected likely branches for the first two checks, and omitted retail's
branch-likely child load. Seven guarded scheduling rows insert the one shared
sentinel word and normalize those branch and delay-slot choices. They do not
replace any recovered computation or data value.

## Evidence

Linked ELF offset `0x1402BC` and decompressed retail offset `0x12D76C` compare
equal across the complete 116-byte span. Both have SHA-256
`fad101c81118abf40b4ecbf34251163af098d3f86db815a56c573d4216c7c90f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,793 / 5,469 (51.07%) | 1 | 2,675 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,222 / 4,791 (46.38%) | 0 | 2,569 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching ELF relink, fresh
progress and matcher, independent 116-byte hashes, and direct byte comparison
pass. The replacement build, project tool checks, padding-tool unit tests,
outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 25-word `func_15125490`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
