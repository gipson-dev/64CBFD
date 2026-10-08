# Game Zone Neighbor Selection Lifetime Screen

Date: 2026-10-06. Starting checkpoint: `c48d111a`.

Continue matching `func_1508B3F8` in
[generated_B3020.c](../../conker/src/game/generated_B3020.c), following
[Note 1022](1022-game-zone-neighbor-selection-recovery-20261006.md).
Retail occupies 369 words / 1476 bytes at 0x1508B3F8..0x1508B9BC,
ROM 0xB88A8..0xB8E6C.

**Intermediate source improvement, not a byte match.** Retaining a typed
pointer to the unchanged query makes the complete C body emit **369 words**,
with no slot-padding words and the retail **0x140 frame**. Aligned-slot
differences fall from **340 to 282**, a reduction of 58. The exact-match
function counts do not increase. No new guards, compiler override, assembly
edit, overflow, insertion/omission or query enlargement.

## Independent Compiler Screen

[Lifetime driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_zone_neighbor_selection_lifetimes.py)
preserves the original 29-form / 58-profile inventory in
[recovery driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_zone_neighbor_selection_candidates.py).
Its `CHECKPOINT` is the old 367-word production source, independent of the
new `SELECTED` pointer form. Three separate receipts cover **91 additional
controls**, all with empty compiler diagnostics:

- 52 lifetime controls: typed query/flag pointers, guarded actor-loop entry,
  cached coordinates, deferred zone initialization and selected byte-best forms.
- 16 cursor controls: independently bias ID and distance cursors, retain the
  query pointer, and compare word/byte best types.
- 23 register-keyword controls, including individual and combined scalar hints.

| Control | Words | Frame | Real Differences | Installed |
| --- | ---: | ---: | ---: | --- |
| Previous byte cursors | 367 | 0x140 | 340 | No, retained checkpoint |
| Retained query pointer / byte cursors | 369 | 0x140 | 282 | Yes |
| Deferred zone / byte cursors | 369 | 0x140 | 289 | No |
| Biased IDs only | 369 | 0x140 | 297 | No |
| Typed cursors / Z reuse | 370 | 0x140 | 257 | No, oversized |
| Retained query pointer / biased distances only | 370 | 0x140 | 237 | No, oversized |
| Previous row / byte best | 370 | 0x140 | 233 | No, oversized |
| Retained query and flag pointers | 369 | 0x148 | 284 | No, wrong frame |

Guarded actor-loop entry and cached coordinates compile identically to their
corresponding original-loop controls. Tested register hints do not change
either selected oversized reference. Deferred zone initialization derives its
cursor from the cached selections, not a refreshed state global, but does not
recover retail's opening lifetime. No shorter body is produced by truncation.

Raw differences include length differences and are sensitive to alignment.
The 233-difference form is still one word too large; its score is not a reason
to install it or claim an instruction-percentage improvement. Non-selected
controls are compiler experiments, not individually qualified production bodies.

## Remaining Match Boundary

The installed query is still at SP+0xE8 instead of retail SP+0xAC. Private
selections/zone/counter homes are +0xE0/+0xDC/+0xCC instead of
+0x124/+0x94/+0x13C. The minimum and node-global addresses remain hoisted in
saved registers; retail instead retains query/flags pointers and constant 255.
Actor-address scheduling, candidate-byte narrowing, temporary register
allocation and loop scheduling also remain different.

The query remains the recovered 88-byte aligned layout, with count +0x2C,
IDs +0x2E, distances +0x0C and flags +0x36. Do not invent padding to force
the retail home. Next investigate real source lifetimes/alias representation,
or obtain stronger evidence for the original query type before changing it.
The retained 370-word controls need a genuine one-word source reduction before
they can be considered for production, followed by full qualification.

`func_15085DF8` still has its typed zero-return placeholder and is unchanged
from the preceding commit. This turn does not recover or qualify that lookup's
body. Opaque helper fixtures and a connected real visitor do not establish
full lookup/caller/gameplay or PC-port acceptance.

## Qualification And Audit

[Parent qualification](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_zone_neighbor_selection_match.py)
now compares retail, installed C, the frozen indexed recovery and the previous
production checkpoint: **2990 four-way guest cases**, with complete non-stack
memory, ordered external writes and ordered calls. It retains helper mutations,
replacement globals, signed bounds, strict/NaN/infinity comparisons, ties,
all candidate counts, saved-register preservation and both stack phases.
Dedicated fixtures cover **369/369 retail parent** and **84/84 visitor** words.
Universal equality of optimized external read histories is not claimed.

The installed source also passes **1424 source-extracted 32-bit native
footprints**. Negative-start fixtures remain guest-address tests, not strict-C
array-portability claims. Repeat-query, missing-clear and inclusive-comparison
negative controls continue to fail as expected.

[Lifetime tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_zone_neighbor_selection_lifetimes.py)
bind all three inventories, fail-closed source transformations, the unchanged
query/helper contract, the old checkpoint, the installed score and the two
explicit oversized controls. **17 combined tests pass in 94.742 seconds**,
no skips. **13 visitor regression tests pass in 48.888 seconds**, no skips.
No shared oracle or ABI/header change; the wider historical corpus is not
rerun in this turn.

Fresh ELF/progress/match-progress targets and `make tools-check` succeed.
The existing duplicate generated_12D630 recipe warning remains unrelated.
The complete **6059-slot before/after audit** preserves every symbol, address
and slot length. **Only func_1508B3F8 changes**. The neighboring function and
all helper slots, including the root placeholder, are byte-for-byte unchanged.

Target SHA-256:
`6658edd944cbf35a6b965b6fd1ba283f26a13f8a6f56a5f0b98ce7c8cc43d31b`.
Before/after slots, protected-section audit and compiler receipts are generated
under ignored `conker/build/game-zone-neighbor-lifetimes/`.

Init **164048 bytes**, Init data **17376 bytes**, Debugger **19800 bytes** and
Game data **189088 bytes / 720 owners** remain retail-exact. All **10643 CSV
guard rows** are unchanged. No data ownership or padding/emitter rule is relaxed.

Exact totals remain **3308/5462 (60.56%)**, Game **2635/4789 (55.02%)**, Init
**492/492**, Debugger **181/181**, zero address drift and **2154 different Game C**.
README aggregate tables/date remain accurate and unchanged. Detailed updates
remain in the documentation, not the root overview.

Whitespace checks and **3026 relative links** across nine current/working
documents pass; zero broken links.

## Reproduction

```powershell
wsl python3 -m tools.experiments.game_zone_neighbor_selection_lifetimes
wsl python3 -m tools.experiments.game_zone_neighbor_selection_lifetimes --cursors
wsl python3 -m tools.experiments.game_zone_neighbor_selection_lifetimes --registers
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_zone_neighbor_selection_match tools.tests.test_game_zone_neighbor_selection_lifetimes -q -f
wsl python3 -m unittest tools.tests.test_game_record_neighbor_visit_match -q -f
wsl make tools-check
git diff --check
```

Run linked-image qualification after the build finishes. No sibling source,
build, save, frozen Release, host transplant or push. The full Game matching
goal remains active; this checkpoint does not finish it.
