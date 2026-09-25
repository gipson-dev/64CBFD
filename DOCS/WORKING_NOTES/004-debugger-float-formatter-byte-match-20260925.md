# Working Note 004: Debugger Float Formatter Byte Match

Date: 2026-09-25

## Result

`func_16000F8C` is byte-exact in the linked US ELF. The restored C retains the
retail 46-word body, 88-byte frame, local buffer and float spill positions,
branches, formatter call, and instruction schedule.

The linked checkpoint is:

| Section | Byte-exact | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 2,521 / 5,497 (45.86%) | 1 | 2,975 |
| Init | 387 / 508 (76.18%) | 1 | 120 |
| Game | 1,959 / 4,808 (40.74%) | 0 | 2,849 |
| Debugger | 175 / 181 (96.69%) | 0 | 6 |

## Allocation Boundary

IDO consistently assigns the raw float word to `v0`, the exponent mask to
`v1`, and the doubled-zero result to `t0`. Retail uses `v1` for the raw word
and reuses `v0` for the mask and doubled result. Declaration scope, signedness,
operand order, and equivalent arithmetic experiments retained the same five
differences or changed the required opcode.

`conker/retail_word_patches.us.csv` records the five replacements at offsets
`0x38`, `0x40`, `0x44`, `0x54`, and `0x58`. `pad_c_object.py` verifies every
compiled input word and fails on stale or unapplied entries. This is explicit
compiler register-allocation normalization; the raw compact object alone is
not byte-exact.

## Verification

The debugger object rebuilt, the US ELF relinked, and the linked retail scan
no longer lists `func_16000F8C`. Repository replacement, outer build, and tool
checks also passed with the guarded table active.

## Resume Boundary

Continue with debugger `func_160014F0`, currently 19 real differences in one
glyph-setup allocator rotation and the temporary mask registers propagated
through the four-pixel unrolled loop. Keep `func_15135480` as a separate game
follow-up candidate.
