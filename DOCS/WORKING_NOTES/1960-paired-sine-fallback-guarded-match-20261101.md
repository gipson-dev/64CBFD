# Paired sine fallback recovered as byte-exact guarded C

Verified 2026-11-01. `func_1511C548` replaces its zero-return placeholder
with the complete paired sine output and phase callback. All **60 retail
words match** with two checked independent scheduling guards. Ordinary C
already supplies the original 40-byte frame, saved first result, complete
arithmetic, calls and branches. No profile changes or volatile filler are used.

Fresh production and independent Native actual-ELF recount report
**4,030/5,507 (73.18%)** total and **3,357/4,834 (69.45%)** Game, zero address
drift and 1,477 different. Init remains 492/492 and Debugger 181/181.
Converted inventory remains 5,507/6,045, Game 4,834/5,324. The 75% threshold
is 4,131: **101 additional exact C functions are needed**.

## Routine, interface and live inputs

- Source `conker/src/game/generated_142560.c`; owner `generated_142560`.
- Original assembly `conker/asm/142560.s` is retained unchanged.
- VA `0x1511C548..0x1511C638`; ROM `0x1499F8..0x149AE8`.
- 240 bytes / 60 words, frame 40, ten relocation bindings.
- Correct interface `void func_1511C548(u8 *state)`; callers ignore the result.

The first `sinf` receives phase `+0x80`; its result survives the second sine
call on live phase `+0x84`. Both results are scaled by 16 and stored at
`+0` and `+8`. The first phase advances by `D_800A31EC * D_800BE9A4`;
the second advances by `D_800A31F0 * D_800BE9A4`. The clock is float, and
its second read follows the first phase store. Coefficients have retail
bits `0x3D958106` and `0x3D851EB8`. Keep both live accesses and their order.

Each phase is then passed through `func_15144B68`. The second phase must be
reloaded after the first wrap call. The helper subtracts its bound only when
strictly above it, then adds the bound while negative. Equality with the bound
is retained; this is not a modulo operation.

After both wraps, live output `+8` and phase `+0x84` are compared with zero.
Only when both compare equal are outputs replaced by **7.5f and 8.0f**.
Both signs of zero satisfy the comparisons. Helper effects can change the
outputs and phases, so entry snapshots cannot replace these final reads.
An early source screen misread the first fallback as 7.0f; raw comparison
caught it before guards or installation. The corrected semantic constant is
also protected by an effective compiled negative control.

## Compiler shape and two guards

Reversing the declarations of the two ordinary float locals recovers the
retail saved-result slot at `SP+0x20`, retaining the 60-word/40-byte shape.
The two remaining differences are an independent store/load exchange:

| Offset | Raw C | Retail |
| --- | --- | --- |
| `0x98` | `LWC1 F6, +8(S0)` | `SWC1 F0, +0x84(S0)` |
| `0x9C` | `SWC1 F0, +0x84(S0)` | `LWC1 F6, +8(S0)` |

The addresses are disjoint and the FP registers independent. No arithmetic,
branch, call, binding or memory value changes. The guard derivation checks
the complete raw payload and all ten bindings before exchanging these two
words; corrupt payloads, missing bindings, repeat installation and stale
expected guard words reject. All predecessor guard bytes remain intact;
exactly two rows append. Raw SHA-256:
`0d4b5aed919b64674400df4ed806030c72cd50bc655dca5f84184ed5a3baf5f9`.

## Runtime and original caller qualification

- **6,144 guest cases / 30,720 executions**, three symbol layouts, four global
  alias arrangements and two stack phases. Providers mutate phases, outputs,
  coefficients and clock while clobbering caller-saved registers and outgoing
  argument homes. Both fallback outcomes and all 60 root words execute.
- Original ASM, padded owner, actual Make and guarded isolated C have equal
  complete modeled states and access traces. Unguarded C has equal public
  memory and preserved ABI state, allowing the independent access order.
- **97 fault prefixes / 388 executions** agree across the four exact programs.
  This qualifies guest instruction order, without a portable-C/raw-C fault-order claim.
- **1,024 connected cases / 5,120 executions** run the original 104-word sine
  and 24-word wrap routines, pinned against ROM and baseline ELF, using their
  pinned constants. The finite corpus reaches 93 sine words and all 24 wrap
  words and agrees with independent polynomial and bounded-wrap references.
  Full FCSR behavior, arbitrary NaN payloads and unbounded wrap inputs are
  outside these tests.
- Both original JALR sites `0x15113EE8/0x15113FC0` execute their complete
  seven-/nine-word windows: **96 cases / 480 executions**, four result poisons.
  S0 is passed as A0; the result is ignored. The larger dispatcher is bounded.
- The original **22-word installer** at `0x1509EBBC` installs row 14 of
  `D_80088C90`, callback `+0x38`, zero secondary callback `+0x78` and zero
  mode byte `+0x92`. All installer words execute. Census finds a sole aligned
  pointer at ROM `0x22D7F8`, VA `0x80088D38`, and no direct JAL/J to this root.
- Native C passes **2,048 cases per profile** at O0/O2/O3 with UBSan and full
  record canaries. Eight compiled controls are effective: wrong first phase,
  lost first result, wrong output amplitude, entry-cached clock, wrong first
  coefficient, missing second wrap, incorrect OR gate and 7.0f fallback.

Native globals are disjoint; global aliases are guest-qualified. Hardware
and gameplay acceptance are outside the byte-matching tests.

## Owner, literal image and production

All 83 raw/padded neighbor functions and normalized pools remain fixed;
owner warnings remain zero. The actual five-command Make recipe yields the
independently qualified object under the existing O2/g3/mips2/o32 profile.

The literal entire-ELF prediction matches first link and production at
**205 changed bytes**, with zero excluded bytes. It updates the target slot,
its symbol extent from 12 to 240, and one closed GNU symbol serialization
pair: `D_800C6360` and `D_8009E6A0` exchange row/name order while retaining
their complete named definitions. The predictor checks the complete old rows
and strings before predicting every changed metadata byte. Negative controls
in text, symbol metadata, string metadata and unrelated image bytes reject.
All 6,056 function addresses, 6,055 other bodies and 189,088 protected Game
bytes across 720 owners remain fixed. Production ELF SHA-256:
`8c16588be8f17bc8b6c570cf5962fe5353055af3a71d7259b915cd2085b4dc84`.

Production Make, the 17,600 predecessor sealed inputs, six public tests per
tools copy before and after adoption, both shared checks and independent
Native recount pass. Only the source, owner object, guard CSV and ELF change;
no dependent object, shared header or Makefile changes occur. Reusable modules:
`game_paired_sine_fallback_match.py`, `game_paired_sine_fallback_oracle.py`,
and `test_game_paired_sine_fallback_match.py`. Existing mirror dirty work is
preserved; only these three identical owned modules are added there.

## Continuation

Evidence is self-contained under
`conker/build/game-paired-sine-fallback-1511C548-match/`: 1,045 frozen focused
inputs, 24 canonical artifacts, early source screens, original helper/caller
execution, closed guard derivation, exact metadata prediction, production
and bank receipts. Historical archived checkpoints require explicit restoration.

Next audit `func_1511AF30`, the 83-word callback in the same owner at
VA `0x1511AF30..0x1511B07C`, ROM `0x1483E0..0x14852C`. Inspect its 32-byte
frame, signed command conversion, one-unit approach, strict absolute-delta
gate, random remainder path, saved conversion lifetime and filtered output.
No next-target credit. Other private candidates remain uncredited. Commit
tools before the consumer pin; no push. Root README gets aggregate rows only.
The wider 75% goal remains active.
