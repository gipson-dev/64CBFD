#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A5440.s. */

typedef struct CleanupNode {
    u8 pad0[8];
    struct CleanupNode *next;
    u8 padC[8];
    u8 *owner;
} CleanupNode;

extern u8 *D_800DCF38;
extern CleanupNode *D_800DCF3C;
extern s32 func_15168118(u8 *arg0);
void func_100111C8(u16 arg0);
void func_1516972C(u8 *arg0);
void func_15169824(u8 *arg0);

s32 func_15177F90() {
    return 0;
}

s32 func_15178268() {
    return 0;
}

s32 func_15178750(u8 *arg0, u8 *arg1, s16 arg2) {
    u8 *record = *(u8 **)(arg1 + 0x14);

    if (record[0x36] & (1 << arg2)) {
        return func_15168118(arg0);
    }
    return (s32)arg0;
}

void func_151787A4(void) {
}

s32 func_151787AC() {
    return 0;
}

s32 func_15178B98(u8 arg0) {
    u8 *node = D_800DCF38;

    while (node != NULL) {
        if (node[0x34] == arg0) {
            return (s32) node;
        }

        node = *(u8 **) (node + 8);
    }

    return 0;
}

void func_15178BE4(u8 arg0, f32 *arg1, s16 arg2) {
    u8 *node = (u8 *) func_15178B98(arg0);

    if (node != NULL) {
        *(f32 **)(node + 0x10) = arg1;
        *(u32 *)(node + 0x14) = 0x80000000;
        *(s16 *)(node + 0x30) = arg2;
    }
}

void func_15178C34(u8 arg0, s32 arg1, s32 arg2, s32 arg3, s16 arg4) {
    u8 *node = (u8 *)func_15178B98(arg0);

    if (node != NULL) {
        *(u32 *)(node + 0x10) = (arg1 << 16) | (arg2 & 0xFFFF);
        *(u32 *)(node + 0x14) = arg3 << 16;
        *(s16 *)(node + 0x30) = (s16)arg4;
    }
}

s32 func_15178C9C() {
    return 0;
}

void func_15178DA4(u8 *arg0) {
    CleanupNode *next;
    CleanupNode *node = D_800DCF3C;

    func_100111C8(*(u16 *)(arg0 + 0x2E));

    while (node != NULL) {
        next = node->next;

        if (node->owner == arg0) {
            func_1516972C((u8 *)node);
        }

        node = next;
    }

    func_15169824(arg0);
}

void func_15178E14(u8 arg0) {
    func_15178DA4(func_15178B98(arg0));
}
