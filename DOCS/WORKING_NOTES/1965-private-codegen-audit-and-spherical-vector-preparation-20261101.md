# Private codegen audit and spherical-vector preparation

Verified 2026-11-01. **No new function is credited or installed in this audit.**
Production stays **4,034/5,507 (73.25%)**, Game **3,361/4,834 (69.53%)**, zero
canonical drift and1,473 different. Threshold4,131 still requires **97 matches**.
The latest code checkpoint is`b09015ec`, tools`cfa7d06`; this audit changes only
documentation and ignored experiment artifacts. The wider goal remains active.

## Actor transform/world-position query remains private

`func_1507E1D0` in`game_A9D90` has53 body words plus3 alignment words and a
56-byte frame. Its recovered four-pointer interface, transformed vertical
offset, interaction-state matrix selection and live fallback position stores
are hypotheses pending guest/native/caller qualification.

The best source remains52 words/frame56/22 differences. Matrix-before-vector
declaration order already recovers the original stack vector offsets. Further
explicit returns produce the same result. Goto and inverted-null forms leave
45/47 differences. Capturing the matrix earlier yields55 words/frame64/55.
Scale/zero locals yield52/frame64/35; a precomputed scaled height yields51/
frame64/52; integer-matrix spelling is ineffective at52/frame56/22.

Inspection corrects the earlier count-gap hypothesis: the unreachable duplicate
`li AT,30` is present in the selected source output too. The remaining word
deficit involves the outer branch/scheduling and shared return-address reload.
Retail restores RA separately on both paths, with one reload in the taken-path
branch delay slot. Do not insert the unreachable constant or force filler.
Saved artifacts:`game-actor-transform-position-1507E1D0-match/`.

## Descriptor tag updater remains private

`func_150174C0` in`game_447B0`,46 words/frame8, adjusts tag-2 halfwords in
24-byte records. Retail reloads the table base and current entry count after
a matching store, and reloads the outer bound after the inner loop. Its signed
outer comparisons differ from the current unsigned declaration's default use.
The current C's returned loop index also needs caller review; the known
`func_15017578` call ignores the result. A void interface is a private hypothesis.

Typed indexing with existing headers emits44 words/frame8/41 differences.
Signed bound casts do not resolve it. An explicit row cursor emits47/frame8/43;
byte addressing emits41/frame8/40. Void variants emit40..46 words without a
match. Separate byte-offset loops and do/while forms do not solve the gap.

Private header experiments with a pointer-typed table produce45/frame8/32;
changing the count signedness adds no improvement. Explicit inner-loop forms
are equivalent in codegen. A fully spelled reload/byte-offset model emits46
words/frame16/44, or48/frame16/40 with a narrowed adjustment. None is qualified.
No shared declaration was changed. The pointer-typed experiments are not directly
installable under current headers; array-entry bounds and live aliases need
qualification before choosing a public data view. Do not choose by length alone.
Saved artifacts:`game-descriptor-tag-adjust-150174C0-match/`.

## Spherical-vector source correction and closed spill pair

`func_1505A184` in`game_83300`, VA`0x1505A184..0x1505A250`,
ROM`0x87634..0x87700`, has51 words/frame48. Its existing interface is
`void(u16 yaw,f32 distance,f32 pitch,f32 *x,f32 *z,f32 *y)`.

Retail and the existing`game_981E0` caller's`&dx,&dz,&dy` order show that the
current C reverses its final X/Z stores. Retail also captures both final trig
results before either final store. The private recovered source preserves that
order, updates the distance formal in place, keeps the pitch and yaw-angle
lifetimes separate, and retains the unsigned yaw conversion.

Initial corrected locals emit56/57 words; sharing the pitch formal across all
four calls emits53 words with an extra saved FP register. Separating the pitch
and yaw lifetimes restores51 words. Declaration order then restores frame48.
Only two words differ: the yaw-angle SWC1/LWC1 pair at`0x8C/0x90` uses private
SP+0x24 instead of retail SP+0x20. Two derived expected-word guards move both
ends of that spill. They change neither opcode, register, binding, length nor
frame. No inserted/omitted words or dummy variables are used.

Selected raw SHA-256:
`7ff6c5cc98280c26984d073494d6f35fff40dbf5bbac54a2da154d83402ab237`.

The complete normalized payload and all eight bindings equal original assembled
ASM. All **88 raw/padded neighbors** and normalized pools remain unchanged.
Owner diagnostics remain **8->8**. The actual five-command Make recipe reproduces
the independently qualified object. All of this remains private preparation.

## Private entire-image and linker-map predictions

The private first link removes the220-byte overflow body at`0x15F00344`.
Five later private bodies move down220 bytes; only`func_150768DC` and
`func_150A7D00` trampolines retarget. All6,045 canonical addresses and6,050 other
bodies stay fixed. Executable inventory changes6,054->6,053 solely by deleting
the obsolete private implementation. Protected Game data remains189,088 bytes
across720 owners, unchanged.

The independent complete-ELF predictor also removes the now-unused
`game_83300.c.o` FILE symbol and its15-byte name. This is in addition to the
private-function symbol and its shared-name string. It reconstructs all string
offsets, two ROM definitions, headers and alignment. ROM cursor movement is224
bytes; ELF length falls284 bytes,3,256,616->3,256,332. Every byte matches, with
zero exclusions. Private ELF SHA-256:
`cded33da308db122019a82f17a72c6f77a3cda2274826ce9b593850acf7315d6`.

An independent complete-map prediction also matches:28 changed/deleted lines.
The private comparison maps nine shadow-object paths and one output filename
to production paths. Production has not been changed or checked against this
map yet. Removing the owner's last overflow contribution removes its map row.

## Required continuation before adoption

Evidence:`conker/build/game-spherical-vector-1505A184-match/`,1,071 frozen
focused inputs. `prepare_overflow_v7.py` and`qualify_map_v8.py` exited0.
The initial generator is historical: later FILE/string metadata refinements
are in`core-draft.py`; do not rerun it over those refinements.

Next qualify guest/native behavior, output/coefficient/incoming-home aliases,
all four call arguments and results, raw-C public state, and the private-spill
contract. Outputs into the callee's private frame cannot support a portable-C
equivalence claim for a private-slot normalization. Run original trig code:
the three-word cosine entry falls through into the73-word sine implementation;
it is not a library-wrapper provider. Existing
`game_oriented_motion_pair_oracle.py` and`game_rotation_matrix_leaf_oracle.py`
provide the76-word connected-code and coefficient reference model.

Enumerate and qualify the original callers and their six-argument X/Z/Y ABI.
Audit relative control flow in all five moved private bodies and dynamically
check both retargeted trampolines. Finish the canonical evidence set and its
fingerprint: `PREPARED_SHA` is still pending and the inherited EVIDENCE list
must be replaced before any public tools/tests are installed.

Then require focused checks in both tools copies, production Make, full sealed
input review, literal ELF/map equality, independent Windows recount, docs,
Graphify retention, tools-before-consumer commits and final seals. Until those
gates pass, keep this candidate uncredited and production unchanged. Original
assembly, older mirror edits, other private candidates and host Release remain
preserved. No push is requested or performed.
