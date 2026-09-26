# Game third one-word aggregate forwarder match - 2026-09-26

## Result

`func_151D343C` is byte-exact across all seventeen words at
`0x151D343C..0x151D3480`. The linked matcher reports
`2633 / 5483 (48.02%)` overall and `2065 / 4794 (43.07%)` game, with one
address-drift blocker and 2,849 total differing C functions. Debugger remains
complete at `181 / 181`.

## Shared contract

The function copies the word at `D_800AB168` into a stack record and calls
`func_15169260(record, 1, arg0, arg1)`. It is the third member of the one-word
aggregate-forwarder family solved in this pass.

The maintained `functions.h` declaration and empty placeholder definition
still typed the record address as `s32`, even though every observed caller
passes a record pointer and several generated slices already declare it as
`void *`. Correcting that shared contract and using a `OneWordCopy` aggregate
lets IDO emit the exact source HI/LO pair, copy through `at`, argument setup,
call delay store, epilogue, and final padding word directly. No guarded rows
are required.

The shared header change rebuilt every affected maintained caller. The fresh
matcher advanced by exactly one function, proving that it introduced no
collateral match regressions.

## Evidence

The final linked and pristine 68-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x2008BC`
- retail `conker/conker.us.bin+0x2008EC`
- SHA-256 `8bbd4d063f5ac36885613ba73e44a6283782e56102abd80040e3ef4f5d8b4e85`

The focused object build, exhaustive header-dependent nonmatching rebuild,
fresh direct matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation declarations and
calls for this function, with no separately maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 18-word `func_1519F3B8`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It fills four words at object
offsets `0x58..0x64`: selector calls `func_1519F1C8(arg0, 6)` and
`func_1519F1C8(arg0, 7)` supply the first and third words, while the second and
fourth are cleared. Compare its retained object/base pointer across both calls
and its interleaved stores against retail before changing source shape.
