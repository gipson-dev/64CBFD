# Game randomized emitter guarded match

Date: 2026-11-14. `func_151A91AC` replaces the zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Its 92-word retail slot is
`0x151A91AC..0x151A931C` (ROM `0x1D665C..0x1D67CC`). The C body has the
same 0x90-byte frame and emits 88 retail words directly. Four expected-word
guards map two compiler-allocated temporary stack slots and their reloads to
the original offsets. Both padded outputs match all words and relocations.

The routine snapshots a three-entry signed-halfword choice table, draws one
random float and four integers, fills an emitter descriptor, and calls
`func_1513C650` with the owner's position, attachment and two owner bytes.
The last random call is sequenced before position and owner-byte reads: a
directly matching expression allowed native C to read the owner too early
when a modeled random helper mutated it. The real random helpers update the
64-bit seed at `D_800885B0`.

The emitter initializes 28 bytes of its 40-byte descriptor. Retail leaves the
last 12 as stack contents, and downstream `func_1513C350` copies all 40.
Guest checks seed and compare all 40 bytes; the native test does not inspect
the 12 indeterminate bytes. This distinction does not prove their later use
or the behavior of the complete effect.

The first entry of `D_8008F970` points to this callback. A retail window in
`func_151A8CEC` dispatches through that table, passing the actor and a
position array in its caller's stack frame. Sixteen cases execute that window
into each emitter stream. Guest tests cover 640 bounded input cases per
stream, five owner/position overlap cases, 64 guest-only position/descriptor
stack overlaps and 204 access prefixes. Retail and padded machine states
agree; raw C is checked against the same behavioral model, with its private
temporary slots at different offsets. The random and emitter helpers are
modeled. These tests do not establish full caller or helper execution,
unrestricted aliases, portable C behavior for guest stack overlaps, hardware
or gameplay.

Native 32-bit C passed 160 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. Seven altered
source controls were detected. Both padding implementations passed 12 GNU
links across four independently rebased symbol layouts. The other 22 owner
functions and normalized constant pools were preserved.

Production Make produced the independently predicted shadow ELF. The strict
whole-image audit accounts for 281 changed bytes with zero exclusions. All
6,051 function addresses and 189,088 protected Game-data bytes remain
fixed. Only the target owner changed among 698 frozen linked objects; the
four guard rows were appended without changing prior rows. The build emitted
pre-existing warnings in other files. A scoped fail-closed Graphify refresh
retained all 60,130 prior node IDs; this was not a full-corpus re-extraction.

Tools commit `2df8ce3` retains the installed regression suite. It passed in
the mounted tools checkout and an isolated
sibling tools overlay, with the sibling checkout's existing changes
preserved. `make tools-check` also passed:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_random_emitter_151a91ac_installed -v
```

Fresh production recount: Game **3,795 / 4,843 (78.36%)**, total
**4,468 / 5,516 (81.00%)**, zero drift. At the current denominator, **221**
additional exact matches are needed to reach 85% total.
