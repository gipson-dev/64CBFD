# Game motion-table updater match

Date: 2026-11-14. `func_150C8350` now matches all 105 retail words at
`0x150C8350..0x150C84F4` (ROM `0xF5800..0xF59A4`). Its recovered `void`
implementation replaces a zero-return placeholder in
`conker/src/game/generated_F5800.c`.

The updater processes ten 10-byte records. It adjusts the current value at
offset 6 toward the signed target at offset 8, integrates position at offset 4
using the direction byte at offset 2, and reflects or clamps the position at
zero and `0x500`. `func_150C84F4` calls the updater for the primary frame
layer; it is reached through callback-table slot 9. Repeated table-pointer
loads preserve the retail access order when the table aliases global storage.

The production compiler emits 103 of the 105 words directly in their retail
positions. Two expected-word guards restore the operand order of a commutative
multiply and addition; they do not insert or delete instructions. Both object
padding paths and 12 GNU links over four symbol layouts produce the retail
stream. Eighteen neighboring functions and normalized constant pools remain
unchanged.

Retail, raw C and guarded instruction streams passed 320 modeled cases covering
signed boundaries and wrapped tick values, and 144 cases overlapping timing
globals. They also agreed in 64 cases overlapping the table-pointer storage,
including 40 mapped-memory faults; those checks compared machine state, memory,
and access order. The connected retail wrapper passed 64 cases, and 695 modeled
fault prefixes agreed. Four altered-instruction controls were rejected. Native
32-bit tests passed 320 cases in each of six O0/O2/O3 and aliasing combinations
with trapping UBSan; three source mutations were rejected. These bounded checks
do not establish gameplay, renderer or hardware behavior.

The actual production Make rebuild matches the independently predicted ELF.
The strict whole-image audit accounts for all 308 changed bytes with zero
exclusions. All 6,051 function addresses and 189,088 protected Game-data bytes
remain fixed. Only `generated_F5800.c.o` changed among the 698 frozen linked
objects; two guard rows were appended, existing rows and the conversion CSV
remain unchanged. A scoped, fail-closed Graphify refresh retained all 60,109
previous nodes; it was not a full-corpus re-extraction.

Tools commit `9e69166` retains the pre-install qualification and installed
regression checks. The pre-install screen is bound to the original fingerprinted
inputs and does not represent a fresh test of the installed checkout. Run the
installed checks with:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_motion_table_150c8350_installed -v
```

Both installed tests passed in the mounted tools checkout and an isolated
sibling overlay, with no skips. `make tools-check` passed. The sibling tools
checkout's existing changes were preserved.

Fresh production recount: Game **3,788 / 4,843 (78.22%)**, total
**4,461 / 5,516 (80.87%)**, zero drift. **87** more Game matches are needed
for 80% at the current denominator.
