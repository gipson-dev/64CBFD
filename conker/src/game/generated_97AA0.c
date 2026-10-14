#include <ultra64.h>
#include "structs.h"

typedef struct {
    u8 *object;
    u8 selector;
} ObjectSelector97AA0;

typedef struct {
    u32 first, second;
} PayloadPair97AA0;
typedef struct {
    ObjectSelector97AA0 target;
    PayloadPair97AA0 payload;
} ActorPayload97AA0;
typedef char ActorPayloadSize97AA0[(sizeof(ActorPayload97AA0) == 16) ? 1 : -1];

void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, unsigned int);

/* Non-matching placeholders for the text-only asm slice asm/97AA0.s. */

typedef struct {
    s16 count;
    u8 pad2[2];
    f32 position[3];
    s16 duration;
    u8 pad12[2];
    f32 radius;
    s16 angle0, range0, angle1, range1;
    f32 speed, speedRange;
    f32 unk28, unk2C;
    f32 direction[3];
    f32 scale, scaleRange;
    f32 unk44, unk48, unk4C, unk50;
    u8 unk54, unk55;
    s16 unk56, unk58;
    u8 pad5A[2];
} ActorBurstPacket97AA0;
typedef char ActorBurstPacketSize97AA0[(sizeof(ActorBurstPacket97AA0) == 0x5C) ? 1 : -1];

void func_151A6F00(ActorBurstPacket97AA0 *, u8, u8, s32);
extern f32 D_80099A10;
extern f32 D_80099A14;
extern f32 D_80099A18;
extern f32 D_80099A1C;
extern f32 D_80099A20;
extern f32 D_80099A24;

extern s32 D_800CC260;
extern u8 D_800CC2D0[];
s32 func_15137610(u8 *, u8 *, u8 *, s32, u8, s32);

void func_151D3480(f32 *, f32 *, void *, u8, u8, s32);

struct225 *func_151602C0(Header *, Header2 *, s32, s32, s32, s32, u8, u8, s32, u8, s32);
extern f32 D_80099A28;

extern u8 D_800D1560[];
extern u8 D_800D1570[];

void func_1506A5F0(u8 *actor, s32 arg1) {
    ActorBurstPacket97AA0 packet;

    packet.count = 3;
    packet.position[0] = *(f32 *)(actor + 0x14);
    packet.position[1] = *(f32 *)(actor + 0x18);
    packet.position[2] = *(f32 *)(actor + 0x1C);
    packet.duration = 90;
    packet.radius = D_80099A10;
    packet.angle0 = 0;
    packet.range0 = 255;
    packet.angle1 = -64;
    packet.range1 = 40;
    packet.speed = D_80099A14;
    packet.speedRange = D_80099A18;
    packet.direction[0] = 0.0f;
    packet.direction[1] = 0.0f;
    packet.direction[2] = 0.0f;
    packet.scale = D_80099A1C;
    packet.scaleRange = D_80099A20;
    packet.unk44 = D_80099A24;
    packet.unk48 = 0;
    packet.unk4C = -4.0f;
    packet.unk50 = 8.0f;
    packet.unk54 = 0;
    packet.unk55 = 0;
    packet.unk56 = 50;
    packet.unk58 = 25;
    func_151A6F00(&packet, 1, 0xFF, 1);
}

s32 func_1506A6FC(s32 arg0, s32 arg1) {
    func_150E0348(arg0, 0xFF, 1);
}

void func_1506A724(s32 arg0, s32 arg1) {
    func_151BB61C(arg0, D_800D1560, D_800D1570, 0xFF, 1);
}

void func_1506A760(s32 arg0, s32 arg1) {
    func_151BBA9C(arg0, D_800D1560, D_800D1570, 0xFF, 1);
}

void func_1506A79C(u8 *actor, s32 arg1) {
    f32 position[3];
    f32 difference[3];

    position[0] = *(f32 *)(actor + 0x14);
    position[1] = *(f32 *)(actor + 0x18);
    position[2] = *(f32 *)(actor + 0x1C);
    difference[0] = *(f32 *)(D_800D1570 + 0) - *(f32 *)(D_800D1560 + 0);
    difference[1] = *(f32 *)(D_800D1570 + 4) - *(f32 *)(D_800D1560 + 4);
    difference[2] = *(f32 *)(D_800D1570 + 8) - *(f32 *)(D_800D1560 + 8);
    func_151D3480(position, difference, NULL, 0, 0xFF, 1);
}

s32 func_1506A83C(s32 arg0, s32 arg1) {
    func_151BC104(arg0, 0xFF, 1);
}

void func_1506A864(u8 *actor, s32 arg1) {
    struct225 *created;
    Header header;
    f32 payload[4];
    Header2 position;

    position.unk0 = (s32)*(f32 *)(actor + 0x14);
    position.unk4 = (s32)(*(f32 *)(actor + 0x18) + 50.0f);
    position.unk8 = (s32)*(f32 *)(actor + 0x1C);
    payload[0] = 0.0f;
    payload[2] = 0.0f;
    header.unk0 = 2;
    header.unk1 = 15;
    header.unk2 = 300;
    header.unk4 = 5;
    payload[1] = 80.0f;
    payload[3] = D_80099A28;
    created = func_151602C0(&header, &position, 0, 0xFF, 0xFF, 90, 0xFF, 0, sizeof(payload), 0xFF, 1);
    if (created != NULL) {
        memcpy((u8 *)created + 0x18, payload, sizeof(payload));
    }
}

void func_1506A968(u8 *actor, s32 arg1) {
    f32 position[3];
    f32 difference[3];

    position[0] = *(f32 *)(actor + 0x14);
    position[1] = *(f32 *)(actor + 0x18);
    position[2] = *(f32 *)(actor + 0x1C);
    difference[0] = *(f32 *)(D_800D1570 + 0) - *(f32 *)(D_800D1560 + 0);
    difference[1] = *(f32 *)(D_800D1570 + 4) - *(f32 *)(D_800D1560 + 4);
    difference[2] = *(f32 *)(D_800D1570 + 8) - *(f32 *)(D_800D1560 + 8);
    func_151D3480(position, difference, NULL, 1, 0xFF, 1);
}

void func_1506AA08(s32 arg0, s32 arg1) {
    func_151B7144(arg0, 0xFF, 1);
    func_151B6320(arg0, 0xFF, 1);
}

void func_1506AA48(u8 *actor, const PayloadPair97AA0 *data) {
    u8 *created;
    ActorPayload97AA0 packet;

    packet.target.object = actor;
    packet.target.selector = actor[0x3B];
    packet.payload = *data;
    created = func_15149130(10, 7, 0x23, -1, 1, 0x21, sizeof(packet), 0xFF, 1);
    if (created != NULL) {
        memcpy(created + 0x28, &packet, sizeof(packet));
    }
}

void func_1506AAE0(s32 arg0, s32 arg1) {
    s32 mask = D_800CC260;
    u8 *actor = D_800CC2D0;

    while (mask != 0) {
        if (mask & 1) {
            func_15137610(actor, D_800D1560, D_800D1570, 0, 0xFF, 1);
        }
        mask >>= 1;
        actor += 0x32C;
    }
}

void func_1506AB7C(s32 arg0, u8 *arg1) {
    func_15103E40(arg0, *(s32 *)arg1, arg1 + 4, 1,
                  *(s32 *)(arg1 + 0x10), 0xFF, 1);
}

void func_1506ABC4(s32 arg0, u8 *arg1) {
    func_15103E40(arg0, *(s32 *)arg1, arg1 + 4, 2,
                  *(s32 *)(arg1 + 0x10), 0xFF, 1);
}

void func_1506AC0C(u8 *arg0, s32 arg1) {
    ObjectSelector97AA0 record;

    record.object = arg0;
    record.selector = arg0[0x3B];
    func_151B7328(&record, 0, 8, 0xFF, 1);
}

void func_1506AC58(s32 arg0, u8 arg1) {
    func_151CEAAC(arg0, 0, 1, 0xFF, 1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_97AA0/func_1506AC8C.s")
