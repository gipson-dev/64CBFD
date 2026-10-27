#include <ultra64.h>
#include "structs.h"
extern u8 *D_800D3098;
extern f32 D_800A1DC0;

/* Non-matching placeholders for the text-only asm slice asm/126F60.s. */

s32 func_150F9AB0() {
    return 0;
}

s32 func_150F9BB0() {
    return 0;
}

s32 func_150FA1B8() {
    return 0;
}

void func_1515D4D4(s32, s32, s32, u8);

/* Set the record timer and apply the requested black or white color override. */
void func_150FA468(struct260 *record, s32 eventAddress, u8 command) {
    if (command == 0x4C) {
        record->unk11 = -1;
        func_1515D4D4(0, 0, 0, 255);
    } else if (command == 0x4D) {
        record->unk11 = 30;
    } else if (command == 0x4E) {
        record->unk11 = -1;
    } else if (command == 0x4F) {
        record->unk11 = -1;
        func_1515D4D4(255, 255, 255, 255);
    }
}

s32 func_150FA520() {
    return 0;
}

typedef struct {
    void *first;
    void *second;
    f32 zero;
} OneShotLinkPayload;

extern u8 D_80088B60;
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Capture both owner links and attach the payload only once allocation succeeds. */
void func_150FAA40(u8 code, s32 value) {
    OneShotLinkPayload payload;
    u8 *effect;

    if (D_80088B60 == 0) {
        payload.first = D_800D3098 + 0x71C;
        payload.second = D_800D3098 + 0x6E8;
        payload.zero = 0.0f;
        effect = func_15149130(300, -1, 0x57, -1, 0, 0x46, 12, code, value);
        if (effect != 0) {
            D_80088B60 = 1;
        }
        if (effect != 0) {
            memcpy(effect + 0x28, &payload, 12);
        }
    }
}

s32 func_150FAAEC() {
    return 0;
}

void func_150FACE4(u8 *arg0, u8 arg1, u8 arg2) {
    if ((arg2 == 0x4E) || (arg2 == 0x4F)) {
        func_1516972C(arg0);
    }
}

void func_150FAD28(void) {
    func_1515F170(8, 0);
    func_1515F170(0xB, 1);
    func_151494E0(D_800D3098 + 0x514, 0x30);
    func_151494E0(0, 0x4D);
}

void func_150FAD78(void) {
    func_1515F170(8, 1);
    func_1515F170(7, 0);
    func_151494E0(D_800D3098 + 0x514, 0x31);
    func_151494E0(0, 0x4C);
}

void func_150FADC8(u8 *arg0, u8 arg1, u8 arg2) {
    if (arg2 == 0x53) {
        *(u32 *) (arg0 + 0x58) |= 2;
    } else if (arg2 == 0x54) {
        *(u32 *) (arg0 + 0x58) &= ~2;
    }
}

s32 func_150FAE18() {
    return 0;
}

typedef struct {
    f32 unk0;
    f32 unk4;
    f32 unk8;
    f32 unkC;
    f32 unk10;
} struct_150FB188_params;

s32 func_15157DEC();

s32 func_150FB188(u8 *arg0) {
    struct_150FB188_params params;

    *(f32 *) (arg0 + 0x5C) = 0.0f;
    *(f32 *) (arg0 + 0x54) = -95.0f;
    *(f32 *) (arg0 + 0x58) = -80.0f;
    params.unk0 = 0.0f;
    params.unk4 = 0.0f;
    params.unk8 = 0.0f;
    params.unkC = D_800A1DC0;
    params.unk10 = D_800A1DC0;
    func_15157DEC(arg0, &params);
    return 1;
}

Gfx *func_151D710C(Gfx *, u8 *, s32, s32, u8 *);
s32 func_15157F80(s32, s32, s32, s32, s32);

void func_150FB1E8(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    arg0 = (s32)func_151D710C((Gfx *)arg0, (u8 *)arg1, arg2, arg3, (u8 *)arg4);
    func_15157F80(arg0, arg1, arg2, arg3, arg4);
}

void func_150FB240(u8 *arg0, s16 arg1, s16 arg2, s16 arg3, s16 arg4) {
    if (arg2 - arg3 < arg1) {
        *arg0 = (arg2 - arg1) * arg4;
    } else {
        *arg0 = 0xFF;
    }
}

s32 func_150FB29C(u8 *arg0) {
    func_150FB240(arg0 + 0x43, *(s16 *) (arg0 + 0x16), *(s16 *) (arg0 + 0x120),
                  *(s16 *) (arg0 + 0x64), *(s16 *) (arg0 + 0x66));
    return 1;
}

s32 func_150FB2E0(u8 *arg0) {
    func_150FB240(arg0 + 0x2E, *(s16 *) (arg0 + 0x22), *(s16 *) (arg0 + 0x70),
                  *(s16 *) (arg0 + 0x26), *(s16 *) (arg0 + 0x28));
    return 1;
}

s32 func_150FB324() {
    return 0;
}
