#include <ultra64.h>
#include "structs.h"
struct260 *func_15149130(s16, s8, s8, s8, u8, u8, struct37 *, u8, s32);
void *memcpy(void *, const void *, u32);
typedef struct {
    u8 *owner;
    u8 identity, first, second, third, fourth, fifth;
} AttachedEffectPayload1199D0;

void func_1502EA98(u8 *arg0, u8 arg1, u8 arg2, u8 arg3, u8 arg4,
                   s32 arg5, u8 arg6);

/* Non-matching placeholders for the text-only asm slice asm/1199D0.s. */

s32 func_150EC520() {
    return 0;
}

s32 func_150EC6B0() {
    return 0;
}

/* Capture the owner and effect settings; publish them only after allocation. */
void func_150ECA68(u8 *owner, u8 first, u8 second, u8 third, u8 fourth,
                   u8 fifth, s16 duration, u8 selector, s32 category) {
    AttachedEffectPayload1199D0 payload;
    u8 *effect;
    payload.owner = owner;
    payload.identity = owner[0x3B];
    payload.first = first;
    payload.second = second;
    payload.third = third;
    payload.fourth = fourth;
    payload.fifth = fifth;
    effect = (u8 *)func_15149130(duration == -1 ? 300 : duration, -1, 0x5D, -1,
                                duration == -1 ? 0 : 1, 0x45,
                                (struct37 *)sizeof(payload), selector, category);
    if (effect != NULL) {
        memcpy(effect + 0x28, &payload, sizeof(payload));
    }
}

void func_150ECB4C(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_150ECB8C(u8 *arg0) {
    u8 *sub = arg0 + 0x28;
    u8 *target = *(u8 **) sub;

    if ((*(s32 *) target == 0) || (sub[4] != target[0x3B])) {
        *(s16 *) (arg0 + 0xE) = -1;
        return;
    }
    func_1502EA98(target, sub[5], sub[6], sub[7], sub[8], 0, sub[9]);
}

void func_150ECC00(u8 *arg0, volatile u8 arg1, s32 arg2) {
    func_151C9AC0(arg0, arg1, arg2);
    func_150ECA68(arg0, 0, 0xFF, 0, 0xFF, 4, -1, arg1, arg2);
}

s32 func_150ECC70() {
    return 0;
}
