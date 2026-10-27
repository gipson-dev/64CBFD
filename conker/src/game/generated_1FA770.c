#include <ultra64.h>
#include "structs.h"
void func_1516972C(struct102 *);
typedef struct { s32 a, b, c; } ThreeWord1FA770;

extern ThreeWord1FA770 D_800AAF9C[];
extern f32 D_800BE9A4;

/* Non-matching placeholders for the text-only asm slice asm/1FA770.s. */

s32 func_151D10E4(u8 *, s32, u8);
void func_151D13E0(u8 *);

typedef struct {
    void *source;
    s32 value;
    s32 zero;
    u8 selector;
    u8 reserved[3];
} EffectRecordPayload;
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Capture record state, attach the payload and return the allocated effect. */
void *func_151CD2C0(void *source, u8 variant, s32 parameter) {
    u8 *effect;
    EffectRecordPayload payload;
    payload.source = source;
    payload.value = *(s32 *)((u8 *)source + 0x18);
    payload.zero = 0;
    payload.selector = *(s32 *)((u8 *)source + 0x1C);
    effect = func_15149130(300, -1, -1, -1, 0, 30, 16, variant, parameter);
    if (effect != 0) {
        memcpy(effect + 0x28, &payload, 16);
    }
    return effect;
}

void func_151CD35C(s32 arg0) {
    s32 value;

    if ((arg0 >= 0) && (arg0 < 4)) {
        value = arg0;
        func_151494E0(&value, 0x17);
    }
}

void func_151CD394(s32 arg0) {
    s32 value;

    if ((arg0 >= 0) && (arg0 < 4)) {
        value = arg0;
        func_151494E0(&value, 0x18);
    }
}

s32 func_151CD3CC() {
    return 0;
}

s32 func_151CD4C0() {
    return 0;
}

s32 func_151CD674() {
    return 0;
}

s32 func_151CD7BC() {
    return 0;
}

s32 func_151CDB94() {
    return 0;
}

s32 func_151CDE20() {
    return 0;
}

void func_151CE47C(u8 *arg0) {
    *(u8 *)(arg0 + 0x30) = 0;
    *(u16 *)(arg0 + 0x1E) &= ~2;
    *(u16 *)(arg0 + 0x1E) |= 8;
}

void func_151CE49C(u8 *arg0) {
    s32 value;
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    value = *(s32 *) (temp_v0 + 0x48);
    func_151494E0(&value, 0x23);
    func_151478F4(arg0);
}

void func_151CE4DC(u8 *arg0) {
    s32 value;
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    value = *(s32 *) (temp_v0 + 0x48);
    func_151494E0(&value, 0x23);
    func_15147928(arg0);
}

s32 func_151CE51C() {
    return 0;
}

extern u8 D_800DCE50[0x340];
extern s8 D_800DD190;
extern s32 D_800A5760[2];

/* Find the first type-11 node whose associated payload names this context. */
void *func_151CE634(void *context) {
    u8 phase;
    u8 *row;
    void **column;
    void *node;

    for (phase = 0; phase < 2; phase++) {
        row = D_800DCE50;
        column = (void **)(row + D_800A5760[phase] * 4);
        do {
            node = *column;
            while (node != 0) {
                if (*(s32 *)((u8 *)node + 0x20) == 11 &&
                    *(void **)((u8 *)*(void **)((u8 *)node + 0x98) + 0x48) == context) {
                    return node;
                }
                node = *(void **)((u8 *)node + 8);
            }
            row += 0x1A0;
            column = (void **)((u32)column + 0x1A0);
        } while (row != (u8 *)&D_800DD190);
    }
    return 0;
}

s32 func_151CE6D0() {
    return 0;
}

s32 func_151CEA20(f32 *arg0) {
    f32 acceleration = arg0[0x40 / 4];
    f32 velocity = arg0[0x44 / 4];

    arg0[0x44 / 4] = velocity + acceleration * D_800BE9A4;
    arg0[0x38 / 4] += (velocity + acceleration * 0.5f * D_800BE9A4) * D_800BE9A4;
    arg0[0x50 / 4] += arg0[0x4C / 4] * D_800BE9A4;
    if (arg0[0x50 / 4] > 1.0f) {
        arg0[0x50 / 4] = 1.0f;
    }
    return 1;
}

s32 func_151CEAAC() {
    return 0;
}

s32 func_151CEC10(f32 *arg0, u8 *arg1, u8 *arg2) {
    if (arg2 != 0) {
        *(ThreeWord1FA770 *) arg0 = *(ThreeWord1FA770 *) (arg2 + 0x40);
    } else {
        arg0[0] = *(f32 *) (arg1 + 0x14);
        arg0[1] = *(f32 *) (arg1 + 0x18);
        arg0[2] = *(f32 *) (arg1 + 0x1C);
    }
    return 1;
}

s32 func_151CEC54() {
    return 0;
}

s32 func_151CF120() {
    return 0;
}

s32 func_151CF380() {
    return 0;
}

void func_151CF844(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *target = *(u8 **) (arg0 + 0x98);

    if (*(s32 *) target != 0) {
        func_15169850(arg1, arg2, (s32) target, (s32) (target + 4), (s32) arg0);
    }
}

s32 func_151CF898() {
    return 0;
}

s32 func_151CFA4C() {
    return 0;
}

s32 func_151D0024(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x18);
}

s32 func_151D0058() {
    return 0;
}

void func_151D0128(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x28);

    if (*(u16 *)(temp_v0 + 0x84) != *(u16 *)(arg0 + 0x2E)) {
        *(s16 *)(arg0 + 0xE) = -1;
    }
}

s32 func_151D014C() {
    return 0;
}

/* Release the owner or retarget its embedded source/identity pair. */
void func_151D08F0(struct260 *record, s32 eventAddress, u8 command) {
    u8 *owner = (u8 *)record;
    u8 *event = (u8 *)eventAddress;
    u8 *state = owner + 0x28;
    s32 value = command;
    if (command == 0 || value == 0x18) {
        value = *(s32 *)event;
        if (value == *(s32 *)state || state[4] == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (value == 0x2D) {
        s32 current = *(s32 *)state;
        value = *(s32 *)event;
        if (value == current) {
            *(s32 *)state = *(s32 *)(event + 4);
            state[4] = event[9];
        } else if (*(s32 *)(event + 4) == current) {
            *(s32 *)state = value;
            state[4] = event[8];
        }
    }
}

s32 func_151D09A8() {
    return 0;
}

s32 func_151D0ED8(u8 *arg0) {
    u8 *temp_a1 = arg0;

    if (*(s32 volatile *)(temp_a1 + 0xA8) != 0) {
        func_1516972C((struct102 *)*(s32 volatile *)(temp_a1 + 0xA8));
    }
}

s32 func_151D0F08(s32 arg0) {
    func_151D0ED8(arg0);
    func_1513173C(arg0);
}

s32 func_151D0F34(s32 arg0) {
    func_151D0ED8(arg0);
    func_1513175C(arg0);
}

s32 func_151D0F60() {
    return 0;
}

s32 func_151D1074(u8 *arg0, f32 *arg1) {
    arg1[0] = *(f32 *) (arg0 + 0x14);
    arg1[1] = *(f32 *) (arg0 + 0x180) + 8.0f;
    arg1[2] = *(f32 *) (arg0 + 0x1C);
    return 1;
}

void func_151D10A4(s32 arg0, s32 arg1) {
    func_151D10E4(arg0, arg1, 0);
}

void func_151D10C4(s32 arg0, s32 arg1) {
    func_151D10E4(arg0, arg1, 1);
}

s32 func_151D10E4(u8 *arg0, s32 arg1, u8 arg2) {
    s32 target;

    target = *(s32 *) (arg0 + 0x1D4);
    if (target == NULL) {
        return 0;
    }
    func_15143134(&D_800AAF9C[arg2], arg1, target);
    return 1;
}

s32 func_151D1138() {
    return 0;
}

void func_151D1328(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_151D1368(u8 *arg0) {
    func_151D13E0(arg0);
}

s32 func_151D1388(s32 arg0) {
    func_151D1368(arg0);
    func_1514933C(arg0);
}

s32 func_151D13B4(s32 arg0) {
    func_151D1368(arg0);
    func_15149368(arg0);
}

void func_151D13E0(u8 *arg0) {
    u8 *owner = arg0 + 0x28;
    u8 *linked;

    if (*(u8 **)(owner + 8) != NULL) {
        linked = *(u8 **)(*(u8 **)(owner + 8) + 0x98);
        *(u8 *)(*(u8 **)(owner + 8) + 0x30) = 0;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1E) &= ~2;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1E) |= 8;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1E) |= 1;
        *(u16 *)(*(u8 **)(owner + 8) + 0x1C) = 0x28;
        *(s32 *)linked = 0;
        *(u8 **)(owner + 8) = NULL;
    }
}

s32 func_151D1448() {
    return 0;
}

s32 func_151D15D0() {
    return 0;
}

s32 func_151D197C() {
    return 0;
}

s32 func_151D1C98() {
    return 0;
}

void func_151D223C(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x98);
    u8 *temp_v1 = *(u8 **)temp_v0;

    if (temp_v1 != NULL) {
        *(s32 *)(temp_v1 + 0x30) = 0;
    }
}

s32 func_151D2258(s32 arg0) {
    func_151D223C(arg0);
    func_151478F4(arg0);
}

s32 func_151D2284(s32 arg0) {
    func_151D223C(arg0);
    func_15147928(arg0);
}

s32 func_151D22B0() {
    return 0;
}
