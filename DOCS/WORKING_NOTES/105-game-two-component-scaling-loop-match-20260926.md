# Game two-component scaling loop match - 2026-09-26

## Result

The false C placeholder for `func_15131918` is replaced by a byte-exact
sixteen-word C implementation across `0x15131918..0x15131958`. The linked
matcher reports `2617 / 5483 (47.73%)` overall and
`2049 / 4794 (42.74%)` game, with one address-drift blocker and 2,865 total
differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine takes a float array and a scale, then loops `D_800BE9E4` times,
multiplying components zero and two by that scale. It is the two-component
sibling of the already exact `func_151318E8`, which scales component one.
The retained `asm/15D730.s` body established the loop structure, field
offsets, FP registers, and branch-delay store.

The first typed-prototype probe left the two callers' offset-`0xA8` fields as
`s32`; IDO inserted integer-to-float conversions and overflowed an earlier
caller slot. Keeping an unprototyped declaration with a typed float definition
is invalid under default argument promotion. A raw-`s32` parameter reinterpreted
through a union preserved callers but created an 8-byte frame, stack spill,
and two reloads, overflowing this function to eighteen words.

The accepted source types both call-site fields as `f32` and declares the
routine as `void func_15131918(f32 *, f32)`. IDO still transfers the mixed
pointer/float argument through `lw a1` at both callers, then emits retail's
opening `mtc1 a1,f12`. The direct loop emits the exact global count relocation,
initial `blez`, two loads and multiplies, decrement, two stores, branch-delay
store, and epilogue. No guarded rows are needed, and the caller extents remain
unchanged.

The exhaustive non-matching link, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x15ED98` and pristine
retail `conker/conker.us.bin+0x15EDC8` are byte-identical for 64 bytes and share
SHA-256
`3357c69ce2bd665e8ca4744d549d7068cc8edb12fb9c766e8a0443c38f6f1232`.
The patch table remains at 808 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling has only three symbol-map metadata hits for this
function and no maintained implementation to update. Its 1,659 existing dirty
entries were left untouched. Frozen Release was not built, modified, or
launched; `build/Release/conker_pc.exe` retains timestamp
`2026-09-23 05:04:28`.

## Next boundary

Continue with 15-word `func_1514143C`, now the first game row with thirteen
real differences. Inspect whether it is a true C near-match or another false
placeholder before attempting schedule guards.
