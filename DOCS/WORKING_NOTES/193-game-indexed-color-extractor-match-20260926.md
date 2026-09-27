# Game indexed color extractor match - 2026-09-26

## Result

`func_15187FC0` is byte-exact across all 20 words and 80 bytes at
`0x15187FC0..0x15188010`. Fresh totals are 2,696 / 5,469 exact C functions
overall and 2,125 / 4,791 in Game.

## Recovery

The function accepts a signed record index and a three-word output buffer. It
leaves the output untouched unless the index is in the half-open range
`[0, D_800DF7B4)`. For a valid index, it selects a 36-byte record from
`D_800DF700`, reads the unsigned bytes at offsets 6, 7, and 8, and writes their
zero-extended values to output offsets 0, 4, and 8.

Nested bounds checks reproduce retail's opening `slt`, `beqz`, and `bltz`
sequence. Expressing the record address as `&D_800DF700[arg0 * 36]` reproduces
the exact shift/add multiplication and base-address lifetime. The three byte
loads and word stores then compile directly with no guarded retail words or
compiler-steering expressions.

## Evidence

Linked ELF offset `0x1C7FC0` and decompressed retail offset `0x1B5470` compare
equal for 80 bytes, both with SHA-256
`24ab31b6bdb61df664e09424955ba7447d6ef120f39a5300999b79db4b371b1a`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,696 / 5,469 (49.30%) | 1 | 2,772 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,125 / 4,791 (44.35%) | 0 | 2,666 |
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

Continue ordinary Game matching with 21-word `func_15190400`, the next
nonblocked Game row at 18 differences. Init alternative `func_10001000`
remains at 14 differences; keep address-blocked `func_10012588` parked.
