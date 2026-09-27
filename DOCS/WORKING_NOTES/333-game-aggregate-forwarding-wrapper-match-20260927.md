# Game aggregate forwarding wrapper match - 2026-09-27

## Result

`func_15049260` is byte-exact across all 27 words and 108 bytes at
`0x15049260..0x150492CC`. Fresh totals are 2,837 / 5,469 (51.87%) overall and
2,265 / 4,791 (47.28%) in Game.

## Recovery

The retail wrapper receives one 36-byte, nine-word aggregate by value and
forwards that aggregate unchanged to `func_150AAD98`. The prior C prototype
modeled nine independent integer arguments, which preserved behavior but
lost the original aggregate ABI and its generated copy loop.

Defining the argument as a nine-word struct reproduces retail directly. IDO
spills the four register-carried words to their incoming argument slots,
copies all 36 bytes into the outgoing area in a three-word loop, reloads
`a0..a3`, and calls the target with the remaining words already on the stack.
No guarded word patches are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x766E0` and pristine retail span at
`conker.us.bin+0x76710` compare equal for all 108 bytes. Both have SHA-256
`cf413bcb9875e8025308d33beffc2313e7dd55575a4fe5a097c866357053ca3f`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,837 / 5,469 (51.87%) | 1 | 2,631 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,265 / 4,791 (47.28%) | 0 | 2,526 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, full relink, fresh matcher, independent linked-span
hashes, and direct byte comparison pass. The replacement build, outer ROM
build, project tool checks, all nine unit tests, guard-table audit, and
whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 25-word Game `func_1507A100`, the next unparked C row at 24 real
differences. It writes a packed two-byte value into an indexed path record;
keep the documented smaller SDK/compiler-special rows parked.
