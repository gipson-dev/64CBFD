# Game vector cross-product restoration - 2026-09-27

## Result

`func_150AD8B0` is restored from a zero-return C placeholder to its original
handwritten 19-word cross-product body at `0x150AD8B0..0x150AD8FC`. The tracked
generated-slice row extends through `0x150AD9A0`, covering one padding word and
the already exact raw vector helpers in `DADB0` and `DAE10`.

Fresh C-only totals are 2,731 / 5,468 (49.95%) overall and 2,160 / 4,790
(45.09%) in Game.

## Classification

The routine computes the three-component cross product of the vectors in
`arg0` and `arg1`, storing the result through `arg2`. Retail interleaves all
six source loads with the multiply/subtract chain, stores the `z` and `x`
components as soon as they are ready, and places the final `y` store in the
`jr ra` delay slot.

Direct component expressions compile to 29 words because output/input aliasing
prevents later loads from moving across earlier stores. Explicit scalar input
snapshots reduce both IDO `-O2` and `-O3` to 21 words, but both retain an FP
hazard `nop` and an empty return delay slot. Named product lifetimes canonicalize
to that same body. The neighboring dot-product and vector-length helpers are
also raw assembly, supporting handwritten math-utility ownership.

The behaviorally equivalent C remains under `#if 0`. A tracked `GLOBAL_ASM`
body preserves the original schedule without inventing compiler patches.

## Evidence

Linked ELF offset `0xED8B0` and decompressed retail offset `0xDAD60` compare
equal for the complete 240-byte tracked span. Both have SHA-256
`7ae7de32b7fe1c2acc411a544cf6b1f5a38233ceb2c6ae35ce0f892d59f65948`.

| Section | C functions | Raw assembly | C bytes | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 571 | 1,931,624 / 2,256,728 (85.59%) | 2,731 / 5,468 (49.95%) | 1 | 2,736 |
| Init | 497 / 538 (92.38%) | 41 | 148,600 / 164,048 (90.58%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 529 | 1,763,384 / 2,072,880 (85.07%) | 2,160 / 4,790 (45.09%) | 0 | 2,630 |
| Debugger | 181 / 182 (99.45%) | 1 | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
240-byte span hashes and `cmp`, replacement build, project tool checks, all
six padding-tool unit tests, outer build, and `git diff --check` pass.

## Next boundary

Keep the documented lower-difference compiler cases parked. Continue with
22-word zero-return placeholder `func_15131C2C`, the next unparked Game C row
in the fresh queue, with 20 real differences.
