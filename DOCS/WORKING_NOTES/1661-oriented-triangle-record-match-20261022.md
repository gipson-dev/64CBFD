# Oriented Triangle Record Direct C Match

Date: 2026-10-22

## Result

Recover `func_1514F640` in `conker/src/game/generated_17CAF0.c` from
its zero-return placeholder. All **42 words / 168 bytes**, the **40-byte
frame** and both call bindings emit directly from normal IDO O2/g3 C.
No guards, profile changes, dummy locals or handwritten function emitter.

VA1514F640..1514F6E8 / ROM17CAF0..17CB98, ends exclusive.
Preserve `conker/asm/17CAF0.s`. Raw unlinked C body SHA-256:
`596ae263014e50a7262b2ebe7f2a163f0f1f8e6a9edafb103d24c07c4f6341db`.
The old body was three words/12 bytes in this 168-byte slot. Restoring it
gains one exact match without changing converted-C counts or denominators.

Use `void func_1514F640(u8 *source, u8 *output)`, descriptive parameters
and a purpose comment. Retain the address-based public symbol. Add canonical
`s32 func_15144E80(s16 *, f32 *, f32 *, f32 *);` and float-returning
`f32 func_15144A74(f32 *, f32 *);` declarations. Cast both wrapper address
words to `u8 *`; their emitted code and empty diagnostics remain unchanged.
No shared header or helper implementation changes.

## Recovered Contract

Write output byte0 =2, then copy the float word at source+0x20 to output+0x28.
Preserve its bits, including negative zero and NaN payloads; do not make this
a numeric conversion or move it after the helper. Bytes1..3 are untouched.

Call `func_15144E80(source+0xC, output+0x10, output+0x1C, output+4)`.
The input vertices are nine signed shorts. The 44-byte output contains the
tag/reserved bytes, normal, secondary cross vector, edge vector and snapshot.
Failure does not clear the vector fields. Any nonzero helper result, including
negative/high-bit words, enables `func_15144A74(output+4, source)`.
Only an ordered result <+0 negates normal X/Y/Z. Both zero signs and NaNs
skip negation. Retain retail's load-three, negate-three, store-three sequence
and saved S0 output lifetime across volatile-register/FPR helper clobbers.

The incoming source pointer is homed at original SP+0; the compiler-created
normal-pointer temporary is at current SP+0x24. A named normal local has the
right length/frame but two SP+0x20 versus SP+0x24 differences. Inline output+4
expressions recover both words without guards or artificial storage. Named
result variants grow the frame. Historical source spelling is not unique.
Physical guest-home aliases are ABI tests, not portable C home guarantees.

Bindings: `R_MIPS_26 func_15144E80` at body offset0x3C and
`R_MIPS_26 func_15144A74` at0x50. All42 target words are dynamically visited.

## Caller And Helper Bounds

The prepared aligned retail input contains two direct target JALs:
ROM17D3C0 in `func_1514FEFC`, and ROM181148 in `func_15153C84`.
No aligned literal target pointer is found. This is static-reference evidence,
not proof that computed runtime entry is impossible.

Both complete wrappers are18 words/frame80, with a 44-byte local at parent
SP+0x24. They forward the record, two full word arguments, argument3's low
byte and the fifth stack argument to `func_1514FF44` or `func_15153CCC`.
Execute every wrapper word and compare all44 guest packet bytes across72
phases. Those consumers remain bounded spies, not restored implementations.
Native checks exercise the builder itself, not complete native wrappers.

Connect original/current `func_15144E80` (141 words), `func_151450B4`
cross product (29) and `func_15144A74` dot product (13). Their source and
linked instructions are unchanged. The first remains preserved GLOBAL_ASM
in `game_16EE20.c`; this work does not count it as a new C conversion.

Across48 finite phases, compare an independent rounded-float32 edge/cross/
dot reference with signed-short boundaries, both facing signs, duplicate
vertices and distinct collinear vertices. The basis helper rejects identical
vertex pairs, not every collinear triangle. Visit136/141 basis-helper words
and all29 cross /13 dot words. The optional NULL-normal path and unvisited
words are not dynamically qualified by these target calls. Guest/native
models do not establish N64 FCSR or exception equivalence.

## Qualification

Tools: `experiments/game_oriented_triangle_record.py` and
`tests/test_game_oriented_triangle_record.py`, identical in both copies.

| Actual Run | Active Tools | Older Mirror | Errors / Failures / Skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests,302.428s | 8 tests,289.992s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests,1.737s | 2 tests,1.698s | 0 / 0 / 0 |

Explicitly reuse the other six pre-install checks per copy only under strict
source, raw/padded object, helpers, inputs and complete-image identity.
They are not fresh installed executions. Both shared project-tool checks pass.

- 704 guest phases cover status words, both zero signs, subnormals, infinities,
  quiet/signaling NaN bit patterns, snapshot bits, source-home/provider
  mutations and two SP phases. Another60 alias phases cover overlapping
  buffers and guest homes. Compare exact reads/writes, calls and complete
  modeled GPR/FPR/HI/LO/RAM/events between original and direct C.
- Native32 O0/O2/O3 each pass36 defined builder cases with trap UBSan.
  All six compiled wrong-C controls return23: tag, snapshot offset, negative
  gate, zero gate, Y negation and success gate. The old stub is rejected by
  an actual missing output effect. Do not assert native private padding.
- Six independent GNU links at three anchors preserve both bindings.
  Check486 fired root-access fault prefixes and five complete-image corruption
  controls. This is emitted guest ordering/state evidence, not portable C
  fault/MMU or hardware-FPU equivalence.
- Pin37 historical inputs and the predecessor padded object. Preserve all40
  owner neighbors, raw/padded pools, all12 GLOBAL_ASM members and empty
  compiler diagnostics. Actual shadow Make executes five productive owner
  commands with the existing profile; only cleanup is skipped.
- Seal15,814 live/cache files, including all1,454 linker objects. Preserve
  all1,534 pre-existing older-mirror dirty paths, statuses and hashes;
  add only the two task files, leaving1,536 dirty paths and its HEAD fixed.
  Commit tools first; do not reset or commit that independently dirty mirror.

## Production And Progress

Normal Make rebuilds the owner, linked ELF and progress CSV in the verified
Linux copy. Mark the unchanged guard manifest old to avoid unrelated rebuilds;
do not append or modify any guard. Adopt only four qualified generated outputs
after live-input revalidation. Linker script and conversion CSV are unchanged.

Production matches the complete independent prediction with zero exclusions:
**120 changed bytes =119 code bytes +1 target-size metadata byte**.
All other6,054 bodies, all6,055 addresses and all720 protected Game-data
owners /189,088 bytes remain fixed. Protected-data SHA-256 remains
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

ELF SHA-256:
`22ee525b9e2f5e7ab90840bc04bf89ab4ea4248914bd09cce219fde15e62505f`.
Installed padded owner:
`f0081485566e1b66bb0d877ab9d1efc9bfa4124a511690c4744ee2055a328659`.
Tools checkpoint: `fad6d019bf57a43eb78f845bea3e0a87ba97f2bb`; no push.

The standard matcher runs against the actual live consumer ELF:
total **3,729/5,505 (67.74%)**, Game **3,056/4,832 (63.25%)**,
Init492/492 and Debugger181/181 exact, zero drift and1,776 different.
The75% threshold remains4,129 exact: **400 more matches are needed**.
Queue shapes:1,645 placeholders,122 semantic/other and nine unlocated entries.
Next `func_151A4CE0` is screened only, not edited or credited. Keep the
862-word owner stub `func_1508CAD8` queued.

The pre-edit graph neighborhood has four relevant nodes and15 edges.
Retail instructions/source establish the calls, not graph edges alone.
Post-commit worker completion and all-old-node retention audits belong in
private checkpoint receipts. Retain the existing excluded-corpus and HTML
size caveats; do not claim full corpus re-extraction.

Root README changes only the two aggregate rows. Preserve unrelated work
and frozen host Release. No complete consumer, full-game, host rendering,
gameplay or complete hardware acceptance is claimed.
