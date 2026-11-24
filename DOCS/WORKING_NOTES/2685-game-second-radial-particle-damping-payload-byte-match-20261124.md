# Second radial particle damping payload byte match - 2026-11-24

`func_150CBABC` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_F8590.c`. All 137 words / 548 bytes match retail after
41 expected-word private-stack displacement guards; 96 other words emit directly.
The 168-byte frame, registers, instruction/call order, arithmetic, control flow,
all 18 bindings and s32 return one are emitted by the compiler. No instruction is
inserted or omitted, no pool/profile/Makefile changes, and no dummy or enlarged
object is introduced. All nine raw/padded owner neighbors remain unchanged.

Production recount: **4,664 / 5,528 (84.37%)** total, Game **3,991 / 4,855
(82.20%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift and 864 different.
**35 more matches are required for 85%**. Only this target gains one match.

Retail VA 150CBABC..150CBCE0, ROM F8F6C..F9190. The shared radial interface
carries 15 o32 words: source, signed index, x/y/z, origin x/y/z, signed heading,
start byte, radius, style, extra float, context and slot byte. This routine uses
coordinates, heading and slot. All four incoming register homes follow retail.
Coordinates reload after the first float RNG; heading reloads with LH and slot
with LBU. The original factory/direction/copy declarations keep their widths.
The registry's generic C callback typedef uses a byte heading, while this body
reloads a signed halfword. The original parents supply byte-range values; these
checks establish the actual o32 instruction ABI, not portable compatibility of
every C function-pointer type in the registry.

The recovered `RadialParticle150CBABC` descriptor is exactly 112 bytes. The
kind-0x29 particle shares the prior radial constructor's packet format but has
different constants: lifetime `%41+40`, channel byte `%157+100`, pitch `%26-25`,
paired size `sample*D_800A0624+300`, speed `(sample*500+1000)*D_800A0628`, final
field62 seven and field22 sixty. The unsigned channel expression can reach 256
before its byte store, which wraps to zero; this boundary is tested explicitly.
Five integer RNG calls and two float RNG calls retain their complete order.
The last two integer draws add flags 0x40/0x80 to base 0xE05. External fields
D_800A062C and D_800A0630 provide the packet coefficient and captured damping.
Actual coefficient bits at D_800A0624/28/2C/30 are pinned as
43C88000/3C23D70A/3F828F5C/3F7645A3, including mutable-provider load ordering.

The factory receives `(&packet,1,4,slot,1)`. On success the captured damping
word copies to result+0xA8; failure skips the copy and still returns one. A late
reload after the factory can mutate the damping global is detected as incorrect.

The private layout map is closed and uniform:

| Object | Raw IDO offset | Retail offset | Bytes |
| --- | ---: | ---: | ---: |
| Saved integer RNG draw | SP+0x28 | SP+0x24 | 4 |
| Captured damping payload | SP+0x30 | SP+0x2C | 4 |
| Descriptor | SP+0x38 | SP+0x34 | 112 |

Each guard preserves the full upper 16 instruction bits and reduces only the SP
displacement by four. Every emitted access/pointer into all three objects is
covered. Both layouts fit the original frame and remain disjoint from RA at
SP+0x1C and all incoming/outgoing argument homes. Frame and saved-register
lifetimes remain unchanged. Both padders yield the same complete owner.

The actual owner Make route contains three commands: IDO, generated padding and
assembly. Unlike the preceding F5800 owner it has no literal or data pools and
no owner-specific pool-checker command. Raw before/candidate retain absent
.rodata/.data sections; both padded owners retain absent .rodata and the same
empty GNU-as .data section as the baseline. No literal-pool
corruption count or updater-checker replay is claimed for this owner.

The independent reference uses frozen old owner C plus original target assembly,
without the recovered target C or its guards. Shadow Make and production equal
the complete predicted ELF: **569 changed bytes, zero exclusions**. All named
definitions/strings are reconstructed; all 189,088 protected Game data bytes,
720 data owners, conversion rows and other frozen inputs remain unchanged.

Four retail-equivalent guest streams each pass 776 cases, execute all 137 words
and agree through 207 complete access-fault quads. An extra raw-C execution per
case agrees after mapping only the three private objects and their pointer
arguments. Random initial private bytes, all descriptor bytes/holes and call
boundary observations are preserved. Coverage includes all 256 radial byte
angles, signed-halfword boundaries, four rounding modes, unsigned remainders,
both flag branches, mutable providers and both factory outcomes. Incoming-home
mutation cases qualify guest ABI behavior, not portable C fault semantics.

SDK32 native O0/O2/O3 each pass 512 legal, backed, nonoverlapping cases with
strict aliasing, controlled rounding and UBSan. Canonical dual32 digests inspect
ordered arguments, globals, output/canaries and the real four copied payload
bytes. Only 52 initialized descriptor bytes are inspected before direction and
84 at submission; 28 unspecified bytes are excluded from native observations.
Thirteen source controls compile and fail comparison with exit 42, including
RNG/divisor/packet, pitch/speed, slot/context/extent, copy-destination, late
payload reload and return changes. No signal, compile failure or UBSan trap is
accepted as an effective comparison control.

The aligned complete pristine-ROM census finds zero direct JAL/J references
and one pointer at ROM 22F4F8 / VA 8008AA38, D_8008AA00[14]. All four complete
original registry parents (1514C2F0, 1514C470, 1514C678, 1514C858) run 384 cases
per retail-equivalent child stream and 384 raw-map cases. All 15 arguments,
352 child calls per stream and saved state agree. Eight return-zero controls
stop after one child where correct return one allows two. Parent coverage is
95/96, 113/130, 112/120 and 128/138 words. Two parents remain unmatched in the
live ELF; these finite original-body executions give them no matching credit.

The 18-word small-particle wrapper, 61-word constructor and 11-word memcpy are
all pinned to pristine ROM and the actual baseline ELF. Eight connected cases
per stream cover both allocation outcomes, exact 0xAC-byte allocation, full
descriptor copy and the extra damping word. All 70 target-reachable helper
words execute for fixed mode one / null optional state; other factory modes
and optional-state paths are excluded. Allocation, RNG and direction stay
opaque. No helper gains matching credit.

Boundary controls reject 82 guarded corruptions, expose 192 unguarded changes,
pin 18 bindings and reject both oversized slots. Sixteen GNU links and 32 guest
rebases cover carry/sign/address regions. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 117.745s | 5 fresh / 0 reused |
| preinstall-sibling | 148.92s | 5 fresh / 0 reused |
| installed-primary | 125.305s | 5 fresh / 0 reused |
| installed-sibling | 122.914s | 5 fresh / 0 reused |

The isolated second tools overlay verifies imported code and data dependencies;
the separately dirty sibling stays unchanged. Prior unchanged neighbor semantic
receipts are reused by body/ABI/binding/pool/guard fingerprints, not called fresh.
This task uses zero Claude calls. Tools commit before consumer. The root README
changes only its two aggregate rows; function detail lives in this note.

Consumer baseline: `032fcf1629cb56be712c6f100279dac10825e383`.
Tools qualification commit: `593c9e1e71c8347b54136a840d4f5f0dcb04c372`.
ELF SHA256: `1babdba11ca66fb63f3d6f384c0837a7550c12e4c2bb4bc971ceac75dd679c33`.
Padded owner SHA256: `fad466a9fbdbb006d919dccf354434f5d6e608049813de03eac4473a03bbf9c3`.
Initial freeze: 3561 inputs / 2155 copies. Receipts:
`conker/build/game-radial-particle-150cbabc-private`.

Graphify was queried before target work. Native update and a scoped AST merge
retain old IDs and qualification after actual hook producers are terminal.
No full-corpus extraction, host build/launch, Release change, push, all-input
equivalence or gameplay acceptance is claimed. The next candidate is
`func_150CB800`, a neighboring unmatched 140-word constructor in this owner.
Existing updater matches remain untouched; private actor-scan/matrix screens
remain unadopted and uncredited. The 85% goal remains active.
