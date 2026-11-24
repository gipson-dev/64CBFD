# Masked lifetime radial particle payload byte match - 2026-11-24

`func_150CC6B8` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_F9430.c`. The complete 135-word / 540-byte slot
matches retail after 41 expected-word guards map closed private SP offsets;
94 other words emit directly. The 168-byte frame, registers, instruction/call
order, arithmetic, control flow, return one and all 18 binding sites are emitted
by the compiler. No instruction is inserted or omitted. There is no new pool,
profile/Makefile change, dummy local or enlarged descriptor.

Actual production: **4,666 / 5,528 (84.41%)** total, Game **3,993 / 4,855
(82.25%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 862 different.
**33 more matches are required for 85%**. Only this target gains one match.

Retail VA 150CC6B8..150CC8D4, ROM F9B68..F9D84. `RadialParticle150CC6B8` is a
112-byte descriptor. The body carries the 15-word radial o32 interface: source,
signed index, x/y/z, origin x/y/z, signed heading, start byte, radius, style,
extra float, context and slot byte. It uses coordinates, heading and slot.
All four register argument homes match retail; coordinates reload after the
first float RNG, heading through LH and slot through LBU. The registry's generic
C typedef uses a byte heading while original parents supply byte-range values.
These checks establish the actual instruction ABI, not portable compatibility
of every C function-pointer type in the registry.

Five integer RNG calls and two float RNG calls retain their full order. The
kind-0x29 descriptor has lifetime `(u32)draw%16+20`, which the compiler emits as
an AND-0xF mask rather than division. This removes two words compared with the
earlier 137-word constructor. Cases explicitly include draws 0, 15, 16, 31 and
0xFFFFFFFF. Channel byte `%156+100` stays within 100..255. Pitch is `%21-25`;
paired size is `sample*D_800A06CC+300`, and speed is
`(sample*200+350)*D_800A06D0`. Two later draws choose flags 0x40/0x80 atop 0xE05.
Final fields are field62 eight, field1E ten, field20 twenty-five and field22
twenty-seven. Packet field24 loads D_800A06D4; damping captures D_800A06D8.
Coefficient bits for D_800A06CC, D_800A06D0, D_800A06D4 and D_800A06D8 are pinned as
43C88000/3DCCCCCD/3F851EB8/3F66A7F0, including mutable-provider load order.

The factory receives `(&packet,1,4,slot,1)`. On success memcpy copies the captured
four-byte damping value to result+0xA8; failure skips the copy and still returns
one. A reload after the factory can mutate the damping global is detected.

The private layout map is uniform and complete:

| Object | Raw IDO offset | Retail offset | Bytes |
| --- | ---: | ---: | ---: |
| Saved integer RNG draw | SP+0x28 | SP+0x24 | 4 |
| Captured damping payload | SP+0x30 | SP+0x2C | 4 |
| Descriptor | SP+0x38 | SP+0x34 | 112 |

Every guard keeps the full upper 16 bits and SP base and reduces only the
displacement by four. All accesses and pointer formations into these objects
are covered. Both layouts fit the unchanged frame, disjoint from RA at SP+0x1C
and all incoming/outgoing homes. No other object, register or operation changes.

This owner needs `structs.h` for its vertex type. The include and new descriptor
declarations preserve all five other function bodies/bindings in the complete
owner, both raw and padded. Both padders agree, and the actual Make route has
three commands: IDO, generated padding and assembly. Raw .rodata/.data remain
absent; padded .rodata is absent and .data stays empty as in the baseline.
No owner-specific pool checker or literal-pool corruption count is claimed.

The independent reference uses frozen old C plus the original target assembly,
without recovered target C or its guards. Shadow and production Make equal
the complete predicted ELF: **550 changed bytes with zero exclusions**.
Named definitions and strings are reconstructed explicitly. All 189,088 protected
Game data bytes, 720 data owners, conversion rows and other frozen inputs stay fixed.

Four normalized/padded/original guest streams each pass 777 cases and
execute all 135 words. An extra raw-C run per case agrees after canonicalizing
only the three private objects and their pointer arguments. Random initial
bytes and all descriptor holes agree at call boundaries. There are
207 complete access-fault quads. Coverage includes all 256 radial byte
angles, signed-halfword boundaries, four rounding modes, remainder/mask
boundaries, both flag branches, mutable providers and both factory outcomes.
Incoming-home mutations qualify guest ABI behavior, not portable C fault semantics.

SDK32 native O0/O2/O3 each pass 513 legal, backed, nonoverlapping cases,
with controlled rounding, strict aliasing and UBSan. Canonical dual32 digests
inspect ordered arguments, globals, output/canaries and the real copied payload.
Only 52 initialized descriptor bytes are inspected before direction and 84 at
submission; 28 unspecified bytes are excluded. All 13 source controls compile
and fail comparison with exit 42, including `%16` changed to `%15`, direction,
slot/context/extent, copy destination, late damping reload and return. No signal,
compile failure or UBSan trap counts as a successful negative control.

The complete aligned pristine-ROM census finds zero direct JAL/J references
and one pointer at ROM 22F504 / VA 8008AA44, D_8008AA00[17]. All four complete
original registry parents run 384 cases per retail-equivalent child stream
plus raw-map cases. All 15 words, 352 child calls per stream and saved state
agree. Eight return-zero controls stop after one child where correct return one
allows two. Parent coverage remains 95/96, 113/130, 112/120, 128/138 words. Two
parents stay unmatched live; finite original-body execution gives them no C
matching credit or all-path equivalence claim.

The original 18-word particle wrapper, 61-word constructor and 11-word memcpy
are pinned to pristine ROM and the actual baseline ELF. Eight connected cases
per stream cover both outcomes, exact 0xAC-byte allocation, descriptor copy and
extra damping word. All 70 target-reachable helper words execute for fixed mode
one / null optional state. Other factory modes and optional-state paths are
excluded. Allocation/RNG/direction stay opaque, and helper matching credit is zero.
The unrelated extended sprite consumer is not substituted for this chain.

Boundary checks reject 82 guarded corruptions, expose
188 unguarded changes, pin 18 bindings and reject both oversized slots.
Sixteen GNU links and 32 guest rebases cover carry/sign/address regions.
Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 107.155s | 5 fresh / 0 reused |
| preinstall-sibling | 102.381s | 5 fresh / 0 reused |
| installed-primary | 101.315s | 5 fresh / 0 reused |
| installed-sibling | 118.364s | 5 fresh / 0 reused |

The isolated second tools overlay verifies code/data dependencies and preserves
the separately dirty sibling. Unchanged neighbor semantic receipts are reused
by body/ABI/binding/pool/guard fingerprints and are not labeled fresh. This task
uses zero Claude calls. Tools commit before consumer; root README changes only
its aggregate rows, with detail in this note and concise entries in five indexes.

Consumer baseline: `644d9421a799a4a5aaf4ff9c3b13b6c241ff8458`.
Tools commit: `1cb802b16351f0852ea06776656c860a84f29028`.
ELF SHA256: `d784c0589bf006a10f7e9d9be529de67a50eb04a1ed3f824da4728e247c9a522`.
Padded owner SHA256: `e2624f505741ce2cda5512fb34698c2f1d285a8c0667acb83120bd0ffafe34c7`.
Freeze: 3582 inputs / 2177 copies. Receipts are in
`conker/build/game-radial-particle-150cc6b8-private`.

Graphify query preceded target work. Native update and scoped AST merge retain
all old IDs/proof metadata after actual hook producers are terminal. No full-
corpus extraction, host build/launch, Release change, push, all-input equivalence
or gameplay acceptance is claimed. Next: `func_150CCA7C`, the adjacent unmatched
142-word radial sprite constructor. Existing matches and private uncredited
actor-scan/matrix screens stay protected. The 85% goal remains active.
