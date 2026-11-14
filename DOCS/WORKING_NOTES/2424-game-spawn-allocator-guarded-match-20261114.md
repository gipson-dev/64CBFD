# Game spawn allocator guarded match

Date: 2026-11-14. `func_151A8B20` replaces the zero-return placeholder in
`conker/src/game/generated_1D4E00.c`. Its 115-word retail slot is
`0x151A8B20..0x151A8CEC` (ROM `0x1D5FD0..0x1D619C`). The semantic C emits
114 words with the original 0xA8-byte frame. Six expected-word guards adjust
two branch spans, move a paired floating temporary from SP+0x48 to SP+0x40,
and restore the spatial-result store and branch-delay flags read. The last
row inserts one read; no original instruction is omitted. Both padded
outputs match all 115 retail words and their relocations.

The typed interface accepts a request pointer, signed-halfword lifetime,
extra payload bytes, byte channel and context. It snapshots 40 request
bytes, initializes the fixed fields of an 88-byte payload, and calls
`func_15149130`. Lifetime -1 selects 300 and disables the lifetime mode;
other lifetimes use the signed-halfword input. The allocation includes 88
base payload bytes plus the extra-byte argument. Failure returns NULL.
Success copies the 88-byte payload into the allocated record at offset
0x28, optionally resolves a spatial record using snapshotted X/Z coordinates,
and chooses owner-derived scale or the squared request size times a global
factor. Flags and owner are reloaded after the spatial helpers.

Thirty copied local payload bytes retain earlier stack contents: offsets
0x30..0x43, 0x4A..0x4B and 0x50..0x57. The final eight bytes are initialized
after the copy. Guest checks seed and compare all copied bytes. Native
checks exclude these indeterminate bytes and use typed, aligned, disjoint
objects. Finite float-to-integer inputs and extra-byte sums without signed
overflow are the portable native domain.

Guest validation compares an independent bounded model with retail, raw C
and padded streams in 1,280 cases. The 4,068 executions include 64 windows
of all four original direct callers (`func_151A90C0`, `func_151A9390`,
`func_15012020`, and `func_1515A974`) and 12 guest-only overlap cases.
The cases cover allocation failure, lifetime narrowing and sentinel,
upper channel bits, flag/owner combinations, floating rounding, mutated
incoming homes, request snapshots and late helper-visible state changes.
Retail and padded modeled machine states agree at 140 fired access
prefixes. All 114 reachable retail instructions are exercised. The original
duplicate load at `0x151A8C3C` is unreachable from normal entry and remains
present; it is not counted as exercised.

Native 32-bit C passes 320 cases in each of six O0/O2/O3 and
strict/no-strict-aliasing configurations with trapping UBSan. All seven
altered source controls are detected. The allocator, memcpy and spatial/
height helper contracts are modeled; complete caller/helper execution,
unrestricted aliases, invalid floating conversions, hardware and gameplay
are not qualified. Earlier receipts for the unchanged complete constructor
bodies remain prior evidence, distinct from the fresh connected call windows.

Both padding implementations pass 12 GNU links across four independently
rebased layouts, including independent global-address carry boundaries.
The other 22 owner functions and normalized pools are unchanged; the target
compile has no diagnostics. Production Make uses the ordinary compiler and
padding rules for the changed owner. Since the six appended guards belong
only to this target and every earlier row is preserved, the scoped build
marks the guard manifest old and reuses the 697 frozen neighboring objects:

```sh
make -C conker -j4 -o retail_word_patches.us.csv build/conker.us.elf progress.csv
```

The production ELF equals the independent shadow prediction. The strict
whole-image audit accounts for all 435 changed bytes with zero exclusions,
including two closed symbol/string-table ordering cycles. All 6,051 function
addresses and 189,088 protected Game-data bytes remain fixed. Only the target
owner changes among 698 frozen linked objects. The conversion manifest,
Makefile and all earlier guard rows remain unchanged.

Tools commit `9513a63` retains the installed regression suite. It passes in the
mounted tools checkout and an isolated sibling tools overlay, preserving
all 2,434 preexisting sibling dirty paths. `make tools-check` also passes:

```sh
PYTHONPATH=. python3 -m unittest tools.tests.test_game_spawn_allocator_151a8b20_installed -v
```

A scoped fail-closed Graphify refresh retains all 60,137 existing node IDs
and produces 60,137 nodes. This is not a full-corpus re-extraction.
The host port needs no source update for this retail-only match; its frozen
Release is untouched and no host runtime acceptance is claimed.

Fresh production recount: Game **3,798 / 4,843 (78.42%)**, total
**4,471 / 5,516 (81.06%)**, zero drift. At the current denominator,
**218** additional exact matches are needed to reach 85% total.
Continue with the adjacent `func_151A8CEC` effect-update callback; keep
private candidates uncredited until the complete qualification gates pass.
