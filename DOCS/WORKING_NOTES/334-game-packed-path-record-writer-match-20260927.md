# Game packed path-record writer match - 2026-09-27

## Result

`func_1507A100` is byte-exact across all 25 words and 100 bytes at
`0x1507A100..0x1507A164`. Fresh totals are 2,838 / 5,469 (51.89%) overall and
2,266 / 4,791 (47.30%) in Game.

## Recovery

The helper selects a path table through `D_800D154C->unk13F`, chooses the
eight-byte record indexed by `D_800D1890`, and uses `D_800D1891` as a
halfword subindex at offset `0x8`. It stores a value whose signed high byte is
`D_800D1892` and whose low byte is `D_800D1893`.

The prior C expressed the destination as record index `D_800D1890 + 1`, which
made IDO emit an extra `addiu` and overflow the retail slot by three words.
Separating the packed value and expressing the destination as the current
record plus an eight-byte field offset restores the retail size and first 19
words. Six guarded words preserve retail's equivalent terminal register chain,
including the `D_800D1891` relocation pair. No instructions are inserted or
omitted.

## Evidence

The rebuilt span at `build/conker.us.bin+0xA7580` and pristine retail span at
`conker.us.bin+0xA75B0` compare equal for all 100 bytes. Both have SHA-256
`8ad8feeacaca9d8b4ac2246da3caa2172958223c80920410221ea0dd92c9d4da`.

| Section | C functions | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,469 / 6,041 (90.53%) | 2,838 / 5,469 (51.89%) | 1 | 2,630 |
| Init | 497 / 538 (92.38%) | 391 / 497 (78.67%) | 1 | 105 |
| Game | 4,791 / 5,321 (90.04%) | 2,266 / 4,791 (47.30%) | 0 | 2,525 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

## Validation

The focused object build, exhaustive rebuild and relink, fresh matcher,
independent linked-span hashes, and direct byte comparison pass. The
replacement build, outer ROM build, project tool checks, all nine unit tests,
guard-table audit, and whitespace check also pass.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with 27-word Game `func_150829D8`, the next unparked C row at 24 real
differences. Keep the documented smaller SDK/compiler-special rows parked.
