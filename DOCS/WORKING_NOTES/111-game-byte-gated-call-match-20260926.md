# Game byte-gated call match - 2026-09-26

## Result

`func_151A9024` is byte-exact across all fifteen words at
`0x151A9024..0x151A9060`. The linked matcher reports
`2623 / 5483 (47.84%)` overall and `2055 / 4794 (42.87%)` game, with one
address-drift blocker and 2,859 total differing C functions. Debugger remains
complete at `181 / 181`.

## Evidence

The function conditionally calls `func_151A931C` when the byte at object
offset `0x4C` equals one. Its third argument is an unsigned byte passed in
`a2`.

The generated C already expressed the correct behavior. IDO emitted the
correct 24-byte frame, argument-home store, byte narrowing, `bnel` early
epilogue, helper call, and return, but rotated thirteen words: it saved `ra`
before the argument home, retained the narrowed byte in `a3` until the call
delay slot, and placed the helper call four bytes earlier. An explicit cast,
an explicit byte temporary, a full-width formal argument, and an empty-block
scheduling probe did not reproduce the complete retail contract and were
rejected.

The accepted implementation keeps the clear original C and uses thirteen
expected-word guards from offset `0x004` through `0x034`. One guarded
relocation move shifts the `func_151A931C` call from `0x020` to `0x024`.
Retail stores the third argument in its home area, narrows it through `t6`,
copies it back to `a2`, saves `ra`, then loads the gate through `t7`. The final
padded `nop` already serves as retail's return delay slot.

The exhaustive non-matching rebuild, link, fresh matcher, outer build, and
project tool checks passed. Linked `conker/build/conker.us.bin+0x1D64A4` and
pristine retail `conker/conker.us.bin+0x1D64D4` are byte-identical for 60 bytes
and share SHA-256
`7dc4eef7baf0bc0fd3f7384828426f0f8cb11046bf1995f5dd14d527dc2fdf9c`.
The patch table contains 844 rows, zero duplicate keys, and thirteen rows for
this function.

The `64CBFDOGL` sibling contains recompilation metadata and a stub declaration
for this address, but no maintained host implementation to update. Its 1,659
existing dirty entries were left untouched. Frozen Release was not built,
modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 15-word `func_151C9B64`, now the first game row with thirteen
real differences. Retail clears bit 1 at object offset `0x58` and writes zero
to `*arg1` when the nested byte at `0x188 -> 0x6F` is nonzero; otherwise it
writes one. The generated C currently tests the opposite condition, so correct
that semantic inversion before investigating the remaining schedule.
