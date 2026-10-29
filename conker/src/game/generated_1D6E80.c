#include <ultra64.h>
#include "structs.h"
extern f32 D_800A8F74;
s32 func_15045800(f32 *, u16, f32, void *);
void func_151ABE40(f32 *, void *, s32, u8, s32);

void func_1516972C(struct102 *);

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } PayloadOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } PayloadOwnerLinkEvent;

/* Non-matching placeholders for the text-only asm slice asm/1D6E80.s. */

s32 func_1519F400();

/* Probe below the attached actor and submit a height-aligned effect on a hit. */
void func_151A99D0(u8 *input) {
    u8 *owner = input;
    f32 position[3];
    u8 *actor;

    actor = *(u8 **)(owner + 0x18);
    position[0] = *(f32 *)(actor + 0x14);
    if (D_800A8F74 < *(f32 *)(actor + 0x118)) {
        position[1] = *(f32 *)(actor + 0x118) + 100.0f;
    } else {
        position[1] = *(f32 *)(actor + 0x18) + 150.0f;
    }
    position[2] = *(f32 *)(actor + 0x1C);
    if (func_15045800(position, 0, position[1] - 300.0f, owner + 0x34)) {
        position[1] = *(f32 *)(owner + 0x34);
        func_151ABE40(position, owner + 0x34, 3, owner[0xC], owner[1]);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9AA4.s")

s32 func_151A9BA0() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9CA0.s")

/* Note 313: original ROM implementation, retained as assembly until C conversion. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9DC0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151A9EC0.s")

s32 func_151A9FC8() {
    return 0;
}

s32 func_151AA09C() {
    return 0;
}

void func_151AA170(s32 arg0) {
}

void func_151AA17C(u8 *arg0) {
    void *volatile rec_ptr;
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = *(u8 **) (arg0 + 0x18);
    rec.code = arg0[0x1C];
    rec_ptr = &rec;
    func_15147D64(&rec, 0xA);
    func_151494E0(rec_ptr, 0xA);
    func_1519F3B8(arg0);
}

void func_151AA1D0(u8 *arg0) {
    func_1519F400(arg0);
}

void func_151AA1F0(u8 *arg0) {
    func_1519F400(arg0);
}

void func_151AA210(u8 *arg0) {
    void *volatile rec_ptr;
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = *(u8 **) (arg0 + 0x18);
    rec.code = arg0[0x1C];
    rec_ptr = &rec;
    func_15147D64(&rec, 0xA);
    func_151494E0(rec_ptr, 0xA);
    func_1519F3B8(arg0);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA264.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA30C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA48C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA5A4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AA6D8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AAA4C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AAABC.s")

s32 func_151AAB50(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80) + 0x58;

    *(s32 *)(temp_v0 + 0x14) = 0;
    func_151352EC(arg0);
}

s32 func_151AAB78(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80) + 0x58;

    *(s32 *)(temp_v0 + 0x14) = 0;
    func_1513530C(arg0);
}

s32 func_151AABA0(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x84) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x84) = 0;
    return result;
}

s32 func_151AABC4() {
    return 0;
}

s32 func_151AADBC(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s32 temp_v1 = *(s16 *) (arg0 + 0x1C) << 4;

    if (temp_v1 >= 0x100) {
        temp_v1 = 0xFF;
    }
    if (temp_v1 < *(temp_v0 + 0x1B)) {
        *(temp_v0 + 0x1B) = temp_v1;
    }
    return 1;
}

s32 func_151AADF8() {
    return 0;
}

s32 func_151AB090() {
    return 0;
}

// Retail retains the otherwise dead temp_v0 + 0x58 update before the call.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB180.s")

s32 func_151AB1C4() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB2C4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB3A4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB6B8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB788.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1D6E80/func_151AB7D8.s")

void func_151AB828(u8 *arg0) {
    func_15141DA4(*(s32 *) (arg0 + 0x18), 0, 4);
}

void *func_15190770(struct185 *, s32, u8, s32);

/* Submit an effect for supported actor types and reset the attached timer. */
void func_151AB854(u8 *record) {
    u8 *actor = *(u8 **)(record + 0x18);
    struct185 packet;

    if (actor[4] == 0 || actor[4] == 1 || actor[4] == 2 || actor[4] == 3 || actor[4] == 4 || actor[4] == 150) {
        packet.unk0 = (struct127 *)actor;
        packet.unk4 = actor[0x3B];
        packet.unk6 = 300;
        packet.unk8 = 0;
        packet.unk9 = 0;
        if (actor[4] == 150) {
            packet.unkA = 3;
        } else {
            packet.unkA = 0;
        }
        if (actor[0x127] != 255) {
            *(s16 *)(*(u8 **)(actor + 0x31C) + 0x66) = 500;
        }
        func_15190770(&packet, 0, record[0xC], record[1]);
    }
}

void func_151AB920(s32 arg0, s32 arg1) {
}

/* Snapshot actor fields, then copy the packet if allocation succeeds. */
void func_151AB930(u8 *actor) {
    extern f32 D_800A9014;
    extern u8 func_151D8E20(void);
    extern void *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
    extern void *memcpy(void *, const void *, u32);
    u8 *created;
    struct {
        u8 *actor;
        u8 slot;
        u32 value;
        f32 time, scale, lifetime;
        u8 selector;
    } packet;

    packet.actor = actor;
    packet.slot = actor[0x3B];
    packet.value = *(u16 *)(actor + 0x84);
    packet.time = 0.0f;
    packet.scale = D_800A9014;
    packet.lifetime = 3.0f;
    packet.selector = func_151D8E20();
    created = func_151491F4(0x3C, -1, 0xE, 1, 9, 0x1C, 0xFF, 0);
    if (created != NULL) {
        memcpy(created + 0x28, &packet, 0x1C);
    }
}

s32 func_151AB9C8() {
    return 0;
}

/* Retarget the payload owner link or release its matching actor. */
void func_151ABD54(struct260 *owner, s32 eventAddress, u8 command) {
    PayloadOwnerLink *link = (PayloadOwnerLink *)((u8 *)owner + 0x28);
    PayloadOwnerLinkEvent *event = (PayloadOwnerLinkEvent *)eventAddress;

    if (command == 0) {
        if (link->owner == event->before || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    }
}

void func_151ABE00(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    func_1516944C(0x20, &rec, 0xC);
}
