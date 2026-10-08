# Game Attachment State Latch Direct Match

Date: 2026-10-08

## Result

Continue the adjacent placeholder from
[Note 1119](1119-game-matrix-creation-and-transform-setup-direct-matches-20261008.md).
Install complete semantic `func_15033838` in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
All **100 words /400 bytes** emit directly under existing IDO5.3 O2/g3,
with the original **0x20 frame** and **zero raw or linked differences**.
The previous zero-return placeholder has 98 real word differences.

VA `0x15033838..0x150339C8`, ROM `0x60CE8..0x60E78`.
Retail: [5D2C0.s](../../conker/asm/5D2C0.s).
No word guards, filler, generated data, compiler-profile, Makefile or shared-header
changes. Add one owner-local six-argument callback declaration; reuse the
existing disable callback declaration. Both calls retain R_MIPS_26 relocations.

## Recovered Contract

1. Save both incoming pointer arguments in their caller homes. Read node byte
   +0x06 and unsigned actor type +0x84. Node and actor storage are required;
   no default-action actor-null shortcut is added.
2. Action 0x16 chooses mode 4 and accepts type 0x165. Action 0x89 chooses
   mode 6 and accepts types 0x221, 0x223 or 0x31B only when the actor's
   attached object at +0x31C has subtype byte +0x198 equal to 2. All other
   actions choose mode 5 and accept type 0x157.
3. Read the complete latch word at node +0x38. With latch zero, invalid type
   returns zero without reading the attachment. With a valid type, read
   attachment byte +0x197 first. Its nonzero value or mode 6 allows the next
   read; mode 6 bypasses the byte's gate, not the byte's required read.
4. Then require attached unsigned flags +0x8A bit 0x2000 and unsigned counter
   +0x19E equal to zero. Store latch 1 **before** calling
   `func_151026BC(actor, -1, mode, 1, 255, 1)`. Return zero regardless of
   callback result, without overwriting a callback's subsequent latch mutation.
5. With any nonzero latch, a valid type first reads attached flags +0x8A.
   When bit 0x2000 is set, a nonzero byte +0x197 or mode 6 preserves the
   latch and returns zero. The activation counter is not read on this hold path.
6. Otherwise store latch zero **before** `func_151027E8(actor)`. Reload the
   actor from its incoming home after the store, preserving a qualified alias
   that makes the latch store overwrite that home. Return zero; no post-call
   node or attachment read is introduced.

The different activation/hold read order and lazy counter/type gates are
observable at required-storage faults. A required attachment is not given an
invented null gate. Caller-private-frame aliases beyond the specified fixture
remain unqualified.

## Source Fit And Controls

[Candidate driver](../../tools/experiments/game_node_attachment_latch_candidates.py)
retains the complete source, four profiles and source/semantic controls.
The initial nested early-return form has C102/frame0x20/21 differences.
A common zero-return label and separate hold-condition jumps recover every
word directly; register annotations on either or both arguments are also exact.
No dead instruction injection or post-compile normalization is needed.

| Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Selected /register-argument controls | 100 | 0x20 | 0 |
| Nested early return | 102 | 0x20 | 21 |
| Nonzero-bit activation expression | 99 | 0x20 | 43 |
| Signed actor-type reads | 100 | 0x20 | 3 |
| O2 without g3 | 97 | 0x20 | 92 |
| O1/g3 | 120 | 0x30 | 115 |
| O1 | 120 | 0x30 | 116 |

The signed-type form is a source control, not a semantic negative: all accepted
constants are below 0x8000, so sign extension cannot change the equality result.
Eighteen measured forms qualify **80 ordinary executions** and **eight effective
compiled semantic negatives**: wrong action/mode, hold-counter gating, omitted
mode-6 bypass, swapped enable arguments, late latch writes and byte counter width.
Alternate profiles qualify public effects, not identical private frames or traces.

## Qualification

[Seven tests](../../tools/tests/test_game_node_attachment_latch_match.py):

- **33,792 guest cases**: all 256 selector bytes, 17 unsigned type boundaries,
  all 256 active/subtype bytes, eight flag patterns, five counter values,
  four latch patterns, four callback mutation modes and two SP phases.
  The selector, gate and byte-axis grids are separate, not one full Cartesian
  product. Compare an independent semantic reference's ordered public reads,
  writes, calls, return and memory. Full GP/FP state, complete trace/memory and
  saved-register lifetimes agree for actual C versus retail.
- **99/100 words execute**. Word 19, the duplicated action-0x89 constant load
  at VA 0x15033884, is bypassed by both retail branch-likely routes. It is
  still compiler-emitted and checked byte-exact.
- Six lazy-storage cases, **23 ordered fault prefixes** and four aliases
  qualify required pointers, widths, byte/flag/counter gate order and partial
  writes. Aliases cover node=actor, attachment=actor, attachment=node and a
  latch store into the actor's incoming home. Callback latch observations prove
  write-before-call; modeled callback mutations prove no late restoration.
- **794,368 actual native32 executions**: 786,432 type-sweep cases across
  all 65,536 unsigned actor types/three action classes/four latch patterns;
  3,840 independent gate-grid cases; 4,096 active/subtype byte-axis cases.
  The type sweep's correlated fields alone do not cover mode-6 activation;
  the added independent grids explicitly cover it. Check all node, actor and
  attachment canaries, callback arguments, observed latch and preserved
  callback latch writes. Pointer width 4 /u16 width 2 are compile-time assertions.
- Actual copied owner has **39 unchanged neighbors**, unchanged relative
  relocations and normalized pool identities, with strict zero diagnostics.
  The real padder emits exactly 400 bytes with no filler/data. Three independent
  links check entry relocation and both symbolic call target rebases.

The initial seven-test pre-install run passes in **43.922s**, no skips, errors
or failures. Strengthen native coverage after identifying the correlated mode-6
gap; its targeted test passes in **1.141s**. Production source is unchanged by
this test-only strengthening. All **29 post-install focused tests pass in
233.647s**, zero skips/errors/failures: seven new, eight matrix caller/helper,
four earlier owner/padder, four selection-binding and six selection-scheduling
checks. Ten shared padder/word-patch tests pass in0.045s. Tools, Python syntax,
driver source/profile screens and whitespace checks pass. Documentation
validation: **102 documents /4,183 relative links /zero broken**.

The callbacks are controlled ABI/state hooks, not execution of their complete
original implementations. Hardware, full gameplay and PC-port acceptance remain
separate. No sibling Release build, save or runtime is modified.

```sh
python3 -m tools.experiments.game_node_attachment_latch_candidates
python3 -m tools.experiments.game_node_attachment_latch_candidates --profiles
python3 -m unittest tools.tests.test_game_node_attachment_latch_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

## Linked Audit

Against `conker/build/game-node-matrix-creation-test/after.json`, retain all
**6,058 symbols /6,042 retail slots /16 overflow symbols**. Only
`func_15033838` changes; **6,057 other bodies** and all addresses/extents
are unchanged. Verify the old placeholder hash and 98 previous differences.
`.init`, `.init_data`, `.debugger` and `.game_data` are unchanged. All
720 Game-data owners /189,088 bytes remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
All **11,144 guard rows** and the conversion CSV hash are unchanged.

Fresh exact totals: **3,375/5,467 (61.73%)**, Game **2,702/4,794 (56.36%)**,
**2,092 different /zero drift**. Init 492/492 and Debugger 181/181 remain
exact. Converted function/byte counts do not change because the placeholder
already counted as C. The root README changes only the two aggregate rows.
New ignored audit/receipts/baseline:
`conker/build/game-node-attachment-latch-test/after.json`.
ELF/progress rebuild succeeds with the existing duplicate generated_12D630
recipe warnings; no repository-wide warning-free claim.

## Next Work

Next local placeholder **`func_150339C8`**, **68 words /272 bytes**, frame
**0x40**, VA `0x150339C8..0x15033AD8`, ROM `0x60E78..0x60F88`.
Static inventory only, not a recovered candidate:

- Preserve node/actor in S1/S0 and first call the already matched tile-scroll
  helper `func_150334B8(node, actor)`, before global mode/freeze gates.
- D_800C35EA equal to 1 exits. D_800BEA0C nonzero conditionally unregisters
  the node's existing +0x3C effect through `func_1000FD38`, then clears it.
- Otherwise retain an existing handle, or create effect 0x448 through
  `func_1000FA64` using truncated signed-16 actor coordinates and the node/
  actor/callback arguments. Store the returned handle OR 0x80000000.
- Preserve callback-pointer relocations, fault/read order and handle lifetime;
  qualify the complete body before installation.

Continue broader Game matching, the open `func_15031070` resolver and complete
callee/runtime work. This checkpoint does not close that goal.
