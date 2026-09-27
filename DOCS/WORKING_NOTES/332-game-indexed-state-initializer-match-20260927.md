# Game indexed state initializer match - 2026-09-27

## Result

`func_1503F108` is byte-exact across all 25 words and 100 bytes at
`0x1503F108..0x1503F16C`. Fresh totals are 2,836 / 5,469 (51.86%) overall and
2,264 / 4,791 (47.26%) in Game.

## Recovery

The helper selects the 16-byte `D_800C6660` entry for `arg0`, writes the
halfword `0x8C` at offset `0xC`, and writes `6` to the matching object field at
`D_800CC364 + arg0 * 0x32C`. It then follows the entry's leading pointer and
stores `10.0f` at offset `0x1EC`.

Typed C reproduces retail's two strength-reduced index calculations and their
interleaved schedule, the global-address relocations, the halfword and word
stores, the pointer load, floating-point constant materialization, and return
tail. Narrow casts preserve the retail field widths where the current partial
struct definitions do not model them. No guarded word patches are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x6C588` and pristine retail span at
`conker.us.bin+0x6C5B8` compare equal for all 100 bytes. Both have SHA-256
`ae4ee765731e161dc2b0b5475eeb4d1f83d597aa03a16a75dd2b18002070592f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,836 / 5,469 (51.86%) | 1 | 2,632 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,264 / 4,791 (47.26%) | 0 | 2,527 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused generated-object build, full relink, fresh matcher, independent
linked-span hashes, and direct byte comparison pass. The replacement build,
outer ROM build, project tool checks, all nine unit tests, guard-table audit,
and whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 27-word Game `func_15049260`, the next unparked C row at 24 real
differences. It forwards nine integer arguments to `func_150AAD98`; keep the
documented smaller SDK/compiler-special rows parked.
