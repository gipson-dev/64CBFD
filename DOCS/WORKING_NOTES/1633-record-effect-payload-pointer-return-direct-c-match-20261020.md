# Record Effect Payload And Pointer Return Direct C Match

Date: 2026-10-20. Consumer predecessor: `1002b47a`; tools predecessor:
`219a63c`. Tools **2a385cc** are committed first. No push.
This completes the isolated draft from
[Note 1632](1632-extended-effect-payload-direct-c-match-20261020.md).
Both the preceding and current goal turns make verified progress.
The wider **75% total C-matching objective remains active**, not complete.

## Installed Result

Replace the false zero-return `func_151CD2C0` body in
[generated_1FA770.c](../../conker/src/game/generated_1FA770.c) with its complete,
typed and purpose-commented C routine, retaining the original name.
VA **151CD2C0..151CD35C**, ROM **1FA770..1FA80C**.
All **39 words / 156 bytes / frame 72** emit directly from the existing
**IDO O2/g3** profile, with **two original call bindings, zero new guards and
no compiler/profile/Makefile changes**.

The recovered interface is
`void *(void *source, u8 variant, s32 parameter)`.
The 16-byte payload at retail SP+34 contains:

| Offset | Field |
| --- | --- |
| 0 | Source pointer |
| 4 | Captured complete word from source +18 |
| 8 | Zero word |
| 12 | Low byte of the complete word read from source +1C |
| 13..15 | Locally unwritten reserved bytes |

Submit `(300, -1, -1, -1, 0, 30, 16, variant, parameter)` to the existing
factory. On success, copy all 16 bytes to result +28 and return the allocation
base, **not memcpy's destination return**. Allocation failure returns null.
The selector store is the factory JAL's delay instruction; the allocation
save at SP+44 is the memcpy JAL's delay instruction. Reload that saved result
after copying. Existing-local declaration order places the real payload and
return home correctly; no padding or volatile workaround is added.

## Typed Existing Caller

A complete pristine scan of every US Init/Game/Debugger function span finds
one direct JAL: **func_15013F9C at 15013FA8**.
Its original ten-word wrapper forwards the source, FF and 1, then explicitly
returns 1, discarding the allocation result.

In [game_40490.c](../../conker/src/game_40490.c), add the recovered pointer-return
prototype and change that wrapper's integer-typed address argument to an opaque
source pointer. Both sides now agree locally without a pointer/integer warning.
All **32 raw and padded caller-owner functions**, pools, addresses and extents
stay unchanged. Execute the actual original wrapper with the recovered target
and optional original memcpy below it; also compile the corrected real C
wrapper in the native32 harness.

The existing nine-argument factory is a bounded call/result/mutation contract.
Its complete allocator implementation is not executed. Keep the legacy
provider's pointer-typed size representation outside this change, as recorded
in Note 1632; no whole-provider ISO C compatibility or gameplay claim is made.

## Fresh Qualification

[The integration helper](../../tools/experiments/game_effect_record_payload.py)
reuses existing compiler, original assembler, object/pool, padder, linker,
actual-Make and protected-data helpers.
[Eight tests](../../tools/tests/test_game_effect_record_payload.py) reuse the
existing MIPS oracle and native32 workflow.

**Eight pre-install and eight installed tests pass in both copies**, with
zero errors, failures or skips:

| Stage | Primary | Standalone Tools Mirror |
| --- | ---: | ---: |
| Pre-install | 61.687s | 27.204s |
| Installed | 14.662s | 10.848s |

- **216 cases / 864 modeled phases** compare independent public accesses,
  canonical calls, output and returned value, plus literal full modeled
  GPR/FPR/condition/HI/LO, private/public RAM, histories and visited words.
- Cover complete signed-word bit patterns, low-byte extraction, unsigned
  variant truncation, complete parameter forwarding, allocation failure,
  factory mutation after capture and retained source/variant/parameter homes.
- **32 phases execute the original C-wrapper instructions**, including its
  unconditional return 1. **432 phases configure original memcpy; 256 actually
  enter its instruction stream**. Assert fired entries separately.
- All **39 target, 10 caller and 11 copy words** execute across the corpus.
  Both modeled and original forward-copy routes agree, including record-buffer
  aliases, capture-field overlap and private payload overlaps at +1/-1.
- Fired private writes alter all incoming argument homes and the three
  reserved bytes. The captured fields/wire arguments and copied reserved
  representation follow the original instruction order.
- **32 guest-only +1-overlap phases actually change the saved allocation
  result** at payload +16 / SP+44. The independent reference models the save,
  forward copy and subsequent reload, rather than assuming a magical preserved
  pointer. These deliberately adversarial physical overlaps are not portable
  C memcpy semantics or evidence of a gameplay bug.
- The first overlap assertion was non-discriminating: its original low mapped
  addresses copied the same high byte already present in the saved pointer.
  Move only the test record mapping to 12028000 so the overwritten byte and
  returned value actually change. No production instruction changes for this
  fixture correction; both actual instruction streams still agree completely.
- **180 native32 cases** pass O0/O2/O3 with trap UBSan. Inputs use real typed
  signed-word subobjects at +18/+1C. Check all defined payload fields, full
  copying/fences, factory mutation, returned allocation versus copy destination,
  and the corrected real C wrapper. Reserved-byte values, private frame
  probes/overlaps and capture-field overlaps remain guest-only.
- **Ten compiled semantic negatives** fail with the expected mismatch:
  late word/selector capture, wrong zero/selector/variant/size, short copy,
  wrong destination, assigning memcpy's result as the allocation, or skipping
  successful copying.
- **Two guest negative phases** reject explicit reserved-byte zeroing.
  **Four more** reject removing the real saved-result reload, with both
  modeled and original memcpy routes. No production ASM is modified.
- **Three independently GNU-linked code/helper rebases** and moved input
  buffers pass **24 additional phases**, including the saved-result overlap.
  Both R_MIPS_26 bindings match independent original assembly; there are no
  data HI16/LO16 bindings to invent.
- **Eight strict-image controls** reject altered header, target/neighbor bytes,
  symbol extent, truncation and appended bytes.
- Both task files agree between tools copies, all four Python copies parse
  and both existing project-tools checks pass. No Claude call was needed.

The domain requires readable aligned source words and valid factory/copy
buffers. Complete allocator, indirect consumers, hardware MMU/FCSR, arbitrary
fault-prefix parity, portable-C private aliases/unwritten values and host-port
acceptance are not established by these bounded tests.

## Whole Owner And Actual Build

All **51 other target-owner functions** and pools remain fixed.
The old target owner already has **eight pointer/integer diagnostics** in
unrelated wrappers. Compare those before/after after normalizing filenames
and line numbers; they stay unchanged. The selected routine itself compiles
without diagnostics. Do not silence or repair unrelated warnings in this step.
The caller's diagnostic set likewise remains unchanged.

The actual Make shadows run **eight productive commands**: normal C-owner
compilation/padding/assembly and the caller's existing assembly-processor
path. Both retain O2/g3 and their complete raw/padded objects match independent
qualification, including every caller function and its existing GLOBAL_ASM.

The production build exits zero in **37.648s** and reproduces the exact
independent ELF prediction:

- **121 changed bytes**: **120 target instruction bytes**, **one target-size
  metadata byte**, extent **12 to 156**.
- No metadata permutation, section/range exclusion or guard/profile change.
- Every **6,056 other linked body**, all **6,057 addresses**, and all
  **189,088 protected Game-data bytes / 720 owners** stay fixed.
- Original ROM/assembly, the entire guard manifest, Makefile and progress CSV
  remain byte-identical. This repairs already-counted C, not a conversion row.
- The inherited owner diagnostics and duplicate generated_12D630 recipe
  warning remain. The full build is not described as warning-free.
- Installed suites require the strict live source/caller/image audit before
  using frozen predecessor fixtures. Never rewrite historical pins to accept
  the replacement. Unchanged broad neighbor suites are reused through exact
  whole-image preservation, not claimed as freshly rerun.

## Counts And Next Function

Fresh full matcher: **overall 3,698/5,505 (67.18%)**,
**Game 3,025/4,832 (62.60%)**, **1,807 different / zero drift**.
Init stays 492/492 exact and Debugger 181/181 exact.
At this denominator, **4,129** exact functions reach 75%:
**431 further matches** are needed. Recompute if the denominator changes.
README receives aggregate rows only; detailed updates stay here.

Refresh the ELF-pinned queue with fresh full instruction classification.
Reuse only source-shape entries protected by the strict source/caller/whole-
image proof; explicitly check that the typed caller stays semantic before
and after. Remove just this newly exact routine:
**1,672 placeholders, 126 semantic/other entries and nine unlocated entries**.
These categories are triage, not qualification.

Next screened short recovery: **func_15116888**, generated_142560,
VA **15116888..15116924**, ROM **143D38..143DD4**.
Its semantic heading-projected-speed draft has **39 words / frame 64** and
**seven differences** in the best `signed-before-product` screen.
It is **not installed and earns no credit**. Name the real integer deltas
and projected product; preserve modulo-word position differences and both
float-to-integer truncations. The heading helper reads X/Z, leaving the
middle vector float locally unwritten. Recover remaining expression scheduling
and register roles, then qualify helper bounds/caller ABI, private storage,
native floating behavior, owner/Make and strict image before installation.
The signed angle expression is not yet accepted as covering arbitrary helper
results; establish the actual helper's return bounds instead of assuming them.
Keep func_15070C40, func_151BB044 and func_1508CAD8 queued.

## Preservation And Receipts

All **1,478 pre-existing dirty mirror paths/statuses/hashes** and HEAD
`ddbdd16b` are preserved. Add only the two absent task files, leaving
**1,480 dirty paths**. No mirror commit/reset/stash/clean, push, dependency/
compiler installation, advisory writer, host/frozen Release build/launch
or real save/config change.

```text
Raw C:      c4899b45f585ceb4509df6486c87110bac7fcc25a4e2c91a2c5f42282906a61d
Linked ELF: ed481ea11966433e90071c0bede0f56f4111452e4ad0545095f2fa8b6a7a8758
Guards:     7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
```

Ignored receipts: `conker/build/game-effect-record-payload/qualified/`
contains primary/mirror suites, native controls, original/rebase objects,
owner/caller/Make/first-link/live/data audits, production/progress/queue,
mirror preservation and post-commit graph closeout.
Next uninstalled screens: `conker/build/game-heading-projected-speed/screen/`.
The 75% objective remains active.
