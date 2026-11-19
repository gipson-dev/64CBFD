# Note 2577: Map-particle emitter guarded byte match

Date: 2026-11-19. Consumer baseline `63abe6032b5248317b395f6e37187eb58e213dd5`;
tools baseline `3964eed225d7c9585dd508b501ef2cb571cac2a5`.

`func_15104C44` is converted from GLOBAL_ASM to complete semantic C and is
**byte-exact across 237 words/948 bytes with the original 224-byte frame**.
Fifty-two expected-word guards restore the proven private initialization and
register schedule. There are no inserted/omitted instructions, artificial frame
padding, volatile variables, duplicate pools or compiler-profile changes.
Ten owner neighbors and all original pools/bindings are unchanged.

Fresh production recount is **4,567 / 5,518 (82.77%)**, Game **3,894 / 4,845
(80.37%)**, zero address drift and 951 different. Init492/492 and Debug181/181
remain exact. Converted C is **5,518 / 6,048 (91.24%)**,86.30% of bytes; Game
4,845/5,327 (90.95%),85.69% of bytes. One ASM conversion row becomes C.
**124 more matches** reach85% at the current denominator; later conversions
can grow that denominator. The full85% goal stays active/unfulfilled.

## Body, caller and recovered data

The body is VA0x15104C44..0x15104FF8, ROM0x1320F4..0x1324A8. Its correct
interface is `void func_15104C44(struct260 *record)`. It is callback slot 60
in `D_8008A4E8`, with the literal pointer at ROM0x22F098/VA0x8008A5D8.
The original dispatcher `func_15149264` does not consume the result. The old
zero-argument/signed-result placeholder declaration is removed locally.

The SDK header occupies0x24 bytes; the actual inline emitter begins at+0x28.
A recovered complete record type contains that header, the observed four-byte
gap and the inline72-byte emitter. The native fixture owns that complete type,
avoiding arithmetic beyond a small SDK-header subobject. Local surface/point/
packet types describe the actual offsets; shared SDK headers are unchanged.

A negative signed16-bit emitter timer skips the routine. Otherwise the current
32-bit frame ticks are subtracted with wrap followed by 16-bit narrowing. Expiry
unregisters `(func_1000EF40, eventID, 0)` and then continues to the gate test.
The source uses an explicit unsigned subtraction before narrowing, preventing
signed-overflow UB for extreme clock values while emitting identical words.

If the gate permits it, a float RNG value contributes
`(D_800A23AC + random * D_800A23B0) * D_800BE9A4` to the accumulator. The
existing rate words are0x3E49BA5F/0x3E99999A in the original rodata owner.
Only an accumulator strictly greater than 1 enters the loop. Each iteration
samples a radial position, probes its ground result, and optionally prepares
an80-byte particle-path descriptor from three direction samples. Unsigned RNG
remainders provide duration8..20, alpha100..255 and piece count5..7. The caller
passes the byte at record+C and category byte+1 to `func_15105CE0`, then reloads
and decrements the accumulator by 1. Equality at 1 does not emit another particle.
The descriptor reuses its copied surface-height field for the upper endpoint,
preserving the original single public height read and later private reload.

## Shape recovery and complete relation

The first full source had237 words/frame 224 but82 word differences and data
homes four bytes too high. Recovering the sampled-height reuse and declaring
the meaningful float temporary before aggregates obtains the exact original
homes and 52 differences: descriptor SP+8C, sampled XYZ SP+80/84/88, first
direction pair SP+78/7C and second pair SP+70/74. No padding is added.
Saved S0..S7/FP and F20/F22/F24/F26 retain their original lifetime. All five
pre-existing unrelated owner diagnostics remain identical after fixture-file
and shifted-line normalization; no diagnostic is suppressed or introduced.

The ordered relation interprets every instruction of both streams and checks a
loop fixed point:86 paired effect nodes,88 edges and 95 worklist steps. It
synchronizes32 public reads,3 public writes,23 FP operations/comparisons,
6 conditional boundaries,18 helper-call boundaries and 4 return boundaries.
FP transitions and FCSR updates are uninterpreted functions of the same ordered
operands/state, rather than assuming commutative NaN or exception behavior.
All stable edges are checked again, and 31 effective mutations include every
FP operand position, saved F26, timer/channel fields, descriptor address,
unsigned remainder, duration, a private store and the final consumer target.

The frame is partitioned by the recovered typed cells. Private accesses can
stutter while public accesses and FP operations stay ordered. Crucially, **all
private descriptor/vector cells are compared before every helper**; only then
may the helper produce arbitrary coupled writes. Equal fresh outputs cannot
hide an earlier discrepancy. The relation assumes valid C object lifetimes,
public allocations distinct from the owned frame and preservation of the
caller's saved frame. It is a normal source-ABI relation, not literal raw
fault-PC/private-prefix identity. An additional stable-edge audit verifies
equal saved GPR/FPR, FCSR and actual return-continuation inputs at all 18 calls.

## Independent execution and integration gates

Primary tools and a954-file sibling overlay each pass eight fresh integration
tests. The real independently dirty tools checkout is not overwritten.

- 608 cases per original/raw guest stream visit all 237 words, checking full
 public memory, call order/arguments, ABI preservation and all 80 copied bytes,
 including seeded padding. Cases include signed timer wrapping, exact thresholds,
 misses/hits, two NaN-selection models and helper mutations of input/state.
 Eight effective instruction controls fail.
- SDK32 native checks run 608 cases each at O0/O2/O3, with strict aliasing and
 UBSan. Each profile includes304 calls through the actual C dispatcher and
 nine effective source controls. Finite results and 73 defined descriptor bytes
 are exact. Forty-four nonfinite accumulator-result cases check NaN category;
 native C NaN payload and hardware FCSR behavior are not claimed.
- The original 45-word dispatcher executes61 scenarios per stream through the
 real registry slot and callback. Its selected path visits25 parent words;
 complete cleanup/other-selector qualification is not claimed. The original
 particle consumer's0x50-byte memcpy confirms descriptor size; its full235-word
 construction behavior remains outside this callback recovery.
- Both padding routes agree for all 11 owner functions and pools. The independent
 route uses original ROM spans and authoritative layout, since this mixed owner
 has no full `asm/131F30.s`. The actual five-command mixed Make recipe retains
 O2/g3 and the five old warnings, producing the predicted complete object.
 Twelve GNU links across six rebases agree. Stale expected words/relocations
 fail in both padders; full-image corruption controls fail without exclusions.

Installed primary/overlay checks freshly rerun full owner/Make/image/relation
qualification and the 608 guest cases. Unchanged native/relocation receipts are
reused only after source/profile/import fingerprints agree. Shared tools checks
pass. Normal production Make exits0; all 1979 frozen inputs are audited.
The entire ELF and every one of 6051 function bodies/addresses remain identical
to the frozen prediction, with **zero changed bytes and zero exclusions**.
Protected data stays exact across 189088 bytes/720 owners. ELF SHA-256 remains
`d3eeddd84c1cd3c6c0877467dfdf37015677dc0a81885ea7f5ed6d528b2f352d`.

The real sibling tools HEAD, raw status and 343 dependency hashes are preserved.
Tools commit precedes the consumer commit; no push. A bounded host-sibling
inspection found the retained `cd64_out` callback stub, not active-host runtime
acceptance evidence. This conversion changes no retail behavior to transfer;
no host files/builds or frozen Release artifacts change. Zero Claude calls.

Graphify's normal update refuses a shrinking corpus. A scoped eight-file AST
merge retains prior node IDs and links the matching manifest to the real C
definition. Historical prior-ASM references remain historical. Hook writers are
observed terminal before heading-alias retention/final sealing. This is not
full-corpus re-extraction. Root README changes only four aggregate status rows;
this note and five concise indexes contain the recovery narrative.

## Next function

Continue with `func_15104FF8`, still GLOBAL_ASM in the same owner:
VA0x15104FF8..0x151050B0, ROM0x1324A8,46 words/frame 72. Its prologue saves A1/A2
and narrows the third argument to a byte. Only the prologue/extent is inspected;
qualify its complete body, caller, argument types and owner neighbors first.
No recovery or matching credit is claimed for it here.

Reproduce: `python3 -m unittest
tools.tests.test_game_map_particle_emitter_15104c44_match -v` under prepared WSL.
Ignored evidence: `conker/build/game-map-particle-emitter-15104c44-match-private/`.
