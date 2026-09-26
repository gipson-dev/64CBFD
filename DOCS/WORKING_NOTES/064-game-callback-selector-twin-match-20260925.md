# Game callback selector twin match - 2026-09-25

## Result

All 33 words of `func_151963B4` now match retail across
`0x151963B4..0x15196438`. The linked matcher reports `2577 / 5484 (46.99%)`
overall and `2009 / 4795 (41.90%)` game, with one address-drift blocker and
2,906 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

This function is the structural twin of `func_15196330`: it reads the same
record, dispatches the same two signed callback selectors, and differs only in
its final direct call to `func_15147928`. An independent retail diff confirmed
the same nine-word `v0`/`v1` rotation and no other difference.

Nine function-specific expected-word guards retain the record pointer in `v0`
and both selectors in `v1`. The frame, stack slots, branches, callback tables,
indirect calls, epilogue, and five relocations remain compiler-produced.

The generated object, full shared-CSV rebuild, linked matcher, and project tool
checks passed. The complete 132-byte ELF span at `0x1D63B4` and pristine retail
span at `conker/conker.us.bin+0x1C3864` both have SHA-256
`cf3ff8a08a41e22809847c2dccc1abd13cd671b7db20372f07d2575926cd3adf`.
The patch table has 625 rows, zero duplicate keys, and nine target rows.

The `64CBFDOGL` sibling has symbol metadata but no hand-maintained
implementation to transplant. Its dirty tree was left untouched, and frozen
Release was not built or launched.

## Next boundary

Continue with 18-word `func_151E5F64`, now the first game row with nine real
differences. Compare source, compact object, retail words, and relocations
before editing.
