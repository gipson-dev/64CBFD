# Resource motion callback guarded match

Date: 2026-11-12. `func_15157AA8` in `conker/src/game/generated_183640.c`
replaces its zero-return placeholder. Its retail slot is VA
`0x15157AA8..0x15157D88`, ROM `0x184F58..0x185238`: **184 words**,
with a `0x30`-byte frame. The original resource dispatcher
`func_151572D0` invokes it through table entry 0 of `D_8008AD90`.
The retail symbol is retained because a more specific game name is not proven.

The reconstructed routine updates resource position and angles using stored
velocities and the global time step. Flag bit 1 enables position integration;
bit 8 repeatedly damps horizontal velocity for the unsigned tick count, bit 4
applies vertical acceleration, and bit 2 advances angles. A local may-alias
view models resource offsets without asserting an unverified wider type.

The compiler emits **168 of 184 words** directly in place. Sixteen checked,
non-relocation word guards restore the retail frame size, floating-point
register scheduling, and two independent reads. Both padders produce the exact
retail body and bindings; every guard was deliberately corrupted in turn and
rejected by each padder, and four rebased GNU links were checked. The
unadjusted compiler body reads the time and acceleration in a different order;
partial-fault or memory-mapped read ordering is only established for the guarded
output. The signed bit pattern of a negative tick count acts as a large unsigned
count in this reconstruction; such long executions were not exhaustively run.

The six-check suite passed in both mounted and staged sibling-tools
configurations before and after adoption. It includes 7,488 bounded finite-input guest
cases against an independent reference, covering every retail instruction;
1,728 native cases at each of O0/O2/O3 with trap UBSan and five semantic
negative controls; and 128 modeled connected dispatcher cases. Access-boundary
checks compare the guarded output with retail. Tests cover bounded tick counts,
finite floating-point values and valid separate object and global storage;
they do not establish hardware FPU exceptions, arbitrary aliasing or gameplay.
The sibling run used staged new files with its available dependencies and
mounted fallbacks; pre-existing sibling changes were preserved.

A private Make-planned owner build predicted the complete ELF; actual scoped
Make produced the same image. All 6,050 function addresses and 25 owner
neighbors are unchanged, as are all 189,088 protected Game-data bytes. The
ELF has 564 changed bytes, no metadata permutations and zero exclusions. The
scoped link held 1,453 other existing objects and the linker script fixed; this
was not a clean rebuild. Make's binary matches independent objcopy output. ELF
SHA-256 `3a875cb61d873bbb37338026bae52818d73aa2c70f2bc1543aec4dcb71bae0e1`;
binary SHA-256 `61f6af3e796f6d2bf60bfbbb1fc3c4eebc7203d85f066548db9c99d7a7c5ecf3`.
Existing unrelated owner diagnostics and a duplicate Make recipe remain. A
full ROM checksum was not re-established.

Tools commit `c2c9889` precedes the consumer change. A read-only host-port
spot check found an empty generated definition in
`64CBFDOGL/recomp_scene/frontend_room_out/.c`; active-build applicability is
unknown. No host build or gameplay test was performed.

Fresh production ELF recount: Game **3,710 / 4,840 (76.65%)** and overall
**4,383 / 5,513 (79.50%)**, zero drift. Game needs 162 additional exact
functions to reach 80%.

The scoped graph refresh retained unrelated nodes: 59,898 before and 59,900
after, with no out-of-scope removals or changes; three relocated IDs matched
by signature. The fail-closed path retained 31,816 existing nodes. This was
not a full-corpus extraction.
