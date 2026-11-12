# Type-0x64 timer callback guarded match

Date: 2026-11-12. `func_151041E4` in
`conker/src/game/generated_131620.c` replaces a zero-return C placeholder.
Retail spans VA `0x151041E4..0x1510448C` and ROM `0x131694..0x13193C`,
170 words. It receives a record pointer and progresses four states: a
height/timer gate, fade-in, timed hold, and fade-out or release. The two
actor-adjust transitions intentionally obtain their tag bytes from different
saved pointers. It is registered as the secondary callback in descriptor
column 100; the allocating routine is documented in [Note 458](458-game-type64-record-allocator-match-20260929.md).

IDO emits 168 words from the recovered semantic C. **76 expected-word guard
rows, including two inserted words**, normalize the linked body and its
relocations to all 170 retail words. This is a guarded match, not a direct
compiler match. The source uses unsigned intermediate arithmetic for 32-bit
wrap before signed comparisons; the conversion of out-of-range unsigned values
to signed and signed right shift rely on the prepared target compiler's
conventions. A 16-byte unused local preserves the retail frame; its original
purpose is unknown. The volatile height access preserves the unconditional
retail read and is not claimed to be the original source qualifier.

Nine durable tools checks pass in the mounted and sibling environments after
installation; the same staged files also passed both before adoption.
The suite checks 3,204 bounded guest cases across normal and signed-boundary
inputs with modeled helpers; 1,056 SDK32 native cases at O0/O2/O3 under
undefined-behavior sanitization; threshold and signed-overflow negative
controls; and 240 original retail-walker cases with modeled downstream helpers.
It also checks 44 modeled external-access cuts, both padders, rejection of 76
corrupted expected words and six corrupted expected relocations per padder,
five wrong replacement/insertion controls, and 12 rebased GNU links. The
private [Note 2314](2314-game-type64-timer-callback-private-screen-20261112.md)
records additional overlapping-layout and successful access-trace screens.
These tests do not establish all aliases, host C fault behavior, hardware FPU
exceptions, full frame execution, or gameplay.

The actual production owner compile, pad and assemble matched the qualified
shadow object. The final production ELF was linked by Make while 1,453 other
existing linker-script objects and the existing linker script were held fixed;
this is a scoped build, not a clean rebuild. Its complete bytes matched the
independently predicted shadow image: **524 changed ELF bytes**, no exclusions,
all function addresses and three owner neighbors unchanged, and 189,088
protected data bytes unchanged. Make objcopy produced the same binary as the
shadow ELF. Production SHA-256: ELF
`d9e10f0fbaf35b429bbaf525df9456962ef01549fb4a132fd282cb3fc73b5f44`, binary
`13a4c1813a081ab174f8e3eb2ec12a4dec093eab8b6f19d08783730472ca8d02`.
The pre-existing `generated_12D630` duplicate recipe warning persists. A full
ROM checksum was not re-established by this scoped build.

The tools commit `7f88d90` precedes the consumer change. The standalone sibling
tools checkout's pre-existing dirty work was preserved. A read-only host-port
spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unverified. No host build or gameplay test was performed.

Fresh production ELF recount: **3,706 / 4,840 (76.57%)** Game and **4,379 /
5,513 (79.43%)** overall, zero drift. The Game 80% target needs 166 more
matches. The secondary walker `func_151671E8` remains private; its other
registered callback `func_151AD174` still has a zero-return placeholder.

The scoped graph refresh retained unrelated nodes: 59,887 before and 59,889
after, with no out-of-scope removals or changes and three relocated IDs matched
by signature. It retained 31,816 existing nodes through the fail-closed path;
this is not a full-corpus extraction.
