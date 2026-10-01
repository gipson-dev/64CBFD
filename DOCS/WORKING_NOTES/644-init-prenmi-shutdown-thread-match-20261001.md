# Init PRENMI shutdown thread match

Date: 2026-10-01

`func_100052A0` occupies 180 words and 720 bytes at
`0x100052A0..0x10005570`. Its recovered body had been disabled because the
SDK `osMotorStop` macro did not reproduce the retail standalone call, leaving
an empty C placeholder in the active build.

The restored routine waits on `D_8003B9D0` when initialization has not yet
completed, sets the shutdown state, stops the two worker threads, and calls
`func_100093CC`. It records `osGetTime`, reinitializes VI, marks the VI state,
and lowers its own thread priority to 11.

When controller support is active, the thread optionally consumes the pending
SI message and scans all four controller slots. Active motors are initialized
with `_MakeMotorData`, stopped through the standalone `osMotorStop` symbol,
and have their active flags cleared. The thread then busy-waits until the
saved time reaches the retail `2,272,727`- and `7,500,000`-tick thresholds,
writes back the data cache, and parks forever. The retail unreachable
epilogue remains part of the matched slot.

Keeping the timer as a function-local static reproduces IDO's compact
`0x2C8`-byte function body and seven saved-register lifetimes while preserving
the preceding byte-exact `func_100050A0` extent. Nineteen relocation-aware
rows bind the local `.bss` references to the canonical `D_8003BC20` and
`D_8003BC24` retail symbols. The other 161 words, including the complete
instruction schedule, emit directly from semantic C. A preliminary inserted
NOP was removed after linked comparison showed that it shifted the
unreachable epilogue by one word; no inserted instruction is required.

The repository-wide stale-check build and final link pass. The authoritative
matcher lists neither `func_100050A0` nor `func_100052A0` as different. The
linked and retail 720-byte spans share SHA-256
`19f1d82d263567b460cce60c28d40fe7c017c72193c23311adbb2664ebb37ba4`.
Project tool checks pass, all 10 focused tool tests pass, and `git diff
--check` is clean.

The checkpoint is `3,143 / 5,457 (57.60%)` overall and
`460 / 488 (94.26%)` in Init, with zero address drift and 28 genuinely
different Init C rows. The next unparked Init candidate is `func_10011BB8`,
also 180 words, with 164 real linked-word differences.
