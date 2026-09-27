# Game seven-argument forwarding wrapper match - 2026-09-27

## Result

`func_150FFCC8` is byte-exact across all 25 words and 100 bytes at
`0x150FFCC8..0x150FFD2C`. Fresh totals are 2,840 / 5,469 (51.93%) overall and
2,268 / 4,791 (47.34%) in Game.

## Recovery

The wrapper accepts five arguments and forwards them unchanged to
`func_151D5A18`. It appends the word in `D_8008FC8C` and the byte addressed by
`D_8008FC94` as the sixth and seventh arguments. It then returns
`func_151D3E6C(arg0, arg1, arg1, 0x8003A)`.

The explicit five-argument signature makes IDO preserve the retail caller-
stack load for the fifth argument. Plain old-style declarations for both
callees retain the seven-argument call ABI and reproduce retail's argument
save/reload schedule. No guarded words are required.

## Evidence

The rebuilt span at `build/conker.us.bin+0x12D148` and pristine retail span at
`conker.us.bin+0x12D178` compare equal for all 100 bytes. Both have SHA-256
`5d1665206f529f78d841815deae9bea9fb5eb553f80dee8c15d26e5acc284415`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,840 / 5,469 (51.93%) | 1 | 2,628 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,268 / 4,791 (47.34%) | 0 | 2,523 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, independent linked-
span hashes, and direct byte comparison pass. The broader replacement,
outer-ROM, tool, unit-test, guard-table, and whitespace checks also pass. All
nine unit tests pass, and the 1,460-row guard table has zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 26-word Game `func_1510448C`, the next ordinary unparked row in
the fresh 24-real-difference queue. Keep the documented smaller
SDK/compiler-special rows parked.
