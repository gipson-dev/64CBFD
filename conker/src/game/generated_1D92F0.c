#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1D92F0.s. */

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

s32 func_151ACA60() {
    return 0;
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

s32 func_151AE2BC() {
    return 0;
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

s32 func_151AE6B0() {
    return 0;
}

s32 func_151AE7B0() {
    return 0;
}

s32 func_151AE890() {
    return 0;
}

s32 func_151AE984() {
    return 0;
}

s32 func_151AEAB4() {
    return 0;
}

/* Note 362: original ROM blood effect and dependencies. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AECA0.s")

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

s32 func_151AF388(f32 *, f32, f32, f32, u8);

void func_151AF338(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4,
                   f32 arg5, u8 *arg6) {
    f32 position[3];

    position[0] = arg0;
    position[1] = arg1;
    position[2] = arg2;
    func_151AF388(position, arg3, arg4, arg5, arg6[0xC]);
}

s32 func_151AF388(f32 *arg0, f32 arg1, f32 arg2, f32 arg3, u8 arg4) {
    return 0;
}

/* Note 362: original ROM blood effect and dependencies. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D92F0/func_151AF4D0.s")
