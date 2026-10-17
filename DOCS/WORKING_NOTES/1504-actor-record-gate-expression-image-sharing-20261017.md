# Actor Record Gate Expression Image Sharing

Verified 2026-10-17. Consumer predecessor4e7e37cb; tools predecessor40a1e62.
Both active checkouts began clean. The preceding turn was progress: it banked
the normal stage captures and rejected prolog-only control. This turn narrows
the opening-load investigation with a fresh normal compiler observation. No
production restoration or matching credit is claimed.

## Target And Question

Continue func_150F2A60, generated_11FF10, asm/11FF10.s,
VA150F2A60..150F2C8C /ROM11FF10..12013C,139 words/frame0x40.
[Note1503](1503-actor-record-gate-compiler-stages-and-prolog-control-20261017.md)
proved that two frontend D_800CC5EC loads become one optimized load. Determine
whether their common expression identity is already constructed before the
later patchvectors/copypropagate/codemotion passes.

The new helper reuses the unchanged frontend transport, normal full-owner
adapter, decoder and complete-object validator. This is an ordinary O2/g3
compile with read-only breakpoints/finish observations in newly owned children.
There is no diagnostic optimizer option, numeric timing interpretation,
compiler decision/guest-memory patch or production flag/type change.

## Fired Native Observations

Prepared cc/cfe/uopt/ugen fingerprints are checked before native addresses are
used and again by the existing validator. For the same fingerprint-locked
UOPT, observe readnxtinst0x485A60 and exprimage0x458080. At procedure760,
select only the two static block747 address loads with four-byte length and
zero offset. Use the current procedure and captured descriptor-defined input
fields; do not interpret unused wire words as operands.

The qualified event order is:

1. First selected read returns a load-node identity with no image association.
2. exprimage receives that node, returns a nonzero image and stores that same
   identity at node+0x14.
3. Second selected read returns a **different** load node, initially unimaged.
4. exprimage receives the second node and returns **the first node's image**,
   again storing it at node+0x14. Both load nodes have the same address operand.
5. Both associations are still present at the entries to patchvectors0x4522A0,
   copypropagate0x468FB0, codemotion0x47BD10 and reemit0x448A80, in that order.

In the fresh run, node identities269150880 and269148096 both associate with
image269150064. The image's raw tag word is0x00940000 and its representative
field contains the first node. The earlier unchanged mode5/6 listing identifies
the initial load as expression0 /identity148|0; that listing is reused, not a
fresh allocation-mode capture. Other raw node/image fields are retained but
not assigned invented meanings.

The normal frontend/optimized wire streams still have two/one opening loads.
Thus **the shared image association predates all four observed global-pass
entries**. It is not first introduced by copypropagate. This does not establish
which later decision eliminates the actual instruction, prove that shared
image identity alone forces elimination, or recover the historical source
qualifiers/compiler profile. Those remain separate questions.

## Qualification And Rejections

Three fresh tests pass in7.394s:

- One complete normal capture checks fired read/image/stage probes, the scoped
  two-node/common-image relationship, descriptor-bound loads and stage order.
  All CFE/UOPT/UGEN/AS1 children and driver exit0, with final null inferior.
- Normal and captured objects have identical text, functions, relocations and
  data/literal pools. Target raw SHA remains
  `28c65059860b7a8f40b59166beecbfbe9fecf1c6b7b392a130d9a74d42dcf125`.
-33 effective counterexamples reject wrong procedure/compiler, duplicate or
  missing nodes/events, changed load type/width, image/representative changes,
  misordered stages, misplaced events and incomplete cleanup. Five additional
  child/driver exit-code controls reject incomplete lifecycles.
- All253 protected entries /233 paths remain unchanged. The existing semantic,
  native32 and fault-prefix receipts from Notes1502/1503 are reused, not rerun
  or described as new full-private qualification.

An initial scratch prototype failed by retaining UOPT-native breakpoints into
the next compiler image; its incomplete run is not accepted evidence. The
qualified helper deletes all six probes on **UOPT exit**, checks zero pending
finish observations and requires removal before UGEN consumes the output.
The final suite also checks the actual interleaved read/image event order.

The donor file in Another Source/CBFD-Recompiled/conker/conker/src/game/
game_11FF10.c remains explicitly non-matching. Its gate uses a word access at
0x120, unlike retail's byte access. It is not installed as an exact donor.
Scratch profile attempts rejected by asm_processor are not compiler results
and do not establish any original retail profile.

## Bank And Resume

Tools **f983786** banks only the new experiment/test pair before consumer
documentation/pin. Both tools copies pass12 shared tests and smoke checks;
four ASCII/AST parses and two exact task-file pairs pass. Preserve all1,120
pre-existing mirror hashes,1,122 dirty paths and mirror HEADddbdd16b. No mirror
commit/reset, push, new Claude call, host operation or frozen Release action.
Finish the consumer commit's owned Graphify rebuild before closing.

Production ELF remains
`f56e3591c3c86189f630e4b8d599d8cfd7920165766e0c309a310970cd12ba6a`.
Production sources/guards/data/CSV and root README remain unchanged. Unchanged
matching totals are Game2,962/4,828 (61.35%), total3,635/5,501 (66.08%),
1,866 different and zero drift. No production rebuild or new match is claimed.

- [x] Observe two distinct gate-load nodes acquiring the same expression image
  before patchvectors/copypropagate/codemotion, with complete normal identity.
- [x] Pass focused corruption/lifecycle controls and preserve both tools copies.
- [ ] Continue this same func_150F2A60 at **exprimage's common-image lookup and
  the later reuse decision**, using the exact nodes/address/type/width as the
  witness. Do not repeat copypropagate-entry or equivalent loop-bound screens.
- [ ] Recover the actor-address rematerialization and all139 words/full private
  state before installation. Keep the137-word baseline and worse135-word
  prolog control rejected; both fade lifetime gaps and wider Game remain open.

```sh
python3 -m tools.experiments.game_actor_record_gate_expression_image
python3 -m unittest tools.tests.test_game_actor_record_gate_expression_image -v
make tools-check
```
