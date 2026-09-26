# Game record/owner match callback - 2026-09-26

## Result

`func_15133DE8` is converted from a zero-return placeholder and byte-exact
across its complete 21-word, 84-byte extent `0x15133DE8..0x15133E38`. The
fresh matcher reports 2,688 / 5,482 exact functions overall and
2,120 / 4,793 in Game.

## Recovered behavior

This three-argument callback first requires its third byte argument to be
zero. It then compares the record's 32-bit identifier at `arg1+0` against the
owner field at `arg0+0x7C`. If those differ, it compares the following record
byte at `arg1+4` against the owner byte at `arg0+0x80`. A match from either
comparison calls `func_1516972C(arg0)`; otherwise the callback returns without
changing state.

## Source and ABI evidence

The old `s32 func_15133DE8(void)` declaration emitted only a three-word
zero-return placeholder. Retail homes and narrows `a2` as an unsigned byte,
uses `a1` as a record pointer, and forwards `a0` unchanged to
`func_1516972C`, establishing the `(owner, record, event-byte)` ABI.

The first typed short-circuit implementation recovered the complete frame,
branches, delay slots, call, and relocation, but used `t7/t8/t9/t0` for the
two comparisons. Naming the 32-bit record identifier as a local lifetime makes
IDO retain it in `v0`, exactly restoring retail's `v0/t7/t8/t9` allocation.
All 21 words then compile directly from C; no guarded patch rows are required.

## Exact-byte evidence

The linked ELF `.game+0x133DE8` span at ELF file offset `0x173DE8` and
pristine retail `conker.us.bin+0x161298` span are both 84 bytes and compare
equal. Both hash to:

`90076a0b24263542cb4bd2d6d371c257b8c5cd3c03c1160ff420bf9ea7cdf8bf`

The focused object build, complete replacement link, fresh matcher, exact-span
comparison, outer build, project-tool checks, six pad-tool unit tests, and
whitespace audit pass.

## Sibling audit

`64CBFDOGL` has no separately maintained host implementation. Its already
dirty generated `recomp_out/.c` currently reflects the old three-word
zero-return placeholder for this routine, so host parity is not yet implied by
the decomp match. That generated output was left untouched for a later
controlled regeneration from the corrected guest input. The sibling's 1,659
existing dirty entries were preserved. Frozen Release was not built, modified,
or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Keep generated `func_151F892C` and `func_151F8960` in raw-assembly ownership,
keep 17-word `func_150721A4` parked as the known live-C compiler overflow, and
keep probable handwritten `func_15125628` outside the ordinary C queue.

Continue with 19-word `func_151444DC`, the next ordinary Game C row with
eighteen real differences in the fresh linked `--list` report. Establish its
behavior, relocations, and current object shape before editing source.
