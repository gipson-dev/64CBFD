#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/DDB60.s. */

void func_150B0C58(u8 *arg0, u8 arg1, s32 arg2);
void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                    u8 arg5, s32 arg6, u8 arg7, s32 arg8);

typedef struct {
    u8 *owner;
    u8 owner_id;
    u8 pad5[3];
    f32 value;
} OwnerPayload;

s32 func_150B06B0() {
    return 0;
}

s32 func_150B0A60() {
    return 0;
}

void func_150B0C34(s32 arg0) {
    func_150B0C58((u8 *)arg0, 0xFF, 1);
}

void func_150B0C58(u8 *arg0, u8 arg1, s32 arg2) {
    OwnerPayload payload;
    u8 *object;

    payload.owner = arg0;
    payload.owner_id = arg0[0x3B];
    payload.value = 0.0f;

    object = func_15149130(0x12C, -1, 0x58, -1, 0, 0x43,
                           sizeof(payload), arg1, arg2);
    if (object != NULL) {
        memcpy(object + 0x28, &payload, sizeof(payload));
    }
}

void func_150B0CE0(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

s32 func_150B0D20() {
    return 0;
}
