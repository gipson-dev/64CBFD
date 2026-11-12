# Sequence transition direct match

Date: 2026-11-12. `func_1501E1B4` in
`conker/src/game/generated_49D30.c` replaces a zero-return placeholder. Its
81-word slot is VA `0x1501E1B4..0x1501E2F8`, ROM `0x4B664..0x4B7A8`.
The existing symbol remains because its original name is not established.

For transition state zero, the active slot and predicate gate determine
whether to clear the trigger; a remaining duration of at least 91 starts a
30-tick transition, fade, synchronization and conditional audio request.
State one counts down using the signed frame delta, or enters state two,
calls the completion handler and resets to zero. Other states leave it alone.
Both predicate and completion calls receive the slot observed in the original
instructions. An external draft passed a state address instead; that argument
was corrected before compilation. Unsigned low-word arithmetic retains the
retail wrap for the duration subtraction and countdown.

IDO O2/g3 with the owner's existing no-unroll setting emits all 81 retail
words and 27 relocation sites directly from C, with no guards. Both owner
padders agree; all 56 other owner functions, normalized pools, register
metadata and diagnostic categories are unchanged.

The six-check suite passed before and after installation in the mounted tools
checkout and a staged sibling environment with mounted fallbacks. The MIPS
model compared 800 cases per raw, retail and padded body, visiting all 81
words. It covered transition states, slot selection, the 90/91 boundary,
signed countdown extremes, and helper changes to the timing data. SDK32 native
checks ran 5,376 cases per O0/O2/O3 with trap UBSan and rejected 12 incorrect
variants. Four rebases, modeled guest access-cut prefixes and 144 cases through
the byte-exact original sequence-time caller prefix passed. The helpers were
modeled in these tests: `func_1501E05C` and `func_1501DF04` remain separate
zero-return placeholders in production, so this match does not establish
complete transition behavior or gameplay.

Actual scoped Make and the independently predicted full ELF agree: 251 changed
bytes, zero exclusions or metadata groups, all 6,050 function addresses fixed,
and 189,088 protected Game data bytes unchanged. The link held 1,453 other
objects fixed; this was not a clean rebuild. Make's binary matches an independent
objcopy. ELF SHA-256
`033eaa1258cf9025bba5d10439c90480d5389b4c26bbb5798958307c353f2db5`;
binary SHA-256
`bc0146e3f256af14651abc699f45327d2d288d426f04e96bcfb7a9bff5646b0a`.
Existing duplicate recipe warnings remain. Tools commit `0ef14bf` precedes the
consumer update.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,723 / 4,840 (76.92%)**, overall
**4,396 / 5,513 (79.74%)**, zero drift. Game requires 149 more exact
functions to reach 80%; the broader matching goal remains open.

The scoped Graphify refresh retained unrelated nodes: 59,922 before and
59,924 after, with three relocated IDs matched by signature and no out-of-scope
removals or changes. Its fail-closed path retained 31,816 existing nodes;
this was not a full-corpus extraction.
