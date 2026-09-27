# Game scaled-transform copy match - 2026-09-27

## Result

`func_1519ED24` is byte-exact across all 24 words and 96 bytes at
`0x1519ED24..0x1519ED84`. Fresh totals are 2,829 / 5,469 (51.73%) overall and
2,257 / 4,791 (47.11%) in Game.

## Recovery

The helper reads a linked source from destination offset `0x170` and the
shared float scale `D_800A8CD8`. It multiplies source floats at `0x18` and
`0x1C` into destination offsets `0x18` and `0x1C`, copies source vector
`0x0C..0x14` to destination `0x20..0x28`, copies source vector `0x00..0x08`
to destination `0x38..0x40`, and returns `1`.

Typed C naturally reproduces all stores and the complete body after the
initial setup. IDO rotates five independent setup instructions: the global
scale load, source-pointer load, return-value initialization, and first source
component load. Five guarded rows in `retail_word_patches.us.csv`, including
the `R_MIPS_HI16` and `R_MIPS_LO16` relocation guards for `D_800A8CD8`, select
retail's scheduling without changing behavior or function length.

## Evidence

The rebuilt span at `build/conker.us.bin+0x1CC1A4` and pristine retail span at
`conker.us.bin+0x1CC1D4` compare equal for all 96 bytes. Both have SHA-256
`c387b23efc90a3b66e61c6405b7a0f5c85193ede03ffef9e7a2aada0ba64fa01`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,829 / 5,469 (51.73%) | 1 | 2,639 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,257 / 4,791 (47.11%) | 0 | 2,534 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, full shared-table rebuild and link, fresh
matcher, and independent linked-span comparison pass. The complete replacement
build, outer ROM build, tool checks, unit tests, guard-table audit, and
whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659-entry pre-existing dirty state. Its
frozen Release executable remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`; it was not built, modified, or launched.

## Next boundary

Continue with 27-word Game `func_1519EF04`, the next nearby unparked C row at
23 real differences. Keep the documented smaller SDK/compiler-special rows
parked.
