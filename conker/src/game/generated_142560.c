#include <ultra64.h>

extern s32 D_800BE9F0;
void func_1511490C(f32 matrix[4][4], u8 *actor);
void func_150A7960(f32 matrix[4][4], f32 x, f32 y, f32 z,
                   f32 *outX, f32 *outY, f32 *outZ);

extern s32 D_800BE9E4;
extern u8 *D_800DBFF0;
extern u8 *D_800DBEF4;
extern u8 D_800C35EA;
extern f32 D_800A31E0;

/* Non-matching placeholders for the text-only asm slice asm/142560.s. */

s32 func_151169B4();
u8 *func_151149AC(u32 arg0);
u8 *func_15083E90(s32 arg0);
f32 func_150484A0(f32 arg0, f32 arg1);
s32 func_15195FB0();
s32 func_15022B08(s32 recordIndex, s32 category);

f32 func_151172D8(u8 *arg0, f32 arg1);
f32 func_15117518(u8 *arg0, f32 arg1);

extern f32 D_800A31F4;
s32 func_151189AC();

void func_151150B0(s32 arg0) {
}

void func_151150BC(u8 *arg0) {
    f32 temp;

    *(f32 *) (arg0 + 0x68) = (f32)((*(s32 *) (arg0 + 0x3C) >> 16) * D_800BE9E4) * 0.00390625f;
    *(f32 *) (arg0 + 0x8) = *(volatile f32 *) (arg0 + 0x68) + *(f32 *) (arg0 + 0x8);
    temp = *(volatile f32 *) (arg0 + 0x8);
    if (temp < 0.0f) {
        *(f32 *) (arg0 + 0x8) = temp + 360.0f;
        return;
    }
    if (temp >= 360.0f) {
        *(f32 *) (arg0 + 0x8) = temp - 360.0f;
    }
}

void func_1511515C(u8 *arg0) {
    f32 temp;

    *(f32 *) (arg0 + 0x64) = (f32)((*(s32 *) (arg0 + 0x3C) >> 16) * D_800BE9E4) * 0.00390625f;
    *(f32 *) (arg0 + 0x4) = *(volatile f32 *) (arg0 + 0x64) + *(f32 *) (arg0 + 0x4);
    temp = *(volatile f32 *) (arg0 + 0x4);
    if (temp < 0.0f) {
        *(f32 *) (arg0 + 0x4) = temp + 360.0f;
        return;
    }
    if (temp >= 360.0f) {
        *(f32 *) (arg0 + 0x4) = temp - 360.0f;
    }
}

void func_151151FC(u8 *arg0) {
    f32 temp;

    *(f32 *) (arg0 + 0x60) = (f32)((*(s32 *) (arg0 + 0x3C) >> 16) * D_800BE9E4) * 0.00390625f;
    *(f32 *) arg0 = *(volatile f32 *) (arg0 + 0x60) + *(f32 *) arg0;
    temp = *(volatile f32 *) arg0;
    if (temp < 0.0f) {
        *(f32 *) arg0 = temp + 360.0f;
        return;
    }
    if (temp >= 360.0f) {
        *(f32 *) arg0 = temp - 360.0f;
    }
}

void func_1511529C(s32 arg0) {
}

s32 func_151152A8() {
    return 0;
}

s32 func_15115368() {
    return 0;
}

s32 func_151155C0() {
    return 0;
}

s32 func_1511575C() {
    return 0;
}

s32 func_15115E0C(f32 arg0, f32 arg1, u8 *arg2) {
    return 0;
}

void func_15115EDC(u8 *arg0, u8 *arg1) {
    f32 old_x;
    f32 old_z;
    f32 x;
    f32 z;

    old_x = *(f32 *) (arg0 + 0x7C);
    old_z = *(f32 *) (arg0 + 0x80);
    func_15115E0C(old_x, old_z, arg1);

    if (*(u16 *) (arg1 + 0x84) == 0x4B) {
        x = *(f32 *) (arg0 + 0x7C);
        z = *(f32 *) (arg0 + 0x80);
        old_x = (x - old_x) * 4.0f;
        old_z = (z - old_z) * 4.0f;
        *(f32 *) (arg0 + 0x7C) = x + old_x;
        *(f32 *) (arg0 + 0x80) = z + old_z;
    }
}

s32 func_15115F68() {
    return 0;
}

s32 func_15116058() {
    return 0;
}

void func_15116110(u8 *arg0) {
    s32 packed;
    u16 selector;
    u8 byte3;
    u8 byte2;

    if (*(s32 *) (arg0 + 0x7C) == 0) {
        packed = *(s32 *) (arg0 + 0x3C);
        selector = packed & 0x7FFF;
        byte3 = packed >> 24;
        byte2 = packed >> 16;
        *(s32 *) (arg0 + 0x7C) = func_15195FB0(
            arg0, selector, packed >> 15, -1, 0, byte3, byte2);
        *(s32 *) (arg0 + 0x3C) = 0;
    }
}

s32 func_1511617C() {
    return 0;
}

s32 func_151162D4() {
    return 0;
}

s32 func_151163C0() {
    return 0;
}

s32 func_1511650C() {
    return 0;
}

#include "structs.h"
s32 func_150490A8(struct17 *);
f32 func_15048A40(u8);

/* Project the actor's speed onto the horizontal direction from an origin. */
s32 func_15116888(s32 originX, s32 originZ, void *unused, void *actor) {
    s32 actorX = (s32)*(f32 *)((u8 *)actor + 0x14);
    s32 actorZ = (s32)*(f32 *)((u8 *)actor + 0x1C);
    s32 deltaZ = (s32)((u32)actorZ - (u32)originZ);
    s32 facing;
    s32 angle;
    f32 scale;
    struct17 offset;
    f32 projected;
    offset.unk0 = (s32)((u32)actorX - (u32)originX);
    offset.unk8 = deltaZ;
    angle = func_150490A8(&offset);
    facing = *(u16 *)((u8 *)actor + 0x76);
    facing = 64 - (facing >> 8);
    facing -= angle;
    scale = func_15048A40((u8)facing);
    projected = *(f32 *)((u8 *)actor + 0x3C) * scale;
    return (s32)projected;
}

void func_15116924(s32 arg0) {
}

void func_15116930(u8 *arg0, u8 *arg1) {
    u8 value;
    u8 **owner_slot = (u8 **) (arg1 + 0x31C);

    if (*(arg0 + 0x4F) & 4) {
        value = *(arg0 + 0x73);

        if (!(value & 3)) {
            if (!(value & 4)) {
                if (*(*owner_slot + 0x57) == 1) {
                    *(arg0 + 0x73) = value & 0xFFFC;
                    *(arg0 + 0x73) |= 2;
                }
            }
        }
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_15116984.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_151169B4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_15116BAC.s")

s32 func_15116D7C() {
    return 0;
}

s32 func_15116EA4() {
    return 0;
}

f32 func_151172D8(u8 *arg0, f32 arg1) {
    return 0.0f;
}

void func_151174A0(u8 *arg0) {
    *(f32 *)(arg0 + 8) = func_151172D8(arg0, *(f32 *)(arg0 + 8));
}

void func_151174C8(u8 *arg0) {
    *(f32 *)(arg0 + 4) = func_151172D8(arg0, *(f32 *)(arg0 + 4));
}

void func_151174F0(u8 *arg0) {
    *(f32 *)(arg0 + 0) = func_151172D8(arg0, *(f32 *)(arg0 + 0));
}

f32 func_15117518(u8 *arg0, f32 arg1) {
    return 0.0f;
}

void func_15117770(u8 *arg0) {
    *(f32 *)(arg0 + 0) = func_15117518(arg0, *(f32 *)(arg0 + 0));
}

void func_15117798(u8 *arg0) {
    *(f32 *)(arg0 + 8) = func_15117518(arg0, *(f32 *)(arg0 + 8));
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_151177C0.s")

s32 func_151179BC() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_15117D3C.s")

s32 func_15117DA4() {
    return 0;
}

s32 func_15117F3C() {
    return 0;
}

void func_1511896C(register s32 arg0) {
    func_151189AC(arg0, 0);
}

void func_1511898C(register s32 arg0) {
    func_151189AC(arg0, 3);
}

s32 func_151189AC() {
    return 0;
}

s32 func_15118F24() {
    return 0;
}

void func_151193AC(u8 *arg0, u8 *arg1) {
    if (*(s32 *) arg1 == 1) {
        if (*(arg1 + 0x65) == 0) {
            u8 temp_v0 = *(arg0 + 0x73);

            if (!(temp_v0 & 3)) {
                if (!(temp_v0 & 4)) {
                    *(arg0 + 0x73) = temp_v0 & 0xFFFC;
                    *(arg0 + 0x73) |= 2;
                }
            }
        }
    }
}

s32 func_151193F4() {
    return 0;
}

s32 func_151194D4() {
    return 0;
}

s32 func_151196D4() {
    return 0;
}

s32 func_15119938() {
    return 0;
}

s32 func_15119FC0() {
    return 0;
}

s32 func_1511A410(s8 *records, s32 *second_index) {
    /* Retail reserves three scratch words although only two matches are kept. */
    s32 matches[3];
    s32 match_count = 0;
    s32 index = 0;

    matches[0] = 0;
    matches[1] = 0;

    while ((records[index << 3] != -0x21) && (match_count < 2)) {
        if (records[index << 3] == -3) {
            matches[match_count] = index;
            match_count++;
        }
        index++;
    }

    *second_index = matches[1];
    return matches[0];
}

s32 func_1511A494() {
    return 0;
}

void func_1511A6FC(u8 *arg0) {
    if (*(s32 *) (arg0 + 0x3C) != 0) {
        func_15116110(arg0);
    }
    func_1511A494(arg0, arg0 + 0x80, arg0 + 0x84);
}

void func_1511A738(u8 *arg0) {
    if (D_800C35EA == 1) {
        if (func_15022B08((arg0 - D_800DBEF4) / 0xA0, 0) != 0) {
            *(s32 *) (arg0 + 0x7C) = 0;
            *(f32 *) (arg0 + 0x18) = 0.0f;
        }
    }

    func_151162D4(arg0);
    func_1511A494(arg0, arg0 + 0x80, arg0 + 0x84);
}

void func_1511A7C0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x80);
    s32 i = 0;
    s32 offset = 0;

    temp_v0[0x1E] = 1;
    *(f32 *) (temp_v0 + 0x10) = 0.0f;
    temp_v0[0x1C] = 0;
    temp_v0[0x1D] = 7;
    *(f32 *) (temp_v0 + 0x14) = 260.0f;
    *(f32 *) (temp_v0 + 0x18) = 100.0f;

    while (i < *(u16 *) (arg0 + 0x16)) {
        *(f32 *) (*(u8 **) (temp_v0 + 4) + offset) = 0.0f;
        i++;
        offset += sizeof(f32);
    }
}

s32 func_1511A838() {
    return 0;
}

s32 func_1511AF30() {
    return 0;
}

s32 func_1511B07C() {
    return 0;
}

s32 func_1511B51C() {
    return 0;
}

s32 func_1511B7D4() {
    return 0;
}

s32 func_1511BA24() {
    return 0;
}

s32 func_1511BB04(u8 *arg0, s32 arg1, s32 arg2, f32 arg3, f32 arg4) {
    return 0;
}

void func_1511BDF4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x80);
    u8 *temp_v1;

    if (temp_v0 != NULL) {
        temp_v1 = temp_v0;
    } else {
        temp_v1 = func_15083E90(*(u8 *)(arg0 + 0x3F));
    }

    if (temp_v1 != NULL) {
        func_1511BB04(arg0, *(s32 *)(temp_v1 + 0x14),
                      *(s32 *)(temp_v1 + 0x1C), 1.0f, 1.0f);
    }
}

void func_1511BE5C(u8 *arg0) {
    *(f32 *)(arg0 + 4) =
        func_150484A0((f32)*(s16 *)(arg0 + 0x10) - *(f32 *)(D_800DBFF0 + 0x2F8),
                      (f32)*(s16 *)(arg0 + 0x14) - *(f32 *)(D_800DBFF0 + 0x300)) *
        D_800A31E0;
}

s32 func_1511BEBC() {
    return 0;
}

void func_1511C540() {
}

s32 func_1511C548() {
    return 0;
}

s32 func_1511C638() {
    return 0;
}

void func_1511CB2C(s32 arg0, f32 *arg1) {
    *arg1 = D_800A31F4;
}

s32 func_1511CB44() {
    return 0;
}

s32 func_1511D394() {
    return 0;
}

s32 func_1511D7BC() {
    return 0;
}

s32 func_1511D9E4() {
    return 0;
}

s32 func_1511DBC4() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_1511DD98.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_1511DF6C.s")

s32 func_1511E780() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_1511EC50.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_1511ED84.s")

s32 func_1511EF40() {
    return 0;
}

/* Position category-0x35 attachments from their linked actor's matrix.
 * Two expected-word guards preserve retail's 0x90-byte matrix frame. */
void func_1511F31C(u8 *object) {
    f32 matrix[4][4];
    f32 x;
    f32 y;
    f32 z;
    u8 *actor;
    u16 selector = *(u16 *)(object + 0x3E);

    if (*(u16 *)(object + 0x54) == 0x8005 && D_800BE9F0 == 0x35) {
        actor = func_151149AC(selector & 0xFF);
        if (actor != NULL) {
            func_1511490C(matrix, actor);
            func_150A7960(matrix, -3.0f, 223.0f, 549.0f, &x, &y, &z);
            *(s16 *)(object + 0x10) = (s16)(s32)x;
            *(s16 *)(object + 0x12) = (s16)(s32)y;
            *(s16 *)(object + 0x14) = (s16)(s32)z;
        }
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_142560/func_1511F3E8.s")

s32 func_1511F4D0() {
    return 0;
}

void func_1511F768(u8 *arg0, s32 arg1) {
    if (*(s32 *)(arg0 + 0x80) == 0) {
        *(s32 *)(arg0 + 0x80) = 1;
    }
}

s32 func_1511F788() {
    return 0;
}

void func_1511F92C(u8 *arg0) {
    register u8 *dst = arg0;
    u8 *src = func_151149AC(*(arg0 + 0x3F));

    if (src != NULL) {
        *(s16 *) (dst + 0x10) = *(s16 *) (src + 0x10);
        *(s16 *) (dst + 0x12) = *(s16 *) (src + 0x12);
        *(s16 *) (dst + 0x14) = *(s16 *) (src + 0x14);
    }
}
