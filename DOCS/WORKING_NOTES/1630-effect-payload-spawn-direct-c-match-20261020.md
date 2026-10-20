# Effect Payload Spawn Direct C Match

Date: 2026-10-20. Consumer predecessor: `5eb37f89`; tools predecessor:
`f1f3716`. Tools checkpoint **67c13be** is committed first. No push.
This completes the isolated draft recorded in
[Note 1629](1629-kinematic-step-direct-c-match-20261020.md).
The wider **75% total C-matching goal remains active**. The previous and current
goal turns both make progress.

## Installed Result

Complete purpose-commented `func_150BA4C0` replaces the false zero-return body in
[generated_E7970.c](../../conker/src/game/generated_E7970.c).
Its original name is retained. All **39 words / 156 bytes / frame 72** emit
directly from the existing **IDO O2/g3 profile**, with **three original call
bindings, zero guards and no Makefile/profile change**.
VA **150BA4C0..150BA55C**, ROM **E7970..E7A0C**.

The recovered interface is `void(void *source, u8 variant, s32 parameter)`.
It captures a source pointer, source byte at 3B and zero float into a 12-byte
payload, computes unsigned random % 9 + 15, submits the nine-argument factory
request and copies all 12 bytes to result + 28 only on successful allocation.
The explicit unsigned cast is applied to the existing **signed** random
helper's result, not encoded as an incompatible unsigned return declaration.

The payload's three reserved bytes at offsets 5..7 are deliberately left
locally unwritten and still copied. They are real copied bytes, not dummy
storage added to obtain a frame. The same source/payload pattern already exists
elsewhere in this project. Native tests constrain defined fields; guest tests
also constrain the actual three incoming stack bytes.

## Caller And Provider Boundaries

A full pristine scan of every US Init/Game/Debugger function span finds exactly
two direct JAL sites:

| Caller | Call PC | Arguments And Return Use |
| --- | --- | --- |
| func_150265CC | 150272B0 | Non-null source from SP+764, unsigned byte from SP+773, third word 1; the common branch delay overwrites v0 with 1 |
| func_1506F02C | 1506F044 | Current actor, FF, 0; epilogue restores RA/SP without reading v0 |

The first caller remains an unrecovered 3,451-word dispatcher. Its call window
is statically qualified; the complete dispatcher is not claimed as executed.
The existing 12-word C wrapper is actually connected and executed in tests.
Its SP restore precedes JR, whose delay is NOP: do not borrow the previous
kinematic routine's different epilogue assertion.

Add the recovered explicit prototype to
[game_981E0.c](../../conker/src/game_981E0.c). The opaque source pointer accepts
the caller's actor pointer without an incompatible character-pointer prototype.
All **328 caller-owner raw and padded functions, pools, addresses and extents**
remain unchanged. Caller warnings are unchanged after filename/line-number
normalization; the recovered target compiles without diagnostics.

Reuse the established nine-argument factory wire declaration and keep its
linked implementation fixed. Its older C representation still uses a
pointer-typed payload-size argument; this step does not repair or claim
whole-provider ISO C type consistency. The bounded factory/random contracts
test calls, results and specified adversarial writes, not complete providers.

## Fresh Qualification

[The integration helper](../../tools/experiments/game_effect_payload_spawn.py)
reuses existing compiler, original-assembly, object, padding, ELF and protected
data helpers. [Eight tests](../../tools/tests/test_game_effect_payload_spawn.py)
reuse the existing MIPS runner with its existing unsigned-divide/HI support.

**Eight pre-install and eight installed tests pass in both copies**, with zero
errors/failures/skips:

| Stage | Primary | Standalone Tools Mirror |
| --- | ---: | ---: |
| Pre-install | 52.795s | 35.383s |
| Installed | 23.670s | 12.919s |

- **338 cases / 1,352 modeled variant/phases** compare ordered public accesses,
  canonical calls, complete public state and literal full modeled GPR/FPR/
  condition/HI/LO/private/public RAM, calls/access histories and visits.
  All **39 target words** execute.
- Test unsigned random boundaries/residues, negative-bit-pattern returns,
  byte truncation of incoming variants, complete parameter-word forwarding,
  null/successful allocation, source changes at both helpers and captured
  fields/payload representation.
- **676 phases are configured** with original retail memcpy. Only **352
  actually enter its instruction stream**, which is asserted separately;
  failed allocations must not execute it. Both modeled and actual forward
  byte-copy paths agree, including private physical overlaps.
- **48 phases execute the actual original C-wrapper instructions**, with the
  recovered function and optional original memcpy connected below them.
- Fired guest writes alter incoming variant/parameter homes and the reserved
  payload bytes. The actual original and direct C follow those live homes
  and copy the same three bytes. Zeroing the reserved array and prematurely
  caching the variant are effective negatives in **four completed phases**.
- **326 native32 cases** pass O0/O2/O3, contraction disabled, with trap UBSan.
  They include the real C wrapper and valid nonoverlapping local-payload
  copies. Native tests decode and verify the pointer, byte and zero-float
  fields and output fences, but deliberately leave the reserved bytes
  unconstrained. Private-frame probes/overlaps are guest-only.
- Six independently compiled native semantic controls return the expected
  mismatch: signed modulus, late source-byte capture, wrong factory flags,
  short copy, wrong destination offset, or suppressed successful copy.
- Three independently GNU-linked code/helper rebases and moved argument
  buffers pass **24 additional phases** against an independently assembled
  original object. All three call bindings are preserved; there are no
  data HI16/LO16 bindings to invent or normalize.
- Eight wrong-image controls reject altered headers, target/neighbor bytes,
  symbol extent, truncation and appended bytes.
- Two task files agree exactly between tools copies; four Python copies parse.
  Both project-tools checks pass.

Two audit assumptions were corrected before acceptance: C-only search missed
the dispatcher call, and its sibling wrapper did not use the assumed JR-delay
SP restore. Assertions now follow the complete pristine caller evidence;
no production instruction was altered to satisfy those assertions.

The source domain requires a readable non-null source byte at 3B and valid
factory/copy buffers. Hardware FCSR/MMU, unobserved indirect-call consumers,
full dispatcher/provider execution, portable-C private aliases/unwritten byte
values and gameplay/host-port acceptance remain separate.

## Actual Build And Scope

All five other target-owner functions and pools are preserved.
The actual expanded Make shadows run **eight productive commands** across the
target and typed caller. Both keep normal O2/g3 flags, and their raw/padded
objects equal the independent qualification. The existing duplicate-rule
Make warning remains recorded; it is not introduced by this recovery.

The production build exits zero in **42.897s** and exactly reproduces the
independent whole-ELF prediction:

- **117 changed bytes**: **116 target instruction bytes**, **one target-size
  metadata byte**, symbol size **12 to 156**.
- No metadata ranges, sections or symbol-order groups are excluded.
- Every **6,056 other linked body**, all **6,057 addresses** and all
  **189,088 protected Game-data bytes / 720 owners** remain fixed.
- The original ROM/assembly, entire guard manifest, Makefile and progress CSV
  remain byte-identical. This replaces already-counted C, not a conversion row.
- Installed tests require strict live source/caller/image audit before using
  frozen predecessor fixtures. Historical pins are not rewritten to accept
  the new bodies. Unchanged neighbor suites are reused through exact whole-image
  preservation, not called freshly rerun broad suites.

## Counts And Next Step

Fresh matcher: **Game 3,022/4,832 (62.54%)**,
**overall 3,695/5,505 (67.12%)**, **1,810 different / zero drift**.
Init stays 492/492 exact; Debugger stays 181/181 exact.
At the current denominator, the 75% target remains **4,129 exact functions**:
**434 more matches** are needed. Recompute if the denominator changes.
Root README receives only the updated aggregate rows.

The fresh ELF-pinned queue has 1,675 simple zero-return placeholders,
126 semantic/other entries and nine unlocated source-shape entries. Those
are triage categories, not ABI/semantic qualification.

Next related short placeholder: **func_150F10D4**, generated_11C2B0,
VA **150F10D4..150F1170**, ROM **11E584..11E620**.
Its first isolated draft already matches **39 words / frame 88**, without
diagnostics, but is **not installed and earns no credit**. It captures a
24-byte payload: source pointer/byte, the same reserved bytes, zero float,
and three float words from source + 14/18/1C; then requests a factory object
and conditionally copies it. Qualify callers, captured-coordinate bit patterns,
saved S0 lifetime, reserved bytes, full owner and actual build/image first.
Other tracked work, including func_15070C40 and func_1508CAD8, remains queued.

## Preservation And Receipts

All **1,472 pre-existing dirty mirror paths/statuses/hashes** and HEAD
`ddbdd16b` are preserved. Only two absent task files are added; final dirty
paths **1,474**. No mirror commit/reset/stash/clean, push, dependency/compiler
update, advisory writer, host/frozen Release operation or save/config change.

```text
Raw C code:      d8e3cee14ee50971a92c633b511552c799a403625b3f35c5b7e26f9c013ee6e1
Installed owner: bc57f47d631163b8243aa84c9cf4363d4d4cd4dfeda24350653802b393788f96
Typed caller:    5703a20f2ea3edf6f697c6f07b4cbc194849a92d4f5125d8cfc38143b2946583
Linked ELF:      e0feb081b6f1afbba274e5142a49aeb0170f6ada3a50cc7cf87328f7476ed6ec
Guards fixed:    7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
```

Ignored receipts: `conker/build/game-effect-payload-spawn/qualified/`
contains primary/mirror logs and JSON, native/control builds, independent
original/rebase objects, caller diagnostics, actual owner/Make/padding/first-
link/build/live/data audits, matching/75%-queue evidence, mirror preservation
and graph closeout after consumer commit.
The next non-installable draft is under
`conker/build/game-effect-position-payload/screen/`.
The wider 75% goal remains active, not complete.
