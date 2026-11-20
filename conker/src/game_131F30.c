#include <ultra64.h>
#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
typedef struct MapTrailRecord131F30 MapTrailRecord131F30;
void func_151058B4(MapTrailRecord131F30 *);
void *func_15105C24(s32 key);
/* End generated placeholder declarations. */

typedef struct { u8 bytes[9]; } MapSequence131F30;
typedef struct {
    s32 length;
    u8 *sequence;
    struct127 *actor;
} MapPacket131F30;
extern u32 *D_800DBF94;
extern MapSequence131F30 D_800A2380, D_800A238C, D_800A2398;

/* Dispatch the map record's sequence or actor pointer to its first active actor. */
void func_15104A80(struct131 *record) {
    void *command;
    s32 index;
    s32 i;
    u32 mask;
    MapPacket131F30 packet;
    MapSequence131F30 first, second, third;
    struct127 *actorOnly;
    struct127 *actor;

    actor = 0;
    index = (s32)((u32)record - (u32)D_800DBEF4) / 0xA0;
    mask = D_800DBF94[index];
    if (mask != 0) {
        for (i = 0; i < 25 && actor == 0; i++) {
            if (D_800CC2D0[i].interaction_state != 0 && (mask & (1U << i))) {
                actor = &D_800CC2D0[i];
            }
        }
    }
    if (((u8 *)record)[0x72] == 0xF9 || ((u8 *)record)[0x72] == 0xF8 ||
        ((u8 *)record)[0x72] == 0xF7) {
        packet.actor = actor;
        if (((u8 *)record)[0x72] == 0xF9) {
            first = D_800A2380;
            packet.length = 9;
            packet.sequence = first.bytes;
            command = (void *)&packet;
        } else if (((u8 *)record)[0x72] == 0xF8) {
            second = D_800A238C;
            packet.length = 9;
            packet.sequence = second.bytes;
            command = (void *)&packet;
        } else if (((u8 *)record)[0x72] == 0xF7) {
            third = D_800A2398;
            packet.length = 9;
            packet.sequence = third.bytes;
            command = (void *)&packet;
        }
        command = (void *)&packet;
        func_151494E0((s32)command, 0x35);
    } else if (((u8 *)record)[0x72] == 0xF6) {
        actorOnly = actor;
        func_151494E0((s32)&actorOnly, 0x38);
    }
}




typedef struct { f32 x, y, z; } MapParticlePoint131F30;
typedef struct { f32 x, z; } MapParticlePair131F30;
typedef struct {
    f32 height;
    s16 vertices[9], pad16;
    u32 metadata;
    u8 flags, state;
    u16 pad1E;
    s32 value;
} MapParticleSurface131F30;
typedef struct {
    s32 eventID;
    f32 accumulator;
    s16 timer;
    u16 reserved0A;
    MapParticlePoint131F30 position;
    f32 radius, height;
    MapParticleSurface131F30 surface;
    s16 *gate;
} MapParticleEmitter131F30;
typedef struct {
    struct260 header;
    u8 reserved24[4];
    MapParticleEmitter131F30 emitter;
} MapParticleRecord131F30;
typedef struct {
    s16 duration;
    u8 enabled, reserved03;
    MapParticlePoint131F30 origin, start, end, sample;
    s8 flag;
    u8 reserved35[3];
    s32 pieces;
    f32 width, spread;
    s16 minimum, maximum;
    u8 red, green, blue, alpha, state;
    u8 reserved4D[3];
} MapParticlePacket131F30;
extern f32 D_800A23AC, D_800A23B0;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
void func_1000FD38(s32, s32, s32);
u8 func_151464B8(s16 *);
void func_15143874(s16, f32, f32 *, f32 *);
s32 func_15046C80(MapParticlePoint131F30 *, u16, f32, MapParticleSurface131F30 *);
void *func_15105CE0(MapParticlePacket131F30 *, s32, u8, s32);

/* Accumulate timed map particles and emit their sampled ground-bound paths. */
void func_15104C44(struct260 *record) {
    f32 randomValue;
    MapParticlePacket131F30 packet;
    MapParticlePoint131F30 sample;
    MapParticlePair131F30 startOffset, endOffset;
    MapParticleEmitter131F30 *emitter;
    s32 angle;

    emitter = &((MapParticleRecord131F30 *)record)->emitter;
    if (emitter->timer < 0) {
        return;
    }
    emitter->timer = (s16)((u32)(s32)emitter->timer - (u32)D_800BE9E4);
    if (emitter->timer < 0) {
        func_1000FD38((s32)func_1000EF40, emitter->eventID, 0);
    }
    if (func_151464B8(emitter->gate) != 0) {
        return;
    }
    randomValue = func_150ADA68();
    emitter->accumulator += (D_800A23AC + randomValue * D_800A23B0) * D_800BE9A4;
    if (emitter->accumulator > 1.0f) {
        sample.y = emitter->position.y + emitter->height;
        packet.enabled = 1;
        packet.flag = -1;
        packet.minimum = 3;
        packet.maximum = 4;
        packet.state = 0;
        packet.spread = 45.0f;
        packet.width = 25.0f;
        packet.origin.x = emitter->position.x;
        packet.origin.y = emitter->position.y + emitter->height;
        packet.origin.z = emitter->position.z;
        packet.red = 0x61;
        packet.green = 0xF2;
        packet.blue = 0xFF;
        packet.start.y = emitter->position.y + emitter->height - 180.0f;
        do {
            angle = func_150ADA20();
            randomValue = func_150ADA68();
            func_15143874((s16)(angle & 0xFF), (randomValue * 0.5f + 0.5f) * emitter->radius,
                &sample.x, &sample.z);
            sample.x += emitter->position.x;
            sample.z += emitter->position.z;
            if (func_15046C80(&sample, 0, emitter->position.y, &emitter->surface) != 0) {
                angle = func_150ADA20();
                randomValue = func_150ADA68();
                func_15143874((s16)(angle & 0xFF), randomValue * 220.0f, &startOffset.x, &startOffset.z);
                angle = func_150ADA20();
                randomValue = func_150ADA68();
                func_15143874((s16)(angle & 0xFF), randomValue * 220.0f, &endOffset.x, &endOffset.z);
                packet.start.x = emitter->position.x + startOffset.x;
                packet.start.z = emitter->position.z + startOffset.z;
                packet.sample.x = sample.x;
                packet.sample.y = emitter->surface.height;
                packet.sample.z = sample.z;
                packet.end.x = packet.sample.x + endOffset.x;
                packet.end.z = packet.sample.z + endOffset.z;
                packet.end.y = packet.sample.y + 180.0f;
                packet.duration = (u32)func_150ADA20() % 13 + 8;
                packet.alpha = (u32)func_150ADA20() % 156 + 100;
                packet.pieces = (u32)func_150ADA20() % 3 + 5;
                func_15105CE0(&packet, 0, ((u8 *)record)[0xC], ((u8 *)record)[1]);
            }
            emitter->accumulator -= 1.0f;
        } while (emitter->accumulator > 1.0f);
    }
}


typedef struct {
    s16 x, y, z;
    u8 reserved06[0xE];
    u8 state;
    u8 reserved15[3];
} MapParticleSoundSource131F30;

typedef struct {
    MapParticleSoundSource131F30 *source;
    f32 accumulator;
    s16 timer;
    u16 reserved0A;
} MapParticleSoundState131F30;

typedef struct {
    struct260 header;
    u8 reserved24[4];
    MapParticleSoundState131F30 state;
} MapParticleSoundRecord131F30;

/* Restart the map particle source's positional sound on an activation command. */
void func_15104FF8(struct260 *record, s32 argument, u8 command) {
    MapParticleSoundState131F30 *emitter;
    MapParticleSoundSource131F30 *source;

    emitter = &((MapParticleSoundRecord131F30 *)record)->state;
    if (command == 0x38 && emitter->source->state == 1) {
        emitter->timer = 300;
        func_1000FD38((s32)func_1000EF40, (s32)emitter->source, 0);
        source = emitter->source;
        func_1000FA64(0x236, source->x, source->y, source->z,
            0x4000, 1500, 1000, (s32)func_1000EF40, source, 0, 8, 0);
    }
}

typedef struct {
    MapParticleSoundSource131F30 *source;
    s16 timer;
    u16 reserved06;
    f32 accumulator;
    MapParticlePoint131F30 positions[4];
    MapParticlePoint131F30 directions[4];
    s16 *gate;
} MapEdgeEmitter131F30;

typedef struct {
    struct260 header;
    u8 reserved24[4];
    MapEdgeEmitter131F30 emitter;
} MapEdgeRecord131F30;

typedef struct {
    f32 parameters[5];
    s16 duration, zero16, step, enabled, count;
    u16 reserved1E;
    s32 kind, mode;
    u8 red, green, blue, alpha, state;
    u8 reserved2D[3];
} MapEdgePacket131F30;

extern f32 D_800A23B4, D_800A23B8, D_800A23BC;
void *func_15106F98(MapParticlePoint131F30 *, MapParticlePoint131F30 *, s32,
    MapEdgePacket131F30 *, f32, u8, u8, s32);

/* Emit interpolated segments between two selected edges of a timed map effect. */
void func_151050B0(struct260 *record) {
    f32 randomValue;
    MapEdgePacket131F30 packet;
    MapParticlePoint131F30 firstPoint, secondPoint;
    MapEdgeEmitter131F30 *emitter;
    f32 width;
    f32 secondScale;
    u32 firstIndex;
    u8 secondIndex;

    emitter = &((MapEdgeRecord131F30 *)record)->emitter;
    if (emitter->timer < 0) {
        emitter->source->state = 1;
    } else {
        emitter->source->state = 0;
        emitter->timer = (s16)((u32)(s32)emitter->timer - (u32)D_800BE9E4);
        if (emitter->timer < 0) {
            func_151494E0(0, 0x39);
            func_151494E0(0, 0x4B);
        }
        if (func_151464B8(emitter->gate) == 0) {
            randomValue = func_150ADA68();
            emitter->accumulator += (D_800A23B4 + randomValue * D_800A23B8) * D_800BE9A4;
            if (emitter->accumulator > 1.0f) {
                width = D_800A23BC;
                secondScale = 2.0f;
                packet.duration = 100;
                packet.zero16 = 0;
                packet.step = 10;
                packet.enabled = 1;
                packet.count = 10;
                packet.kind = 4;
                packet.mode = 2;
                packet.red = 0x7E;
                packet.green = 0xF9;
                packet.blue = 0xFF;
                packet.alpha = 0x37;
                packet.state = 200;
                packet.parameters[0] = 10.0f;
                packet.parameters[1] = 15.0f;
                packet.parameters[2] = 20.0f;
                packet.parameters[3] = 44.0f;
                packet.parameters[4] = 37.0f;
                do {
                    firstIndex = (u8)(func_150ADA68() * 3.0f);
                    secondIndex = (u8)(func_150ADA68() * secondScale + 1.0f + firstIndex);
                    if (secondIndex >= 4) {
                        secondIndex -= 4;
                    }
                    randomValue = func_150ADA68();
                    firstPoint.x = emitter->positions[firstIndex].x + emitter->directions[firstIndex].x * randomValue;
                    firstPoint.y = emitter->positions[firstIndex].y + emitter->directions[firstIndex].y * randomValue;
                    firstPoint.z = emitter->positions[firstIndex].z + emitter->directions[firstIndex].z * randomValue;
                    randomValue = func_150ADA68();
                    secondPoint.x = emitter->positions[secondIndex].x + emitter->directions[secondIndex].x * randomValue;
                    secondPoint.y = emitter->positions[secondIndex].y + emitter->directions[secondIndex].y * randomValue;
                    secondPoint.z = emitter->positions[secondIndex].z + emitter->directions[secondIndex].z * randomValue;
                    func_15106F98(&firstPoint, &secondPoint, 3, &packet, width, 2,
                        ((u8 *)record)[0xC], ((u8 *)record)[1]);
                    emitter->accumulator -= 1.0f;
                } while (emitter->accumulator > 1.0f);
            }
        }
    }
}

void func_1510550C(struct102 *arg0, s32 arg1, u8 arg2) {
    if (arg2 == 0x4B) {
        func_1516972C(arg0);
    }
}

void func_15105548(struct207 *arg0, s32 *arg1, u8 arg2) {
    struct206 *temp_v0 = &arg0->unk28;
    if ((arg2 == 0x38) && (temp_v0->unk0->unk14 == 1)) {
        temp_v0->unk70 = *arg1;
        temp_v0->unk4 = 300;
    }
}

typedef struct { s32 values[1]; } MapBurstIDs131F30;
typedef struct { f32 values[1]; } MapBurstScales131F30;

typedef struct { u16 values[9]; } MapBurstSurface131F30;

typedef struct {
    u8 reserved00[0x30];
    MapParticlePoint131F30 position;
    u8 reserved3C[0x24];
    MapParticlePoint131F30 direction;
    MapBurstSurface131F30 surface;
    u8 reserved7E[0xA];
    u32 tag;
    f32 countdown;
    u8 reserved90[0xC];
    s8 callback;
    u8 reserved9D[3];
} MapBurstEmitter131F30;

typedef struct {
    u8 header[0x110];
    MapBurstEmitter131F30 emitter;
} MapBurstRecord131F30;

typedef struct {
    s32 kind, mode;
    MapParticlePoint131F30 position, direction;
    MapBurstSurface131F30 surface;
    u16 reserved32;
    f32 parameters[5];
    s16 minimum, maximum;
    f32 tailParameters[3];
} MapBurstPacket131F30;

extern MapBurstIDs131F30 D_800A23A4;
extern MapBurstScales131F30 D_800A23A8;
extern f32 D_800A23C0, D_800A23C4, D_800A23C8, D_800A23CC, D_800A23D0;
extern f32 D_800A23D4, D_800A23D8, D_800A23DC, D_800A23E0, D_800A23E4, D_800A23E8;
void *func_15102920(f32, u8, MapBurstSurface131F30 *, MapParticlePoint131F30 *,
    s32, s32, s32, u32, u8, s32);
void func_151C329C(MapParticlePoint131F30 *, s32, s32);
void *func_15151D6C(MapBurstPacket131F30 *, MapBurstIDs131F30 *, MapBurstScales131F30 *, s32, u8, s32);

/* Emit an expired object's randomized effect and optional point/surface burst. */
void func_1510558C(MapBurstRecord131F30 *record) {
    f32 randomValue;
    u32 firstRandom;
    MapBurstPacket131F30 packet;
    MapBurstIDs131F30 effectIDs;
    MapBurstScales131F30 scales;
    MapBurstEmitter131F30 *emitter;

    randomValue = func_150ADA68();
    firstRandom = (u32)func_150ADA20();
    emitter = &record->emitter;
    func_15102920(randomValue * 25.0f + 15.0f, (u8)(firstRandom % 56 + 200),
        &emitter->surface, &emitter->position, (u32)func_150ADA20() % 81 + 50,
        1, 1, emitter->tag, ((u8 *)record)[0xC], ((u8 *)record)[1]);
    if ((emitter->tag & 31) == 9) {
        if (func_150ADA68() < D_800A23C0) {
            func_151C329C(&emitter->position, ((u8 *)record)[0xC], ((u8 *)record)[1]);
        }
    } else {
        if (func_150ADA68() < D_800A23C4) {
            func_151C329C(&emitter->position, ((u8 *)record)[0xC], ((u8 *)record)[1]);
        }
        if (func_150ADA68() < D_800A23C8) {
            effectIDs = D_800A23A4;
            scales = D_800A23A8;
            packet.kind = 1;
            packet.mode = 3;
            packet.position = emitter->position;
            packet.direction.x = -emitter->direction.x;
            packet.direction.y = -emitter->direction.y;
            packet.direction.z = -emitter->direction.z;
            packet.surface = emitter->surface;
            packet.parameters[0] = D_800A23CC;
            packet.parameters[1] = D_800A23D0;
            packet.parameters[2] = D_800A23D4;
            packet.parameters[3] = D_800A23D8;
            packet.parameters[4] = D_800A23DC;
            packet.minimum = 15;
            packet.maximum = 15;
            packet.tailParameters[0] = D_800A23E0;
            packet.tailParameters[1] = D_800A23E4;
            packet.tailParameters[2] = D_800A23E8;
            func_15151D6C(&packet, &effectIDs, &scales, 1,
                ((u8 *)record)[0xC], ((u8 *)record)[1]);
        }
    }
}

typedef struct { s16 x, y, z; u8 reserved06[16]; } MapTrailSource131F30;
typedef struct {
    MapTrailSource131F30 *source;
    f32 scale;
    s16 *gate;
    u8 flags, reserved0D[3];
} MapTrailEmitter131F30;
struct MapTrailRecord131F30 {
    u8 header[0x28];
    MapTrailEmitter131F30 emitter;
};

typedef struct {
    f32 value;
    vertex direction;
    f32 parameter;
    u8 fixed14, fixed15, fixed16;
    u8 byte17, byte18, byte19, byte1A, byte1B, byte1C, byte1D, byte1E, byte1F;
    u8 fixed20, fixed21, reserved22[2];
    s32 field24, field28;
    s16 field2C, field2E, field30;
    u8 field32, reserved33;
    f32 field34;
    s8 field38, field39;
    u8 reserved3A[2];
} MapTrailPacket131F30;
typedef struct {
    MapParticlePoint131F30 position;
    s16 duration;
    u16 field0E;
    s32 constant10;
    s8 flag, count;
    u8 reserved16[2];
} MapTrailHeader131F30;

extern f32 D_800A23EC, D_800A23F0, D_800A23F4, D_800A23F8, D_800A23FC, D_800A2400;
void func_151432BC(MapTrailSource131F30 *, f32 *, f32 *, f32 *, f32 *);
void func_15143794(s16, s16, f32, vertex *);
void *func_1515C2F0(MapTrailHeader131F30 *, s32, MapTrailPacket131F30 *, s32, u8, s32);

void func_15105848(struct207 *arg0, s32 arg1, u8 arg2) {
    MapTrailEmitter131F30 *temp_v0;

    if (arg2 == 0x38) {
        temp_v0 = &((MapTrailRecord131F30 *)arg0)->emitter;
        func_151058B4((MapTrailRecord131F30 *)arg0);
        temp_v0->flags |= 1;
    } else {
        temp_v0 = &((MapTrailRecord131F30 *)arg0)->emitter;
        if (arg2 == 0x39) {
            temp_v0->flags &= 0xFFFE;
        }
    }
}

typedef struct { f32 bottom, top; MapTrailPacket131F30 packet; MapTrailHeader131F30 header; } MapTrailScratch131F30;

/* Emit randomized trail particles while the local floating count exceeds one. */
void func_151058B4(MapTrailRecord131F30 *record) {
    f32 rangeScale, rangeBase;
    MapTrailEmitter131F30 *emitter;
    MapTrailScratch131F30 scratch;
    u32 first, second;
    f32 remaining;

    if (func_151464B8(record->emitter.gate) == 0) {
        emitter = &record->emitter;
        remaining = (func_150ADA68() * D_800A23EC + D_800A23F0) * emitter->scale;
        if (remaining > 1.0f) {
            scratch.header.field0E = 21;
            scratch.header.constant10 = 10;
            scratch.header.flag = -1;
            scratch.packet.fixed14 = 4;
            scratch.packet.fixed15 = 2;
            scratch.packet.fixed16 = 3;
            scratch.packet.byte17 = 0x61;
            scratch.packet.byte18 = 0xF2;
            scratch.packet.byte19 = 0xFF;
            scratch.packet.byte1B = 0xFF;
            scratch.packet.byte1C = 0xFF;
            scratch.packet.byte1D = 0xFF;
            scratch.packet.byte1E = 0xFF;
            scratch.packet.byte1F = 0xFF;
            scratch.packet.fixed20 = 3;
            scratch.packet.fixed21 = 0x24;
            scratch.packet.field24 = 0x200005;
            scratch.packet.field28 = 0x60600;
            scratch.packet.field2C = 20;
            scratch.packet.field2E = 12;
            scratch.packet.field30 = 1;
            scratch.packet.field32 = 0;
            scratch.packet.field34 = 1.0f;
            scratch.packet.field38 = -1;
            scratch.packet.field39 = 0;
            scratch.header.position.y = (f32)emitter->source->y;
            rangeScale = D_800A23F8;
            rangeBase = D_800A23F4;
            do {
                scratch.packet.byte1A = (u8)((u32)func_150ADA20() % 101U + 155);
                scratch.header.count = (s8)(((u32)func_150ADA20() & 3) + 3);
                func_151432BC(emitter->source, &scratch.header.position.x, &scratch.header.position.z, &scratch.top, &scratch.bottom);
                scratch.header.duration = (s16)((u32)func_150ADA20() % 31U + 30);
                scratch.packet.value = func_150ADA68() * rangeScale + rangeBase;
                first = (u32)func_150ADA20();
                second = (u32)func_150ADA20();
                func_15143794((s16)(first & 255), (s16)(second % 22U - 54),
                    func_150ADA68() * 20.0f + 30.0f, &scratch.packet.direction);
                scratch.packet.parameter = func_150ADA68() * D_800A23FC + D_800A2400;
                func_1515C2F0(&scratch.header, 0, &scratch.packet, 0, ((u8 *)record)[0xC], ((u8 *)record)[1]);
                remaining -= 1.0f;
            } while (remaining > 1.0f);
        }
    }
}

void func_15105BC8(struct204 *arg0) {
    if ((arg0->unk34 & 1) != 0) {
        func_1508B20C(arg0->unk28->unk0, arg0->unk28->unk2, arg0->unk28->unk4, 500.0f);
    }
}

typedef struct MapChainNode131F30 {
    u8 reserved00[8];
    struct MapChainNode131F30 *next;
    u8 reserved0C[7];
    u8 type;
    u8 reserved14[0x14];
    s32 key;
} MapChainNode131F30;

/* Find the first matching type-0x2E node in both selected list columns. */
void *func_15105C24(s32 key) {
    s32 group, row;
    s32 nextGroup, nextRow;
    s32 column;
    MapChainNode131F30 *node;
    group = 0;
next_group:
    column = D_800A5770[group] * 4;
    row = 0;
next_row:
    node = *(MapChainNode131F30 **)(D_800DCE50 + (((row * 4 - row) * 4 + row) << 5) + column);
    if (node != NULL) {
next_node:
        if (node->type == 0x2E && node->key == key) { return node; }
        node = node->next;
        if (node != NULL) { goto next_node; }
    }
    nextRow = (u8)(row + 1);
    row = nextRow;
    if (nextRow < 2) { goto next_row; }
    nextGroup = (u8)(group + 1);
    group = nextGroup;
    if (nextGroup < 2) { goto next_group; }
    return NULL;
}
