#include <ultra64.h>

#include "functions.h"
/* This owner reads the retail base-pointer word at D_800D3098. */
#define D_800D3098 D_800D3098_legacy_array
#include "variables.h"
#undef D_800D3098

typedef struct {
    u8 reserved[0x15];
    u8 kindFlags;
    u8 tail[0x1E];
} DispatchRecord40490;
typedef s32 (*RecordCallback40490)(DispatchRecord40490 *);
extern DispatchRecord40490 *D_800D3098;
extern RecordCallback40490 D_80082E30[];
typedef void (*RecordModeCallback40490)(u8 *, f32);
extern RecordModeCallback40490 D_80082F28[];
extern f32 D_80096650;
extern u8 D_800C35E8;

/* Generated placeholder declarations. */
void func_15013000(void);
s32 func_150130B4();
s32 func_15013778();
s32 func_150139AC();
s32 func_15013DE8();
s32 func_150142EC();
s32 func_150144B8();
s32 func_1501474C();
s32 func_15014B60();
s32 func_15014F6C(DispatchRecord40490 *record);
s32 func_150151D4();
s32 func_15015354();
s32 func_150156F4();
/* End generated placeholder declarations. */
u8 *func_1515F1B0(u8 *arg0);
void *func_1515D088(void *);
void *func_151CD2C0(void *source, u8 variant, s32 parameter);

s32 func_151BE850(struct17 *arg0, s32 arg1, u8 arg2, u8 arg3, u8 arg4, u8 arg5, u8 arg6);
void func_151A9390(u8 arg0, u8 arg1, const void *position, const f32 *floatPosition, f32 arg4, f32 arg5, s32 arg6, u8 arg7, s32 arg8);

void func_15012FE0(void) {
    D_800BE570 = 0;
    D_800BE574 = 0;
    D_800BE575 = 0;
}

/* Reset both accumulators and dispatch each record's type callback. */
void func_15013000(void) {
    u8 kindFlags;
    u32 index;
    RecordCallback40490 callback;

    D_800DCDC4 = 0;
    D_800DCD90 = 0.0f;
    for (index = 0; index < (u32)D_800D3094; index++) {
        kindFlags = D_800D3098[index].kindFlags;
        callback = D_80082E30[(u8)(kindFlags >> 2)];
        if (callback != NULL) {
            callback(&D_800D3098[index]);
        }
    }
}
// requires jump table
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150130B4.s. */
s32 func_150130B4() {
    return 0;
}

s32 func_1501370C(struct16 *arg0) {
    u8 idx = arg0->unk17;
    void (*func)(void) = D_80082EA0[idx];

    if (func != NULL) {
        func();
    }
    return 1;
}

s32 func_1501374C(struct16 *arg0) {
    arg0->unk16 |= 4;
    func_1515D088(arg0);
    return 1;
}

// fat struct definition:
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15013778.s. */
s32 func_15013778() {
    return 0;
}

s32 func_1501396C(struct16 *arg0) {
    u8 idx = arg0->unk17;
    void (*func)(void) = D_80082ECC[idx];

    if (func != NULL) {
        func();
    }
    return 1;
}

// another struct
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150139AC.s. */
s32 func_150139AC() {
    return 0;
}

/* Dispatch the record's scaled value unless the current mode suppresses it. */
s32 func_15013C38(u8 *record) {
    RecordModeCallback40490 callback;
    s32 mode;
    f32 scaled;

    record[0x16] |= 4;
    mode = *(s32 *)(record + 0x18);
    if ((((u8 *)D_800D2E4C)[0x11] & 4) && D_800BE9F0 == 0x13) {
        return 1;
    }
    if (D_800C35EA == 1 &&
        (D_800C35E8 == 0xF || D_800C35E8 == 0x10 ||
         D_800C35E8 == 0x11)) {
        return 1;
    }
    if (mode >= 6) {
        return 1;
    }
    callback = D_80082F28[mode];
    if (callback != NULL) {
        scaled = (f32)*(u32 *)(record + 0x1C) * D_80096650;
        callback(record, scaled);
    }
    return 1;
}

s32 func_15013D38(u8 *arg0) {
    struct17 tmp;
    s32 storedValue;
    s32 value;

    arg0[0x16] |= 4;
    tmp.unk0 = *(s16 *)(arg0 + 0);
    tmp.unk4 = *(s16 *)(arg0 + 2);
    tmp.unk8 = *(s16 *)(arg0 + 4);

    storedValue = *(s32 *)(arg0 + 0x18);
    value = storedValue != 0 ? storedValue : 1;

    func_151BE850(&tmp, *(s32 *)(arg0 + 0x10), value, arg0[0x1F], 1, 0xFF, 1);
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15013DE8.s. */
s32 func_15013DE8() {
    return 0;
}

s32 func_15013F9C(void *source) {
    func_151CD2C0(source, 0xFF, 1);
    return 1;
}

s32 func_15013FC4(struct133 *arg0) {
    u8 idx = arg0->unk1B;
    void (*func)(void) = D_80082F40[idx];

    if (func != NULL) {
        func();
    }
    return 1;
}

s32 func_15014004(struct134 *arg0) {
    s32 temp_v1 = arg0->unk1C;
    if (temp_v1 < 0) {
        return 1;
    }
    if (temp_v1 >= 6) {
        return 1;
    }
    D_800E0900[temp_v1] = arg0;
    return 1;
}

s32 func_15014040(struct134 *arg0) {
    s32 temp_v0 = arg0->unk18;
    arg0->unk16 |= 4;
    if (temp_v0 == 0) {
        D_800D9A20 = arg0;
    } else if (temp_v0 == 1) {
        D_800D9A24 = arg0;
    }
    return 1;
}

s32 func_1501407C(s32 arg0) {
    D_800D987C = (u8)0;
    return 1;
}

/* Spawn a type-0x21 effect with the original partially initialized record. */
s32 func_15014094(u8 *record) {
    /* Retail copies the untouched payload bytes; do not clear this buffer. */
    u8 data[0x34];
    u8 *effect;

    record[0x16] |= 4;
    *(void **)(data + 0) = record;
    *(f32 *)(data + 4) = func_15144598((struct134 *)record);
    *(f32 *)(data + 8) = 0.0f;
    func_1510F800(0);
    *(s32 *)(data + 0xC) = (s32)func_1510FD20(*(s16 *)(record + 0), *(s16 *)(record + 4));
    data[0x2C] = 0;
    effect = (u8 *)func_15149130(0x12C, -1, 0x21, -1, 0, 0, (struct37 *)0x34, 0xFF, 1);
    if (effect != NULL) {
        memcpy(effect + 0x28, data, 0x34);
    }
    /* The record dispatcher ignores this callback's incidental return value. */
}
/* Submit record effect flags, inverting bit 1 and preserving bits 0..4. */
s32 func_15014144(u8 *record) {
    s32 bits = *(s32 *)(record + 0x18);

    func_151A9390((bits & 1 ? 1 : 0) | (bits & 2 ? 0 : 2) | (bits & 4 ? 4 : 0) | (bits & 8 ? 8 : 0) | (bits & 0x10 ? 0x10 : 0), record[0x1F], record, NULL,
        *(f32 *)&D_8009667C, 100.0f, -1, 0xFF, 1);
    return 1;
}

s32 func_15014220(u8 *arg0) {
    struct {
        f32 unk0;
        void *unk4;
        u8 unk8;
        u8 pad[3];
    } data;
    u8 *temp_v0;

    arg0[0x16] |= 4;
    data.unk0 = 0.0f;
    data.unk4 = arg0;
    data.unk8 = 1;

    temp_v0 = (u8 *)func_15149130(0x12C, -1, 0x26, -1, 0, 0x24, (struct37 *)0xC, 0xFF, 0);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0xC);
    }
    return 1;
}
s32 func_150142AC(u8 *arg0) {
    s32 idx;

    arg0[0x16] |= 4;
    idx = arg0[0x1B];
    if ((idx < 0) || (idx >= 3)) {
        return 1;
    }
    D_800D9AA0[idx] = (struct134 *)arg0;
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150142EC.s. */
s32 func_150142EC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150144B8.s. */
s32 func_150144B8() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_1501474C.s. */
s32 func_1501474C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15014B60.s. */
s32 func_15014B60() {
    return 0;
}
typedef struct {
    u8 *owner;
    u32 minimum;
    u32 extraRange;
    u32 selected;
    f32 matrix[4][4];
    u8 mode;
    u8 variant;
    u8 padding52[2];
} RandomizedEffectPacket40490;

/* Snapshot the range, build the transform, then attach the complete effect packet. */
s32 func_15014F6C(DispatchRecord40490 *record) {
    RandomizedEffectPacket40490 packet;
    u8 *source = (u8 *)record;
    u8 *result;
    s32 mode;

    source[0x16] |= 4;
    packet.variant = *(u32 *)(source + 0x20);
    mode = (*(u32 *)(source + 0x1C) & 1) ? 1 : 0;
    packet.mode = mode;
    packet.owner = source;
    packet.minimum = *(u32 *)(source + 0x18) & 0xFFFF;
    packet.extraRange = (*(u32 *)(source + 0x18) >> 16) & 0xFFFF;
    packet.selected = (u32)func_150ADA20() % (packet.extraRange + 1) + packet.minimum;
    func_150A8050(packet.matrix, *(f32 *)(source + 0x0C), *(f32 *)(source + 0x10), 0.0f);
    packet.matrix[3][0] = *(s16 *)(source + 0);
    packet.matrix[3][1] = *(s16 *)(source + 2);
    packet.matrix[3][2] = *(s16 *)(source + 4);
    /* The existing factory declaration carries the payload size in a pointer-typed word. */
    result = (u8 *)func_15149130(300, -1, 0x31, -1, 0, 0x2A, (struct37 *)sizeof(packet), 0xFF, 0);
    if (result != NULL) {
        memcpy(result + 0x28, &packet, sizeof(packet));
    }
    return 1;
}

s32 func_150150A4(u8 *arg0) {
    u8 *temp_v0 = func_1515F1B0(arg0);
    if (temp_v0 == NULL) {
        return 1;
    }

    func_1515F25C(&D_800DCDC4, temp_v0);
    D_800DCD90 += *(f32 *)(temp_v0 + 8);
    return 1;
}

s32 func_15015104(u8 *arg0) {
    struct {
        void *unk0;
        u8 unk4;
        u8 pad5[3];
        s32 unk8;
        u8 unkC;
        u8 padD[3];
        s32 unk10;
    } data;
    u8 *temp_v0;
    s32 flags;

    arg0[0x14] = 1;
    data.unk0 = arg0;
    data.unk4 = *(s32 *)(arg0 + 0x1C);
    func_1510F800(0);
    data.unk8 = (s32)func_1510FD20(*(s16 *)(arg0 + 0), *(s16 *)(arg0 + 4));

    flags = *(s32 *)(arg0 + 0x20);
    data.unkC = (flags ? 1 : 0) | (flags ? 2 : 0);
    data.unk10 = 0;

    temp_v0 = (u8 *)func_15149130(0x12C, -1, -1, -1, 0, 0x2C, (struct37 *)0x14, 0xFF, 0);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0x14);
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150151D4.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_40490/func_150151D4.s")

s32 func_15015300(struct134 *arg0) {
    void (*func)(void);
    s32 idx = arg0->unk1C;

    if ((idx < 0) || (idx >= 2)) {
        return 1;
    }

    func = D_80082F70[idx];
    if (func != NULL) {
        func();
    }

    return 1;
}


/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15015354.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_40490/func_15015354.s")
s32 func_15015644(u8 *arg0) {
    struct {
        void *unk0;
        f32 unk4;
        s32 unk8;
        u8 unkC;
        u8 padD[3];
    } data;
    u8 *temp_v0;

    arg0[0x16] |= 4;
    arg0[0x14] = 1;
    data.unk0 = arg0;
    data.unk4 = func_15144598((struct134 *)arg0);
    func_1510F800(0);
    data.unk8 = (s32)func_1510FD20(*(s16 *)(arg0 + 0), *(s16 *)(arg0 + 4));
    data.unkC = 0;

    temp_v0 = (u8 *)func_15149130(0x12C, -1, 0x44, -1, 0, 0x2F, (struct37 *)0x10, 0xFF, 0);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0x10);
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150156F4.s. */
s32 func_150156F4() {
    return 0;
}
