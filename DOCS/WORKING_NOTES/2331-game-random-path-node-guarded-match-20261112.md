# Random path node guarded match

Date: 2026-11-12. `func_150793D8` in `conker/src/game_A28B0.c`
replaces a zero-return placeholder. Its 102-word slot is VA
`0x150793D8..0x15079570`, ROM `0xA6888..0xA6A20`. Its original name is
not established, so the existing symbol is retained.

The handler converts the first object's X/Z coordinates to signed halfwords;
if either lies outside the inclusive -1180..1180 range, it resets both to
zero. It passes a random 16-bit yaw and a 550-unit distance to
`func_1505A184`, adds the resulting planar offsets, clamps each signed
halfword to -1200..1200, and stores X/Z into the next node of the active
actor's selected path. It reloads the current actor and command byte after
the helper calls. The original dispatcher calls table entry
`D_80086730[180]` and does not consume a result.

IDO O2/g3 emits the complete semantic routine with 97 of 102 words matching
directly. Five expected-word guards change only the saved local coordinate
slots from stack offsets `0x2A`/`0x28` to retail's `0x24`/`0x22`:
the two possible X stores, Z store, and corresponding two reloads. The
helper-output floats are at `0x34`, `0x30`, and `0x2C`; the unchanged
argument area is below these slots. No relocation is altered. Both isolated
padders and the full owner padder yield the retail body. All 210 other owner
functions, normalized pools, register metadata, and diagnostic categories
are unchanged. Guard corruption is rejected for every row.

The six-check suite passed before and after installation in the mounted tools
checkout and a staged sibling environment with mounted fallbacks. A bounded
MIPS model compared 3,600 cases per raw, retail and padded body, including
the -1180/1180 and -1200/1200 boundaries, signed coordinates, path selection,
and helper-driven current-actor and command changes. SDK32 native checks ran
9,800 cases per O0/O2/O3 with trap UBSan and rejected 12 incorrect variants.
Four rebases, modeled guest access-cut prefixes, and 288 cases connected to
the byte-exact original dispatcher passed. Both helper implementations were
checked byte-exact against the live ELF; their behavior was modeled in these
tests, not executed. Results cover finite, representable float conversions and
valid path storage; unrestricted portable-C casts, hardware exceptions and
gameplay are not claimed.

Actual scoped Make and the independently predicted complete ELF agree: 329
changed bytes, zero exclusions or metadata groups, all 6,050 function
addresses fixed, and 189,088 protected Game data bytes unchanged. The link
held 1,453 other objects fixed; it was not a clean rebuild. Make's binary
matches an independent objcopy. ELF SHA-256
`e0ae08dcd90b7f19dc640aa6a155686afef6cf3c534e53576309bfbdd7d95330`;
binary SHA-256
`b2ff29dfd83ead9231fa0f7d8fb6c3e4b5fc4b69e19e0153c8b2d9edce3bec45`.
Existing compiler and duplicate recipe warnings remain. Tools commit `c073699`
precedes the consumer update.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,722 / 4,840 (76.90%)**, overall
**4,395 / 5,513 (79.72%)**, zero drift. Game requires 150 more exact
functions to reach 80%; the broader matching goal remains open.

The scoped Graphify refresh retained unrelated nodes: 59,920 before and
59,922 after, with three relocated IDs matched by signature and no out-of-scope
removals or changes. Its fail-closed path retained 31,816 existing nodes;
this was not a full-corpus extraction.
