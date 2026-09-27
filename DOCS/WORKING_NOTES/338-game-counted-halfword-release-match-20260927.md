# Game counted halfword release match - 2026-09-27

## Result

`func_1510D630` is byte-exact across all 25 words and 100 bytes at
`0x1510D630..0x1510D694`. Fresh totals are 2,842 / 5,469 (51.97%) overall and
2,270 / 4,791 (47.38%) in Game.

## Recovery

The allocation begins with a signed halfword count followed by that many
signed halfword entries. The helper walks the entries, passes each one to
`func_1510D694`, and finally releases the original allocation through
`func_10004074`.

Keeping an explicit `allocation` alias makes IDO retain the original pointer
in `$a1`, spill it only across the callback loop, and form the end pointer as
`allocation + count + 1`. Writing the loop condition as `end != entry`
preserves retail's `$s1,$s0` branch operand order. All 25 words compile
directly from C without guards.

## Evidence

The rebuilt span at `build/conker.us.bin+0x13AAB0` and pristine retail span at
`conker.us.bin+0x13AAE0` compare equal for all 100 bytes. Both have SHA-256
`b9daef576d039ea0ae4a4688e13a98f687a438a57216ee6b3ca60d49774d7ed7`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,842 / 5,469 (51.97%) | 1 | 2,626 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,270 / 4,791 (47.38%) | 0 | 2,521 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, independent linked-
span hashes, and direct byte comparison pass. The broader replacement,
outer-ROM, tool, unit-test, guard-table, and whitespace checks also pass. All
nine unit tests pass, and the 1,466-row guard table has zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 25-word Game `func_151148A8`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
