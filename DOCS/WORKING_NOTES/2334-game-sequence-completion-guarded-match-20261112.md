# Sequence completion guarded match

Date: 2026-11-12. `func_1501DF04` in
`conker/src/game/generated_49D30.c` replaces a zero-return placeholder. Its
86-word slot is VA `0x1501DF04..0x1501E05C`, ROM `0x4B3B4..0x4B50C`.
The existing symbol remains because its original name is not established.

The routine polls a provider, conditionally stops audio, finds and releases an
actor, and refreshes the selected sequence slot. Its loop snapshots the
pending byte before each refresh and checks that saved value alongside the
live busy byte; helper changes therefore affect subsequent iterations. It can
submit a fade, then scans 25 actor records and clears the byte at offset
`0xA4` only for occupied records. The external draft wrote an entire word at
that offset; retail uses a byte store. Finally it clears a flag, synchronizes,
and writes the concluding mode bytes.

IDO O2/g3 with the owner's existing no-unroll setting emits 84 of the 86
retail words directly. Two expected-word guards swap independent LO16 address
completion instructions for the actor array and its end; their relocation
bindings move with the instructions. No memory operation is reordered. Both
owner padders agree; all 56 other owner functions, normalized pools, register
metadata and diagnostic categories are unchanged. Each corrupted guard fails.

The seven-check suite passed before and after installation in the mounted tools
checkout and a staged sibling environment with mounted fallbacks. The MIPS
model compared 512 cases per raw, retail and padded body, visiting all 86
words. Cases include bounded helper mutations, loop termination, both valid
slots, fade gates, and 25 actor records. SDK32 native checks ran 256 cases
per O0/O2/O3 with trap UBSan and rejected 12 incorrect variants. Four rebases,
modeled guest access-cut prefixes and 128 cases through the byte-exact
original `func_1501E1B4` completion call site passed. Sixteen cases also
execute one complete byte-exact `func_1501DE18` refresh, with its nested
providers modeled. Other helper paths, full transition behavior, hardware
and gameplay are not established by these tests.

Actual scoped Make and the independently predicted full ELF agree: 258 changed
bytes, zero exclusions or metadata groups, all 6,050 function addresses fixed,
and 189,088 protected Game data bytes unchanged. The link held 1,453 other
objects fixed; this was not a clean rebuild. Make's binary matches an independent
objcopy. ELF SHA-256
`431c9bd0c7f4927d9b370c5c0bec6be0759b319d1c6beac685edd305e5d86b1c`;
binary SHA-256
`4789b3ebfe5d77680372ccc9c05a956e3ec8addda7d2e5d15e209d1c2afcd19b`.
Existing duplicate recipe warnings remain. Tools commit `e33ae2b` precedes the
consumer update.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,725 / 4,840 (76.96%)**, overall
**4,398 / 5,513 (79.78%)**, zero drift. Game requires 147 more exact
functions to reach 80%; the broader matching goal remains open.

The scoped Graphify refresh retained unrelated nodes: 59,926 before and
59,928 after, with three relocated IDs matched by signature and no out-of-scope
removals or changes. Its fail-closed path retained 31,816 existing nodes;
this was not a full-corpus extraction.
