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
void func_151B2690(u8 *volatile);

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


typedef struct {
    OwnerLinkEndpoint2348 endpoint;
    OwnerLinkVector2348 end;
    f32 width;
    u8 *actor;
} OwnerEffectPacket2690;
extern OwnerLinkVector2348 D_800AA368, D_800AA374;
extern f32 D_800AA388, D_800AA38C;
void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);

typedef struct { f32 x, y, z; } OwnerQuadPosition2974;
extern u8 *D_800DBFF0;
extern u8 D_80090DE8[];
extern u32 D_800D2C9C, D_800A4AC8[];
void func_151D5D60(void *, s16, s32, Vtx **, u8 *);
void func_15143134(void *, void *, u8 *);
Gfx *func_15142B7C(Gfx *, u32, u32);
Gfx *func_15142E24(Gfx *, void *, s32, s32, s32, s32, s32, u8, u8 *, u8 *, s32);
Gfx *func_15142C10(Gfx *, s32, s32, s32, s32, u8 *);
Gfx *func_15142CF0(Gfx *, s32, s32, s32, s32, s32, s32, u8 *);
Gfx *func_1513F4E4(Gfx *, u8, u8 *);
Gfx *func_15142FBC(Gfx *, u32, u32, u8 *);

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

void func_151B2690(u8 *volatile actor) {
    u8 *pair = actor;
    u8 *endpoint = *(u8 **)(pair + 0x28);
    struct { OwnerEffectPacket2690 effect; OwnerLinkPacket2348 packet; OwnerLinkRequest2348 request; } work;
    u8 *created;

    work.packet.actor = pair;
    work.packet.route = 1;
    work.packet.first.owner = endpoint;
    work.packet.first.code = endpoint[0x3B];
    work.packet.first.kind = 5;
    work.packet.first.offset = D_800AA320;
    work.packet.second.owner = endpoint;
    work.packet.second.code = endpoint[0x3B];
    work.packet.second.kind = 2;
    work.packet.second.offset = D_800AA368;
    work.request.tail = 0;
    work.request.flags = 0;
    work.request.duration = 100;
    work.request.start.x = *(f32 *)(endpoint + 0x14);
    work.request.start.y = *(f32 *)(endpoint + 0x18);
    work.request.start.z = *(f32 *)(endpoint + 0x1C);
    work.request.end.x = *(f32 *)(endpoint + 0x14);
    work.request.end.y = *(f32 *)(endpoint + 0x18);
    work.request.end.z = *(f32 *)(endpoint + 0x1C);
    work.request.active = 1;
    work.request.enabled = 1;
    work.request.extra = 1;
    work.request.kind = 3;
    work.request.width = 5.0f;
    work.request.distance = 180.0f;
    work.request.limitA = D_800AA388;
    work.request.limitB = D_800AA38C;
    created = func_151B30B0(&work.request, 0.0015f, 48, 255, 0);
    pair = *(u8 **)&actor + 0x28;
    *(u8 **)(pair + 0x14) = created;
    if (created != NULL) {
        memcpy((*(u8 **)(pair + 0x14)) + 0x150, &work.packet, 48);
    }

    work.packet.route = 0;
    work.packet.first.offset = D_800AA32C;
    work.packet.second.offset = D_800AA374;
    work.request.extra = 1;
    created = func_151B30B0(&work.request, 0.0015f, 48, 255, 0);
    *(u8 **)(pair + 0x10) = created;
    if (created != NULL) {
        memcpy((*(u8 **)(pair + 0x10)) + 0x150, &work.packet, 48);
    }

    work.effect.endpoint.owner = endpoint;
    work.effect.endpoint.code = endpoint[0x3B];
    work.effect.endpoint.kind = 2;
    work.effect.endpoint.offset = D_800AA368;
    work.effect.end = D_800AA374;
    work.effect.width = 5.0f;
    work.effect.actor = *(u8 **)&actor;
    created = func_15149130(300, -1, -1, 0, 0, 19, 40, 255, 1);
    *(u8 **)(pair + 0x1C) = created;
    if (created != NULL) {
        memcpy((*(u8 **)(pair + 0x1C)) + 0x28, &work.effect, 40);
    }
}

void func_151B2950(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x178);

    if (temp_v0 != NULL) {
        *(s32 *)(temp_v0 + (*(u8 *)(arg0 + 0x17C) * 4) + 0x38) = 0;
    }
}

Gfx *func_151B2974(Gfx *output, u8 *actor, s16 view) {
    u8 *pair;
    u8 invalid;
    u8 sync;
    Vtx *cursor;
    OwnerQuadPosition2974 *origin;
    f32 dx, dy, dz, rx, ry, rz;
    f32 length;
    OwnerQuadPosition2974 first, second;
    f32 nx, ny, nz;
    u8 *matrix;
    f32 scale;

    invalid = 0;
    pair = actor + 0x28;
    if (**(s32 **)pair == 0 || pair[4] != (*(u8 **)pair)[0x3B]) {
        invalid = 1;
    }
    pair = actor + 0x28;
    if (!invalid && *(u8 **)(*(u8 **)pair + 0x1D4) != NULL) {
        func_151D5D60(actor + 0x14, view, 64, &cursor, NULL);
        if (cursor == NULL) {
            return output;
        }
        matrix = (pair[5] << 6) + *(u8 **)(*(u8 **)pair + 0x1D4);
        func_15143134(pair + 8, &first, matrix);
        func_15143134(pair + 0x14, &second, matrix);
        sync = 1;
        origin = (OwnerQuadPosition2974 *)(D_800DBFF0 + view * 0x9A0 + 0x2F8);
        output = func_15142B7C(output, 0x200005, 0x60600);
        output = func_15142E24(output, D_80090DE8, 0, 0, 0, 0, 54, 0, NULL, &sync, 3);
        output = func_15142C10(output, 255, 255, 255, 255, &sync);
        output = func_15142CF0(output, 0, 0, 255, 255, 255, 255, &sync);
        output = func_1513F4E4(output, 0x2B, &sync);
        output = func_15142FBC(output, D_800D2C9C | 0x80000 | 0x2CA0,
            D_800A4AC8[10] | D_800A4AC8[11], &sync);
        dx = second.x - first.x;
        dy = second.y - first.y;
        dz = second.z - first.z;
        rx = dx * 0.5f + first.x - origin->x;
        ry = dy * 0.5f + first.y - origin->y;
        rz = dz * 0.5f + first.z - origin->z;
        nx = dy * rz - ry * dz;
        ny = dz * rx - rz * dx;
        nz = dx * ry - rx * dy;
        length = nx * nx + ny * ny + nz * nz;
        if (length == 0.0f) {
            nx = 0.0f; ny = 0.0f; nz = 0.0f;
        } else {
            length = sqrtf(length);
            scale = *(f32 *)(pair + 0x20) / length;
            nx = nx * scale;
            ny = ny * scale;
            nz = nz * scale;
        }
        cursor->v.ob[0] = (s32)(second.x + nx);
        cursor->v.ob[1] = (s32)(second.y + ny);
        cursor->v.ob[2] = (s32)(second.z + nz);
        cursor->v.tc[0] = 0;
        cursor->v.tc[1] = 0;
        cursor++;
        cursor->v.ob[0] = (s32)(second.x - nx);
        cursor->v.ob[1] = (s32)(second.y - ny);
        cursor->v.ob[2] = (s32)(second.z - nz);
        cursor->v.tc[0] = 0x3C0;
        cursor->v.tc[1] = 0;
        cursor++;
        cursor->v.ob[0] = (s32)(first.x - nx);
        cursor->v.ob[1] = (s32)(first.y - ny);
        cursor->v.ob[2] = (s32)(first.z - nz);
        cursor->v.tc[0] = 0x3C0;
        cursor->v.tc[1] = 0x3C0;
        cursor++;
        cursor->v.ob[0] = (s32)(first.x + nx);
        cursor->v.ob[1] = (s32)(first.y + ny);
        cursor->v.ob[2] = (s32)(first.z + nz);
        cursor->v.tc[0] = 0;
        cursor->v.tc[1] = 0x3C0;
        cursor++;
        gSPVertex(output++, cursor - 4, 4, 0);
        gSP1Triangle(output++, 0, 1, 2, 0);
        gSP1Triangle(output++, 0, 2, 3, 0);
    }
    if (invalid) {
        *(s16 *)(actor + 0xE) = -1;
    }
    return output;
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
