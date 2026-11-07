#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1513B5E0();
void func_1513B798(u8 *arg0);
s32 func_1513B83C();
s32 func_1513BAE8(void);
s32 func_1513BBFC();
s32 func_1513BEB0();
s32 func_15109064(struct132 *, s32, u8);
void func_151BA468(struct132 *, s32, u8);
/* End generated placeholder declarations. */

extern s32 (*D_80089C18[])(u8 *);

/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513B5E0.s. */
s32 func_1513B5E0() {
    return 0;
}
void func_1513B798(u8 *arg0) {
    s32 remove = 0;
    s8 callbackIndex;

    if ((arg0[0x10] & 1) != 0) {
        *(s16 *)(arg0 + 0x14) -= D_800BE9E4;
        if (*(s16 *)(arg0 + 0x14) < 0) {
            remove = 1;
        }
    }

    if (remove == 0) {
        callbackIndex = *(s8 *)(arg0 + 0x11);
        if ((callbackIndex != -1) && (D_80089C18[callbackIndex](arg0) == 0)) {
            remove = 1;
        }
    }

    if (remove != 0) {
        func_1516972C((struct102 *)arg0);
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513B83C.s. */
s32 func_1513B83C() {
    return 0;
}

s32 func_1513B968(s32 arg0, s32 arg1) {
    // FIXME: &arg0->unk_120[D_800BE9C0]
    func_150A7B80(arg0 + 120 + (D_800BE9C0 << 6));
    return 1;
}

void func_1513B9A8(struct132 *arg0) {
    func_100043B4(arg0->unk4C, 4);
    func_15169804(arg0);
}

void func_1513B9DC(struct132 *arg0) {
    func_100043B4(arg0->unk4C, 4);
    func_15169824(arg0);
}

void func_1513BA10(struct132 *arg0) {
    D_80089C44[arg0->unk48]();
}

void func_1513BA44(struct132 *arg0) {
    D_80089C54[arg0->unk48]();
}

void func_1513BA78(struct132 *arg0, s32 arg1, u8 arg2) {
    switch (arg0->unk48) {
        case 1:
            func_15109064(arg0, arg1, arg2);
            break;
        case 2:
            func_151BA468(arg0, arg1, arg2);
            break;
    }
}

s32 func_1513BAD4(s32 arg0, s32 arg1) {
    return 0;
}

typedef struct {
    u8 field0, field1, field2, pad3;
    s16 field4;
    u8 pad6[2];
    s32 field8, fieldC, field10, field14, field18, field1C, field20;
    u8 field24, field25, pad26[10];
    s32 field30, field34;
    u8 field38;
} EffectDescriptor1513BAE8;
typedef struct { f32 value0, value4, value8, valueC, value10; } EffectPayload1513BAE8;

/* Build the fixed effect and preserve its handle even on validation release. */
s32 func_1513BAE8(void) {
    u32 handle;
    EffectDescriptor1513BAE8 descriptor;
    EffectPayload1513BAE8 payload;
    payload.value0 = 0.0f;
    payload.value4 = 0.0f;
    payload.valueC = 0.0f;
    payload.value10 = 0.0f;
    payload.value8 = 0.0f;
    descriptor.field0 = 0;
    descriptor.field1 = 2;
    descriptor.field2 = 5;
    descriptor.field4 = 300;
    descriptor.field30 = 9;
    descriptor.field34 = 430;
    descriptor.field8 = 1;
    descriptor.fieldC = 0x220205;
    descriptor.field10 = 0x40600;
    descriptor.field24 = 0;
    descriptor.field25 = 0;
    descriptor.field14 = 1;
    descriptor.field18 = 54;
    descriptor.field1C = 128;
    descriptor.field20 = 32;
    descriptor.field38 = 3;
    handle = func_1513B5E0(&descriptor, 1, 20, 255, 1);
    if (handle != 0) {
        if (*(s32 *)(handle + 0x50) != 0x1180) {
            func_1516972C((struct102 *)handle);
        } else {
            memcpy((void *)(handle + *(s32 *)(handle + 0x50) + 0xF8), &payload, 20);
        }
    }
    return handle;
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513BBFC.s. */
s32 func_1513BBFC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_168A90/func_1513BEB0.s. */
s32 func_1513BEB0() {
    return 0;
}
