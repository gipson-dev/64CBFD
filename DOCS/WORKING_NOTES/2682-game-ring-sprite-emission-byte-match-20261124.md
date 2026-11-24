# Ring sprite emission callback byte match - 2026-11-24

`func_150C9DC4` is recovered as semantic C in `conker/src/game/generated_F5800.c`.
Its complete 174-word / 696-byte body matches retail after seven expected-word
scheduling guards. The compiler emits the 176-byte frame and all 30 relocation
sites directly. The other 167 instruction words match without normalization.
No inserted or omitted instruction, copied assembly body, profile, pool or
Makefile change is involved.

Production recount: **4,661 / 5,528 (84.32%)** total; Game **3,988 / 4,855
(82.14%)**; Init **492 / 492**, Debugger **181 / 181**, zero drift, 867 different.
**38 more matches are required for 85%**. Only this callback gains one match.

Retail VA 150C9DC4..150CA07C, ROM F7274..F752C. The callback returns void and takes
the ring record, a vertex pointer, a byte angle and two unused float payloads.
The direction helper retains its s16/s16/f32/vertex* interface; submission uses
the existing void*/s32/s32/s32/u8/s32 signature and its return is ignored.
The opening color-ramp helper takes its float argument in F12 and three output
pointers in A1..A3. Its actual call and writes are preserved even though this
callback does not consume the resulting colors.

Three ordered integer RNG draws select signed pitch, lifetime and a byte channel.
Eight ordered float draws select rotations, direction speed, two lateral values,
acceleration and paired sizes. Point copying occurs after the color helper and
before the first RNG. Owner scale, external coefficients and final slot/context
bytes reload at their observed provider boundaries. Provider mutations retain
that ordering; the unused sine/cosine payloads remain unused.

The complete original 256-word `func_1513264C` and 15-word `func_15132A4C` wrapper
are independently assembled, relocated and compared with pristine ROM. The
retail consumer calls memcpy with 0x7C at VA 151328C4..151328C8. This establishes
the 124-byte descriptor extent, including its unwritten six-byte tail, rather
than adding storage merely to force a frame. The installed consumer remains
unmatched (184 real word differences in the prior recount); the wrapper is
byte-exact. Neither helper gains matching credit or whole-helper semantic proof.

The descriptor begins at SP+0x34. The unused-but-addressed color outputs occupy
SP+0x30/0x2C/0x28 and the integer RNG result lives at SP+0x20. A named float sample
and the actual signed RNG local recover those homes. Reserving the true ABI tail
recovers the packet base; using addition of -130.0f and the retail paired-size
assignment order recovers the floating instructions and store order directly.

Guards at 0x30/0x34/0x38 reorder the same point-pointer reload and construction
of floating 1.0. Guards at 0x5C/0x60/0x64/0x6C reorder three scale stores and the
flags store, all before the first RNG. Both groups preserve instruction multisets
and all bindings. The complete remaining routine emits directly. All historical
guard bytes remain an exact prefix. All 18 raw/padded owner neighbors and both
compact/padded pools are unchanged. The existing updater literal-pool checker
and four-command Make route remain active and pass against the new whole owner.

The independent image reference uses frozen old C and the original target ASM.
Shadow Make and production Make equal its literal full-ELF prediction: 662 changed
bytes with zero exclusions. Symbol definitions, metadata order and strings are
reconstructed explicitly. All 189,088 protected Game data bytes, 720 data owners,
conversion rows and other frozen inputs remain unchanged.

Four guest instruction streams agree with pristine retail across 780 cases each,
all 174 executed words, all 256 angles, four rounding modes, unsigned remainder
boundaries, mutated providers, unused payloads and guest-only point overlaps.
There are 268 access-fault quads with equal full state. Full 124-byte sparse
packet snapshots preserve the original unwritten guest stack bytes at all 14
call boundaries. Guest faults/overlaps qualify instructions, not portable C.

SDK32 native O0/O2/O3 each pass 512 legal, backed, nonoverlapping cases under
strict aliasing, rounding controls and UBSan. Canonical dual32 digests compare
ordered arguments and owner/point/global state. Native packet observations read
only 54 initialized bytes before direction output and 112 initialized bytes at
submission; holes and reserved tail are never read. Twelve effective source
controls fail comparison with exit 42; no signal or UBSan trap counts as proof.
These finite cases establish no all-input equivalence or gameplay acceptance.

A complete aligned pristine-ROM census finds zero direct JALs and one pointer at
ROM 22D31C / VA 8008885C. The authentic parent callback window runs 192 cases
across four streams, qualifying all five o32 arguments, slot-one dispatch,
angle masking, saved-register state and two stack alignments. A wrong mask changes
valid calls/output. Complete parent execution and helper internals stay contracted.

Boundary controls reject 14 guarded corruptions, expose 334 unguarded corruptions,
pin 30 bindings and reject both oversized slots. Sixteen GNU links and 32 guest
rebases cover carry/sign/address regions. Eighteen retained-pool corruptions are
also rejected against the new owner. Shared `make tools-check` passes.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 104.853s | 5 fresh / 0 reused |
| preinstall-sibling | 90.638s | 5 fresh / 0 reused |
| installed-primary | 80.626s | 5 fresh / 0 reused |
| installed-sibling | 76.402s | 5 fresh / 0 reused |

The second tools copy is an isolated dependency-verified overlay; separately
dirty sibling work remains untouched. Unchanged neighbor semantic receipts are
reused by body/ABI/relocation/pool/guard fingerprints, not called fresh testing.
This routine uses zero Claude calls. One packet-only, tool-free Claude advisory
was used for the separate private actor-scan screen in Note 2681; its source
hypotheses did not improve emitted code and were not adopted.

Consumer baseline: `fb58b27d838695b8bc8b610c61ebb4d38bb21419`.
Tools qualification commit: `c127af5ea40219b20eafd11a1eb88337f2d6ff84`.
Production ELF SHA256: `e52f8d42b639543a818de7d3990a0dec4367e2d72805e9624d783ef79bbc341a`.
Padded owner SHA256: `d6da239822c28e14bd7657fe51ac3c62048a8b116bcc47de3eabe0055181c571`.
Initial freeze: 3529 inputs / 2123 copies; receipts are in
`conker/build/game-ring-sprite-150c9dc4-private`.

Graphify was queried first. Native update plus a scoped AST merge retain old
IDs/qualification after actual hook producers become terminal. No full-corpus
extraction, host/Release change, push or runtime acceptance is claimed.
Next: the related 106-word `func_150CAC28` repeated-damping updater. The private
actor scan and earlier matrix callback remain uncredited. The 85% goal is active.
