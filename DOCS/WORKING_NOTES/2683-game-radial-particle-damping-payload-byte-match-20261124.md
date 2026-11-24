# Radial particle and damping payload byte match - 2026-11-24

`func_150CAA04` replaces its zero-return placeholder with semantic C in
`conker/src/game/generated_F5800.c`. The complete 137-word / 548-byte slot is
retail-exact after 41 expected-word private-stack displacement guards. The
compiler emits the 168-byte frame, all 18 relocation sites, control flow,
registers, arithmetic and return directly. The other 96 words are raw-exact.
No instruction is inserted or omitted. The frame, saved-register slots,
incoming/outgoing argument homes, profile, Makefile and literal pools are unchanged.

Production recount: **4,662 / 5,528 (84.33%)** total, Game **3,989 / 4,855
(82.16%)**, Init **492 / 492**, Debugger **181 / 181**, zero drift, 866 different.
**37 more matches are required for 85%**. Only this target gains one match.

The prior handoff selected `func_150CAC28`, but live source, graph and recount
show it was already directly matched in [Note 2298](2298-game-four-damping-callbacks-match-20261112.md).
It remains unchanged and receives no duplicate credit. This checkpoint moves
to the adjacent unmatched radial constructor. The private actor-scan and matrix
screens likewise remain unadopted and uncredited.

Retail VA 150CAA04..150CAC28, ROM F7EB4..F80D8. The return is s32 and always one,
including allocation failure. The radial interface carries 15 o32 argument words:
source, signed index, x/y/z, origin x/y/z, signed heading, start byte, radius,
style, extra float, context and slot byte. Only x/y/z, heading and slot affect
this body; incoming homes still follow retail. Heading reloads through LH and
slot through LBU. The existing signed-short direction and five-argument particle
factory declarations are reused with their actual widths.

The constructor builds a kind-0x29 0x70-byte particle descriptor. Five ordered
integer RNG calls choose lifetime, a byte channel, signed pitch and two flags;
two float RNG calls choose paired sizes and direction speed. Position scalar
homes reload after the first float call. Globals D_800A05AC/B0/B4/B8 retain bits
43C88000/3DCCCCCD/3F851EB8/3F7374BD. Provider mutations exercise their load order.
The factory receives mode 1, four extra bytes, the current slot and context 1.
On success, memcpy writes the captured four-byte damping value to result+0xA8;
it must retain the value loaded before the factory can mutate its global.

Named live pitch, RNG draw, sample, payload and result locals recover the body
and frame. Source screens retain the exact 112-byte descriptor extent and a
four-byte damping scalar. No dummy/dead local or enlarged descriptor is used.
The remaining mapping is uniform and confined to three private objects:

| Object | Raw IDO offset | Retail offset | Bytes |
| --- | ---: | ---: | ---: |
| Saved integer RNG draw | SP+0x28 | SP+0x24 | 4 |
| Captured damping payload | SP+0x30 | SP+0x2C | 4 |
| Descriptor | SP+0x38 | SP+0x34 | 112 |

All 41 changed instructions preserve their complete upper 16 bits and reduce
only the SP displacement by four. Both layouts fit the unchanged frame and
remain disjoint from RA at SP+0x1C and all outgoing/incoming argument homes.
Every emitted access and pointer formation into these objects is audited;
no unchanged private access is omitted. All bindings remain at identical sites.
The corrected paired-size assignment emits the retail store order directly.

Both object padders, the existing four-command Make route and its updater pool
checker pass. All 18 raw/padded neighbors, compact/padded pools and historical
guard bytes remain unchanged. The independent image uses frozen old C plus
the original target assembly. Shadow Make and production Make equal its full
predicted ELF: 490 changed bytes with zero exclusions. Named definitions and
strings are reconstructed explicitly. All 189,088 protected Game data bytes,
720 data owners, conversion rows and remaining frozen inputs are unchanged.

Four normalized/padded/original guest streams pass 776 cases each and execute
all 137 words. Cases cover four rounding modes, all 256 radial byte angles,
signed-halfword boundaries, unsigned remainders, both flag branches, mutable
providers and both factory outcomes. An additional raw-C execution per case
agrees after canonicalizing only the three private object locations and their
pointer arguments; initial private bytes are mapped, never zero-filled. All
112 descriptor bytes and unused holes agree at each call boundary. There are
207 complete access-fault quads across the retail-equal streams. Guest-only
incoming-home mutation cases do not claim portable C or native fault semantics.

SDK32 native O0/O2/O3 each pass 512 legal, backed, nonoverlapping cases with
strict aliasing, rounding controls and UBSan. Ordered arguments, global state,
output/canaries and the real four-byte copied payload use canonical dual32
digests. Only 52 initialized descriptor bytes are inspected before direction
output and 84 at submission; 28 unspecified bytes are excluded from native
observation. Thirteen source controls fail comparison with exit 42. They cover
descriptor fields, RNG divisors, direction, slot/context, allocation extent,
copy destination, late damping reload and return value. No signal,
compile failure or UBSan trap counts as an effective negative control.

A complete aligned pristine-ROM census finds zero direct JAL/J references and
one pointer at ROM 22F50C / VA 8008AA4C, registry D_8008AA00[19]. All four table
consumers are inspected: func_1514C2F0, func_1514C470, func_1514C678 and
func_1514C858. Their complete original bodies execute 384 cases across four
retail-equal child streams, plus 384 raw-stack-map cases. All 15 arguments,
352 child calls per stream and saved state agree. Eight return-zero controls
stop after one child where return one permits two. Original parent coverage is
95/96, 113/130, 112/120 and 128/138 words; this is finite provider-backed retail
execution, not all-parent-path coverage. Two parents remain unmatched in
production and receive no C conversion or matching credit here.

The complete 18-word factory wrapper, 61-word constructor and 11-word memcpy
are pinned against pristine ROM and the actual baseline ELF. Eight connected
factory cases per child stream exercise both outcomes, exact 0xAC-byte
allocation arguments, descriptor copy and the extra damping copy. All 70 helper
words reachable for this target's fixed mode 1 / null optional-state contract
execute; other factory modes and the optional-state path are excluded. Allocation,
RNG and direction providers remain modeled. No helper gains new matching credit.

Boundary controls reject 82 guarded corruptions, expose 192 unguarded corruptions,
pin 18 bindings, reject both oversized slots and reject 18 retained-pool
corruptions. Sixteen GNU links and 32 guest rebases cover carry/sign/address
regions. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 105.823s | 5 fresh / 0 reused |
| preinstall-sibling | 91.466s | 5 fresh / 0 reused |
| installed-primary | 94.903s | 5 fresh / 0 reused |
| installed-sibling | 103.105s | 5 fresh / 0 reused |

The second tools copy is an isolated dependency-verified overlay; unrelated
sibling edits stay untouched. Unchanged neighbor semantic receipts are reused
by their body/ABI/relocation/pool/guard fingerprints, not called fresh checks.
This routine uses zero Claude calls. During the first object gate, one WSL
read blocked on a frozen hardlinked Python fixture. Native reads verified the
same SHA256 for live/frozen/banked copies, and the same job resumed without a
restart or byte change. Subsequent gates ran to normal completion.

Consumer baseline: `0d20aaf01e73a7a02885da8cff9cd390079514d2`.
Tools qualification commit: `6e585f6be8af1625e9f7f664a6b238ab03f53636`.
Production ELF SHA256: `e9c8709f2abecb6cba1a0fbd45f03a2f5cf40756c088e365092e82397c7d9f27`.
Padded owner SHA256: `542e5c9c0ab13b90aca639f602a315f841dca423b2e639d4d3dc3b343a9bef25`.
Initial freeze: 3540 inputs / 2134 copies; receipts are in
`conker/build/game-radial-particle-150caa04-private`.

Graphify was queried before selecting the unmatched target. Native update and
a scoped AST merge retain old IDs/qualification after actual hook producers
are terminal. No full-corpus extraction, host/Release change, push, all-input
equivalence or gameplay acceptance is claimed. Next: `func_150CADD0`, the adjacent
142-word radial constructor, confirmed unmatched in the current recount.
The 85% goal remains active.
