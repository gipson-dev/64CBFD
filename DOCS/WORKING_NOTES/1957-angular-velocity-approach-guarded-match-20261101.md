# Three-axis angular velocity approach recovered as byte-exact guarded C

Verified 2026-11-01. `func_15116D7C` replaces its zero-return placeholder with
the complete three-axis angular-velocity approach and angle update. All
**74 retail words match** with fourteen checked words for a closed register
remap and independent opening schedule. No compiler profile changes,
insertions, omissions or volatile filler are used.

Fresh production and independent Native actual-ELF recount report
**4,027/5,507 (73.13%)** total and **3,354/4,834 (69.38%)** Game, zero address
drift and 1,480 different. Init remains 492/492; Debugger remains 181/181.
The converted C inventory stays 5,507/6,045, Game 4,834/5,324. The 75%
threshold is 4,131: **104 additional exact C functions are needed**.

## Routine and semantics

- Source: `conker/src/game/generated_142560.c`; owner `generated_142560`.
- Original ASM retained: `conker/asm/142560.s`.
- VA `0x15116D7C..0x15116EA4`; ROM `0x14422C..0x144354`.
- 296 bytes / 74 words, no stack frame, two HI16/LO16 bindings to
  `D_800BE9E4` at offsets `4/8`.
- Recovered interface: `void func_15116D7C(u8 *state)`; A0 is the record
  pointer. Original callback continuations ignore the result register.

The signed full 32-bit field at `+0x3C`, converted to single precision and
multiplied by `1/256`, supplies a per-call approach step. The signed global
tick count is converted separately and captured before the loop. Each of
three velocity floats at `+0x60/+0x64/+0x68` approaches its corresponding
target at `+0x7C/+0x80/+0x84`, with a store/reload and overshoot clamp in each
direction. The approach step is not multiplied by ticks. Negative steps
retain retail's behavior rather than being sanitized.

Each angle at `+0/+4/+8` then receives `velocity * ticks`. A negative result
gets one addition of 360; otherwise a result at least 360 gets one
subtraction. This is a single correction, not modulo or repeated wrapping.
Integer conversion, float rounding, equality and branch order are retained.

## Closed compiler differences

The natural candidate already has 74 words, all arithmetic and all branches.
The best declaration/do-while shape reduces the initial forty differences
to fourteen. A checked transformation independently derives the guard rows:

- During the loop, raw V0 (counter) maps to retail V1, raw V1 (angle cursor)
  maps to A3, and raw A0 (loop bound) maps to V0. Velocity and target cursors
  remain A1/A2. This map applies after the incoming A0 record pointer is used.
- Counter initialization and angle capture exchange their independent slots;
  both pointer initializers remain fixed and capture the original argument.
- The independent opening velocity/target loads exchange slots. Equality's
  two FP operands exchange spelling without changing the comparison.

Raw payload SHA-256:
`19a4a4eac9c99cc627d5e8cfa760e88a85fb7ba3f7cfae38e76e59df22eba0ea`.

The normalized raw payload is pinned before relocation. The actual assembler,
padder and GNU links separately verify retail at three symbol layouts.
Fourteen manifest rows are appended; every predecessor byte is retained.
Corrupted payloads, bindings and expected guard words fail closed.

## Semantic, caller and native qualification

- **4,608 guest cases / 23,040 executions** compare original ASM, qualified
  padded owner, actual Make object, guarded isolated C and unguarded isolated
  C at three address layouts. The first four have equal complete modeled
  state and traces; unguarded C has equal public memory and preserved ABI
  state, allowing its different caller-saved temporaries.
- Cases cover signed step/tick extremes, equality, both approach directions,
  both clamps, signed zero and all wrapping branches. Three global layouts
  put the tick word separately, on angle zero, or on velocity zero, verifying
  that its initial value remains captured through all three axes.
- All **72 reachable words** execute. The remaining two words, offsets
  `0xA0/0x100`, are retail duplicate operations skipped by the branch-likely
  schedules. They are still present and byte-exact in the complete slot.
- **109 access prefixes / 436 executions** preserve complete states across
  the four exact programs. No equivalent unguarded-C fault-order claim is
  made. These are guest instruction-order checks, not portable C faults.
- Both original indirect call sites, JALR at `0x15113EE8` and `0x15113FC0`,
  run through their complete seven- and nine-word windows: **128 cases /
  640 executions**, five programs and four result-register poisons. Both pass
  S0 as A0 and ignore the result while their original continuations execute.
- The original **22-word callback installer** at `0x1509EBBC` installs row 75
  of `D_80088C90`: the callback at record `+0x38`, zero at `+0x78`, and mode
  byte zero at `+0x92`. All installer words execute. The aligned ROM census
  finds one pointer at `0x22DAD4`, VA `0x80089014`, and no direct JAL/J.
- Native C passes **2,048 cases per profile** at `-O0/-O2/-O3`, with 32-bit
  SSE single precision, disabled contraction, UBSan and full record canaries.
  Eight compiled controls are effective: unsigned step, step multiplied by
  ticks, wrong step factor, either missing clamp, wrong axis count, wrong wrap
  equality, and reversed angle direction.

Native cases use disjoint globals; global aliases are guest-qualified. Full
FCSR behavior, arbitrary NaN payloads, complete execution of the larger
dispatcher and hardware/gameplay acceptance are outside these bounded tests.

## Owner, production and complete image

All 83 other raw and padded functions and normalized pools are unchanged;
owner warnings remain zero. The actual five-command Make recipe produces
exactly the independently qualified object with ordinary O2/g3/mips2/o32.
No shared headers, Makefile or neighboring source routines are changed.

The independent entire-ELF prediction changes only the target slot and its
symbol size, from 12 to 296 bytes. The complete first link and production
image match at **187 changed bytes**, with zero exclusions or metadata
serialization exceptions. All 6,056 function addresses, 6,055 other bodies
and 189,088 protected Game bytes across 720 owners remain fixed.

Production ELF SHA-256:
`ef752d6de30fdb6cd6b23a51a476140e6fac2238a1686819edc572d4eb6f6664`.

Production Make, all 17,579 predecessor sealed inputs, six public tests per
tools copy before and after adoption, both shared tool checks, and the fresh
Native recount pass. Only source, its object, guard manifest and ELF change;
no dependent objects change. The reusable tools are
`game_angular_velocity_approach_match.py`,
`game_angular_velocity_approach_oracle.py`, and
`test_game_angular_velocity_approach_match.py`. The older tools mirror receives
only those three identical new modules; its previous dirty work is preserved.

## Continuation

Evidence lives in `conker/build/game-angular-velocity-approach-15116D7C-match/`:
1,031 frozen focused inputs, 24 canonical preparation artifacts, runtime,
caller, guard derivation, production, installed audit and bank receipts.
Early failed fixtures are retained: one screen generated a statement before
C89 declarations, and the first guard-proof check compared unrelocated raw
words to linked addresses. Corrected proofs keep HI16/LO16 bindings explicit.

Next audit `func_1511617C`, an 86-word placeholder in the same owner. Inspect
its saved coordinate, `func_1510F648` call and halfword output behavior before
conversion. Other private candidates remain uncredited. Tools are committed
before the consumer pin; no push. Root README contains aggregate rows only.
The wider 75% goal remains active; no host port, editor or Release changes.
