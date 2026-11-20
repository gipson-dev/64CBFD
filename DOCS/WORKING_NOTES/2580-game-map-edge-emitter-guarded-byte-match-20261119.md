# Note 2580: Map-edge emitter guarded byte match

Date: 2026-11-19. Consumer baseline `efddd0755200f9e18aaf51155cd0345ee114063d`;
tools baseline `218288c6214eb22380bc249b67284b796c7bddd1`.

`func_151050B0` is converted from GLOBAL_ASM to complete semantic C and matches
all **279 words / 1,116 bytes**, with the original **208-byte frame**. There
are 43 guard rows: 42 source-word/binding replacements and four inserted
schedule words, with no omissions. 233 of the 275 compiled words remain direct.
No volatility, artificial padding, additional pools or profile changes occur.
All ten owner neighbors, their bindings and all pools remain unchanged.

Production recount: **4,569 / 5,520 (82.77%)** total, **3,896 / 4,847 (80.38%)**
Game, zero address drift and 951 different. Init 492/492 and Debugger 181/181
remain exact. Converted C is **5,520 / 6,048 (91.27%)**,
86.36% of bytes; Game is 4,847/5,327 (90.99%),
85.75% of bytes. One ASM conversion row becomes C.
**123 more matches** reach 85% at the current denominator; subsequent ASM
conversions can increase that denominator. The full 85% goal remains active.

## Recovered body and concrete layout

[Note 2579](2579-game-map-edge-emitter-recovery-and-frame-20261119.md) records
the complete semantic recovery, typed 152-byte outer record, 112-byte emitter,
48-byte descriptor, original slot 61 dispatcher and RNG-domain evidence. The
interface is `void func_151050B0(struct260 *record)`, VA 0x151050B0..0x1510550C,
ROM 0x132560..0x1329BC. The local false signed-result placeholder is removed.

The installed C retains timer/state updates and expiry dispatches, explicit
initial RNG sequencing, cached width, strict accumulator thresholds, two
bounded distinct index selections, ordered endpoint interpolation and the
complete helper ABI. Data homes remain secondPoint at SP+0x84, firstPoint at SP+0x90 and
packet at SP+0x9C. All 48 copied guest bytes, including seeded padding, match.

The raw body has 275 words; the guarded body has 279. The four additional retail
operation roles are the saved-F28 store/load and a second 1.0 materialization/
FP transfer. Physical insertion slots are target indices 11, 91, 94 and 268, with
words F7BC0040, 3C013F80, 4481C000 and D7BC0040. Packing moves an existing 2.0 FP
transfer into one inserted schedule slot while another guarded slot carries
the duplicate 1.0 transfer. These are meaningful save/constant/schedule words,
not padding. The opcode census only constrains this rewrite; the complete
effect relation below is required to certify it.

All 43 rows check the actual compiled words and expected relocation lists.
Their replacements/insertions produce the original raw 279-word object and
complete relocation map. The entire original ASM remains intact as evidence.
The owner keeps its existing O2/g3 profile and five old unrelated warnings;
diagnostic comparison normalizes only fixture filenames and shifted lines.

## Complete ordered CFG and FCSR relation

The paired relation reaches a fixed point with 113 effect nodes, 122 edges and
160 worklist steps. Incoming states meet by intersection of modular affine
equalities; every final edge is independently rechecked. It synchronizes 30
public reads, 5 public writes, 13 conditional boundaries, 11 call boundaries,
32 FP boundaries, 6 FCSR reads, 12 FCSR writes and 4 return boundaries.

FP and FCSR transitions are arbitrary deterministic functions of the same
ordered operands and control/condition state. No floating-point commutation,
NaN-payload rule or particular exception implementation is assumed. FCSR writes
update both the control register and its condition-bit view; SDK R4300.h
identifies FPCSR_C as bit 23. The return relation compares both views too.

The original 276 and raw 272 structurally reachable words are all visited,
including unsigned conversion fallback branches absent from the bounded RNG
tests. Three unreachable word pairs are separately identified by an explicit
delay-slot CFG walk and pinned literally: original offsets 0x60/0x248/0x300 versus
raw 0x5C/0x23C/0x2F4, words 8E590000/44105000/44028000. Every original/raw word is
therefore accounted for; unreachable words are retained, not deleted.

The complete 72-byte private helper-input region (both vectors and all 48
descriptor bytes) is compared **before every helper**. Only then may a paired
helper apply arbitrary coupled data writes and volatile results. Its full
32-byte outgoing argument area may be clobbered independently. Equal helper
outputs cannot repair unequal inputs. Saved-frame/entry ghosts prove each
stream's ABI preservation, including the different saved FP roles.

This relation assumes valid public objects disjoint from the owned frame and
helpers preserving the caller's saved frame. It proves the source ABI and
ordered effects, not literal raw private fault-PC/return-continuation identity
or hardware timing. The normalized installed words are literally retail.
Eighty-one effective mutations cover every FP operand position, FCSR read/write
registers, timer/source/descriptor/channel/consumer fields, saved/restored F28
and all three unreachable literals. Both streams also pass self-relation checks.

## Integration, production and retained scope

Primary tools and an isolated 972-file sibling overlay each pass eight fresh
tests. Four semantic checks from recovery are reused as test code; the old
"private layout still open" boundary is replaced by actual matching/installed/
image gates. The independently dirty sibling's HEAD, raw status and 343
dependency hashes are preserved. Overlay composition: 341 byte-equal sibling
files, 626 explicit primary fallbacks, four task files and one bootstrap.

- 684 cases per original/raw guest stream preserve all public bytes, call
  arguments, ordered accesses, ABI registers and all 48 copied descriptor bytes.
  Two explicit NaN-selection models and helper mutations remain covered.
- 158 fired public prefixes agree. Thirty-five scenarios per stream execute
  the original 45-word dispatcher through actual registry slot 61. Complete
  cleanup/other-selector and full child-constructor behavior remain separate.
- Actual SDK32 native builds at O0/O2/O3 each pass 496 finite cases, 248 calls
  through the actual C dispatcher, strict aliasing and UBSan. Eight compiled
  source controls fail. Each profile exhausts all 65,536 masked RNG values and
  checks valid distinct 0..3 indices. Native packet comparisons cover 43 defined
  bytes; nonfinite/padding/control-state claims remain scoped as in Note 2579.
- Both object padders agree on all eleven functions and pools. The actual
  five-command mixed C/ASM Make route reproduces the padded object under the
  existing profile. Twelve independent GNU links across six symbol rebases
  match; stale word/relocation controls fail both padders.
- The strict full-image prediction equals the entire frozen ELF with zero
  exclusions. Corruption controls fail. Production Make and a fresh recount
  confirm identical objects/image. Production Make completed in 369.369 seconds.
  All 6,051 function bodies/extents/addresses
  and 189,088 protected data bytes across 720 owners remain unchanged.

All 2,008 predecessor input hashes are audited. After installation, both tools
configurations rerun two focused tests; setup repeats owner/Make/padding/image
and full positive relation qualification, and the guest test repeats 684 cases.
Native/caller/rebase/negative-control receipts are reused explicitly under exact
source/tool/input fingerprints, not described as freshly rerun post-install.
`make tools-check` passes. Tools commit precedes consumer source/docs/gitlink;
no push or Claude calls occur. No host files, builds or frozen Release change.
The retail ELF has no behavior delta requiring a host transfer; retained
generated stubs are not active-host gameplay acceptance evidence.

Graphify retains old IDs and links this matching manifest to the actual C
definition. The original ASM reference is explicitly historical. The native
update exited 1 after refusing a smaller replacement; all 67,996 existing node
IDs were retained. The scoped four-file AST merge passed with zero lost IDs.
Post-commit writer/alias receipts are retained. This is a scoped AST refresh,
not a full-corpus semantic extraction. Root README changes only
four aggregate rows. This note and five short indexes carry the narrative.

## Next function

Continue with `func_1510558C`, still GLOBAL_ASM in the same owner: VA
0x1510558C..0x15105848, ROM 0x132A3C..0x132CF8, 175 words/frame 184. Only its
extent/prologue were inspected. Recover its whole body/types/caller/FP order
before another adoption; no candidate or credit is claimed here.

Reproduce under prepared WSL:
`python3 -m unittest tools.tests.test_game_map_edge_emitter_151050b0_match -v`.
The older recovery-only suite is historical after adoption. Evidence is in
`conker/build/game-map-edge-emitter-151050b0-match-private/`.
