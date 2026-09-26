# Game indexed byte selector match - 2026-09-25

## Result

All 18 words of `func_151E5F64` now match retail across
`0x151E5F64..0x151E5FAC`. The linked matcher reports `2578 / 5484 (47.01%)`
overall and `2010 / 4795 (41.92%)` game, with one address-drift blocker and
2,905 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function returns its input index when both global enable bytes are zero.
Otherwise it reads a signed byte from `D_800E0C00[index]`, clamps negative
values to zero, and returns the result. The prior equivalent C put the early
return first; IDO merged the return shape, emitted a likely `bgezl`, and
produced nine reported differences.

Expressing the enabled lookup as the positive `||` branch and leaving
`return arg0` last makes IDO preserve retail's two return sites. It also emits
the exact branch distances, the non-likely `bgez` with a `nop` delay slot, and
the final `move v0, v1` return-delay update. All four global relocations remain
compiler-produced. No guarded patch rows are used by this function.

The generated object and full linked build completed. The ordinary `make`
verification target still reports the repository-wide expected ROM SHA-1
mismatch; `make NON_MATCHING=1` confirms the current nonmatching build target
is otherwise up to date. The complete 72-byte ELF span at `0x225F64` and
pristine retail span at `conker/conker.us.bin+0x213414` both have SHA-256
`0beb65faa2a495c68f3866e3915fa51747ea7149656f30e71e53a1a6828cdace`.
The patch table remains at 625 rows, has zero duplicate keys, and has zero
rows for this function.

The `64CBFDOGL` sibling has generated recompilation metadata and an older
investigation note referring to this routine, but no maintained source body
to update. Its dirty tree was left untouched, and frozen Release was not built
or launched.

## Next boundary

Continue with 10-word `func_151E81EC`, now the last game row with nine real
differences. It was parked earlier, so re-establish its source, linked words,
relocations, and current compiler behavior before editing.
