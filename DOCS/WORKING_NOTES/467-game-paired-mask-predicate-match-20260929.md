# Game paired-mask predicate byte match

Date: 2026-09-29

## Scope and behavior

`func_1503EF4C` in `conker/src/game/generated_6B320.c` spans 30 words and
120 bytes. It selects a two-word mask record from `D_8008446C`. Each nonzero
word must overlap the corresponding per-player mask at `D_800C6664` or
`D_800C6668`; zero words are accepted. The routine returns one only when both
tests pass.

Explicit base, byte-offset, entry, and first-word lifetimes reproduce retail's
complete register sequence and nested branch-likely control flow. Twenty-eight
words emit directly from C. Two fail-closed guards preserve only the
commutative operand order of the mask `and` instructions.

## Verification

- The focused padded object reproduces all 30 retail instructions.
- The shared guard table passed a complete single-job rebuild and relink.
- Direct comparison passes all 120 linked bytes. Both spans share SHA-256
  `a0fd6178724b9b83a3389a5846d315a002e7711dc8b2dbb3b83129cce9650649`.
- Fresh totals are `2,969 / 5,465 (54.33%)` overall and
  `2,395 / 4,789 (50.01%)` in Game, with one address-drift row.

## Resume boundary

Continue with the next ordinary 29-difference Game placeholder. Keep
`func_150AFBF4` parked at its documented compiler pointer-lifetime boundary.
