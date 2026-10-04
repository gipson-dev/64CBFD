#include <ultra64.h>
#include "structs.h"
extern void *D_800D9A20[];
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
extern f32 D_800A137C;
extern f32 D_800A1380;
extern f32 D_800A1384;
extern f32 D_800A1388;
extern f32 D_800A138C;
extern f32 D_800A1390;
extern f32 D_800A1394;
extern f32 D_800A1398;
extern f32 D_800A139C;
extern f32 D_800A13A0;
extern f32 D_800A13A4;
extern f32 D_800A13A8;
extern f32 D_800A13AC;
extern f32 D_800A13B0;
extern f32 D_800A13B4;
extern f32 D_800A13B8;
extern f32 D_800A13BC;
extern f32 D_800A13C0;
extern f32 D_800A13C4;
extern u8 D_800A12F0[];
extern f32 D_800A12F4[];
extern f32 D_800A13C8;
extern f32 D_800A13CC;
extern f32 D_800A13D0;
extern f32 D_800A13D4;
extern f32 D_800A13D8;
extern f32 D_800A13DC;
extern f32 D_800A13E0;
extern f32 D_800A13E4;
extern s32 D_80088A5C[2];
extern u8 D_80088A64;
extern s32 D_80088A68[3];
extern s32 D_80088A74[3];
extern s32 D_800BE9E8;
extern u8 *D_800DBFF0;
extern s32 D_80088A80[4];
extern u8 D_800BE9EB;
extern u8 *D_800DCDC4;
extern f32 D_800DCD90;
typedef struct EventPair113D60 {
    s32 first;
    s32 second;
} EventPair113D60;
typedef struct EventPayload113D60 {
    f32 field00;
    f32 field04;
    f32 field08;
} EventPayload113D60;
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
typedef struct EventPositionPayload113D60 {
    WorldPosition113D60 position;
    EventPayload113D60 parameters;
} EventPositionPayload113D60;

typedef struct ExtendedEventPositionPayload113D60 {
    EventPositionPayload113D60 payload;
    f32 field18;
    u8 reserved1C[0x14];
    s32 field30;
    u8 field34;
    u8 field35;
    u8 reserved36[2];
    s32 field38;
} ExtendedEventPositionPayload113D60;

typedef struct EventWeightNode113D60 {
    void *descriptor;
    s32 field04;
    f32 weight;
    struct EventWeightNode113D60 *next;
} EventWeightNode113D60;

typedef struct ChildEmissionDescriptor113D60 {
    u32 field00;
    u32 field04;
    s16 field08;
    s16 field0A;
    u32 field0C;
    u32 field10;
    u8 field14;
    u8 field15;
    u8 field16;
    u8 field17;
    u8 field18;
    u8 field19;
    u8 field1A;
    u8 field1B;
    u8 field1C;
    u8 field1D;
    s16 field1E;
    s16 field20;
    s16 field22;
    f32 field24;
    f32 field28;
    f32 field2C;
    vertex position;
    f32 field3C;
    f32 field40;
    f32 field44;
    f32 field48;
    f32 field4C;
    f32 field50;
    f32 field54;
    u32 flags;
    u8 reserved5C[4];
    u8 field60;
    u8 field61;
    u8 field62;
    u8 field63;
    u8 reserved64[0xC];
} ChildEmissionDescriptor113D60;

typedef struct ExtendedChildEmissionDescriptor113D60 {
    f32 field00;
    f32 field04;
    f32 field08;
    f32 field0C;
    f32 field10;
    f32 field14;
    f32 field18;
    f32 field1C;
    f32 field20;
    f32 field24;
    vertex position;
    f32 field34;
    f32 field38;
    f32 field3C;
    f32 field40;
    f32 field44;
    f32 field48;
    f32 field4C;
    u32 flags;
    s16 field54;
    u16 resource;
    u8 field58;
    u8 reserved59[3];
    u32 field5C;
    u8 field60;
    u8 field61;
    u8 field62;
    u8 field63;
    u8 field64;
    u8 field65;
    u8 field66;
    u8 field67;
    u8 field68;
    u8 reserved69;
    u8 field6A;
    u8 reserved6B;
    u32 field6C;
    u8 field70;
    u8 reserved71;
    s16 field72;
    s16 field74;
    u8 reserved76[6];
} ExtendedChildEmissionDescriptor113D60;

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
void func_1514470C(void *descriptor, void *position);
f32 *func_15144B34(s32 player);
void func_151436B4(f32 angle0, f32 angle1, f32 radius, vertex *position);
void *func_15130374(void *descriptor, u8 mode, s32 payloadBytes, u8 slot, s32 context);
void *func_15132A4C(void *descriptor, s32 resource, s32 value, s32 payloadBytes,
                  u8 slot, s32 context);
s32 func_1514ECE0(void *node, s16 key, void **result);
void func_150E8930(void);
void func_150E8A80(void);
void func_150E90DC(void);
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

void func_150E8A80(void) {
    void *result;
    EventPayload113D60 payload;

    payload.field00 = D_800A137C;
    payload.field04 = D_800A1380;
    payload.field08 = 0.0f;
    result = func_15149130((s16)((u32)func_150ADA20() % 41 + 30), -1, 0x33, -1,
                          1, 0, 12, 0xFF, 1);
    if (result != NULL) {
        memcpy((u8 *)result + 0x28, &payload, 12);
    }
}

void func_150E8B1C(u8 *record) {
    void *result;
    f32 limit;
    f32 first;
    f32 second;
    EventPayload113D60 *payload;
    EventWeightNode113D60 *node;
    f32 *origin;
    f32 fraction;
    f32 dx;
    f32 dy;
    f32 dz;
    EventPositionPayload113D60 child;

    origin = func_15144B34(D_800BE9E8);
    fraction = func_150ADA68();
    payload = (EventPayload113D60 *)(record + 0x28);
    payload->field08 += ((payload->field00 + fraction * payload->field04) * D_800BE9A4) * D_800DCD90;
    if (payload->field08 > 1.0f) {
        second = D_800A1384;
        first = D_800A1388;
        limit = D_800A138C;

        do {
            fraction = func_150ADA68();
            fraction *= D_800DCD90;
            node = (EventWeightNode113D60 *)D_800DCDC4;
            while (node->weight < fraction) {
                fraction -= node->weight;
                node = node->next;
            }
            func_1514470C(node->descriptor, &child.position);
            dx = child.position.x - origin[0];
            dy = child.position.y - origin[1];
            dz = child.position.z - origin[2];
            if ((dx * dx + dy * dy) + dz * dz < limit) {
                s16 duration;

                child.parameters.field00 = first;
                child.parameters.field04 = second;
                child.parameters.field08 = 0.0f;
                duration = (u32)func_150ADA20() % 13 + 5;
                result = func_15149130(duration, -1, 0x34, -1,
                                      1, 0, 24, record[0xC], record[1]);
                if (result != NULL) {
                    memcpy((u8 *)result + 0x28, &child, 24);
                }
            }
            payload->field08 -= 1.0f;
        } while (payload->field08 > 1.0f);
    }
}

void func_150E8D5C(u8 *record) {
    void *result;
    EventPositionPayload113D60 *payload;
    ChildEmissionDescriptor113D60 descriptor;
    f32 fraction;
    f32 bonus;
    f32 period;
    f32 angle0;
    f32 angle1;
    f32 radius;
    u32 firstFlag;
    u32 secondFlag;
    s16 size;

    fraction = func_150ADA68();
    payload = (EventPositionPayload113D60 *)(record + 0x28);
    payload->parameters.field08 += (payload->parameters.field00 + fraction * payload->parameters.field04) * D_800BE9A4;
    if (payload->parameters.field08 > 1.0f) {
        bonus = D_800A1390;
        period = D_800A1394;
        /* Reserved bytes have no retail initializer; write only defined fields. */
        descriptor.field00 = 0x200005;
        descriptor.field04 = 0;
        descriptor.field08 = 0xE01;
        descriptor.field0C = 0;
        descriptor.field10 = 0;
        descriptor.field17 = 255;
        descriptor.field1C = 255;
        descriptor.field1D = 0x16;
        descriptor.field1E = 30;
        descriptor.field20 = 8;
        descriptor.field3C = 0.0f;
        descriptor.field40 = 0.0f;
        descriptor.field44 = 0.0f;
        descriptor.field48 = 0.0f;
        descriptor.field50 = 0.0f;
        descriptor.field54 = 0.0f;
        descriptor.flags = 0x801E05;
        descriptor.field60 = 3;
        descriptor.field61 = 3;
        descriptor.field62 = 0x1A;
        descriptor.field63 = 255;

        do {
            size = ((u32)func_150ADA20() & 15) + 40;
            descriptor.field0A = size;
            descriptor.field22 = size;
            descriptor.field1B = (u32)func_150ADA20() % 119 + 100;
            fraction = func_150ADA68() * 59.0f + 80.0f;
            descriptor.field28 = fraction;
            descriptor.field2C = fraction;
            fraction = func_150ADA68();
            descriptor.field24 = (fraction * D_800A1398 + D_800A139C) * D_800A13A0;
            descriptor.flags &= ~0xC0;
            firstFlag = ((u32)func_150ADA20() & 1) << 7;
            secondFlag = ((u32)func_150ADA20() & 1) << 6;
            descriptor.flags |= firstFlag | secondFlag;
            descriptor.field14 = 0xF;
            descriptor.field15 = 0x11;
            descriptor.field16 = 5;
            descriptor.field18 = 0x44;
            descriptor.field19 = 0x3C;
            descriptor.field1A = 0x27;
            angle0 = func_150ADA68();
            angle1 = func_150ADA68();
            radius = func_150ADA68() * 20.0f;
            func_151436B4(angle0 * period, angle1 * period, radius, &descriptor.position);
            descriptor.position.x += payload->position.x;
            descriptor.position.y += payload->position.y;
            descriptor.position.z += payload->position.z;
            fraction = func_150ADA68();
            descriptor.field4C = (fraction * D_800A13A4 + D_800A13A8) * D_800A13AC;
            result = func_15130374(&descriptor, 0, 4, record[0xC], record[1]);
            if (result != NULL) {
                memcpy((u8 *)result + 0xA8, &bonus, 4);
            }
            payload->parameters.field08 -= 1.0f;
        } while (payload->parameters.field08 > 1.0f);
    }
}

void func_150E90DC(void) {
    void *result;
    EventPayload113D60 payload;

    payload.field00 = D_800A13B0;
    payload.field04 = D_800A13B4;
    payload.field08 = 0.0f;
    result = func_15149130((s16)((u32)func_150ADA20() % 26 + 5), -1, 0x36, -1,
                          1, 0, 12, 0xFF, 1);
    if (result != NULL) {
        memcpy((u8 *)result + 0x28, &payload, 12);
    }
}

void func_150E9178(u8 *record) {
    void *result;
    f32 limit;
    f32 first;
    f32 second;
    f32 parameter;
    EventPayload113D60 *payload;
    EventWeightNode113D60 *node;
    f32 *origin;
    f32 fraction;
    f32 dx;
    f32 dy;
    f32 dz;
    ExtendedEventPositionPayload113D60 child;

    origin = func_15144B34(D_800BE9E8);
    fraction = func_150ADA68();
    payload = (EventPayload113D60 *)(record + 0x28);
    payload->field08 += ((payload->field00 + fraction * payload->field04) * D_800BE9A4) * D_800DCD90;
    if (payload->field08 > 1.0f) {
        parameter = D_800A13B8;
        second = D_800A13BC;
        first = D_800A13C0;
        limit = D_800A13C4;

        do {
            fraction = func_150ADA68();
            fraction *= D_800DCD90;
            node = (EventWeightNode113D60 *)D_800DCDC4;
            while (node->weight < fraction) {
                fraction -= node->weight;
                node = node->next;
            }
            func_1514470C(node->descriptor, &child.payload.position);
            dx = child.payload.position.x - origin[0];
            dy = child.payload.position.y - origin[1];
            dz = child.payload.position.z - origin[2];
            if ((dx * dx + dy * dy) + dz * dz < limit) {
                s16 duration;

                /* Retail leaves the reserved bytes unspecified. */
                child.payload.parameters.field00 = first;
                child.payload.parameters.field04 = second;
                child.payload.parameters.field08 = 0.0f;
                child.field18 = parameter;
                child.field30 = 0;
                child.field34 = 0;
                child.field35 = 0;
                child.field38 = 0;
                duration = (u32)func_150ADA20() % 13 + 5;
                result = func_15149130(duration, -1, 0x37, -1,
                                      1, 0, 60, record[0xC], record[1]);
                if (result != NULL) {
                    memcpy((u8 *)result + 0x28, &child, 60);
                }
            }
            payload->field08 -= 1.0f;
        } while (payload->field08 > 1.0f);
    }
}

void func_150E93DC(u8 *record) {
    EventPositionPayload113D60 *payload;
    ExtendedChildEmissionDescriptor113D60 descriptor;
    u8 extra[0x1C];
    void *result;
    f32 sample;
    f32 spread;
    f32 scale;
    f32 angle0;
    f32 angle1;
    f32 radius;
    f32 period;

    sample = func_150ADA68();
    payload = (EventPositionPayload113D60 *)(record + 0x28);
    payload->parameters.field08 +=
        (payload->parameters.field00 + sample * payload->parameters.field04) * D_800BE9A4;
    if (payload->parameters.field08 > 1.0f) {
        spread = D_800A13C8;
        scale = D_800A13CC;

        /* Retail leaves descriptor holes and the extra payload unspecified. */
        descriptor.field00 = 0.0f;
        descriptor.field04 = 1.0f;
        descriptor.field1C = 1.0f;
        descriptor.field20 = 1.0f;
        descriptor.field24 = 1.0f;
        descriptor.flags = 0x49E8;
        descriptor.field34 = 0.0f;
        descriptor.field38 = 0.0f;
        descriptor.field3C = 0.0f;
        descriptor.field44 = 0.0f;
        descriptor.field58 = 0;
        descriptor.field5C = 0;
        descriptor.field60 = 255;
        descriptor.field62 = 0;
        descriptor.field63 = 0;
        descriptor.field64 = 0;
        descriptor.field65 = 0;
        descriptor.field66 = 0;
        descriptor.field67 = 0;
        descriptor.field68 = 2;
        descriptor.field6A = 2;
        descriptor.field6C = 0;
        descriptor.field70 = 0;
        descriptor.field72 = 1;
        descriptor.field74 = 255;

        do {
            func_150ADA20();
            descriptor.resource = D_800A12F0[0];
            sample = func_150ADA68();
            descriptor.field08 = ((sample * D_800A13D0 + 400.0f) * D_800A12F4[0]) * scale;
            descriptor.field0C = descriptor.field08;
            descriptor.field10 = func_150ADA68() * 360.0f;
            descriptor.field14 = func_150ADA68() * 360.0f;
            descriptor.field18 = func_150ADA68() * 360.0f;
            sample = func_150ADA68();
            descriptor.field4C = (sample * D_800A13D4 + D_800A13D8) * scale;
            func_150ADA20();
            descriptor.field54 = 100;
            sample = func_150ADA68();
            descriptor.field40 = (sample * spread + D_800A13DC) * scale;
            sample = func_150ADA68();
            descriptor.field48 = (sample * spread + D_800A13E0) * scale;
            angle0 = func_150ADA68();
            angle1 = func_150ADA68();
            radius = func_150ADA68();
            period = D_800A13E4;
            func_151436B4(angle0 * period, angle1 * period, radius * 50.0f,
                          &descriptor.position);
            descriptor.position.x += payload->position.x;
            descriptor.position.y += payload->position.y;
            descriptor.position.z += payload->position.z;
            descriptor.field61 = 8;
            result = func_15132A4C(&descriptor, 3, 0xFF, 0x1C, record[0xC], record[1]);
            if (result != NULL) {
                memcpy((u8 *)result + 0x170, extra, 0x1C);
            }
            payload->parameters.field08 -= 1.0f;
        } while (payload->parameters.field08 > 1.0f);
    }
}

s32 func_150E971C() {
    return 0;
}
