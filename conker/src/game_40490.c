#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15013000();
s32 func_150130B4();
s32 func_15013778();
s32 func_150139AC();
s32 func_15013C38();
s32 func_15013DE8();
s32 func_150142EC();
s32 func_150144B8();
s32 func_1501474C();
s32 func_15014B60();
s32 func_15014F6C();
s32 func_150151D4();
s32 func_15015354();
s32 func_150156F4();
/* End generated placeholder declarations. */

s32 func_151BE850(struct17 *arg0, s32 arg1, u8 arg2, u8 arg3, u8 arg4, u8 arg5, u8 arg6);
void func_151A9390(u8 arg0, u8 arg1, f32 arg2, f32 arg3, s32 arg4, u8 arg5, s32 arg6);

void func_15012FE0(void) {
    D_800BE570 = 0;
    D_800BE574 = 0;
    D_800BE575 = 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15013000.s. */
s32 func_15013000() {
    return 0;
}
// requires jump table
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150130B4.s. */
s32 func_150130B4() {
    return 0;
}

s32 func_1501370C(struct16 *arg0) {
    u8 idx = arg0->unk17;
    void (*func)(void) = D_80082EA0[idx];

    if (func != NULL) {
        func();
    }
    return 1;
}

s32 func_1501374C(struct16 *arg0) {
    arg0->unk16 |= 4;
    func_1515D088(arg0);
    return 1;
}

// fat struct definition:
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15013778.s. */
s32 func_15013778() {
    return 0;
}

s32 func_1501396C(struct16 *arg0) {
    u8 idx = arg0->unk17;
    void (*func)(void) = D_80082ECC[idx];

    if (func != NULL) {
        func();
    }
    return 1;
}

// another struct
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150139AC.s. */
s32 func_150139AC() {
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15013C38.s. */
s32 func_15013C38() {
    return 0;
}

s32 func_15013D38(u8 *arg0) {
    struct17 tmp;
    s32 value;

    arg0[0x16] |= 4;
    tmp.unk0 = *(s16 *)(arg0 + 0);
    tmp.unk4 = *(s16 *)(arg0 + 2);
    tmp.unk8 = *(s16 *)(arg0 + 4);

    value = *(s32 *)(arg0 + 0x18);
    if (value == 0) {
        value = 1;
    }

    func_151BE850(&tmp, *(s32 *)(arg0 + 0x10), value, arg0[0x1F], 0xFF, 1, 1);
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15013DE8.s. */
s32 func_15013DE8() {
    return 0;
}

s32 func_15013F9C(s32 arg0) {
    func_151CD2C0(arg0, 0xFF, 1);
    return 1;
}

s32 func_15013FC4(struct133 *arg0) {
    u8 idx = arg0->unk1B;
    void (*func)(void) = D_80082F40[idx];

    if (func != NULL) {
        func();
    }
    return 1;
}

s32 func_15014004(struct134 *arg0) {
    s32 temp_v1 = arg0->unk1C;
    if (temp_v1 < 0) {
        return 1;
    }
    if (temp_v1 >= 6) {
        return 1;
    }
    D_800E0900[temp_v1] = arg0;
    return 1;
}

s32 func_15014040(struct134 *arg0) {
    s32 temp_v0 = arg0->unk18;
    arg0->unk16 |= 4;
    if (temp_v0 == 0) {
        D_800D9A20 = arg0;
    } else if (temp_v0 == 1) {
        D_800D9A24 = arg0;
    }
    return 1;
}

s32 func_1501407C(s32 arg0) {
    D_800D987C = (u8)0;
    return 1;
}

s32 func_15014094(u8 *arg0) {
    u8 data[0x34];
    u8 *temp_v0;

    arg0[0x16] |= 4;
    bzero(data, sizeof(data));
    *(void **)(data + 0) = arg0;
    *(f32 *)(data + 4) = func_15144598((struct134 *)arg0);
    *(f32 *)(data + 8) = 0.0f;
    func_1510F800(0);
    *(s32 *)(data + 0xC) = func_1510FD20(*(s16 *)(arg0 + 0), *(s16 *)(arg0 + 4));

    temp_v0 = (u8 *)func_15149130(0x12C, -1, 0x21, -1, 0, 0, (struct37 *)0x34, 0xFF, 1);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, data, 0x34);
    }
    return 1;
}
// NON-MATCHING: kinda right idea, but not executed correctly
// void func_15014094(struct134 *arg0) {
//     struct135 tmp;
//
//     tmp.unk0 = arg0;
//     // tmp.unk4 = tmp.unk0;
//     tmp.unk0->unk16 |= 4;
//     // tmp.unkC = tmp.unk0;
//     // arg0 = tmp.unk0;
//     tmp.unk10 = func_15144598(tmp.unk4); //, tmp.unk0);
//     tmp.unk14 = 0.0f;
//     func_1510F800(0);
//     tmp.unk18 = func_1510FD20(arg0->unk0, arg0->unk4, arg0);
//     tmp.unk1C = 0;
//     tmp.unk8 = func_15149130(0x12C, -1, 0x21, -1, 0, 0, 0x34, 0xFF, 1);
//     if (tmp.unk8 != 0) {
//         memcpy(tmp.unk8 + 0x28, &tmp, 0x34);
//     }
// }

s32 func_15014144(u8 *arg0) {
    s32 flags = 0;
    s32 bits = *(s32 *)(arg0 + 0x18);

    if (bits & 8) {
        flags |= 8;
    }
    if (bits & 4) {
        flags |= 4;
    }
    if ((bits & 2) == 0) {
        flags |= 2;
    }
    if (bits & 1) {
        flags |= 1;
    }
    if (bits & 0x10) {
        flags |= 0x10;
    }

    func_151A9390(flags, arg0[0x1F], *(f32 *)&D_8009667C, 100.0f, -1, 0xFF, 1);
    return 1;
}

s32 func_15014220(u8 *arg0) {
    struct {
        f32 unk0;
        void *unk4;
        u8 unk8;
        u8 pad[3];
    } data;
    u8 *temp_v0;

    arg0[0x16] |= 4;
    data.unk0 = 0.0f;
    data.unk4 = arg0;
    data.unk8 = 1;

    temp_v0 = (u8 *)func_15149130(0x12C, -1, 0x26, -1, 0, 0x24, (struct37 *)0xC, 0xFF, 0);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0xC);
    }
    return 1;
}
s32 func_150142AC(u8 *arg0) {
    u8 idx = arg0[0x1B];

    arg0[0x16] |= 4;
    if (idx < 3) {
        D_800D9AA0[idx] = (struct134 *)arg0;
    }
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150142EC.s. */
s32 func_150142EC() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150144B8.s. */
s32 func_150144B8() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_1501474C.s. */
s32 func_1501474C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15014B60.s. */
s32 func_15014B60() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15014F6C.s. */
s32 func_15014F6C() {
    return 0;
}

s32 func_150150A4(void) {
    struct17 *temp_v0 = func_1515F1B0();
    if (temp_v0 == NULL) {
        return 1;
    }

    func_1515F25C(&D_800DCDC4, temp_v0);
    D_800DCD90 += temp_v0->unk8;
    return 1;
}

s32 func_15015104(u8 *arg0) {
    struct {
        void *unk0;
        u8 unk4;
        u8 pad5[3];
        s32 unk8;
        u8 unkC;
        u8 padD[3];
        s32 unk10;
    } data;
    u8 *temp_v0;
    s32 flags;

    arg0[0x14] = 1;
    data.unk0 = arg0;
    data.unk4 = *(s32 *)(arg0 + 0x1C);
    func_1510F800(0);
    data.unk8 = func_1510FD20(*(s16 *)(arg0 + 0), *(s16 *)(arg0 + 4));

    flags = *(s32 *)(arg0 + 0x20) != 0;
    data.unkC = flags | (flags ? 2 : 0);
    data.unk10 = 0;

    temp_v0 = (u8 *)func_15149130(0x12C, -1, -1, -1, 0, 0x2C, (struct37 *)0x14, 0xFF, 0);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0x14);
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150151D4.s. */
s32 func_150151D4() {
    return 0;
}

s32 func_15015300(struct134 *arg0) {
    void (*func)(void);
    s32 idx = arg0->unk1C;

    if ((idx < 0) || (idx >= 2)) {
        return 1;
    }

    func = D_80082F70[idx];
    if (func != NULL) {
        func();
    }

    return 1;
}


/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_15015354.s. */
s32 func_15015354() {
    return 0;
}
s32 func_15015644(u8 *arg0) {
    struct {
        void *unk0;
        f32 unk4;
        s32 unk8;
        u8 unkC;
        u8 padD[3];
    } data;
    u8 *temp_v0;

    arg0[0x16] |= 4;
    arg0[0x14] = 1;
    data.unk0 = arg0;
    data.unk4 = func_15144598((struct134 *)arg0);
    func_1510F800(0);
    data.unk8 = func_1510FD20(*(s16 *)(arg0 + 0), *(s16 *)(arg0 + 4));
    data.unkC = 0;

    temp_v0 = (u8 *)func_15149130(0x12C, -1, 0x44, -1, 0, 0x2F, (struct37 *)0x10, 0xFF, 0);
    if (temp_v0 != NULL) {
        memcpy(temp_v0 + 0x28, &data, 0x10);
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_40490/func_150156F4.s. */
s32 func_150156F4() {
    return 0;
}
