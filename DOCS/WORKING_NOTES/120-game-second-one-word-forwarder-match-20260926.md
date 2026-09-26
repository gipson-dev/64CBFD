# Game second one-word aggregate forwarder match - 2026-09-26

## Result

`func_151A561C` is byte-exact across all seventeen words at
`0x151A561C..0x151A5660`. The linked matcher reports
`2632 / 5483 (48.00%)` overall and `2064 / 4794 (43.05%)` game, with one
address-drift blocker and 2,850 total differing C functions. Debugger remains
complete at `181 / 181`.

## Compiler shape

The function copies the word at `D_800A8D70` into a stack record and calls
`func_15169260(record, 1, arg0, arg1)`. Its previous scalar-array source was
behaviorally complete but folded the source load and scheduled the local
record pointer too late.

The same source pattern already proven by `func_1518F45C` matches directly:
use `OneWord1D0840` for the local and source aggregate, pass its address, and
declare the callee's first parameter as `void *`. IDO then emits retail's
argument-home store, byte narrowing, source HI/LO address pair, `at` copy,
call delay store, epilogue, and final padding word without guarded patches.

## Evidence

The final linked and pristine 68-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1D2A9C`
- retail `conker/conker.us.bin+0x1D2ACC`
- SHA-256 `4a45a442193db0684da0464798590aa269e40e6c6c2e7865c0716abec79c107a`

The focused generated-object build, full nonmatching link, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation declarations and
calls for this function, with no separately maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 17-word `func_151D343C`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It forwards a one-word stack record
loaded from `D_800AB168` to `func_15169260`; remove its stale nonmatching note
and test the same aggregate local and pointer-typed callee contract first.
