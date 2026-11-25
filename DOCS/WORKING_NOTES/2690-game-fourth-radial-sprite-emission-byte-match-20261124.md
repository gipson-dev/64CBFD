# Fourth radial sprite emission byte match - 2026-11-24

`func_150CDF10` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_FB060.c`. Its 142-word / 568-byte instruction body
matches after 38 expected-word guards map private descriptor SP displacements.
The complete retail slot is 144 words / 576 bytes; two trailing owner-alignment
NOPs remain unchanged. They are padding rather than extra recovered C operations.
The other 104 words emit directly. The original frame, registers, instruction
sequence, arithmetic, control flow, s32 return one and all 26 binding sites
are emitted by the compiler. No instruction insertion/omission, new pool,
profile/Makefile change, dummy local or enlarged descriptor is introduced.

Actual production is **4,669 / 5,528 (84.46%)** total, Game **3,996 / 4,855
(82.31%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 859 different.
**30 more matches are required for 85%**. Only this target gains one match.
Both raw/padded owner neighbors, including the adopted CDCF4 body, stay fixed.

The instruction body spans VA 150CDF10..150CE148 / ROM FB3C0..FB5F8;
the slot extends to VA 150CE150 / ROM FB600. The two padding words are pinned
against the frozen ELF and pristine ROM by the independent image predictor.
The final owner fragment retains the original slot extent. Both oversized
controls exceed the full 144-word slot. Its radial interface carries
15 o32 words: source, signed index, x/y/z, origin x/y/z, signed heading, start
byte, radius, style, extra float, context and slot byte. This body uses only
coordinates, heading and slot. Positions are captured before RNG providers;
incoming A0/A1 homes, signed LH heading, LBU slot and outgoing homes match
retail. The generic registry C typedef has a byte heading; original parents
supply byte-range values. These checks establish the actual o32 instruction
ABI, without claiming every portable C function-pointer type is compatible.

`RadialSprite150CDF10` is exactly 124 bytes. Initial rotations are zero,
scales and field00 one, flags 0x29E8, field56 32 and field04 D_800A07C4.
Three ordered unsigned integer RNG calls choose pitch `%41-61`, lifetime `%21+50`
and byte field60 `%76+180`. Five float RNG calls choose direction speed
`(sample*101+150)*D_800A07C8`, lateral components `(sample*260-130)`
multiplied by D_800A07CC and D_800A07D0 respectively, acceleration
`(sample*D_800A07D4+D_800A07D8)*D_800A07DC`, and paired size
`(sample*302+52)*D_800A07E0`. Tail field61 is eight. The factory receives
`(&packet,3,255,0,slot,0)`; its pointer is ignored and there is no damping copy.
The function returns one for either factory outcome.

The eight coefficient bits at D_800A07C4..D_800A07E0 are pinned in address
order as 3E4CCCCD/3DCCCCCD/3DCCCCCD/3DCCCCCD/439B8000/C4982000/3A83126F/3A83126F.
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
predicted ELF: **635 changed bytes, zero exclusions**. Named definitions
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
and one pointer at ROM 22F520 / VA 8008AA60, D_8008AA00[24]. All four complete
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
and damping-copy chain from CDCF4 are not substituted for this contract.

Boundary controls reject 76 guarded corruptions, expose
208 unguarded changes, pin all 26 bindings, reject both oversized slots,
and pass 16 GNU links / 32 guest rebases through carry/sign/address regions.
Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 206.67s | 5 fresh / 0 reused |
| preinstall-sibling | 204.351s | 5 fresh / 0 reused |
| installed-primary | 191.279s | 5 fresh / 0 reused |
| installed-sibling | 194.767s | 5 fresh / 0 reused |

The second tools copy is an isolated dependency-verified overlay; the separately
dirty real sibling is preserved. Prior unchanged neighbor semantic receipts
are reused by body/ABI/binding/pool/guard fingerprints, not called fresh.
This task uses zero Claude calls. Tools commit before consumer; root README
changes only aggregate rows, with detailed narrative in this note.

Consumer baseline: `74db017350d8347d7b4b46f303fde143b35d1e62`.
Tools commit: `257110f83b4788e88a22018221f7e7e5359524c9`.
Production ELF SHA256: `afa8df6626c13e49fb4a65e9fc21830358be4845540d183770b3ca8dc14467d3`.
Padded owner SHA256: `23bea549dc4d0bdce8ff8a437c87e6f545041a0d87b159c14cc756b916b9aba9`.
Freeze: 3614 inputs / 2210 copies. Receipts are in
`conker/build/game-radial-sprite-150cdf10-private`.

Graphify query preceded target work. Native update and scoped AST merge retain
old IDs/qualification after actual hook producers are terminal. No full-corpus
extraction, host build/launch, Release change, push, all-input equivalence or
gameplay acceptance is claimed. Next: select the next unmatched family from the current production recount and
Graphify. Existing matches stay fixed; private actor-scan/matrix screens remain
unadopted. The 85% goal stays active.

The qualified source retains one blank line at EOF. The scoped whitespace
review verifies that this is the only default whitespace finding, keeps the
qualified source bytes and SHA unchanged, and passes all other whitespace
checks with only the EOF-blank rule disabled for that command. No repository
configuration or source/binary qualification pin is changed.
