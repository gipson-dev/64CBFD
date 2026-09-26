# Game mirrored counter/table update match - 2026-09-26

## Result

All 20 words of `func_15031E2C` now match retail across
`0x15031E2C..0x15031E7C`. The linked matcher reports `2600 / 5484 (47.41%)`
overall and `2032 / 4795 (42.38%)` game, with one address-drift blocker and
2,883 total differing C functions. Debugger remains complete at `181 / 181`.

## Evidence

The function reflects counter values three through five into table indices two
through zero, loads a halfword value from `D_800902BC`, advances the persistent
counter, and wraps it to zero at six. Current C already emitted retail's
20-word control-flow graph, branches, delay slots, stores, and return.

Declaration-order, split-assignment, and K&R/ANSI definition probes all emitted
the same stable allocation. Twelve guarded words therefore normalize only the
independent register schedule: persistent counter `v1`, reflected index `v0`,
advanced counter `t9`, and table address/value `t8`. The table HI16 and LO16
guards explicitly preserve their `D_800902BC` relocations. No instruction is
inserted, removed, or moved.

The exhaustive non-matching rebuild, linked matcher, outer build, and project
tool checks passed. Linked `conker/build/conker.us.bin+0x5F2AC` and pristine
retail `conker/conker.us.bin+0x5F2DC` share SHA-256
`d1fcfc04e9e799d2864afd8d204547594fe1f79d94eba637d63fe84656099ddf`.
The patch table has 723 rows, zero duplicate keys, and twelve rows for this
function.

The `64CBFDOGL` sibling has no hand-maintained source body for this function.
Its 1,659 existing dirty entries were left untouched. Frozen Release was not
built, modified, or launched; `build/Release/conker_pc.exe` retains its
2026-09-23 timestamp.

## Next boundary

Continue with 21-word `func_150337E4`, now the first game row with twelve real
differences. Its control flow and instruction positions already agree. Compare
the accumulated counter (`v0` current versus retail `t8`), toggled-state
pipeline (`t8`/`t9` current versus retail `t0`/`t1`), and final table pipeline
(`v1`/`t1` current versus retail `t2`/`t4`) before deciding whether source
lifetime changes can recover the schedule or guarded words are required.
