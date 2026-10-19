# Actor Pair Scheduler Frame And Buffer Homes

Date: 2026-10-19

## Result

Continue `func_1508C5B8` from
[Note1607](1607-actor-pair-scheduler-recovery-and-frame-boundary-20261019.md).
The complete experimental C now directly emits the retail **192-byte frame**,
group-pointer home **SP+0x7C**, cost array **SP+0x80**, choice array **SP+0x90**,
incoming homes **SP+0xC0/C4**, and saved primary-actor lifetime in **FP**.
The first call's second mask clear also emits in its actual delay slot.

| Complete Body | Words | Frame | Word Differences |
| --- | ---: | ---: | ---: |
| Note1607 selected | 256 | 208 | 241 |
| New selected | 255 | 192 | 238 |
| Retail | 261 | 192 | 0 |

This is **not installed or byte-exact**. Seventeen opening words are exact,
and access cuts0..14 now match literally at both stack phases. The next
measured literal-state difference is access15: the context pointer has been
loaded into retail A2 versus raw V1. The remaining GP/FP/copy/branch layout
must still be recovered; identical RAM is not complete CPU-state parity.

Consumer predecessor `ac7ce338` and primary tools predecessor `63868c8` were
clean. Only two new tools files and this documentation/pin checkpoint change.
Tools `ed38dd5` is committed before the consumer documentation/pin.
Preserve all 1,414 pre-existing dirty leaf hashes and HEAD `ddbdd16b` in the
standalone mirror; copy only the two absent task files. No mirror commit,
reset, stash or clean. No push, host/frozen Release, save or dependency work.

## Direct Source Recovery

The selected body uses the original three-entry ranking plus fourth scratch
cells, explicit five-bit unsigned shift masks and all Note1607 semantics.
Its source is `tools/experiments/game_actor_pair_scheduler_home_candidates.py`,
candidate `compact-homes-dx`; the earlier candidate/test files remain unchanged.

1. Remove the redundant Z coordinate copy, but retain the separate X copy
   needed to keep the retail self-subtraction under IDO. Reuse the Z-delta
   temporary for displaced rank costs only after the squared cost is formed.
   These real lifetimes recover frame192 without a frame patch.
2. Reuse the integer cursor across the disjoint initializer, rank-shift and
   selected-choice loops. Put actor initialization inside the positive primary
   count arm. This recovers FP's advancing actor pointer without an extra
   call spill/reload; the background actor-base lifetime remains separate.
3. Order the real scalar/choice/cost/group declarations so the live arrays
   and captured pointer occupy retail90/80/7C. Moving X, DX or cost into the
   same declaration position gives identical instructions. No dummy storage,
   volatile declarations or physical-register binding is introduced.

Source-register hints produce no improvement and are not selected. Explicit
integer-address induction-bound screens grow to258/269/270 words; a signed
candidate-width screen grows to276. These are rejected diagnostics, not new
compiler profiles or a reason to weaken the current C arithmetic/array gates.

Selected raw SHA256:
`ad992aec1fad04999e4966bb07af529738e8312aaabcd1815eae3b6ea152d630`.

## Qualification

The final ten-test primary suite passes in43.090s, no skips:

```sh
python3 -m unittest tools.tests.test_game_actor_pair_scheduler_homes -v -f
make tools-check
make -C conker match-progress NON_MATCHING=1
```

- 83 fixtures/166 completed retail/raw pairs agree with the independent
  public reference, ordered public stores, returns and callback snapshots.
  All 261 retail words are visited. Native32 O0/O2/O3 with UBSan passes80
  fixtures and eight effective updated semantic negatives.
- **All RAM is identical in166 completed pairs**, including the full private
  frame, with exactly ordered group/rank scratch stores. These complete-RAM
  comparisons use the documented opaque pair effects, not arbitrary callees.
- **30 fired literal cut pairs** cover cuts0..14 at two phases, closing the
  previous cut0 frame failure. Both cut15 controls actually fire; requested
  access and RAM agree, while the complete GP-register state differs as above.
- Four completed guest aliases place the captured group table over the live
  SP80 ranking scratch. Retail/raw RAM, calls and return values agree. The old
  frame/buffer implementation is an effective call/public-store negative in
  all four cases. These deliberate guest stack aliases are not native C inputs.
- Both complete raw owner profiles preserve all72 other functions and pools;
  target payloads equal the standalone payload. Twelve actual NULL-actor
  child runs return, and two negative budgets fire equal bounded-prefix stops.
- Every frozen production input retains its hash. No old assertion or guard
  is weakened, no normal override is added, and the original stub remains.
  The earlier eight-test recovery suite also passed unchanged during this
  investigation; the final focused suite discovers only its ten intended tests.

The new mirror modules pass the same ten tests in44.382s against the prepared
consumer inputs, redirecting only the test input root, not their mirror imports.
Separate primary/mirror receipts live under the ignored directory
`conker/build/game-actor-pair-scheduler/homes/qualification/`.

No production rebuild is needed for these uninstalled experiments. Fresh
match-progress remains **Game3014/4832 (62.38%)**, **total3687/5505 (66.98%)**,
1,818 different and zero address drift. Init492/492 and Debugger181/181 remain
exact. Owner `generated_B3020` remains66/73 exact; seven routines are unfinished.
The root README and production source/CSV/Makefile/ELF are unchanged.

## Next Matching Boundary

Continue this same255-word body, not another conversion batch. Do not redo the
now-qualified frame and homes or promote it merely because RAM agrees.

- Close the A2/V1 context-pointer allocation boundary and the primary-phase
  first/second/primary/mask saved-role cycle. Retain the saved FP actor lifetime.
- Recover retail's distinct X-copy roles, three-entry initialization bound,
  choice-versus-cost rank induction and candidate-loop predicate/schedule.
- Recover the background count-address/base/stride lifetimes, repeated live
  count loads, redundant first-index copy and mask-check schedules. Preserve
  all five explicit count-mask semantics and fresh context access order.
- Only then qualify complete source-origin layout/relocations, literal
  registers/FP/private/fault behavior, effective aliases, independent GNU maps,
  actual padding/Make and strict linked scope before installing all261 words.

Note1607's bounded negative-budget, synthetic wide-count/endian-alias, NaN/FCSR,
opaque geometry and full-gameplay limitations still apply. There is no new
guard manifest, blanket instruction transplant or matching credit here.
