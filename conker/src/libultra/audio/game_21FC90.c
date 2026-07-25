#include <n_libaudio.h>

/* Generated placeholder declarations. */
void func_151F2BE8();
void func_151F2C4C();
s32 func_151F2CDC();
void func_151F2D6C();
s32 func_151F2E88();
void func_151F39E4();
s32 func_151F3D78();
/* End generated placeholder declarations. */

extern s32  D_800E0E00;
extern s32  D_800E0E04;
extern s32  D_800E0E08;
extern s32  D_800E0E10;
extern s16  D_800E0E14;
extern s16  D_800E0E16;
extern u8   D_800E0E18;
extern u8   D_800E0E2C;
extern s32  D_800E0E20;
extern s32  D_800E0E24;
extern s32  D_800E0E28;
extern s32  *D_800E0E30; // 0x8000
extern s32  D_800E0D80; // libaudio struct?
extern s16  D_800E0DB0;
extern s16  D_800E0DB2;
extern s32  D_800E0DD8;
extern s32  D_800E0DE0;
extern s32  D_800E0DE4;
extern s32  D_800E0DFC;
extern s16  D_8002BC10[];
extern s16  D_8002BD0E[];
extern u8   D_800428C1;
extern u8   D_800428C2;
extern s32  D_800BE9F0;
extern s32  D_800E0D84;
extern s32  D_800E0D88;
extern s16  D_800E0D8C;
extern s16  D_800E0D8E;
extern s16  D_800E0D90;
extern s16  D_800E0D92;
extern s16  D_800E0D94;
extern s16  D_800E0D96;
extern u16  D_800E0D98;
extern s16  D_800E0D9A;
extern s16  D_800E0D9C;
extern u16  D_800E0D9E;
extern s16  D_800E0DA0;
extern s16  D_800E0DA2;
extern s16  D_800E0DA4;
extern s32  D_800E0DA8;
extern s32  D_800E0DAC;
extern s32  D_800E0DDC;
extern s32  D_800E0DE8;
extern s32  D_800E0DEC;
extern s32  D_800E0DF0;
extern s32  D_800E0DF4[];
extern s32  D_800E0DF8;
extern u8   D_800E0E19;


void func_151F2960(s32 arg0, s32 arg1) {
    if (D_800E0DFC == 0) {
        return;
    }
    D_800E0E04 = 4;
    if (D_800E0E2C == 0) {
      D_800E0E2C = 1;
        D_800E0E30 = allocate_memory(0x8000, 0xFF, 2, 1);
        if (D_800E0E30 == 0) {
            D_800E0E2C = 0;
            return;
        }
        D_800E0E20 = func_1502B5C8(0, 2, 0x17, 4);
        if (D_800E0E20 != 0) {
            func_100043B4(D_800E0E20, 0xFF);
        }
        D_800E0E24 = func_1502B5C8(0, 2, 0x17, 5);
        if (D_800E0E24 != 0) {
            func_100043B4(D_800E0E24, 0xFF);
        }
        D_800E0E28 = func_1502B5C8(0, 2, 0x17, 6);
        if (D_800E0E28 != 0) {
            func_100043B4(D_800E0E28, 0xFF);
        }
        if ((D_800E0E20 == 0) || (D_800E0E24 == 0) || (D_800E0E28 == 0)) {
            if (D_800E0E20 != 0) {
                func_10004074(D_800E0E20);
            }
            if (D_800E0E24 != 0) {
                func_10004074(D_800E0E24);
            }
            if (D_800E0E28 != 0) {
                func_10004074(D_800E0E28);
            }
            func_10004074(D_800E0E30);
            D_800E0E30 = 0;
            D_800E0E2C = 0;
            return;
        }
        func_151F3DE0();
    }
    D_800E0D80 = arg0;
    D_800E0DE0 = arg1;
    D_800E0DE4 = 0;
    D_800E0E10 = 0;
    D_800E0E18 = 5;
    D_800E0E04 = 5;
}

void func_151F2BA8(void) {
    u32 mask = osSetIntMask(1);
    D_800E0E04 = 3;
    osSetIntMask(mask);
}

void func_151F2BE8(void) {
    u32 mask = osSetIntMask(1);
    if (D_800E0E04 == 5) {
        D_800E0E04 = 6;
    } else {
        D_800E0E04 = 2;
    }
    osSetIntMask(mask);
}

void func_151F2C4C(void) {
    u32 mask = osSetIntMask(1);
    if (D_800E0E04 == 2) {
        D_800E0E18 = 5;
        D_800E0E04 = 7;
    } else if (D_800E0E04 == 6) {
        D_800E0E18 = 5;
        D_800E0E04 = 5;
    }
    osSetIntMask(mask);
}

s32 func_151F2CDC(void) {
    s32 ret = 0;
    u32 mask = osSetIntMask(1);
    if ((D_800E0E04 == 1) || (D_800E0E04 == 5) || (D_800E0E04 == 6) || (D_800E0E04 == 7) || (D_800E0E04 == 2)) {
        ret = D_800E0E04;
    }
    osSetIntMask(mask);
    return ret;
}

void func_151F2D6C(s32 arg0, s32 arg1) {
    u32 mask = osSetIntMask(1);
    if (arg0 < 0) {
        D_800E0E08 = 0;
    } else if (arg0 >= 0x8000) {
        D_800E0E08 = 0x7FFF;
    } else {
        D_800E0E08 = arg0;
    }
    D_800E0E10 = arg1;
    osSetIntMask(mask);
}

void func_151F2DFC(s32 arg0, s32 arg1) {
    if (arg0 >= 0x80) {
        arg0 = (u16)0x7F;
    } else {
        if (arg0 < 0) {
            arg0 = (u16)0;
        }
    }
    D_800E0E16 = arg0;
    if (arg1 != 0) {
        D_800E0E14 = (s16) D_800E0E16;
    }
}

void func_151F2E4C(s32 arg0, s32 arg1) {
    D_800E0DB2 = arg0;
    D_800E0DB0 = arg1;
    if (D_800E0DD8 == 0) {
        D_800E0DD8 = 2;
    }
}

s32 func_151F2E88(s32 arg0, s32 *arg1) {
    s32 delta;
    s32 seg1Size;
    s32 seg2Size;
    s32 buf2Addr;
    s32 buf2Len;
    s32 dmaAddr;
    s32 dmaCount;
    s32 j;
    s32 *cur;

    buf2Addr = 0;
    dmaCount = 0;
    seg1Size = 0x4E0;
    seg2Size = 0x650;

    if (D_800E0E14 != D_800E0E16) {
        delta = D_800E0E16 - D_800E0E14;
        if (delta < -2) {
            D_800E0E14 -= 2;
        } else if (delta < 3) {
            D_800E0E14 += delta;
        } else {
            D_800E0E14 += 2;
        }
    }

    if (D_800E0E04 == 5) {
        func_151F3D78();
        if (D_800E0E18 != 0) {
            D_800E0E18 -= 1;
        } else {
            D_800E0D84 = func_151F85C4(0, D_800E0DFC, D_800E0DE0);
            if (D_800E0D84 == 0) {
                D_800E0DE4 = 0;
                D_800E0E10 = 0;
                D_800E0E18 = 5;
                func_151F3D78();
                D_800E0E04 = 5;
                return 0;
            }
            D_800E0E04 = 1;
            D_800E0DA4 = 1;
            D_800E0DE8 = 0;
            D_800E0DEC = 0;
            D_800E0DF0 = 0;
            D_800E0DF8 = 0;
            bzero(*(void **) ((u8 *) &D_800E0D80 + 0x74), 0x440);
        }
    }

    if (D_800E0E04 == 7) {
        func_151F3D78();
        if (D_800E0E18 == 0) {
            D_800E0E04 = 1;
        } else {
            D_800E0E18 -= 1;
        }
    }

    if (D_800E0E04 == 1) {
        if (D_800E0DEC < (arg0 + D_800E0DF0)) {
            D_800E0DEC -= D_800E0DF0;
            if ((D_800E0DEC != 0) && (D_800E0DE8 != 0)) {
                buf2Addr = (D_800E0DF0 << 1) + D_800E0DE8;
                buf2Len = D_800E0DEC;
            }
            D_800E0DF0 = 0;
            D_800E0DEC = 0;
            if (func_151F86B0(D_800E0D84, &dmaAddr, &dmaCount) != 0) {
                D_800E0DE8 = dmaAddr;
                j = 0;
                if (dmaCount > 0) {
                    do {
                        cur = (s32 *) *arg1;
                        *arg1 = (s32) (cur + 2);
                        cur[0] = 0x08000000;
                        cur[1] = osVirtualToPhysical((void *) D_800E0DF4[j]);
                        cur = (s32 *) *arg1;
                        *arg1 = (s32) (cur + 2);
                        cur[0] = 0x07000000 | (D_800E0DF8 & 0xFFFF);
                        cur[1] = osVirtualToPhysical((void *) dmaAddr);
                        dmaAddr += 0x488;
                        j++;
                    } while (j < dmaCount);
                }
                D_800E0DF8 = (D_800E0DF8 - 0x24) & 0x1E;
                D_800E0DEC = 0x240;
                D_800E0E19 = (dmaCount == 2);
            }
        }

        func_151F3D78();
        if (D_800E0E19 == 0) {
            seg1Size = 0;
        }
        if (buf2Addr != 0) {
            cur = (s32 *) *arg1;
            *arg1 = (s32) (cur + 2);
            cur[0] = 0x04000000 | (((buf2Addr << 1) & 0xFFF) << 12) | (seg1Size & 0xFFF);
            cur[1] = osVirtualToPhysical((void *) buf2Addr);
            if (D_800E0E19 != 0) {
                buf2Addr += 0x488;
                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x04000000 | (((buf2Len << 1) & 0xFFF) << 12) | (seg2Size & 0xFFF);
                cur[1] = osVirtualToPhysical((void *) buf2Addr);
            }
            seg1Size += buf2Len << 1;
            seg2Size += buf2Len << 1;
            arg0 -= buf2Len;
        }

        if ((arg0 > 0) && (D_800E0DE8 != 0)) {
            buf2Addr = (D_800E0DF0 << 1) + D_800E0DE8;
            cur = (s32 *) *arg1;
            *arg1 = (s32) (cur + 2);
            cur[0] = 0x04000000 | (((arg0 << 1) & 0xFFF) << 12) | (seg1Size & 0xFFF);
            cur[1] = osVirtualToPhysical((void *) buf2Addr);
            if (D_800E0E19 != 0) {
                buf2Addr += 0x488;
                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x04000000 | (((arg0 << 1) & 0xFFF) << 12) | (seg2Size & 0xFFF);
                cur[1] = osVirtualToPhysical((void *) buf2Addr);
            }
            D_800E0DF0 += arg0;
        }

        func_151F39E4((u8 *) &D_800E0D80);
        if (D_800E0E19 == 0) {
            cur = (s32 *) *arg1;
            *arg1 = (s32) (cur + 2);
            cur[0] = 0x020004E0;
            cur[1] = 0x2E0;
            cur = (s32 *) *arg1;
            *arg1 = (s32) (cur + 2);
            cur[0] = 0x020007C0;
            cur[1] = 0x2E0;

            if (D_800E0DB2 > 0) {
                if (D_800E0DD8 != 0) {
                    func_1001CF38((u8 *) &D_800E0D80 + 0x30, 0x46AC0800);
                }
                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x0B000020;
                cur[1] = osVirtualToPhysical((u8 *) &D_800E0D80 + 0x38) & 0xFFFFFF;
                if (D_800E0DD8 == 2) {
                    D_800E0DD8 = 0;
                }
                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x0E000000 | ((D_800E0DD8 & 0xFF) << 16);
                cur[1] = osVirtualToPhysical((void *) D_800E0DDC) & 0xFFFFFF;
                D_800E0DD8 = 0;
            }

            if (D_800E0DA4 != 0) {
                D_800E0DA4 = 0;
                D_800E0D9C = (D_8002BC10[D_800E0D8C] * D_800E0D8E) >> 15;
                D_800E0D9A = _getRate((f32) D_800E0D90, (f32) D_800E0D9C, D_800E0DAC, &D_800E0D98);
                D_800E0DA2 = (D_8002BD0E[-D_800E0D8C] * D_800E0D8E) >> 15;
                D_800E0DA0 = _getRate((f32) D_800E0D92, (f32) D_800E0DA2, D_800E0DAC, &D_800E0D9E);

                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x09060000 | (D_800E0D90 & 0xFFFF);
                cur[1] = ((D_800E0D94 & 0xFFFF) << 16) | (D_800E0D96 & 0xFFFF);

                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x09040000 | (D_800E0DA2 & 0xFFFF);
                cur[1] = ((D_800E0DA0 & 0xFFFF) << 16) | (D_800E0D9E & 0xFFFF);

                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x09000000 | (D_800E0D9C & 0xFFFF);
                cur[1] = ((D_800E0D9A & 0xFFFF) << 16) | (D_800E0D98 & 0xFFFF);

                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x03010000 | (D_800E0D92 & 0xFFFF);
                cur[1] = osVirtualToPhysical((void *) D_800E0D88);
            } else {
                cur = (s32 *) *arg1;
                *arg1 = (s32) (cur + 2);
                cur[0] = 0x03000000;
                cur[1] = osVirtualToPhysical((void *) D_800E0D88);
            }

            D_800E0DA8 += 0xB8;
            if (D_800E0DAC < D_800E0DA8) {
                D_800E0DA8 = D_800E0DAC;
            }
        }
        return 1;
    } else if (D_800E0E04 == 3) {
        if (D_800BE9F0 != 0x35) {
            if (D_800E0E2C != 0) {
                func_10004074(D_800E0E20);
                func_10004074(D_800E0E24);
                func_10004074(D_800E0E28);
                D_800E0E2C = 0;
            }
            if (D_800E0E30 != 0) {
                func_10004074(D_800E0E30);
                D_800E0E30 = 0;
            }
            D_800E0E04 = 0;
        }
        return 0;
    }
    return 0;
}

void func_151F39E4(u8 *arg0) {
    if ((*(s16 *)(arg0 + 0xE) != *(s32 *)(arg0 + 0x88)) || (*(s16 *)(arg0 + 0xC) != *(s16 *)(arg0 + 0x94))) {
        if (*(s32 *)(arg0 + 0x28) < *(s32 *)(arg0 + 0x2C)) {
            *(s16 *)(arg0 + 0x1C) = (D_8002BC10[*(s16 *)(arg0 + 0xC)] * *(s16 *)(arg0 + 0xE)) >> 15;
            *(s16 *)(arg0 + 0x22) = (D_8002BD0E[-*(s16 *)(arg0 + 0xC)] * *(s16 *)(arg0 + 0xE)) >> 15;
            *(s32 *)(arg0 + 0x28) = *(s32 *)(arg0 + 0x2C);
            *(s16 *)(arg0 + 0x10) = *(s16 *)(arg0 + 0x1C);
            *(s16 *)(arg0 + 0x12) = *(s16 *)(arg0 + 0x22);
        } else {
            *(s16 *)(arg0 + 0x10) = _getVol(*(s16 *)(arg0 + 0x10), *(s32 *)(arg0 + 0x28), *(s16 *)(arg0 + 0x1A), *(u16 *)(arg0 + 0x18));
            *(s16 *)(arg0 + 0x12) = _getVol(*(s16 *)(arg0 + 0x12), *(s32 *)(arg0 + 0x28), *(s16 *)(arg0 + 0x20), *(u16 *)(arg0 + 0x1E));
        }
        if (*(s16 *)(arg0 + 0x10) == 0) {
            *(s16 *)(arg0 + 0x10) = 1;
        }
        if (*(s16 *)(arg0 + 0x12) == 0) {
            *(s16 *)(arg0 + 0x12) = 1;
        }
        *(s16 *)(arg0 + 0xE) = (s16) *(s32 *)(arg0 + 0x88);
        if ((*(s16 *)(arg0 + 0xE) == 0) && (*(s32 *)(arg0 + 0x90) != 0)) {
            func_151F2BA8();
        }
        if (*(s16 *)(arg0 + 0xC) != *(s16 *)(arg0 + 0x94)) {
            if (D_800428C2 != 0) {
                *(s16 *)(arg0 + 0xC) = (*(s16 *)(arg0 + 0x94) >> 1) + 0x20;
            } else if (D_800428C1 != 0) {
                *(s16 *)(arg0 + 0xC) = 0x40;
            } else {
                *(s16 *)(arg0 + 0xC) = *(s16 *)(arg0 + 0x94);
            }
        }
        *(s32 *)(arg0 + 0x28) = 0;
        *(s32 *)(arg0 + 0x2C) = ((u32) (*(s32 *)(arg0 + 0x90) + 0xB7) / 184) * 0xB8;
        *(s16 *)(arg0 + 0x24) = 1;
    }
}

void func_151F3C1C(s32 arg0) {
    D_800E0E00 = arg0;
}

void func_151F3C34(s32 arg0) {
    D_800E0DFC = arg0;
}

s32 func_151F3C4C(s32 arg0, u8 *arg1, s32 arg2, s32 arg3) {
    s32 state;
    ALDMAproc dmaProc;
    s32 ret;

    if (arg3 != -1) {
        D_800E0DE4 = arg3;
    }
    if (D_800E0DE0 < (D_800E0DE4 + arg2)) {
        arg2 = D_800E0DE0 - D_800E0DE4;
    }
    dmaProc = n_syn->dma(&state);
    ret = dmaProc(D_800E0D80 + D_800E0DE4, arg2, 0);
    if (ret == 0) {
        return 0;
    }
    ret += 0x80000000;
    osInvalDCache((void *) ret, arg2);
    bcopy((void *) ret, arg1, arg2);
    D_800E0DE4 += arg2;
    return arg2;
}

/* Non-matching C placeholders for asm/nonmatchings/libultra/audio/game_21FC90/func_151F3D78.s. */
s32 func_151F3D78() {
    return 0;
}
