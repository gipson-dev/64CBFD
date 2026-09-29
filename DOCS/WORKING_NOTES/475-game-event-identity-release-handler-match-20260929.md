# Game event identity-release handler byte match

Date: 2026-09-29

## Scope and behavior

`func_150F1684` in `conker/src/game/generated_11C2B0.c` spans 22 words and 88
bytes at `0x150F1684..0x150F16DC`. It handles command `0x43`, compares the
incoming five-byte identity against the embedded identity at owner offset
`0x18`, and calls `func_1516972C` when either the four-byte key or trailing
identity byte matches. Other commands and complete identity mismatches return
without releasing the owner.

The recovered C keeps a named pointer to the embedded identity and expresses
the word comparison before the byte fallback. IDO emits the retail frame,
low-byte argument home and reload, branch structure, branch-likely return,
dispatcher call, and epilogue directly.

Fifteen words emit directly from semantic C. Seven fail-closed expected-word
guards normalize one closed register-allocation cycle: IDO retains the
embedded pointer in `v0`, while retail uses `v1`, then assigns the two word
loads and two byte loads to the corresponding retail temporaries. No
relocation is moved or replaced.

## Verification

- The focused generated-slice object builds with all seven expected-word
  guards firing and matches the 22-word retail listing.
- The complete non-matching object rebuild and ELF relink pass.
- Direct comparison passes all 88 linked bytes. Both spans share SHA-256
  `c4af721c70a7170cd352101e862a3e86c2bdb4ff161979503d064105f56f0ff9`.
- The authoritative matcher reports `2,977 / 5,465 (54.47%)` overall and
  `2,403 / 4,789 (50.18%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary small Game candidate. Keep `func_151A8584`
and `func_151A85D4` parked at their early-spill boundary, and keep
`func_1506EF5C` parked at its broad register-allocation mismatch. No
experimental source remains in those functions.
