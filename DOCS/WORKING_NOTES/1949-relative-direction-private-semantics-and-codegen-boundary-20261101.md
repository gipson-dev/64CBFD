# Relative-direction candidate: semantics qualified, compiler mismatch remains

`func_1506B3B8` now has a privately qualified C reconstruction. It retains
retail's **77 words and 32-byte frame**, but **36 real words still differ**.
Separating the signed heading byte from its unsigned magnitude improved the
previous best result from 48 differences. No production source, guards,
compiler profile, tools pin, or aggregate matching credit changed.

Production remains **4,021/5,506 (73.03%)**, Game **3,348/4,833 (69.27%)**,
Init 492/492 and Debugger 181/181, zero drift, 1,485 different. **109 more**
exact functions are required for the active 4,130/5,506 threshold. These are
the prior bank's counts: this checkpoint preserves its ELF and source bytes,
and does not claim a new production build or recount.

## Recovered operation

Owner/source: `game_981E0`, `conker/src/game_981E0.c`.
VA **1506B3B8..1506B4EC**, ROM **98868..9899C**, 308 bytes.
The intended interface is `void func_1506B3B8(void)`. The existing integer
placeholder and obsolete commented draft remain untouched pending adoption.

1. Initialize a local choice byte to zero. Compute pool-slot-zero X minus
   current-actor X, and current-actor Z minus pool-slot-zero Z.
2. Call `u16 func_1505A630(f32, f32, s32)` with those two hard-float arguments
   in f12/f14 and zero in a2. The recovered helper body converts the offset
   to a 16-bit angle; the qualification uses an adversarial provider rather
   than claiming connected atan2 or hardware floating-point acceptance.
3. Reload the current actor after the helper. Compute the signed 16-bit
   difference `unk7A + (unk1FD << 8) - returnedAngle`. The high signed byte
   determines the side. Fold its unsigned representation to a magnitude in
   0..128; high byte 0x80 folds to 128, not zero.
4. Compare magnitude strictly with the byte at D_80099A3C. Below it selects
   entry 1. Otherwise use entry 5 when the byte at D_80099A43 is strictly
   smaller than magnitude, entry 2 when the byte at D_80099A3E is strictly
   smaller, or the initial zero. Add four for negative direction and three
   otherwise, with byte wrap. The normal reachable indices are 1,3,4,5,6,8,9.
5. Clear the captured post-helper actor's byte +0x138. Then fetch the chosen
   **byte** from the D_80099A3C table. Reload the current actor for the +0x244
   halfword store, reload it again, and set +0x21C to 20000. These live loads
   and access ordering are retained.

The shared table declarations retain their legacy s16 views. This private
body uses explicit byte views; no speculative shared-header repair was made.

## Measured qualification

- **6,148 guest cases / 12,296 executions**, original and fresh candidate,
  across retail plus two rebased layouts with low-half carry boundaries.
  Retail has 4,100 cases; each other layout has 1,024 boundary cases.
- Every high heading byte, four low-byte boundaries at retail, four threshold
  arrangements, offset wrap, positive/negative boundaries, both stack phases,
  helper return upper-bit poison, current-actor retargeting and post-helper
  actor/table mutations are covered. Four float-edge cases add signed zero,
  subnormals, overflow and NaN-class observations; this is model evidence,
  not hardware FCSR evidence.
- Public memory, the helper's raw float/integer arguments, public access
  traces, and saved GPR/FPR values agree. **All 76 reachable words** execute
  in both programs. The unreachable duplicate at relative **+0xFC** remains.
  Private stack layouts differ, so complete machine-state identity is not
  claimed.
- Native **O0/O2/O3 each pass 4,096 cases with UBSan** and background
  canaries. All seven negative controls are effective: stale actor, inclusive
  threshold, wrong side increment, ignored heading offset, missing magnitude
  fold, halfword table lookup, and wrong timeout. Native fixtures seed the
  overlapping table labels consistently as separate C globals; guest tests
  supply their actual overlapping addresses.
- The complete original eight-word wrapper `func_1506B4EC` is connected to
  each body in **88 cases / 176 executions**, with identical public results,
  helper observations, access traces and saved registers.

The complete aligned ROM census finds one direct JAL, ROM **989A4** inside
that wrapper, and one pointer literal, ROM **22AE48** / VA **80086388**,
which is **D_8008630C[31]**. This table is used by `func_1505E0C4` to install
an action callback; it is not the D_800863FC dispatcher used by recent targets.
The original ten-word constructor window **1505E394..1505E3BC** passes its
null and slot-31 installation paths. The downstream indirect callback
invocation and complete constructor reachability remain unaudited.

Two caller harness setup errors (WindowCode owner/end initialization and an
unmapped output fixture) were corrected before the passing v23 run. Failed
v19/v20/v22 receipts remain available; they are not qualification receipts.
The first profile probe also exposed asm-processor flag restrictions; later
probes separate processor flags from actual compiler flags. Unsupported
compiler switches were rejected and never adopted or counted as successful
profiles. O1, O2 without g3, and no-unroll did not improve the best match.

## Compiler boundary and next work

The selected ordinary O2/g3 body has raw SHA-256
`767ed565fb82d88238a197d7231288c76ef00af3dbe1cc22e2000ebed41856af`.
The 308-byte retail slot is
`ae0be3144abf6933f86fafb0b14f6c505139cd51bf2e07c9efb21770e6546502`.
All three layouts have the same 36 different word positions.

The original choice byte lives at SP+0x19; this candidate uses SP+0x1F.
Retail retains an early table HI16 and uses a separate scalar threshold
load; the candidate shares a complete table base. Actor/pool register roles,
that address materialization, and surrounding schedules account for the
remaining measured differences. Source type/width, local choice lifetime,
byte table declaration/view, register hint and bounded profile probes are
retained; none is byte exact. No filler, volatile access or word guard was
introduced to force the result.

Next inspect CFE/UOPT local-home and address common-expression decisions
against this fixed semantic body. Preserve the signedHigh-to-byte conversion
that reduced the mismatch, and qualify each further source change with the
existing guest/native controls. Before adoption, also finish downstream
callback qualification, raw/padded owner and 327-neighbor checks, actual Make,
independent literal full-image prediction, protected data/addresses,
production checks, a fresh recount, documentation and graph banking.

## Retained evidence and commands

Private stage: `conker/build/game-relative-direction-1506B3B8-match/`.
The **1,011-input** snapshot, candidate C and object, original object,
`private-semantics-v16.json`, `private-native-v17.json`, `caller-census.json`,
screen matrices, versioned drivers and terminal receipts are retained.
Focused transport verifies selected evidence in Windows and the prepared WSL
cache; unsuccessful screen objects remain in WSL and are not all duplicated
into the recently cleaned Windows build folder.

From the consumer root, the versioned transport drivers reproduce the work:

```text
python -X utf8 conker/build/game-relative-direction-1506B3B8-match/run_cache.py DRIVER.py
python -X utf8 conker/build/game-relative-direction-1506B3B8-match/pull_focused_v21.py
```

Use a new driver version for another run: the launcher refuses to overwrite
an existing terminal receipt. Successful qualification drivers are v16
semantics, v17 native, and v23 callers. All have terminal exit zero.
The production ELF remains
`56dfb862d6a37ea40ec9e0bfdb47acc8a1d1faefbd4d69fdfa26afe27741e3d6`.
No Claude calls, host/editor changes, Release work or pushes were made.

## Frozen private candidate

This source is retained for review and continuation; it is not installed and
is not an exact C match.

```c
#include <ultra64.h>
#include "structs.h"
extern struct127 D_800CC2D0[26];
extern struct127 *D_800D154C;
extern s16 D_80099A3C[],D_80099A3E;
extern u8 D_80099A43;
u16 func_1505A630(f32,f32,s32);
/* Select a relative-facing table entry, restart it, and set the actor timeout. */
void func_1506B3B8(void) {
    u8 choice = 0;
    s16 difference;
    s32 signedHigh;
    s32 highByte;
    u8 magnitude;
    u16 angle;
    struct127 *actor;

    angle = func_1505A630(D_800CC2D0[0].x_position - D_800D154C->x_position,
                         D_800D154C->z_position - D_800CC2D0[0].z_position, 0);
    actor = D_800D154C;
    difference = actor->unk7A + (actor->unk1FD << 8) - angle;
    signedHigh = difference >> 8;
    highByte = signedHigh & 0xFF;
    magnitude = signedHigh;
    if ((highByte & 0x80) != 0) {
        magnitude = (u8)-highByte;
    }
    if (magnitude < ((u8 *)D_80099A3C)[0]) {
        choice = 1;
    } else {
        if (D_80099A43 < magnitude) {
            choice = 5;
        } else if (((u8 *)&D_80099A3E)[0] < magnitude) {
            choice = 2;
        }
        if (difference < 0) {
            choice += 4;
        } else {
            choice += 3;
        }
    }
    actor->unk138 = 0;
    D_800D154C->unk244 = ((u8 *)D_80099A3C)[choice];
    D_800D154C->unk21C = 20000;
}
```
