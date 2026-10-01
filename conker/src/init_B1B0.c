
#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_1000B3D4(struct00 *arg0, struct151 *volatile arg1);
s32 func_1000B638(s32 arg0, u8 arg1, s32 arg2, s32 arg3);
s32 func_1000BCBC(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4);
s32 func_1000BF60();
s32 func_1000C350(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4);
s32 func_1000C7E8(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4);
s32 func_1000C934(s32 arg0, s32 arg1, s32 arg2, s32 arg3);
s32 func_1000CAE4(s32 arg0, s32 arg1, s32 arg2, s32 arg3);
s32 func_1000CDA0(u8 arg0, struct137 *arg1);
s32 func_1000CEAC(s32 arg0);
s32 func_1000D2F8(s32 arg0, f32 arg1, f32 arg2, s32 arg3);
s32 func_1000D96C(s32 arg0, s32 arg1, s32 arg2);
void func_1000E17C(void);
void func_1000E2F4(s32 arg0);
void func_1000E934(void);
/* Preserve the three independent retail address-materialization lifetimes. */
extern struct137 D_800419A8_pass2[12];
extern struct137 D_800419A8_pass3[12];
extern OSMesgQueue D_80041E58_pass1[3];
extern OSMesgQueue D_80041E58_pass2[3];
extern OSMesgQueue D_80041E58_pass3[3];
extern u8 D_800C35E8;
s32 func_15178EFC(s32 arg0);
s32 func_151F2CDC(void);
/* End generated placeholder declarations. */

struct151 *func_1000B1B0(s32 arg0) {
    s32 i;

    for(i = 0; i < 3; i++)
    {
        if ((D_800417B0[i] != 0) && (arg0 == D_800417B0[i]->unk4)) {
            return D_800417B0[i];
        }
    }

    return NULL;
}

struct151 *func_1000B1FC(s32 arg0) {
    s32 i;
    struct151 *child;

    for (i = 0; i < 3; i++) {
        if ((D_800417B0[i] != NULL) && (D_800417B0[i]->unk4 == arg0)) {
            return D_800417B0[i];
        }
    }

    for (i = 0; i < 3; i++) {
        if (D_800417B0[i] != NULL) {
            child = (struct151 *)D_800417B0[i]->unk60;
            if ((child != NULL) && (child->unk4 == arg0)) {
                return child;
            }
        }
    }

    return NULL;
}

void func_1000B294(s32 *arg0) {
    struct151 **ptr;
    struct151 *current;
    struct151 *child;

    current = *D_800417B0;
    ptr = D_800417B0;
    do {
        current = *ptr;
        if (current != NULL) {
            if (current->unk10 == arg0) {
                current->unk10 = (s32 *)current;
                current = *ptr;
            }

            child = (struct151 *)current->unk60;
            if ((child != NULL) && (child->unk10 == arg0)) {
                child->unk10 = (s32 *)child;
            }
        }
        ptr++;
    } while (ptr != (struct151 **)&D_800417BC);
}

struct137 *func_1000B2F4(s32 arg0) {
    s32 i;

    for (i = 0; i < 12; i++)
    {
        if (D_800419A8[i].unk4 == -1) {

            bzero(&D_800419A8[i], 100);

            D_800419A8[i].unk0 = -1;

            if (arg0 < 150) {
                D_800419A8[i].unk2C = D_8002B074[arg0].unk0; // (s32)(u16)
            } else {
                D_800419A8[i].unk2C = 26000;
            }
            D_800419A8[i].unk30 = D_800419A8[i].unk2C;
            D_800419A8[i].unk4E = D_800419A8[i].unk4C = D_800419A8[i].unk52 = D_800419A8[i].unk54 = D_800419A8[i].unk58 = D_800419A8[i].unk5A = 32768;
            D_800419A8[i].unk4 = arg0;
            D_800419A8[i].unk8 = &D_8002B9D4;
            D_800419A8[i].unkC = &D_8002B9F4;
            D_800419A8[i].unk10 = &D_800419A8[i];
            return &D_800419A8[i];
        }
    }
    return NULL;
}

void func_1000B3D4(struct00 *arg0, struct151 *volatile arg1) {
    s32 i;
    struct00 *child;
    struct151 *parent;
    struct151 **slot;
    struct151 *allocated;

    parent = arg1;
    allocated = NULL;
    i = 0;
    if (parent != NULL) {
        child = parent->unk60;
        if ((child != NULL) && (arg0 != child)) {
            if (arg0->unk4 == child->unk4) {
                arg0->unk4 = -1;
                return;
            }
            child->unk4 = -1;
        }
        arg1->unk60 = arg0;
        return;
    }

    do {
        if ((allocated == NULL) &&
            (((slot = &D_800417B0[i]), *slot == NULL) ||
             (((*slot)->unk4 <= 0) && ((*slot)->unk60 == NULL)))) {
            allocated = (struct151 *)func_1000B2F4(0);
            if (allocated != NULL) {
                allocated->unk0 = i;
                allocated->unk60 = arg0;
                *slot = allocated;
                goto next;
            } else {
                arg0->unk4 = -1;
                return;
            }
        }

        if (allocated == NULL) {
            slot = &D_800417B0[i];
            if ((*slot != NULL) && ((*slot)->unk60 != NULL) &&
                ((*slot)->unk60->unk4 == 0)) {
                allocated = (struct151 *)-1;
                func_1000B294(&(*slot)->unk60->unk0);
                (*slot)->unk60->unk4 = -1;
                (*slot)->unk60->unk0 = -1;
                (*slot)->unk60 = arg0;
            }
        }
next:
        i++;
    } while (i != 3);
}

s32 func_1000B548(s32 *arg0) {
    s32 ret = 0;
    s32 i;

    for (i = 0; i < 12; i += 4) {
        if ((D_800419A8[i].unk4 != -1) && (D_800419A8[i].unk0 != -1)) {
            if (ret < 3) {
                *arg0++ = D_800419A8[i].unk4;
                ret++;
            }
        }
        if ((D_800419A8[i + 1].unk4 != -1) && (D_800419A8[i + 1].unk0 != -1)) {
            if (ret < 3) {
                *arg0++ = D_800419A8[i + 1].unk4;
                ret++;
            }
        }
        if ((D_800419A8[i + 2].unk4 != -1) && (D_800419A8[i + 2].unk0 != -1)) {
            if (ret < 3) {
                *arg0++ = D_800419A8[i + 2].unk4;
                ret++;
            }
        }
        if ((D_800419A8[i + 3].unk4 != -1) && (D_800419A8[i + 3].unk0 != -1)) {
            if (ret < 3) {
                *arg0++ = D_800419A8[i + 3].unk4;
                ret++;
            }
        }
    }
    return ret;
}

s32 func_1000B638(s32 arg0, u8 arg1, s32 arg2, s32 arg3) {
    struct151 *entry;
    s32 pending;

    entry = D_800417B0[arg1];
    pending = arg0 & 2;
    arg0 &= 1;

    if ((entry == NULL) || (entry->unk30 < 500)) {
        D_80041F04 &= ~1;
    }

    if ((D_80041F04 & 1) != 0) {
        if (arg0 == 0) {
            func_100088F0(arg1, 0x8000, 1);
            if ((D_800BE9F0 == 1) || (D_800BE9F0 == 0xC)) {
                func_10008790(arg1, 0x7000, 0, 0);
            } else if (D_800BE9F0 != 7) {
                func_10008790(arg1, 0xCA, 0, 0);
            }
            func_100085B8(arg1, 0xF, 1);
        }
        arg0 = 1;
    } else {
        if (arg0 != 0) {
            func_100088F0(arg1, 0x8000, 0);
            if ((D_800BE9F0 == 1) || (D_800BE9F0 == 0xC)) {
                func_10008790(arg1, 0x7000, 0xFF, 0);
            } else if (D_800BE9F0 != 7) {
                func_10008790(arg1, 0xCA, 0xFF, 0);
            }
            func_100085B8(arg1, 0xF, 0);
            arg0 = 0;
        }
    }

    if (D_800BE9F0 == 0x27) {
        func_10011FA0((s32 *)4);
        if (pending == 0) {
            pending = 2;
            func_1000E704(1, 1, 0xFFFF);
        }
    } else if (pending != 0) {
        func_1000E704(1, 0, 0xFFFF);
        pending = 0;
    }

    return pending | arg0;
}


s32 func_1000B830(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 tmp = D_800DBFF0->unk5F0 & 1;
    if ((tmp != 0) && (arg0 == 0)) {
        arg0 = 1;
        func_1000E40C(16, 1000);
    } else if ((tmp == 0) && (arg0 != 0)) {
        arg0 = 0;
        func_1000E40C(16, 18000);
    }
    return arg0;
}

s32 func_1000B8B8(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    s32 tmp;

    if (D_800BE9F0 == 4) {
        if (((arg0 & 1) != 0) && (D_80041F0C == 0)) {
            func_1000E46C(19, 0, 4096, 0);
            arg0 = arg0 & ~1;
        } else {
            if (D_80041F0C != 0) {
                tmp = D_80041F08 / D_80041F0C / 80;
                if (tmp >= 101) {
                    tmp = 100;
                }
                func_1000E588(19, tmp, 4096);
                arg0 |= 1;
            }
        }
        D_80041F08 = 0;
        D_80041F0C = 0;
        if ((arg0 & 2) == 0) {
            func_1000DF68(19, 0, 1);
            func_1000DF68(19, 32768, 0);
            arg0 |= 2;
        }
        return arg0;
    }
    return func_1000C530(arg0, arg1, arg2, arg3, arg4);
}

s32 func_1000BA18(u32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    u32 sp44;
    s32 sp40;
    s32 sp3C;

    sp44 = 0;
    sp3C = arg0 & 0x00FFFFFF;
    arg0 = arg0 & 0xFF000000;
    func_100114D0(0, -377, 8227, 32767, 4000, 3000, &sp40, &sp44, 0);
    sp44 = (sp44 << 16) & 0xFF000000;
    if (arg0 != sp44) {
        arg0 = sp44;
        func_1000E588(0x4D, arg0 >> 24, 0x6000);
    }
    sp3C = func_1000C530(sp3C, arg1, arg2, arg3, arg4) & 0xFFFFFF;
    // fakematch
    sp44 = sp3C & 0xFFFFFFFFFFFFFFFF;
    return arg0 | sp44;
}

/* Non-matching C placeholders for asm/nonmatchings/init_B1B0/func_1000BAFC.s. */
s32 func_1000BAFC(u32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    u32 sp44;
    s32 sp40;
    s32 sp3C;

    sp44 = 0;
    sp3C = arg0 & 0x00FFFFFF;
    arg0 = arg0 & 0xFF000000;
    func_100114D0(0, 0, 0, 0x7FF8, 0xE74, 0xA28, &sp40, &sp44, 0);
    sp44 = ((0x7FFF - sp44) << 16) & 0xFF000000;
    if (arg0 != sp44) {
        arg0 = sp44;
        func_1000E588(0x93, arg0 >> 24, 0x6000);
    }
    sp3C = func_1000C530(sp3C, arg1, arg2, arg3, arg4) & 0xFFFFFF;
    sp44 = sp3C & 0xFFFFFFFFFFFFFFFF;
    return arg0 | sp44;
}

s32 func_1000BBE8(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    if (arg0 == 0) {
        func_1000E704(20, 1, 0xFFFF);
        arg0 = 1;
    }
    return arg0;
}

s32 func_1000BC28(s32 arg0, u8 arg1, s32 arg2, s32 arg3) {
    s32 tmp = func_10008A4C(arg1, 0) + func_10008A4C(arg1, 6) + 1;
    if (tmp >= 256) {
        tmp = 255;
    } else {
        if (tmp < 16) {
            tmp = 1;
        }
    }
    if (tmp != arg0) {
        func_150C851C(tmp - 1);
        arg0 = tmp;
    }
    return arg0;
}


s32 func_1000BCBC(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    f32 value;
    u8 level;

    if (arg0 == 0) {
        func_10008790(arg1, 3, 0x10, 0);
        func_1000886C(arg1, 4, 0);
        arg0 = 1;
    } else if (D_800BE9F0 == 0x13) {
        arg2 -= 24.0f;
        arg4 -= D_8002C220;
        value = (arg2 * arg2) + (arg4 * arg4);
        if (D_8002C224 < value) {
            level = 4;
        } else {
            level = (u8)((u32)((D_8002C228 - sqrtf(value)) * D_8002C22C) + 4);
        }

        if (arg0 != level) {
            func_1000886C(arg1, 3, level);
        }

        if (func_150A29C8(0, 0x4041) == 0) {
            if (D_8002C230 < arg3) {
                level = 0x20;
            } else {
                value = (D_8002C230 - arg3) * D_8002C234;
                if (223.0f <= value) {
                    level = 0xFF;
                } else {
                    level = (u8)((u32)value + 0x20);
                }
            }
        } else {
            level = 0;
        }

        if (level != func_10008A4C(arg1, 2)) {
            func_1000886C(arg1, 4, level);
        }
    }
    return arg0;
}
/* Non-matching C placeholders for asm/nonmatchings/init_B1B0/func_1000BF60.s. */
s32 func_1000BF60() {
    return 0;
}
s32 func_1000C350(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    if ((arg0 & 0x80) == 0) {
        arg0 |= 0x80;
        if (D_800C35EA != 1) {
            func_1000886C(arg1, 0x1E, 1);
            func_1000886C(arg1, 1, 1);
            func_1000E40C(0x23, 0x61A8);
        } else if (D_800C35E8 == 3) {
            func_1000E40C(0x23, 0xFA);
            func_15178EFC(2);
        } else if (D_800C35E8 == 6) {
            func_1000886C(arg1, 0x1E, 1);
            func_1000886C(arg1, 1, 0x40);
            func_15178EFC(2);
        } else {
            func_1000E40C(0x23, 0x61A8);
        }
        return arg0;
    }

    if (D_800BE9F0 != 0x1D) {
        func_10008F24(arg1);
        return arg0;
    }
    if (D_80041F08 != (arg0 & 0x7F)) {
        switch (D_80041F08) {
            case 1:
                func_10008790(arg1, 0x1E, 0, 0);
                func_10008790(arg1, 1, 0x40, 0);
                break;
            case 2:
                func_10008790(arg1, 0x18, 0xFF, 0);
                func_10008790(arg1, 6, 0, 0);
                func_10008790(arg1, 1, 1, 0);
                break;
        }
        arg0 = D_80041F08 | 0x80;
    }
    return arg0;
}
s32 func_1000C530(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    s32 oldState;
    s32 state;
    s32 timer;
    s32 oldValue;
    s32 value;
    s32 oldMode;
    s32 mode;
    u32 fade;
    u32 fadeStep;

    oldState = arg0 & 3;
    state = oldState;
    timer = ((u32)arg0 >> 2) & 0x3F;
    oldValue = ((u32)arg0 >> 8) & 0xFF;
    value = oldValue;
    oldMode = ((u32)arg0 >> 16) & 0xFF;
    mode = oldMode;
    fade = arg0 & 0xFF000000;

    if (D_80041F08 != 0) {
        if ((oldState != 2) || (timer == 0) || (D_80041F08 != 2)) {
            state = D_80041F08;
            value = D_80041F0C & 0xFF;
            mode = D_80041F0C >> 8;
            timer = 0x1E;
        }
    }

    if (timer != 0) {
        timer -= D_800BE9E4;
        if (timer <= 0) {
            timer = 0;
            state = 0;
        }
    }

    if (state != oldState) {
        if (oldState != 0) {
            func_100085F8(arg1, oldState + 9);
        }
        if (state != 0) {
            func_10008824(arg1, state + 9, value);
            func_100086FC(arg1, state + 9, mode >> 7);
            func_10008744(arg1, state + 9, mode & 0x7F);
        }
    } else if ((oldState != 0) && (D_80041F08 != 0) &&
               (((u32)arg0 >> 8) != D_80041F0C)) {
        if (oldValue != value) {
            func_10008824(arg1, oldState + 9, value);
        }
        if (oldMode != mode) {
            if (((oldMode ^ mode) & 0x80) != 0) {
                func_100086FC(arg1, state + 9, mode >> 7);
            }
            func_10008744(arg1, state + 9, mode & 0x7F);
        }
    }

    if ((D_80041F04 & 0x10) != 0) {
        D_80041F04 &= ~0x10;
        if (fade == 0) {
            func_1000886C(arg1, 0xC0, 0x80);
        }
        fade = 0xFF000000;
    }

    if (fade != 0) {
        fadeStep = (D_800BE9E4 << 23) & 0xFF000000;
        if (fadeStep < fade) {
            fade -= fadeStep;
        } else {
            func_10008790(arg1, 0xC0, 0, 0x5A);
            fade = 0;
        }
    }

    D_80041F08 = 0;
    return (timer << 2) | state | (value << 8) | (mode << 16) | fade;
}
s32 func_1000C7E8(s32 arg0, u8 arg1, f32 arg2, f32 arg3, f32 arg4) {
    f32 offset = arg2;
    f32 value;
    f32 clamped;

    if (D_800BE9F0 == 0x31) {
        if (arg0 != 2) {
            if (func_1000B1B0(9) == NULL) {
                func_1000E704(0x3E, 0, 0xFFFF);
                func_1000E40C(0x3E, 0x7FFF);
                func_1000D96C(0x3D, 0x3E, 4);
            }
            return 2;
        }
        return 0;
    }

    if (D_8002B070 == 0) {
        D_8002B070 = 1;
    }
    if (arg0 != D_8002B070) {
        arg0 = D_8002B070;
    }

    offset -= -4000.0f;
    value = D_8002C238 - sqrtf((offset * offset) + (arg4 * arg4)) * 10.0f;
    clamped = value;
    if (value < 100.0f) {
        clamped = 100.0f;
    } else if (D_8002C238 < value) {
        clamped = D_8002C238;
    }
    func_1000E40C(0x3E, clamped);
    return arg0;
}

s32 func_1000C934(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 value;
    s32 limit;
    s32 enabled;

    value = 0;
    enabled = D_800DBFF0->unk5F0 & 1;
    if (enabled != 0) {
        limit = 0x7FFF;
    } else {
        limit = 12000;
    }

    if ((D_800BE9F0 == 0x37) && (enabled == 0)) {
        func_100114D0(2200, 1066, -1600, limit, 3000, 1500, 0, &value, 0);
        value = limit - (value & 0xFF00);
    }

    if ((value != arg0) & 0xFFFF) {
        func_1000E40C(84, value);
    }
    return value | 0x80000000;
}

s32 func_1000CA18(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 tmp;

    if (D_800BE9F0 == 55) {
        if ((D_800DBFF0->unk5F0 & 1) != 0) {
            tmp = 0;
        } else {
            func_100114D0(2200, 1066, -1600, 24000, 3000, 1500, 0, &tmp, 0);
            tmp &= 0xFF00;
        }
    } else {
        tmp = 24000;
    }

    if ((tmp != arg0) & 0xFFFF) {
        func_1000E40C(84, tmp);
    }
    return tmp | 0x80000000;
}

s32 func_1000CAE4(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 pending;

    pending = arg0 & 2;
    arg0 &= 1;
    if (D_800BE9F0 == 0x42) {
        func_10011FA0((s32 *)4);
        if (arg0 == 0) {
            arg0 = 1;
            func_1000E704(0x58, 1, 0xFFFF);
        }
    } else if (arg0 != 0) {
        func_1000E704(0x58, 0, 0xFFFF);
        func_1000E40C(0x58, 16000);
        arg0 = 0;
    }

    if (pending == 0) {
        func_10008790(arg1, 0x1000, 0, 1);
        pending = 2;
    }
    return pending | arg0;
}

void func_1000CBA8(s32 arg0) {
    if (D_800417B0[0] != NULL) {
        D_800417B0[0]->unk4E = arg0;
        D_800417B0[0]->unk50 = (u16)0x500;
    }
    if (D_800417B0[1] != NULL) {
        D_800417B0[1]->unk4E = arg0;
        D_800417B0[1]->unk50 = (u16)0x500;
    }
}

void func_1000CBF0(s32 arg0, s32 arg1, s32 arg2) {
    s32 i;

    for (i = 0; i < 3; i++) {
        if (((1 << i) & arg2) != 0) {
            if (D_800417B0[i] != NULL) {
                D_800417B0[i]->unk5A = arg0;
                D_800417B0[i]->unk5C = arg1;
                if (arg1 == 0) {
                    D_800417B0[i]->unk58 = arg0;
                }
            }
        }
    }
}

// #pragma GLOBAL_ASM("asm/nonmatchings/init_B1B0/func_1000CC54.s")
void func_1000CC54(s32 arg0) {
    s32 phi_a3;
    struct151 *temp_v0;

    temp_v0 = D_800417B0[arg0];
    if (temp_v0 != 0) {
        phi_a3 = (((u32) (temp_v0->unk58 * ((u32) (temp_v0->unk4C * temp_v0->unk52) >> 0xF)) >> 0xF) * temp_v0->unk2C) >> 0xF;
        if (phi_a3 != temp_v0->unk30) {
            if (temp_v0->unk30 == 0) {
                func_10008988(arg0, temp_v0->unk38 ^ 0xFFFF, 1);
            } else {
                if (phi_a3 == 0) {
                    func_10008988(arg0, temp_v0->unk38 ^ 0xFFFF, 0);
                }
            }
            temp_v0->unk30 = phi_a3;
            func_10008EE0(arg0, phi_a3);
        }
    }
}

s32 func_1000CD40(s32 arg0, s32 arg1, s32 arg2) {
    if (arg1 != arg0) {
        arg2 = arg2 * D_800BE9E4;
        if (arg0 < arg1) {
            arg0 = arg0 + arg2;
            if (arg1 < arg0) {
                arg0 = arg1;
            }
        } else {
            arg0 = arg0 - arg2;
            if ((arg0 < arg1) || (arg0 < 0)) {
                arg0 = arg1;
            }
        }
    }
    return arg0;
}

s32 func_1000CDA0(u8 arg0, struct137 *arg1) {
    s32 index;

    if (arg0 == 0) {
        return 1;
    }
    if (arg1 != NULL) {
        index = arg1->unk0;
        if (index >= 0) {
            if ((D_800417B0[index] == NULL) || (arg1->unk4 <= 0)) {
                return 1;
            }
            if (func_1000853C(index & 0xFF) == 3) {
                return 1;
            }
            if ((D_8002B078[arg1->unk4][0] & 0x20) == 0) {
                D_800418AC[arg1->unk0] |= 3;
            }
            arg0 &= ~D_800418AC[arg1->unk0];
            arg0 &= 0xFF;
            return arg0 == 0;
        }
        return 1;
    }
    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/init_B1B0/func_1000CEAC.s. */
s32 func_1000CEAC(s32 arg0) {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/init_B1B0/func_1000D2F8.s. */
s32 func_1000D2F8(s32 arg0, f32 arg1, f32 arg2, s32 arg3) {
    return 0;
}
void func_1000D758(f32 arg0, f32 arg1, s32 arg2) {
    struct151 *entry;
    s32 group5;
    s32 flagged;
    s32 group34;
    s32 group12;
    s32 type;
    s32 i;
    s32 level;

    group5 = 0;
    flagged = 0;
    group34 = 0;
    group12 = 0;
    if (D_80041F00 != 0) {
        return;
    }

    for (i = 0; i < 3; i++) {
        entry = D_800417B0[i];
        if ((entry != NULL) && (entry->unk4 > 0)) {
            type = *(s32 *)&D_8002B074[entry->unk4].unk4;
            if ((type & 0x40) != 0) {
                flagged |= 1 << i;
            }
            type &= ~0xF0;
            if (type == 5) {
                group5 |= 1 << i;
            } else if ((type == 4) || (type == 3)) {
                group34 |= 1 << i;
            } else if ((type == 1) || (type == 2)) {
                group12 |= 1 << i;
            }
        }
    }

    if (group5 != 0) {
        func_1000CBF0(0x1770, 0x400, (group5 ^ 0xFF) ^ flagged);
        func_1000CBF0(0x8000, 0x6400, group5);
    } else if (group34 != 0) {
        func_1000CBF0(0x1F4, 0x400, group34 ^ 0xFF);
        func_1000CBF0(0x8000, 0x800, group34);
    } else {
        if (func_151F2CDC() != 1) {
            goto default_mix;
        }
        level = (u16)D_800427F4;
        if (((level < 0x7D) || (level >= 0x81)) && (level < 0x1C9) &&
            (level != 0x170) && (level != 0x171)) {
            func_1000CBF0(0x36B0, 0x200, group12 ^ 0xFF);
            goto update_channels;
        }
default_mix:
        func_1000CBF0(0x8000, 0x800, 0xFF);
    }

update_channels:
    for (i = 0; i < 3; i++) {
        func_1000CEAC(i);
    }
    for (i = 0; i < 3; i++) {
        func_1000D2F8(i, arg0, arg1, arg2);
    }
}
/* Non-matching C placeholders for asm/nonmatchings/init_B1B0/func_1000D96C.s. */
s32 func_1000D96C(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}
void func_1000DEC4(void);

// Matched with guarded local-array placement normalization.
void func_1000DE1C(s32 arg0, s32 arg1) {
    s32 ids[3];
    s32 count;
    s32 i;

    arg0 &= 0xFFF;
    if (arg0 == 0) {
        func_1000DEC4();
        count = func_1000B548(ids);
        for (i = 0; i < count; i++) {
            if (ids[i] > 0) {
                func_1000D96C(0, ids[i], arg1);
            }
        }
    } else {
        func_1000D96C(0, arg0, arg1);
    }
}

void func_1000DEC4(void) {
    s32 i;

    for (i = 0; i < 12; i++) {
        if (D_800419A8[i].unk0 == -1) {
            if (D_800419A8[i].unk4 != -1) {
                D_800419A8[i].unk4 = -1;
            }
        } else if (func_1000853C(D_800419A8[i].unk0 & 0xFF) == 0) {
            D_800417B0[D_800419A8[i].unk0] = NULL;
            D_800419A8[i].unk0 = -1;
            D_800419A8[i].unk4 = -1;
        }

        *(s32 *)&D_800419A8[i].pad60 = 0;
    }
}

void func_1000DF68(s32 arg0, s32 arg1, s32 arg2) {
    struct151 *entry;
    s32 step;

    entry = func_1000B1FC(arg0);
    if (entry != NULL) {
        entry->unk4E = arg1;
        if (arg2 == 1) {
            entry->unk4C = arg1;
            if (entry->unk0 >= 0) {
                func_1000CC54(entry->unk0);
            }
        }

        if (arg2 >= 2) {
            step = entry->unk4C - arg1;
            if (step < 0) {
                step = -step;
            }
            step /= arg2;
            if (step <= 0) {
                step = 2;
            } else if (step >= 0x8000) {
                step = 0x7FFF;
            }
            entry->unk50 = step;
        } else {
            entry->unk50 = 0x200;
        }
    }
}

void func_1000E054(s32 arg0, s32 arg1) {
    struct151 *sp1C;

    sp1C = func_1000B1B0(arg0);
    if (sp1C != 0) {
        if ((2 == sp1C->unk15) && (arg1 == 0)) {
            func_100084D8(sp1C->unk0);
            sp1C->unk15 = 0;
            sp1C->unk30 = -1;
            func_1000CC54(sp1C->unk0);
            return;
        }
        if ((2 != sp1C->unk15) && (arg1 != 0)) {
            if (sp1C->unk15 != 1) {
                func_10008F58(sp1C->unk0);
            }
            sp1C->unk15 = 2;
        }
    }
}

s32 func_1000E0F8(s32 arg0) {
    struct151 *tmp;

    arg0 &= 0xFFF;
    tmp = func_1000B1FC(arg0);

    if (tmp && tmp->unk60 == 0) {
        return 1;
    } else {
        return 0;
    }
}

s32 func_1000E134(s32 arg0) {
    s32 tmp;

    if (arg0 < 150) {
        tmp = D_8002B078[arg0][0] & ~0xF0;
        if ((tmp == 1) || (tmp == 3)) {
            return 1;
        }
    }
    return 0;
}

void func_1000E17C(void) {
    struct137 *entry;
    struct137 *linked;
    s32 type;

    entry = D_800419A8;
    do {
        if (entry->unk4 > 0) {
            type = *(s32 *)&D_8002B074[entry->unk4].unk4 & ~0xF0;
            if (((type == 1) || (type == 3)) && (entry->unk0 == -1)) {
                entry->unk4 = -1;
            }
        }
        entry++;
    } while (entry < (struct137 *)D_80041E58_pass1);

    entry = D_800419A8_pass2;
    do {
        if (entry->unk4 > 0) {
            linked = *(struct137 **)&entry->pad60;
            if ((linked != NULL) && (linked->unk4 == -1)) {
                *(struct137 **)&entry->pad60 = NULL;
            }

            linked = entry->unk10;
            if ((linked != NULL) && (linked->unk4 == -1)) {
                entry->unk10 = NULL;
            }
        }
        entry++;
    } while (entry < (struct137 *)D_80041E58_pass2);

    entry = D_800419A8_pass3;
    do {
        if (entry->unk4 > 0) {
            type = *(s32 *)&D_8002B074[entry->unk4].unk4 & ~0xF0;
            if (((type == 1) || (type == 3)) && (entry->unk0 != -1)) {
                func_1000DE1C(entry->unk4, 4);
            }
        }
        entry++;
    } while (entry != (struct137 *)D_80041E58_pass3);
}
void func_1000E2F4(s32 arg0) {
    struct151 *entry;
    s32 i;

    for (i = 0; i < 3; i++) {
        entry = D_800417B0[i];
        if ((entry != NULL) && (entry->unk4 > 0) && (entry->unk15 == 0)) {
            if (arg0 != 0) {
                func_10008EE0(i, 0);
                entry = D_800417B0[i];
                if ((*(u32 *)&D_8002B074[entry->unk4].unk4 & 0x10) == 0) {
                    func_10008F58(i);
                }
            } else {
                if ((*(u32 *)&D_8002B074[entry->unk4].unk4 & 0x10) == 0) {
                    func_100084D8(i);
                    entry = D_800417B0[i];
                }
                entry->unk30 = -1;
                func_1000CC54(i);
            }
        }
    }
    D_80041F00 = arg0;
}

void func_1000E40C(s32 arg0, s32 arg1) {
    struct151 *temp_v0;

    if (arg1 >= 0x8000) {
        arg1 = 0x7FFF;
    } else if (arg1 < 0) {
        arg1 = 0;
    }
    temp_v0 = func_1000B1FC(arg0);
    if (temp_v0 != NULL) {
        if (temp_v0->unk0 < 0) {
            temp_v0->unk30 = arg1;
        }
        temp_v0->unk2C = arg1;
    }
}

s32 func_1000E46C(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct151 *entry;
    s32 i;

    entry = func_1000B1FC(arg0);
    arg1 = (arg1 * 0xFF) / 100;
    if (arg1 >= 0x100) {
        arg1 = 0xFF;
    } else if (arg1 < 0) {
        arg1 = 0;
    }

    if (entry != NULL) {
        if (entry->unk0 >= 0) {
            if (arg3 < 0) {
                func_1000886C((u8)entry->unk0, arg2, (u8)arg1);
            } else {
                func_10008790((u8)entry->unk0, arg2, (u8)arg1, arg3);
            }
            return 1;
        }

        if (arg1 == 0) {
            entry->unk38 |= arg2;
        } else if (arg1 > 0) {
            entry->unk38 &= ~arg2;
        }

        i = 0;
        while (arg2 != 0) {
            if (arg2 & 1) {
                entry->unk3C[i] = arg1;
            }
            i++;
            arg2 >>= 1;
        }
        return 1;
    }
    return 0;
}
s32 func_1000E588(s32 arg0, s32 arg1, s32 arg2) {
    struct151 *entry;
    u8 value;

    entry = func_1000B1FC(arg0);
    if (entry != NULL) {
        if (entry->unk0 >= 0) {
            if (arg1 >= 101) {
                arg1 = 100;
            } else if (arg1 < 0) {
                arg1 = 0;
            }
            value = (arg1 * 0xFF) / 100;
            func_1000886C((u8)entry->unk0, arg2, value);
            return 1;
        }
        if (arg1 <= 0) {
            entry->unk38 |= arg2;
            return 1;
        }
        if (arg1 > 0) {
            entry->unk38 &= ~arg2;
            return 1;
        }
    }
    return 0;
}

s32 func_1000E654(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct151 *sp1C;
    struct151 *phi_a0;

    sp1C = func_1000B1FC(arg0);
    phi_a0 = NULL;
    if (arg3 >= 0) {
        phi_a0 = func_1000B1FC(arg3);
    }

    if (sp1C != NULL) {
        if (arg2 == 0) {
            if (sp1C->unk0 >= 0) {
                func_10008C6C(sp1C->unk0, arg1 - 1);
                return 1;
            }
        }
        sp1C->unk24 = arg1;
        sp1C->unk20 = arg2;
        if (phi_a0 != NULL) {
            sp1C->unk10 = phi_a0;
        }
        return 1;
    }
    return 0;
}

s32 func_1000E704(s32 arg0, s32 arg1, s32 arg2) {
    struct151 *tmp = func_1000B1B0(arg0);
    if (tmp && tmp->unk0 >= 0) {
        func_10008A94(tmp->unk0, arg2, arg1);
        return 1;
    }
    return 0;
}

void func_1000E75C(s32 arg0) {
    D_8002B070 = arg0 >> 1;
}

s32 func_1000E770(s32 *arg0, s32 *arg1) {
    if (arg0 != 0) {
        *arg0 = D_80041F08;
    }
    if (arg1 != 0) {
        *arg1 = D_80041F0C;
    }
    return D_80041F04;
}

/* Non-matching C placeholders for asm/nonmatchings/init_B1B0/func_1000E7A0.s. */
void func_1000E7A0(u32 arg0, s32 arg1) {
    if ((arg0 & 1) == 1) {
        D_80041F04 |= 1;
    } else if (arg0 & 2) {
        D_80041F08 += arg1;
        D_80041F0C += 1;
    } else if (arg0 & 4) {
        D_80041F08 = arg1 + 1;
        D_80041F04 |= 4;
    } else if (arg0 & 8) {
        D_80041F0C = arg1 >> 8;
        arg1 &= 0xFF;
        if ((arg1 == 0) || (arg1 == 4) || (arg1 == 5)) {
            D_80041F08 = 2;
        } else if (arg1 == 10) {
            D_80041F08 = 1;
        } else {
            D_80041F08 = 3;
        }
    } else if (arg0 & 0x10) {
        D_80041F04 |= 0x10;
    }
}
// NON-MATCHING: mostly just wrong registers
// void func_1000E7A0(u32 arg0, s32 arg1) {
//     if ((arg0 & 1) == 1) {
//         D_80041F04 |= 1;
//     } else if (arg0 & 2) {
//         D_80041F08 += arg1;
//         D_80041F0C += 1;
//     } else if (arg0 & 4) {
//         D_80041F08 = 1 + arg1;
//         D_80041F04 |= 4;
//     } else if (arg0 & 8) {
//         D_80041F0C = (arg1 >> 8) & 0xff;
//         if ((D_80041F0C == 0) || (D_80041F0C == 4) || (D_80041F0C == 5))  {
//             D_80041F08 = 2;
//         } else if (D_80041F0C == 10) {
//             D_80041F08 = 1;
//         } else {
//             D_80041F08 = 3;
//         }
//     } else if (arg0 & 16) {
//         D_80041F04 |= 16;
//     }
// }

void func_1000E8C4(s32 arg0) {
    if ((arg0 & 1) == 1) {
        D_80041F04 &= -2; // truncate odd to even
    }
}

u8 func_1000E8F0(s32 arg0) {
    struct151 *temp_v0 = func_1000B1B0(arg0);
    if ((temp_v0 != 0) && (temp_v0->unk0 >= 0)) {
        return D_800418AC[temp_v0->unk0];
    } else {
        return 0;
    }
}

void func_1000E934(void) {
    u32 channel;
    s32 slot;
    s32 value8000;
    s32 value100;
    s32 bound;
    s32 record;
    s32 *table8000;
    s32 *table100;
    struct151 **roots;
    s32 *stateA0;
    s32 *state90;
    s32 *state80;
    s32 *cursor8000;
    s32 *cursor100;

    value8000 = 0x8000;
    value100 = 0x100;
    bound = 16;
    table8000 = D_800418B0;
    table100 = D_800417C0;
    roots = D_800417B0;
    stateA0 = D_800418A0;
    state90 = D_80041890;
    state80 = D_80041880;

    channel = 0;
    do {
        slot = 0;
        cursor8000 = table8000;
        cursor100 = table100;
        do {
            slot += 4;
            cursor8000[1] = value8000;
            cursor100[1] = value100;
            cursor8000[2] = value8000;
            cursor100[2] = value100;
            cursor8000[3] = value8000;
            cursor100[3] = value100;
            cursor8000 += 4;
            cursor100 += 4;
            cursor8000[-4] = value8000;
            cursor100[-4] = value100;
        } while (slot != bound);

        func_10008F24(channel);
        channel++;
        table8000 += 16;
        table100 += 16;
        roots++;
        stateA0++;
        state90++;
        state80++;
        roots[-1] = NULL;
        stateA0[-1] = 0;
        state90[-1] = 0;
        state80[-1] = 0;
    } while (channel < 3);

    bzero(D_800419A8, sizeof(D_800419A8));
    D_800419A0 = 0;

    record = 0;
    do {
        record += 4;
        D_800419A8[record - 3].unk4 = -1;
        D_800419A8[record - 2].unk4 = -1;
        D_800419A8[record - 1].unk4 = -1;
        D_800419A8[record - 4].unk4 = -1;
    } while ((struct137 *)D_80041E58 != &D_800419A8[record]);
}

u16 func_1000EA94(s32 arg0) {
    u16 tmp;

    if (arg0 == 0) {
        tmp = 82;
    } else if (arg0 == 2) {
        tmp = 81;
    } else if (arg0 == 1) {
        tmp = 83;
    }
    func_1000D96C(tmp, 0, 0);
    return tmp;
}
