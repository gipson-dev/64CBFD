# Game record ring-slot match - 2026-09-28

## Result

`func_1512D604` is byte-exact across its complete 26-word, 104-byte retail span
at `0x1512D604..0x1512D66C`.

The fresh linked matcher reports 2,883 / 5,466 (52.74%) exact C functions
overall and 2,309 / 4,790 (48.20%) in Game, with one address-drift blocker and
2,582 genuinely different C rows overall.

## Recovery

The function uses the byte at caller offset `0x23D` to select a `0xB0`-byte
record from the table addressed by `D_800DC2B0`. It reads the record cursor at
offset `0xA8`, returns the eight-byte slot selected by the old cursor, advances
the cursor, and resets it to zero when the incremented value reaches 20.

The recovered C preserves retail's repeated record lookup and the old-cursor
lifetime. IDO emits the complete control flow and memory behavior, but assigns
one closed set of integer temporaries to different registers. Twenty scoped
expected-word guards normalize that allocation cycle. The two address words
retain matching `R_MIPS_HI16` and `R_MIPS_LO16` relocations for
`D_800DC2B0`; no address or call target is hard-coded.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x16D604` and the
pristine retail span at `conker/conker.us.bin` offset `0x15AAB4` compare equal
across all 104 bytes. Both have SHA-256:

`b692143b5131d7eb23aa0e7f5a09d9b82b602c1715a48b1e69562da46b18a17c`

The matcher no longer lists `func_1512D604`. The guard audit finds exactly 20
rows for this function and no duplicate `(filename, function, offset)` keys in
the complete guard table.

## Validation

The full non-matching replacement build, linked matcher, direct byte
comparison, and guard-table audit pass. The outer ROM build, project tool
checks, focused Python tests, and whitespace validation are rerun before this
change is banked. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 29-word Game `func_1514F5CC`, currently at 25
real differences. Keep the documented special and near-match rows, Init SDK
cache routines, address-drift-blocked `func_10012588`, and larger parked HUD
renderers in their existing lanes.
