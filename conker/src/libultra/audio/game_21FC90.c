#include <n_libaudio.h>

void func_151F39E4(void *arg0);

void *func_1502B5C8(s32 *size, u32 depth, ...);

typedef struct { u32 w0; u32 w1; } StreamAudioCommand;
s16 _getVol();
s16 _getRate(f32, f32, s32, void *);
void *func_151F85C4(s32, s32, s32);
s32 func_151F86B0();

/* Generated placeholder declarations. */
void func_151F2BE8();
void func_151F2C4C();
s32 func_151F2CDC();
void func_151F2D6C();
void func_151F3D78();
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
        D_800E0E20 = (s32)func_1502B5C8(0, 2, 0x17, 4);
        if (D_800E0E20 != 0) {
            func_100043B4(D_800E0E20, 0xFF);
        }
        D_800E0E24 = (s32)func_1502B5C8(0, 2, 0x17, 5);
        if (D_800E0E24 != 0) {
            func_100043B4(D_800E0E24, 0xFF);
        }
        D_800E0E28 = (s32)func_1502B5C8(0, 2, 0x17, 6);
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

/* Advance the stream state and emit audio commands for the requested samples. */
s32 func_151F2E88(s32 arg0, StreamAudioCommand **arg1) {
    s32 i;
    s32 delta;
    s32 nbuf;
    void *pbuf;
    void *src;
    s32 len;
    s32 outL;
    s32 outR;

    nbuf = 0;
    src = 0;
    outL = 0x4E0;
    outR = 0x650;

    if (D_800E0E14 != D_800E0E16) {
        delta = D_800E0E16 - D_800E0E14;
        if (delta >= -2 && delta < 3) {
            D_800E0E14 = D_800E0E14 + delta;
        } else if (delta >= 3) {
            D_800E0E14 = D_800E0E14 + 2;
        } else {
            D_800E0E14 = D_800E0E14 - 2;
        }
    }

    if (D_800E0E04 == 5) {
        func_151F3D78();
        if (D_800E0E18 == 0) {
            D_800E0D84 = (s32)func_151F85C4(0, D_800E0DFC, D_800E0DE0);
            if (D_800E0D84 == 0) {
                D_800E0DE4 = 0;
                D_800E0E10 = 0;
                D_800E0E18 = 5;
                func_151F3D78();
                D_800E0E04 = 5;
                return 0;
            } else {
                D_800E0E04 = 1;
                D_800E0DA4 = 1;
                D_800E0DE8 = 0;
                D_800E0DEC = 0;
                D_800E0DF0 = 0;
                D_800E0DF8 = 0;
                bzero(*(void **) ((char *) &D_800E0D80 + 0x74), 0x440);
            }
        } else {
            D_800E0E18 = D_800E0E18 - 1;
        }
    }

    if (D_800E0E04 == 7) {
        func_151F3D78();
        if (D_800E0E18 == 0) {
            D_800E0E04 = 1;
        } else {
            D_800E0E18 = D_800E0E18 - 1;
        }
    }

    if (D_800E0E04 == 1) {
        if (arg0 + D_800E0DF0 > D_800E0DEC) {
            D_800E0DEC = D_800E0DEC - D_800E0DF0;
            if (D_800E0DEC != 0 && D_800E0DE8 != 0) {
                src = (void *) (D_800E0DF0 * 2 + D_800E0DE8);
                len = D_800E0DEC;
            }
            D_800E0DF0 = 0;
            D_800E0DEC = 0;
            if (func_151F86B0(D_800E0D84, &pbuf, &nbuf) != 0) {
                D_800E0DE8 = (s32) pbuf;
                for (i = 0; i < nbuf; i++) {
                    {
                        StreamAudioCommand *a = (*arg1)++;
                        a->w0 = 0x8000000;
                        a->w1 = osVirtualToPhysical((void *) D_800E0DF4[i]);
                    }
                    {
                        StreamAudioCommand *a = (*arg1)++;
                        a->w0 = (D_800E0DF8 & 0xFFFF) | 0x7000000;
                        a->w1 = osVirtualToPhysical(pbuf);
                    }
                    pbuf = (char *) pbuf + 0x488;
                }
                D_800E0DF8 = (D_800E0DF8 - 0x24) & 0x1E;
                D_800E0DEC = 0x240;
                D_800E0E19 = nbuf == 2;
            } else {
            }
        }

        func_151F3D78();
        if (D_800E0E19 == 0) {
            outL = 0;
        }

        if (src != 0) {
            {
                StreamAudioCommand *a = (*arg1)++;
                a->w0 = (((len + len) & 0xFFF) << 12 | 0x4000000) | (outL & 0xFFF);
                a->w1 = osVirtualToPhysical(src);
            }
            if (D_800E0E19 != 0) {
                src = (char *) src + 0x488;
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = (((len + len) & 0xFFF) << 12 | 0x4000000) | (outR & 0xFFF);
                    a->w1 = osVirtualToPhysical(src);
                }
            }
            outL += len + len;
            outR += len + len;
            arg0 = arg0 - len;
        }

        if (arg0 > 0 && D_800E0DE8 != 0) {
            src = (void *) (D_800E0DF0 * 2 + D_800E0DE8);
            {
                StreamAudioCommand *a = (*arg1)++;
                a->w0 = (((arg0 + arg0) & 0xFFF) << 12 | 0x4000000) | (outL & 0xFFF);
                a->w1 = osVirtualToPhysical(src);
            }
            if (D_800E0E19 != 0) {
                src = (char *) src + 0x488;
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = (((arg0 + arg0) & 0xFFF) << 12 | 0x4000000) | (outR & 0xFFF);
                    a->w1 = osVirtualToPhysical(src);
                }
            }
            D_800E0DF0 = D_800E0DF0 + arg0;
        }

        func_151F39E4(&D_800E0D80);

        if (D_800E0E19 == 0) {
            {
                StreamAudioCommand *a = (*arg1)++;
                a->w0 = 0x20004E0;
                a->w1 = 0x2E0;
            }
            {
                StreamAudioCommand *a = (*arg1)++;
                a->w0 = 0x20007C0;
                a->w1 = 0x2E0;
            }

            if (D_800E0DB2 > 0) {
                if (D_800E0DD8 != 0) {
                    func_1001CF38((char *) &D_800E0D80 + 0x30, 0x46AC0800);
                }
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = 0xB000020;
                    a->w1 = osVirtualToPhysical((char *) &D_800E0D80 + 0x38) & 0xFFFFFF;
                }
                if (D_800E0DD8 == 2) {
                    D_800E0DD8 = 0;
                }
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = ((D_800E0DD8 & 0xFF) << 16) | 0xE000000;
                    a->w1 = (osVirtualToPhysical((void *) D_800E0DDC) & 0xFFFFFF) & 0xFFFFFF;
                }
                D_800E0DD8 = 0;
            }

            if (D_800E0DA4 != 0) {
                D_800E0DA4 = 0;
                D_800E0D9C = (D_8002BC10[D_800E0D8C] * D_800E0D8E) >> 15;
                D_800E0D9A = _getRate((f32) D_800E0D90, (f32) D_800E0D9C, D_800E0DAC,
                                      (char *) &D_800E0D80 + 0x18);
                D_800E0DA2 = (D_8002BD0E[-D_800E0D8C] * D_800E0D8E) >> 15;
                D_800E0DA0 = _getRate((f32) D_800E0D92, (f32) D_800E0DA2, D_800E0DAC,
                                      (char *) &D_800E0D80 + 0x1E);
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = (D_800E0D90 & 0xFFFF) | 0x9060000;
                    a->w1 = ((D_800E0D94 & 0xFFFF) << 16) | (D_800E0D96 & 0xFFFF);
                }
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = (D_800E0DA2 & 0xFFFF) | 0x9040000;
                    a->w1 = ((D_800E0DA0 & 0xFFFF) << 16) | (D_800E0D9E & 0xFFFF);
                }
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = (D_800E0D9C & 0xFFFF) | 0x9000000;
                    a->w1 = ((D_800E0D9A & 0xFFFF) << 16) | (D_800E0D98 & 0xFFFF);
                }
                {
                    StreamAudioCommand *a = (*arg1)++;
                    a->w0 = (D_800E0D92 & 0xFFFF) | 0x3010000;
                    a->w1 = osVirtualToPhysical((void *) D_800E0D88);
                }
            } else {
                StreamAudioCommand *a = (*arg1)++;
                a->w0 = 0x3000000;
                a->w1 = osVirtualToPhysical((void *) D_800E0D88);
            }

            D_800E0DA8 = D_800E0DA8 + 0xB8;
            if (D_800E0DA8 > D_800E0DAC) {
                D_800E0DA8 = D_800E0DAC;
            }
        }
    } else if (D_800E0E04 == 3 && D_800BE9F0 != 0x35) {
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
        return 0;
    } else {
        return 0;
    }
    return 1;
}

/* Update the stream volume and pan ramp, honoring output mode overrides. */
void func_151F39E4(void *arg0) {
    if (*(s32 *) ((char *) arg0 + 0x88) != *(s16 *) ((char *) arg0 + 0xE) ||
        *(s16 *) ((char *) arg0 + 0x94) != *(s16 *) ((char *) arg0 + 0xC)) {
        if (*(s32 *) ((char *) arg0 + 0x28) >= *(s32 *) ((char *) arg0 + 0x2C)) {
            *(s16 *) ((char *) arg0 + 0x1C) =
                (*(s16 *) ((char *) arg0 + 0xE) * D_8002BC10[*(s16 *) ((char *) arg0 + 0xC)]) >> 15;
            *(s16 *) ((char *) arg0 + 0x22) =
                (*(s16 *) ((char *) arg0 + 0xE) * D_8002BD0E[-*(s16 *) ((char *) arg0 + 0xC)]) >> 15;
            *(s32 *) ((char *) arg0 + 0x28) = *(s32 *) ((char *) arg0 + 0x2C);
            *(s16 *) ((char *) arg0 + 0x10) = *(s16 *) ((char *) arg0 + 0x1C);
            *(s16 *) ((char *) arg0 + 0x12) = *(s16 *) ((char *) arg0 + 0x22);
        } else {
            *(s16 *) ((char *) arg0 + 0x10) =
                _getVol(*(s16 *) ((char *) arg0 + 0x10), *(s32 *) ((char *) arg0 + 0x28),
                        *(s16 *) ((char *) arg0 + 0x1A), *(u16 *) ((char *) arg0 + 0x18));
            *(s16 *) ((char *) arg0 + 0x12) =
                _getVol(*(s16 *) ((char *) arg0 + 0x12), *(s32 *) ((char *) arg0 + 0x28),
                        *(s16 *) ((char *) arg0 + 0x20), *(u16 *) ((char *) arg0 + 0x1E));
        }

        if (*(s16 *) ((char *) arg0 + 0x10) == 0) {
            *(s16 *) ((char *) arg0 + 0x10) = 1;
        }
        if (*(s16 *) ((char *) arg0 + 0x12) == 0) {
            *(s16 *) ((char *) arg0 + 0x12) = 1;
        }

        *(s16 *) ((char *) arg0 + 0xE) = *(s32 *) ((char *) arg0 + 0x88);
        if (*(s16 *) ((char *) arg0 + 0xE) == 0 && *(s32 *) ((char *) arg0 + 0x90) != 0) {
            func_151F2BA8();
        }

        if (*(s16 *) ((char *) arg0 + 0x94) != *(s16 *) ((char *) arg0 + 0xC)) {
            if (D_800428C2 != 0) {
                *(s16 *) ((char *) arg0 + 0xC) = (*(s16 *) ((char *) arg0 + 0x94) >> 1) + 0x20;
            } else if (D_800428C1 != 0) {
                *(s16 *) ((char *) arg0 + 0xC) = 0x40;
            } else {
                *(s16 *) ((char *) arg0 + 0xC) = *(s16 *) ((char *) arg0 + 0x94);
            }
        }

        *(s32 *) ((char *) arg0 + 0x28) = 0;
        *(s32 *) ((char *) arg0 + 0x2C) = (*(u32 *) ((char *) arg0 + 0x90) + 0xB7) / 0xB8 * 0xB8;
        *(s16 *) ((char *) arg0 + 0x24) = 1;
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

    if (arg3 != -1) {
        D_800E0DE4 = arg3;
    }
    if (D_800E0DE0 < (D_800E0DE4 + arg2)) {
        arg2 = D_800E0DE0 - D_800E0DE4;
    }
    dmaProc = n_syn->dma(&state);
    state = dmaProc(D_800E0D80 + D_800E0DE4, arg2, 0);
    if (state == 0) {
        return 0;
    }
    state += 0x80000000;
    osInvalDCache((void *) state, arg2);
    bcopy((void *) state, arg1, arg2);
    D_800E0DE4 += arg2;
    return arg2;
}

void func_151F3D78(void) {
    s32 state;
    ALDMAproc dmaProc;

    dmaProc = n_syn->dma(&state);
    dmaProc(D_800E0D80 + D_800E0DE4, 0x810, 0);
}
