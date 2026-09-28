# Game display-list matrix-pair match - 2026-09-28

## Result

`func_15157F80` is byte-exact across its complete 26-word, 104-byte retail span
at `0x15157F80..0x15157FE8`.

The fresh linked matcher reports 2,885 / 5,466 (52.78%) exact C functions
overall and 2,311 / 4,790 (48.25%) in Game, with one address-drift blocker and
2,580 genuinely different C rows overall.

## Recovery

The function appends two matrix commands to a caller-owned display list. The
first references the fixed matrix at `D_80089470`; the second references the
matrix at `D_800DCC10 + index * 0x40`. It advances the `Gfx` cursor after each
command, writes `1` to the fifth argument's output byte, and returns the
advanced cursor.

Using the SDK `gSPMatrix` macro preserves the two append operations and IDO's
retail cursor lifetimes. Under `F3DEX_GBI_2`, that macro XORs its parameter with
`G_MTX_PUSH`, so source flags `2` and `6` intentionally emit retail command
words `0xDA380003` and `0xDA380007`. Both matrix-address relocation pairs are
preserved. No expected-word guards or compiler-profile override are required.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x197F80` and the
pristine retail span at `conker/conker.us.bin` offset `0x185430` compare equal
across all 104 bytes. Both have SHA-256:

`27f9bccbe8de968c10894a8ba9a1faf522220334fcab24e553d392dfce0692e4`

The fresh linked matcher no longer lists `func_15157F80`.

## Validation

The focused object build, full non-matching replacement build, linked matcher,
direct byte comparison, outer ROM build, project tool checks, focused Python
tests, and whitespace validation pass. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_15168B44`, currently at 25
real differences. Keep the documented smaller special and near-match rows,
Init SDK cache routines, address-drift-blocked `func_10012588`, and larger
parked HUD renderers in their existing lanes.
