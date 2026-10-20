# Kinematic Step Direct C Match

Date: 2026-10-20. Consumer predecessor: `d20c7204`; tools predecessor:
`b66644c`. Tools checkpoint **f1f3716** is committed first. No push.
This follows the short-candidate queue from
[Note 1628](1628-pickup-update-complete-match-20261020.md).
The active **75% total C-matching goal remains unfinished**. Both the previous
and current goal turns make progress.

## Installed Result

Complete purpose-commented `func_1519BE1C` replaces the zero-return placeholder
in [generated_1C2C60.c](../../conker/src/game/generated_1C2C60.c).
The original name is retained, with a recovered no-return-value interface:

```c
void func_1519BE1C(KinematicVector *position, KinematicVector *velocity,
                   f32 acceleration, f32 timestep);
```

Its complete **39 words / 156 bytes / frame 16** emit directly from the
existing **IDO O2/g3 profile**, with **zero word guards, zero relocations,
zero compiler diagnostics and no Makefile change**.
VA **1519BE1C..1519BEB8**, ROM **1C92CC..1C9368**.

The three-float vector has size 12, checked in native compilation. C first
copies the entire incoming velocity vector into a real local, then updates
vertical velocity and integrates position from the saved components.
The acceleration term retains the original left-associated float32 sequence:
`((0.5f * acceleration) * timestep) * timestep`, not a reassociated
equivalent over real numbers.

Both original calls, at **15199AF0** and **15199FC0**, pass position and the
velocity vector at position + C, with acceleration/timestep float bits in
a2/a3. Neither consumes a return value. The second setup explicitly retains
a1 = a0 + C through its component initialization and scalar captures.
The source/header search finds no existing C caller/prototype needing an ABI
change: those original callers are still unrecovered assembly-side bodies.

## Qualification

[The experiment and production gates](../../tools/experiments/game_kinematic_step.py)
reuse existing compiler, object, padder, ELF, data-layout and original-assembly
helpers. [Seven focused tests](../../tools/tests/test_game_kinematic_step.py)
reuse the existing MIPS floating-point/word-memory engine rather than adding
a new interpreter.

**Seven pre-install and seven installed tests pass in both copies**, with
zero errors/failures/skips:

| Stage | Primary | Standalone Tools Mirror |
| --- | ---: | ---: |
| Pre-install | 17.650s | 17.946s |
| Installed | 24.934s | 7.563s |

- **263 cases / 526 stack phases** compare public outputs and all ordered
  public reads/writes to an independent float32 reference. The compiled C
  and original agree on full modeled GPR/FPR/condition/lo/private/public RAM,
  access/call histories and visited instruction addresses. All **39 original
  words** execute.
- **290 physically overlapping guest phases** cover same-vector and partial
  overlaps. The **147 native cases** use only valid same or separate complete
  vector elements, not partial overlapping-struct assumptions.
- Those 147 native32 fixtures pass **O0/O2/O3** with SSE float32 evaluation,
  contraction disabled and trap-mode UBSan. Signed zero, negative/zero/fractional
  timesteps, rounding-sensitive terms and deterministic finite random values
  are included.
- Five separately compiled semantic controls return the expected mismatch:
  use live rather than copied velocity, omit its update, use full rather than
  half acceleration, reverse the velocity acceleration sign, or reassociate
  the float32 polynomial. The actual installed-predecessor stub is also an
  effective guest-state negative.
- Three independently GNU-linked code rebases, with independently relocated
  argument buffers, pass **24 modeled phases** against the independently
  assembled original. There are no symbolic bindings or LO16 carries in
  this leaf to normalize or pretend to qualify.
- Eight wrong-image controls reject altered headers, target/neighbor bytes,
  symbol extent, truncation and appended bytes.
- Two task files agree byte-for-byte between copies, four Python copies parse,
  and both project-tools checks pass.

The float reference covers the stated finite domain. Full hardware FCSR/MMU,
NaN/exception environments, unrestricted pointer validity and whole-game/
host-port acceptance are not claimed. Guest partial-overlap probes are not
portable-C alias guarantees. Exact instruction identity is separate from a
new connected-caller or gameplay qualification.

## Owner, Make And Full Image

Both raw owner versions preserve all **68 other bodies and pools**.
Actual padding retains every owner address and every other extent/pool, while
changing only the target symbol size **12 to 156 bytes**.

The expanded, unchanged Make rule executes its actual **three productive
commands**: normal O2/g3 compilation, existing padding and GNU assembly.
Its raw functions and linked padded code/metadata equal the independent
qualification objects. Cleanup is intentionally skipped only in the shadow.
The inherited duplicate-rule warning for generated_12D630 is recorded,
not attributed to this source change.

The actual production build succeeds in **23.396s** and exactly reproduces
the independently predicted complete ELF:

- **120 changed bytes**: **119 target instruction bytes** and **one target-size
  metadata byte**. There are no symbol-order permutations or metadata exclusions.
- Every **6,056 other linked body**, all **6,057 function addresses** and
  all **189,088 protected Game-data bytes / 720 owners** remain fixed.
- The entire guard manifest, original assembly, Makefile, ROM and progress CSV
  are byte-identical. This replaces already-counted C, not a new conversion row.
- Installed tests validate the strict current source/image against frozen
  predecessor snapshots. No historical fingerprint is rewritten to accept
  the recovery. Prior unchanged neighbor suites are reused through exact
  whole-image preservation, not reported as fresh broad tests.

## Counts And Next Work

Fresh matcher: **Game 3,021/4,832 (62.52%)**,
**overall 3,694/5,505 (67.10%)**, **1,811 different / zero drift**.
Init remains 492/492 exact and Debugger 181/181 exact.
Root README receives aggregate table updates only.

The 75% threshold at denominator 5,505 remains **4,129 exact functions**;
**435 further matches** are needed. Recompute if the denominator changes.
The refreshed ELF-pinned queue has 1,676 simple zero-return placeholders,
126 semantic/other definitions and nine not located by the source-shape
screen. Those are triage categories, not ABI/semantic qualification.

Next short placeholder: **func_150BA4C0**, 39 words, generated_E7970.
Its complete original body has been read. An ignored first C draft already
matches **39 words/frame 72 with zero differences/diagnostics**, but is
**not installed and earns no match credit**. It captures a source pointer,
source byte 3B and zero float, requests a randomized effect and conditionally
copies 12 payload bytes to effect + 28. Before qualification/import, audit all
callers/return use and the three locally unwritten payload bytes at offsets
5..7, represented as struct padding in the draft and copied by memcpy. Do not
silently initialize them or claim portable C equivalence for arbitrary guest
aliases.

The existing semantic 39-word func_15070C40 remains another short candidate.
The larger func_1508CAD8 (862 words) still remains the other B3020 owner stub.

## Preservation And Receipts

All **1,470 pre-existing dirty mirror paths/statuses/hashes** and HEAD
`ddbdd16b` are preserved. Only two absent task files are added; final dirty
paths **1,472**. No mirror commit/reset/stash/clean, push, dependency/compiler
change, advisory writer, host/frozen Release operation or save/config change.

```text
Direct C code: bb8182b9e84050b6ec032736c6a2d0f747be0a363fd4db7c474d01e8712b5a5d
Installed C:   e1f98784ff6a8b5d87ec9f3c63cbd8344010349de2b6459e399b2c253ae4c778
Linked ELF:    e4eaf78905135b93afb7efa7e88ae3e5f9fcaf2226f1d91e7b98c809c0565fe7
Guards fixed:  7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
```

Ignored receipts: `conker/build/game-kinematic-step/qualified/`.
These include primary/mirror pre-install and installed logs/JSON, native builds,
independent original/rebase objects, actual owner/Make/padding/first-link/build/
installed/data audits, fresh matching/75%-queue evidence, mirror preservation
and graph before/after closeout. The next non-installable draft is under
`conker/build/game-effect-payload-spawn/screen/`.
Graph closeout follows the consumer commit. The wider 75% goal stays active.
