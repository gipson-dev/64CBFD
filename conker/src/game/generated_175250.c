#include <ultra64.h>

typedef struct { s32 words[8]; } RenderRecord15147DA0;
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);

typedef struct { u32 words[3]; } ActorPosition15147EB8;
extern s32 (*D_8008A3E0[])(u8 *);
extern s32 (*D_8008A3F8[])(u8 *);
extern s32 (*D_8008A42C[])(u8 *);

/* Non-matching placeholders for the text-only asm slice asm/175250.s. */

s32 func_151478F4(s32 arg0);

u8 *func_15147DA0(void *request, void *descriptor, s32 payloadBytes,
    s32 active, s32 first, s32 second, s32 third, s32 fourth, s32 fifth,
    s32 fadeFlag, s32 fadeAlpha, void *render, s32 extraBytes, u8 channel, s32 context) {
    u8 *created;
    u8 *payload;

    *(s32 *)((u8 *)request + 0x10) = 1;
    created = func_15147A80(request, (u32)payloadBytes + 0x48, 0x14, 1, 0, 1,
        fadeFlag, fadeAlpha, (void *)extraBytes, channel, context);
    if (created == NULL) {
        return NULL;
    }
    payload = *(u8 **)(created + 0x98);
    memcpy(payload, descriptor, 32);
    payload[0x20] = active;
    payload[0x21] = first;
    payload[0x22] = second;
    payload[0x23] = third;
    payload[0x24] = fourth;
    payload[0x25] = fifth;
    *(RenderRecord15147DA0 *)(payload + 0x28) = *(RenderRecord15147DA0 *)render;
    return created;
}

s32 func_15147EB8(u8 *actor) {
    u8 *payload = *(u8 **)(actor + 0x98);
    s8 failed = 0;
    s32 success;
    s32 selector;
    s32 value;
    u8 *records;

    selector = payload[0x20];
    if (selector != 0) {
        if (D_8008A3E0[selector](actor) == 0) {
            failed = 1;
        }
    }
    selector = payload[0x21];
    if (selector != 0 && !failed) {
        if (D_8008A3F8[selector](actor) == 0) {
            failed = 1;
        }
    }
    if ((payload[0x18] & 0x40) && !failed) {
        value = *(s16 *)(actor + 0x1C);
        if (value < *(s16 *)(payload + 0x1C)) {
            s32 product;
            product = (u32)value * (u32)*(s16 *)(payload + 0x1E);
            if (product < payload[0x1B]) {
                payload[0x1B] = product;
            }
        }
    }
    success = !failed;
    if (failed) {
        selector = payload[0x22];
        if (selector != 0) {
            D_8008A42C[selector](actor);
        }
    }
    records = *(u8 **)(actor + 0x94);
    if (*(s8 *)(actor + 0x2C) > 0) {
        *(ActorPosition15147EB8 *)(actor + 0x54) = *(ActorPosition15147EB8 *)(
            records + *(s8 *)(actor + 0x2D) * 20);
    } else {
        *(f32 *)(actor + 0x54) = 0.0f;
        *(f32 *)(actor + 0x58) = 0.0f;
        *(f32 *)(actor + 0x5C) = 0.0f;
    }
    return (s8)success;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_1514803C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_151488C4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_15148AF4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_15148BA4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_15148DE0.s")

s32 func_15148EF8(u8 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    u8 *temp_v1 = *(u8 **) (arg0 + 0x98);

    temp_v1[0x20] = 4;
    return 1;
}

s32 func_15148F1C() {
    return 0;
}

s32 func_151490C8(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 3;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    *(temp_v0 + 0x1B) = temp_v1;
    if ((temp_v1 & 0xFF) < 0) {
        return 0;
    }
    return 1;
}

void func_15149104(s32 arg0) {
    func_151478F4(arg0);
}
