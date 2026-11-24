# Ring emission callback byte match - 2026-11-24

`func_150C99B4` is recovered as semantic C in `conker/src/game/generated_F5800.c`.
The complete 138-word / 552-byte body is byte-exact after one expected-word guard
at offset 0x1DC. The compiler emits the retail 168-byte frame, argument homes,
packet at SP+0x38, pitch at SP+0x32 and saved flag lifetime at SP+0x28. All 137 other
raw instruction words and every relocation binding already match. No inserted
or omitted instruction, profile change, copied assembly body or Makefile edit.

Production recount: **4,660 / 5,528 (84.30%)** total, Game **3,987 / 4,855
(82.12%)**, Init **492 / 492** and Debugger **181 / 181**, zero drift and 868 different.
**39 more functions are required for 85%**. Only this callback gains one match.

Retail VA 150C99B4..150C9BDC, ROM F6E64..F708C. The callback returns void and takes
the ring record, a vertex pointer, byte angle and two unused float payloads.
The direction helper uses its existing s16/s16/f32/vertex* interface; submission
uses the existing void*/u8/s32/u8/s32 signature and its returned pointer is ignored.
The proper RNG prototypes and explicit unsigned remainders preserve all widths.

The callback builds a randomized kind 0x26 particle descriptor. Five ordered
integer RNG draws choose lifetime, a byte channel, two flags and signed pitch;
three ordered float RNG draws choose sizes, acceleration and direction speed.
The point is copied only after the first float draw. The speed calculation reads
the current owner scale after the final float draw; slot and context bytes are
reloaded after the direction helper. Provider-induced mutations are retained
at those exact boundaries. The unused incoming sine/cosine payloads stay unused.

The original downstream `func_15130280` copies exactly 0x70 bytes. Its complete
61-word body is independently checked against pristine ROM and the frozen ELF,
so the packet extent and 12-byte reserved tail are verified ABI storage rather
than artificial frame padding. The packet also retains its unwritten interior
word at 0x5C. Source fields and local variables reproduce the observed layout.

The lone guard swaps the operands of the same floating multiply:
`46008482` becomes `46100482`. Both operands, destination and dataflow are the
same. The complete remaining function emits directly, including both RNG flag
branches and all helper calls. Every old guard byte remains an exact prefix.
All 18 raw and padded owner neighbors are unchanged, as are compact and padded
pools. The existing four-command Make recipe and updater pool checker are reused
unchanged; that checker also passes against the newly compiled complete owner.

The independent image reference uses frozen old C plus the original target
assembly. Actual shadow Make and production Make equal its full predicted ELF,
with 467 changed bytes and zero exclusions. Named metadata and strings are
accounted for independently. All 189,088 protected Game data bytes, 720 data
owners, conversion rows and other frozen inputs remain unchanged.

Four instruction streams agree with pristine retail. Guest qualification runs
780 cases per stream, all 138 words and all 256 angles, covering all four rounding
modes, unsigned remainder boundaries, both outcomes of each flag branch, mutable
inputs/constants, ignored payloads, submission outcomes and guest-only overlaps.
There are 236 complete access-fault quads with equal register, memory, call and
FP state. Full 112-byte sparse packet snapshots preserve the original unwritten
stack contents at every call boundary. These are instruction-level observations,
not portable C guarantees for indeterminate bytes or invalid object overlaps.

SDK32 native O0/O2/O3 each pass 512 legal backed, nonoverlapping cases with strict
aliasing and UBSan. Ordered helper arguments, owner/point/global state and only
initialized packet bytes at the direction/submission boundaries are compared
using canonical dual32 digests. Reserved holes and the still-unwritten direction
output are excluded from native observations. Eleven effective source controls
exit 42 from comparison; no signal or UBSan trap counts as a passing control.
These finite cases are not an all-input equivalence or gameplay claim.

A complete aligned pristine-ROM census finds no direct JALs and one pointer at
ROM 22D318 / VA 80088858. The original ring-updater callback window executes 192
cases across four streams, qualifying all five o32 arguments, byte-angle masking,
callee-saved state and two stack alignments. A wrong angle mask changes valid
calls and output. The complete parent and helper internals remain contracted,
with no added matching credit. The consumer's 61-word check establishes its
descriptor-copy contract, not a fresh helper conversion.

Boundary controls reject both corrupted copies of the guard word, expose 274
unguarded corruptions, pin 18 bindings and reject both oversized slots. Sixteen
GNU links and 32 guest rebases cover HI16 carry, LO16 sign and address regions.
Eighteen retained-pool corruption controls also pass against the new owner.

| Qualification | Elapsed | Coverage |
| --- | ---: | --- |
| preinstall-primary | 90.108s | 5 fresh / 0 reused |
| preinstall-sibling | 91.321s | 5 fresh / 0 reused |
| installed-primary | 83.35s | 5 fresh / 0 reused |
| installed-sibling | 93.544s | 5 fresh / 0 reused |

Shared `make tools-check` passes. Both tools copies use final source, guard and
data fingerprints. The second copy is an isolated dependency-verified overlay;
the separately dirty tools checkout stays untouched. Prior neighbor semantic
receipts are reused with unchanged body/ABI/relocation/pool/guard inputs and are
not called fresh neighbor testing. This routine uses zero Claude calls.

Consumer baseline: `c0b2b4fc520d8711e688b32ff27fb7214f1e46e1`.
Tools qualification commit: `e45a005114107355de3f319846d52b9dbd8b0bc5`.
Production ELF SHA256: `2ac2f15441bd908c10613cb41588d0d48281febf16076f2055063f955d9e0969`.
Padded owner SHA256: `f80e6b9c0f1ce73a0e649a7310d750500c66c2e11e8d7e08aa1afe4276cd8f82`.
Initial freeze: 3518 inputs / 2110 copies. Private receipts are in
`conker/build/game-ring-emitter-150c99b4-private`.

Graphify was queried first. Native update and a scoped AST merge retain old
IDs and qualification; observe actual hook producers terminal before the final
merge and bank. No full-corpus extraction, host/Release change or push is claimed.
Next: the 122-word `func_150C9BDC` ring update callback. The 85% goal remains active.
