# Note 2578: Map-particle sound activation byte match

Date: 2026-11-19. Consumer baseline `26fd1c76294d22658754ef7beb7acf401171bab3`;
tools baseline `960b6f9a893c7b7f430c3018b29b369953c28c1a`. The wider 85% matching goal remains active.

`func_15104FF8` now has complete semantic C and matches all **46 words / 184
bytes / original 72-byte frame**. Four expected-word guards relocate two paired
private spill cells; the other 42 words and every relocation emit directly.
There are no insertions, omissions, volatile declarations, artificial frame
padding, additional pools or compiler-profile changes. All ten owner neighbors
and pools remain unchanged, with the same five unrelated compiler warnings.

Production recount: **4,568 / 5,519 (82.77%)** total, **3,895 / 4,846 (80.38%)**
Game, zero address drift and 951 different. Init 492/492 and Debugger 181/181
stay exact. Converted C is **5,519 / 6,048 (91.25%)**,
86.31% of bytes; Game is 4,846/5,327 (90.97%),
85.69% of bytes. This converts one original ASM row to C.
**124 more matches** reach 85% at the current denominator; subsequent ASM
conversions can increase that denominator.

## Recovery and interface

The body is VA 0x15104FF8..0x151050B0, ROM 0x1324A8..0x132560. Its interface is
`void func_15104FF8(struct260 *record, s32 argument, u8 command)`; the middle
argument is unused. The old zero-argument/signed-result placeholder is removed
locally. Callback registry `D_8008A8D8` slot 45 contains the original pointer at
VA 0x8008A98C / ROM 0x22F44C. The original 23-word dispatcher `func_15149434`
passes all three arguments and does not consume a return value.

For command 0x38 only, the callback reads the inline source pointer at record
+0x28 and tests its state byte at +0x14 for exact equality to 1. It stores 300
to the signed 16-bit timer at record +0x30, then stops the registered sound with
`func_1000FD38(func_1000EF40, source, 0)`. It reloads the source pointer after
that helper, reads signed 16-bit XYZ at source +0/+2/+4, and submits positional
sound 0x236 with arguments `(XYZ, 0x4000, 1500, 1000, func_1000EF40, source,
0, 8, 0)` to `func_1000FA64`. It ignores the returned sound handle.

Local named source/state/record views describe the observed pointer and inline
layout. The complete outer record contains the SDK 36-byte header, observed
four-byte gap and 12-byte state prefix. Native fixtures own this complete type,
so the code does not step beyond a standalone SDK-header subobject. Shared SDK
headers and the preceding emitter routine are unchanged.

An initial integer view of the source field emitted 45 words. Recovering its
pointer type recovers all 46 words and the original 72-byte frame. Meaningful
source-lifetime/callback-local probes are retained privately; none is installed.
The accepted source differs at offsets 0x48/0x4C/0x58/0x5C only: the callback
spill moves SP+0x38 -> SP+0x3C and the emitter spill SP+0x3C -> SP+0x40.

## Qualification and limits

The private-cell relation checks all 46 instruction positions. Only the two
paired stores/loads differ under that injective four-byte cell renaming.
The cells are disjoint from arguments, saved RA and incoming homes; their
addresses never escape. Every public access, branch, delay slot, helper call,
argument and saved-register operation is otherwise identical. This proves the
source ABI relation for valid public allocations disjoint from the owned frame,
with helpers preserving caller-private cells. Raw private fault-address identity
is not claimed. Installed normalized words are literally the original words.
Eleven effective relation mutations reject changes outside this closed mapping.

Primary tools and an isolated 962-file sibling overlay each pass seven fresh
tests. The real independently dirty sibling checkout and its dependency hashes
are preserved. The overlay uses 341 byte-equal sibling files, 614 explicit
primary fallbacks, six task files and an empty package bootstrap.

- 2,196 cases per original/raw guest stream cover every command byte, four
  source states, both stack phases, signed coordinates, helper mutations,
  three public-memory alias layouts and all 46 words. Public bytes, ordered
  public accesses, call arguments and preserved ABI registers agree. A rejected
  command also works with the source-pointer bytes absent.
- 23 fired public-access prefixes agree across both streams. These describe
  the emitted guest instructions, not portable C fault or hardware semantics.
- Five scenarios per stream execute the original 23-word dispatcher through
  slot 45; 20 parent words are visited. Other slots and all dispatcher paths
  are not claimed qualified.
- Native actual SDK32 builds at O0/O2/O3 each pass 49,152 cases, including
  24,576 calls through the actual C dispatcher and eight effective source
  controls. Strict aliasing and UBSan are enabled. All source/record bytes and
  surrounding sentinels are checked. Guest overlapping views are separate from
  these native typed-allocation tests. Eight effective guest controls also pass.
- Both object padders agree on all eleven functions and pools. The actual
  five-command mixed C/ASM Make route agrees under the existing O2/g3 profile.
  Twelve GNU links across six symbol rebases match; stale expected-word and
  relocation controls fail both padders.
- The strict image prediction is byte-for-byte equal to the frozen full ELF,
  with zero exclusions. Corruption controls fail. All 6,051 function bodies,
  extents and addresses and 189,088 protected data bytes across 720 owners stay
  fixed. Production Make and a fresh linked recount confirm this result.

An early guest fixture placed a source at the interpreter stack address; its
incoming argument initialization overwrote a coordinate. Moving that synthetic
source to a disjoint allocation fixed the test; production C was unchanged.

After installation, both tools configurations rerun two focused checks, whose
setup repeats owner/Make/padding/image qualification and whose guest test checks
all 2,196 cases again. Native/caller/rebase receipts are explicitly reused under
unchanged source/tool/input fingerprints, not described as freshly rerun then.
The shared `make tools-check` passes. Tools are committed before the consumer
source/docs/gitlink. No push, Claude calls or host/Release changes occur.

Graphify uses a scoped five-file AST merge with old-node retention and a link
from this manifest to the actual installed C definition. Native update results
are retained separately; this is not full-corpus semantic re-extraction. The
post-commit writer is observed terminal before final graph/handoff sealing.
Root README changes only four aggregate rows; narratives live in this note and
five concise index entries. The unchanged retail ELF requires no host transfer;
no host runtime or gameplay acceptance is inferred.

## Next function

Continue with `func_151050B0`, still GLOBAL_ASM in this owner: VA
0x151050B0..0x1510550C, ROM 0x132560, 279 words / frame 208. Its prologue and
tail identify an emitter timer/source gate; the complete body, source types,
FP operation order and caller still need qualification. No credit is claimed.

Reproduce under prepared WSL:
`python3 -m unittest tools.tests.test_game_map_particle_sound_15104ff8_match -v`.
Private evidence: `conker/build/game-map-particle-sound-15104ff8-private/`.
