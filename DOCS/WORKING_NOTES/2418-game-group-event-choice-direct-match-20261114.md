# Game group-event selection direct match

Date: 2026-11-14. `func_15023264` now emits all 86 retail instructions
directly from C, with no word guards. Its slot is
`0x15023264..0x150233BC` (ROM `0x50714..0x5086C`) in
`conker/src/game/generated_49D30.c`.

The function scans a group's record pointers and calls `func_15023BB0`
for command 3 on each non-null record. An event with a score strictly less
than the current best supplies a signed halfword selection at event offset 2.
If the final selection is -1, it searches the group's eight-byte default
entries for the first halfword equal to 1, falling back to zero if none
qualifies. The scan reloads the group count after each iteration, so a
modeled parser can change the number of records visited; the default pass
uses the last loaded count. The second input is retained for the retail ABI.
The original caller at `0x15020F44..0x15020F60` saves the low byte of the
result to `D_800C35F8`.

The raw and both padded instruction streams match the original words and
relocations. Both padding paths passed 12 GNU links over four independent
symbol layouts. All 56 neighboring functions and normalized constant pools
remain unchanged; the owner's existing no-loop-unroll compiler profile is
retained. The equivalent `index <= liveCount - 1` expression in the
fallback loop preserves retail's signed comparison; that loop is entered
only when the byte-derived count is positive.

Retail, raw C and padded guest streams agreed with an independent model in
1,024 bounded cases per stream. These cover absent records/events, signed
scores and event values, score ties, fallback entries, two groups, stack
alignment, and parser-driven count growth and shrinkage. A further 128
cases execute the original seven-instruction caller window; 160 fired access
prefixes compare complete guest machine state. The corpus visited 85 of the
86 instruction words. The parser was modeled, not executed, and these tests
do not establish complete caller, parser, hardware or gameplay behavior.

Native 32-bit C passed 1,024 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Six altered
source controls were detected. These bounded fixtures cover valid group
indices and initialized, aligned records and do not claim unrestricted
portable C aliases or guest fault behavior.

The actual production Make rebuild equals the independently predicted shadow
ELF. The strict whole-image audit accounts for 268 changed bytes with zero
exclusions; all 6,051 function addresses and 189,088 protected Game-data
bytes remain fixed. Only the target owner changed among 698 frozen linked
objects. Existing guard and conversion manifests remain unchanged. A scoped
fail-closed Graphify refresh retained all 60,123 previous node IDs; it was
not a full-corpus re-extraction.

Tools commit `bd2c7be` retains the installed regression suite:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_group_event_choice_15023264_installed -v
```

The installed suite passed in both the mounted checkout and isolated sibling
tools overlay, and `make tools-check` passed. The sibling checkout's
pre-existing edits were preserved.

Fresh production recount: Game **3,793 / 4,843 (78.32%)**, total
**4,466 / 5,516 (80.96%)**, zero drift. **82** more Game matches are needed
for 80% at the current denominator. The private random-scatter candidate in
[Note 2417](2417-game-random-scatter-scheduling-screen-20261114.md) remains
uncredited.
