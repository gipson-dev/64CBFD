# Game packed four-byte reader match - 2026-09-26

## Result

All 16 words of `func_1507A3E8` now match retail across
`0x1507A3E8..0x1507A428`. The linked matcher reports `2613 / 5484 (47.65%)`
overall and `2045 / 4795 (42.65%)` game, with one address-drift blocker and
2,870 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine reads `D_800D1890` through `D_800D1893` and packs the four bytes
into one big-endian 32-bit result. Its source expression, 16-word extent,
return, and semantics were already correct. Thirteen words differed because
IDO evaluated and scheduled the four independent loads and OR-tree using a
different set of temporaries.

The existing source investigation had already exhausted useful structural
forms. Reordering terms fixed some loads but reversed OR operands. Chained
`|=` selected a named accumulator register. Four byte locals fixed load order
but changed the allocation class, while volatile declarations changed address
formation. Swapping the inner pair still hoisted address loads instead of
keeping retail's adjacent HI16/LO16 pairs. The plain expression was therefore
retained.

Thirteen expected-word guards reproduce retail's schedule. The first three
globals are loaded adjacently into `t7`, `t0`, and `t4`; the first byte is
shifted before the fourth address is materialized and loaded into `t9`.
Retail then merges through `t8`/`t1`, `t2`, `t5`, and `t6`. The guards
explicitly move and validate every `R_MIPS_HI16`/`R_MIPS_LO16` pair for
`D_800D1890` through `D_800D1893`. The opening address load and final
`jr`/`nop` are source-emitted and exact.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0xA7868` and pristine
retail `conker/conker.us.bin+0xA7898` are byte-identical for 64 bytes and share
SHA-256
`c542b461c15efeba5d814856ab3ff92fc74b2482448be8462a1718c97a228e9d`.
The patch table contains 803 rows, zero duplicate keys, and thirteen rows for
this function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 17-word `func_1507FF94`, now the first game row with thirteen
real differences. Inspect its source, relocation ownership, and current versus
retail instruction schedule before choosing source reshaping or guarded words.
