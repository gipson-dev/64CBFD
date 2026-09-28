# Game packed-counter state match - 2026-09-28

## Result

`func_15168B44` is byte-exact across its complete 26-word, 104-byte retail span
at `0x15168B44..0x15168BAC`.

The fresh linked matcher reports 2,886 / 5,466 (52.80%) exact C functions
overall and 2,312 / 4,790 (48.27%) in Game, with one address-drift blocker and
2,579 genuinely different C rows overall.

## Recovery

The function treats the word at state offset `0x14` as two packed 16-bit
counters. When the low counter is nonzero, it decrements that counter and
refreshes the signed timer at offset `0x38` to `0x1E`. Retail deliberately
writes the packed state twice: first the preserved upper half with a cleared
low half, then the merged decremented value in the return delay slot. The
state is therefore modeled as volatile so the intermediate write remains an
observable part of the recovered behavior.

When the low counter is zero, the upper counter is compared with the available
byte at offset `0x3F`. If the counter fits, the function subtracts it from the
available byte and refreshes the timer; otherwise it clears the timer.

The typed `PackedCountState` reproduces all field offsets, branches, stores,
and delay slots. IDO emits the exact routine length and instruction shape from
the semantic C. Twenty expected-word guards preserve one closed register-
allocation and independent-instruction scheduling cycle. The function has no
relocations, and the guards do not alter its control flow or data accesses.

## Evidence

The linked span at `conker/build/conker.us.elf` file offset `0x1A8B44` and the
pristine retail span at `conker/conker.us.bin` offset `0x195FF4` compare equal
across all 104 bytes. Both have SHA-256:

`91d2487272a1dd78117e7208d614ec5effbacba6016686c0fbcfd79603aed69a`

The fresh linked matcher no longer lists `func_15168B44`. The guard table has
exactly 20 rows for this function and no duplicate filename/function/offset
keys across the complete table.

## Validation

The focused object build and full non-matching replacement build pass. The
linked matcher, direct byte comparison, guard-table audit, outer ROM build,
project tool checks, focused Python tests, and whitespace validation are the
completion gate. Fresh gameplay was not run.

## Sibling boundary

The sibling `64CBFDOGL` retains its pre-existing dirty state. Its frozen
Release checkpoint was not built, modified, or launched.

## Next boundary

Continue with ordinary unparked 26-word Game `func_15169900`, currently at 25
real differences. Keep the documented smaller special and near-match rows,
Init SDK cache routines, address-drift-blocked `func_10012588`, and larger
parked HUD renderers in their existing lanes.
