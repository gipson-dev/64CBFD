# Game cached render-mode wrapper match - 2026-09-27

## Result

`func_15142FBC` is byte-exact across all 34 words and 136 bytes at
`0x15142FBC..0x15143044`. Fresh totals are 2,822 / 5,469 (51.60%) overall and
2,250 / 4,791 (46.96%) in Game.

## Recovery

The existing C behavior was correct but its combined equality test sent both
failed comparisons into the update path. Expressing the inverse cache-mismatch
block makes IDO branch the second successful comparison directly to retail's
shared return. A retained `Gfx *cmd = arg0++` also restores the command pointer
used after an optional pipe sync.

Three guarded words rotate the independent cursor increment, first cached-word
store, and second cached-word HI16 setup into retail order. The relocation is
moved with its `lui`; no address is baked into the table.

## Evidence

The rebuilt span at `build/conker.us.bin+0x17043C` and pristine retail span at
`conker.us.bin+0x17046C` compare equal for all 136 bytes. Both have SHA-256
`2f32966b66192dae3b5e58437d96dc69ea5606a1b676b41966996d9d980460ea`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,822 / 5,469 (51.60%) | 1 | 2,646 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,250 / 4,791 (46.96%) | 0 | 2,541 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused build/disassembly, required full guard-table rebuild, linked
matcher, direct comparison, replacement build, outer ROM build, tool checks,
all seven relocation tests, guard-table validation, and whitespace check pass.
The guard table now has 1,415 rows with zero duplicate keys.

## Sibling boundary

The sibling `64CBFDOGL` retains its 1,659 pre-existing status entries. Frozen
Release was not built, modified, or launched; `conker_pc.exe` remains
13,712,896 bytes with timestamp `2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word Game `func_15143DA8`, the next ordinary unparked C row at
23 real differences. Keep the documented smaller special-case rows parked.
