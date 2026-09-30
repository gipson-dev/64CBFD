# Game signed-position effect dispatcher byte match

Date: 2026-09-30

`func_15013D38` occupies 44 words and 176 bytes at
`0x15013D38..0x15013DE8`. It sets bit two of the source byte at offset `0x16`,
converts the signed halfwords at offsets zero, two, and four into a local
three-float position, and forwards that position to `func_151BE850`.

The recovered value selection reads the word at offset `0x18` and substitutes
one only when that word is zero. Expressing this as a ternary reproduces
retail's default-value register and explicit two-arm branch. The dispatch also
forwards the word at offset `0x10`, byte at offset `0x1F`, and the trailing
arguments `(1, 0xFF, 1)`. The previous C had those last three arguments in the
incorrect order `(0xFF, 1, 1)`; the retail stack stores prove the correction.

Thirty-nine words emit directly from semantic C. Five stale-checked,
non-relocating guards normalize one closed IDO schedule: retail forms the
local vector address before materializing the three overflow call constants
and the default value, while the compiler materializes the default first. The
frame, saved registers, signed conversions, local offsets, branch structure,
call relocation, arguments, return value, and epilogue are unchanged.

The focused object, complete shared-guard rebuild, replacement link, outer
`NON_MATCHING=1` ROM build, project tool checks, whitespace check, and fresh
authoritative matcher pass. The linked ELF and pristine decompressed retail
spans share SHA-256
`d8ddb22ea0408713dc0b53f28741dd3aefe9de2acb182b2f2f71ee34a63fa1ed`.
The matcher advances exactly one row to `3,070 / 5,461 (56.22%)` overall and
`2,491 / 4,788 (52.03%)` in Game, with zero address drift.

Keep the five documented ownership/compiler-boundary rows parked. Resume with
33-word Game `func_15024130`, the next ordinary matcher row.
