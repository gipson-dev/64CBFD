# Game float scale-and-offset match - 2026-09-26

## Result

`func_151BD750` is byte-exact across all nineteen words at
`0x151BD750..0x151BD79C`. The linked matcher reports
`2636 / 5483 (48.08%)` overall and `2068 / 4794 (43.14%)` game, with one
address-drift blocker and 2,846 total differing C functions. Debugger remains
complete at `181 / 181`.

## Compiler shape

The maintained source already expresses the correct operation: convert the
signed halfword at object offset `0x80`, multiply it by `2.0f` and
`D_800AA860`, add `D_800AA864`, and advance the halfword by `D_800BE9E4`.
IDO strength-reduces the literal multiply to `add.s`, schedules the halfword
update earlier, and allocates a different set of FP temporaries.

An explicit bit-preserving union probe produced retail's FP dependency chain
but required a stack frame and overflowed the 76-byte slot by eight bytes, so
it was rejected. The compact semantic source was retained. Fifteen guarded
rows plus two insertions restore retail's immediate `2.0f`, ordered global
loads, `f6/f8/f10/f16/f18/f4` lifetimes, halfword-update position, result copy,
and return sequence. Six moved address words declare both expected and
replacement relocations.

The patch table now has 903 unique rows. Exactly fifteen belong to this
function, two carry insertions, and there are no duplicate
`(filename, function, offset)` keys.

## Evidence

The final linked and pristine 76-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x1EABD0`
- retail `conker/conker.us.bin+0x1EAC00`
- SHA-256 `614a29e037a05c46e1fe34e72c91217d5e5e776b72e027dab31c086cbfa4800f`

The focused object build, exhaustive nonmatching rebuild, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only a generated recompilation translation
and declaration, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 21-word `func_151417C4`, now the smallest ordinary-C game row
among the fourteen-difference candidates. Retail copies both words at
`D_8008A074` through a retained source pointer into an eight-byte stack record
at `sp + 0x1C`, narrows the low byte of `arg0` into the adjacent byte at
`sp + 0x24`, and calls `func_15169260(record, 2, &byte, arg1)`. The current
scalar-array source instead places the record at `sp + 0x20`, the byte at
`sp + 0x1F`, and emits independent source loads. Probe a typed two-word
aggregate assignment before adding guarded normalization.
