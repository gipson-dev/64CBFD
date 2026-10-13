# Game Actor Matrix Clear Byte Match - 2026-10-12

## Scope And Recovery

Resume the full Game matching goal from consumer `9b5d16c2` / tools `84cfb3a`
and [Note 1319](1319-game-actor-type-dispatch-direct-match-20261012.md).
Both active checkouts were clean. Inspect the focused graph, complete original,
actual27-word caller,25-word helper, table, owner and normal O2/g3/MIPS2/o32 profile.
Zero Claude calls; preserve the independent older tools checkout and host Release.

Target [func_15034728](../../conker/src/game/generated_61490.c:59):
VA0x15034728..0x150347E8, ROM0x61BD8..0x61C98,48 words/192 bytes/frame0x20.
Replace its three-word zero-return placeholder,47 real differences, with the
complete void actor matrix clear and one local s32 bone-count helper prototype.
No shared header, compiler-profile, layout, original assembly or data change.

Read the actor's buffer+0x1D4 first and mask+0x9C second; either zero returns
without the type read/helper. Pass unsigned byte+4 to func_1502DB20. Subtract one
with the original low32 wrap, signed-clamp the last index to31, and reload the
buffer after the helper. Negative last index performs no matrix write.
Scan selected bones backwards, re-reading the live mask after each iteration.
Clear positive float zero at offsets0,4,8 of rows0,16,32 in each64-byte matrix.
Preserve all fourth components and the final row,28 bytes per matrix. Mask
aliases must affect subsequent iterations; a cached mask changes the contract.
Keep saved S0 at SP+0x18, RA at+0x1C and the original branch-likely delay work.

## Compiler Fit And Guard Derivation

The initial indexed-float form emits46/frame0x20/37 differences. Byte offsets
reach48/27, but IDO advances a pointer and strength-reduces the row counter.
The explicit32-bit address view, row shift and separate signed clamp recover
the exact48-word instruction/control-flow/access structure, with18 differences.
Declaration/pointer/loop controls do not improve that allocation. O2 without g3
has24 differences; no-unroll remains18; O1 controls are longer and farther away.
Keep the actual owner profile, not a broad build/profile change.

The raw C is **not direct matching**. Eighteen expected-word guards normalize
one closed post-helper GPR cycle A2->A3->T0->T1->T2->T3->T4->T5->T6->T7->A2,
plus the commutative integer addu operand order at offset0x7C.
Derive replacements from instruction fields, not copied retail instructions.
No opcode, immediate, branch target, access width, delay-slot work, frame,
floating register, helper relocation, instruction insertion or omission changes.
The helper's R_MIPS_26 relocation at0x28 is outside every guard.
All48 normalized words equal retail; all18 sealed raw inputs reject corruption.
No physical register binding, fabricated field, arbitrary NOP or ROM-word body.

## Qualification

```sh
python3 -m tools.experiments.game_actor_matrix_clear_candidates
python3 -m unittest tools.tests.test_game_actor_matrix_clear_match -v
```

Eight pre-install tests pass in29.285 seconds; eight final installed tests
pass in29.990 seconds, no skips. Reuse the prepared compiler/parsers/oracles.

- 4,320 isolated guest cases plus24 mask-alias cases cover signed/wrapped count
  edges, all256 type bytes, masks including bit31, null gates, two stack phases
  and provider mutations of buffer/mask. Raw/fitted/original public storage,
  writes, accesses, calls, FPR and visited instructions agree with an independent
  reference. All48 words are visited. Raw GPR comparisons canonicalize the
  closed cycle after an opaque provider colors its ten affected scratch registers
  uniformly; this is not arbitrary incoming scratch-register/hardware parity.
- All361 own-access fault cuts fire for raw/fitted/original with completed
  controls; full fitted fault-prefix state agrees. Exclude opaque provider
  accesses from the cut count. A null buffer succeeds with type/mask unmapped;
  an active missing type byte fails closed. Alias storage includes valid mapped
  backing below the actor, not silently permitted unmapped writes.
- Native32 O2/O0 executes the unchanged selected C for16,384 cases each,
  checking the entire actor and both2,048-byte matrix buffers. Five fresh
  fourth-row, fourth-component, cached-buffer, wrong-clamp and byte-mask controls
  fail by observed behavior. Wrapped full-word provider returns are ABI probes;
  the connected actual helper has its own unsigned16 count/subtract-four domain.
- 36 connected guest cases run all27 original caller words,48 target words and
 25 real func_1502DB20 words with its actual64-entry jump table. Compare raw
  public storage/accesses/calls and fitted complete machine state to retail.
  Independent reference covers disable0/1/255, empty/active rows, null buffers,
  count adjustments and aliased writes that affect later actor eligibility.
- The caller scans25 records: (D_800D121C-D_800CC2D0)/0x32C=25, not the entire
  declared26-entry array. Native32 O2/O0 runs the unchanged caller/helper/target
  C chain for12 cases each, using explicit linker aliases for that real end
  boundary. Native comparisons total32,792 including these24 connected cases.
- All nine copied-owner neighbors and relative relocations stay identical,
  normalized pools stay fixed, and raw target bytes/relocations equal the isolated
  object. Complete GLOBAL_ASM postprocessing and both full-owner padders agree.
  Three independent original assembly/C symbol layouts match after normalization;
  the helper relocation rebases normally, without a guarded literal call address.

Test-only corrections fix an over-read beyond the27-word caller, unmapped alias
backing, a missed coverage update for null-buffer cases and a GCC indentation
warning in the connected fixture. The reusable historical guard-count helper
has an older limit that does not accept the current14,623-row manifest. Leave
it unchanged; this target pins the complete previous manifest SHA and checks
the exact18-row append. Do not claim all historical suites were rerun/passing.

Software models and native fixtures do not prove hardware PC/EPC/FCSR, rendered
animation, host integration or full gameplay. Wider Game matching stays open.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds. Updating the
shared guard manifest triggers a wider rebuild. Preserve/report the known
duplicate generated_12D630 recipe warning and existing diagnostics in unchanged
files; the target owner introduces no diagnostic. No ROM build/replacement.

The literal whole-ELF gate permits only the192-byte target slot and symbol
size12->192. Exactly147 target bytes across47 words and one size byte change,
148 total; no symbol serialization exception is needed. Every other ELF byte,
function body/address/extent, section and named symbol stays fixed.
All189,088 Game-data bytes /720 owners remain exact, SHA0bbc00e1.
The previous guard byte prefix is identical; rows14,623->14,641 add only the
derived18 target guards. Progress.csv, layout and Makefile stay byte-identical.

Fresh matching: Game2,820/4,823 (58.47%), total3,493/5,496 (63.56%), drift0,
different2,003. Converted totals stay5,496/6,044 and Game4,823/5,323.
The root README changes only its two measured matching rows.

Source SHA256: fd0157bc0b31b73ae7540aafb748a418c58c054f01281b25eb78de63d7b09d61.
ELF SHA256: 596bbcfec8dc41b2397ad6a4f19ddb6026de18ef928042c7a3b4d44c3d342635.
Guard SHA256: 8bd422a0acd766c6dbd4e3cbaedf01c22e43cee418079facdf566eca08151cc4.
Makefile SHA256 remainsfa975a22531dab077a7ac6ccd90c03084c485fe8df5915cf2f57cfbe52c65127.

After literal image/guard proof, archive the previous text manifest, ELF and
guard snapshots in this target's ignored build folder. Advance only those two
validated fingerprints and preserve all seven other text inputs. Fresh text
tests05/06 pass in1.743 seconds with effective corruption controls. No text
implementation, shared oracle semantics or historical image-gate changes.
Explicitly reuse unchanged broader receipts from Note1319, not fresh-test claims.

## Banking And Next

Mounted tools `969150247e589a0b4088236aad18e2b94761bb1e` is committed first,
then consumer source,18 guard rows, docs/README aggregates and tools gitlink.
Consumer/mounted/older tools checks, both Windows syntax checks and whitespace
checks pass. Older HEAD`ddbdd16b` and all112 unrelated saved task fingerprints
remain fixed. Copy only two absent new files and the verified shared text pin;
dirty390 becomes392 and saved fingerprints113 become115. No older commit.
Banking includes relative-link validation, clean active checkouts, post-bank
integrity and a fresh terminal Graphify Rebuilt/zero-workers receipt. Preserve
existing graph scan/version/HTML-size warnings and the CSV EOL warning; no push,
dependency/compiler install, host/OGL Release, save/configuration or editor change.

Next ordinary target is func_150345E4 in the same owner:81 words/frame0x20,
current78 differences, original ROM0x61A94..0x61BD8. Recover the mounted-buffer
gate, live state/flag dispatch through func_1503453C, type-specific callbacks,
incoming index home and actor pointer saved around helper calls. No candidate
or matching credit is accepted for it yet. Keep text218/114/cut27 and translator
49/34 open; do not close or silently pause the full Game goal.
