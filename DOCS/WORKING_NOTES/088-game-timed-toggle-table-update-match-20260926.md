# Game timed toggle/table update match - 2026-09-26

## Result

All 21 words of `func_150337E4` now match retail across
`0x150337E4..0x15033838`. The linked matcher reports `2601 / 5484 (47.43%)`
overall and `2033 / 4795 (42.40%)` game, with one address-drift blocker and
2,882 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function advances the signed counter at offset `0x38` by `D_800BE9E4`,
wraps it at sixteen while toggling the state at offset `0x3C`, then selects a
halfword from `D_800902FC` using that state. The former accumulated-value and
index locals gave IDO `v0`/`v1`-centered lifetimes even though the control flow
and instruction positions already agreed.

Updating and testing offset `0x38` directly, then indexing the table directly
from offset `0x3C`, recovers retail without guards. IDO now keeps the
accumulated value in `t8`, toggles through `t0`/`t1`, and performs the final
table lookup through `t2`/`t3`/`t4`. Both global HI16/LO16 relocation pairs,
the branch delay store, return, and complete extent match.

The complete non-matching link, linked matcher, outer build, and project tool
checks passed. Linked `conker/build/conker.us.bin+0x60C64` and pristine retail
`conker/conker.us.bin+0x60C94` share SHA-256
`54b59cd622a7bc63daf39021633dca3bfe362e4cf2812761b2aa81f4273bac76`.
The patch table remains at 723 rows with zero duplicate keys and no row for
this function.

The `64CBFDOGL` sibling has no hand-maintained source body for this function.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains its
2026-09-23 timestamp.

## Next boundary

Continue with 46-word `func_1504BA38`, now the first game row with twelve real
differences. Its arithmetic and control flow already agree. The differences
are localized to the three-byte record pipeline: retail uses `v1` for the
record pointer, `a1` for byte two, and `v0` for byte one, while current C uses
`v0` for the pointer and `v1` for both bytes. Existing source comments record
failed declaration-order, block-scope, early-return, and extra-parameter
allocation probes; verify those measurements before adding guarded words.
