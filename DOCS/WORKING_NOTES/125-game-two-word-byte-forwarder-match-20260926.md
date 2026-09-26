# Game two-word and byte forwarder match - 2026-09-26

## Result

`func_151417C4` is byte-exact across all twenty-one words at
`0x151417C4..0x15141818`. The linked matcher reports
`2637 / 5483 (48.09%)` overall and `2069 / 4794 (43.16%)` game, with one
address-drift blocker and 2,845 total differing C functions. Debugger remains
complete at `181 / 181`.

## Type and layout recovery

The function copies the two words at `D_8008A074` into a stack record, narrows
its first argument to one byte in an adjacent local, and calls
`func_15169260(record, 2, &byte, arg1)`.

Replacing the scalar array with a `TwoWord16DC80` aggregate recovers retail's
retained source pointer and copy through `at` and `t9`. Declaring the one-byte
array before the aggregate gives IDO retail's record at `sp + 0x1C` and byte at
`sp + 0x24`. Correcting the first argument from `s32` to `u8` restores the
`lbu` from the low byte of its big-endian home slot at `sp + 0x2B`. Together
these source changes reproduce all instructions and relocations directly; no
guarded rows are required, and the patch table remains at 903 unique rows.

## Evidence

The final linked and pristine 84-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x16EC44`
- retail `conker/conker.us.bin+0x16EC74`
- SHA-256 `ef850b0471b25abd9bcafff4af8626a3d7fd00d66013e1888ded1ea4574e9d37`

The focused object build, nonmatching relink, fresh direct matcher, outer
build, and project tool checks passed.

The `64CBFDOGL` sibling contains only a generated recompilation translation
and declaration, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 25-word `func_15144BC8`, now the smallest ordinary-C game row
among the fourteen-difference candidates. Retail copies incoming `f12` to a
local value in `f2`, then loads zero into `f12` and performs both 360-degree
normalization loops on `f2`. The current source mutates `arg0` directly, which
keeps the value in `f12` and places zero in `f2`. Mirror neighboring
`func_15144B68` with `f32 ret = arg0`, loop on `ret`, and return `ret` before
considering guarded normalization.
