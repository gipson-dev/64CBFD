#include <ultra64.h>
extern u8 D_800CC2D0[];
void func_151B47D8(u8 *, u8 *, s32, u8);
void func_1516972C(u8 *);

typedef struct {
    u8 *owner;
    u8 ownerCode, reserved05[3];
    u8 *resource;
    u8 active, state, reserved0E[2];
    u8 cleared[12];
    s32 value;
} OwnerDescriptor151B2060;
u8 *func_15083E90(s32);
u8 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

s32 func_151B22F4(u8 *);
void func_151B222C(u8 *);
void func_151B2348(u8 *);
void func_151B2690(u8 *);

typedef struct { f32 x, y, z; } OwnerLinkVector2348;
typedef struct {
    u8 *owner;
    u8 code, kind, reserved06[2];
    OwnerLinkVector2348 offset;
} OwnerLinkEndpoint2348;
typedef struct {
    OwnerLinkEndpoint2348 first, second;
    u8 *actor;
    u8 route, reserved2D[3];
} OwnerLinkPacket2348;
typedef struct {
    u8 flags, reserved01;
    s16 duration;
    OwnerLinkVector2348 start, end;
    u8 active, enabled, extra, reserved1F;
    f32 width;
    u8 kind, reserved25[3];
    f32 distance, limitA, limitB;
    u8 tail, reserved35[3];
} OwnerLinkRequest2348;
extern OwnerLinkVector2348 D_800AA350, D_800AA35C, D_800AA320;
extern OwnerLinkVector2348 D_800AA338, D_800AA32C, D_800AA344;
extern f32 D_800AA380, D_800AA384;
u8 *func_151B30B0(void *, f32, s32, u8, s32);


/* Non-matching placeholders for the text-only asm slice asm/1DF510.s. */

void func_151B222C(u8 *);

void func_151B2060(u8 *owner) {
    u8 *created;
    OwnerDescriptor151B2060 descriptor;

    if (owner != NULL) {
        descriptor.owner = owner;
        descriptor.ownerCode = owner[0x3B];
        descriptor.resource = func_15083E90(1);
        descriptor.active = 1;
        descriptor.state = 0;
        bzero(descriptor.cleared, 12);
        descriptor.value = 0;
        created = func_151491F4(300, -1, 0x16, 0, 0x12, 32, 255, 1);
        if (created != NULL) {
            memcpy(created + 0x28, &descriptor, 32);
        }
    }
}

void func_151B2100(u8 *actor) {
    u8 *first = *(u8 **)(actor + 0x28);
    u8 *second = *(u8 **)(actor + 0x30);
    u8 *pair = actor + 0x28;
    u8 previous;

    if (*(s32 *)first == 0 || first[4] == 255 || pair[4] != first[0x3B] ||
        *(s32 *)second == 0 || second[4] == 255 || pair[12] != second[0x3B]) {
        *(s16 *)(actor + 0xE) = -1;
    } else {
        previous = pair[13];
        pair[13] = func_151B22F4(actor);
        if (previous != pair[13]) {
            func_151B222C(actor);
            if (pair[13] == 1) {
                func_151B2348(actor);
            }
            if (pair[13] == 2 || pair[13] == 0) {
                func_151B2690(actor);
            }
        }
    }
}

void func_151B220C(u8 *arg0) {
    func_151B222C(arg0);
}

void func_151B222C(u8 *arg0) {
    u8 *base = arg0 + 0x28;
    s32 i;
    u8 *entry;

    i = 0;
    do {
        entry = *(u8 **)(base + 0x10 + i * 4);
        if (entry != NULL) {
            func_1516972C(entry);
        }
        i = (u8)(i + 1);
    } while (i < 3);

    entry = *(u8 **)(base + 0x1C);
    if (entry != NULL) {
        func_1516972C(entry);
    }
}

s32 func_151B229C(s32 arg0) {
    func_151B220C(arg0);
    func_1514933C(arg0);
}

s32 func_151B22C8(s32 arg0) {
    func_151B220C(arg0);
    func_15149368(arg0);
}

s32 func_151B22F4(u8 *arg0) {
    s32 temp_v0 = *(s32 *)(arg0 + 0x28);
    u8 *temp_v1 = *(u8 **)(arg0 + 0x30);

    if ((((temp_v0 - (s32)D_800CC2D0) / 0x32C) + 1 == temp_v1[0x65]) &&
        (*(s32 *)(temp_v1 + 0x5C) == 1)) {
        return 1;
    }
    return 2;
}

void func_151B2348(u8 *actor) {
    u8 *second = *(u8 **)(actor + 0x30);
    u8 *first = *(u8 **)(actor + 0x28);
    u8 *pair;
    struct { OwnerLinkPacket2348 packet; OwnerLinkRequest2348 request; } work;
    u8 *created;

    work.packet.route = 2;
    work.packet.actor = actor;
    work.packet.first.owner = second;
    work.packet.first.code = second[0x3B];
    work.packet.first.kind = 5;
    work.packet.first.offset = D_800AA350;
    work.packet.second.owner = second;
    work.packet.second.code = second[0x3B];
    work.packet.second.kind = 10;
    work.packet.second.offset = D_800AA35C;
    work.request.tail = 0;
    work.request.flags = 0;
    work.request.duration = 1000;
    work.request.start.x = *(f32 *)(second + 0x14);
    work.request.start.y = *(f32 *)(second + 0x18);
    work.request.start.z = *(f32 *)(second + 0x1C);
    work.request.end.x = *(f32 *)(second + 0x14);
    work.request.end.y = *(f32 *)(second + 0x18);
    work.request.end.z = *(f32 *)(second + 0x1C);
    work.request.active = 1;
    work.request.enabled = 1;
    work.request.extra = 0;
    work.request.kind = 3;
    work.request.width = 5.0f;
    work.request.distance = 80.0f;
    work.request.limitA = D_800AA380;
    work.request.limitB = D_800AA384;
    created = func_151B30B0(&work.request, 0.0015f, 48, 255, 0);
    pair = *(u8 **)&actor + 0x28;
    *(u8 **)(pair + 0x18) = created;
    if (created != NULL) {
        memcpy((*(u8 **)(pair + 0x18)) + 0x150, &work.packet, 48);
    }

    work.packet.route = 1;
    work.packet.first.owner = first;
    work.packet.first.code = first[0x3B];
    work.packet.first.kind = 5;
    work.packet.first.offset = D_800AA320;
    work.packet.second.owner = second;
    work.packet.second.code = second[0x3B];
    work.packet.second.kind = 5;
    work.packet.second.offset = D_800AA338;
    work.request.start.x = *(f32 *)(first + 0x14);
    work.request.start.y = *(f32 *)(first + 0x18);
    work.request.start.z = *(f32 *)(first + 0x1C);
    work.request.end.x = *(f32 *)(second + 0x14);
    work.request.end.y = *(f32 *)(second + 0x18);
    work.request.end.z = *(f32 *)(second + 0x1C);
    work.request.extra = 0;
    work.request.distance = 170.0f;
    created = func_151B30B0(&work.request, 0.0015f, 48, 255, 0);
    *(u8 **)(pair + 0x14) = created;
    if (created != NULL) {
        memcpy((*(u8 **)(pair + 0x14)) + 0x150, &work.packet, 48);
    }

    work.packet.route = 0;
    work.packet.first.owner = first;
    work.packet.first.code = first[0x3B];
    work.packet.first.kind = 5;
    work.packet.first.offset = D_800AA32C;
    work.packet.second.owner = second;
    work.packet.second.code = second[0x3B];
    work.packet.second.kind = 10;
    work.packet.second.offset = D_800AA344;
    work.request.start.x = *(f32 *)(first + 0x14);
    work.request.start.y = *(f32 *)(first + 0x18);
    work.request.start.z = *(f32 *)(first + 0x1C);
    work.request.end.x = *(f32 *)(second + 0x14);
    work.request.end.y = *(f32 *)(second + 0x18);
    work.request.end.z = *(f32 *)(second + 0x1C);
    work.request.extra = 0;
    created = func_151B30B0(&work.request, 0.0015f, 48, 255, 0);
    *(u8 **)(pair + 0x10) = created;
    if (created != NULL) {
        memcpy((*(u8 **)(pair + 0x10)) + 0x150, &work.packet, 48);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1DF510/func_151B2690.s")

void func_151B2950(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x178);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + (*(u8 *)(arg0 + 0x17C) * 4) + 0x38) = 0;
    }
}

s32 func_151B2974() {
    return 0;
}

void func_151B2EC4(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x28), (s32) (arg0 + 0x2C), (s32) arg0);
}

void func_151B2F04(u8 *owner, u8 *packet, u8 kind) {
    u8 *pair = owner + 0x28;

    if (kind == 0x2D) {
        if (*(s32 *)packet == *(s32 *)pair) {
            *(s32 *)pair = *(s32 *)(packet + 4);
            pair[4] = packet[9];
        } else if (*(s32 *)(packet + 4) == *(s32 *)pair) {
            *(s32 *)pair = *(s32 *)packet;
            pair[4] = packet[8];
        }
        if (*(s32 *)packet == *(s32 *)(pair + 8)) {
            *(s32 *)(pair + 8) = *(s32 *)(packet + 4);
            pair[12] = packet[9];
        } else if (*(s32 *)(packet + 4) == *(s32 *)(pair + 8)) {
            *(s32 *)(pair + 8) = *(s32 *)packet;
            pair[12] = packet[8];
        }
    }
}

void func_151B2FA0(u8 *arg0, s32 arg1, u8 arg2) {
    func_151B47D8(arg0, arg0 + 0x150, arg1, arg2);
}

void func_151B2FD0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x4C);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + 0x44) = 0;
    }
}

s32 func_151B2FE8(s32 arg0) {
    func_151B2FD0(arg0);
    func_1514933C(arg0);
}

s32 func_151B3014(s32 arg0) {
    func_151B2FD0(arg0);
    func_15149368(arg0);
}

void func_151B3040(u8 *arg0, s32 arg1, volatile u8 arg2) {
    u8 *base = arg0 + 0x150;

    func_15169850(arg1, arg2, (s32) base, (s32) (base + 4), (s32) arg0);
    func_15169850(arg1, arg2, (s32) (base + 0x14), (s32) (base + 0x18), (s32) arg0);
}
