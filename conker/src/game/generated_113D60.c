#include <ultra64.h>
extern s32 D_800D9A20[];
extern f32 D_800A1378;
extern f32 D_800BE9A4;
extern f32 *D_80088A44[6];
extern f32 D_800A1310;
extern f32 D_800A1314;
extern f32 D_800A1318;
extern f32 D_800A131C;
extern f32 D_800A1320;
extern f32 D_800A1324;
extern f32 D_800A1328;
extern f32 D_800A132C;
extern f32 D_800A1330;
extern f32 D_800A1334;
extern f32 D_800A1338;
extern f32 D_800A133C;
extern f32 D_800A1340;
extern f32 D_800A1344;
extern f32 D_800A1348;
extern f32 D_800A134C;
extern f32 D_800A1354;
extern f32 D_800A1358;
extern f32 D_800A135C;
extern f32 D_800A1360;
extern f32 D_800A1364;
extern s32 D_80088A5C[2];
extern u8 D_80088A64;
extern s32 D_80088A68[3];
extern s32 D_80088A74[3];
extern s32 D_800BE9E8;
extern u8 *D_800DBFF0;
extern s32 D_80088A80[4];
extern u8 D_800BE9EB;
extern u8 *D_800DCDC4;
typedef struct EventPair113D60 {
    s32 first;
    s32 second;
} EventPair113D60;
typedef struct EmitterPosition113D60 {
    f32 x;
    f32 y;
} EmitterPosition113D60;
typedef struct EmitterDescriptor113D60 {
    EmitterPosition113D60 position;
    f32 scale[2];
    u8 tag;
    u8 pad11;
    s16 id;
    u16 flags;
    s16 size0;
    s16 size1;
    u8 kind;
    u8 field1B;
    u8 field1C;
    u8 field1D;
    u8 duration;
    u8 field1F;
    u8 field20;
    u8 field21;
    u8 field22;
    u8 opacity;
    s32 field24;
    s32 field28;
    s32 field2C;
    s32 field30;
    s32 field34;
    s32 field38;
    s32 field3C;
    u8 field40;
    u8 field41;
    u8 reserved42[0x16];
} EmitterDescriptor113D60;
s32 func_1515548C(void *descriptor, s32 arg1, s32 *pair, s32 mode,
                 s32 arg4, u8 slot, s32 context);
typedef struct RandomPacket113D60 {
    u8 kind;
    u8 pad1;
    s16 duration;
    u8 count;
    u8 mode;
    s8 index;
    u8 pad7;
} RandomPacket113D60;
typedef struct CurvePayload113D60 {
    f32 value;
    f32 progress;
    s16 count;
    s16 cursor;
} CurvePayload113D60;

typedef struct WorldPosition113D60 {
    f32 x;
    f32 y;
    f32 z;
} WorldPosition113D60;

typedef struct WorldEmitterDescriptor113D60 {
    s16 field00;
    s16 field02;
    s16 field04;
    s16 field06;
    s32 field08;
    s32 field0C;
    WorldPosition113D60 position;
    f32 field1C;
    f32 field20;
    f32 field24;
    f32 field28;
    f32 field2C;
    f32 field30;
    s32 field34;
    s32 field38;
    f32 field3C;
    f32 field40;
    f32 field44;
    f32 field48;
    s16 field4C;
    s16 field4E;
    s16 field50;
    s16 field52;
    s16 field54;
    s16 field56;
    s8 field58;
    u8 pad59[3];
} WorldEmitterDescriptor113D60;
extern WorldPosition113D60 D_800A1290[8];
void func_151D3FF4(WorldPosition113D60 *position, u8 slot, s32 context);
void func_1514FCE8(WorldEmitterDescriptor113D60 *descriptor, u8 slot, s32 context);
s32 func_150E75A0(f32 *position, f32 scale, s16 id, u8 flags, s32 duration,
                 s32 opacity, s32 size0, s32 size1, s32 *pair, s32 mode,
                 u8 slot, s32 context);
s32 func_150E76D0(f32 scale, s16 id, u8 flags, u8 duration, s32 opacity,
                 s32 size0, s32 size1, s32 *pair, s32 mode, u8 slot, s32 context);
void func_10010F30(s32 arg0, u16 arg1, u8 arg2, s16 arg3, u8 arg4);
void func_15164F0C(u8 kind, u8 index, s32 arg2, u8 slot, s32 context);
s32 func_151D8868(void *packet, s32 arg1, s32 arg2, s32 arg3);
f32 func_150484A0(f32 x, f32 y);
f32 sqrtf(f32 value);
f32 func_150ADA68(void);
f32 func_151423D8(u8 angle);
s32 func_1514ECE0(void *node, s16 key, void **result);
void func_150E8930(void);
s32 func_150E8A80(void);
s32 func_150E90DC(void);
void func_15169260(void *pair, s32 count, s32 payload, u8 kind);
void *func_15149130(s16 arg0, s8 arg1, s8 arg2, s8 arg3, u8 arg4,
                    u8 arg5, s32 arg6, u8 arg7, s32 arg8);
void *func_151491F4(s16 arg0, s8 arg1, s8 arg2, u8 arg3, u8 arg4,
                    s32 arg5, u8 arg6, s32 arg7);
void func_1512D748(void *actor, s32 arg1, s32 arg2);
f32 func_15142A80(f32 parameter);
f32 func_15142AC0(f32 parameter);
f32 func_15142B04(f32 parameter);
f32 func_15142B44(f32 parameter);

/* Non-matching placeholders for the text-only asm slice asm/113D60.s. */

s32 func_150E68B0() {
    return 0;
}

s32 func_150E6B84() {
    return 0;
}

s32 func_150E6E34() {
    return 0;
}

void func_150E6ED8(u8 *arg0) {
    func_1514470C(D_800D9A20[func_150ADA20() & 1], arg0);
}

void func_150E6F18(f32 *output) {
    f32 *range = D_80088A44[(u32)func_150ADA20() % 6];
    f32 fraction = func_150ADA68();

    output[0] = range[0] + (range[3] - range[0]) * fraction;
    output[1] = range[1] + (range[4] - range[1]) * fraction;
    output[2] = range[2] + (range[5] - range[2]) * fraction;
}

void func_150E6FAC(f32 *output, u8 *actor) {
    void *node;
    u8 *record;
    f32 radius;
    s16 angle;
    f32 xOffset;
    f32 zOffset;

    if (func_1514ECE0(*(void **)(actor + 0x2F4), 0x16, &node)) {
        radius = func_150ADA68() * 100.0f + 80.0f;
        angle = func_150ADA20() & 0xFF;
        xOffset = func_151423D8((u8)(angle - 0x40));
        zOffset = func_151423D8((u8)angle);
        record = *(u8 **)((u8 *)node + 0x10);
        output[0] = (*(f32 *)(record + 0x38) * -80.0f + *(f32 *)(actor + 0x14)) + xOffset * radius;
        output[1] = (*(f32 *)(record + 0x3C) * -80.0f + *(f32 *)(actor + 0x18)) + 100.0f;
        output[2] = (*(f32 *)(record + 0x40) * -80.0f + *(f32 *)(actor + 0x1C)) + zOffset * radius;
    } else {
        output[0] = *(f32 *)(actor + 0x14);
        output[1] = *(f32 *)(actor + 0x18);
        output[2] = *(f32 *)(actor + 0x1C);
    }
}

void func_150E70CC(f32 *arg0, u8 *arg1) {
    arg0[0] = *(f32 *)(arg1 + 0x14);
    arg0[1] = *(f32 *)(arg1 + 0x18);
    arg0[2] = *(f32 *)(arg1 + 0x1C);
}

void func_150E70EC(s32 arg0, s32 arg1, f32 *vector, f32 *output) {
    output[0] = func_150484A0(vector[0], vector[2]);
    output[2] = func_150ADA68() * D_800A1310;
    output[4] = func_150ADA68() * D_800A1314;
    output[6] = func_150ADA68() * 0.5f;
    output[1] = func_150484A0(sqrtf(vector[2] * vector[2] + vector[0] * vector[0]), vector[1]) - D_800A1318;
    output[3] = func_150ADA68() * D_800A131C;
    output[5] = func_150ADA68() * D_800A1320;
    output[7] = func_150ADA68() * 0.5f;
}

void func_150E71E4(s32 arg0, s32 arg1, f32 *vector, f32 *output) {
    output[0] = func_150484A0(vector[0], vector[2]);
    output[2] = D_800A1324;
    output[4] = func_150ADA68() * D_800A1328;
    output[6] = func_150ADA68() * D_800A132C;
    output[1] = D_800A1330;
    output[3] = D_800A1334;
    output[5] = func_150ADA68() * D_800A1338;
    output[7] = func_150ADA68() * D_800A133C;
}

void func_150E7290(u8 index, u8 slot, s32 context) {
    s32 pair[2];
    f32 position[2];
    RandomPacket113D60 packet;
    f32 sample;
    u32 idWord;
    u32 durationWord;
    s32 flag0;
    s32 flag1;

    if (func_150ADA68() < D_800A1340) {
        pair[0] = D_80088A5C[0];
        pair[1] = D_80088A5C[1];
        if (func_150ADA68() < D_800A1344) {
            position[0] = func_150ADA68() * 300.0f + -150.0f;
            position[1] = func_150ADA68() * 200.0f + -100.0f;
            sample = func_150ADA68();
            idWord = (u32)func_150ADA20();
            flag0 = (func_150ADA20() & 1) ? 2 : 0;
            flag1 = (func_150ADA20() & 1) ? 4 : 0;
            durationWord = (u32)func_150ADA20();
            func_150E75A0(position, (sample * 150.0f + 200.0f) * D_800A1348,
                         (s16)(idWord % 201 + 500), (u8)(flag0 | flag1 | 9),
                         durationWord % 26 + 100, 255, 64, 3, pair, 2, slot, context);
        } else {
            sample = func_150ADA68();
            idWord = (u32)func_150ADA20();
            durationWord = (u32)func_150ADA20();
            func_150E76D0((sample * 100.0f + 150.0f) * D_800A134C,
                         (s16)(idWord % 201 + 500), 9, (u8)(durationWord % 26 + 100),
                         255, 64, 3, pair, 2, slot, context);
        }
        func_10010F30(0x360, 0x7FFF, 0, 0, 0);
        func_15164F0C(1, index, 0, slot, context);
        packet.kind = 1;
        packet.duration = (u32)func_150ADA20() % 26 + 25;
        packet.mode = 1;
        packet.count = (u32)func_150ADA20() % 6 + 3;
        packet.index = -1;
        func_151D8868(&packet, 0, 255, 0);
    }
}

s32 func_150E75A0(f32 *position, f32 scale, s16 id, u8 flags, s32 duration,
                 s32 opacity, s32 size0, s32 size1, s32 *pair, s32 mode,
                 u8 slot, s32 context) {
    EmitterDescriptor113D60 descriptor;
    u8 tag = D_80088A64;

    descriptor.position = *(EmitterPosition113D60 *)position;
    descriptor.tag = tag;
    descriptor.id = id;
    descriptor.flags = flags | 0x40;
    descriptor.size1 = size1;
    descriptor.field20 = 255;
    descriptor.field21 = 255;
    descriptor.kind = 4;
    descriptor.field1B = 255;
    descriptor.field1C = 230;
    descriptor.field1D = 190;
    descriptor.field1F = 255;
    descriptor.size0 = size0;
    descriptor.duration = duration;
    descriptor.scale[0] = scale;
    descriptor.scale[1] = scale;
    descriptor.field22 = 255;
    descriptor.field24 = 1;
    descriptor.field28 = 0;
    descriptor.field2C = 0;
    descriptor.field40 = 0;
    descriptor.field41 = 10;
    descriptor.field30 = 7;
    descriptor.field34 = 60;
    descriptor.field38 = 128;
    descriptor.field3C = 32;
    descriptor.opacity = opacity;
    return func_1515548C(&descriptor, 0, pair, mode, 0, slot, context);
}

s32 func_150E76D0(f32 scale, s16 id, u8 flags, u8 duration, s32 opacity,
                 s32 size0, s32 size1, s32 *pair, s32 mode, u8 slot, s32 context) {
    EmitterDescriptor113D60 descriptor;
    s32 sideTags[3];
    s32 topTags[3];
    u8 variant = func_150ADA20() & 3;

    descriptor.id = id;
    descriptor.flags = flags & 0xFFF9;
    descriptor.size0 = size0;
    descriptor.size1 = size1;
    descriptor.kind = 5;
    descriptor.field1B = 255;
    descriptor.field1C = 230;
    descriptor.field1D = 190;
    descriptor.duration = duration;
    descriptor.field1F = 255;
    descriptor.field20 = 255;
    descriptor.field21 = 255;
    descriptor.field22 = 255;
    descriptor.opacity = opacity;
    descriptor.field24 = 1;
    descriptor.field28 = 0;
    descriptor.field2C = 0;
    descriptor.field40 = 0;
    descriptor.field41 = 10;
    descriptor.field30 = 7;
    descriptor.field34 = 60;
    descriptor.field38 = 128;
    descriptor.field3C = 32;
    descriptor.scale[0] = scale;
    descriptor.scale[1] = scale;

    if (variant < 2) {
        sideTags[0] = D_80088A68[0];
        sideTags[1] = D_80088A68[1];
        sideTags[2] = D_80088A68[2];
        descriptor.tag = sideTags[(u32)func_150ADA20() % 3];
        descriptor.position.y = func_150ADA68() * 160.0f + -80.0f;
        if (variant == 0) {
            descriptor.position.x = 145.0f - scale;
            descriptor.flags |= 2;
        } else {
            descriptor.position.x = scale - 145.0f;
        }
    } else {
        topTags[0] = D_80088A74[0];
        topTags[1] = D_80088A74[1];
        topTags[2] = D_80088A74[2];
        descriptor.tag = topTags[(u32)func_150ADA20() % 3];
        descriptor.position.x = func_150ADA68() * 260.0f + -130.0f;
        if (variant == 2) {
            descriptor.position.y = 110.0f - scale;
            descriptor.flags |= 4;
        } else {
            descriptor.position.y = scale - 110.0f;
        }
    }
    return func_1515548C(&descriptor, 0, pair, mode, 0, slot, context);
}

void *func_150E7994(s16 count, f32 value, u8 slot, s32 context) {
    u8 *record;
    CurvePayload113D60 payload;
    RandomPacket113D60 packet;
    EmitterPosition113D60 controls[4];
    f32 *output;
    f32 parameter;
    f32 step;
    f32 weight2;
    f32 weight1;
    f32 weight0;
    f32 weight3;
    s16 i;

    if (count < 2) {
        return NULL;
    }
    func_1512D748(D_800DBFF0 + D_800BE9E8 * 0x9A0, 0, 1);
    packet.kind = 1;
    packet.duration = (u32)func_150ADA20() % 11 + 30;
    packet.count = 8;
    packet.index = -1;
    packet.mode = 1;
    func_151D8868(&packet, 0, 255, 0);

    payload.value = value;
    payload.count = count;
    payload.cursor = 0;
    payload.progress = 0.0f;
    record = func_151491F4(300, -1, 16, 1, 12, count * 8 + 16, slot, context);
    if (record != NULL) {
        memcpy(record + 0x28, &payload, sizeof(payload));
        controls[0].x = -146.0f;
        controls[0].y = func_150ADA68() * 160.0f - 80.0f;
        controls[1].x = -50.0f;
        controls[1].y = func_150ADA68() * 160.0f - 80.0f;
        controls[2].x = 50.0f;
        controls[2].y = func_150ADA68() * 160.0f - 80.0f;
        controls[3].x = 146.0f;
        controls[3].y = func_150ADA68() * 160.0f - 80.0f;
        parameter = -1.0f;
        step = 3.0f / (count - 1);
        output = (f32 *)(record + 0x38);
        for (i = 0; i < count; i++) {
            weight2 = func_15142B04(parameter);
            weight1 = func_15142AC0(parameter);
            weight0 = func_15142A80(parameter);
            weight3 = func_15142B44(parameter);
            output[i * 2] = ((weight0 * controls[0].x + weight1 * controls[1].x) +
                weight2 * controls[2].x) + controls[3].x * weight3;
            weight2 = func_15142B04(parameter);
            weight1 = func_15142AC0(parameter);
            weight0 = func_15142A80(parameter);
            weight3 = func_15142B44(parameter);
            output[i * 2 + 1] = ((weight0 * controls[0].y + weight1 * controls[1].y) +
                weight2 * controls[2].y) + controls[3].y * weight3;
            parameter += step;
        }
    }
    return record;
}

void func_150E7C9C(u8 *record) {
    CurvePayload113D60 *payload = (CurvePayload113D60 *)(record + 0x28);
    /* Only X/Y are initialized; the third slot retains the retail frame extent. */
    f32 position[3];
    f32 sample;
    s32 flag0;
    s32 flag1;

    payload->progress += payload->value * D_800BE9A4;
    while (payload->progress > 1.0f && payload->cursor != payload->count) {
        position[0] = ((f32 *)payload)[payload->cursor * 2 + 4];
        position[1] = ((f32 *)payload)[payload->cursor * 2 + 5];
        sample = func_150ADA68();
        flag0 = (func_150ADA20() & 1) ? 4 : 0;
        flag1 = (func_150ADA20() & 1) ? 2 : 0;
        func_150E75A0(position, sample * 12.0f + 30.0f, 300, (u8)(flag1 | flag0),
                     (u32)(func_150ADA68() * 25.0f + 100.0f), 255, 1, 255,
                     NULL, 0, record[0xC], record[1]);
        func_10010F30(0x360, 0x7FFF, (u8)(position[0] * 0.4315068424f + 64.0f), 0, 0);
        payload->progress -= 1.0f;
        payload->cursor++;
    }
    if (payload->cursor >= payload->count) {
        *(s16 *)(record + 0xE) = -1;
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_113D60/func_150E7FEC.s")

void func_150E81A8(u8 index, u8 slot, s32 context) {
    WorldPosition113D60 position;
    WorldEmitterDescriptor113D60 descriptor;
    RandomPacket113D60 packet;

    if (index == 4 || index == 5 || index == 6 || index == 7) {
        position = D_800A1290[index];
        position.y += 200.0f;
        func_151D3FF4(&position, slot, context);
        descriptor.field00 = 0;
        descriptor.field02 = 255;
        descriptor.field04 = -64;
        descriptor.field06 = 77;
        descriptor.field08 = 10;
        descriptor.field0C = 5;
        descriptor.position = position;
        descriptor.field1C = 252.0f;
        descriptor.field20 = 117.0f;
        descriptor.field24 = 308.0f;
        descriptor.field28 = 256.0f;
        descriptor.field2C = D_800A1354;
        descriptor.field30 = D_800A1358;
        descriptor.field34 = 4;
        descriptor.field38 = 7;
        descriptor.field3C = 27.0f;
        descriptor.field40 = D_800A135C;
        descriptor.field44 = D_800A1360;
        descriptor.field48 = D_800A1364;
        descriptor.field4C = 25;
        descriptor.field4E = 15;
        descriptor.field50 = 100;
        descriptor.field52 = 100;
        descriptor.field54 = 12;
        descriptor.field56 = 20;
        descriptor.field58 = 0;
        func_1514FCE8(&descriptor, slot, context);
        packet.kind = 1;
        packet.duration = (u32)func_150ADA20() % 11 + 30;
        packet.count = 8;
        packet.index = -1;
        packet.mode = 1;
        func_151D8868(&packet, 0, 255, 0);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_113D60/func_150E83AC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_113D60/func_150E8470.s")

s32 func_150E8824(u8 *arg0, u8 arg1) {
    func_15131828(arg0, arg0 + 0xAC, arg0 + 0xA8, arg0 + 0xAA);
    return 1;
}

void func_150E8854(void) {
    f32 payload;
    void *result;

    payload = 10.0f;
    result = func_15149130(0x12C, -1, 0x35, -1, 0, 0, 4, 0xFF, 1);
    if (result != 0) {
        memcpy((u8 *) result + 0x28, &payload, 4);
    }
}

void func_150E88C0(u8 *arg0) {
    f32 *timer = (f32 *) (arg0 + 0x28);

    *timer -= D_800BE9A4;
    if (*timer < 0.0f) {
        *timer = func_150ADA68() * D_800A1378 + 201.0f;
        func_150E8930();
    }
}

void func_150E8930(void) {
    EventPair113D60 pair = *(EventPair113D60 *)D_80088A80;
    RandomPacket113D60 packet;

    func_15169260(&pair, 2, 0, 0x1B);
    func_15164F0C(0, D_800BE9EB, 0, 0xFF, 1);
    packet.kind = 1;
    packet.duration = (u32)func_150ADA20() % 21 + 20;
    packet.mode = 1;
    packet.count = (u32)func_150ADA20() % 6 + 3;
    packet.index = -1;
    func_151D8868(&packet, 0, 255, 1);
    if (D_800DCDC4 != NULL) {
        func_150E8A80();
    }
    if (D_800DCDC4 != NULL) {
        func_150E90DC();
    }
    func_10010F30(0x4C8, 0x7FFF, 0x40, (s16)(0x200 - (func_150ADA20() & 0x400)), 0);
    func_10010F30(0x4CD, 0x5DC0, 0x40, (s16)(0x200 - (func_150ADA20() & 0x400)), 0);
}

s32 func_150E8A80() {
    return 0;
}

s32 func_150E8B1C() {
    return 0;
}

s32 func_150E8D5C() {
    return 0;
}

s32 func_150E90DC() {
    return 0;
}

s32 func_150E9178() {
    return 0;
}

s32 func_150E93DC() {
    return 0;
}

s32 func_150E971C() {
    return 0;
}
