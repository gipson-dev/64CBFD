#include <ultra64.h>
#include "structs.h"

typedef struct {
    s32 first;
    s32 second;
    s32 third;
    s32 fourth;
} FourWord1CC440;

/* Non-matching placeholders for the text-only asm slice asm/1CC440.s. */

void func_1519F48C(u8 *arg0);
void func_151A0928(u8 *arg0);
void func_1516972C(u8 *arg0);

s32 func_1519EF90() {
    return 0;
}

void func_1519F108(u8 *arg0) {
    register u8 **link = *(u8 ***)(arg0 + 0x98);
    register u8 *record = *link;

    if (record != NULL) {
        register s32 state = *(s32 *)(arg0 + 0x20);
        register FourWord1CC440 *fields = (FourWord1CC440 *)(record + 0x58);

        if (state == 6) {
            fields->first = 0;
        }
        if (*(s32 *)(arg0 + 0x20) == 7) {
            fields->third = 0;
        }
    }
    func_151478F4(arg0);
}

void func_1519F168(u8 *arg0) {
    register u8 **link = *(u8 ***)(arg0 + 0x98);
    register u8 *record = *link;

    if (record != NULL) {
        register s32 state = *(s32 *)(arg0 + 0x20);
        register FourWord1CC440 *fields = (FourWord1CC440 *)(record + 0x58);

        if (state == 6) {
            fields->first = 0;
        }
        if (*(s32 *)(arg0 + 0x20) == 7) {
            fields->third = 0;
        }
    }
    func_15147928(arg0);
}

s32 func_1519F1C8() {
    return 0;
}

void func_1519F3B8(u8 *arg0) {
    FourWord1CC440 *temp_v1;
    s32 r = func_1519F1C8(arg0, 6);

    temp_v1 = (FourWord1CC440 *) (arg0 + 0x58);
    temp_v1->first = r;
    temp_v1->second = 0;
    r = func_1519F1C8(arg0, 7);
    temp_v1->third = r;
    temp_v1->fourth = 0;
}

/* Note 535: four-resource ownership-specific teardown. */
void func_1519F400(u8 *arg0) {
    u8 **resources = (u8 **) (arg0 + 0x58);

    if (resources[0] != NULL) {
        func_1519F48C(resources[0]);
    }
    if (resources[2] != NULL) {
        func_1519F48C(resources[2]);
    }
    if (resources[1] != NULL) {
        func_151A0928(resources[1]);
        func_1516972C(resources[1]);
    }
    if (resources[3] != NULL) {
        func_151A0928(resources[3]);
        func_1516972C(resources[3]);
    }
}

void func_1519F48C(u8 *arg0) {
    register u8 **link = *(u8 ***)(arg0 + 0x98);
    register u8 *record = *link;

    if (record != NULL) {
        register s32 state = *(s32 *)(arg0 + 0x20);
        register FourWord1CC440 *fields = (FourWord1CC440 *)(record + 0x58);

        if (state == 6) {
            fields->first = 0;
        }
        if (*(s32 *)(arg0 + 0x20) == 7) {
            fields->third = 0;
        }
        *link = NULL;
    }

    arg0[0x30] = 0;
    *(u16 *)(arg0 + 0x1E) &= ~2;
    ((u8 *)link)[4] |= 1;
}

s32 func_1519F4F0() {
    return 0;
}

s32 func_1519F7F0() {
    return 0;
}

s32 func_1519FE6C() {
    return 0;
}

s32 func_151A084C() {
    return 0;
}

void func_151A0928(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x28) + 0x58;

    if (arg0[0x2C] == 6) {
        *(s32 *) (temp_v0 + 4) = 0;
    } else {
        *(s32 *) (temp_v0 + 0xC) = 0;
    }
}

void func_151A0950(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 **link = *(u8 ***)(arg0 + 0x98);
    u8 *record;
    s32 owner;

    if (arg2 == 0xA) {
        record = *link;
        if (record != NULL) {
            owner = *(s32 *)(record + 0x18);
            if (owner == *(s32 *)arg1 || record[0x1C] == arg1[4]) {
                func_1519F48C(arg0);
            }
        }
    }
}

void func_151A09B4(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *child = *(u8 **)(*(u8 **)(arg0 + 0x28) + 0x18);

    if (arg2 == 0 &&
            (child == *(u8 **)arg1 || child[0x3B] == arg1[4])) {
        func_151A0928(arg0);
        func_1516972C(arg0);
    }
}

typedef struct {
    f32 x;
    f32 y;
    f32 z;
    u8 selected;
    u8 padD[3];
    f32 zero;
} ActorHeightEffectPayload;
extern u8 D_800C35EA;
u32 func_1510F8CC(u32);
struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
/* Capture the actor position and cached height, then submit the selected effect. */
void func_151A0A10(u8 *actor, s16 effect, u8 variant, s32 flags) {
    struct260 *record;
    ActorHeightEffectPayload payload;

    if (actor != NULL) {
        payload.x = *(f32 *)(actor + 0x14);
        payload.z = *(f32 *)(actor + 0x1C);
        if (D_800C35EA != 1) {
            payload.y = *(f32 *)(actor + 0x180);
            payload.zero = 0.0f;
            switch (func_1510F8CC(*(u32 *)(actor + 0x184))) {
                case 10:
                    payload.selected = 0;
                    break;
                case 15:
                case 17:
                    payload.selected = 1;
                    break;
                default:
                    payload.selected = 0;
                    break;
            }
            record = func_151491F4(effect, -1, 1, 1, 0, 0x14, variant, flags);
            if (record != NULL) {
                memcpy((u8 *)record + 0x28, &payload, 0x14);
            }
        }
    }
}

s32 func_151A0AF8() {
    return 0;
}

s32 func_151A0C0C() {
    return 0;
}

extern f32 D_800A8D20;
void func_151A11CC(f32, f32, f32, f32, f32, s32, s32, s32, s32, s32, f32, s32, s32, s32, s32, s32, s32, f32, s32, s32, s32, s32, s32, s32, s32, s32, u32, s32);
/* Submit the original fixed debug-display argument packet to its retail stub. */
void func_151A0E40(f32 x, f32 y, f32 value, u8 variant, s32 flags) {
    func_151A11CC(
        x, y, value, 163.0f, D_800A8D20,
        160, 75, 1055, 1270, 1, D_800A8D20,
        135, 68, 1055, 1270, 2, 1, D_800A8D20,
        70, 66, 1055, 1270, 7, 65, 4, 1, variant, flags);
}

extern f32 D_800A8D24;
/* Submit the original fixed debug-display argument packet to its retail stub. */
void func_151A0F28(f32 x, f32 y, f32 value, u8 variant, s32 flags) {
    func_151A11CC(
        x, y, value, 163.0f, D_800A8D24,
        160, 75, 1055, 1270, 1, D_800A8D24,
        135, 68, 1055, 1270, 2, 1, D_800A8D24,
        70, 66, 1055, 1270, 7, 65, 4, 1, variant, flags);
}

s32 func_151A1010() {
    return 0;
}

void func_151A11CC(f32 arg0, f32 arg1, f32 arg2, f32 arg3, f32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9, f32 arg10, s32 arg11, s32 arg12, s32 arg13, s32 arg14, s32 arg15, s32 arg16, f32 arg17, s32 arg18, s32 arg19, s32 arg20, s32 arg21, s32 arg22, s32 arg23, s32 arg24, s32 arg25, u32 arg26, s32 arg27) {
}

s32 func_151A11E4() {
    return 0;
}

s32 func_151A175C() {
    return 0;
}

typedef struct {
    f32 x, y, z;
} EffectPacketPosition1CC440;

typedef struct {
    EffectPacketPosition1CC440 position;
    f32 sourceValueA;
    f32 phase;
    f32 sourceValueB;
    s16 parameters[4];
} RecordEffectPacket1CC440;

struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);

/* Spawn an effect from the record's captured 32-byte parameter packet. */
void func_151A18DC(struct260 *record) {
    struct260 *effect;
    RecordEffectPacket1CC440 packet;

    packet.position = *(EffectPacketPosition1CC440 *)((u8 *)record + 0x28);
    packet.sourceValueA = *(f32 *)((u8 *)record + 0x34);
    packet.phase = 0.0f;
    packet.sourceValueB = *(f32 *)((u8 *)record + 0x38);
    packet.parameters[0] = *(s16 *)((u8 *)record + 0x3E);
    packet.parameters[1] = *(s16 *)((u8 *)record + 0x40);
    packet.parameters[2] = *(s16 *)((u8 *)record + 0x42);
    packet.parameters[3] = *(s16 *)((u8 *)record + 0x44);
    effect = func_151491F4(*(s16 *)((u8 *)record + 0x3C), -1, 3, 1, 0,
                          sizeof(packet), ((u8 *)record)[0xC], ((u8 *)record)[1]);
    if (effect != NULL) {
        memcpy((u8 *)effect + 0x28, &packet, sizeof(packet));
    }
}

s32 func_151A1998() {
    return 0;
}

/* Later matching lifetime ramps intentionally override earlier ramps. */
void func_151A1E34(u8 *effect) {
    s16 *parameters = (s16 *)(effect + 0x50);
    s32 time = *(s16 *)(effect + 0x38);

    if (parameters[2] < time) {
        effect[0x3F] = parameters[0] * (parameters[1] - time);
    }
    if (parameters[5] < time) {
        *(s16 *)(effect + 0x34) = *(s16 *)(effect + 0x36) = parameters[3] * (parameters[4] - time);
    }
    if (time < parameters[6]) {
        effect[0x3F] = parameters[7] * time;
    }
    if (time < parameters[8]) {
        *(s16 *)(effect + 0x34) = *(s16 *)(effect + 0x36) = parameters[9] * time;
    }
}

typedef struct {
    EffectPacketPosition1CC440 position;
    f32 sourceValueA;
    f32 phase;
    f32 sourceValueB;
    s16 parameters[6];
} RecordEffectPacketSix1CC440;

/* Spawn an effect from the record's captured 36-byte parameter packet. */
void func_151A1EE8(struct260 *record) {
    struct260 *effect;
    RecordEffectPacketSix1CC440 packet;
    u8 *bytes = (u8 *)record;

    packet.position = *(EffectPacketPosition1CC440 *)(bytes + 0x28);
    packet.sourceValueA = *(f32 *)(bytes + 0x34);
    packet.phase = 0.0f;
    packet.sourceValueB = *(f32 *)(bytes + 0x38);
    packet.parameters[0] = *(s16 *)(bytes + 0x3E);
    packet.parameters[1] = *(s16 *)(bytes + 0x40);
    packet.parameters[2] = *(s16 *)(bytes + 0x42);
    packet.parameters[3] = *(s16 *)(bytes + 0x44);
    packet.parameters[4] = *(s16 *)(bytes + 0x46);
    packet.parameters[5] = *(s16 *)(bytes + 0x48);
    effect = func_151491F4(*(s16 *)(bytes + 0x3C), -1, 4, 1, 0,
                          sizeof(packet), bytes[0xC], bytes[1]);
    if (effect != NULL) {
        memcpy((u8 *)effect + 0x28, &packet, sizeof(packet));
    }
}

s32 func_151A1FB4() {
    return 0;
}

s32 func_151A24A8() {
    return 0;
}

s32 func_151A25E0() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A26EC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2960.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2A14.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2AD4.s")

void func_151A2B84(f32 *arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4, f32 *arg5) {
    f32 t = 1.0f - arg4;

    arg5[0] = arg0[0] * t;
    arg5[1] = arg0[1] * t;
    arg5[2] = arg0[2] * t;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2BD0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1CC440/func_151A2C24.s")

s32 func_151A2F0C() {
    return 0;
}

s32 func_151A3150() {
    return 0;
}
