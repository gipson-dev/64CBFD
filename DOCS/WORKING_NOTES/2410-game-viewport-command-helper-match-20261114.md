# Game viewport command helper match

Date: 2026-11-14. `func_1510B7B4` now matches all 105 retail words in
`conker/src/game/generated_138520.c`, at `0x1510B7B4..0x1510B958` (ROM
`0x138C64..0x138E08`). This promotes the semantic SDK display-list helper
from [Note 982](982-game-viewport-command-helper-semantic-recovery-20261005.md)
to a byte match. It writes twelve command packets, reads the view normalization,
base, page and matrix table in retail order, and returns the advanced cursor.

The source expresses the first view lookup as an indexed 0x180-byte row and
computes the second view offset using explicit unsigned low-word arithmetic.
The production O2/g3 compiler emits 105 words, 81 already at retail positions.
Twenty-four expected-word guards restore one closed register-allocation and
instruction-scheduling region; no instruction insertions or deletions are
used. Both independent padding paths and 12 GNU links over four symbol layouts
produce the same 105-word retail stream. The 13 other functions in the owner and
its normalized constant pools remain unchanged.

The candidate, guarded stream and retail stream agree in 96 modeled cases,
including boundary normalization values, wrapping-index model cases and output
aliases; ordered reads, stores and returned cursors are checked. Three invalid
slot/page prefixes and 310 modeled access-fault prefixes agree, and three
altered-instruction controls are rejected. The candidate also passes 65,600
native32 cases at O2 with strict aliasing disabled, including an actual
helper-to-color cursor connection. These are bounded guest and native checks;
they do not establish complete renderer execution, submitted graphics, or
hardware pixels.

The actual production Make rebuild matches the independently predicted ELF.
A strict whole-image comparison explains all 358 changed bytes with no
exclusions; all 6,051 function addresses and 189,088 protected Game-data
bytes remain fixed. Of 698 previously frozen linked objects, only
`generated_138520.c.o` changed. All earlier guard rows and the conversion CSV remain unchanged; 24 guard rows
were appended. A scoped Graphify
refresh retained all 60,107 prior node IDs; it was fail-closed and was not a
full-corpus re-extraction.

Tools commit `9c96e54` retains the fingerprinted pre-install screen and
updates the installed regression checks. The pre-install screen is bound to
its recorded original ELF, owner and guard inputs; its receipt is not a test
of the already installed checkout. For the installed checkout, run:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_viewport_command_helper tools.tests.test_game_viewport_renderer -q
```

All 26 installed helper/renderer tests passed in both the mounted tools
checkout and an isolated sibling overlay, with no skips; `make tools-check`
passed. Two old renderer test expectations were refreshed against the frozen
pre-change ELF and current caller source. The sibling tools checkout's prior
dirty paths were preserved.

Fresh production recount: Game **3,787 / 4,843 (78.20%)**, total
**4,460 / 5,516 (80.86%)**, zero drift. **88** more Game matches are needed
for 80% at the current denominator.
