# Actor Target Timer Recovery And Matching Boundary

Verified: 2026-10-19. **Experimental semantic recovery, not installed and not
byte-exact.** Resume `func_1508D850`, generated_B3020, VA
`1508D850..1508DA1C`, ROM `BAD00..BAECC`, 115 words / 460 bytes, frame80.
Consumer predecessor **d1e7a5b**, tools predecessor **6dbeb82**. Bank tools
**4211351** before this documentation/tools-pin checkpoint. No push.

## Recovered Behavior

The complete candidate uses meaningful slot, actor, target, timer and distance
names without inventing original symbols or a speculative record structure.

1. Cache the initial context's target and timer array bases. Publish the
   target's low byte to the actor's nested `+0x129` byte, then reread the
   signed full-word target. Negative targets take the explicit zero exit.
   The publication may alias the target word; do not cache the value early.
2. Compute horizontal distance from actor/target X and Z at `+0x14/+0x1C`,
   with float32 subtraction, multiplication, addition and square root.
   Class0 is strictly beyond5000; class1 is strictly beyond2000; otherwise
   class2. The5000 constant is D_8009DA8C from2424E0.rodata.s.
3. Read the signed-byte selector and signed16 threshold at selector*3+class.
   If threshold is strictly less than the signed32 timer, clear the original
   timer, reload the global context and target word, then test the current
   context's `+0x16C0` mask. Call func_1508EB90(slot,0x61,0x2000) if set.
4. Preserve the original timer and actor pointers across that callback. Reread
   the old timer afterward. If zero, clear the actor's current nested flag
   byte `+0x12A`, call the float RNG, freshly read selector/probability, and
   compare signed probability against truncated float32(sample*100).
5. On success, reload the actor's current nested pointer and set flag1.
   Callbacks can change context, old timer, nested pointer, selector and
   probability. The saved actor/timer and fresh nested/selector reads matter.

## Compiler And Return Boundary

All12 initial/fitting/lifetime screens have empty IDO diagnostics. Measured
representative results under the existing no-unroll profile:

| Form | Words | Frame | Word differences |
| --- | ---: | ---: | ---: |
| Initial void operation | 110 | 88 | 113 |
| Partial-int, array bases | 114 | 80 | 90 |
| Ternary distance class | 115 | 80 | 76 |
| Ternary, direct coordinate expressions | 115 | 80 | 60 |
| Shared byte offset, direct coordinates | 114 | 72 | 102 |

The best research form recovers the complete retail floating-point load and
arithmetic sequence, including source X/Z before target X/Z, the later5000
load, and the redundant branch produced by the second-class ternary. Its
raw, unrelocated function digest is:

```text
7a173d55e1f6d80293c18209802ce9ab0bb18cba06317baa1329024ca4adc601
```

It still has60 differences, not just a proven register permutation. Examples:
duplicate slot shifts, later selector/threshold address setup, distinct GP
lifetimes, and the notification-mask branch/reload schedule. Keep these as
source/compiler research; no broad expected-word recipe has been added.

Retail explicitly puts zero in V0 only for negative targets. Other paths leave
distance-class, notification-provider or RNG residual state. The RNG leaves
the new seed's low16 bits in V0 and its scaled fraction in F0; casting the
fraction to int does not recover that state. The sole direct caller propagates
V0 through its epilogue but does not interpret it in the bounded window.
This does not establish a coherent numeric C return contract.

`RESEARCH_PARTIAL` therefore remains an experimental s32 body with only the
observed negative-path return. `SELECTED` is its void semantic counterpart,
used for result-discarding native qualification. Neither is a production ABI
decision. No native fallthrough result is consumed or claimed meaningful.
Continue the caller's upstream/result-consumer audit before installation.

## Fresh Qualification

All **seven tests pass in15.317 seconds**, without skips:

- **158 fixtures/two stack phases:316 paired public-state checks** compare
  retail and raw research C with an independent reference. Check every backed
  public byte, ordered public stores, helper order/arguments and preserved ABI
  registers. All115 retail instructions are visited. This is not full scratch
  GP/FP/private-stack identity or a general numeric-return claim.
- Native32 **O0, O2 and O2+UBSan** each pass158 complete translated-buffer
  fixtures. Pointer fields and numeric word/halfword values are translated to
  host representation, not compared as big-endian byte aliases. Five effective
  negatives change threshold equality, probability equality, probability sign,
  cached timer context or distance equality; each exits21 or23, not a signal.
- Corpus includes adjacent float32 views of2000/5000, nonuniform thresholds
  that make distance classes observable, signed timer/selector/threshold/
  probability edges, slots0/7/25, targets below zero and0..25, notification
  masks and mutations at both providers. Samples-.25 and1.25 are explicitly
  finite modeled-provider stress, outside the actual RNG's0..1 range.
- **50 actual-RNG fixture pairs** execute all25 original func_150ADA68 words
  using the existing wide-register runner. Check the real64-bit seed read/
  write, scale bits37800080 (1/65535), F0-dependent effects and incidental
  V0=next_seed&65535. Seed89413 reaches65535 and sample1.0 exactly. The signed
  probability and strict100 endpoint remain checked. This is a bounded
  instruction model, not hardware FCSR/exception qualification.
- Connect the **actual26-word** func_1508EB90 wrapper to a modeled
  func_1509BFB0 script provider. Check identity0xE3 becomes0x20E3 and forwarded
  arguments are(1,0x20E3,0x61,0x2000). An initial test correctly rejected a
  mistaken32-word window containing six instructions from the next routine;
  the corrected window executes every owned word. Do not call the script
  interpreter itself executed or qualified.
- **32 fired access-cut pairs** agree in requested access and prior public
  stores on the callback-changing path. The requested cut actually fires;
  this is narrower than hardware faults or complete private literal state.
- A completed backed guest alias changes initial target01000000 to0 through
  the early byte publication, then exercises the fresh target read. This
  emitted-binary check is not native C out-of-bounds evidence.
- **20 actual returning-caller runs** retain the full-word A0 delay load from
  S0+8, branch/RA delay load and S0/SP/JR/NOP epilogue. The aligned direct-JAL
  scan finds only ROM CB5EC / VA1509E13C. The caller's72-byte frame and saved
  slots are explicit live-ins; upstream dispatch is not executed.
- Both complete-owner profiles reproduce the same115/80/60 candidate with
  empty diagnostics and preserve72 other routines and normalized pools.
  Actual private padding preserves those neighbors, pools and all73 function
  addresses. Every frozen production input remains byte-identical.

Commands from64CBFD under WSL:

```sh
python3 -m tools.experiments.game_actor_target_timer_candidates --lifetimes
python3 -m unittest tools.tests.test_game_actor_target_timer_recovery -v
python3 -m tools.match_progress conker/progress.csv conker/build/conker.us.elf conker/conker.us.bin
```

Receipts, commands, diagnostics, candidate objects and native programs are
ignored under `conker/build/game-actor-target-timer/`. Python syntax checks
pass in both tools copies. The standalone mirror retains its old HEAD and all
1,355 prior dirty-file hashes; only the three new task files are copied there,
with identical hashes. No mirror commit or history change.

## Production And Resume

No production source, assembly, guard, Makefile, ELF or progress CSV change;
no production rebuild. Root README stays unchanged because there is no new
matching credit. Fresh measurement remains:

```text
Game:     3005 / 4832 (62.19%)
Total:    3678 / 5505 (66.81%)
Init:      492 / 492
Debugger:  181 / 181
Different:1827; address drift:0
Owner:      57 / 73 exact,16 still different
```

Baseline digests remain ownerf6aa1bdc..., guardsd59c93d7...,
ELF06b43755...; their complete expected hashes are in the candidate's INPUTS.
No host-port or frozen Release changes, Claude/REA calls, dependency installs
or push. The broad Game matching goal remains open.

Next steps, in order:

1. Resolve the real return contract beyond the bounded caller epilogue. Keep
   the void semantic body and partial-int compiler study explicitly separate.
2. Recover shared slot-offset/address lifetimes without losing frame80 or the
   recovered FP sequence. Hoisting address definitions is not permission to
   hoist mutable memory reads across publication or callbacks.
3. Recover the notification likely-branch/timer-reload placement. Prove any
   eventual scheduling/GP recipe against complete private/literal states,
   fired boundaries and independent rebases; do not patch60 observed words.
4. Only after those gates, qualify an exact private image, install, rebuild,
   remeasure, update README aggregates and commit the next checkpoint.
