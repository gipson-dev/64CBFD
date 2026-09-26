# Game random indexed-effect setup match - 2026-09-26

## Result

`func_150718E4` is byte-exact across all forty-five words at
`0x150718E4..0x15071998`. The linked matcher reports
`2639 / 5483 (48.13%)` overall and `2071 / 4794 (43.20%)` game, with one
address-drift blocker and 2,843 total differing C functions. Debugger remains
complete at `181 / 181`.

## Local layout and register schedule

The function conditionally chooses one byte from `D_80099BB8`, builds a
`struct17` effect record using the current actor's child pointer, raises its
height by `20.0f`, and submits it through `func_151C329C`.

Reversing the `struct17` and source-word declarations gives IDO retail's
48-byte frame layout: the source word at `sp + 0x20`, the record at
`sp + 0x24`, and its adjusted float at `sp + 0x28`. The remaining compact body
uses a different but equivalent register allocation after `func_150ADA20`.
Ten guarded rows restore retail's selected-byte and actor-pointer lifetimes in
`t0..t5`. Four relocation-bearing words declare both expected and replacement
`D_800D154C` relocations. No insertions or control-flow changes are required.

The patch table now has 913 unique rows. Exactly ten belong to this function,
none carry insertions, and there are no duplicate
`(filename, function, offset)` keys.

## Evidence

The final linked and pristine 180-byte spans are byte-identical:

- linked `conker/build/conker.us.bin+0x9ED64`
- retail `conker/conker.us.bin+0x9ED94`
- SHA-256 `f128977f492f1068d911ae7303cfcd80a685d2b28a8d282f84da46832064af76`

The focused object build, exhaustive nonmatching rebuild, fresh direct
matcher, outer build, and project tool checks passed.

The `64CBFDOGL` sibling contains only generated recompilation translations and
declarations, with no separately maintained host implementation to update.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28` and size `13,712,896` bytes.

## Next boundary

Continue with 16-word `func_150142AC`, now the smallest ordinary-C game row
among the fifteen-difference candidates. Retail sets object flag `0x04`, loads
the byte at offset `0x1B` into `v1`, retains an explicit negative-index early
return, then checks `idx < 3` before storing the object into
`D_800D9AA0[idx]`. The current source uses `u8 idx` and only the upper-bound
condition, yielding a shorter single-exit shape. Recover the original signed
temporary and explicit lower/upper bound source before considering guards.
