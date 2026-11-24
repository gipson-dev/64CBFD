# Radial sprite emission byte match - 2026-11-24

`func_150CADD0` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_F5800.c`. Its complete 142-word / 568-byte retail slot
matches after 38 expected-word guards map the private descriptor's SP offsets.
The other 104 words emit directly. The compiler emits the original instruction
sequence, frame, registers, arithmetic, return and all 26 relocation sites.
There is no instruction insertion/omission, new literal pool, compiler profile
or Makefile change. Eighteen raw/padded neighbors and all prior guard rows remain fixed.

Actual production recount is **4,663 / 5,528 (84.35%)** total and Game
**3,990 / 4,855 (82.18%)**; Init **492 / 492**, Debugger **181 / 181**,
zero address drift and 865 different. **36 more matches are required for 85%**.
Only this target receives one new match. The already matched updater
`func_150CB008` and independently inspected helpers receive no duplicate credit.

Retail VA 150CADD0..150CB008, ROM F8280..F84B8. The routine returns s32 one
regardless of the factory result. Its shared radial ABI carries 15 o32 words:
source, signed index, x/y/z, origin x/y/z, signed heading, start byte, radius,
style, extra float, context and slot byte. This body uses x/y/z, heading and
slot. Incoming A0/A1 homes, signed LH heading reload, LBU slot reload and all
outgoing argument homes follow retail. Positions are captured before providers;
later incoming-home changes must not move them. The signed-short direction
prototype and six-argument sprite factory declaration are reused unchanged.

The existing `RingSprite150C9DC4` descriptor is exactly 124 bytes. Initial
rotations are zero, scales one, flags 0x29E8, field00 one and field56 32.
Three ordered unsigned integer RNG draws select pitch `%21-40`, lifetime
`%51+50`, and byte field60 `%76+180`. Five ordered float RNG draws determine
direction speed, two lateral components, acceleration and paired sizes.
Direction speed is `(sample*204+500)*D_800A05C0`; lateral components use
`(sample*260-130)` with their own coefficient. Acceleration is
`(sample*1008+D_800A05CC)*D_800A05D0`; sizes use
`(sample*D_800A05D4+200)*D_800A05D8`.

The eight external coefficients at D_800A05BC..D_800A05D8 retain, in address
order, bits 3E4CCCCD/3DCCCCCD/3DCCCCCD/3DCCCCCD/C540D000/3A83126F/44164000/3A83126F.
Their actual baseline ELF values are pinned in the caller gate. Provider
mutations exercise load ordering. The factory receives `(&packet,3,255,0,slot,0)`.
No extra payload or conditional success copy is added; the return pointer is ignored.

Source screens recover the original chained-store ordering with live pitch,
sample and saved integer draw locals. The descriptor extent remains 0x7C;
there is no dummy/dead local or enlarged descriptor. The remaining mapping is:

| Object | Raw IDO offset | Retail offset | Bytes |
| --- | ---: | ---: | ---: |
| Descriptor | SP+0x2C | SP+0x28 | 124 |

Every one of the 38 guards preserves the full upper 16 instruction bits and
reduces only its SP displacement by four. Every access/pointer formation into
the descriptor is covered. Both layouts fit the unchanged 168-byte frame;
RA stays at SP+0x1C, the saved RNG word at SP+0x20, and incoming/outgoing homes
stay fixed. The mapped descriptor remains disjoint from all these objects.

Both padders, the actual four-command Make route and existing updater literal
pool checker pass. The independent image is built from frozen old owner C plus
the original target assembly, without the recovered target C or its guards.
Shadow Make and production Make equal its complete predicted ELF: **607 changed
bytes with zero exclusions**. ELF named definitions and strings are reconstructed
explicitly. All 189,088 protected Game data bytes and 720 data owners, conversion
rows and remaining frozen inputs stay unchanged.

Four normalized/padded/original guest streams pass 776 cases each, execute all
142 words and agree through 220 complete access-fault quads. Cases include
all 256 radial byte angles, signed-halfword boundaries, four rounding modes,
unsigned remainder boundaries, both factory outcomes and mutable providers.
An extra raw-C run per case agrees after canonicalizing only descriptor bytes
and descriptor pointer arguments. Private initial bytes are mapped, never
zero-filled; all 124 bytes, including unspecified holes, agree at call boundaries.
Incoming-home mutation cases exercise the guest ABI only and make no portable C
or native fault-semantics claim.

SDK32 native O0/O2/O3 each pass 512 legal, backed, nonoverlapping cases under
strict aliasing, controlled rounding and UBSan. Ordered arguments, coefficient
state, factory output/canaries and initialized packet bytes use canonical
dual32 digests. Only 54 initialized descriptor bytes are observed before
direction, and 112 at submission; 12 unspecified bytes are excluded from native
observation. Fourteen source controls compile and fail comparison with exit 42:
flags, lifetime, alpha byte, pitch, speed, lateral component, acceleration,
size, slot, context, payload extent, resource, tail field and return value.
No compile failure, signal or UBSan trap counts as an effective negative control.

The complete aligned pristine-ROM census finds zero direct JAL/J references
and one pointer at ROM 22F510 / VA 8008AA50, registry D_8008AA00[20]. All four
table consumers are covered: func_1514C2F0, func_1514C470, func_1514C678 and
func_1514C858. Their complete original bodies execute 384 cases per retail-equal
child stream and another 384 raw-stack-map cases. All 15 arguments, 352 child
calls per stream and saved state agree. Eight return-zero controls stop after
one child where the correct return one permits two. Visited parent words are
95/96, 113/130, 112/120 and 128/138. This is finite provider-backed original
parent execution; two parents remain unmatched in production and no all-path
parent equivalence is claimed.

The complete original 15-word factory wrapper and 256-word extended sprite
consumer are independently assembled and bound against pristine ROM. The
wrapper also matches the live ELF. The extended consumer remains unmatched
there; its original 0x7C-byte memcpy contract is pinned separately. Helper
internals remain contracted rather than freshly executed here. The unchanged
contract is not transferred from the distinct small-particle factory. No helper
matching credit or live consumer correctness is claimed.

Boundary gates reject 76 guarded corruptions, expose 208 unguarded corruptions,
pin all 26 bindings, reject both oversized slots and reject 18 retained-pool
corruptions. Sixteen GNU links and 32 guest rebases cover carry/sign/address
regions. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 95.024s | 5 fresh / 0 reused |
| preinstall-sibling | 112.861s | 5 fresh / 0 reused |
| installed-primary | 112.967s | 5 fresh / 0 reused |
| installed-sibling | 123.986s | 5 fresh / 0 reused |

The second tools copy is an isolated dependency-verified overlay; the separately
dirty sibling is untouched. Unchanged neighbor semantic receipts are reused
by body/ABI/binding/pool/guard fingerprints and are not labeled fresh checks.
This routine uses zero Claude calls. The tools qualification commits before
the consumer. Root README changes only its two aggregate status rows.

Consumer baseline: `0e44c37f21e4f505ecf953946e14f01998ea2dca`.
Tools qualification commit: `f0df56ea57a08ddeafb35e56ecb7e74f7acfc988`.
Production ELF SHA256: `ab21814d815f72053d949d4a7ae3bda19870fd2ea3f156936a194ec1f9dafdb4`.
Padded owner SHA256: `88d999d1a4706f1293bb263dae1fdd356590e84957aeb67cf0fdce89a17b4001`.
Initial freeze: 3550 inputs / 2144 copies; receipts are in
`conker/build/game-radial-sprite-150cadd0-private`.

Graphify was queried before target selection. Native update and a scoped
AST merge retain old IDs and qualification after actual hook producers are
terminal. This is not a full-corpus extraction. The host sibling has no usable
source checkout at its expected path; no host build, launch or Release change
is performed. No push, all-input equivalence or gameplay acceptance is claimed.
Next: `func_150CBABC`, another 137-word radial constructor in generated_F8590.c.
Its private draft has the retail length/frame and 41 stack-offset differences,
but remains uninstalled and uncredited pending a fresh frozen qualification.
The larger actor-driven func_150CB1F4 remains a candidate; func_150CB008 is already matched.
The private actor-scan and matrix screens remain unadopted and uncredited.
The 85% goal remains active.
