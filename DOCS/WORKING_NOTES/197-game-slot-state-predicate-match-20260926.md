# Game slot-state predicate match - 2026-09-26

## Result

`func_151B22F4` is byte-exact across all 21 words and 84 bytes at
`0x151B22F4..0x151B2348`. Fresh totals are 2,700 / 5,469 exact C functions
overall and 2,129 / 4,791 in Game.

## Recovery

The function converts the pointer at object offset `0x28` into a one-based
index relative to `D_800CC2D0`, whose records have stride `0x32C`. It compares
that index against the owner byte at offset `0x65` of the record referenced by
object offset `0x30`, then requires that record's 32-bit state at offset
`0x5C` to equal one. It returns one when both checks pass and two otherwise.

Expressing the pointer distance as signed 32-bit arithmetic followed by
division by `0x32C` reproduces retail's `subu` and signed `div`. The direct
short-circuit predicate preserves the delayed owner-record load, default
return value, and `return 1` in the first `jr` delay slot. All 21 words compile
directly without guarded retail words or compiler-steering expressions.

## Evidence

Linked ELF offset `0x1F22F4` and decompressed retail offset `0x1DF7A4` compare
equal for 84 bytes, both with SHA-256
`0831d55fc5252d7dd1179e8eb002d59cc94a5f0e0a074103537cee91c689d0d9`.

| Section | Byte-exact C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,700 / 5,469 (49.37%) | 1 | 2,768 |
| Init | 390 / 497 (78.47%) | 1 | 106 |
| Game | 2,129 / 4,791 (44.44%) | 0 | 2,662 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

## Parked callback pair

`func_151A8584` and `func_151A85D4` are behaviorally recovered but remain
parked. Typed callback-local, direct-table, unprototyped callback, K&R formal,
`register`, assignment-in-condition, and minimal typed-record forms all emit
`0x54` bytes rather than retail's `0x50`. The extra sequence homes `arg0` at
entry and reloads it before table indexing; retail indexes directly through
`a0` and conditionally stores it only in the `jalr` delay slot. No speculative
body was retained.

## Sibling and validation

`64CBFDOGL/recomp_out/.c` still contains the old two-instruction zero-return
generated body for `func_151B22F4`; a future controlled regeneration must
consume this restored guest function. The sibling's 1,659 dirty entries and
frozen Release executable remain untouched.

The focused object, full replacement link, fresh progress and LIST matcher,
independent span comparison, tool checks, six unit tests, outer build, and
`git diff --check` pass.

## Next boundary

Continue ordinary Game matching with existing 23-word `func_151D73A8`, the
next unparked nonblocked Game row at 18 differences. Init alternative
`func_10001000` remains at 14 differences; keep address-blocked
`func_10012588` parked.
