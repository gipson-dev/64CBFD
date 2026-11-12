# Path movement duration direct match

Date: 2026-11-12. `func_1507602C` in `conker/src/game_A28B0.c`
replaces a zero-return placeholder. Its 103-word slot is VA
`0x1507602C..0x150761C8`, ROM `0xA34DC..0xA3678`. The old draft's
single combined index was wrong: retail selects a path using the actor's
`unk13F`, then indexes that path with the script byte and reads the next
8-byte node's signed X and Z fields. The draft was removed. The existing
function name is retained because its original name is not established.

The routine calls `func_15075548`, publishes the node index, calculates the
planar distance and a duration from current movement rate, clamps durations
below 12 while adjusting that rate, and sets the duration counter, vertical
velocity, and state byte. The scale `D_8009A140` is word `0x3DAAAA7E`
(approximately 0.083333); both semantic fixtures use this retail value.
The callback is table entry `D_80086730[16]`; its observed dispatcher does
not consume a return value. Its original setup helper and nested flag helper
are each byte-exact in the current ELF.

IDO O2/g3 emits all 103 retail words and nine relocation sites directly
from C without guards. Both padders agree; 210 other owner functions,
normalized pools, register metadata and diagnostic categories are unchanged.
The focused seven-check suite passed before and after installation, in the
mounted tools checkout and a staged sibling environment with mounted fallbacks.
The modeled MIPS checks cover 96 finite cases per raw, retail and padded body,
visiting 85 words; native SDK32 checks cover 48 cases at O0/O2/O3 under trap
UBSan and reject ten deliberately wrong variants. Four symbol rebases and
modeled guest access-cut prefixes pass. Sixty-four cases connect the original
dispatcher window; 64 connect both original helpers with a rate sentinel and
the actor override disabled. Those routines were verified against the live ELF.
The helper-switch screen uses a model, and floating exceptions, arbitrary C
pointer/conversion behavior, full helper coverage and gameplay are not claimed.

Actual scoped Make and the strict independent full-image prediction agree:
308 changed ELF bytes, zero exclusions or metadata groups, all 6,050 function
addresses unchanged, and all 189,088 protected Game data bytes unchanged.
The scoped link held 1,453 other objects fixed; it was not a clean rebuild.
Make's binary matches an independent objcopy. ELF SHA-256
`2dfafae72eac82b1d1aa43a7897320a74cd7d66c337b1368afdb4ee6ac417820`;
binary SHA-256
`208ef701a01015dbd9eac5f4c823308dd6d9e112199419b64c3f94d4048d9173`.
Existing compiler and duplicate recipe warnings remain; diagnostic categories
were unchanged. Tools commit `59792d1` precedes this consumer update.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,721 / 4,840 (76.88%)**, overall
**4,394 / 5,513 (79.70%)**, zero drift. Game requires 151 more exact
functions to reach 80%; the broader matching goal remains open.

The scoped Graphify refresh retained unrelated nodes: 59,918 before and
59,920 after, with three relocated IDs matched by signature and no out-of-scope
removals or changes. Its fail-closed path retained 31,816 existing nodes;
this was not a full-corpus extraction.
