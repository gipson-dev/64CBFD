# Game state-toggle event callback match - 2026-09-27

## Result

`func_1514F130` is byte-exact across all 25 words and 100 bytes at
`0x1514F130..0x1514F194`. Fresh totals are 2,796 / 5,469 (51.12%) exact C
functions overall and 2,225 / 4,791 (46.44%) in Game.

## Recovery

The zero-return placeholder was a three-argument event callback. Its object
contains a state pointer at offset `0x14`; that state has a Boolean byte at
offset 9. Event `0xD` clears the byte and event `0xE` sets it. Both handled
events return one. Every other event forwards all three original arguments to
`func_1514E89C` and returns that function's result.

Typed `GameObjectWithState` and `GameObjectState` structures make those nested
offsets explicit. A two-case switch gives IDO the complete retail instruction
shape on the first faithful implementation: the comparisons against `0xD` and
`0xE`, branch-likely nested-pointer load, two store delay slots, default call,
and duplicated return-address loads all match directly.

No guarded instruction rows or assembly replacements are required.

## Evidence

Linked ELF offset `0x18F130` and decompressed retail offset `0x17C5E0` compare
equal across the complete 100-byte span. Both have SHA-256
`63ea08e9138c95d21ba223d62a809f68cadb1a9455a21ae59f7a0b6841fef142`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,796 / 5,469 (51.12%) | 1 | 2,672 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,225 / 4,791 (46.44%) | 0 | 2,566 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, full nonmatching rebuild and link,
fresh progress and matcher, independent 100-byte hashes, and direct byte
comparison pass. The replacement build, project tool checks, padding-tool
unit tests, outer nonmatching build, and whitespace check also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 24-word `func_1517F7B4`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
