# Game three-byte record schedule match - 2026-09-26

## Result

All 46 words of `func_1504BA38` now match retail across
`0x1504BA38..0x1504BAF0`. The linked matcher reports `2602 / 5484 (47.45%)`
overall and `2034 / 4795 (42.42%)` game, with one address-drift blocker and
2,881 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The source logic was already correct. All twelve real differences were
register choices in the three-byte record pipeline: the compiler kept the
record pointer in `v0` and reused `v1` for bytes one and two, while retail
keeps the pointer in `v1`, byte two in `a1`, and byte one in `v0`.

Declaration-order, block-scope, early-return/if-else, and unused-argument
K&R/ANSI probes either preserved the same allocation or introduced an unwanted
incoming-argument spill. Twelve same-position guarded words restore the retail
register lifetimes without changing control flow, instruction count, or either
existing `D_80099140` and `D_800991D4` HI16/LO16 relocation pair. No C source
body was changed.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x78EB8` and pristine
retail `conker/conker.us.bin+0x78EE8` are byte-identical for 184 bytes and share
SHA-256 `f6b31137a29e73ab755499f92e5ae0090afb835db155431476753cb081e410b4`.
The patch table contains 735 rows, zero duplicate keys, and twelve rows for
this function.

The `64CBFDOGL` sibling has no hit for this function in its maintained source,
headers, tools, scripts, or documentation. Its 1,659 existing dirty entries
were left untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains its 2026-09-23 timestamp.

## Next boundary

Continue with 13-word `func_150882B0`, now the first game row with twelve real
differences. It is an indexed signed-byte getter over `D_800872A0`. Retail
begins with `move a1,a0`, performs the 132-byte stride arithmetic from `a1`,
and uses `a0` for the final record pointer. Current C optimizes away its `idx`
copy, performs the arithmetic directly from `a0`, and uses `t7` for the final
pointer. The `D_800872A0` HI16/LO16 relocation pair and control flow otherwise
agree; determine whether a source-level argument lifetime can retain the
opening copy before considering a guarded expansion.
