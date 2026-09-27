# Game byte-scaled dispatch match - 2026-09-27

## Result

`func_1510448C` is byte-exact across all 26 words and 104 bytes at
`0x1510448C..0x151044F4`. Fresh totals are 2,841 / 5,469 (51.95%) overall and
2,269 / 4,791 (47.36%) in Game.

## Recovery

The helper returns `arg0` when its signed 16-bit gate is nonzero or byte
`0x1B` of the supplied record is zero. Otherwise it scales that byte by
`63 / 256` and forwards the result to `func_1517F08C` with three zero
arguments and the original signed gate.

The short-circuit condition and address-taken record parameter reproduce the
retail frame, spills, pointer reload, branches, delay slots, and 20 of the 26
words directly. Six guarded words restore one equivalent producer/consumer
register chain: the scaled value uses retail `$a1/$t8`, and the reloaded gate
uses retail `$t9`. No instruction is added, removed, or redirected.

## Evidence

The rebuilt span at `build/conker.us.bin+0x13190C` and pristine retail span at
`conker.us.bin+0x13193C` compare equal for all 104 bytes. Both have SHA-256
`4f28f367f8ab43a3b00119126304196f2ace9b38088f5fe71694993340b6c9bf`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,841 / 5,469 (51.95%) | 1 | 2,627 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,269 / 4,791 (47.36%) | 0 | 2,522 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, exhaustive rebuild and relink, fresh matcher,
independent linked-span hashes, and direct byte comparison pass. The broader
replacement, outer-ROM, tool, unit-test, guard-table, and whitespace checks
also pass. All nine unit tests pass, and the 1,466-row guard table has zero
duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 25-word Game `func_1510D630`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
