#include <ultra64.h>

typedef struct { s32 words[8]; } RenderRecord15147DA0;
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);

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

#pragma GLOBAL_ASM("asm/nonmatchings/generated_175250/func_15147EB8.s")

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
