# Game paired-table dispatcher match - 2026-09-27

## Result

`func_150DEC28` is byte-exact across its tracked 26 words and 104 bytes at
`0x150DEC28..0x150DEC90`. Fresh totals are 2,791 / 5,469 (51.03%) exact C
functions overall and 2,220 / 4,791 (46.34%) in Game.

## Recovery

The false zero-return placeholder now narrows its first argument to a byte and
multiplies it by four. The resulting offset selects a byte from `D_800A0D0B`
for `func_151616D0(value, 0x22, 0)`, then the corresponding byte from
`D_800A0D2B` for `func_151417C4(value, 0x22)`. The second incoming byte is
homed by the ABI but otherwise unused.

A modern byte-typed prototype changed the already exact old-style caller, and
promoted `s32` parameters lost retail's first argument home. The compatible
K&R definition with byte parameter declarations reproduces both sides: the
caller remains unchanged, while IDO emits the original argument homes,
`a0`-to-`a3` narrowing, shared scaled offset spill, and call schedule. The
generated slice padder retains three original layout nops after the 23-word
body. No guarded retail words are needed.

## Evidence

Linked ELF offset `0x11EC28` and decompressed retail offset `0x10C0D8` compare
equal across the complete 104-byte span. Both have SHA-256
`631364ff57f69fc8abf662ae782237dd7fcdc1413a777d7270bda3ae3624c8f0`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,791 / 5,469 (51.03%) | 1 | 2,677 |
| Init | 497 / 538 (92.38%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,791 / 5,321 (90.04%) | 2,220 / 4,791 (46.34%) | 0 | 2,571 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build and disassembly, unchanged neighboring caller, full
nonmatching ELF relink, fresh progress and matcher, independent 104-byte
hashes, and direct byte comparison pass. The replacement build, project tool
checks, padding-tool unit tests, outer nonmatching build, and whitespace check
also pass.

## Sibling audit

The sibling `64CBFDOGL` checkout retains its pre-existing dirty state; none of
its files were changed. Frozen Release was not built, modified, or launched.

## Next boundary

Continue with 24-word `func_150F4CFC`, the next unparked Game C row in the
fresh ordered queue at 22 real instruction differences. Keep the documented
lower-difference compiler cases parked unless new source or compiler evidence
appears.
