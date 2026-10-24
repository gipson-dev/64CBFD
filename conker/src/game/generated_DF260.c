#include <ultra64.h>
#include <string.h>
#include "structs.h"
s32 func_1509BE40(s32, ...);

/* Non-matching placeholders for the text-only asm slice asm/DF260.s. */

// Handwritten two-block 64-bit word transform.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_DF260/func_150B1DB0.s")

/* Update event-driven actor flags and the attached record's target scalar. */
void func_150B1E20(void *actor) {
    void *temp_v0;

    if (func_1509BE40(1, 0x4054, 6, 0x9000) != 0) {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) | 0x10000);
    } else {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) & 0xFFFEFFFF);
    }
    if ((func_1509BE40(1, 0x405C, 6, 0x9000) == 0) && (func_1509BE40(1, 0x405B, 6, 0x2000) != 0) && ((*(s32 *)((char *)(actor) + 0x2C)) != 0x40)) {
        temp_v0 = (void *)(*(s32 *)((char *)(actor) + 0x3D0));
        (*(f32 *)((char *)(temp_v0) + 0x17C)) = (f32) ((*(f32 *)((char *)(temp_v0) + 0x180)) + 10.0f);
    }
}

typedef struct {
    f32 x, y, z;
} PayloadVectorDF260;

typedef struct {
    PayloadVectorDF260 position;
    f32 scalar;
} RandomVectorPayloadDF260;

s32 func_150ADA20(void);
struct260 *func_15149130(s16, s8, s8, s8, u8, u8, struct37 *, u8, s32);

/* Copy the spawn vector and submit a randomized-lifetime payload. */
void func_150B1EE0(u8 *owner, PayloadVectorDF260 *position, s32 unused2, s32 unused3) {
    RandomVectorPayloadDF260 payload;
    u8 *record;
    u32 lifetime;

    payload.position = *position;
    payload.scalar = 0.0f;
    lifetime = func_150ADA20() % 133U + 69U;
    record = (u8 *)func_15149130((s16)lifetime,
        -1, 0x49, -1, 1, 0, (struct37 *)0x10, owner[0xC], owner[1]);
    if (record != NULL) {
        memcpy(record + 0x28, &payload, sizeof(payload));
    }
}

s32 func_150B1F90() {
    return 0;
}

s32 func_150B2340() {
    return 0;
}
