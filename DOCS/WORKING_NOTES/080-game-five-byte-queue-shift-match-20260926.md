# Game five-byte queue shift match - 2026-09-26

## Result

All 15 words of `func_1507EEB8` now match retail across
`0x1507EEB8..0x1507EEF4`. The linked matcher reports `2593 / 5484 (47.28%)`
overall and `2025 / 4795 (42.23%)` game, with one address-drift blocker and
2,890 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The routine pushes one byte into a five-byte queue. The former five scalar
assignments produced repeated base-relative accesses and stored the new byte
before shifting the existing values.

Expressing the operation as a fixed reverse loop from index four through one
recreates retail's complete unrolled form: one `arg1 + 4` end pointer, loads
from indices two, one, zero, and three, four negative-offset stores, and the
new byte store last. The incoming `u8` normalization, registers, ordering,
return, and delay slot all match directly from C. No guarded row was added.

The complete non-matching link and project tool checks passed. The linked span
at `conker/build/conker.us.bin+0xAC338` and pristine retail span at
`conker/conker.us.bin+0xAC368` both have SHA-256
`bec0e721180c79c0dfb9915789558fbb481fe906c5fee1e835496f9727260b1f`.
The patch table remains at 700 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling exposes this function only through generated dispatch,
declaration, and symbol-table artifacts. It has no hand-maintained host body
requiring a transplant. Its existing dirty work was left untouched, and frozen
Release was not built, modified, or launched.

## Next boundary

Continue with 17-word `func_150B6D34`, now the first game row with eleven real
differences. Compare its source model, compact object, retail words, and
relocations before editing.
