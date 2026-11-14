# Game world-emitter descriptor direct match

Date: 2026-11-14. `func_150D7120` now emits all 91 retail instructions
directly from C, with no word guards. Its slot is
`0x150D7120..0x150D728C` (ROM `0x1045D0..0x10473C`) in
`conker/src/game/generated_1045D0.c`.

The function calls three precursor effects in order, copies the position
after those calls, and builds a 0x5C-byte emitter descriptor with fixed
halfword, integer and float fields plus three global float values. It then
passes that descriptor, the low byte of the slot and the context to
`func_1514FCE8`. The descriptor's final three bytes are retained stack
bytes; the routine does not initialize them. Guest tests seed and compare
those bytes, while native tests exclude them.

The raw and both padded streams match the original words and relocations.
Both padder paths passed 12 GNU links across four independent symbol layouts.
The other owner function and normalized constant pools remain unchanged;
compiler diagnostics are empty.

Retail, raw C and padded guest streams agreed with an independent model in
384 bounded cases per stream, including full-word slot inputs, contexts,
precursor changes to position and globals, and changes to incoming argument
homes. Another 64 cases execute windows of both original callers, 32
guest-only cases overlap the input position with the descriptor's stack
area, and 204 fired access prefixes compare complete guest machine state.
The four called helpers were modeled. These checks do not establish complete
helper or caller execution, portable C behavior for stack overlaps, hardware
or gameplay.

Native 32-bit C passed 96 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Seven altered
source controls were detected. Native fixtures use typed, aligned positions
and do not read the three indeterminate descriptor bytes.

The actual production Make rebuild equals the independently predicted shadow
ELF. The strict whole-image audit accounts for 307 changed bytes, including
one equal-address symbol metadata ordering group, with zero exclusions. All
6,051 function addresses and 189,088 protected Game-data bytes remain fixed.
Only the target owner changed among 698 frozen linked objects; the guard and
conversion manifests remain unchanged. A scoped fail-closed Graphify refresh
retained all 60,127 prior node IDs; this was not a full-corpus re-extraction.

Tools commit `6af9162` retains the installed regression suite:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_emitter_descriptor_150d7120_installed -v
```

The installed suite passed in the mounted checkout and an isolated sibling
tools overlay, and `make tools-check` passed. The sibling checkout's
pre-existing edits were preserved.

Fresh production recount: Game **3,794 / 4,843 (78.34%)**, total
**4,467 / 5,516 (80.98%)**, zero drift. **81** more Game matches are needed
for 80% at the current denominator. The renderer candidate in
[Note 2419](2419-game-render-queue-private-screen-20261114.md) remains
uncredited.
