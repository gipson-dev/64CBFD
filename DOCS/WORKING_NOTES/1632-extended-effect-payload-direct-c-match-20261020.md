# Extended Effect Payload Direct C Match

Date: 2026-10-20. Consumer predecessor: `0e8564bc`; tools predecessor:
`db39e84`. Tools **219a63c** are committed before the consumer pin. No push.
This completes the nine-difference draft from
[Note 1631](1631-effect-position-payload-direct-c-match-20261020.md).
The preceding and current goal turns both make progress.
The wider **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace `func_151A499C`'s false zero-return body in
[generated_1D0840.c](../../conker/src/game/generated_1D0840.c) with the complete
typed, purpose-commented routine, retaining its original name.
VA **151A499C..151A4A38**, ROM **1D1E4C..1D1EE8**.
All **39 words / 156 bytes / frame 80** emit directly from ordinary **IDO
O2/g3**, with **four original bindings**, **zero new guards** and no Makefile
or compiler/profile change.

The recovered interface is `void(void *source, u8 variant)`.
The 32-byte payload at retail SP+2C contains:

| Offset | Field |
| --- | --- |
| 0 | Source pointer |
| 4 | Source byte from 3B |
| 5..7 | Locally unwritten reserved bytes |
| 8 | Captured global float D_800A8D64 |
| 12 | Zero float |
| 16 | Active byte 1 |
| 17..19 | Second locally unwritten reserved range |
| 20, 24, 28 | Three zero floats |

Submit the eight-argument request `(300, -1, 5, 0, 1, 32, variant, 0)` to
func_151491F4; copy all 32 bytes to result + 28 only on successful allocation.
The global float and source byte are captured before the factory. The low
variant byte is loaded from its real incoming argument home before the call.

The prior nine differences were **one four-byte payload-base displacement**,
not nine independent scheduling errors. Declaring the existing result pointer
before the payload places it at **SP+2C**, not SP+30, and closes every word.
Two of six real-local declaration orders match; source-volatile controls regress.
No unused locals, synthetic padding, volatile qualifier or assembly substitution
is introduced. The two reserved ranges remain locally unwritten and copied.

## Caller And Provider Boundary

A pristine scan of every US Init/Game/Debugger function span finds one direct
JAL: **func_151A3390 at 151A3458**. The original 93-word caller forwards its
saved actor S0 and the byte at SP+9F in the call's delay slot. It does not
consume the target's return value. This caller remains an unrecovered C stub:
its ABI window is checked statically, **not represented as full caller execution**.
There is no existing C call requiring another owner/prototype edit.

The original **28-word func_151491F4 wrapper** is connected and executed in
tests. It forwards the eight arguments to func_15149130, inserting the fourth
argument -1 and preserving the remaining wire values. The original
**11-word memcpy** is also connected and executed. Both helpers' pristine
instructions equal their pre-install linked ELF bodies.

The underlying allocation provider is a bounded call/result/mutation contract,
not a complete allocator execution. Keep its linked implementation fixed.
The established opaque-pointer factory wire declarations are used; the older
provider's pointer-typed payload-size representation remains outside this
change. Do not infer whole-provider ISO C type consistency or gameplay parity.

## Fresh Qualification

[The integration helper](../../tools/experiments/game_effect_extended_payload.py)
reuses the existing compiler, original assembler, object/pool parser, padder,
Make shadow, linker, ELF and protected-data helpers.
[Eight tests](../../tools/tests/test_game_effect_extended_payload.py) reuse the
existing MIPS oracle and native32 workflow.

**Eight pre-install and eight installed tests pass in both copies**, with zero
errors, failures or skips:

| Stage | Primary | Standalone Tools Mirror |
| --- | ---: | ---: |
| Pre-install | 24.941s | 27.441s |
| Installed | 23.721s | 52.778s |

- **164 cases / 1,312 modeled phases** compare independent ordered public
  accesses/calls/output and literal full modeled GPR/FPR/condition/HI/LO,
  private/public RAM, histories and visited instructions.
- Exercise byte/variant truncation boundaries, signed zeros, finite extremes,
  guest-only nonfinite float representations, null/successful allocation,
  source/global mutation after capture and correct active/zero fields.
- **656 phases execute the original factory wrapper**. **656 configure original
  memcpy, but only 392 actually enter it**; failed allocation must skip it.
  Assert fired entries separately. All **39 target, 28 factory and 11 copy
  words** execute across the corpus.
- An independent forward-byte-copy reference qualifies actor-output aliases
  and private payload overlaps at +1/-1. Fired private writes alter both
  reserved ranges and incoming source/variant homes without changing the
  already captured source/global/variant values.
- **94 native32 cases** pass O0/O2/O3 with trap UBSan and contraction disabled.
  Decode every defined payload field, check complete copy/fences, and retain
  finite factory-mutation/actor-alias cases. Leave all six reserved bytes
  unconstrained natively; private homes/overlaps/nonfinite FPU are guest-only.
- **Nine compiled semantic negatives** fail with the expected mismatch:
  late byte/global capture, wrong active/zero/variant/size, short copy, wrong
  destination or skipped successful copy.
- **Two guest negative phases** reject explicitly zeroing both reserved ranges.
  A separately compiled wrong-declaration layout reproduces exactly **nine
  instruction differences**; it is rejected as a literal-layout control, not
  claimed as an independent defined-field semantic failure.
- **Three independently GNU-linked code/helper/global rebases**, with moved
  argument buffers, pass **24 additional phases**. The global is tested at
  800B7FFC/800B8000/800AFFFC to exercise signed HI16/LO16 carries. Both call
  bindings and the original global HI16/LO16 pair match independent assembly.
- **Fourteen strict-image controls** reject corrupted headers, target/neighbor
  bytes, extent, truncation/appending, and each of the three metadata names
  or values. All other named symbol definitions are compared canonically.
- Both task files agree between tools copies, all four Python copies parse,
  and both existing project-tools checks pass.

The domain requires a valid source byte and valid factory/copy buffers.
Hardware FCSR/MMU, indirect consumers, complete caller/allocator execution,
portable-C private aliases or specific unwritten-byte values and host-port
acceptance remain separate. No Claude call was needed for this bounded recovery.

## Owner And Closed Image Proof

Preserve all **22 other target-owner functions** and pools. This owner retains
its existing GLOBAL_ASM function, so the actual Make shadow runs **five**
productive preprocessing/compiler/postprocessing/padding/assembly commands,
not the earlier C-only owner's three. Handle its explicit output redirection
without invoking an unquoted shell. Raw/padded objects match qualification.

The first body-and-size-only image check correctly rejects **18 extra metadata
bytes**. They are a closed rotation of three pre-existing symbol/string entries:

```text
Before: D_800A8D64, D_800A80E4, D_80096914
After:  D_800A80E4, D_80096914, D_800A8D64
```

Predict that exact cycle using the existing structured symbol parser/record
layout. Require contiguous original entries and strings, and preserve every
named definition. No symbol-table/string-table section or arbitrary range is
excluded. Do not relax historical input pins to accept the new image.

The production build exits zero in **21.593s**, reproducing the strict image:

- **138 changed ELF bytes**: **119 target instruction bytes**, **one target-size
  byte** (12 to 156), and the **18 closed symbol/string-order bytes**.
- Every **6,056 other linked body**, all **6,057 addresses**, and all
  **189,088 protected Game-data bytes / 720 owners** remain fixed.
- ROM, original assembly, full guard manifest, Makefile and progress CSV are
  byte-identical. This replaces already-counted C, not a conversion row.
- The known duplicate generated_12D630 recipe warning remains; no new target
  compiler diagnostics. Do not claim a warning-free full build.
- Installed tests audit the strict live source/ELF before frozen predecessor
  fixtures. Unchanged broad neighbor suites are reused through exact whole-image
  preservation, not described as newly rerun.

## Counts And Next Recovery

Fresh full matcher: **3,697/5,505 (67.16%) overall**,
**Game 3,024/4,832 (62.58%)**, **1,808 different / zero drift**.
Init remains 492/492 exact and Debugger 181/181 exact.
The present 75% threshold is **4,129**, requiring **432 further exact matches**.
Recompute if the denominator changes. README receives aggregate rows only.

The ELF-pinned queue is refreshed with fresh full classification. Reuse only
unchanged source-shape entries, justified by the strict sole-function source
replacement and whole-image audit. Remove exactly this newly exact entry:
**1,673 placeholders, 126 semantic/other and nine unlocated entries** remain.
These are triage categories, not semantic qualification.

Next related short draft: **func_151CD2C0**, generated_1FA770,
VA **151CD2C0..151CD35C**, ROM **1FA770..1FA80C**.
Its isolated C now matches **39 words / frame 72**, without diagnostics,
after reordering existing locals. It is **not installed and earns no credit**.
Qualify the returned allocation pointer across memcpy, 16-byte payload,
captured word/low-byte fields at source +18/+1C, three copied reserved bytes,
argument homes, factory/callers and full owner/Make/image before installation.
Keep func_15070C40, func_151BB044 and the 862-word func_1508CAD8 queued.

## Preservation And Receipts

All **1,476 pre-existing dirty mirror paths/statuses/hashes** and HEAD
`ddbdd16b` are preserved; add only the two absent task files, leaving
**1,478 dirty paths**. No mirror commit/reset/stash/clean, push, dependency/
compiler installation, host/frozen Release build/launch or save/config changes.

```text
Raw C:      9af53304c32e1774d0320b267ef08ce07a23cea116ad46fad9540e61f121cb82
Linked ELF: 918bb7a8922586bf687eb35db0a5cfb1971b05fe4c12cd723280165692ecc6e1
Guards:     7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
```

Ignored receipts: `conker/build/game-effect-extended-payload/qualified/`
contains primary/mirror suites, native controls, independent originals/rebases,
owner/actual-Make/closed-image/live/data audits, production/progress/queue,
mirror preservation and post-commit graph closeout.
The next uninstalled draft is under
`conker/build/game-effect-record-payload/screen/`.
The wider 75% objective remains active.
