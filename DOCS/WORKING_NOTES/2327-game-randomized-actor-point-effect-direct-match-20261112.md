# Randomized actor point effect direct match

Date: 2026-11-12. `func_15146E84` in `conker/src/game/generated_173D40.c`
replaces a zero-return placeholder with the recovered callback. Its 111-word
slot spans VA `0x15146E84..0x15147040`, ROM `0x174334..0x1744F0`.
Its original symbol is retained because a more specific name is not established.

When the attachment at actor `+0x1D4` exists and `func_15146890` succeeds,
the callback obtains an effect slot. Amounts at least 71 first emit a slot
and point effect. The callback then builds a position from the selected X/Z and
the returned height. An integer random draw chooses between a wide effect
with a second integer draw and a simpler effect. Both paths draw a floating
sample and an integer random value in the retail order; their scales, ranges,
result vertices and point payload are preserved. The code deliberately
sequences random calls before constructing the arguments. The original table
`D_8008A0B4` entry 4 records this callback and count 80; this is a bounded
static caller observation, not a complete dynamic-caller census.

IDO O2/g3 emits all 111 retail instructions and 11 relocation sites directly
from C, including the original `0x88` frame, without new expected-word guards.
Ordering the local declarations reproduced the retail local stack slots;
the earlier same-length candidate differed in 14 local-offset instructions.
Both padders reproduce all 13 owner functions and the retail target, and all
12 other compiled owner functions and diagnostic rows remain unchanged.

Six focused checks passed in the mounted and staged sibling environments before
installation, and the full staged sibling suite passed again after installation. The guest model compared 8,192 cases per raw, retail and padded
body, reaching all 111 retail words. It covers all mode bytes, the 70/71
boundary, both random branches, varied integer draws, finite float samples,
helper mutations, output bytes and call order. SDK32 native tests ran 4,096
cases at each of O0/O2/O3 with trap UBSan and rejected 11 incorrect controls.
Four GNU relocation rebases, 320 original dispatcher-window cases and 96
connected cases through the actual 19-word retail `func_151D8E20` provider
also passed; its nested query return was modeled. The mounted owner, native,
dispatcher and provider checks passed again after installation. Other helpers,
random returns and bounded single-precision arithmetic are modeled; this does
not establish hardware floating exceptions, unrestricted aliases, complete
runtime dispatch, or gameplay. The sibling run uses staged changed files with
available sibling dependencies and mounted fallbacks, preserving its dirty work.

Actual scoped Make reproduced the independently predicted complete ELF: 329
changed bytes, zero metadata groups or exclusions, all 6,050 function addresses
and 12 neighboring owner bodies unchanged, and all 189,088 protected Game-data
bytes unchanged. The link held 1,453 other objects and its linker script fixed;
this was not a clean rebuild. Make's binary matches independent objcopy output.
ELF SHA-256 `5feed036c79d2bb26aba174846735356b846c86cd2a6b31b9af0532f9174e16d`;
binary SHA-256 `4cea976b600861b00c81f1682d5e6532d591a4b842a07f8af4df3ea6e80792a5`.
The pre-existing duplicate `generated_12D630` recipe warning remains; a full
ROM checksum was not re-established. Tools commit `275995d` precedes the
consumer change.

A read-only host-port spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production recount: Game **3,718 / 4,840 (76.82%)**, overall
**4,391 / 5,513 (79.65%)**, zero drift. Game needs 154 more exact functions
to reach 80%. The remaining neighboring stub `func_151470FC` is a possible
next candidate; its packet initialization and random calls require qualification.

A scoped Graphify refresh retained unrelated nodes: 59,912 before and 59,914
after; three relocated IDs matched by signature. Its fail-closed path retained
31,816 existing nodes. This was not a full-corpus extraction.
