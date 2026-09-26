# Game embedded vertex-copy match - 2026-09-26

## Result

`func_1514143C` is byte-exact across all fifteen words at
`0x1514143C..0x15141478`. The linked matcher reports
`2618 / 5483 (47.75%)` overall and `2050 / 4794 (42.76%)` game, with one
address-drift blocker and 2,864 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

The existing C logic was correct: if the vertex pointer at object offset
`0x154` is non-null, copy float components `0x34`, `0x38`, and `0x3C` into its
first three fields. Retail first loads the pointer into `t6` for the null
check, materializes `arg0 + 0x110` in `v0`, and reloads the same pointer from
`0x44(v0)` into `t7`, `t8`, and `t9` before the three stores.

A local nested-structure overlay and a nested parameter type both compiled
back to the original thirteen-word direct-offset body. A register-qualified
volatile base pointer preserved an `arg0 + 0x110` value but moved it before
the branch, created an 8-byte frame, spilled and reloaded the pointer three
times, and expanded the body to twenty words. Those source-only probes were
rejected.

The accepted implementation keeps the clear logical C and uses thirteen
guarded replacements in `retail_word_patches.us.csv`. The patcher's supported
`insert_after` fields add retail's interior-base `addiu` after the branch-delay
`nop` and the final delay-slot `nop` after the moved `jr`. Every row carries an
expected compiler word, so source or compiler drift fails the build rather
than silently applying stale scheduling.

The exhaustive non-matching rebuild, link, fresh matcher, outer build, and
project tool checks passed. Linked `conker/build/conker.us.bin+0x16E8BC` and
pristine retail `conker/conker.us.bin+0x16E8EC` are byte-identical for 60 bytes
and share SHA-256
`ece713344a6d544b52be8d4872c069537905ba5ec0888141d0f8d854a64c9dcb`.
The patch table contains 821 rows, zero duplicate keys, and thirteen rows for
this function.

The `64CBFDOGL` sibling has symbol-map and recompilation-configuration metadata
for this function but no maintained implementation to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 24-word `func_15144B68`, now the first game row with thirteen
real differences. Inspect source, retained assembly, current object code, and
retail bytes before choosing source changes or guarded scheduling.
