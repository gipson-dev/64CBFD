#include <ultra64.h>
#include "structs.h"
extern u16 D_800BE598[];
extern u8 D_800BE590;
extern u8 D_800CC2D0[];
extern u8 D_800BE616;
extern s32 D_800BE9F0;
extern u8 D_800D2100;
extern u8 D_800D2101;
extern s32 func_1507DF10();
extern s32 func_150ADA20();
s32 func_150843AC();

/* Non-matching placeholders for the text-only asm slice asm/AEB40.s. */

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AEB40/func_15081690.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AEB40/func_15081C20.s")

s32 func_15081E0C(u8 *arg0, u16 arg1, u8 arg2) {
    if (D_800BE616 != 0) {
        return;
    }
    if (arg0[0x1CA] != 0) {
        arg0[0x1CA] = 7;
    }
    if ((arg2 == 0) || (arg1 != 0xA)) {
        func_1507DF10(arg0, arg1);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AEB40/func_15081E78.s")

s32 func_150825C0() {
    return 0;
}

s32 func_1508295C(s32 arg0, u8 *arg1, s32 arg2) {
    s32 start;
    s32 i;
    s32 end;

    if (arg2 != 0) {
        start = 0;
        end = D_800D2101;
    } else {
        start = D_800D2101;
        end = D_800D2100;
    }

    if (start < end) {
        i = start;
        do {
            func_150825C0(i, arg1);
            i++;
        } while (i != end);
    }
}

void func_150829D8(u8 *arg0) {
    u8 *temp_v0;

    *(u32 *)(arg0 + 0xF8) &= 0xF7FFFFFD;
    *(u32 *)(arg0 + 0xF8) |= 4;
    temp_v0 = *(u8 **)(arg0 + 0x31C);
    if ((temp_v0 != NULL) && (temp_v0[0x56] == 0)) {
        switch (D_800BE9F0) {
            case 0:
            case 10:
            case 14:
            case 18:
            case 19:
            case 25:
            case 27:
            case 44:
            case 60:
            case 61:
            case 66:
            case 67:
            case 68:
                break;
            default:
                *(u32 *)(arg0 + 0xF8) |= 2;
                break;
        }
    }
}

s32 func_15082A44() {
    return 0;
}

s32 func_150832AC() {
    return 0;
}

s32 func_15083384() {
    return 0;
}

typedef struct {
    u8 *records;
    u8 count;
    u8 padding[3];
} AnimationDescriptor15083568;
extern AnimationDescriptor15083568 D_80086CC4[];
u8 *func_15083AC8(u8 *, s32, s32, s32, s32, s32, s32, s32, f32);
u8 *func_15030AF4(u8 *, s32, s32, s32, s32, s32, s32, s32, s32, u8 *, s32, s32, s32);

u8 *func_15083568(u8 *actor, s32 animation, f32 scale, s32 mode) {
    AnimationDescriptor15083568 *descriptor;
    u8 *record;
    u8 *records;
    u8 *created = 0;
    s32 i;

    animation--;
    descriptor = &D_80086CC4[(u32)animation];
    records = descriptor->records;
    i = 0;
    if (descriptor->count > 0) {
        record = records;
        do {
            if (record[3] == 0) {
                created = func_15083AC8(actor, record[1], record[0], 0,
                    record[2], record[4], record[5], record[6], scale);
            } else {
                created = func_15030AF4(actor, record[0], record[1], record[7],
                    record[4], record[5], mode, animation + 1, record[2],
                    record + 8, record[3] == 2 ? record[6] : -1, record[14], record[15]);
            }
            i++;
            record += 16;
        } while (i < descriptor->count);
    }
    return created;
}

s32 func_150836CC() {
    return 0;
}

extern u8 *D_800D1C90[];
extern u16 D_800C5A90[];
void func_15062BDC(u8 *, f32, f32);
s32 func_15084D00(u8 *);
u32 func_1502B020(u32 *, u32, ...);

void func_150837D4(s32 slot, s32 identity, s32 unused) {
    u8 *actor;
    u8 **resource;

    actor = D_800CC2D0 + (u32)slot * 0x32C;
    actor[4] = identity;
    if (identity == 255) {
        *(s16 *)(actor + 0xE4) = 0;
        *(s16 *)(actor + 0xE6) = 0;
        *(s16 *)(actor + 0xE8) = 0;
        *(s16 *)(actor + 0xD2) = 70;
        *(s16 *)(actor + 0xD4) = 70;
        *(s16 *)(actor + 0xD6) = 0;
        *(s16 *)(actor + 0x160) = 0;
        *(f32 *)(actor + 0xC8) = 0.0f;
    } else {
        resource = &D_800D1C90[identity];
        *(f32 *)(actor + 0xC8) = (f32)*(s16 *)(*resource + 6);
        func_15062BDC(actor, *(f32 *)(actor + 0x14C), *(f32 *)(actor + 0x150));
        actor[5] = (*resource)[0x12];
    }
    identity = func_15084D00(actor);
    actor[6] = identity;
    identity &= 255;
    if (D_800C5A90[identity] != 0) {
        *(u32 *)(actor + 0x58) = func_1502B020(NULL, 2, 2, identity);
    }
}

s32 func_150838EC() {
    return 0;
}

s32 func_150839B8() {
    return 0;
}

u8 *func_15083AC8(u8 *actor, s32 arg1, s32 arg2, s32 arg3,
    s32 arg4, s32 arg5, s32 arg6, s32 arg7, f32 scale) {
    return 0;
}

s32 func_15083DA0() {
    return 0;
}

s32 func_15083E0C() {
    return 0;
}

u8 *func_15083E90(u8 arg0) {
    return 0;
}

s32 func_15083FB0(u8 arg0) {
    u8 *temp_v0 = func_15083E90(arg0);

    if (temp_v0 != 0) {
        return ((s32)temp_v0 - (s32)D_800CC2D0) / 0x32C;
    }
    return -1;
}

s32 func_15084000(s32 arg0) {
    s32 temp_v0 = func_1505EEF4(arg0);

    if (temp_v0 != 0) {
        return (temp_v0 - (s32) D_800CC2D0) / 0x32C;
    }
    return -1;
}

s32 func_15084044() {
    return 0;
}

void func_1508434C(u8 *arg0) {
    s32 count = arg0[0x2C9];
    s32 i;

    if (count == 0) {
        count = 1;
    }
    for (i = 0; i < count; i++) {
        func_150843AC(arg0, i);
    }
}

s32 func_150843AC() {
    return 0;
}

s32 func_15084488() {
    return 0;
}

s32 func_15084558() {
    return 0;
}

s32 func_150849A0(u8 *arg0) {
    s32 temp_v1 = arg0[0x1C9];

    if (temp_v1 != 0) {
        return (*(u8 **) (arg0 + 0x2C4))[temp_v1 - 1];
    }
    return **(u8 **) (arg0 + 0x2C4);
}

s32 func_150849CC(u8 *arg0, s32 *arg1) {
    s32 index;
    s32 value;

    value = arg0[0x1C9];
    if (value != 0) {
        index = value - 1;
    } else {
        value = arg0[0x2C8];
        index = 0;
        if (value != 0) {
            index = value - 1;
        }
    }

    if (arg1 != NULL) {
        *arg1 = index;
    }
    return (*(u8 **) (arg0 + 0x2C4))[index];
}

s32 func_15084A18() {
    return 0;
}

void func_15084C30(struct127 *arg0) {
    register struct197 *record;
    register u32 remainder;

    if (arg0->id == 0x94) {
        record = arg0->unk2D0;
        remainder = (u32) func_150ADA20() % (s32) record->unk18;
        record->unk8 = remainder;
    }
}

s32 func_15084CB0(s32 arg0) {
    s32 found = 0;
    s32 i = 0;
    s32 count = D_800BE590;

    if (count > 0) {
        do {
            if (arg0 == D_800BE598[i]) {
                found = i;
                break;
            }
            i += 1;
        } while (i < count);
    }
    return found;
}
