#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_10008F90();
s32 func_100095A0(struct50 *arg0, struct51 *arg1);
s32 func_100099BC(void);
s32 func_1000A03C();
void func_1000A348(void);
extern s32 D_100291A0_pass2;
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/init_8F90/func_10008F90.s. */
s32 func_10008F90() {
    return 0;
}
// NON-MATCHING: so much to do
// void func_10008F90(struct15 *arg0, OSPri arg1, struct52 *arg2) {
//     // ? sp160;
//     s32 sp58;
//     // ? *temp_t4_2;
//     f32 temp_f0;
//     s32 temp_f8;
//     s32 temp_t4;
//     s32 temp_t7;
//     s32 temp_v0;
//     // u32 temp_a1;
//     // u32 temp_s0_2;
//     // void *temp_a0;
//     // void *temp_s0;
//     // void *temp_s0_3;
//     // void *temp_s1;
//     // void *temp_t0;
//     // void *temp_v0_2;
//     // void *temp_v0_3;
//     // void *temp_v0_4;
//     // void *temp_v1;
//     u32 phi_v1;
//     void *phi_t0;
//     s32 *phi_t4;
//     // void *phi_s0;
//     // void *phi_s1;
//     // void *phi_v0;
//     // s32 phi_v1_2;
//     // u32 phi_a1;
//     // u32 phi_s0_2;
//     // void *phi_s0_3;
//
//     func_10012588(&D_8003E370);
//     arg0->unk10 = func_10009980;
//     temp_v0 = osAiSetFrequency(arg2->unk0);
//     arg0->unk2C = temp_v0;
//     arg0->unk14 = func_10009FFC;
//     arg0->unk18 = func_10009B2C;
//     arg0->unk1C = func_10009B90;
//     arg0->unk20 = func_10009B4C;
//     temp_f0 = ((f32) (u32) arg2->unk4 * (f32) temp_v0) / 30.0f;
//     temp_f8 = (s32) temp_f0;
//     D_80040F8C = temp_f8;
//     phi_v1 = temp_f8;
//     if ((f32) (u32) temp_f8 < temp_f0) {
//         temp_t4 = temp_f8 + 1;
//         D_80040F8C = temp_t4;
//         phi_v1 = (u32) temp_t4;
//     }
//     temp_t7 = ((phi_v1 / 184) * 184) + 184;
//     D_80040F8C = temp_t7;
//     D_80040F88 = temp_t7 - 184;
//     D_80040F90 = temp_t7 + 84;
//     D_80040F84 = (u8)0;
//     phi_t0 = D_8002AE54;
//     phi_t4 = &sp58;
// // loop_3:
// //     temp_t0 = phi_t0 + 0xC;
// //     temp_t4_2 = phi_t4 + 0xC;
// //     temp_t4_2->unk-C = (s32) *phi_t0;
// //     temp_t4_2->unk-8 = (s32) temp_t0->unk-8;
// //     temp_t4_2->unk-4 = (s32) temp_t0->unk-4;
// //     phi_t0 = temp_t0;
// //     phi_t4 = temp_t4_2;
// //     if (temp_t0 != 0x8002B064) {
// //         goto loop_3;
// //     }
// //     arg0->unk34 = &sp58;
// //     arg0->unk38 = &sp160;
// //     n_alInit(0x8003E640, arg0, (void *)0x80040F8C, &sp58);
// //     *(void *)0x8003E380 = 0x8003E640;
// //     D_800406B8.unk4 = 0;
// //     D_800406B8.unk0 = 0;
// //     phi_s0 = &D_800406B8;
// //     phi_s1 = (void *)0x800406CC;
// // loop_5:
// //     temp_v0_2 = phi_s0->unk0;
// //     phi_s0->unk18 = phi_s0;
// //     phi_s0->unk14 = temp_v0_2;
// //     if (temp_v0_2 != 0) {
// //         temp_v0_2->unk4 = phi_s1;
// //     }
// //     phi_s0->unk0 = phi_s1;
// //     temp_s1 = phi_s1 + 0x14;
// //     temp_s0 = phi_s0 + 0x14;
// //     temp_s0->unk-4 = alHeapDBAlloc(0, 0, arg0->unk28, 1, 2048);
// //     phi_s0 = temp_s0;
// //     phi_s1 = temp_s1;
// //     if ((u32) temp_s1 < (u32) &D_80040AC8) {
// //         goto loop_5;
// //     }
// //     temp_s0->unk10 = alHeapDBAlloc(0, 0, arg0->unk28, 1, 2048);
// //     bzero(&D_80040AC8, 1200);
// //     D_80040AC8.unk4 = 0;
// //     D_80040AC8.unk0 = 0;
// //     phi_v0 = &D_80040AC8;
// //     phi_v1_2 = 0x80040AE0;
// //     phi_a1 = 0U;
// // loop_9:
// //     temp_a0 = phi_v0->unk0;
// //     phi_v0->unk1C = phi_v0;
// //     phi_v0->unk18 = temp_a0;
// //     if (temp_a0 != 0) {
// //         temp_a0->unk4 = phi_v1_2;
// //     }
// //     phi_v0->unk0 = phi_v1_2;
// //     temp_a1 = phi_a1 + 1;
// //     temp_v0_3 = phi_v0 + 0x18;
// //     temp_v0_3->unk-8 = 0;
// //     phi_v0 = temp_v0_3;
// //     phi_v1_2 = phi_v1_2 + 0x18;
// //     phi_a1 = temp_a1;
// //     if (temp_a1 < 0x31U) {
// //         goto loop_9;
// //     }
// //     temp_v0_3->unk10 = 0;
// //     phi_s0_2 = 0x8003E388U;
// // loop_13:
// //     temp_s0_2 = phi_s0_2 + 4;
// //     temp_s0_2->unk-4 = alHeapDBAlloc(0, 0, arg0->unk28, 1, arg2->unk8 * 8);
// //     phi_s0_2 = temp_s0_2;
// //     if (temp_s0_2 < 0x8003E390U) {
// //         goto loop_13;
// //     }
// //     *(void *)0x80040F94 = (s32) arg2->unk8;
// //     phi_s0_3 = (void *)0x8003E388;
// // loop_15:
// //     temp_v0_4 = alHeapDBAlloc(0, 0, arg0->unk28, 1, 0x90);
// //     phi_s0_3->unk8 = temp_v0_4;
// //     temp_v0_4->unk70 = (u16)2;
// //     temp_v1 = phi_s0_3->unk8;
// //     temp_v1->unk74 = temp_v1;
// //     temp_s0_3 = phi_s0_3 + 4;
// //     phi_s0_3->unk8->unk0 = alHeapDBAlloc(0, 0, arg0->unk28, 1, *(void *)0x80040F90 * 4);
// //     phi_s0_3 = temp_s0_3;
// //     if (temp_s0_3 != 0x8003E394) {
// //         goto loop_15;
// //     }
//
//     osCreateMesgQueue(&D_8003E608, &D_8003E620, 8);
//     osCreateMesgQueue(&D_8003E5D0, &D_8003E5E8, 8);
//     osCreateMesgQueue(&D_80041298, &D_800412B0, 32);
//     osCreateMesgQueue(&D_800416F0, &D_80041708, 40);
//     osCreateThread(&D_8003E3A0, 4, (void *) func_10009400, 0, &D_800406A0, arg1);
//     D_8002AE40 = (u8)1;
//     osStartThread(&D_8003E3A0);
// }

void func_100093CC(void) {
    if (D_8002AE40 != 0) {
        osStopThread(&D_8003E3A0);
    }
}

// audio thread
void func_10009400(s32 arg0) {
    OSMesg msg;
    volatile s32 sp54;
    OSPfs *sp4C;
    s16 temp_v0;
    u32 phi_s0;
    s32 phi_s1;
    s32 phi_s3;
    s32 phi_s4;
    s32 phi_s5;

    msg = NULL;
    sp54 = 0;
    phi_s0 = 0;
    phi_s5 = 0;
    phi_s4 = 1;
    phi_s1 = 0;
    func_100051C8(&sp4C, &D_8003E5D0);
    phi_s3 = 4;
    do {
        osRecvMesg(&D_8003E5D0, &msg, 1);
        if (D_8002AC5C != 0) {
            ((struct53*)msg)->unk0 = phi_s3;
        }
        temp_v0 = ((struct53*)msg)->unk0;
        switch (temp_v0) {
        case 1:
            if (phi_s0 >= 2U) {
                phi_s0 = 0;
            }
            if (phi_s0 == 0 && func_100095A0(D_8003E390[D_8002AE44 % 3U], phi_s5) != 0) {
                if (phi_s4 == 0) {
                    osRecvMesg(&D_8003E608, &msg, 1);
                    phi_s5 = ((struct53*)msg)->unk4;
                }
                phi_s4 = 0;
            }
            phi_s0++;
            break;
        case 4:
            phi_s1 = 1;
            break;
        case 10:
            phi_s1 = 1;
            break;
        }
    } while (phi_s1 == 0);

    n_alClose(&D_8003E640);
    while (1) {
        osRecvMesg(&D_8003E5D0, &msg, 1);
    }
}

s32 func_100095A0(struct50 *arg0, struct51 *arg1) {
    Acmd *commands;
    s32 physical;
    s32 commandCount[3];
    s32 samples;

    physical = osVirtualToPhysical(arg0->unk0);
    func_100099BC();
    func_1000A03C();
    samples = IO_READ(AI_LEN_REG) >> 2;

    if (arg1 != NULL) {
        osAiSetNextBuffer((void *)arg1->unk4, arg1->unk8 * 4);
    }

    if ((samples >= 0xF9) && (D_80040F84 == 0)) {
        arg0->unk8 = D_80040F88;
        D_80040F84 = 2;
    } else {
        arg0->unk8 = D_80040F8C;
        if (D_80040F84 != 0) {
            D_80040F84--;
        }
    }

    if (((physical + (arg0->unk8 * 4)) & 0x1FFF) == 0) {
        arg0->unk4 = arg0->unk0 + 0x10;
        physical += 0x10;
    } else {
        arg0->unk4 = arg0->unk0;
    }

    commands = n_alAudioFrame((Acmd *)D_8003E388[D_8002AE4C],
                              &commandCount[2], (s16 *)physical, arg0->unk8);
    if (commandCount[2] == 0) {
        return 0;
    }

    arg0->unk10 = 0;
    arg0->unk68 = (s32)&D_8003E608;
    arg0->unk6C = (s32)&arg0->unk70;
    arg0->unk1C = 2;
    arg0->unk20 = 0;
    arg0->unk58 = D_8003E388[D_8002AE4C];
    arg0->unk5C = (((s32)commands - D_8003E388[D_8002AE4C]) >> 3) << 3;
    arg0->unk28 = 2;
    arg0->unk30 = (s32)&D_100290D0;
    arg0->unk34 = (s32)&D_100291A0 - (s32)&D_100290D0;
    arg0->unk2C = 0;
    arg0->unk38 = (s32)&D_100291A0_pass2;
    arg0->unk40 = (s32)&D_8002C960;
    arg0->unk44 = 0x800;
    arg0->unk60 = 0;
    arg0->unk64 = 0x400;

    osWritebackDCacheAll();
    osSendMesg(&D_8003B200, (OSMesg)&arg0->unk10, OS_MESG_BLOCK);
    D_8002AE4C ^= 1;
    return 1;
}
// NON-MATCHING: so far away
// s32 func_100095A0(struct50 *arg0, struct51 *arg1) {
//     s32 sp3C;
//     s32 sp34;
//     u32 sp30;
//     s32 temp_a2;
//     s32 temp_v1;
//     u32 temp_t7;
//     u8 temp_v0;
//     s32 phi_v1;
//     s32 phi_a2;
//
//     sp3C = osVirtualToPhysical(arg0->unk0);
//     func_100099BC();
//     func_1000A03C();
//     temp_a2 = sp3C;
//     temp_t7 = (u32) AI_A4500004 >> 2;
//     phi_v1 = (s32) temp_t7;
//     if (arg1 != 0) {
//         sp3C = temp_a2;
//         sp30 = temp_t7;
//         func_10002DB0(arg1->unk4, arg1->unk8 * 4, temp_a2);
//         phi_v1 =  sp30;
//     }
//     if ((phi_v1 >= 0xF9) && (D_80040F84 == 0)) {
//         arg0->unk8 = D_80040F88; // *
//         D_80040F84 = 2U;
//     } else {
//         arg0->unk8 = D_80040F8C; // *
//         temp_v0 = D_80040F84;
//         if (temp_v0 != 0) {
//             D_80040F84 = (u8) (temp_v0 - 1);
//         }
//     }
//     if (((temp_a2 + (arg0->unk8 * 4)) & 0x1FFF) == 0) {
//         arg0->unk4 = (s32) (arg0->unk0 + 16);
//         phi_a2 = temp_a2 + 16;
//     } else {
//         arg0->unk4 = (s32) arg0->unk0;
//         phi_a2 = temp_a2;
//     }
//     // temp_v1 = alAudioFrame(D_8003E388[D_8002AE4C], &sp34, phi_a2, arg0->unk8);
//     if (sp34 == 0) {
//         return 0;
//     }
//     arg0->unk10 = 0;
//     arg0->unk68 = 0x8003E608;
//     arg0->unk6C = arg0->unk70;
//     arg0->unk1C = 2;
//     arg0->unk20 = 0;
//     arg0->unk58 = (s32) D_8003E388[D_8002AE4C];
//     arg0->unk5C = (s32) (((s32) D_8003E388[temp_v1 - D_8002AE4C] >> 3) * 8);
//     arg0->unk28 = 2;
//     arg0->unk30 = 0x100290D0;
//     arg0->unk34 = (s32) (D_100291A0 - D_100290D0);
//     arg0->unk2C = 0;
//     arg0->unk38 = 0x100291A0;
//     arg0->unk40 = 0x8002C960;
//     arg0->unk44 = 2048;
//     arg0->unk60 = 0;
//     arg0->unk64 = 1024;
//     // D_8002AE4C, 0x8003E388, 2
//     osWritebackDCacheAll();
//     osSendMesg(&D_8003B200, &arg0->unk10, 1);
//     D_8002AE4C = D_8002AE4C ^ 1;
//     return 1;
// }

s32 func_100097CC(u32 arg0, s32 arg1, s32 arg2) {
    struct54 *current;
    struct54 *previous;
    s32 lowBit;
    s32 dramAddress;

    current = (struct54 *)D_80040F78.unk4;
    previous = NULL;
    while (current != NULL) {
        if (arg0 < current->unk8) {
            break;
        }
        previous = current;
        if ((s32)(current->unk8 + 0x800) >= (s32)(arg0 + arg1)) {
            current->unkC = D_8002AE44;
            return osVirtualToPhysical(current->unk10 + arg0 - current->unk8);
        }
        current = current->unk0;
    }

    current = (struct54 *)D_80040F78.unk8;
    if (current == NULL || D_8002AE48 >= 0x20U) {
        return 0;
    }

    D_80040F78.unk8 = (s32)current->unk0;
    if (current->unk0 != NULL) {
        current->unk0->unk4 = current->unk4;
    }
    if (current->unk4 != NULL) {
        current->unk4->unk0 = current->unk0;
    }

    if (previous != NULL) {
        current->unk4 = previous;
        current->unk0 = previous->unk0;
        if (previous->unk0 != NULL) {
            previous->unk0->unk4 = current;
        }
        previous->unk0 = current;
    } else {
        if (D_80040F78.unk4 != 0) {
            current->unk0 = (struct54 *)D_80040F78.unk4;
            D_80040F78.unk4 = (s32)current;
            current->unk4 = NULL;
            current->unk0->unk4 = current;
        } else {
            D_80040F78.unk4 = (s32)current;
            current->unk0 = NULL;
            current->unk4 = NULL;
        }
    }

    lowBit = arg0 & 1;
    dramAddress = current->unk10;
    arg0 -= lowBit;
    current->unk8 = arg0;
    current->unkC = D_8002AE44;
    arg2 = D_8002AE48;
    D_8002AE48 = arg2 + 1;
    osPiStartDma((OSIoMesg *)&D_80040F98[arg2], 1, 0, arg0,
                 dramAddress, 0x800, (OSMesgQueue *)&D_80041298);
    return osVirtualToPhysical(dramAddress) + lowBit;
}

s32 func_10009980(s32 *arg0) {
    if (D_80040F78.unk0 == 0) {
        D_80040F78.unk4 = (u8) 0;
        D_80040F78.unk8 = &D_800406B8;
        D_80040F78.unk0 = 1;
    }
    *arg0 = 0;
    return func_100097CC;
}

s32 func_100099BC(void) {
    OSMesg messages[2];
    struct54 *current;
    struct54 *next;
    struct54 *previous;
    struct54 *freeHead;
    struct54 *freeNext;
    u32 received;

    messages[0] = NULL;
    received = 0;
    if (D_8002AE48 != 0) {
        do {
            if (osRecvMesg((OSMesgQueue *)&D_80041298, &messages[0], OS_MESG_NOBLOCK) == -1) {
                osRecvMesg((OSMesgQueue *)&D_80041298, &messages[0], OS_MESG_BLOCK);
            }
            received++;
        } while (received < (u32)D_8002AE48);
    }

    current = (struct54 *)D_80040F78.unk4;
    while (current != NULL) {
        next = current->unk0;
        if ((u32)(current->unkC + 1) < D_8002AE44) {
            if (current == (struct54 *)D_80040F78.unk4) {
                D_80040F78.unk4 = (s32)next;
            }

            if (current->unk0 != NULL) {
                current->unk0->unk4 = current->unk4;
            }
            previous = current->unk4;
            if (previous != NULL) {
                previous->unk0 = current->unk0;
            }

            freeHead = (struct54 *)D_80040F78.unk8;
            if (freeHead != NULL) {
                current->unk4 = freeHead;
                current->unk0 = freeHead->unk0;
                freeNext = freeHead->unk0;
                if (freeNext != NULL) {
                    freeNext->unk4 = current;
                }
                freeHead->unk0 = current;
            } else {
                D_80040F78.unk8 = (s32)current;
                current->unk0 = NULL;
                current->unk4 = NULL;
            }
        }
        current = next;
    }

    D_8002AE48 = 0;
    D_8002AE44++;
    return (s32)current;
}

void func_10009B2C(struct54 *arg0) {
    if (((s32)arg0 & 1) == 0) {
        arg0->unk14--;
    }
}

void func_10009B4C(struct54 *arg0) { // struct147 unk14 is wrong type
    if (((s32)arg0 & 1) == 0) {
        arg0->unk14--;
        if (arg0->unk14 == 0) {
            func_10009BE4(arg0);
        }
    }
}

void func_10009B90(struct54 *arg0) {
    if (((s32)arg0 & 1) == 0) {
        if (1 == arg0->unk15) {
            if (1 == arg0->unk16) {
                arg0->unk14 += 1;
            }
            arg0->unk15 = 2;
            return;
        }
        arg0->unk14 += 1;
    }
}

void func_10009BE4(struct54 *arg0) {
    register volatile struct147 *manager;
    struct54 *next;
    struct54 *previous;
    struct54 *free;
    struct54 *free_head;
    struct54 *free_next;
    u32 *release;

    manager = &D_800406A0;

    if (((s32)arg0 & 1) != 0) {
        D_8003C8E0 = 0x0F000004;
        func_150AD770();
        return;
    }

    release = (u32 *)arg0->unkC;
    *release = arg0->unk8;
    if (arg0 == (struct54 *)manager->unk4) {
        D_800406A4 = arg0->unk0;
    }
    next = arg0->unk0;
    if (next != NULL) {
        next->unk4 = arg0->unk4;
    }
    previous = arg0->unk4;
    if (previous != NULL) {
        previous->unk0 = arg0->unk0;
    }

    free = manager->unk10;
    if (free != NULL) {
        arg0->unk4 = free;
        free_head = free;
        arg0->unk0 = free->unk0;
        free_next = free->unk0;
        if (free_next != NULL) {
            free_next->unk4 = arg0;
            free_head->unk0 = arg0;
        } else {
            free_head->unk0 = arg0;
        }
    } else {
        D_800406B0 = arg0;
        arg0->unk0 = NULL;
        arg0->unk4 = NULL;
    }
}
// void func_10009BE4(struct00 *arg0) {
//     struct00 *temp_a1;
//     struct00 *temp_v0;
//     struct00 *temp_v1;
//
//     if (((s32)arg0 & 1) != 0) {
//         D_8003C8E0 = 0x0F000004;
//         func_150AD770(); // 0x80040000
//         return;
//     }
//     arg0->unkC = (s32) arg0->unk8;
//     if ((s32)arg0 == D_800406A0.unk4) {
//         D_800406A4 = (struct54 *) arg0->unk0;
//     }
//     temp_v0 = arg0->unk0;
//     if (temp_v0 != 0) {
//         temp_v0->unk4 = (struct54 *) arg0->unk4;
//     }
//     temp_v0 = arg0->unk4;
//     if (temp_v0 != 0) {
//         temp_v0 = (struct54 *) arg0->unk0;
//     }
//     temp_v1 = D_800406A0.unk10;
//     if (temp_v1 != 0) {
//         arg0->unk4 = temp_v1;
//         arg0->unk0 = (struct54 *) &temp_v1;
//         temp_a1 = &temp_v1;
//         if (temp_a1 != 0) {
//             temp_a1->unk4 = arg0;
//         }
//         temp_v1 = arg0;
//         return;
//     }
//     D_800406B0 = arg0;
//     arg0->unk0 = NULL;
//     arg0->unk4 = NULL;
//     // return temp_v0;
// }

/* Non-matching C placeholders for asm/nonmatchings/init_8F90/func_10009CBC.s. */
s32 func_10009CBC(void *arg0, s32 arg1) {
    return 0;
}

s32 func_10009FFC(void) {
    if (D_800406A0.unk0 == 0) {
        D_800406A0.unk4 = NULL;
        D_800406A0.unk8 = &D_80040AC8;
        D_800406A0.unkC = 0;
        D_800406A0.unk10 = NULL;
        D_800406A0.unk0 = (u8)1U;
    }
    return func_10009CBC;
}

/* Non-matching C placeholders for asm/nonmatchings/init_8F90/func_1000A03C.s. */
s32 func_1000A03C() {
    return 0;
}
void func_1000A348(void) {
    struct54 *current;
    struct54 *next;
    struct54 *free;
    struct54 *free_head;
    struct54 *free_next;
    u32 *release;

    current = (struct54 *)D_800406A0.unk4;
    while (current != NULL) {
        next = current->unk0;
        if ((current->unk14 == 0) && (current->unk16 == 0)) {
            release = (u32 *)current->unkC;
            *release = current->unk8;
            current->unkC = 0;

            if (current == (struct54 *)D_800406A0.unk4) {
                D_800406A0.unk4 = (s32)next;
            }
            if (current->unk0 != NULL) {
                current->unk0->unk4 = current->unk4;
            }
            if (current->unk4 != NULL) {
                current->unk4->unk0 = current->unk0;
            }

            free = D_800406A0.unk10;
            if (free != NULL) {
                current->unk4 = free;
                free_head = free;
                current->unk0 = free->unk0;
                free_next = free->unk0;
                if (free_next == NULL) {
                    free_head->unk0 = current;
                } else {
                    free_next->unk4 = current;
                    free_head->unk0 = current;
                }
            } else {
                D_800406A0.unk10 = current;
                current->unk0 = NULL;
                current->unk4 = NULL;
            }
        }
        current = next;
    }
}
