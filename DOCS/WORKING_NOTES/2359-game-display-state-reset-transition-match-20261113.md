# Game display state reset and transition matches

Date: 2026-11-13. `func_15178EB0` and `func_15178EFC` in
`generated_1A6360.c` replace placeholders with recovered display-state
operations. The 19-word initializer occupies VA `0x15178EB0..0x15178EFC`
and ROM `0x1A6360..0x1A63AC`; it matches directly from C. The 67-word
transition occupies VA `0x15178EFC..0x15179008` and ROM
`0x1A63AC..0x1A64B8`. Six expected-word guards normalize a closed register
allocation cycle, and both supported padders reproduce its retail body.

The initializer resets the state, status, timers, and list pointer. State 2
of the transition disposes the non-null entries in a 300-slot list, reloads
the live list after each disposal callback before clearing the entry, frees the
current list, and resets the associated resource and timers. State 3 updates
the timer or status before setting the mode; other values store the mode byte.
The focused caller checks exercise original Game and Init caller windows;
they do not qualify the entirety of those callers or helper implementations.

The second function was previously missing from the linked inventory: an
obsolete generated absolute-symbol assignment hid the separate object symbol.
The tracked layout now records the two verified assembly boundaries, and the
tracked symbol definition tells Splat that the second function is defined.
Only that stale local generated assignment was removed. An inventory-only
relink changed two ELF bytes for the symbol section, with no executable or
data changes. On this corrected baseline, before the C replacements, Game
was **3,747 / 4,843 (77.37%)** and total **4,420 / 5,516 (80.13%)**.
The denominator increased because an existing function was no longer hidden.

Tools commit `dc218ae` provides the focused checks:

```sh
wsl -d PSBBN --exec python3 -m unittest tools.tests.test_game_hud_state_15178eb0_match -v
```

An independent guest model passed 240 cases per entry across retail, raw C,
and both padded streams, including callbacks that mutate the live list.
Original Init and Game caller windows passed 108 cases across the streams;
84 selected access-cut prefixes were compared for retail and padded code.
The unguarded transition was checked semantically because of its different
register allocation. Native 32-bit checks passed eight reset and 120
transition cases at each of `-O0`, `-O2`, and `-O3`, with UBSan and eight
effective negative controls. Twenty-four GNU links across three symbol
layouts verified both padded objects against rebased retail. The real Splat
parser and symbol writer passed a canary and an effective negative control.
These focused checks do not establish live gameplay behavior.

The suite passed after installation in mounted tools and against staged
sibling dependencies; the sibling checkout was not changed. The production
object and ELF equal the audited shadow and the other 1,453 linked objects
remain unchanged. The strict full-image comparison against the corrected
inventory accounts for 314 changed bytes with zero exclusions. Only the two
intended bodies differ among 6,051 functions, all addresses are unchanged,
and all 189,088 protected Game-data bytes are identical. Seven other owner
functions, pools, and diagnostics are unchanged.

The production recount reports Game **3,749 / 4,843 (77.41%)**, total
**4,422 / 5,516 (80.17%)**, zero address drift, and **126** more Game
matches required for 80%.
