# Second radial sprite emission byte match - 2026-11-24

`func_150CB800` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_F8590.c`. Its full 140-word / 560-byte retail slot
matches after 38 expected-word guards map private descriptor SP displacements.
The other 102 words emit directly. The original frame, registers, instruction
sequence, arithmetic, control flow, s32 return one and all 26 binding sites
are emitted by the compiler. No instruction insertion/omission, new pool,
profile/Makefile change, dummy local or enlarged descriptor is introduced.

Actual production is **4,665 / 5,528 (84.39%)** total, Game **3,992 / 4,855
(82.22%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 863 different.
**34 more matches are required for 85%**. Only this target gains one match.
All nine raw/padded owner neighbors, including the adopted CBABC body, stay fixed.

Retail VA 150CB800..150CBA30, ROM F8CB0..F8EE0. Its radial interface carries
15 o32 words: source, signed index, x/y/z, origin x/y/z, signed heading, start
byte, radius, style, extra float, context and slot byte. This body uses only
coordinates, heading and slot. Positions are captured before RNG providers;
incoming A0/A1 homes, signed LH heading, LBU slot and outgoing homes match
retail. The generic registry C typedef has a byte heading; original parents
supply byte-range values. These checks establish the actual o32 instruction
ABI, without claiming every portable C function-pointer type is compatible.

`RadialSprite150CB800` is exactly 124 bytes. Initial rotations are zero,
scales and field00 one, flags 0x29E8, field56 32 and field04 D_800A0604.
Three ordered unsigned integer RNG calls choose pitch `%36-55`, lifetime `%33+32`
and byte field60 `%101+155`. Five float RNG calls choose direction speed
`(sample*200+200)*D_800A0608`, lateral components `(sample*300-149)`
multiplied by D_800A060C and D_800A0610 respectively, acceleration
`(sample*D_800A0614+D_800A0618)*D_800A061C`, and paired size
`(sample*300+101)*D_800A0620`. Tail field61 is two. The factory receives
`(&packet,3,255,0,slot,0)`; its pointer is ignored and there is no damping copy.
The function returns one for either factory outcome.

The eight coefficient bits at D_800A0604..D_800A0620 are pinned in address
order as 3E4CCCCD/3DCCCCCD/3DCCCCCD/3DCCCCCD/4416C000/C5162000/3A83126F/3A83126F.
Provider mutations exercise actual load order. Native definitions, initializers
and snapshots follow address order, accounting for this routine's three-global
acceleration expression and constant size multiplier.

The closed private map moves only the 124-byte descriptor from raw SP+0x2C
to retail SP+0x28. Every one of 38 changed words preserves its upper 16 bits
and SP base and reduces only the displacement by four. Every descriptor access
and pointer formation is covered. Both layouts fit the unchanged 168-byte
frame; RA stays at SP+0x1C, saved RNG at SP+0x20, and incoming/outgoing homes
are untouched. No other object is mapped. Raw C also executes independently
with initial descriptor bytes mapped and only descriptor pointers canonicalized.

Both padders agree. The actual owner Make route has three commands (IDO,
generated padding, assembly), with no owner-specific pool checker. Raw
.rodata/.data are absent; padded .rodata is absent and .data is empty exactly
as in the baseline. No F5800 updater-checker or pool-corruption count is claimed.

The independent reference uses frozen old C and original target ASM, without
the recovered target C or guards. Shadow and production Make equal the full
predicted ELF: **574 changed bytes, zero exclusions**. Named definitions
and strings are reconstructed explicitly. All 189,088 protected Game data
bytes, 720 data owners, conversion rows and other frozen inputs are unchanged.

Four normalized/padded/original guest streams each pass 776 cases;
an extra raw-C run per case agrees after the private mapping. All 140 words
execute, including 220 complete access-fault quads. Cases cover all
256 radial byte angles, signed-halfword boundaries, four rounding modes,
unsigned remainder boundaries, mutable providers and both factory outcomes.
All 124 descriptor bytes and holes agree at call boundaries. Incoming-home
mutation cases qualify guest ABI behavior only, not portable C fault semantics.

SDK32 native O0/O2/O3 each pass 512 legal, backed, nonoverlapping cases
with controlled rounding, strict aliasing and UBSan. Canonical dual32 digests
inspect ordered arguments, coefficient/global state, output/canaries and only
54 initialized descriptor bytes before direction / 112 at submission; 12
unspecified bytes are excluded. All 14 source controls compile and fail
comparison with exit 42. No compile failure, signal or UBSan trap is counted.

The entire aligned pristine-ROM census finds zero direct JAL/J references
and one pointer at ROM 22F4FC / VA 8008AA3C, D_8008AA00[15]. All four complete
original registry parents execute 384 cases per retail-equal stream and
the same number of raw-map cases, observing all 15 words and
352 child calls per stream. Eight return-zero controls stop after one child
where return one allows two. Parent coverage remains 95/96, 113/130, 112/120,
128/138 words. Two parents remain unmatched live; finite original executions
do not grant parent matching credit or prove all paths.

The complete original 15-word factory wrapper and 256-word extended consumer
are independently assembled/bound against pristine ROM. The wrapper matches
the live ELF; the extended consumer remains unmatched there. Its 0x7C-byte
copy contract is pinned independently. Internals remain contracted, not freshly
executed here, and helper matching credit is zero. The small-particle factory
and damping-copy chain from CBABC are not substituted for this contract.

Boundary controls reject 76 guarded corruptions, expose
204 unguarded changes, pin all 26 bindings, reject both oversized slots,
and pass 16 GNU links / 32 guest rebases through carry/sign/address regions.
Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 194.12s | 5 fresh / 0 reused |
| preinstall-sibling | 173.17s | 5 fresh / 0 reused |
| installed-primary | 139.381s | 5 fresh / 0 reused |
| installed-sibling | 243.239s | 5 fresh / 0 reused |

The second tools copy is an isolated dependency-verified overlay; the separately
dirty real sibling is preserved. Prior unchanged neighbor semantic receipts
are reused by body/ABI/binding/pool/guard fingerprints, not called fresh.
This task uses zero Claude calls. Tools commit before consumer; root README
changes only aggregate rows, with detailed narrative in this note.

Consumer baseline: `c206d20c36d447a81fbbe82f20bff3730fc9e7ed`.
Tools commit: `a7b8363c69542b2e5807469b5131956e03781eda`.
Production ELF SHA256: `ccdab705d0d113020ccbc8786fb27398ad64bae1996a919fb06ace108822f36c`.
Padded owner SHA256: `a2a31f6f0a886c2c77cd9a5e33914bae23c69a3c8adf3d84940cd4405fdb2b70`.
Freeze: 3571 inputs / 2165 copies. Receipts are in
`conker/build/game-radial-sprite-150cb800-private`.

Graphify query preceded target work. Native update and scoped AST merge retain
old IDs/qualification after actual hook producers are terminal. No full-corpus
extraction, host build/launch, Release change, push, all-input equivalence or
gameplay acceptance is claimed. Next: inspect the unmatched radial constructors
`func_150CC6B8` (135 words) and `func_150CCA7C` (142 words). Existing matches stay
fixed; private actor-scan/matrix screens remain unadopted. The 85% goal stays active.
