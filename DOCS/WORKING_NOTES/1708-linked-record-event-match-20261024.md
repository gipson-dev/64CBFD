# Linked-Record Event Match

Verified 2026-10-24. Recover `func_150F887C` in
[generated_124920.c](../../conker/src/game/generated_124920.c), replacing its
zero-return placeholder with a complete event callback. All 44 retail words
match with nine checked compiler-layout rows and two derived return-load
copies. This is guarded semantic C, not compiler-only matching.

## ABI And Layout

VA `150F887C..150F892C`, ROM `125D2C..125DDC`, 176 bytes, no alignment
tail. The complete C body emits 42 words under normal O2/g3, frame 24,
with one helper binding at raw +0x90 / fitted +0x98.

Use the actual callback signature `void(struct260 *, s32, u8)`: owner,
packet address word and byte command. Do not replace the word-shaped
argument with an incompatible pointer-typed callback signature. The local
packet view converts that address explicitly. Preserve the complete incoming
A2 word home before byte narrowing; private homes are guest-only evidence.

The local linked-record view starts at owner+0x28:

| Relative Offset | Observed Use |
| --- | --- |
| 0 | signed word compared with packet word zero |
| 4 | tag byte compared with packet byte four |
| 8 | selected-index byte, published as seven |
| 0xC..0x28 | eight record pointers |

Command 0x42 compares the tag bytes. On equality, load each of the first
seven pointers and write one to record+0x6E; then reload the eighth pointer,
write zero to its +0x6E and publish selected index seven. Preserve the byte
loop counter and late pointer reads. Pointers may alias later pointer bytes;
preloading the eighth pointer changes observable results and is rejected.

Command 0x3F compares packet word zero with owner+0x28 and calls
`func_150F892C(owner)` only on equality. Other command bytes dereference
neither input. Do not add NULL guards to the selected commands; retain their
actual emitted fault boundaries. The large callee stays unrecovered and
uncredited, with its existing legacy declaration retained. Its original
entry saves the owner in S3 and overwrites A1/A2 before its first branch;
the callback's observed owner handoff is bounded, not a complete callee
recovery or inferred return contract.

## Registration And Caller

An aligned scan of all 616,822 words in the frozen matching reference
conker/conker.us.bin finds no direct JAL sites and a single literal
registration at slot 56 of the 74-entry
`D_8008A8D8` table at VA `8008A9B8` / ROM `22F478`, in
[22EF80.rodata.s](../../conker/asm/data/22EF80.rodata.s).
Verify that slot against both retail and the predecessor ELF.

The unchanged original 23-word `func_15149434` dispatcher in
[game_1765E0.c](../../conker/src/game/done/game_1765E0.c) reads the unsigned
header selector, falls back to index zero for >=74, gates NULL entries and
forwards the canonical word/byte arguments. Execute its complete entry to
return in 2,048 cases over all 256 selector bytes, both selected commands,
NULL/present handlers and optional index-zero routing. Visit every original
dispatcher word. Controlled entries qualify lookup/call behavior, not every
unrelated handler in the production table. Caller source/object are unchanged.

## Derived Normalization

Fifty-six source spellings screen control flow, loop form, comparison order
and pointer views. None supplies a directly exact 44-word source. Keep the
complete defined void callback rather than introducing padding or a guessed
integer-return ABI for a better shape.

The normalizer validates every raw word by hash, the sole symbolic binding
and the frame/save/return pattern. Derive these changes from that body:

- Permute raw setup positions 9..14 as 12,9,10,11,14,13. Compute the tag
  address through the existing owner+0x28 group value; subtract that offset
  from the original +0x2C load. Close the tag/packet temporary-register swap.
  The order of the two memory reads remains unchanged.
- Change the mismatch BNE to its likely form. Copy the existing SP+0x14
  RA restore into its delay slot and target the following stack-pop label,
  replacing the shared-return edge without a second dynamic restore.
- Move the selected-index store before its unconditional return branch.
  Copy the same existing RA restore into that branch delay slot and target
  the stack-pop label. The restore remains after the last potentially
  aliased store.
- Derive all six relative branch distances from the instruction map.
  Carry the sole R_MIPS_26 binding from raw +0x90 to fitted +0x98.
  No instruction comes from a canned retail-body replacement.

Nine expected-word rows encode the setup/branch changes and two insertions.
Every preceding CSV byte remains identical. The independent original
assembly and normalized C agree on all words and bindings, including
independent GNU code/helper rebases.

Raw body SHA256:
`f2b02e8534548f0f7d738710ad067ccfbf75ea7f85aa8d8410d589a259588da3`.
Complete retail body SHA256:
`ca33fd71aa84e7b731007d6f840322324a96fefa1e137fe6e91d57e99b5c98d9`.

## Qualification

[Experiment](../../tools/experiments/game_linked_record_event.py) and
[focused tests](../../tools/tests/test_game_linked_record_event.py) reuse the
existing compiler/padder, MIPS/fault oracle, object/pool and native32 helpers.
Both copies pass eight fresh pre-install and eight fresh installed tests,
zero failures/errors/skips/reused checks, plus shared project checks.

- 3,240 guest cases cover all command/tag bytes, high incoming word homes,
  signed/high reference words, match gates, six alias layouts, provider
  mutations and two stack phases. Raw C public semantics and fitted/original
  complete modeled private state are checked separately. All 44 root words
  are visited; no unreachable word is silently omitted.
- Native32 O0/O2/O3 trap UBSan executes the actual recovered C callback and
  retained C dispatcher: 6,144 cases per profile, eleven effective defined
  wrong-C controls, canonical function-pointer types and complete destination
  canaries. Unsupported NULL commands are defined native cases.
- The compiled early-eighth-pointer control fails on a concrete big-endian
  pointer-byte alias in the guest. Private-stack aliases and native allocated
  layouts are not equated.
- 81 fired root-access prefix pairs, seven unsupported NULL commands
  and two selected-command NULL faults preserve emitted guest order. This
  does not establish portable C fault semantics or hardware behavior.
- Forty-two changed-raw-word controls, three binding/extent controls, two
  actual generated-padder expectation corruptions and a guard-prefix control
  fail closed. Four full-image corruptions are rejected.
- Six independent GNU links across three code/helper layouts compare original
  and fitted code and execute the selected paths. All helper binding moves
  are explicit.
- Preserve sixteen complete-owner neighbors/pools, including handwritten
  `func_150F7470`. The real five-command mixed-owner Make recipe matches
  all seventeen compact functions and the complete padded object.
  Isolated diagnostics are empty; owner diagnostics are unchanged.
  Inherited duplicate generated_12D630 recipe warnings remain.

Initial development failures were fixture/launcher defects: a duplicate
control name, an unused native fixture variable rejected by unchanged
`-Werror`, and a scratch inspect.py shadowing the standard library in direct
test launches. Correct the test runner import path; do not weaken warnings,
source semantics, negative controls or immutable fixtures. Final suites are
fresh and do not reuse those failed runs. Routine work uses zero Claude
calls; no package/provider or host changes.

## Production And Progress

Tools `c75016126bb12d402b7e583838e7471387584e80` committed first. Seal 16,002 files, 29 focused inputs and
all 1,454 linker objects in native/Linux-cache copies, using checked
stdin/tar transfer without DrvFS project reads. Preserve all 1,628 older
mirror dirty paths/statuses/hashes/HEAD; add only the two owned modules,
leaving 1,630 dirty paths. Do not commit or reset that independent mirror.

Production Make passes. Adopt only source, generated guard append, target
object and ELF as four qualified overrides. Caller object, linker script
and progress CSV remain identical. Strict full-image delta is exactly 132
bytes: 131 target-code bytes and one target-size byte, 12 to 176. There are
no metadata exclusions or symbol cycles. All other 6,054 bodies and all
6,055 function addresses remain fixed.

All 720 protected Game-data owners / 189,088 bytes remain exact:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Adopted ELF SHA256:
`4a81856d3680867e99ffd3e6ef5f6328701162418f849ffe023dd444f7dc511c`.

Fresh recount of actual adopted native ELF bytes: total **3,785/5,505
(68.76%)**, Game **3,112/4,832 (64.40%)**, Init 492/492, Debugger 181/181,
zero drift, 1,720 different. Threshold 4,129 requires **344 more** exact
functions. The remaining source-shape queue has 1,591 placeholders,
120 semantic/other definitions and nine parser misses; it is not C/ABI
qualification. Remove only this target from the previous queue.

Next audit `func_151AE590` from the freshly ELF-pinned screen. Keep
`func_1510D8C0`'s existing semantic Gfx* body separate from parser misses,
and `func_15014094` as existing-C matching work. The large helper and
`func_1509E730`, `func_1508CAD8`, `func_15169070` stay separate.
Root README gets only aggregate rows. Refresh the normal graph after the
consumer commit and explicitly audit old-node retention; not full-corpus
re-extraction or old-edge preservation. Full helper/gameplay acceptance is
not claimed. Goal remains open.
