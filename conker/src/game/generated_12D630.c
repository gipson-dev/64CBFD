#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/12D630.s. */

extern s32 D_800BE9E4;
extern void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                          u8 arg5, s32 arg6, u8 arg7, s32 arg8);

typedef struct {
    void *owner;
    u8 owner_id;
    u8 pad5;
    s16 state;
} Generated12D630Owner;

s32 func_15100180(u8 *arg0) {
    struct { u8 *ptr; u8 value; } temp;

    temp.ptr = arg0;
    temp.value = *(u8 *)(arg0 + 0x3B);
    func_151494E0(&temp, 0x48);
}

void func_151001B4(u8 *arg0) {
    Generated12D630Owner owner;
    void *object;

    owner.owner = arg0;
    owner.owner_id = arg0[0x3B];
    owner.state = 0;

    object = func_15149130(0x12C, -1, 0x4E, -1, 0, 0x3B, 8, 0xFF, 1);
    if (object != NULL) {
        memcpy((u8 *)object + 0x28, &owner, sizeof(owner));
    }
}

void func_15100230(s32 arg0, s32 arg1, u8 arg2) {
    if (arg2 == 0x48) {
        if (((Generated12D630Owner *)(arg0 + 0x28))->owner == *(void **)arg1 ||
            ((Generated12D630Owner *)(arg0 + 0x28))->owner_id == *(u8 *)(arg1 + 4)) {
            func_1516972C((void *)arg0);
        }
    } else {
        func_15149514(arg1, arg2, arg0 + 0x28, arg0 + 0x2C, arg0);
    }
}

void func_151002BC(u8 *arg0) {
    s16 invalid = -1;
    u8 *state = arg0 + 0x28;
    u8 *entry = *(u8 **) state;

    if (*(s32 *) entry == 0) {
        goto invalid_state;
    }
    if (entry[4] == 0xFF) {
        goto invalid_state;
    }
    if (state[4] == entry[0x3B]) {
        goto valid_state;
    }

invalid_state:
    *(s16 *) (arg0 + 0xE) = invalid;
    return;

valid_state:
    if (*(s32 *) (entry + 0x318) != 0) {
        *(s16 *) (state + 6) -= D_800BE9E4;
    }
}
