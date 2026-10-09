# Game Record Ring Renderer Live-Value Proof

Date: 2026-10-08

## Result

Continue the same complete `func_151D80C4` from
[Note 1142](1142-game-record-ring-renderer-setup-fitting-20261008.md), using
the [focused workflow](../AGENT_WORKFLOW.md). VA 0x151D80C4..0x151D8718,
ROM 0x205574..0x205BC8: **405 words / 1,620 bytes / frame 0xD0**.
The C baseline is still **SETUP_FITTED / 185 raw word differences**.
No new source form, production normalization, installation or conversion credit.
Preserve the original retained assembly and older natural/fitted controls.

The new target-only relational checker closes the factor-arm transformation
and checks the whole reachable renderer's GP live-value relationships under
explicit equal-memory, owned-stack, nontrapping-operation and bounded-callee
assumptions. It reaches a fixed point in **689 worklist iterations**, covering
**383 CFG nodes / 404 words / 560 operand obligations / six call sites**.
The sole unreachable word, **+0x1A8**, is unchanged and checked separately.
Four independently GNU-linked symbol sets satisfy the same obligations.
This is a conditional congruence proof, not hardware/gameplay acceptance or
an instruction-mask-only match claim.

Fresh **30 distinct focused tests pass across selected runs**. The final clean
run comprises eight proof tests plus the older fitted-layout test:
**nine tests in 13.682s**, no skips. The other 21 are the sixteen complete
SETUP_FITTED tests, four prior scheduling tests and original uninstalled-shape
check. An initial combined command used a nonexistent older-layout selector;
its 29 real tests passed in 177.645s, but that command correctly exited one.
The corrected selector is included in the final clean nine-test run. Do not
describe the initial command as passing or claim a fresh full-module run.

Every installed body/address/extent, data, source, assembly, compiler profile,
progress row and **11,275 guards** remains unchanged. Last installed conversion:
[Note 1138](1138-game-record-ring-shaping-conversion-20261008.md).
Converted totals stay **5,481 / Game 4,808**; exact **3,392 / Game 2,719**,
zero drift and 2,089 different. Root README stays aggregate-only and unchanged.

## Closed Factor Block

The [proof helper](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_ring_renderer_proof.py)
derives its reordered stream from the candidate's complete expected nine-word
block at **+0x278..+0x298**, not from replacement retail words. Invert BNE to
BEQ, move both arms together, and move ANDI into the unconditional branch delay.
Retain the non-annulled `trunc.w.s` delay at +0x27C and the +0x29C join.
No relocation, inserted/omitted instruction, FP register change or memory
reordering is introduced by this block transformation.

The [proof suite](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_ring_renderer_proof.py)
reuses the existing MIPS numeric oracle rather than introducing another engine:

- **131,072 factor pairs / 262,144 executions** cover all 65,536 signed
  halfword opacity values and both flag paths. Complete GP/FP state, memory
  and ordered accesses agree between raw and factor-reordered streams.
  Factor is 255 or the low byte of signed opacity times twelve.
- **120 additional FP edge pairs / 240 executions** cover signed zero,
  subnormal/normal boundaries, finite extrema, infinities and NaN bit patterns
  using the existing bounded nontrapping truncation model. No FCSR/trap claim.
- **Four missing-halfword-byte pairs / eight executions** preserve the
  optional read and show that truncation occurs before either required-byte
  fault. The inactive factor path does not read the missing halfword.
- An annulled-delay negative actually loses the required converted F16 value
  on the default path; rejection is not only an expected-word assertion.
- **432 complete-renderer cases / 1,296 executions** compare raw,
  factor-reordered and retail streams across four flags, three phase patterns,
  views 0/3/-1, two SP phases and six live mutation modes. Raw versus reordered
  has identical complete GP/FP state, all memory, calls and access events at
  completed exit. Raw versus retail has identical complete exit memory,
  return cursor, callbacks and whole-entry public prefixes. Private raw-versus-
  retail GP/FP state and fault-store-prefix identity are not asserted.

The original partition remains eight factor-block differences, two save-order
differences and 175 other GP-only differences. Merely reordering the factor
block gives **182**, not 177, differences: five GP field differences remain
inside the now-aligned factor block. Thus 175 outside-block GP words plus five
inside-block GP words plus two saves still differ. This is an experimental
derived stream, not a reduction in the raw C candidate's 185 differences.

## Whole-Body Live Values

The checker tracks equivalence classes over paired GP and FP files, HI/LO,
the FP condition and immutable entry S2/S3 anchors. Each operation is
congruent only when its necessary inputs agree. Copies preserve aliases;
arithmetic and loads produce new paired values. Joins intersect must-equalities
instead of merging reaching-definition sets that could hide swapped paths.
Operand obligations are checked only after convergence, including the loop
backedge, branch-likely annulment and non-annulled delays.

All non-GP opcode, literal, FP-field and displacement bits must agree.
Mask only actually decoded GP fields, not reserved SLL bits. Unchanged dead
code is checked separately. Unknown instructions, branch subtypes or callees
fail closed. This is target-specific analysis, not a general optimizer or
numeric emulator.

Calls require equal integer arguments and the maintained equal-memory
invariant, including stack arguments. Their equal-effect/return contracts are
explicitly bounded. Kill volatile GP/FP, HI/LO and condition relationships
independently across the two streams; do not assume the callee produces equal
scratch-register values. Restore only the known return-value relationship and
retain callee-saved relationships. The six caller ABI boundaries are checked.

The S2/S3 saves at +0x14/+0x34 are not naively swapped raw instructions:
the intervening output move would otherwise save an overwritten value.
Validate each save against its immutable entry-register anchor and original
slot, and close the store-only window at +0x34. The intervening stores are
SP-relative and disjoint; there is no load/call/SP modification. Equal private
saved-slot memory is restored before the first owner read at +0x4C. This needs
an owned mapped frame and does **not** assert equality if that window faults.

Six effective GP-only negative controls keep opcode/literal masks intact but
fail at live-input obligations: wrong output/owner, backend owner, killed
post-MODE value, alpha product, loop decrement and live goal. Seven structural
controls reject reserved bits, FP operation, displacement, changed dead code,
overlapping save, wrong saved entry value and annulled factor delay. Six unknown
call controls and two unsupported branch-subtype controls also fail closed.
No timeout or unsupported-opcode outcome substitutes for a live-value witness.

Four independently assembled/linked original and compiled-candidate symbol
sets retain **16 relocation uses**, HI16 carry/LO16 sign and JAL regions.
Each fresh proof covers the same 404 words and 560 obligations. The existing
complete-body rebased execution suite is also freshly passed in the sixteen
SETUP_FITTED tests, as are native32, aliases, original caller/actual backend,
22 copied-owner neighbors, pools, diagnostics and real padder gates.

## Next Installation Gates

1. Keep the same complete SETUP_FITTED body. Derive a bounded GP-field/save/
   factor normalizer from the proven relationships, not a blanket retail-word
   replacement or smaller substitute body. Record exact expected words and
   preserve relocation metadata. No guard batch is installed in this turn.
2. Qualify raw/derived/retail public behavior and derived-versus-retail complete
   private GP/FP/memory/access state at completed and fault boundaries. Retain
   the explicit owned-frame bound for the raw save-order exception.
3. Add stale, missing and partial-transform negatives that actually expose
   logical errors, then requalify rebases, aliases, copied owner and padder.
4. Only then install/rebuild and audit every linked body/address/extent, data,
   guard-history and progress row before refreshing README aggregate totals.

Linked setup/dispatcher/combiner restoration, hardware/gameplay and reduced-
corpus graph repair remain separate open work. OGL Release remains frozen.

## Banking And Verification

Entry parent `e5d134d071ae60971db34c0b0c56821b1fd44d32`, mounted tools
`b0f5e404a8c695a3b978b571fd7b729ebd9d8819`: clean. Per **"Keep commited"**,
bank the two reviewed new proof files first at
**`4253f3a9138d113fb84a99af81b0de076b2d6624`**, then this note, concise
indexes and that exact parent gitlink. No push or remote publication verified.

Older standalone tools HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`.
New mirror paths were absent before copying. Prior candidate/recovery hashes
were checked first and unchanged. Only the two new proof paths are added to
its dirty status; all pre-existing status and both independently modified
file fingerprints remain unchanged. No reset/stash or duplicate history commit.

Fresh shared checks: **11 matcher/padder tests in 0.045s** and **three
repository-setup tests in 0.067s**, both tools project checks, proof CLI and
scoped checks of **129 documents / 4,109 relative links / zero broken links**
and four tools syntax/mirror pairs. The detailed numerical candidate and
unchanged neighbor evidence is distinguished from this turn's proof additions.

All seven protected SHA-256 fingerprints remain unchanged, including full ELF
`f240ca73721dfd7a24c0a85fd5697d45ea1ebc724a11ebd76d965e6b3cd86e99`;
the fresh baseline test verifies all **6,058 installed linked bodies**. Ignored
sources/receipts stay in `conker/build/game-record-ring-renderer-test/proof/`.
No ROM/transient file tracked, host/runtime/save/Release or account changes.

Graph query precedes investigation. Fresh manual `graphify update .` exits one,
refusing **16,857 nodes over the retained 38,646-node graph** and preserving
19,398 nodes from 2,972 still-existing excluded files. No force, upgrade,
changed ignore policy or graph-repair claim. One Codex writer, zero Claude calls.

```sh
python3 -m unittest tools.tests.test_game_record_ring_renderer_proof -v
python3 -m tools.experiments.game_record_ring_renderer_proof
```
