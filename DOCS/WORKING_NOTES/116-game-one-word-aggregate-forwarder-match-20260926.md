# Game one-word aggregate forwarder match - 2026-09-26

## Result

`func_1518F45C` is byte-exact across all sixteen words at
`0x1518F45C..0x1518F49C`. The linked matcher reports
`2628 / 5483 (47.93%)` overall and `2060 / 4794 (42.97%)` game, with one
address-drift blocker and 2,854 total differing C functions. Debugger remains
complete at `181 / 181`.

## Compiler shape

The function copies the word at `D_800A74D4` into a stack record and calls
`func_15169260(record, 1, arg0, arg1)`. The previous scalar-array source was
behaviorally complete, but IDO folded the source address into a relocated
`lw`, formed the stack-record pointer late, and scheduled the saved arguments
before retail's `a2` and `a0` setup.

Using the existing `OneWord1BA1D0` aggregate for the local and source copy,
and declaring the callee's first parameter as `void *`, gives IDO the exact
retail shape. It forms the local address directly in `a0`, preserves `arg0` in
`a2`, stores the byte argument in its home slot, narrows it into `a3`, retains
the global source base in `t6`, and copies the word through `at` into the call
delay slot. No guarded word rows are required.

## Evidence

The final linked and pristine 64-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1BC8DC`
- retail `conker/conker.us.bin+0x1BC90C`
- SHA-256 `a12d1a70f23ef188ceab15dfff522bff9dc5c41350fa247959c712cad4992c5c`

The focused generated-object build, full nonmatching link, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation declarations and
calls for this function, with no separately maintained host implementation to
update. Its 1,659 existing dirty entries were left untouched. Frozen Release
was not built, modified, or launched; `build/Release/conker_pc.exe` retains
timestamp `2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 16-word `func_151A5130`, now the smallest ordinary-C game row
among the fourteen-difference candidates. It narrows its third argument to a
signed halfword, indexes callback table `D_8008F900` through byte offset
`arg1 + 0x14`, and invokes the selected callback. The current old-style C body
omits those explicit argument uses from the call expression, so its generated
frame and indirect-call schedule need to be measured against retail.
