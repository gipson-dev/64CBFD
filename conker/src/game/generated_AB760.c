#include <ultra64.h>
extern u8 D_8009D910[];

/* Non-matching placeholders for the text-only asm slice asm/AB760.s. */

void func_1507EB4C();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E2B0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E3C0.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E500.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E5C8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E6B8.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E73C.s")

s32 func_1507E968(u8 *);
u8 *func_1507E908(u8 *, s32);
u8 *func_1507E9F8(u8 *, s32 *);
void func_150302F0(s32, s32);
void func_1507E5C8(u8 *, s32);

void func_1507E7E4(u8 *actor, u8 channel, u8 priority, u16 duration, s32 amount) {
    u8 *definition;
    u8 *animations;
    s32 oldChannel = actor[0x6F];

    if (oldChannel == channel && actor[0x71] == priority &&
        *(u16 *)(actor + 0x72) == duration) {
        return;
    }
    if (priority == 3 || actor[0x70] == oldChannel || channel == oldChannel ||
        *(u16 *)(actor + 0x72) == 0 || actor[0x71] < priority) {
        if (channel < func_1507E968(actor)) {
            definition = func_1507E908(actor, actor[0x6F]);
            if (definition[4] != 0) {
                animations = func_1507E9F8(actor, 0);
                if (animations != 0) {
                    func_150302F0((s32)actor, animations[definition[4] - 1]);
                }
            }
            actor[0x6F] = channel;
            *(u16 *)(actor + 0x72) = duration;
            actor[0x71] = priority;
            func_1507E5C8(actor, amount);
        }
    }
}

extern u8 *D_800D1C90[];
s32 func_150849A0(u8 *);

u8 *func_1507E908(u8 *actor, s32 index) {
    u8 *archive;
    u8 *records;

    archive = D_800D1C90[func_150849A0(actor)];
    if (archive != 0) {
        archive -= 8;
        records = *(u8 **)archive;
        if (records != 0) {
            return records + (u32)index * 10;
        }
    }
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507E968.s")

void func_1507E9E8(s32 arg0, s32 arg1) {
}

u8 *func_1507E9F8(u8 *arg0, s32 *arg1) {
    if (func_150849A0(arg0) == 0) {
        if (arg1 != 0) {
            *arg1 = 5;
        }
        return D_8009D910;
    }
    if (arg1 != 0) {
        *arg1 = 0;
    }
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_AB760/func_1507EA44.s")

void func_1507E7E4(u8 *, u8, u8, u16, s32);

void func_1507EABC(u8 *actor) {
    func_1507E7E4(actor, actor[0x70], 3, 0xFFFF, 10);
    actor[0x71] = 0;
    *(u16 *)(actor + 0x72) = 0;
    if (actor[0x6C] >= 10) {
        actor[0x6C] = 0;
        actor[0x6A] = 0;
    }
    if (actor[0x6D] >= 10) {
        actor[0x6D] = 0;
        actor[0x6B] = 0;
    }
}

void func_1507EB2C(register s32 arg0) {
    func_1507EB4C(arg0, 0);
}

void func_1507EB4C(u8 *arg0, s32 arg1) {
    if (arg1 != *(arg0 + 0x70)) {
        *(arg0 + 0x70) = arg1;
        func_1507EABC(arg0);
    }
}
