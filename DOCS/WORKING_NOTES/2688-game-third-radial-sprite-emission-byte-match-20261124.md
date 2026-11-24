# Third radial sprite emission byte match - 2026-11-24

`func_150CCA7C` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_F9430.c`. Its full 142-word / 568-byte retail slot
matches after 38 expected-word guards map private descriptor SP displacements.
The other 104 words emit directly. The original frame, registers, instruction
sequence, arithmetic, control flow, s32 return one and all 26 binding sites
are emitted by the compiler. No instruction insertion/omission, new pool,
profile/Makefile change, dummy local or enlarged descriptor is introduced.

Actual production is **4,667 / 5,528 (84.42%)** total, Game **3,994 / 4,855
(82.27%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 861 different.
**32 more matches are required for 85%**. Only this target gains one match.
All five raw/padded owner neighbors, including the adopted CC6B8 body, stay fixed.

Retail VA 150CCA7C..150CCCB4, ROM F9F2C..FA164. Its radial interface carries
15 o32 words: source, signed index, x/y/z, origin x/y/z, signed heading, start
byte, radius, style, extra float, context and slot byte. This body uses only
coordinates, heading and slot. Positions are captured before RNG providers;
incoming A0/A1 homes, signed LH heading, LBU slot and outgoing homes match
retail. The generic registry C typedef has a byte heading; original parents
supply byte-range values. These checks establish the actual o32 instruction
ABI, without claiming every portable C function-pointer type is compatible.

`RadialSprite150CCA7C` is exactly 124 bytes. Initial rotations are zero,
scales and field00 one, flags 0x29E8, field56 32 and field04 D_800A06DC.
Three ordered unsigned integer RNG calls choose pitch `%44-63`, lifetime `%51+50`
and byte field60 `%101+155`. Five float RNG calls choose direction speed
`(sample*200+300)*D_800A06E0`, lateral components `(sample*260-130)`
multiplied by D_800A06E4 and D_800A06E8 respectively, acceleration
`(sample*D_800A06EC+D_800A06F0)*D_800A06F4`, and paired size
`(sample*500+100)*D_800A06F8`. Tail field61 is three. The factory receives
`(&packet,3,255,0,slot,0)`; its pointer is ignored and there is no damping copy.
The function returns one for either factory outcome.

The eight coefficient bits at D_800A06DC..D_800A06F8 are pinned in address
order as 3E4CCCCD/3DCCCCCD/3DCCCCCD/3DCCCCCD/44BB8000/C55AC000/3A83126F/3A83126F.
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
predicted ELF: **611 changed bytes, zero exclusions**. Named definitions
and strings are reconstructed explicitly. All 189,088 protected Game data
bytes, 720 data owners, conversion rows and other frozen inputs are unchanged.

Four normalized/padded/original guest streams each pass 776 cases;
an extra raw-C run per case agrees after the private mapping. All 142 words
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
and one pointer at ROM 22F508 / VA 8008AA48, D_8008AA00[18]. All four complete
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
and damping-copy chain from CC6B8 are not substituted for this contract.

Boundary controls reject 76 guarded corruptions, expose
208 unguarded changes, pin all 26 bindings, reject both oversized slots,
and pass 16 GNU links / 32 guest rebases through carry/sign/address regions.
Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 134.709s | 5 fresh / 0 reused |
| preinstall-sibling | 104.498s | 5 fresh / 0 reused |
| installed-primary | 94.93s | 5 fresh / 0 reused |
| installed-sibling | 118.627s | 5 fresh / 0 reused |

The second tools copy is an isolated dependency-verified overlay; the separately
dirty real sibling is preserved. Prior unchanged neighbor semantic receipts
are reused by body/ABI/binding/pool/guard fingerprints, not called fresh.
This task uses zero Claude calls. Tools commit before consumer; root README
changes only aggregate rows, with detailed narrative in this note.

Consumer baseline: `ae3a7ba334afcdd95f63b62b2fc6ef8bad73039d`.
Tools commit: `768311c3d9e3b48e241f7b5efd250261b7e6ce5b`.
Production ELF SHA256: `2667fb46b47d1be7e6927fa4150c2ee10a2f167f955ca71ba97460962afb24fa`.
Padded owner SHA256: `37091e9aed884558c5bb80513023df5a64341ff34b689a890f92490c0939c534`.
Freeze: 3592 inputs / 2187 copies. Receipts are in
`conker/build/game-radial-sprite-150cca7c-private`.

Graphify query preceded target work. Native update and scoped AST merge retain
old IDs/qualification after actual hook producers are terminal. No full-corpus
extraction, host build/launch, Release change, push, all-input equivalence or
gameplay acceptance is claimed. Next: select the next unmatched family from the current production recount and
Graphify. Existing matches stay fixed; private actor-scan/matrix screens remain
unadopted. The 85% goal stays active.
