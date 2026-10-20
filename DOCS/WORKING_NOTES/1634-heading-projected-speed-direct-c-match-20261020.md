# Heading-Projected Speed Direct C Match

Date: 2026-10-20. Consumer predecessor: `5faa4bd1`; tools predecessor:
`2a385cc`. Tools **55e2533** are committed first. No push.
This completes the seven-difference draft from
[Note 1633](1633-record-effect-payload-pointer-return-direct-c-match-20261020.md).
Both the preceding and current goal turns make verified progress.
The wider **75% total C-matching objective remains active**, not complete.

## Installed Recovery

Replace `func_15116888`'s false zero-return body in
[generated_142560.c](../../conker/src/game/generated_142560.c) with the complete,
typed, purpose-commented routine, retaining its original name.
VA **15116888..15116924**, ROM **143D38..143DD4**.
All **39 words / 156 bytes / frame 64** emit directly from normal **IDO O2/g3**,
with **two original call bindings, zero new guards and no profile/Makefile
change**.

The recovered interface is
`s32(s32 originX, s32 originZ, void *unused, void *actor)`.
Truncate the actor's float X/Z at 14/1C to signed words first. Form signed
modulo-word differences from the origins and convert them back to float in
the canonical `struct17` vector. The middle float is deliberately locally
unwritten. Call the heading helper, then read the facing halfword at 76,
compute `64 - (facing >> 8) - heading` and pass its low byte to the scale
helper. Read the actor's speed at 3C **after** that second call, multiply as
float32 and truncate the projected result to a signed word.

Use [the existing struct17 type](../../conker/include/structs.h), not a
parallel vector definition. Its shared header is pinned and unchanged.
Both helper prototypes now use their actual existing interfaces:
`s32 func_150490A8(struct17 *)` and `f32 func_15048A40(u8)`.

## Closing The Seven Differences

The initial complete expression was reassociated by IDO into negate/subtract/
add operations. Splitting the complement and heading subtraction restores
the retail instruction schedule. Loading the facing halfword into that same
named result before shifting removes a temporary register, restoring the
remaining six register words.

Every real local has a semantic use: captured/truncated coordinates, modular
delta, facing, heading, scale, canonical vector and projected float. Existing-
local ordering recovers SP+1C and frame 64. No padding, unused locals, register
bindings, volatile qualifier, frame guard or assembly substitution is added.

## Actual Caller And Helper Bounds

The full pristine US Init/Game/Debugger scan finds one direct JAL:
**func_1511650C at 1511654C**. The original 223-word caller:

- Gates the call on its record's byte 4F bit 4.
- Passes signed halfwords at record +10/+14 as the two origins.
- Passes record +7C as an **unused context pointer**, not an integer quantity.
- Passes the global actor at D_800CC2D0 as the fourth argument.
- Arithmetic-shifts the signed returned word right by three before continuing.

Check the exact twelve-word argument/gate/return window. The caller remains
an unrecovered stub: this is **static ABI evidence, not full caller execution**.
There is no existing C call requiring another source-owner edit.

All four actual math helpers are already byte-exact and remain unchanged:

| Helper | Words | ROM |
| --- | ---: | --- |
| func_150490A8 | 40 | 76558 |
| func_15048864 | 25 | 75D14 |
| func_15048A40 | 12 | 75EF0 |
| func_150489B0 | 36 | 75E60 |

The 25-word lookup reads an **unsigned halfword**, shifts it right by ten,
then returns either that value or `255 - value` as an exact integer-valued
float. Its ranges are 0..63 or 192..255. The heading routine's zero-vector
return and positive-Z transforms preserve the enclosing **0..255** bound.
This is derived from the complete original instruction flow and unsigned
load, not assumed from a helper name or sampled min/max alone.

The facing high byte is 0..255, so the staged signed angle intermediates are
within **-446..64**. No signed overflow is required there. Coordinate
differences instead retain explicit unsigned-word arithmetic followed by the
target's signed-word interpretation. Valid float-to-int inputs and final
products are constrained to finite signed-word range.

## Fresh Qualification

[The integration helper](../../tools/experiments/game_heading_projected_speed.py)
reuses existing compiler, independent original assembler, object/pool parser,
padder, actual Make, linker and protected-data gates.
[Eight tests](../../tools/tests/test_game_heading_projected_speed.py) reuse
the existing MIPS runner, extending only the scalar sqrt/abs/neg/trunc patterns
already used by sibling math oracles. Standard-library sqrt plus explicit
float32 rounding is a bounded model, not a new hardware emulator.

**Eight pre-install and eight installed tests pass in both copies**, with
zero errors, failures or skips:

| Stage | Primary | Standalone Tools Mirror |
| --- | ---: | ---: |
| Pre-install | 22.369s | 27.475s |
| Installed | 17.698s | 19.981s |

- **392 cases / 784 modeled phases** compare independently described ordered
  accesses, helper arguments, public state and return, plus literal full modeled
  GPR/FPR/condition/HI/LO, private/public RAM, histories and visits.
- Exercise all **256 scale arguments**, coordinate truncation before subtraction,
  signed zero, fractional coordinates, signed-word extremes and wraparound,
  halfword high/low bytes, heading boundaries and float32 product truncation.
- Callback-boundary writes change coordinates/facing/speed after capture.
  Physical guest-only writes switch the actor incoming home after either
  helper and alter finished origin/unused homes. The target follows the actual
  late actor/facing/speed reloads; these probes are not portable-C alias claims.
- The vector's real middle word at SP+20 remains its incoming stack bytes;
  observe it without inserting an own read into the target. Native helper
  contracts read only the initialized X/Z fields.
- **738 additional phases execute the original four-helper chain**, with the
  original frozen math-table bytes. **736 actually enter the lookup**; two
  zero-vector phases correctly skip it. All **113 helper words** and all 39
  target words execute across the corpus.
- An independent higher-level float32/table reference agrees with the original
  chain, including all scale quadrants and zero-vector handling. Frozen table
  bytes remain unchanged; observed headings span 0..255.
- **386 native32 cases** pass O0/O2/O3 with trap UBSan and contraction disabled.
  Inputs have real typed float/halfword subobjects, the vector's existing
  three-float layout is mirrored explicitly, and field/output fences are
  checked. Integer-to-pointer conversion for the unused context is restricted
  to the existing 32-bit test ABI; it is never dereferenced.
- **Nine compiled semantic controls** fail with the expected mismatch:
  floating subtraction before coordinate truncation, wrong Z, early facing,
  early speed, low facing byte, wrong heading direction, next scale entry,
  addition instead of multiplication, or biased final truncation.
- **Eight guest negative phases** reject zeroing the middle vector word or
  prematurely caching the actor across a fired incoming-home change, with
  both modeled and original helper routes. The negative's volatile cached
  pointer is a test witness only, not a recovered production qualifier.
- **Three independent GNU code/helper rebases** and moved actor buffers pass
  **24 phases** against independently assembled original code. Both call
  bindings remain correct; there are no data bindings in the target itself.
- **Eight strict-image controls** reject corrupted headers, target/neighbor
  bytes, symbol size, truncation and appended bytes.
- Both task files agree across copies; all four Python copies parse and both
  existing project-tools checks pass. No Claude call was needed.

Native math providers are bounded argument/result/mutation contracts, not
native executions of the complete SDK. The guest chain executes the actual
113 words with the supplied data. Hardware FCSR/MMU, out-of-domain conversions,
arbitrary fault-prefix parity, full caller/gameplay and host-port acceptance,
and portable-C physical parameter aliases or unwritten float values remain
separate.

## Owner And Exact Production Image

Preserve all **83 other owner functions** and pools. Its ten existing
GLOBAL_ASM entries remain in the normal preprocessing path. The actual shadow
uses **five productive Make commands**, with unchanged O2/g3 and no new
compiler diagnostics; raw/padded code and metadata agree with independent
qualification. The known duplicate generated_12D630 recipe warning remains.

The production build exits zero in **22.454s** and reproduces the whole-image
prediction exactly:

- **121 changed bytes**: **120 target instruction bytes**, **one target-size
  byte**, extent **12 to 156**.
- No metadata cycle, excluded section/range, guard or profile change.
- All **6,056 other linked bodies**, all **6,057 addresses**, and all
  **189,088 protected Game-data bytes / 720 owners** remain fixed.
- ROM, original assembly, the shared struct header, full guard manifest,
  Makefile and progress CSV stay byte-identical. This repairs already-counted C,
  not a conversion row.
- Installed tests audit the live source/image before using immutable
  predecessor fixtures. Historical pins are not advanced to accept the body.
  Unchanged broad neighbor suites are reused through whole-image preservation,
  not described as freshly rerun.

## Counts And Next Function

Fresh full matcher: **overall 3,699/5,505 (67.19%)**,
**Game 3,026/4,832 (62.62%)**, **1,806 different / zero drift**.
Init stays 492/492 exact; Debugger stays 181/181 exact.
The present 75% threshold is **4,129**, requiring **430 further matches**.
Recompute if the denominator changes. Root README receives aggregate rows only.

The refreshed ELF-pinned queue uses fresh full instruction classification
and reuses only source-shape entries protected by the strict source/whole-
image proof. Exactly this newly exact entry is removed:
**1,671 placeholders, 126 semantic/other and nine unlocated entries**.
These are triage categories, not qualification.

Next related short fit: **func_15070C40**, game_981E0,
VA **15070C40..15070CDC**, ROM **9E0F0..9E18C**.
It already has semantic C; the initial isolated body is 40 words and seventeen
differences. Expressing the selected actor directly as a conditional helper
argument produces an isolated **39-word / frame-64 exact draft**, without
diagnostics. It is **not installed and earns no credit**. Qualify its captured
three-float position, one-based actor selection and valid index domain, helper
wire contract/callers, private storage, full large owner and actual Make/image
before installing. Preserve the existing canonical structs/prototype.
Keep func_151BB044 and the 862-word func_1508CAD8 queued.

## Preservation And Receipts

Preserve all **1,480 pre-existing dirty mirror paths/statuses/hashes** and HEAD
`ddbdd16b`. Add only two absent task files, leaving **1,482 dirty paths**.
No mirror commit/reset/stash/clean, push, dependency/compiler installation,
advisory writer, host/frozen Release build/launch or save/config changes.

```text
Raw C:      df612e007f52979d28c4e7fbe5dfad60e89bccf6171133743112b25d24734b26
Linked ELF: 69b7bb9032dcf6d3c48b8e131d24e91b6da6fc96219252b6e551f48fb1e49e87
Structs:    081b0f0bd0f86173c34674f1d1434a9a09a6f59e6e05d5fa375613afbed7be69
Guards:     7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
```

Ignored receipts: `conker/build/game-heading-projected-speed/qualified/`
contains primary/mirror suites, native controls, original/rebased objects,
caller static disassembly, actual owner/Make/image/live/data audits, production/
progress/queue, mirror preservation and post-commit graph closeout.
Next uninstalled screen: `conker/build/game-owner-position-dispatch/screen/`.
The wider 75% goal remains active.
