# Game three-word aggregate forwarder match - 2026-09-26

## Result

All 20 words of `func_15131D4C` now match retail across
`0x15131D4C..0x15131D9C`. The linked matcher reports `2606 / 5484 (47.52%)`
overall and `2038 / 4795 (42.50%)` game, with one address-drift blocker and
2,877 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function copies three words from `D_800A37F0` into a stack record and
calls `func_15169260(record, 3, arg0, arg1)`. The previous scalar assignments
made IDO batch all three loads into `t6`, `t7`, and `t8` before emitting the
stores. Retail instead retains the source base in `t6` and interleaves its
loads and stores through `at` and `t9`.

Replacing the scalar array with `ThreeWord15D730` and assigning the source as
one aggregate immediately reproduced retail's interleaved copy. With the old
integer callee contract, however, IDO formed the stack destination in `v0`,
copied it to `a0`, and emitted 21 words into the 20-word slot. Declaring the
callee's first argument as `void *`, consistent with neighboring generated
files, removes that conversion: IDO forms the destination directly in `a0`
and emits every retail word. No expected-word guards were needed.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x15F1CC` and pristine
retail `conker/conker.us.bin+0x15F1FC` are byte-identical for 80 bytes and
share SHA-256
`0c3949fd9d561f5442219ef46c00c7ce47d53bf0a05c7263f3e0ff7e392891f0`.
The patch table remains at 762 rows with zero duplicate keys.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 40-word `func_151355B8`, now the first game row with twelve real
differences. Its case-three match path masks bit zero from the word at offset
`0x10`. Retail retains two identical stores of the masked value; current C
optimizes the duplicate statements into one store, leaving a padding word at
the end and shortening three exit branches. Retail also carries the loaded
field in `t5` and the masked result in `t6`, while current C uses `v0` and
`t5`. Test a chained assignment or a volatile-qualified access to retain both
stores before considering guarded register normalization.
