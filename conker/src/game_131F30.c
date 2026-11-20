#include <ultra64.h>
#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1510558C();
s32 func_151058B4(s32 arg0);
s32 func_15105C24();
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

/* Non-matching C placeholders for asm/nonmatchings/game_131F30/func_1510558C.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_131F30/func_1510558C.s")

void func_15105848(struct207 *arg0, s32 arg1, u8 arg2) {
    struct206 *temp_v0;

    if (arg2 == 0x38) {
        temp_v0 = &arg0->unk28;
        func_151058B4(arg0);
        temp_v0->unkC |= 1;
    } else {
        temp_v0 = &arg0->unk28;
        if (arg2 == 0x39) {
            temp_v0->unkC &= 0xFFFE;
        }
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_131F30/func_151058B4.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_131F30/func_151058B4.s")
// void func_151058B4(void *arg0) {
//     s8 spE1;
//     s8 spE0;
//     ?32 spDC;
//     s16 spDA;
//     s16 spD8;
//     ? spD4;
//     f32 spD0;
//     ? spCC;
//     s8 spC9;
//     s8 spC8;
//     f32 spC4;
//     s8 spC2;
//     s16 spC0;
//     s16 spBE;
//     s16 spBC;
//     ?32 spB8;
//     ?32 spB4;
//     s8 spB1;
//     s8 spB0;
//     s8 spAF;
//     s8 spAE;
//     s8 spAD;
//     s8 spAC;
//     s8 spAB;
//     s8 spAA;
//     s8 spA9;
//     s8 spA8;
//     s8 spA7;
//     s8 spA6;
//     s8 spA5;
//     s8 spA4;
//     f32 spA0;
//     ? sp94;
//     f32 sp90;
//     ? sp8C;
//     ? sp88;
//     f32 temp_f20;
//     f32 temp_f20_2;
//     f32 temp_f24;
//     f32 temp_f26;
//     s32 temp_s0;
//     u32 temp_s1;
//     void *temp_s4;
//     f32 phi_f20;
//
//     if (func_151464B8(arg0->unk30) == 0) {
//         temp_s4 = arg0 + 0x28;
//         temp_f20 = ((func_150ADA68() * *(void *)0x800A23EC) + *(void *)0x800A23F0) * temp_s4->unk4;
//         if (temp_f20 > 1.0f) {
//             spDA = 0x15;
//             spDC = 0xA;
//             spA7 = 0x61;
//             spA8 = 0xF2;
//             spE0 = -1;
//             spA4 = 4;
//             spA5 = 2;
//             spA6 = 3;
//             spA9 = 0xFF;
//             spAB = 0xFF;
//             spAC = 0xFF;
//             spAD = 0xFF;
//             spAE = 0xFF;
//             spAF = 0xFF;
//             spB0 = 3;
//             spB1 = 0x24;
//             spB4 = 0x200005;
//             spB8 = 0x60600;
//             spBC = 0x14;
//             spBE = 0xC;
//             spC0 = 1;
//             spC2 = 0;
//             spC4 = 1.0f;
//             spC8 = -1;
//             spC9 = 0;
//             temp_f26 = *(void *)0x800A23F4;
//             temp_f24 = *(void *)0x800A23F8;
//             spD0 = (f32) temp_s4->unk0->unk2;
//             phi_f20 = temp_f20;
// loop_3:
//             spAA = (func_150ADA20() % 0x65U) + 0x9B;
//             spE1 = (func_150ADA20() & 3) + 3;
//             func_151432BC(temp_s4->unk0, &spCC, &spD4, &sp8C, &sp88);
//             spD8 = (func_150ADA20() % 0x1FU) + 0x1E;
//             sp90 = (func_150ADA68() * temp_f24) + temp_f26;
//             temp_s0 = func_150ADA20();
//             temp_s1 = func_150ADA20();
//             func_15143794((s16) (temp_s0 & 0xFF), (s16) ((temp_s1 % 0x16U) - 0x36), (func_150ADA68() * 20.0f) + 30.0f, &sp94);
//             spA0 = (func_150ADA68() * *(void *)0x800A23FC) + *(void *)0x800A2400;
//             func_1515C2F0(&spCC, 0, &sp90, 0, (?32) arg0->unkC, (?32) arg0->unk1);
//             temp_f20_2 = phi_f20 - 1.0f;
//             phi_f20 = temp_f20_2;
//             if (temp_f20_2 > 1.0f) {
//                 goto loop_3;
//             }
//         }
//     }
// }

void func_15105BC8(struct204 *arg0) {
    if ((arg0->unk34 & 1) != 0) {
        func_1508B20C(arg0->unk28->unk0, arg0->unk28->unk2, arg0->unk28->unk4, 500.0f);
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_131F30/func_15105C24.s. */
#pragma GLOBAL_ASM("asm/nonmatchings/game_131F30/func_15105C24.s")
// void *func_15105C24(s32 arg0) {
//     s32 temp_t4;
//     s32 temp_t5;
//     void *temp_a0;
//     void *temp_a0_2;
//     s32 phi_v1;
//     s32 phi_v0;
//     void *phi_a0;
//
//     phi_v0 = 0;
// loop_1:
//     phi_v1 = 0;
// loop_2:
//     temp_a0 = *((((((phi_v1 * 4) - phi_v1) * 4) + phi_v1) << 5) + 0x800DCE50 + (((phi_v0 * 4) + 0x800A0000)->unk5770 * 4));
//     phi_a0 = temp_a0;
//     if (temp_a0 != 0) {
// loop_3:
//         if ((phi_a0->unk13 == 0x2E) && (arg0 == phi_a0->unk28)) {
//             return phi_a0;
//         }
//         temp_a0_2 = phi_a0->unk8;
//         phi_a0 = temp_a0_2;
//         if (temp_a0_2 != 0) {
//             goto loop_3;
//         }
//     }
//     temp_t4 = (phi_v1 + 1) & 0xFF;
//     phi_v1 = temp_t4;
//     if (temp_t4 < 2) {
//         goto loop_2;
//     }
//     temp_t5 = (phi_v0 + 1) & 0xFF;
//     phi_v0 = temp_t5;
//     if (temp_t5 < 2) {
//         goto loop_1;
//     }
//     return NULL;
// }
