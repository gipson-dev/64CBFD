#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1000ECCC();
s32 func_1000EFB4(struct57 *arg0, s32 arg1, s32 *arg2, struct11 *arg3,
                  s32 arg4, s32 *arg5, u16 *arg6);
s32 func_1000F568(s32 arg0, u32 arg1);
s32 func_1000F6B8(s32 arg0, s16 arg1, s16 arg2, s16 arg3, void *arg4, s16 arg5, s16 arg6);
struct31 *func_10017438(void *bank, s16 soundNum, u16 vol, u8 pan, f32 pitch,
                       u8 fxmix, u8 fxbus, struct31 **handle);
void func_10011310(void);
s32 func_10011624(struct15 *arg0, s32 *arg1, s32 arg2, s32 arg3);
void func_10011BB8(void);
u16 func_10011EB8(s32 arg0, s16 *arg1, s32 arg2);
/* End generated placeholder declarations. */

s32 func_1000EB00(struct04 *arg0, s32 arg1, s32 *arg2, s32 *arg3, s32 arg6, s32 arg7, u16 *arg8) {
    if (arg0->unk24 != 0) {
        arg0->unk24 = 0;
    }
    *arg3 = 64;
    if (D_800CC37D || (*arg2 == 0)) {
        *arg2 = 0;
        *arg8 = 0;
        return 0;
    }
    arg0->unk18 -= D_800BE9E4;
    if (arg0->unk18 > 0) {
        *arg2 = 0;
        *arg8 = 0;
    } else {
        arg0->unk18 = (func_150ADA20() & 0x7F) + 0x80;
        arg0->unk0 = (func_150ADA20() % 3U) + 0x6C;
    }
    return 0;
}

s32 func_1000EBC4(struct00 *arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 temp_v0 = arg0->unkC;
    s32 temp_v1 = arg0->unk18;
    temp_v1 -= D_800BE9E4;

    if (temp_v1 <= 0) {
        temp_v0 = temp_v0 - D_800BE9E4 * 1000;
        if (temp_v0 < 0) {
            return 1;
        }
        arg0->unkC = temp_v0;
    }
    arg0->unk18 = temp_v1;
    return 0;
}

s32 func_1000EC24(struct251 *arg0, s32 arg1, s32 *arg2, struct11 *arg3, struct04 *arg4, s32 *arg5, u16 *arg6) {
    s16 temp_v1 = arg0->unk18.h[1];

    if (*arg6 != 0) {
        arg0->unk1C = *arg6;
        arg0->unk0 = 0;
        *arg6 = 0;
    }

    temp_v1 -= D_800BE9E4;

    if (temp_v1 <= 0) {
        if (*arg2 != 0) {
            func_10010F30(arg0->unk1C, *arg2, arg3->unk3, arg4->unk2, *arg5);
        }
        return 1;
    }
    arg0->unk18.w = temp_v1;
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/init_EB00/func_1000ECCC.s. */
s32 func_1000ECCC(struct251 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, u16 *arg6) {
    s16 temp_a1;
    s32 temp_v1;
    unsigned long temp_v0;
    s16 temp_t4;

    temp_v1 = arg0->unk18.w;
    temp_v0 = *arg6;
    temp_a1 = temp_v1;
    if (temp_v0 != 0) {
        (0, arg0)->unk18.w = ((0, temp_v0) << 0x10) | (temp_v1 & 0xFFFF);
        (0, arg0)->unk0 = 0;
        *arg6 = 0;
        temp_v1 = arg0->unk18.w;
    }
    temp_a1 -= D_800BE9E4;
    if ((0, temp_a1) <= 0) {
        temp_t4 = temp_v1 >> 0x10;
        *arg6 = (0, temp_t4);
        arg0->unk0 = (0, temp_t4);
        if (func_10010894((0, arg0)->unk1C) == 0) {
            func_10010344(*arg6, (0, arg0)->unk1C, *(s32 *)((s32)(0, arg0) + 0xC), *(s16 *)((0, (s32)(0, arg0)) + 0xA), *(u16 *)((s32)(0, arg0) + 8));
        }
        return 1;
    }
    arg0->unk18.w = (temp_v1 & 0xFFFF0000) | temp_a1;
    return 0;
}
// ? func_1000ECCC(void *arg0, ? arg1, ? arg2, ? arg3, void *arg6) {
//     s16 temp_a1;
//     s32 temp_t4;
//     s32 temp_v1;
//     u16 temp_v0;
//
//     temp_v1 = arg0->unk18;
//     temp_v0 = *arg6;
//     if (temp_v0 != 0) {
//         arg0->unk18 = (s32) ((temp_v0 << 0x10) | (temp_v1 & 0xFFFF));
//         arg0->unk0 = (u16)0;
//         *arg6 = (u16)0U;
//     }
//     temp_a1 = (s16) temp_v1 - *(void *)0x800BE9E4;
//     if ((s32) temp_a1 <= 0) {
//         temp_t4 = arg0->unk18 >> 0x10;
//         *arg6 = (u16) temp_t4;
//         arg0->unk0 = (s16) temp_t4;
//         if (func_10010894(arg0->unk1C, temp_a1, arg6) == 0) {
//             func_10010344(*arg6, arg0->unk1C, arg0->unkC, arg0->unkA, (?32) arg0->unk8);
//         }
//         return 1;
//     }
//     arg0->unk18 = (s32) ((arg0->unk18 & 0xFFFF0000) | temp_a1);
//     return 0;
// }

s32 func_1000EDA0(struct15 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, u16 *arg6) {
    s16 timer;
    s32 packed;

    packed = arg0->unk18;
    timer = packed;
    if (*arg6 != 0) {
        arg0->unk18 = (*arg6 << 16) | (packed & 0xFFFF);
        *(s16 *)arg0 = 0;
        *arg6 = 0;
        packed = arg0->unk18;
    }

    timer -= D_800BE9E4;
    if (timer <= 0) {
        *arg6 = packed >> 16;
        *(s16 *)arg0 = packed >> 16;
        func_10010630(*arg6, (struct127 *)arg0->unk1C, arg0->unkC,
                      *(s16 *)((u8 *)arg0 + 0xA), *(u16 *)((u8 *)arg0 + 8));
        return 1;
    }
    arg0->unk18 = (packed & 0xFFFF0000) | timer;
    return 0;
}
s32 func_1000EE70(struct15 *arg0, s32 arg1, s32 *arg2, s32 arg3, s32 arg4, s32 *arg5) {
    struct127 *actor;
    s32 key;

    actor = (struct127 *)arg0->unk18;
    if (actor == NULL) {
        goto return_one;
    }
    if (*arg2 == 0) {
        goto return_one;
    }

    key = arg0->unk1C & 0xFF;
    if ((actor->interaction_state != 0) &&
        (actor->unique_id == key)) {
        *arg5 = (((u32)actor->unk184 >> 3) & 0x30) << 1;
        *(s16 *)((u8 *)arg0 + 2) = actor->x_position;
        *(s16 *)((u8 *)arg0 + 4) = actor->y_position;
        *(s16 *)((u8 *)arg0 + 6) = actor->z_position;
        return 0;
    }
    if (func_1000F44C(arg0->unk24) != 0) {
        goto return_one;
    }
    return 0;

return_one:
    return 1;
}

s32 func_1000EF40(struct57 *arg0, struct57 *arg1, s32 *arg2, s32 arg3, s32 arg4, s32 arg5, u16 *arg6) {
    if (arg0->unk10 & 0x80) {
        arg0->unk10 = (s32) (arg0->unk10 & -0x81);
    }
    if (*arg2 == 0) {
        if (arg0->unk24 != 0) {
            func_100111C8(arg0->unk24);
            arg0->unk24 = 0;
        }
        *arg6 = 0;
    }
    return 0;
}

s32 func_1000EFB4(struct57 *arg0, s32 arg1, s32 *arg2, struct11 *arg3,
                  s32 arg4, s32 *arg5, u16 *arg6) {
    struct127 *actor;
    u16 *id;

    actor = (struct127 *)arg0->unk18;
    if (actor == NULL) {
        goto return_one;
    }
    if (*arg2 == 0) {
        goto return_one;
    }

    if (actor->interaction_state != 0) {
        id = (u16 *)arg0->unk1C;
        while (*id != 0) {
            if ((actor->unk84.uh == *id) || ((arg0->unk10 & 1) == 0)) {
                *arg5 = (((u32)actor->unk184 >> 3) & 0x30) << 1;
                *(s16 *)((u8 *)arg0 + 2) = actor->x_position;
                *(s16 *)((u8 *)arg0 + 4) = actor->y_position;
                *(s16 *)((u8 *)arg0 + 6) = actor->z_position;
                return 0;
            }
            id++;
        }
    }

    if (*arg6 == 0xCA) {
        func_10010F30(0xCB, *arg2, arg3->unk3, 0, *arg5);
    } else if (*arg6 == 0x2CF) {
        func_10010F30(0x2D7, *arg2, arg3->unk3, 0, *arg5);
        func_10010F30((func_150ADA20() % 3U) + 0x2EB, 0x3E80,
                      arg3->unk3, 0, *arg5);
    } else if (*arg6 == 0x2D2) {
        func_10010F30(0x2DA, *arg2, arg3->unk3, 0, *arg5);
        func_10010F30((func_150ADA20() % 3U) + 0x2EB, 0x3E80,
                      arg3->unk3, 0, *arg5);
    }

return_one:
    return 1;
}

void func_1000F1A8(void) {
    s32 i;

    D_80042760 = 0;
    D_80041FD9 = 1;
    D_80041FD8 = 0;

    bzero(D_800425E0, 0x180);

    for (i = 0; i < 16; i++) {
        D_800425E0[i].unk2 = i + 0x10;
    }

    D_80041F50 = 0;
    func_100176EC();
    D_80041F60 = D_80041F61 = 0;
}

void func_10017780(u8 arg0, u16 arg1);
s32* allocate_memory(s32, s32, s32, s32);
void func_1000F248(s32 arg0) {
    u16 tmp;

    func_1000F1A8();
    if (arg0 == 4) {
        D_80041F54 = 0;
        D_80041F58 = D_8002C3F8; // 0.009999999776482582
    } else {
        D_80041F54 = 23000;
        D_80041F58 = D_8002C3FC; // 0.10000000149011612
    }

    if (arg0 == 0x35) {
        D_80041FD9 = 0;
    } else if (arg0 == 0x36) {
        D_80041FD9 = 0;
    } else if (arg0 == 0x3C) {
        D_80041FD9 = 0;
        D_80041FD8 = 0x3C;
    } else if (arg0 == 0x27) {
        D_80041FD9 = 0;
        D_80041FD8 = 0x28;
    } else if ((arg0 == 0x3A) || (arg0 == 0x40)) {
        D_80041FD9 = 0;
        D_80041FD8 = 0x3C;
    }

    D_80041F5C = allocate_memory(1762, 1, 0, 0);

    bzero(D_80041F5C, 1762);

    if (arg0 == 0x31) {
        D_80041FDC = 14000;
    } else {
        D_80041FDC = 23000;
    }
    func_10011E88(arg0);
    D_80041F60 = D_80041F61 = 0;
    func_10017780(0, D_80041F56);
    func_10017780(1, D_80041F56);
    func_10017780(2, 23000);
    // fakematch
    if (arg0) {}
}

s32 func_1000F3D0(u16 arg0) {
    struct120 *temp_v1;

    temp_v1 = &D_800425E0[arg0 & 0xF];
    if (temp_v1->unk8 != 0) {
        if ((temp_v1->unk0 == arg0) || (arg0 == (arg0 & 0xF))) {
            if (func_100173C4(&temp_v1->unk8) != 0) {
                return 1;
            }
        }
    }
    return 0;
}

s32 func_1000F44C(u16 arg0) {
    u32 mask;
    struct120 *temp_a1;
    struct31 *temp_a2;

    mask = __osDisableInt();
    temp_a1 = &D_800425E0[arg0 & 0xF];
    temp_a2 = temp_a1->unk8;
    if ((temp_a2 != 0) && (temp_a1->unk0 == arg0) && ((temp_a2->unk53 & 2) != 0)) {
        __osRestoreInt(mask);
        return 1;
    }
    __osRestoreInt(mask);
    return 0;
}

s32 func_1000F4D8(u16 arg0) {
    s32 i;
    struct120 *current;

    arg0 &= 0x7FFF;

    for (i = 0; i < 16; i++) {
        current = &D_800425E0[i];
        if ((current->unk8 != 0) && ((current->unk4 & 0x7FFF) == arg0)) {
            if (func_100173C4(&current->unk8) != 0) {
                return 1;
            }
        }
    }

    return 0;
}
s32 func_1000F568(s32 arg0, u32 arg1) {
    s32 choices;
    u32 random;
    u32 selected;
    u8 *state;
    u32 raw;
    u32 updated;
    u32 available;

    random = func_150ADA20() % arg1;
    selected = random;
    if (arg0 >= 0x6E2) {
        return 1;
    }
    if ((s32)arg1 < 2) {
        return arg0;
    }

    state = (u8 *)D_80041F5C + arg0;
    if (D_80041F5C != NULL) {
        raw = *state;
        if ((s32)arg1 < 8) {
            available = raw;
            if (((raw & 0x80) == 0) ||
                ((choices = (1 << arg1) - 1, (raw & choices) == 0))) {
                choices = (1 << arg1) - 1;
                raw = available = 0xFF;
            }
            if ((available & (1 << random)) == 0) {
                do {
                    selected = (s32)(selected + 1) % (s32)arg1;
                } while ((available & (1 << selected)) == 0);
            }
            updated = available ^ (1 << selected);
            *state = updated;
            if ((updated & 0xFF & choices) == 0) {
                *((u8 *)D_80041F5C + arg0) = available ^ choices;
            }
        } else {
            *state = random + 1;
        }
    }
    return arg0 + selected;
}
s32 func_1000F6B8(s32 arg0, s16 arg1, s16 arg2, s16 arg3, void *arg4, s16 arg5, s16 arg6) {
    struct00 *entry;
    struct00 *end;
    struct00 *selected;
    u32 distance;
    u32 nearest;
    s32 dx;
    s32 dy;
    s32 dz;
    s32 selectedDx;
    s32 selectedDy;
    s32 selectedDz;
    s32 result;

    if (D_80082FA0 != 0) {
        if (D_80082FA0 >= 0) {
            end = &D_80041F68[D_80082FA0];
            entry = D_80041F68;
            nearest = -1;
            do {
                dx = arg1 - entry->unkC;
                dy = arg2 - entry->unk10;
                dz = arg3 - entry->unk14;
                distance = (dx * dx) + (dy * dy) + (dz * dz);
                if (distance < nearest) {
                    nearest = distance;
                    selected = entry;
                    selectedDx = dx;
                    selectedDy = dy;
                    selectedDz = dz;
                }
                entry++;
            } while (entry <= end);
        }
    } else {
        selected = D_80041F68;
        selectedDx = arg1 - selected->unkC;
        selectedDy = arg2 - selected->unk10;
        selectedDz = arg3 - selected->unk14;
    }

    func_1000A420(
        selectedDx,
        selectedDy,
        selectedDz,
        selected->unk18,
        arg1 - selected->unk0,
        arg2 - selected->unk4,
        arg3 - selected->unk8,
        arg6,
        arg5,
        arg4,
        &result,
        NULL);
    return result;
}
/* Non-matching C placeholders for asm/nonmatchings/init_EB00/func_1000F85C.s. */
void func_1000F85C(u16 arg0, u16 arg1, s32 arg2) {
}
// NON-MATCHING: not even close
// void func_1000F85C(s32 arg0, s16 arg1, s32 arg2) {
//     f32 sp1C;
//     s32 sp18;
//     s16 temp_a1;
//     s16 temp_a1_2;
//     s32 temp_t6;
//     s16 phi_a1;
//
//     temp_t6 = arg0 & 0xFFFF;
//     temp_a1 = arg1;
//     if (temp_t6 >= 16) {
//         sp18 = temp_t6;
//         arg1 = temp_a1;
//         temp_a1_2 = arg1;
//         if (func_1000F3D0(temp_t6) != 0) {
//             if (temp_a1_2 == 16) {
//                 sp18 = sp18;
//                 arg1 = temp_a1_2;
//                 sp1C = alCents2Ratio(arg2, temp_a1_2);
//                 arg2 = (s32) sp1C;
//                 phi_a1 = arg1;
//             } else {
//                 phi_a1 = temp_a1_2;
//                 if (temp_a1_2 == 0x11) {
//                     phi_a1 = (u16)0x10;
//                 }
//             }
//             func_10017714((((sp18 & 0xF) * 0xC) + 0x80040000) - 0x25E8, phi_a1, arg2);
//         }
//     }
// }

void func_1000F91C(u16 arg0, u16 arg1, s16 arg2, u8 arg3, s32 arg4,
                   s16 arg5, s16 arg6, s16 arg7, s16 arg8, s16 arg9) {
    s32 sp2C;
    s32 tmp = func_1000F6B8(arg4, arg5, arg6, arg7, &sp2C, (s32) arg8, (s32) arg9);

    func_1000F85C(arg0, 8, (u32) (tmp * arg1) >> 0xF);
    func_1000F85C(arg0, 4, sp2C & 0x7F);
    func_1000F85C(arg0, 256, (sp2C & 0x80) | arg3);
    func_1000F85C(arg0, 16, arg2);
}

void func_1000F9D4(u16 arg0, s16 arg1, s16 arg2, s16 arg3) {
    u32 tmp;

    func_1000F6B8(-1, arg1, arg2, arg3, &tmp, 32760, 32765);
    func_1000F85C(arg0, 4, tmp & 0x7F);
    func_1000F85C(arg0, 256, tmp & 0x80);
}

u16 func_1000FA64(u16 arg0, s16 arg1, s16 arg2, s16 arg3, s32 arg4, u16 arg5, s16 arg6, s32 arg7, void *arg8, s32 arg9, s32 argA, s32 argB) {
    struct15 *entry;
    s32 count;
    s32 index;
    s16 *y;

    y = &arg2;
    index = D_80042760;
    if (index >= 0x20) {
        return 0;
    }
    D_80042760 = index + 1;

    entry = &D_80041FE0[index];
    if (arg7 != 0) {
        entry->unk10 = argA | 0x12;
    } else {
        entry->unk10 = (argA & 0x108) | 2;
    }

    if ((argA & 0x40) != 0) {
        *y = func_15083E0C((u8)arg1);
        if (*y == -1) {
            return 0;
        }
    }

    *(u16 *)((u8 *)entry + 0x0) = arg0;
    *(s16 *)((u8 *)entry + 0x2) = arg1;
    *(s16 *)((u8 *)entry + 0x4) = *y;
    *(s16 *)((u8 *)entry + 0x6) = arg3;
    *(u16 *)((u8 *)entry + 0x8) = arg5;
    *(s16 *)((u8 *)entry + 0xA) = arg6;
    entry->unkC = arg4;
    entry->unk14 = arg7;
    entry->unk18 = (s32)arg8;
    entry->unk1C = arg9;
    *(s16 *)((u8 *)entry + 0x20) = argB;
    *((u8 *)entry + 0x22) = 0;
    *((u8 *)entry + 0x23) = 0;
    *(s32 *)((u8 *)entry + 0x24) = 0;
    *(s16 *)((u8 *)entry + 0x28) = 0;
    *(f32 *)&entry->unk2C = alCents2Ratio(argB);

    count = D_80042760;
    func_10011624(D_80041FE0, &D_80042760, index, index + 1);
    if (count != D_80042760) {
        return 0;
    }

    entry->unk10 |= 0x1000;
    return entry->unk24;
}
/* Non-matching C placeholders for asm/nonmatchings/init_EB00/func_1000FC18.s. */
void func_1000FC18(u16 arg0, s16 arg1, s16 arg2, s16 arg3, u16 arg4) {
    s32 temp_s2;
    s32 temp_s3;
    s32 temp_s4;
    s32 temp_s5;
    s32 i;
    struct15 *ptr;
    u16 temp_a0;

    temp_s2 = arg0;
    temp_s3 = arg1;
    temp_s4 = arg2;
    temp_s5 = arg3;
    i = 0;
    if (D_80042760 > 0) {
        do {
            ptr = &D_80041FE0[i];
            if ((temp_s2 == *(u16 *)((s32)ptr + 0)) &&
                (temp_s3 == *(s16 *)((s32)ptr + 2)) &&
                (temp_s4 == *(s16 *)((s32)ptr + 4)) &&
                (temp_s5 == *(s16 *)((s32)ptr + 6)) &&
                (arg4 == (*(u16 *)((s32)ptr + 8) & 0x7FFF))) {
                temp_a0 = D_80041FE0[i].unk24;
                if ((unsigned int)temp_a0 != 0) {
                    func_100111C8(temp_a0);
                }
                D_80041FE0[i].unk10 |= 0x80;
            }
            i++;
        } while (i < D_80042760);
    }
}
void func_1000FD38(s32 arg0, s32 arg1, s32 arg2) {
    s32 i;
    struct15 *current;

    for (i = 0; i < D_80042760; i++) {
        current = &D_80041FE0[i];
        if ((current->unk14 == arg0) && (current->unk18 == arg1) && (current->unk1C == arg2)) {
            if (current->unk24 != 0) {
                func_100111C8(current->unk24);
            }
            current->unk10 |= 0x80;
        }
    }
}

void func_1000FDF4(u16 arg0) {
    s32 temp_s2;
    s32 i;
    u16 temp_a0;

    temp_s2 = arg0;
    i = 0;
    if (D_80042760 > 0) {
        do {
            temp_a0 = D_80041FE0[i].unk24;
            if (temp_a0 == temp_s2) {
                if ((unsigned int)temp_a0 != 0) {
                    func_100111C8(temp_a0);
                }
                D_80041FE0[i].unk10 |= 0x80;
            }
            i++;
        } while (i < D_80042760);
    }
}

s32 func_1000FE88(struct15 *arg0, s32 arg1, s32 *arg2) {
    struct15 *current;

    if (arg1 < *arg2) {
        current = (struct15 *)((u8 *)arg0 + (arg1 * sizeof(struct15)));
        if (current->unk24 != 0) {
            func_100111C8(current->unk24);
        }
        current->unk10 |= 0x80;
        return 0;
    }

    return 1;
}

s32 func_1000FEF0(u16 arg0, struct127 *arg1, s32 arg2) {
    struct15 *current;
    s32 i;
    u16 key;

    if (arg0 == 0) {
        return -1;
    }

    i = 0;
    key = arg0;
    if (D_80042760 > 0) {
        current = D_80041FE0;
        do {
            if ((current->unk24 == key) &&
                ((s32)arg1 == current->unk18) &&
                (arg2 == current->unk1C) &&
                ((current->unk10 & 0x80) == 0)) {
                return i;
            }
            i++;
            current++;
        } while (i < D_80042760);
    }

    return -1;
}

s32 func_1000FF90(s32 arg0, s32 arg1, u32 arg2) {
    struct15 *current;
    s32 i;

    for (i = 0; i < D_80042760; i++) {
        current = &D_80041FE0[i];
        if ((arg0 == current->unk14) &&
            ((arg1 == current->unk18) || (arg1 == -1)) &&
            ((arg2 == current->unk1C) || (arg2 == 0xFFFFFFFFU)) &&
            ((current->unk10 & 0x80) == 0)) {
            return i;
        }
    }

    return -1;
}
/* Non-matching C placeholders for asm/nonmatchings/init_EB00/func_1001001C.s. */
void func_1001001C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    s32 i;
    struct15 *ptr;

    ptr = D_80041FE0;
    if (D_80042760 > 0) {
        i = 0;
        do {
            if ((arg0 == ptr->unk14) && (arg1 == ptr->unk18) && (arg2 == ptr->unk1C)) {
                *(f32 *)&ptr->unk2C = alCents2Ratio(arg4);
                ptr->unkC = arg3;
            }
            i++;
            ptr++;
        } while (i < D_80042760);
    }
}
void func_100100E0(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    s32 count;
    struct15 *current;

    count = D_80042760;
    if (count > 0) {
        current = D_80041FE0;
        do {
            if ((current->unk14 == arg0) &&
                (current->unk18 == arg1) &&
                (current->unk1C == arg2)) {
                current->unk14 = arg3;
                current->unk18 = arg4;
                current->unk1C = arg5;
            }
            current++;
        } while (current < &D_80041FE0[count]);
    }
}
s32 func_10010154(u16 arg0, void *arg1, u16 arg2, s16 arg3, u16 arg4) {
    struct127 *actor;
    s32 handle;
    s32 flags;

    actor = arg1;
    handle = 0;
    flags = 0;
    if ((actor->interaction_state == 0) ||
        (actor->interaction_state == 5)) {
        return 0;
    }

    if (actor->camera != NULL) {
        handle = func_10010BE8(actor->unk8E, (s32)actor, arg2, 0x40, 0,
                              (((u32)actor->unk184 >> 3) & 0x30) << 1,
                              D_80041FD9);
        actor->unk8E = handle;
        return actor->unk8E;
    }

    if (actor->id == 0x16) {
        arg3 *= 2;
        if (arg4 < arg3) {
            arg3 = arg4 - 0xC8;
        }
    } else if ((actor->id == 5) || (actor->id == 0x4F) ||
               (actor->id == 0x83)) {
        flags = 4;
    } else if ((actor->unk13C != 0) &&
               ((actor->id == 0x8A) || (actor->id == 0x23))) {
        flags = 0x100;
    }

    func_1000FD38((s32)func_1000EE70, (s32)actor,
                  actor->unique_id | 0x10000);
    if (actor->interaction_state != 0) {
        handle = func_1000FA64(arg0, (s16)actor->x_position,
                               (s16)actor->y_position,
                               (s16)actor->z_position, arg2, arg4, arg3,
                               (s32)func_1000EE70, actor,
                               actor->unique_id | 0x10000, flags, 0);
    }

    actor->unk8E = handle;
}
s32 func_10010344(u16 arg0, void *arg1, s32 arg2, s16 arg3, u16 arg4) {
    struct127 *actor;
    s32 flags;
    s32 packed;
    u8 priority;

    actor = arg1;
    flags = 0;
    if ((actor->interaction_state == 0) ||
        (actor->interaction_state == 5)) {
        return 0;
    }

    if (arg2 < 0) {
        arg2 = -arg2;
        flags = 0x100;
    }

    if (actor->camera != NULL) {
        packed = (((u32)actor->unk184 >> 3) & 0x30) << 1;
        priority = D_80041FD9;
        if ((actor->unk31C != NULL) && ((u8)actor->unk31C->unk94 == 1)) {
            priority = 1;
            arg2 = 0x7FFF;
        }
        flags = func_10010BE8(actor->unk8C, arg0, arg2, 0x40, 0,
                             packed, priority);
        actor->unk8C = flags;
        goto done;
    }

    if (actor->id == 0x16) {
        arg3 *= 2;
        if (arg4 < arg3) {
            arg3 = arg4 - 0xC8;
        }
    } else if ((actor->id == 0x8A) && (actor->unk13C != 0)) {
        flags |= 0x100;
    } else if ((actor->id == 0x4F) || (actor->id == 0x83)) {
        flags |= 4;
    }

    func_1000FD38((s32)func_1000EE70, (s32)actor,
                  actor->unique_id | 0x20000);
    flags = func_1000FA64(arg0, (s16)actor->x_position,
                          (s16)actor->y_position,
                          (s16)actor->z_position, arg2, arg4, arg3,
                          (s32)func_1000EE70, actor,
                          actor->unique_id | 0x20000, flags, 0);
    actor->unk8C = flags;

done:
    return flags;
}
/* Non-matching C placeholders for asm/nonmatchings/init_EB00/func_10010558.s. */
void func_10010558(u16 arg0, struct127 *arg1, s32 arg2, s16 arg3, u16 arg4, s32 arg5) {
    if (arg5 <= 0) {
        func_10010344(arg0, arg1, arg2, arg3, arg4);
    } else {
        func_1000FA64(arg0, (s16)arg1->x_position, (s16)arg1->y_position, (s16)arg1->z_position, arg2, arg4, arg3, (s32)func_1000ECCC, (void *)arg5, (s32)arg1, 0, 0);
    }
}

void func_10010630(u16 arg0, struct127 *arg1, s32 arg2, s16 arg3, u16 arg4) {
    struct127 *actor;
    s32 value;

    actor = arg1;
    value = arg2;
    if (actor->interaction_state != 0) {
        if (actor->camera != 0) {
            func_10010F30(arg0, (u16)value, 64, 0,
                          (((u32)actor->unk184 >> 3) & 0x30) * 2);
        } else {
            func_1000FA64(arg0, (s16)actor->x_position,
                          (s16)actor->y_position, (s16)actor->z_position,
                          value, arg4, arg3, (s32)func_1000EE70, actor,
                          actor->unique_id, 0, 0);
        }
    }
}

void func_10010720(u16 arg0, struct127 *arg1, s32 arg2, s16 arg3, u16 arg4, s32 arg5) {
    if (arg5 <= 0) {
        func_10010630(arg0, arg1, arg2, arg3, arg4);
    } else {
        func_1000FA64(arg0, arg1->x_position, arg1->y_position, arg1->z_position, arg2, arg4, arg3, func_1000EDA0, arg5, arg1, 0, 0);
    }
}

s32 func_100107F8(struct127 *arg0) {
    if (arg0->interaction_state == 0) {
        return 0;
    } else {
        if (arg0->camera != 0) {
            if (arg0->unk8E != 0) {
                if (func_1000F3D0(arg0->unk8E) != 0) {
                    return 1;
                }
            }
        } else {
            if (func_1000FF90(func_1000EE70, arg0, arg0->unique_id | 0x10000) != -1) {
                return 1;
            }
        }
        arg0->unk8E = 0;
    }
    return 0;
}

s32 func_10010894(struct127 *arg0) {
    if (arg0->camera != 0) {
        if (arg0->unk8C != 0) {
            if (func_1000F3D0(arg0->unk8C) != 0) {
                return 1;
            }
        }
    } else {
        if (func_1000FF90(func_1000EE70, arg0, arg0->unique_id | 0x20000) != -1) {
            return 1;
        }
    }
    arg0->unk8C = 0;
    return 0;
}

void func_1001091C(struct127 *arg0, s32 arg1) {
    s32 temp_v0;

    if (arg1 == 0) {
        return;
    }
    if (arg0->interaction_state == 0) {
        return;
    }
    if (arg0->camera != 0) {
        if (arg0->unk8E != 0) {
            func_1000F85C(arg0->unk8E, 8, arg1);
        }
        return;
    }
    temp_v0 = func_1000FF90((s32)func_1000EE70, (s32)arg0, arg0->unique_id | 0x10000);
    if (temp_v0 != -1) {
        D_80041FEC[temp_v0][0] = arg1;
    } else {
        arg0->unk8E = 0;
    }
}

void func_100109D0(struct127 *arg0) {
    if (arg0->camera) {
        if (arg0->unk8E) {
            func_100111C8(arg0->unk8E);
        }
    } else {
        func_1000FD38(func_1000EE70, arg0, arg0->unique_id | 0x10000);
    }
    arg0->unk8E = 0;
}

void func_10010A3C(struct127 *arg0) {
    if (arg0->camera) {
        if (arg0->unk8C) {
            func_100111C8(arg0->unk8C);
        }
    } else {
        func_1000FD38(func_1000EE70, arg0, arg0->unique_id | 0x20000);
    }
    arg0->unk8C = 0;
}

void func_10010AA8(struct127 *arg0) {
    s32 sp24;
    struct15 *tmp;

    if (arg0->camera != 0) {
        if (arg0->unk8C && func_1000F44C(arg0->unk8C)) {
            func_100111C8(arg0->unk8C);
        }
        if (arg0->unk8E && func_1000F44C(arg0->unk8E)) {
            func_100111C8(arg0->unk8E);
        }
    } else {
        sp24 = func_1000FEF0(arg0->unk8C, arg0, arg0->unique_id);
        if (sp24 != -1) {
            if (func_1000F44C(arg0->unk8C)) {
                func_100111C8(arg0->unk8C);
            }
            tmp = &D_80041FE0[sp24];
            tmp->unk10 |= 0x80;
        }
        sp24 = func_1000FEF0(arg0->unk8E, arg0, arg0->unique_id);
        if (sp24 != -1) {
            if (func_1000F44C(arg0->unk8E)) {
                func_100111C8(arg0->unk8E);
            }
            tmp = &D_80041FE0[sp24];
            tmp->unk10 |= 0x80;
        }
    }
    arg0->unk8C = 0;
    arg0->unk8E = 0;
}

u16 func_10010BE8(s32 arg0, s32 arg1, u16 arg2, u8 arg3, s16 arg4, u8 arg5, u8 arg6) {
    struct120 *slot;
    u16 handle;
    u16 next;
    s32 index;
    s32 soundId;
    u8 mix;
    volatile s32 normalizedHandle;

    normalizedHandle = arg0 & 0xFFFF;
    arg0 = normalizedHandle;
    index = arg0 & 0xF;
    slot = &D_800425E0[index];

    if ((slot->unk0 == arg0) && (arg0 != 0)) {
        if ((slot->unk8 != NULL) && (func_100173C4(&slot->unk8) != 0)) {
            func_10017594(slot->unk8);
            slot->unk8 = NULL;
        }
    } else {
        if (((slot->unk8 != NULL) && (func_100173C4(&slot->unk8) != 0)) ||
            ((slot->unk4 & 0x8000) != 0)) {
            index = 0;
            slot = &D_800425E0[0];
            if (((slot->unk8 != NULL) && (func_100173C4(&slot->unk8) != 0)) ||
                ((slot->unk4 & 0x8000) != 0)) {
                while (++index < 16) {
                    slot = &D_800425E0[index];
                    if (((slot->unk8 == NULL) || (func_100173C4(&slot->unk8) == 0)) &&
                        ((slot->unk4 & 0x8000) == 0)) {
                        break;
                    }
                }
            }
        }
    }

    if (arg2 < 100) {
        return 0;
    }
    if (index >= 16) {
        handle = 0;
        goto done;
    }
    if (arg1 == 0) {
        return 0;
    }

    soundId = arg1 & 0x7FFF;
    if (soundId >= 0x6E3) {
        return 0;
    }

    slot = &D_800425E0[index];
    handle = slot->unk2;
    next = handle + 0x10;
    slot->unk0 = handle;
    if (next < 0x10) {
        next += 0x10;
    }
    slot->unk2 = next;
    slot->unk4 = arg1;
    if (slot->unk8 != NULL) {
        slot->unk8->unk54 = 5;
    }

    mix = arg5;
    if (((mix & 0x7F) + (u8)D_80041FD8) < 0x80) {
        mix += (u8)D_80041FD8;
    } else {
        mix |= 0x7F;
    }

    func_10017438((void *)D_8003E368, (s16)soundId, arg2, arg3,
                  alCents2Ratio(arg4), mix, arg6, &slot->unk8);
done:
    return handle;
}
u16 func_10010E78(u16 arg0, s32 arg1, u16 arg2, s16 arg3, u8 arg4, s32 arg5, s16 arg6, s16 arg7, s16 arg8, s16 arg9, s16 argA) {
    s32 packed;
    s32 scaled;

    scaled = ((u32)arg2 * func_1000F6B8(arg5, arg6, arg7, arg8, &packed, arg9, argA)) >> 15;
    if (scaled != 0) {
        return func_10010BE8(arg0, arg1, scaled, packed & 0x7F, arg3,
                            (packed & 0x80) | arg4, D_80041FD9);
    }
    return 0;
}

void func_10010F30(s32 arg0, u16 arg1, u8 arg2, s16 arg3, u8 arg4) {
    func_10010BE8(0, arg0, arg1, arg2, arg3, arg4, D_80041FD9);
}

u16 func_10010E78(u16 arg0, s32 arg1, u16 arg2, s16 arg3, u8 arg4, s32 arg5, s16 arg6, s16 arg7, s16 arg8, s16 arg9, s16 argA);

void func_10010F88(s32 arg0, u16 arg1, s16 arg2, u8 arg3, s32 arg4, s16 arg5, s16 arg6, s16 arg7, s16 arg8, s16 arg9) {
    func_10010E78(0, arg0, arg1, arg2, arg3, arg4, arg5, arg6, arg7, arg8, arg9);
}
u16 func_10010FFC(s32 arg0, s32 arg1, u16 arg2, s16 arg3, u8 arg4, struct127 *arg5) {
    f32 scale;

    arg0 &= 0xFFFF;

    if ((arg5 == NULL) || (arg5->interaction_state == 0)) {
        return 0;
    }

    if (arg5->camera != NULL) {
        return func_10010BE8(arg0, arg1, arg2, 0x40, arg3, arg4, D_80041FD9);
    }

    arg2 = ((arg2 + arg2) + arg2) >> 2;
    if (arg5->id != 0xFF) {
        scale = (u16)D_800D1C90[arg5->id]->unkE * arg5->xz_scale;
    } else {
        scale = 0.0f;
    }

    if (scale > 256.0f) {
        scale = 1.0f;
    } else if (scale < 80.0f) {
        scale = 0.3125f;
    } else {
        scale *= 0.00390625f;
    }

    return func_10010E78(arg0, arg1, arg2, arg3, arg4, 0,
                         arg5->x_position, arg5->y_position, arg5->z_position,
                         500, (s32)(2000.0f * scale) + 501);
}

void func_100111C8(u16 arg0) {
    struct120 *tmp = &D_800425E0[arg0 & 0xF];

    if ((tmp->unk8 != 0) && (tmp->unk0 == arg0)) {
        tmp->unk0 = 0;
        tmp->unk4 = 0;
        func_10017594(tmp->unk8);
        tmp->unk8 = 0;
    }
}

void func_1001123C(u16 arg0) {
    struct120 *tmp = &D_800425E0[arg0 & 0xF];

    if ((tmp->unk8 != 0) && (tmp->unk0 == arg0)) {
        if (func_100112BC(arg0, 1) == 0) {
            func_10017594(tmp->unk8);
            tmp->unk8 = 0;
        }
    }
}

s32 func_100112BC(s32 arg0, s32 arg1) {
    struct49 *temp_a0;
    s32 temp_v1 = D_80041F50;

    if (temp_v1 < 16) {
        temp_a0 = &D_80041F10[temp_v1];
        temp_a0->unk0 = arg0;
        temp_a0->unk2 = arg1;
        temp_a0->unk3 = arg0 & 0xF;
        D_80041F50 = temp_v1 + 1;
        return 1;
    } else {
        return 0;
    }
}

void func_10011310(void) {
    struct49 *current;
    struct49 *end;
    struct120 *slot;
    s32 destinationIndex;
    s32 compacting;
    u32 count;
    u32 remaining;

    count = D_80041F50;
    compacting = 0;
    destinationIndex = 0;
    remaining = count;

    if ((s32)count > 0) {
        current = D_80041F10;
        do {
            if ((u8)current->unk2 > 0) {
                current->unk2 = (u8)current->unk2 - 1;
                end = &D_80041F10[D_80041F50];
            } else {
                compacting = 1;
                slot = &D_800425E0[(u8)current->unk3];
                if ((u16)slot->unk0 == (u16)current->unk0) {
                    void *allocation = slot->unk8;

                    slot->unk0 = 0;
                    slot->unk4 = 0;
                    if (allocation != NULL) {
                        func_10017594(allocation);
                    }
                    slot->unk8 = NULL;
                }
                remaining--;
                end = &D_80041F10[D_80041F50];
            }

            if (&D_80041F10[destinationIndex] != current) {
                D_80041F10[destinationIndex] = *current;
            }
            current++;
            if (compacting != 0) {
                destinationIndex++;
            } else {
                compacting = 0;
            }
        } while (current < end);
    }

    D_80041F50 = remaining;
}

s32 func_1001147C(u16 arg0) {
    struct120 *tmp;

    if (arg0 != 0) {
        tmp = &D_800425E0[arg0 & 0xF];
        if (tmp->unk0 == arg0) {
            return tmp->unk4 & 0x7FFF;
        }
    }
    return -1;
}

void func_100114D0(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 *arg6, s32 *arg7, s32 *arg8) {
    struct00 *entry;
    struct00 *selected;
    u32 count;
    u32 limit;
    u32 index;
    u32 distance;
    u32 nearest;
    s32 dx;
    s32 dy;
    s32 dz;
    s32 result;

    count = D_80082FA0;
    selected = D_80041F68;
    if (count != 0) {
        limit = count;
        entry = D_80041F68;
        nearest = -1;
        index = 0;
        do {
            dx = arg0 - entry->unkC;
            dy = arg1 - entry->unk10;
            dz = arg2 - entry->unk14;
            distance = (dx * dx) + (dy * dy) + (dz * dz);
            if (distance < nearest) {
                nearest = distance;
                selected = entry;
            }
            entry++;
            index++;
        } while (index <= limit);
    }

    func_1000A420(
        arg0 - selected->unkC,
        arg1 - selected->unk10,
        arg2 - selected->unk14,
        selected->unk18,
        arg0 - selected->unk0,
        arg1 - selected->unk4,
        arg2 - selected->unk8,
        arg4,
        arg5,
        arg6,
        &result,
        arg8);
    *arg7 = ((u32)result * arg3) >> 15;
}
/* Non-matching C placeholders for asm/nonmatchings/init_EB00/func_10011624.s. */
s32 func_10011624(struct15 *arg0, s32 *arg1, s32 arg2, s32 arg3) {
    return 0;
}
void func_10011BB8(void) {
    struct108 *player;
    struct00 *listener;
    struct00 *listenerEnd;
    struct15 *source;
    struct15 *destination;
    struct15 *recordEnd;
    s32 playerIndex;
    s32 activeCount;
    s32 step;

    if ((D_80041F60 == 0) && (D_80041F61 == 0)) {
        playerIndex = D_80082FA0;
        listener = D_80041F68;
        if (playerIndex >= 0) {
            player = D_800DBFF0;
            listenerEnd = (struct00 *)((u8 *)D_80041F68 + (playerIndex * 0x1C));
            do {
                if ((playerIndex != 0) || ((player->unk2C & 0x80000) != 0)) {
                    listener->unk0 = player->unk2F8;
                    listener->unk4 = player->unk2FC;
                    listener->unk8 = player->unk300;
                } else {
                    listener->unk0 = player->unk2A4;
                    listener->unk4 = player->unk2A8;
                    listener->unk8 = *(f32 *)&player->unk2AC;
                }
                listener->unkC = player->unk2F8;
                listener->unk10 = player->unk2FC;
                listener->unk14 = player->unk300;
                *(f32 *)&listener->unk18 = player->unk380;
                listener++;
                player++;
            } while (listener <= listenerEnd);
        }

        func_10011310();
        func_10011624(D_80041FE0, &D_80042760, 0, D_80042760);

        activeCount = 0;
        if (D_80042760 > 0) {
            source = D_80041FE0;
            recordEnd = &source[D_80042760];
            destination = source;
            do {
                *destination = *source;
                if ((destination->unk10 & 0x80) == 0) {
                    activeCount++;
                    destination++;
                }
                source++;
            } while (source < recordEnd);
        }
        D_80042760 = activeCount;
    }

    if ((D_80041FDC != D_80041F54) || (D_80041F61 != D_80041F60)) {
        if (D_80041F61 == 1) {
            func_10017780(0, 0);
            func_10017780(1, 0);
        } else {
            func_10017780(0, D_80041F54);
            func_10017780(1, *(u16 *)((u8 *)&D_80041F54 + 2));

            step = (D_80041FDC - D_80041F54) * D_80041F58;
            if (step != 0) {
                D_80041F54 += step;
            } else {
                D_80041F54 = D_80041FDC;
            }
        }
        D_80041F60 = D_80041F61;
    }
}

void func_10011E88(s32 arg0) {
}

void func_10011E94(s32 arg0) {
    if (arg0) {
        D_80041F61 = 1;
    } else {
        D_80041F61 = 0;
    }
}

u16 func_10011EB8(s32 arg0, s16 *arg1, s32 arg2) {
    u16 (*table)[5][2];
    u16 *entry;
    s32 index;
    s32 value;

    index = arg0;
    index = func_1510F8CC(index);
    if (arg1 != NULL) {
        if (D_80082FA0 != 0) {
            *arg1 = 0x7FFF / (D_80082FA0 + 1);
        } else {
            *arg1 = 0x7FFF;
        }
    }

    table = (u16 (*)[5][2])D_8002C240;
    entry = table[index][arg2];
    value = entry[0];
    if (entry[1] >= 2) {
        value = func_1000F568(value, entry[1]);
    }
    return value;
}
// NON-MATCHING: whats going on here
// u16 func_10011EB8(s32 arg0, s16 *arg1, s32 arg2, s32 arg3) {
//     struct120 *temp_v1_2;
//     s32 temp_v0;
//     s32 temp_a0;
//
//     temp_v0 = func_1510F8CC(arg0);
//     if (arg1 != NULL) {
//         if (D_80082FA0 != 0) {
//             *arg1 = 0x7FFF / (D_80082FA0 + 1);
//         } else {
//             *arg1 = 0x7FFF;
//         }
//     }
//     temp_v1_2 = &D_8002C240[temp_v0 + arg2];
//     temp_a0 = temp_v1_2->unk0;
//     if (temp_v1_2->unk2 >= 2) {
//         temp_a0 = func_1000F568(temp_v0, temp_v1_2->unk2);
//     }
//     return temp_a0;
// }
