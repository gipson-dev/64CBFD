# Note 2581: Expiry-triggered map-burst emitter byte match

Date: 2026-11-19. Consumer baseline `b4858c1cacfe47190b05985109d3854d6c0d6719`;
tools baseline `d7e99a363b5551600f302afaa7a31bd58f13ec00`.

`func_1510558C` is restored from GLOBAL_ASM to semantic C and matches all
**175 words / 700 bytes**, retaining its **184-byte frame**. Fifty-seven
expected-word/relocation rows normalize temporary homes and register allocation;
118 raw words remain direct. There are no insertions or omissions. The existing
O2/g3 profile, ten owner neighbors, pools and original assembly are preserved.

Fresh production recount: **4,570 / 5,521 (82.77%)** total, **3,897 / 4,848
(80.38%)** Game, zero address drift and 951 different. Init 492/492 and Debugger
181/181 remain exact. Converted C: **5,521 / 6,048 (91.29%)**,
86.39% of bytes; Game **4,848 / 5,327 (91.01%)**,
85.78% of bytes. One ASM conversion row becomes C. The 85%
goal remains active: **123 more matches** at the current denominator, which
future ASM conversions can increase.

## Interface and actual dispatch

The routine spans VA 0x1510558C..0x15105848, ROM 0x132A3C..0x132CF8. Its local
void interface takes a typed `MapBurstRecord131F30 *`, describing an observed
432-byte object prefix and an emitter at +0x110. The first 0x110 bytes are opaque;
the body observes header bytes +1 and +0xC. The emitter models position +0x30,
direction +0x60, an 18-byte surface at +0x6C and a 32-bit tag at +0x88. The
actual caller additionally observes countdown +0x8C and signed callback +0x9C.
The types describe this prefix, not the complete unrecovered allocator object.

This callback belongs to **slot 5 of `D_8008FBD0`**, literal VA 0x8008FBE4 / ROM
0x2346A4. The complete original 58-word `func_151C455C` decrements the countdown,
checks expiry and flag bit 1, loads its signed selector and calls the table entry
with the original object pointer. It clears its own result after the callback,
supporting the void interface. `func_151C2734` supplies object +0x110 as the state
argument. The isolated target census finds one literal pointer and no direct
J/JAL sites; arbitrary computed calls are not excluded by that census.

An initial fixture had assumed the neighboring routine's dispatcher. Its literal
table check failed; the fixture was replaced with the actual expiry dispatcher
before any adoption or matching credit. Native checks call the target directly;
they do not claim a native reconstruction of the parent or its optional attached-
object callback.

## Recovered behavior and storage

The body obtains one float and two unsigned integer RNG results, then submits
`func_15102920` with rate `random * 25 + 15`, the narrowed byte
`first % 56 + 200`, and `second % 81 + 50`. It supplies the source surface,
position, tag and two header bytes through the complete ten-argument ABI.

It reloads the tag after this helper. Tag low bits equal to 9 select one strict
probability test and an optional point effect. Other tags select a point test
followed by an independent surface-burst test. Thresholds are read after their
RNG calls; helper mutations exercise tag, position, surface, direction, header,
ID/scale and parameter reloads. The original IDO object proves its actual access
and FP order. Portable native claims remain limited to the tested provider
contract and finite vectors; unspecified C argument evaluation is not a claim
of arbitrary helper or hardware scheduling parity.

The final helper receives an 88-byte packet with kind/mode, copied position,
negated direction, the 18-byte surface, five parameters, two bounds and three
tail parameters. Its two additional lists each have one element: an s32 effect
ID from `D_800A23A4` and a float scale from `D_800A23A8`. The consumer loads the
former as a word narrowed to a short and the latter as a float, indexed at a
four-byte stride. Aggregate list copies retain the original LW/SW representation.

The packet is at SP+0x58, ID list at SP+0x54 and scale list at SP+0x50 in both
streams. Raw initial RNG homes SP+0xB4/SP+0xB0 correspond to retail SP+0x44/SP+0x48;
raw cached position/surface homes SP+0x40/SP+0x3C correspond to retail SP+0x3C/SP+0x38.
Those paired moves and the verified register allocations account for
all 57 guarded differences. This is source-ABI equivalence with the documented
owned-frame contract, not literal raw private-memory/fault-PC identity.

## Qualification and production

- A paired symbolic execution checks all **six paths and all 175 words**.
  Ordered public reads, FP operands/control state, branch conditions and helper
  inputs agree. All **96 private helper-input bytes** (packet and two lists) are
  compared before helper effects. The whole 40-byte outgoing area may be
  clobbered. Saved ABI registers and final paired FCSR state agree. Valid public
  objects are disjoint from the owned frame; complete-record alignment is four.
  This also establishes the aligned addresses underlying the emitted LWL/LWR
  and SWL/SWR copies. Both self-relations pass; **122 effective model mutations**
  are rejected. This is not hardware exception/timing acceptance.
- **368 cases per guest stream** visit every word, preserve ordered public
  accesses and compare all 88 packet bytes, including seeded padding. Two
  explicit NaN-selection models cover nonfinite values separately. **55 fired
  public prefixes** agree. Full raw private fault state is not claimed.
- **31 cases per stream** execute the original 58-word expiry parent and actual
  slot-5 callback. Its optional attached-object callback remains outside scope.
- Actual SDK32 C builds at **O0/O2/O3 each pass 180 finite cases**, strict aliasing
  and UBSan. Eight compiled source controls fail at runtime. The mask control
  was corrected after GCC rejected an impossible comparison; a tag with bit 5
  set now makes the valid mask mutation effective. Native packet checks compare
  86 defined bytes; padding and nonfinite claims use the guest/symbolic scope.
- Both full-owner padders agree across all eleven functions and pools. The actual
  five-command mixed C/ASM Make route agrees. Twelve GNU links across six symbol
  rebases, stale-word/relocation guards and full-image corruption controls pass.
- Production Make passes in **354.362 seconds**. The target object
  and entire ELF equal the independent prediction: **zero changed image bytes,
  no exclusions**, all 6,051 function bodies/extents/addresses unchanged and
  189,088 protected data bytes across 720 owners unchanged. All **2,021 previous
  input hashes** are audited. Five pre-existing unrelated owner warnings remain.

Primary tools and a 979-file sibling overlay each pass eight fresh preinstall
tests; both configurations rerun two focused installed tests. Installed setup
repeats owner, Make, padding, full-image and positive relation gates, and the
guest test repeats all 368 cases. Other native/caller/rebase/negative-control
receipts are reused explicitly under unchanged fingerprints. `make tools-check`
passes. The real dirty sibling's HEAD, raw status and 343 dependency hashes are
preserved; its overlay uses 341 equal sibling files, 630 explicit primary
fallbacks, seven task files and one bootstrap. Tools commit precedes consumer.
No push or Claude call occurs. The identical retail image requires no host delta;
no host files or frozen Release artifacts are touched.

Graphify retains old IDs and links this manifest to the actual C definition;
the original ASM reference is historical. Its native update exited 1 after
refusing a smaller replacement and retained all 68,044 previous IDs. The scoped
six-file AST merge passed with zero lost IDs. Post-commit hook receipts are
retained; this is not a full-corpus extraction.
The root README changes only four aggregate rows. This note and five concise
indexes hold the recovery narrative.

## Next function

Continue `func_151058B4`, still GLOBAL_ASM in the same owner: VA
0x151058B4..0x15105BC8, ROM 0x132D64..0x133078, **197 words/frame 240**.
Only extent and prologue were inspected; no recovery or matching credit yet.

Reproduce with `python3 -m unittest tools.tests.test_game_map_burst_emitter_1510558c_match -v`
under the prepared WSL environment. Evidence is in
`conker/build/game-map-burst-emitter-1510558c-private/`.
