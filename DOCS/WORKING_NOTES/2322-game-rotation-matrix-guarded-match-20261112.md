# Alternate rotation matrix guarded match

Date: 2026-11-12. `func_15187D6C` in
`conker/src/game/generated_1B1600.c` replaces a zero-return placeholder.
The executable retail span is 83 words at VA `0x15187D6C..0x15187EB8`,
ROM `0x1B521C..0x1B5368`; the 85-word layout slot includes two padding words.
The retail symbol is retained because a more specific original name has not
been established. [Note 2321](2321-game-rotation-matrix-private-screen-20261112.md)
records the private investigation and the owner compiler-profile constraint.

The routine scales three input angles by `D_8008D578`, calls `sinf` and
`cosf` for each, initializes a 4-by-4 identity matrix with `func_151EFE00`,
and fills its nine rotation cells. The original caller window at `0x15187BD8`
selects this routine from a per-record byte and then passes its output to a
matrix-combination helper. Full caller reachability and gameplay remain open.

The semantic C uses the owner's existing `-O2 -g3 -Wo,-loopunroll,0`
profile. Ten checked word guards restore eight opening instruction and
relocation positions and two uses of one private stack slot; no instructions
are inserted. Both padders match all 83 original instructions and their
relocations. The seven-check tools suite passed in mounted and staged sibling
environments before and after installation. It includes 686 finite-input guest
cases for each raw, retail and guarded body covering all 83 original words;
343 SDK32 native cases at each of O0/O2/O3 with trap UBSan and five effective
negative controls; twenty guard-corruption rejections; four GNU relocation
rebases; and 250 connected caller-window cases. Trig and identity helpers were
modeled in the bounded semantic checks, which do not prove hardware FPU behavior,
arbitrary aliases, full caller behavior or gameplay. The forced global-load
fault test confirms a difference in the raw body's stack-save order; the
guarded output restores the retail instruction order. The sibling run used
its available dependencies and mounted fallbacks; its existing dirty work was
preserved.

Actual scoped Make produced the independently predicted complete ELF: 298
changed bytes, two audited symbol-order groups, zero exclusions, and all 6,050
function addresses and 31 owner neighbors unchanged. All 189,088 protected
Game-data bytes remain unchanged. The link held 1,453 other existing objects
and the linker script fixed; it was not a clean rebuild. Make's binary matches
independent objcopy output. ELF SHA-256
`487d69181acd1fb7108c4a1dd34b025e564f71ad37b500739fa0677ec2798225`;
binary SHA-256
`f4fa53d80c6e72606d58b243e69e8c3a9c68dbe471910e69b8c371e3eccd744a`.
The existing duplicate `generated_12D630` Make recipe warning remains. A full
ROM checksum was not re-established.

Tools commit `efc769f` precedes the consumer change. A read-only host-port
spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,711 / 4,840 (76.67%)** and overall
**4,384 / 5,513 (79.52%)**, zero drift. Game needs 161 additional exact
functions to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,902 before and 59,904
after, with no out-of-scope removals or changes; three relocated IDs matched
by signature. The fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
