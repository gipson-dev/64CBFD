# Sequence transition predicate direct match

Date: 2026-11-12. `func_1501E05C` in
`conker/src/game/generated_49D30.c` replaces a zero-return placeholder. Its
86-word slot is VA `0x1501E05C..0x1501E1B4`, ROM `0x4B50C..0x4B664`.
The existing symbol remains because its original name is not established.

The predicate considers the current scene, a one-shot trigger, an event byte,
controller button bits, hardware state, lock and override bytes, a sequence
availability helper, and the current/limit times. Scene `0x1D` can consume
the trigger; scene `0x21` uses a distinct button/hardware/time test. Other
paths can call `func_1501D2C4` with the scene and slot's event, then re-read
the force and time values after that helper. The external draft treated
`D_800BE710` as a pointer; retail reads a halfword directly. The 30-tick
addition uses explicit unsigned arithmetic to retain low-word wrap.

IDO O2/g3 with the owner's existing no-unroll setting emits all 86 retail
words and 27 relocation sites directly from C, with no guards. Both owner
padders agree; all 56 other owner functions, normalized pools, register
metadata and diagnostic categories are unchanged.

The seven-check suite passed before and after installation in the mounted
tools checkout and a staged sibling environment with mounted fallbacks. The
MIPS model compared 12,288 cases per raw, retail and padded body, visiting
85 of 86 words; it covers both scene gates, button/lock/override combinations,
valid slots, the 300/301 threshold and helper mutations. SDK32 native checks
ran 24,576 cases per O0/O2/O3 with trap UBSan and rejected 13 incorrect
variants. Four rebases, modeled guest access-cut prefixes, and 768 cases
connected to the byte-exact original `func_1501E1B4` call site passed. Sixteen
cases execute the byte-exact original `func_1501D2C4` override branch; its
remaining paths and other external behavior are not established by that test.
The completion handler `func_1501DF04` remains a placeholder, and gameplay
and hardware behavior were not tested.

Actual scoped Make and the independently predicted full ELF agree: 262 changed
bytes, zero exclusions or metadata groups, all 6,050 function addresses fixed,
and 189,088 protected Game data bytes unchanged. The link held 1,453 other
objects fixed; this was not a clean rebuild. Make's binary matches an independent
objcopy. ELF SHA-256
`96c81d37d3b4dfba78e365f792785ebb17cc8c884de949667572761834bddfa5`;
binary SHA-256
`7e071ba57834bb8a51e92d8cae4634f8d2400985cc8dffc23f0b4c83fbd15e78`.
Existing duplicate recipe warnings remain. Tools commit `e4089f2` precedes the
consumer update.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,724 / 4,840 (76.94%)**, overall
**4,397 / 5,513 (79.76%)**, zero drift. Game requires 148 more exact
functions to reach 80%; the broader matching goal remains open.

The scoped Graphify refresh retained unrelated nodes: 59,924 before and
59,926 after, with three relocated IDs matched by signature and no out-of-scope
removals or changes. Its fail-closed path retained 31,816 existing nodes;
this was not a full-corpus extraction.
