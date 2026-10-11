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

void func_150302F0(u8 *, s32);
u8 *func_1505F0AC(u8);
void func_15060F28(u8 *, s32);

void func_150836CC(u8 *actor, s32 animation) {
    AnimationDescriptor15083568 *descriptor;
    u8 *record;
    u8 *records;
    u8 *child;
    s32 i;

    func_150302F0(actor, animation);
    animation--;
    descriptor = &D_80086CC4[(u32)animation];
    records = descriptor->records;
    i = 0;
    if (descriptor->count > 0) {
        record = records;
        do {
            if (record[3] == 0) {
                child = func_1505F0AC(record[0]);
                if (child != NULL) {
                    if ((s32)((u32)actor - (u32)D_800CC2D0) / 0x32C + 1 == child[0x65]) {
                        func_15060F28(child, 0);
                    }
                }
            }
            i++;
            record += 16;
        } while (i < descriptor->count);
    }
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

extern u32 D_800D1588[];
void *allocate_memory(s32, s32, s32, s32);
void func_1505E650(u8 *, u16, f32, f32, f32, f32, s32);

s32 func_150838EC(u8 *actor, s32 state, s32 mode, f32 scale) {
    s32 identity;
    u8 *allocated;
    u8 *destination;

    identity = actor[4];
    if (D_800D1588[identity] == 0) {
        return 0;
    }
    if (D_800C5A90[identity] == 0) {
        return 0;
    }
    allocated = allocate_memory(0x3E0, 1, 2, 0);
    destination = actor;
    *(u8 **)(destination + 0x2D0) = allocated;
    if (allocated == NULL) {
        return 1;
    }
    bzero(*(u8 **)(destination + 0x2D0), 0x40);
    func_1505E650(actor, (u16)state, scale, 0.0f, 0.0f, 0.0f, mode);
    return 0;
}

extern u32 D_80086CAC[];
void func_15036C70(u8 *);

void func_150839B8(u8 *actor, s32 identity, u8 *configuration) {
    u8 *resource;
    u16 value;

    if (identity != 255) {
        resource = D_800D1C90[identity];
        if (configuration != NULL) {
            value = *(u16 *)(configuration + 0x2C);
            if (value == 0) {
                *(u16 *)(actor + 0x10) = *(u16 *)(resource + 0x2A);
            } else if (value == 1) {
                *(u16 *)(actor + 0x10) = 0;
            } else {
                *(u16 *)(actor + 0x10) = value;
            }
            if (D_800BE9F0 == 0x1D) {
                *(u16 *)(actor + 0x10) = 1000;
            }
        } else {
            *(u16 *)(actor + 0x10) = 0;
        }
        actor[0x13B] = resource[0x39];
        actor[0x2CB] = *(s8 *)(resource + 0x33);
        *(u32 *)(actor + 0x2CC) = *(u32 *)(resource + 0x34);
        actor[5] = resource[0x12];
        actor[0x68] = resource[0x3B];
        actor[0x69] = resource[0x3C];
        *(s16 *)(actor + 0x160) = *(s16 *)(resource + 2);
        if (resource[4] != 0) {
            *(u32 *)(actor + 0x2C4) = D_80086CAC[resource[5]];
            actor[0x2C8] = resource[4];
        }
        actor[0x2C9] = resource[0x38] + actor[0x2C8];
        if (resource[0x29] != 0) {
            func_15036C70(actor);
        }
    }
}

extern u8 D_800CC2D0[];
extern u8 *D_800D1C90[];
extern s32 D_80082FA0;
extern u8 D_800C35EA, D_800C3638;
void func_1503D774(s32, s32);
void func_1503D660(s32, s32);
u8 *func_1505ED34(void);
void func_150615DC(u8 *);
u32 func_1515D480(s32);
u32 func_1515D440(void);
void func_150837D4(s32, s32, s32);

u8 *func_15083AC8(u8 *actor, s32 attachment, s32 identity, s32 kind,
    s32 value, s32 flags, s32 inheritScale, s32 state, f32 scale) {
    u8 *created;
    u8 *cursor;
    s32 i;
    s32 mode;
    s32 active;
    u32 bits;
    u32 maskedBits;
    u32 magnitude;
    s32 parentSlot;

    func_1503D774(identity, 0);
    func_1503D660(identity, 0);
    created = func_1505ED34();
    created[0x3B] = 255 - (s32)((u32)created - (u32)D_800CC2D0) / 0x32C;
    created[0xAB] = kind;
    *(s32 *)(created + 0) = value;
    func_150615DC(created);
    parentSlot = (s32)((u32)actor - (u32)D_800CC2D0) / 0x32C + 1;
    created[0x232] = 1;
    created[0x1CA] = 1;
    created[0x125] = 255;
    /* Preserve retail's ordered status stores, including the repeated flag writes. */
    *(volatile u8 *)(created + 0x65) = parentSlot;
    *(volatile s32 *)(created + 0x5C) = attachment;
    *(volatile u8 *)(created + 0x123) = 1;
    *(volatile u8 *)(created + 4) = identity;
    bits = actor[0x66];
    *(volatile u8 *)(created + 0x66) = bits;
    maskedBits = bits & ~0x10;
    *(volatile u8 *)(created + 0x66) = maskedBits;
    *(volatile u8 *)(created + 0x66) = maskedBits;
    created[0x1DD] = actor[0x1DD];
    created[0x1DE] = actor[0x1DE];
    created[0x1DF] = actor[0x1DE];
    created[0x1E0] = actor[0x1E0];
    created[0x1E1] = actor[0x1E1];
    created[0x1E2] = actor[0x1E2];
    if (inheritScale == 0) {
        *(f32 *)(created + 0x14C) = 1.0f;
        *(f32 *)(created + 0x150) = 1.0f;
        *(f32 *)(created + 0x154) = 1.0f;
        *(f32 *)(created + 0x158) = 1.0f;
    } else {
        *(f32 *)(created + 0x14C) = *(f32 *)(actor + 0x14C);
        *(f32 *)(created + 0x150) = *(f32 *)(actor + 0x150);
        *(f32 *)(created + 0x154) = *(f32 *)(actor + 0x154);
        *(f32 *)(created + 0x158) = *(f32 *)(actor + 0x158);
    }
    created[0x101] = inheritScale;
    created[0xAC] = flags;
    func_1503D774(identity, 0);
    if (flags & 1) {
        *(u32 *)(created + 0xF8) |= 0x4000;
        magnitude = *(volatile u16 *)(D_800D1C90[identity] + 0xE);
        *(f32 *)(created + 0x270) = (f32)magnitude * *(volatile f32 *)(created + 0x14C);
    }
    mode = 0;
    if (flags & 2) {
        mode = 1;
    }
    i = 0;
    cursor = created;
    if (D_80082FA0 >= 0) {
        do {
            *(u32 *)(cursor + 0x304) = func_1515D480(1);
            i++;
            cursor += 4;
        } while (i <= D_80082FA0);
    }
    if (*(u32 *)(created + i * 4 + 0x300) != 0) {
        created[0x301] = 1;
    }
    *(u32 *)(created + 0x314) = func_1515D440();
    if (D_800C35EA == 1) {
        active = 1;
    } else {
        active = 0;
    }
    if (active) {
        D_800C3638 = 0;
    }
    func_150839B8(created, identity, 0);
    func_150837D4((s32)((u32)created - (u32)D_800CC2D0) / 0x32C, identity, 1);
    func_150838EC(created, state, mode, scale);
    if (active) {
        D_800C3638 = 1;
    }
    return created;
}

typedef struct {
    u8 padding[0x28];
    u8 identity;
    u8 tail[7];
} IndexRecord15083E0C;
extern IndexRecord15083E0C *D_800D20FC;

s32 func_15083DA0(void) {
    s32 identity = 1;
    s32 i;

    for (i = 0; i < D_800D2100; i++) {
        if (D_800D20FC[i].identity == identity) {
            identity++;
            i = 0;
        }
    }
    if (identity >= 0x100) {
        identity = 0xFF;
    }
    return identity;
}

s32 func_15083E0C(u8 selector) {
    s32 i;

    if (selector == 0) {
        return -1;
    }
    for (i = 0; i < D_800D2100; i++) {
        if (D_800D20FC[i].identity == selector) {
            return &D_800D20FC[i] - D_800D20FC;
        }
    }
    return -1;
}

u8 *func_15083E90(u8 selector) {
    u8 *actor;
    s32 i;

    if (selector == 0) {
        return NULL;
    }
    actor = D_800CC2D0;
    for (i = 0; i < 26; i++, actor += 0x32C) {
        if ((*(s32 *)actor != 0) && (actor[0x3B] == selector)) {
            return actor;
        }
    }
    return NULL;
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
