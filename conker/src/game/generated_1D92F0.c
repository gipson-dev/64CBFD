#include <ultra64.h>
extern f32 D_800A9D70;
s32 func_15045800(f32 *, u16, f32, void *);
u16 func_10010FFC(s32, s32, u16, s16, u8, void *);
extern f32 D_800A9D84, D_800A9D88;
f32 func_150ADA68(void);
void *func_151AE984(void *, f32, f32, f32, u8, u8);
s32 func_151AEAB4();

/* Recovered routines and remaining placeholders for asm/1D92F0.s. */

s32 func_151AE3A8();
s32 func_151AE0E4(u8 *arg0, u8 arg1);
s32 func_151AE264(u8 *arg0, u8 arg1);

extern f32 D_800BE9A4;

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151ABE40.s")

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AC078.s")

s32 func_151AC3CC(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_151AC408() {
    return 0;
}

u8 func_151D8E20(void);
void func_151DBCBC(u8, f32, s16, s32, void *, u8, s32);

typedef struct { f32 x, y, z, velocityY, other; } ImpactMotionRecord;

/* Submit the impact effect, then mark the captured payload as handled. */
s32 func_151AC550(u8 *actor, f32 previousX, f32 previousY, f32 previousZ,
                  f32 height, void *result) {
    u8 *payload = *(u8 **)(actor + 0x98);
    ImpactMotionRecord *records = *(ImpactMotionRecord **)(actor + 0x94);
    f32 position[3];
    u8 selector;

    position[0] = records[*(s8 *)(actor + 0x2D)].x;
    position[1] = height;
    position[2] = records[*(s8 *)(actor + 0x2D)].z;
    selector = func_151D8E20();
    func_151DBCBC(selector, *(f32 *)payload * 7.0f, payload[0x1B],
                  (s32)result, position, actor[0xC], actor[1]);
    payload[0x20] = 4;
    return 1;
}

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AC61C.s")

s32 func_151AC810() {
    return 0;
}

s32 func_151AC9EC(f32 *arg0) {
    f32 delta = arg0[0x4C / 4] * D_800BE9A4;

    arg0[0x2C / 4] += delta;
    arg0[0x30 / 4] += delta;
    return 1;
}

s32 func_151ACA20(u8 *arg0) {
    s32 temp_v0 = 0xFF;
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C);

    if (temp_v1 < 0x10) {
        temp_v0 = (s16) (temp_v1 << 4);
    }
    if (temp_v0 < *(arg0 + 0x5C)) {
        *(arg0 + 0x5C) = temp_v0;
    }
    return 1;
}

extern u8 D_800CC2D0[];
void *func_15167A68(s32, s32, s32, s32, u8, s32);
s32 func_151ACB38(u8 *, u8 *);
void func_1516979C(void *);

/* Allocate an admitted owner record and return its 32-bit address handle. */
s32 func_151ACA60(u8 *owner, f32 scale, s32 payloadSize) {
    u8 *record;

    if (owner == NULL) {
        return 0;
    }
    record = func_15167A68(0x30, 0, (s32)((u32)payloadSize + 0x30U), 1, 0xFF, 1);
    if (record == NULL) {
        return 0;
    }
    if (func_151ACB38(owner, record + 0x18) == 0) {
        func_1516979C(record);
        return 0;
    }
    *(u8 **)(record + 0x1C) = owner;
    record[0x20] = owner[0x3B];
    *(s32 *)(record + 0x24) = (s32)((u32)owner - (u32)D_800CC2D0) / 0x32C;
    *(f32 *)(record + 0x28) = scale;
    *(s32 *)(record + 0x10) = 1;
    *(s32 *)(record + 0x14) = 0;
    return (s32)record;
}

s32 func_151ACB38(u8 *arg0, u8 *arg1) {
    s32 result = 0;

    if (arg0[0x3B] == 1) {
        *arg1 = 1;
        result = 1;
    }
    return result;
}

// Matched with guarded call-delay argument home.
void func_151ACB60(u8 *arg0) {
    s32 temp_v0 = *(s32 *) (*(u32 *) (*(u32 *) (arg0 + 0x1C) + 0x31C) + 0x9C);

    if (temp_v0 != 0) {
        func_151AE3A8(arg0);
    }
}

void func_151ACB94(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x1C), (s32) (arg0 + 0x20), (s32) arg0);
}

s32 func_151ACBD4() {
    return 0;
}

s32 func_151AD174() {
    return 0;
}

s32 func_151AD92C() {
    return 0;
}

void func_151AE06C(u8 *arg0, u8 *arg1) {
    u8 admission;
    u8 requested;
    s32 current;

    if (func_151ACB38(arg0, &admission) != 0) {
        requested = arg1[0x1B];
        current = (*(u8 **)(arg0 + 0x31C))[0x98];
        if (current == 0) {
            func_151AE0E4(arg0, requested);
            return;
        }
        if (current == requested) {
            return;
        }
        func_151AE264(arg0, requested);
        func_151AE0E4(arg0, requested);
    }
}

s32 func_151AE0E4(u8 *arg0, u8 arg1) {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AE264.s")

typedef struct {
    u8 reserved00[4];
    f32 value;
    u8 reserved08[0x10];
} CurveKnot1D92F0;
typedef struct {
    u8 reserved00[0x38];
    CurveKnot1D92F0 *knots;
    u8 reserved3C[6];
    u8 count;
} CurveProgress1D92F0;

/* Locate the height segment and publish its normalized curve progress. */
void func_151AE2BC(f32 *output, CurveProgress1D92F0 *curve,
                  f32 x, f32 height, f32 z) {
    s32 count = curve->count;
    s32 index = 0;
    CurveKnot1D92F0 *knot;
    f32 fraction;

    if ((count - 1) > 0) {
        knot = curve->knots;
        do {
            if (height <= knot->value) break;
            index++;
            knot++;
        } while (index < (count - 1));
    }
    if (index >= count - 2) {
        *output = 1.0f;
        return;
    }
    if (index == 0) {
        *output = 0.0f;
        return;
    }
    knot = &curve->knots[index];
    fraction = knot->value - knot[-1].value;
    if (fraction != 0.0f) fraction = (height - knot[-1].value) / fraction;
    else fraction = 0.0f;
    *output = (f32)(index - 1) / (f32)(count - 3) + fraction / (f32)(count - 1);
}

s32 func_151AE3A8() {
    return 0;
}

/* Only selected head cells and the node's link/key prefix are known here. */
typedef struct LookupNode1D92F0 LookupNode1D92F0;
struct LookupNode1D92F0 {
    u8 reserved00[8];
    LookupNode1D92F0 *next;
    u8 reserved0C[4];
    u8 key;
};
typedef struct {
    LookupNode1D92F0 *cells[104];
} LookupRow1D92F0;

extern u8 D_800DCE50[0x340];
extern s32 D_800A9270[2];

/* Search selected columns first, scanning both rows before the next column. */
LookupNode1D92F0 *func_151AE590(u8 key) {
    LookupNode1D92F0 *node, *next;
    u8 outer, row;
    s32 column;

    outer = 0;
    do {
        column = D_800A9270[outer];
        row = 0;
        do {
            node = ((LookupRow1D92F0 *)D_800DCE50)[row].cells[column];
            while (node != NULL) {
                next = node->next;
                if (key == node->key) return node;
                node = next;
            }
            row++;
        } while (row < 2);
        outer++;
    } while (outer < 2);
    return NULL;
}

void func_151AE640(u8 *arg0, s32 *arg1, u8 arg2) {
    s32 value;

    if (arg2 == 0) {
        value = arg1[0];
        if (value == *(s32 *)(arg0 + 0x44)) {
            *(s32 *)(arg0 + 0x44) = 0;
        }
        return;
    } else if (arg2 == 0x2D) {
        value = arg1[0];
        if (value == *(s32 *)(arg0 + 0x44)) {
            *(s32 *)(arg0 + 0x44) = arg1[1];
            return;
        } else if (arg1[1] == *(s32 *)(arg0 + 0x44)) {
            *(s32 *)(arg0 + 0x44) = value;
        }
    }
}

/* Probe below the attached actor, submit an effect, and start its hit sound. */
void func_151AE6B0(u8 *input) {
    u8 *owner = input;
    f32 position[3];
    u8 *actor;

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A9D70 < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 5, owner[0xC], owner[1]);
        func_10010FFC(0, 0x11, 0x5208, 0, 0, actor);
    }
}

typedef struct {
    u32 zero0, zero4;
    u8 ownerIdentity, reserved09[3];
    u8 *owner;
    u8 attachment, reserved11[3];
    f32 vector[3];
    f32 value20, value24;
    s16 duration;
    u8 flags, kind;
    s8 callback;
    u8 mode;
} OwnerEffectDescriptor1D92F0;

extern f32 D_800A9DCC, D_800A9DD0;
void func_1516962C(s32, void *, u8);
void *func_1513418C(void *, s32, u8, s32);

extern f32 D_800A9D80;

/* Notify the owner, then submit an attached effect with the selected lifetime. */
void *func_151AE7B0(u8 *owner, f32 scale, s16 duration, u8 selector, s32 category) {
    void *created;
    OwnerEffectDescriptor1D92F0 descriptor;

    if (owner == NULL) {
        return NULL;
    }
    func_1516962C(40, owner, 17);
    descriptor.zero0 = 0;
    descriptor.zero4 = 0;
    descriptor.ownerIdentity = owner[0x3B];
    descriptor.owner = owner;
    descriptor.attachment = 1;
    descriptor.vector[0] = 0.0f;
    descriptor.vector[1] = 0.0f;
    descriptor.vector[2] = 0.0f;
    descriptor.value20 = D_800A9D80;
    descriptor.value24 = scale;
    descriptor.flags = 2;
    if (duration != 0) {
        descriptor.duration = duration;
        descriptor.flags = 6;
    } else {
        descriptor.duration = 300;
    }
    descriptor.kind = 6;
    descriptor.callback = -1;
    descriptor.mode = 5;
    created = func_1513418C(&descriptor, 0, selector, category);
    return created;
}

/* Route a position and raw effect payload through a random constructor. */
void func_151AE890(f32 x, f32 y, f32 z, f32 effectX,
                   f32 effectY, f32 effectZ, u8 *actor) {
    f32 position[3];
    f32 sample;

    position[0] = x;
    position[1] = y;
    position[2] = z;
    sample = func_150ADA68();
    if (sample < D_800A9D84) {
        return;
    }
    if (sample < 0.25f) {
        func_151AEAB4(position,
                      0.0f < func_150ADA68() ? 1 : 0, actor[0xC]);
    } else {
        s32 flag = D_800A9D88 < func_150ADA68() ? 1 : 0;
        func_151AE984(position, effectX, effectY,
                      effectZ, flag, actor[0xC]);
    }
}

extern f32 D_800A9D8C, D_800A9D90, D_800A9D94;
s32 func_150ADA20(void);
void *func_151D9014(void *, f32 *, u8, f32, s16, u8, f32, u8,
                    f32, f32, u8, s32, u8, u8, u8, s32);

/* Construct a randomized effect from three incoming floating-point values. */
void *func_151AE984(void *position, f32 x, f32 y, f32 z,
                    u8 mode, u8 selector) {
    f32 velocity[3];
    f32 first, second;
    u32 firstValue, secondValue;

    velocity[0] = -x * D_800A9D8C;
    velocity[1] = -y * D_800A9D8C;
    velocity[2] = -z * D_800A9D8C;
    first = func_150ADA68();
    firstValue = func_150ADA20();
    secondValue = func_150ADA20();
    second = func_150ADA68();
    return func_151D9014(position, velocity, 0,
        first * D_800A9D90 + D_800A9D94,
        firstValue % 31U + 60, secondValue % 101U + 155,
        second * 219.0f + 77.0f, mode, 1.0f, 1.0f,
        0, 0, 1, 0, selector, 1);
}

s32 func_151AEAB4() {
    return 0;
}

/* Note 362: original ROM blood effect and dependencies. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AECA0.s")

/* Notify the owner before constructing its attached effect descriptor. */
void *func_151AF270(u8 *owner, u8 selector, s32 category) {
    void *created;
    OwnerEffectDescriptor1D92F0 descriptor;

    if (owner == NULL) {
        return NULL;
    }
    func_1516962C(40, owner, 22);
    descriptor.zero0 = 0;
    descriptor.zero4 = 0;
    descriptor.ownerIdentity = owner[0x3B];
    descriptor.owner = owner;
    descriptor.attachment = 1;
    descriptor.vector[0] = 0.0f;
    descriptor.vector[1] = 0.0f;
    descriptor.vector[2] = 0.0f;
    descriptor.value20 = D_800A9DCC;
    descriptor.value24 = D_800A9DD0;
    descriptor.flags = 6;
    descriptor.duration = 320;
    descriptor.kind = 10;
    descriptor.callback = -1;
    descriptor.mode = 9;
    created = func_1513418C(&descriptor, 0, selector, category);
    return created;
}

void *func_151AF388(f32 *, f32, f32, f32, u8);

void func_151AF338(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151AF388(position, arg3, arg4, arg5, arg6[0xC]);
}

extern f32 D_800A9DD4, D_800A9DD8, D_800A9DDC, D_800A9DE0;
/* Spawn an effect using a reversed velocity and five ordered random samples. */
void *func_151AF388(f32 *position, f32 x, f32 y, f32 z, u8 selector) {
    f32 size;
    f32 velocity[3];
    f32 scale = D_800A9DD4;
    f32 second;
    u32 alpha, duration;
    f32 first;
    u8 variant;
    velocity[0] = -x * scale;
    velocity[1] = -y * scale;
    velocity[2] = -z * scale;
    if (func_150ADA20() & 1) {
        variant = 1;
    } else {
        variant = 0;
    }
    first = func_150ADA68();
    duration = (u32)func_150ADA20();
    alpha = (u32)func_150ADA20();
    second = func_150ADA68();
    size = D_800A9DD8;
    return func_151D9014(position, velocity, 0,
        first * D_800A9DDC + D_800A9DE0,
        (duration & 15U) + 10, alpha % 45U + 137,
        second * 202.0f + 142.0f, variant,
        size, size, 0, 0, 1, 0, selector, 1);
}

/* Note 362: original ROM blood effect and dependencies. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AF4D0.s")
