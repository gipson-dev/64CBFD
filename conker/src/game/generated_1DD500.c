#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1DD500.s. */

s32 func_151B0050() {
    return 0;
}

s32 func_151B01B8() {
    return 0;
}

/* Note 362: original ROM blood effect and dependencies. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1DD500/func_151B03B8.s")

s32 func_151B09BC() {
    return 0;
}

s32 func_151B0B88() {
    return 0;
}

s32 func_151B118C() {
    return 0;
}

s32 func_151B1478(u8 *arg0) {
    s32 temp_v0 = *(s16 *)(arg0 + 0x1C);

    if (temp_v0 < 0x20) {
        s32 temp_v1 = temp_v0 << 3;
        if (temp_v1 < *(u8 *)(arg0 + 0x5C)) {
            *(u8 *)(arg0 + 0x5C) = temp_v1;
        }
    }
    return 1;
}

s32 func_151B14AC() {
    return 0;
}

s32 func_151B1828() {
    return 0;
}

void func_1516972C(void *arg0);

typedef struct {
    void *child;
    s32 first;
    s32 second;
} CleanupSlot1DD500;

void func_151B1918(u8 *arg0) {
    u8 *cursor = arg0 + 0x28;
    CleanupSlot1DD500 *slot;
    CleanupSlot1DD500 *current;
    s32 offset;

    *(s32 *)(arg0 + 0x30) = 0;
    slot = (CleanupSlot1DD500 *)(cursor + 0xC);
    *(f32 *)(arg0 + 0xB8) = 0.0f;
    offset = 0;
    do {
        current = slot;
        if (*(void **)(cursor + 0xC) != NULL) {
            func_1516972C(slot->child);
        }
        current->child = NULL;
        current->first = 0;
        current->second = 0;
        offset += 0xC;
        cursor += 0xC;
        slot++;
    } while (offset != 0x84);
}

s32 func_151B19A4() {
    return 0;
}

s32 func_151B1A58(s32 arg0) {
    func_151B1918((u8 *)arg0);
    func_1514933C(arg0);
}

s32 func_151B1A84(s32 arg0) {
    func_151B1918((u8 *)arg0);
    func_15149368(arg0);
}

void *func_151491F4(s16 arg0, s8 arg1, s8 arg2, u8 arg3, u8 arg4, s32 arg5, u8 arg6, s32 arg7);

typedef struct {
    void *owner;
    u8 selector;
    u8 pad5[3];
    f32 value;
} Generated1DD500Payload;

void func_151B1AB0(u8 * volatile arg0) {
    u8 *record;
    Generated1DD500Payload payload;

    if (arg0 != NULL) {
        payload.owner = arg0;
        payload.selector = ((u8 *)payload.owner)[0x3B];
        payload.value = 0.0f;
        record = func_151491F4(0x3C, -1, 0x15, 1, 0x11, 0xC, 0xFF, 1);
        if (record != NULL) {
            memcpy(record + 0x28, &payload, sizeof(payload));
        }
    }
}

s32 func_151B1B34() {
    return 0;
}

s32 func_151B1FAC() {
    return 0;
}
