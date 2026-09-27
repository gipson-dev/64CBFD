# Game signed fixed-point clamp match - 2026-09-27

## Result

`func_1515F0AC` is byte-exact across its 24-word, 96-byte tracked span at
`0x1515F0AC..0x1515F10C`. Fresh totals are 2,733 / 5,468 exact C functions
overall and 2,162 / 4,790 in Game.

## Recovery

The routine clamps its float argument to the inclusive upper bound in
`D_800A6524` and the lower bound `-32768.0f`. It truncates the selected value
to a signed integer and stores it in `D_800DCD10[arg1]`.

Direct IDO `-O2 -g3` C produces the complete control flow, register choices,
branch-likely forms, conversion, and store, but emits 25 words. It hoists the
independent `0xC700` lower-clamp `lui` before the first `c.le.s`, then inserts
a hazard `nop` after the compare. Retail places the compare first, fills its
latency slot with that `lui`, and therefore needs only 24 words.

Three guarded entries in `retail_word_patches.us.csv` reorder those two
independent words and omit the now-unneeded `nop`. `pad_generated_object.py`
now supports guarded omission while retaining the existing stale compiled-word
and relocation checks, rejecting patches that request omission and insertion
together. A focused unit test verifies function-size contraction, following
symbol placement, and emitted words.

## Evidence

Linked ELF offset `0x19F0AC` and decompressed retail offset `0x18C55C` compare
equal for all 96 bytes. Both spans have SHA-256
`eb00f652ed78de4e60ec74635e029f60fed83a99c0277df0d27706c69fc97107`.

| Section | C functions | C bytes | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,468 / 6,039 (90.54%) | 1,931,720 / 2,256,728 (85.60%) | 2,733 / 5,468 (49.98%) | 1 | 2,734 |
| Init | 497 / 538 (92.38%) | 148,600 / 164,048 (90.58%) | 390 / 497 (78.47%) | 1 | 106 |
| Game | 4,790 / 5,319 (90.05%) | 1,763,480 / 2,072,880 (85.07%) | 2,162 / 4,790 (45.14%) | 0 | 2,628 |
| Debugger | 181 / 182 (99.45%) | 19,640 / 19,800 (99.19%) | 181 / 181 (100.00%) | 0 | 0 |

## Sibling audit

The sibling `64CBFDOGL` checkout retains 1,659 pre-existing dirty entries;
none were changed. Frozen Release was not built, modified, or launched, and
`build/Release/conker_pc.exe` remains 13,712,896 bytes with timestamp
`2026-09-23 05:04:28`.

## Validation

The focused object and full link, fresh progress and matcher, independent
96-byte span hashes and `cmp`, guarded-omission unit test, replacement build,
project tool checks, padding-tool tests, outer build, and `git diff --check`
pass.

## Next boundary

Continue with 21-word `func_1516706C`, the next unparked Game C row in the
fresh queue, with 20 real differences. Keep `func_150721A4`, the
`func_151A8584`/`func_151A85D4` pair, `func_1506EF5C`, `func_1507A4D4`,
`guMtxIdentF`, `func_150F1684`, and `func_15155FD4` parked.
