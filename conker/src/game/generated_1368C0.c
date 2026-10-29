#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1368C0.s. */

s32 func_15109410() {
    return 0;
}

s32 func_151094FC() {
    return 0;
}

s32 func_15109848() {
    return 0;
}

s32 func_15109C20() {
    return 0;
}

s32 func_15109ED4() {
    return 0;
}

s32 func_15109FB8() {
    return 0;
}

typedef struct {
    u8 *owner;
    u8 ownerId;
    f32 value0;
    f32 value1;
    f32 value2;
} OwnerFloatPayload;
extern f32 D_800A2684;
extern f32 D_800A2688;
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Create an owner-linked payload with three initial float values. */
void *func_1510A344(u8 *owner, s16 lifetime, u8 priority, s32 arg3) {
    u8 *created;
    OwnerFloatPayload payload;

    if (owner == NULL) {
        return NULL;
    }
    payload.owner = owner;
    payload.ownerId = owner[0x3B];
    payload.value0 = 0.0f;
    payload.value1 = D_800A2684;
    payload.value2 = D_800A2688;
    created = func_15149130(lifetime, -1, 0x1C, -1, 1, 0x1C,
                           sizeof(payload), priority, arg3);
    if (created != NULL) {
        memcpy(created + 0x28, &payload, sizeof(payload));
    }
    return created;
}

s32 func_1510A40C() {
    return 0;
}

// Matched with guarded commutative branch operand normalization.
void func_1510A870(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x28;

    if (arg2 == 0x2D) {
        s32 temp_v1 = *(s32 *)arg1;
        s32 temp_a2 = *(s32 *)temp_v0;

        if (temp_v1 == temp_a2) {
            *(s32 *)temp_v0 = *(s32 *)(arg1 + 4);
            temp_v0[4] = arg1[9];
        } else {
            if (temp_a2 != *(s32 *)(arg1 + 4)) {
                return;
            }
            *(s32 *)temp_v0 = temp_v1;
            temp_v0[4] = arg1[8];
        }
    }
}

// Matched with guarded commutative branch operand normalization.
void func_1510A8CC(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x28;

    if (arg2 == 0x2D) {
        s32 temp_v1 = *(s32 *)arg1;
        s32 temp_a2 = *(s32 *)temp_v0;

        if (temp_v1 == temp_a2) {
            *(s32 *)temp_v0 = *(s32 *)(arg1 + 4);
            temp_v0[4] = arg1[9];
        } else {
            if (temp_a2 != *(s32 *)(arg1 + 4)) {
                return;
            }
            *(s32 *)temp_v0 = temp_v1;
            temp_v0[4] = arg1[8];
        }
    }
}
