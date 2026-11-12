# Resource matrix callback direct match

Date: 2026-11-12. `func_15157918` in
`conker/src/game/generated_183640.c` replaces its zero-return placeholder.
The retail slot is VA `0x15157918..0x15157AA8`, ROM
`0x184DC8..0x184F58`: **100 words**, frame `0x20`. All instructions and five
named relocations emit directly from C under the existing IDO O2/g3 profile,
with **no new guards, insertions, or profile changes**. The retail symbol is
retained because a more specific gameplay name is not established.

The callback asks `func_150A8050` to build the selected resource matrix from
three stored parameters, copies the resource position into its translation
row, and multiplies its 3-by-3 portion by the stored scale. It reloads the
selected index and scale as shown by the retail instructions. The constructor
`func_15157010` initializes matrices at offsets `0x7C` and `0xBC`; the normal
frame path toggles `D_800BE9C0` with XOR 1. The local view models these two
slots and uses a GNU may-alias annotation. The checks cover indices 0 and 1;
arbitrary corrupted indices and out-of-bounds C behavior are not established.
The matrix builder remains original assembly in the decomp.

The installed five-check suite passed in mounted and standalone-sibling tools
environments. It includes 128 bounded guest/reference cases covering all 100
retail instructions, including a modeled helper changing the selected slot,
position and scale; 64 SDK32 native cases at each of O0/O2/O3 with trap UBSan
and four effective semantic negative controls; both padders and four rebased
GNU links; and 64 connected cases through the installed, retail-exact resource
dispatcher `func_151572D0` and table entry 1. The matrix builder and the
downstream update helper are modeled, and finite floating-point inputs were
used. These tests do not establish hardware FPU exceptions, arbitrary aliases,
full gameplay, or behavior outside the documented index domain. The sibling
run used staged new files with its own available dependencies and mounted
fallbacks where absent; its pre-existing dirty work was preserved.

The actual Make owner compile, pad, and assemble produced the qualified
object. A scoped Make link held 1,453 other existing objects and the existing
linker script fixed; this is not a clean rebuild. The complete ELF equals the
independently predicted image: **321 changed bytes**, zero exclusions or
metadata permutations, all 6,050 function addresses and 25 owner neighbors
unchanged, and all 189,088 protected Game-data bytes unchanged. Make's binary
matches independent objcopy output. Production SHA-256: ELF
`a5464c41c70f07cf9eb38737720e654f4295b695327f25d5d7b50b05fc85b909`, binary
`d106fea579204bdd62bd7e1383d781fc99d516bd5c5648cc0d31999292662624`.
The existing duplicate `generated_12D630` recipe and unrelated owner
pointer/integer diagnostics remain. A full ROM checksum was not re-established.

Tools commit `1133307` precedes the consumer change. A read-only host-port
spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; its active-build applicability
is unknown. No host build or gameplay test was performed.

Fresh production ELF recount: **3,709 / 4,840 (76.63%)** Game and
**4,382 / 5,513 (79.48%)** overall, with zero address drift. Game needs 163
more exact functions to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,896 before and 59,898
after, with no out-of-scope removals or changes. Three relocated IDs matched
by signature; the fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
