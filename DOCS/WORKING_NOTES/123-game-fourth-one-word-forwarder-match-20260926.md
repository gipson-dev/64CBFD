# Game fourth one-word aggregate forwarder match - 2026-09-26

## Result

`func_15160274` is byte-exact across all nineteen words at
`0x15160274..0x151602C0`. The linked matcher reports
`2635 / 5483 (48.06%)` overall and `2067 / 4794 (43.12%)` game, with one
address-drift blocker and 2,847 total differing C functions. Debugger remains
complete at `181 / 181`.

## Source contract

The function copies the word at `D_800A6670` into a stack record and calls
`func_15169260(record, 1, arg0, arg1)`. Its generated slice still declared the
record parameter as `s32`, although the shared contract and observed callers
establish it as a pointer.

Correcting that local declaration to `void *` and replacing the scalar array
with a `OneWord18D250` aggregate lets IDO emit retail's exact frame, `a2/a3`
argument setup, record address, source HI/LO pair, copy through `at`, call
delay store, epilogue, and three trailing padding words directly. No guarded
rows are required, and the patch table remains at 888 unique rows.

## Evidence

The final linked and pristine 76-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x18D6F4`
- retail `conker/conker.us.bin+0x18D724`
- SHA-256 `497bea249d36ac1992358cdbaa93c18017215abfef7e0bde6ff7fd9b6481f632`

The focused object build, nonmatching relink, fresh direct matcher, outer
build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation code, calls, and
a declaration for this function, with no separately maintained host
implementation to update. Its 1,659 existing dirty entries were left
untouched. Frozen Release was not built, modified, or launched;
`build/Release/conker_pc.exe` retains timestamp `2026-09-23 05:04:28` and size
`13,712,896` bytes.

## Next boundary

Continue with 19-word `func_151BD750`, now the smallest ordinary-C game row
among the fourteen-difference candidates. Retail loads a literal `2.0f`,
converts the halfword at object offset `0x80`, multiplies first by that literal
and then by `D_800AA860`, updates the halfword with `D_800BE9E4` between those
FP operations, and finally adds `D_800AA864`. The current build doubles with
`add.s` and uses a different FP register and scheduling shape. Probe explicit
float temporaries and operation grouping before considering guarded words.
