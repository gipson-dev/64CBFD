# Game conditional minimum update match - 2026-09-26

## Result

All 16 words of `func_151ACA20` now match retail across
`0x151ACA20..0x151ACA60`. The linked matcher reports `2598 / 5484 (47.37%)`
overall and `2030 / 4795 (42.34%)` game, with one address-drift blocker and
2,885 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function starts with a signed halfword, substitutes `0xFF` unless that
value is below `0x10`, otherwise scales it left by four and sign-extends it,
then lowers the byte at offset `0x5C` when the candidate is smaller. It always
returns one.

Declaring the candidate before the source gives IDO retail's `v0` candidate
and `v1` source lifetimes. Collapsing the intermediate candidate copy into
`temp_v0 = (s16) (temp_v1 << 4)` retains the exact `move`/`sll`/`sra`
sequence while allowing the constant return to occupy retail's second
branch-likely delay slot. Both byte loads, the conditional store, final return,
and all branch targets now match directly from C.

The complete non-matching link, outer build, and project tool checks passed.
The linked span at `conker/build/conker.us.bin+0x1D9EA0` and pristine retail
span at `conker/conker.us.bin+0x1D9ED0` both have SHA-256
`2650fd7f0a4ea8c62ed6c2de28b52fbf4bac60fc9924be173f872ad030eb954a`.
The patch table remains at 711 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling carries this function through generated recompilation
metadata/output and has no hand-maintained host body requiring a transplant.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains its
2026-09-23 timestamp.

## Next boundary

Continue with 19-word `func_1501CFF8`, the first game row with twelve real
differences. Retail keeps the byte count in `a1`, the index in `v0`, and tests
the do-while back edge with `slt`/`bnez`; current C keeps the count in `v0`,
the index in `a1`, and emits a direct `bne`. Compare local declaration order,
counter type, and a loop shape that prevents IDO from reducing the signed
less-than test before considering guarded scheduling words.
