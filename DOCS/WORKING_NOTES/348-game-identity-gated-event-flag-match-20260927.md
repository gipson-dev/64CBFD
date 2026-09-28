# Game identity-gated event flag match - 2026-09-27

## Result

`func_151A931C` is byte-exact across all 29 words and 116 bytes at
`0x151A931C..0x151A9390`. Fresh totals are 2,852 / 5,469 (52.15%) overall and
2,280 / 4,791 (47.59%) in Game.

## Recovery

The function handles two event IDs after confirming that the event record's
first byte matches object byte `0x80`. Event `0x17` sets bit `0x1` in object
byte `0x28`; event `0x18` clears that bit. Other IDs and identity mismatches
leave the object unchanged.

Giving the function its real three-argument prototype, including the narrow
third argument, restores the retail argument-home store, byte normalization,
and register flow. That prototype also makes caller `func_151A9024` compile
directly to all 15 retail words, allowing its 13 old scheduling rows to be
removed. Four function-scoped rows remain for `func_151A931C`: two branch
extents and the unscheduled early store/return pair with its delay-slot nop.
The guard table therefore shrinks by nine rows overall.

## Evidence

The rebuilt target span at `build/conker.us.bin+0x1D679C` and pristine retail
span at `conker.us.bin+0x1D67CC` compare equal for all 116 bytes. Both have
SHA-256
`446dc159df56fc710bf2b9167bf56038ddf19db80a6eb46cf527e64adf94fc15`.
The rebuilt and pristine 60-byte `func_151A9024` spans also compare equal.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,852 / 5,469 (52.15%) | 1 | 2,616 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,280 / 4,791 (47.59%) | 0 | 2,511 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, complete relink, fresh matcher, independent target
and caller comparisons, and target hashes pass. The 1,461-row guard table has
zero duplicate `(filename, function, offset)` keys. The broader replacement,
outer-ROM, tool, unit-test, and whitespace checks are run before the commit.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Classify 28-word Game `func_151928B0`, the first undocumented Game row after
the known parked compiler cases in the fresh queue. Keep Init and raw-assembly
conversion as separate workstreams.
