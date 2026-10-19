# Route Actor Update Correction Prefix Layout

Date: 2026-10-18. **244-word normalized prefix only; not installed; zero credit.**

Continue `func_15087350`, generated_B3020, VA `15087350..15087CC0`, after
[Note1573](1573-route-actor-update-local-homes-and-error-lifetime-20261018.md).
Consumer before this checkpoint: `fc36fa0`; tools before: `b668034`.
Bank tools **3076fa7** first, then the consumer pin and this handoff. No push.

## Closed Prefix Recipe

`game_route_actor_update_prefix_layout.normalize()` accepts only the complete
qualified594-word storage candidate and all70 bindings from Note1573. It emits
**only244 words**, ending after the copy call's delay slot. After relocation,
all244 words equal retail. It does not emit a return/tail, guards, or a padded
604-word replacement, and is not an installable function.

The recipe permutes the244 source positions and renames closed GPR/FPR roles.
One scheduling NOP becomes a signed-error register copy derived from the C
call-save operand. The modular offset moves from SP+54 to SP+68; the selection
call's error spill/reload move from SP+160 to SP+1A8. One integer address sum
changes commutative operand order. No floating arithmetic is reassociated,
no original volatile qualifier is inferred, and no retail word array is used
as normalizer input. The test forbids file reads during normalization.

Branch destinations follow moved operations, with an explicit block-entry
label for the step-clamp join: its call-save moves into the call delay slot,
but the block still starts with the argument move. Twenty symbol bindings
move with their actual operations. Raw source and binding fingerprints are
unchanged from Note1573. Normalized unlinked prefix SHA-256:

`4ae1b781680bacb0f1c751c0dbf2028ae828e16e5344759945b12e9d8ca12c80`.

## Bounded Execution

The new oracle reuses the existing instruction engine and494 verified retail
helper words. It emits no unqualified tail instructions. A separate code-fetch
gate stops before the first exit at retail word244,380, or593; corresponding
raw exits are244,373,583. Unknown destinations fail rather than execute a guessed
continuation. No complete function return/ABI or tail qualification is inferred.

**Seven tests pass in24.790 seconds, no skips.**

- All244 literal words match. A fresh primary-profile compile still emits
 594 words/frame456/450 differences and preserves72 neighbors and pools.
- Reuse the same553-input connected corpus, plus six null-table cases covering
  both stack phases and signed/wide indices. Its exits are477 copy-boundary,
  71 nonmoving-branch, and five null-table cases. Four additional clamp witnesses
  exercise both limit assignments. Together they execute243 prefix words.
  Word54 is the fallback load bypassed by the mode branch and unconditional
  branch at52; no observed execution of it is claimed.
- Compare raw-source public memory, actual physical helper arguments, canonical
  helper calls, mapped scalar homes and error/offset carriers at every bounded
  exit. Compare normalized/retail complete memory, GPRs, FPRs, calls, events,
  PC, delay ownership, condition and LO. Do not claim raw register/private parity.
- All850 fired caller-access cuts agree between normalized and retail prefixes
  on six phase/path combinations. The original raw cut14 still rejects in all
  six controls. This closes that boundary only in the normalized prefix, not
  in the compiler's unchanged raw object. Helper-internal fault cuts, arbitrary
  aliases, hardware traps/FCSR and gameplay remain outside this qualification.
- Reject594 single-word raw mutations,70 binding removals and111 register-recipe
  mutations. Two executed-word negatives affect public memory: removing the
  error copy on an eleven-advance path, and misplacing the selection spill on
  a zero-advance path. Both gates are asserted before interpreting the result.
- Three independent GNU assembler/linker maps cover the original bindings and
  two complete data/call rebases, with distinct HI16/LO16 carry boundaries and
  all six calls. Rebased runtime execution is not claimed.

Early test failures were qualification-fixture errors, not production defects:
anchor discovery initially included suffix-only library aliases, the existing
553 corpus already contained null-table cases, and the wrong-spill negative
needed a no-advance witness because an earlier advance had saved the same error.
All are corrected and the final full suite above passes.

The complete C/native32 qualification from Note1573 is **reused, not rerun**.
The new suite checks its retained553-case receipt's raw SHA and exact native-O2
source body. No new compiler capture, debugger attach, alternate compiler profile
or host/Release action. The old completed capture remains audit-only.

## Bank And Resume

Two new tools files are synchronized identically to the older standalone mirror.
Preserve its `ddbdd16` HEAD and all1,290 pre-existing dirty leaf hashes; do not
commit/reset that mirror. Both copies pass their three repository-setup tests
and project-tool smoke checks; consumer `make tools-check` passes. Both new files
are ASCII/AST-valid. Tools **3076fa7** is committed before the consumer pin.

All23 protected production inputs remain frozen, and the installed Note1568
whole-image audit passes again. No production source, ELF, guard, Make, progress
or root README change, and no fresh progress recount. Carry forward installed
Game2991/4828, total3664/5501,1,837 different and zero drift. The full raw candidate
is still594 of604 words/frame456/450 differences. This prefix earns no conversion
or matching credit. Graph refresh/preservation is checked after the consumer
commit; see the ignored `graph-audit.json` receipt beside the new test receipts.

```sh
python3 -m unittest tools.tests.test_game_route_actor_update_prefix_layout -v
python3 -m tools.experiments.game_route_record_integration --audit
make tools-check
```

Continue **the same function**, using the recipe as an explicitly bounded phase:

1. Extend operation provenance through look-ahead, coordinates and the branch
   join. Derive the genuine SP+48 conversion spills/reloads; do not pad by count.
2. Reconcile the nonmoving projection's start-Z spill and constant lifetime,
   then the finalizer/ranking induction and join schedules. Ten words remain
   missing in the full raw body; no full604-word recipe exists yet.
3. Complete source-derived all-word/binding and private/alias proof, qualify
   every continuation and return, then exercise actual mixed padding/Make,
   independent rebases and the first whole-ELF prediction before installation.
4. Install only the complete qualified routine, audit all linked bodies/data,
   and recount progress. Keep broader Game work active.

User confirmed the earlier overwritten `Conkers` path was disposable scratch;
no recovery is needed. No unrelated file was restored or removed.
