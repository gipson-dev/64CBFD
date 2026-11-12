# Type-0x64 timer callback: private semantic screen

Date: 2026-11-12. `func_151041E4` owns VA `0x151041E4..0x1510448C` and
retail ROM `0x131694..0x13193C`, 170 words. The production
`generated_131620.c` definition remains an `s32` zero-return placeholder.
The secondary callback walker work in [Note 2291](2291-game-secondary-walker-type-audit-20261112.md)
needs an interface compatible with this registered callback.

The retail routine consumes one record pointer. State 0 evaluates a selector
and either a height threshold of 19.0 or a timer; on activation it saves two
record pointers, sets a flag, starts audio and adjusts the owner's actor. State
1 increases a fade byte until it reaches 255, state 2 counts down a timer and
restores a flag/actor, and state 3 decreases the fade or releases the record.
The two actor-adjust transitions intentionally read their tag bytes from
different saved pointers. These are observed operations, not established
in-game names for every field.

The candidate below is **private and uncredited**. Its standard O2/g3 owner
compilation emits 168 words, with 130 positional differences against the
170-word retail slot; all three owner neighbors remained unchanged and both
compilation diagnostics were empty. A restricted insertion-aware alignment
screen found 89 guard rows and two insertions for this candidate. A scratch
screen of 24 uniquely named local-declaration permutations plus frame padding
found a best score of 80 rows and two insertions; those variants have not
received the complete semantic checks below. This score is only within the
screened alignment choices, not a proof of the global minimum or a qualified
guard mapping. The 72-byte retail frame was reproduced by a 16-byte unused
local in these variants, whose original purpose is unknown. An attempted
`-g0` route was rejected by the asm-processor invocation; it was not a valid
compiler-profile comparison.

The raw unpadded base candidate and retail were compared with an independent
model in 1,476 bounded guest cases across all four states, modeled helper
calls, threshold/timer boundaries, finite nonnegative tick values, a quiet
NaN, and helper-induced changes to saved pointers. The retail cases visited
169 of 170 instruction positions. A candidate with `height > 19.0` in place of
`>=` failed at the threshold. In separate SDK32 native tests, 192 modeled
cases passed at O0, O2 and O3 with undefined-behavior sanitization; the same
threshold mutation was rejected at each optimization level. The native test
checks selected record fields, pointer identities and modeled helper-call
arguments, not complete machine access ordering.

These screens do not establish arbitrary alias safety, portable behavior under
signed arithmetic overflow or invalid pointers, hardware FPU exceptions,
complete callback implementations, full caller/gameplay behavior, or a
byte-exact production image. The volatile height load reflects the retail
unconditional memory read but is still a hypothesis about the original C.
Helper prototypes and object types must be checked as the remaining callbacks
are recovered. The other registered callback `func_151AD174` also remains an
incompatible zero-return C placeholder. Do not install the walker solely from
this screen.

The scratch scripts and receipts are under
`conker/build/game-timer-callback-151041E4-screen/`; generated binaries and
candidate variants may be cleaned. The base candidate is retained here so the
semantic work can be resumed:

```c
#include <ultra64.h>
#include "structs.h"
extern s32 D_800BE9E4, D_800BEA08;
extern u8 D_800BEA0C;
void func_100176C4(void);
void func_10010F30(s32, u16, u8, s16, u8);
void func_1000E2F4(s32);
void func_151254F4(struct108 *, s32);
void func_151D66F0(s32, s32);
void func_1516972C(struct102 *);

/* Progress the type-0x64 record through its timer and fade states. */
void func_151041E4(u8 *record) {
    u8 *owner;
    u8 *other;
    u8 *actor;
    s32 trigger;
    s32 value;
    f32 height;

    switch (record[0x1A]) {
    case 0:
        owner = *(u8 **)(record + 0x10);
        actor = *(u8 **)(owner + 0x2D0);
        height = *(volatile f32 *)(actor + 8);
        trigger = 0;
        if (record[0x1C] == 0) {
            if (height >= 19.0f) trigger = 1;
        } else if (record[0x1C] == 1) {
            if (D_800BE9E4 < *(u16 *)(record + 0x18)) {
                *(u16 *)(record + 0x18) -= D_800BE9E4;
            } else trigger = 1;
        }
        if (trigger) {
            other = *(u8 **)(record + 0x14);
            owner = *(u8 **)(record + 0x10);
            record[0x1A] = 1;
            D_800BEA0C = 1;
            func_100176C4();
            func_10010F30(0x5B2, 0x7FFF, 0, 0, 0);
            func_10010F30(0x5B2, 0x7FFF, 0x7F, -100, 0);
            func_10010F30(0x5B2, 0x7FFF, 0, 0, 0);
            func_10010F30(0x5B2, 0x7FFF, 0x7F, -100, 0);
            func_151D66F0(0xD2, 2);
            func_151254F4(*(struct108 **)(owner + 0x318), other[0x13F]);
            *(f32 *)(*(u8 **)(owner + 0x318) + 0x674) = 0.0f;
        }
        break;
    case 1:
        value = record[0x1B] + D_800BEA08 * 10;
        if (value >= 255) {
            record[0x1B] = 255;
            record[0x1A] = 2;
            *(u16 *)(record + 0x18) = 180;
        } else record[0x1B] = value;
        break;
    case 2:
        if (D_800BEA08 < *(u16 *)(record + 0x18)) {
            *(u16 *)(record + 0x18) -= D_800BEA08;
        } else {
            owner = *(u8 **)(record + 0x10);
            D_800BEA0C = 0;
            func_1000E2F4(0);
            func_151254F4(*(struct108 **)(owner + 0x318), owner[0x13F]);
            *(f32 *)(*(u8 **)(owner + 0x318) + 0x674) = 0.0f;
            record[0x1A] = 3;
        }
        break;
    case 3:
        value = record[0x1B] - D_800BEA08 * 10;
        if (value <= 0) {
            func_1516972C((struct102 *)record);
            func_151D66F0(0, 0);
        } else {
            func_151D66F0((value * 210) >> 8, 2);
            record[0x1B] = value;
        }
        break;
    }
}
```

Next, improve the source/profile alignment without changing the observed access
and helper behavior, build and qualify durable guest/native tests with effective
controls, and reconcile the other callback's interface. Then run the complete
padder, caller, actual Make, independent whole-image, production and recount
gates before crediting a match. No production source, count or ROM changed in
this screen; the last verified Game checkpoint remains **3,705 / 4,840
(76.55%)**, 167 matches short of 80%.
