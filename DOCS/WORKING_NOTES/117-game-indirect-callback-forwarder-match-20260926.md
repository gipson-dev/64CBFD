# Game indirect-callback forwarder match - 2026-09-26

## Result

`func_151A5130` is byte-exact across all sixteen words at
`0x151A5130..0x151A5170`. The linked matcher reports
`2629 / 5483 (47.95%)` overall and `2061 / 4794 (42.99%)` game, with one
address-drift blocker and 2,853 total differing C functions. Debugger remains
complete at `181 / 181`.

## Recovered call contract

The function uses byte `arg1[0x14]` to select a callback from `D_8008F900`.
Retail invokes that unprototyped callback with the original `arg0` and `arg1`
still live in their incoming registers and with `arg2` narrowed to the
declared signed-halfword type in `a2`.

The previous C expression called the callback with an empty argument list.
IDO consequently treated `arg2` as unused, omitted its narrowing, and emitted
an unnecessary home store for `arg0`. Passing `arg0`, `arg1`, and `arg2`
through the existing unprototyped callback makes the ABI contract explicit.
IDO then reproduces retail's `a2` home store, `sll`/`sra` narrowing through
`t6`, callback-table index in `t8`, `t9`, and `at`, indirect call, and
epilogue directly. No guarded word rows are required.

## Evidence

The final linked and pristine 64-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1D25B0`
- retail `conker/conker.us.bin+0x1D25E0`
- SHA-256 `2ad708b8b146d23e66d5aaaf986a104bede706f803d39c5d2febf7bfdc9f910f`

The focused generated-object build, full nonmatching link, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation declarations for
this function, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 17-word `func_1508F060`, now the smallest ordinary-C game row
among the fourteen-difference candidates. Its C body clears six bytes in the
`D_800D2460` state block and the separate `D_800D24C0` byte. Compare the
current compiler-selected global bases and store order with retail before
changing the still-unresolved array declaration noted in the source.
