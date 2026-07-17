#include <ultra64.h>
#include "string.h"

#include "functions.h"
#include "variables.h"


void func_16000000(void) {
    func_160012B0(278, &D_160046AC);
}

s32 func_16000028(void) {
    if (D_16003890 & 0xC000) {
        D_16003AF4 = 1;
        return 3;
    }
    return 0;
}

void func_16000058(void) {
    s32 i;
    s32 phi_s2;

    func_16001338(255, 255, 255);
    func_160012B0(44, &D_160046D0); // "MAIN MENU"
    phi_s2 = 108;
    for(i = 0; i < 2; i++) {
        if (D_16003B1C == i) {
            func_16001338(255, 0, 0);     // red
        } else {
            func_16001338(255, 255, 255); // white
        }
        func_160012B0(phi_s2, D_16003B20[i]);
        phi_s2 += 32;
    }
    if (D_16003B1C == 2) {
        func_16001338(255, 0, 0);     // red
    } else {
        func_16001338(255, 255, 255); // white
    }
    if (D_16003AF0 != 0) {
        if ((D_1600389C->unk120 == 32) && (D_160038A4 == 0)) {
            func_160012B0(phi_s2, &D_160046DC);
        } else if (D_16003AF0 != 0) {
            func_160012B0(phi_s2, &D_160046E8);
        }
    } else {
        func_160012B0(phi_s2, &D_160046F4); // "RETRY CODE"
    }
    func_16001338(255, 255, 255);
    func_160012B0(611, &D_16004700); // "Version"
    func_16001044(619, 1, 163);
    func_160012B0(643, &D_16004708); // "Built"
    func_160012B0(651, &D_16004710); // "Dec 19 2000"
    func_160012B0(663, &D_1600471C); // "09:57:42"
}

s32 func_16000224(void) {
    s32 res = 0;

    if (D_16003890 & 0x40000) { // D_JPAD is 0x0400
        D_16003B1C -= 1;
        res = 1;
    }
    if (D_16003890 & 0x80000) { // U_JPAD is 0x0800
        D_16003B1C += 1;
        res = 1;
    }
    if (D_16003B1C >= 3) {
        D_16003B1C = 0;
    }
    if (D_16003B1C < 0) {
        D_16003B1C = 2;
    }
    if (D_16003890 & A_BUTTON) {
        switch(D_16003B1C) {
            case 0:
                res = 3;
                D_16003AF4 = 2;
                break;
            case 1:
                res = 3;
                D_16003AF4 = 3;
                break;
            case 2:
                res = 4;
                break;
        }
    }
    return res;
}

void func_16000304(void) {
}

void func_1600030C(void) {
}

void func_16000314(void) {
    switch(D_16003B28) {
        case 0:
            func_16000424(D_1600389C);
            func_160006CC(D_1600389C);
            break;
        case 1:
        case 2:
            func_16000590(D_1600389C);
            break;
    }
}

s32 func_16000384(void) {
    s32 res = 0;

    if (D_16003890 & (R_CBUTTONS | D_CBUTTONS)) {
        D_16003B28 += 1;
        if (D_16003B28 >= 3) {
            D_16003B28 = 0;
        }
        return 3;
    }
    if (D_16003890 & (L_CBUTTONS | U_CBUTTONS)) {
        D_16003B28 -= 1;
        if (D_16003B28 < 0) {
            D_16003B28 = 2;
        }
        return 3;
    }
    if (D_16003890 & B_BUTTON) {
        D_16003AF4 = 1;
        res = 3;
    }
    return res;
}

void func_16000424(struct118 *arg0) {
    // TODO is this a RGB struct?
    u32 tmp0;
    u32 tmp1;
    s32 pad;

    func_16001338(255, 255, 255);
    func_160012B0(35, &D_16004728);     // "Pc"
    func_16001044(43, 0, arg0->unk11C);
    func_160012B0(67, &D_1600472C);     // "Cause"
    func_16001044(75, 0, arg0->unk120);
    func_16001338(128, 128, 255);
    tmp0 = arg0->unk120;
    tmp1 = (tmp0 >> 2) & 0xF;

    func_160012B0(107, D_16003848[tmp1]);
    if (tmp1 == 11) {
        func_16001044(111, 1, (tmp0 >> 28) & 3);
    }
    func_16001338(255, 255, 255);
    func_160012B0(131, &D_16004734);      // "Sr"
    func_16001044(139, 0, arg0->unk118);
    func_160012B0(163, &D_16004738);      // "Badvadr"
    func_16001044(171, 0, arg0->unk124);
    func_160012B0(195, &D_16004740);      // "Thread"
    func_16001044(203, 1, arg0->unk14);
    if (D_160038A4 != 0) {
        func_160012B0(52, &D_16004748);   // "Lockup_Now"
    }
}

// NON-MATCHING: one word short of retail, but converted for raw-progress accounting.
void func_16000590(void *arg0) {
    s32 s2 = *(s32 *) ((u8 *) arg0 + 0x12C);
    s32 bits;
    s32 pos = 0x2C;
    s32 i;
    s32 v0;
    s32 s4 = 0;
    s32 val;
    u8 *s3;

    func_160012B0(3, D_160047A4);
    func_16001044(0xA, 0, s2);

    bits = (u32) s2 >> 12;
    for (i = 0; i < 6; i++) {
        if (bits & 1) {
            func_160012B0(pos, D_16003B30[i]);
            pos += 0x20;
        }
        bits >>= 1;
    }

    if (D_16003B28 == 1) {
        pos = 0xC3;
        v0 = 0x4C;
    } else {
        v0 = 0x6C;
        s4 = 0x10;
    }
    val = s4;
    s3 = (u8 *) arg0 + v0 * 4;
    for (i = 0; i < 0x10; i++) {
        func_160012B0(pos, D_160047AC);
        func_16001044(pos + 2, 1, val);
        func_16001044(pos + 5, 2, *(s32 *) (s3 + 4));
        s3 += 8;
        pos += 0x20;
        val += 1;
    }
}

// NON-MATCHING: one word short of retail, but converted for raw-progress accounting.
void func_160006CC(void *arg0) {
    s32 sp3C = D_16003B48;
    u8 *label = (u8 *) &sp3C;
    u8 *entry = D_160037F0;
    s32 pos = 0x123;

    func_16001338(0xC0, 0xC0, 0xFF);
    label[0] = D_160037F0[0];
    do {
        label[1] = entry[1];
        func_160012B0(pos, label);
        pos += 3;
        func_16001044(pos, 0, ((s32 *) arg0)[entry[2] + 1]);
        pos += 0xD;
        label[0] = entry[3];
        entry += 3;
    } while (label[0] != 0);
}

// NON-MATCHING: close but still some stuff to figure out
void func_1600078C(void) {
    s32 temp_s0;
    u8 range_prefix;
    u32 temp_s2;
    s32 temp_s5;
    s32 phi_s1;
    u32 *phi_s2;
    u32 phi_s5;
    s32 i;

    temp_s0 = *(s32 *) ((u8 *) D_1600389C + 0xF4);
    func_16001338(0, 255, 0);
    func_160012B0(11, &D_160047B0);
    temp_s2 = (D_16003B4C * 4) + temp_s0;
    if (((temp_s2 & 3) == 0) && (temp_s2 >= 0x80000000U) && (temp_s2 < 0x80800001U)) {
        if (D_16003B4C == 0) {
            func_16001338(255, 0, 0);
            phi_s5 = (u32)&D_8002D4B0;
        } else {
            temp_s5 = (s32)&D_8002D4B0 - 0x2B50;
            if ((temp_s2 >= (u32)temp_s5) && (temp_s2 < (u32)(temp_s5 + 0x400))) {
                func_16001338(128, 128, 255);
                phi_s5 = temp_s5;
            } else if ((temp_s2 >= (u32) &D_8002D8B0) && (temp_s2 < ((u32)&D_8002D8B0 + 0x4000))) {
                func_16001338(255, 128, 128);
                phi_s5 = temp_s5;
            } else {
                func_16001338(255, 255, 255);
                phi_s5 = temp_s5;
            }
        }
        phi_s1 = 97;
        phi_s2 = (u32 *)temp_s2;
        for (i = 0; i < 22; i++) {
            func_16001044(phi_s1, 0, (s32)phi_s2);
            func_160012B0(phi_s1 + 8, &D_160047BC);
            range_prefix = (*phi_s2 >> 24);
            if (range_prefix == 0x80) {
                func_16001338(128, 128, 255);
            } else if (range_prefix == 0x15) {
                func_16001338(255, 0, 0);
            } else if (range_prefix == 0x16) {
                func_16001338(128, 255, 128);
            } else if (range_prefix == 0x10) {
                func_16001338(255, 0, 0);
            } else {
                func_16001338(255, 255, 255);
            }
            func_16001044(phi_s1 + 0xC, 0, *phi_s2);
            func_160012B0(phi_s1 + 0x16, &D_160047C0);
            func_16001338(255, 255, 255);
            func_16001044(phi_s1 + 0x16, 1, *phi_s2);
            if (((u32) phi_s2 >= phi_s5) && ((u32) phi_s2 < (phi_s5 + 0x400))) {
                func_16001338(128, 128, 0xFF);
            } else if (((u32) phi_s2 >= (u32) &D_8002D8B0) && ((u32) phi_s2 < ((u32)&D_8002D8B0 + 0x4000))) {
                func_16001338(255, 128, 128);
            } else {
                func_16001338(255, 255, 255);
            }
            phi_s1 += 0x20;
            phi_s2 += 1;
        }
    }
}

s32 func_16000A5C(void) {
    s32 res = 0;

    if ((D_160036F3 >= 41) || (D_16003890 & U_CBUTTONS)) {
        D_16003B4C -= 1;
        if (D_16003B4C < 0) {
            D_16003B4C = 0;
        } else {
            res = 3;
        }
    } else if ((D_160036F3 < -40) || (D_16003890 & D_CBUTTONS)) {
        D_16003B4C += 1;
        if (D_16003B4C >= 201) {
            D_16003B4C = 200;
        }
        res = 3;
    }
    if ((D_16003890 & B_BUTTON)) {
        D_16003AF4 = 1;
        res = 3;
    }
    return res;
}

// called from func_10007DAC
// NON-MATCHING: mips-to-c cleaned skeleton, converted for raw-progress accounting.
s32 func_16000B14(struct118 *arg0) {
    s32 firstPass = 1;
    s32 state = 0;
    s32 cur;
    s32 maskedPc;
    s32 hasOddPage;
    s32 tlbBase;
    s32 i;
    void (*drawFunc)(void);
    s32 (*inputFunc)(void);

    if (D_8002AC5C != 0) {
        return 0;
    }
    D_16003888 = 0;
    if ((D_8002AAE8[0] == 0) || (D_8002AAE8[1] == 0)) {
        D_8002AAE8[0] = 0x80350000;
        D_8002AAE8[1] = 0x80350000;
        return 0;
    }

    func_16003650();
    D_160038AC[15] = D_8003C8E8[0];
    D_1600392C[15] = D_8003C8E8[1];
    D_160039E8 = D_8003C8E8[2];
    D_16003A68 = D_8003C8E8[3];

    cur = arg0->unk11C;
    if ((cur & 0xFF000000) != 0x15000000) {
        D_16003AF0 = 1;
    } else {
        maskedPc = cur & ~0xFFF;
        hasOddPage = maskedPc & 0x1000;
        maskedPc &= ~0x1000;
        D_16003AF0 = 0;
        for (i = 0; i < 32; i += 4) {
            if ((maskedPc == D_160039AC[i + 0]) && ((hasOddPage ? D_1600392C[i + 0] : D_160038AC[i + 0]) & 2)) {
                D_16003AF0 = 1;
            }
            if ((maskedPc == D_160039AC[i + 1]) && ((hasOddPage ? D_1600392C[i + 1] : D_160038AC[i + 1]) & 2)) {
                D_16003AF0 = 1;
            }
            if ((maskedPc == D_160039AC[i + 2]) && ((hasOddPage ? D_1600392C[i + 2] : D_160038AC[i + 2]) & 2)) {
                D_16003AF0 = 1;
            }
            if ((maskedPc == D_160039AC[i + 3]) && ((hasOddPage ? D_1600392C[i + 3] : D_160038AC[i + 3]) & 2)) {
                D_16003AF0 = 1;
            }
        }
    }

    if (((u32)D_8003C8E0 >> 24) == 0xC) {
        arg0 = (struct118 *)&D_80031AE0;
    }
    if (D_8002BDE0[1] == D_8002AAE8[1]) {
        D_16003888 = 1;
    }
    D_1600389C = arg0;
    D_160038A4 = 0;
    if ((arg0->unk120 == 0x20) && (arg0->unk11C == (s32)func_150AD770)) {
        D_160038A4 = 1;
    }

    do {
        if ((firstPass == 0) && (state & 2)) {
            func_16001678();
        }
        drawFunc = D_16003AF8[D_16003AF4];
        if (drawFunc != NULL) {
            drawFunc();
        }
        osWritebackDCacheAll();
        do {
            state = 0;
            D_16003898 = D_16003894;
            func_16001700();
            func_16001830(&D_160036F0);
            if (firstPass != 0) {
                D_16003898 = D_16003894;
            }
            D_16003894 = D_160036F0.unk0;
            if (D_160036F0.unk2 >= 0x33) {
                D_16003894 |= 0x20000;
            }
            if (D_160036F0.unk2 < -0x32) {
                D_16003894 |= 0x10000;
            }
            if (D_160036F0.unk3 >= 0x33) {
                D_16003894 |= 0x40000;
            }
            if (D_160036F0.unk3 < -0x32) {
                D_16003894 |= 0x80000;
            }
            D_16003890 = (D_16003894 ^ D_16003898) & D_16003894;
            inputFunc = D_16003B08[D_16003AF4];
            if (inputFunc != NULL) {
                state = inputFunc();
            }
        } while ((state & 5) == 0);
        firstPass = 0;
    } while ((state & 4) == 0);

    if (D_16003AF0 == 0) {
        arg0->unk10 = 4;
        arg0->unk12 = 0;
        return 1;
    }
    tlbBase = 0;
    if ((arg0->unk120 == 0x20) && (D_160038A4 == 0)) {
        tlbBase = 1;
        arg0->unk11C += 4;
    }
    return tlbBase;
}

// NON-MATCHING: lots to figure out
void func_16000F8C(s32 arg0, f32 arg1) {
    u8 tmp[0x2C];
    s32 temp_v1;
    u32 temp_t9;

    if ((arg0 >= (D_160038A0 << 5)) && (arg0 < 833)) {
        temp_v1 = *(s32*)&arg1;
        temp_t9 = (u32) (temp_v1 & 0x7F800000) >> 0x17;
        if ((temp_t9 == 0) || (temp_t9 >= 0xFFU)) {
            if ((temp_v1 * 2) != 0) {
                func_160012B0(arg0, &D_160047D0);
                return;
            }
        }
        func_16001B34(tmp, &D_160047D4, &D_160047DC, &D_160047E0, (f64) arg1);
        func_160012B0(arg0, tmp);
    }
}

// draw a number at a screen position: mode 0=hex, 1=decimal, 2=float
typedef struct {
    s32 v[10];
} Table1044; // for the divisor-table block copy below

// NEARLY MATCHING (151/155 words, ~35 real diffs)
void func_16001044(s32 arg0, s32 arg1, s32 arg2) {
    s32 sp78[10];
    s32 fb;
    s32 i;

    *(Table1044 *) sp78 = *(Table1044 *) D_16003B50;

    if (arg0 >= (D_160038A0 << 5) && arg0 < 0x341) {
        fb = func_1600160C(arg0);
        if (arg1 == 0) {
            fb += 0x70;
            for (i = 0; i < 8; i++) {
                u8 c = arg2 & 0xF;

                if (c >= 10) {
                    c += 7;
                }
                c += 0x30;
                fb = func_160014F0(fb, c);
                arg2 = arg2 >> 4;
                fb -= 0x10;
            }
        } else if (arg1 == 1) {
            s32 printed;
            s32 *p;
            s32 *base;
            s32 *stop;

            if (arg2 < 0) {
                fb = func_160014F0(fb, '-');
                arg2 = -arg2;
            }
            printed = 0;
            stop = sp78;
            base = sp78;
            p = &sp78[9];
            do {
                s32 divisor = *p;
                s32 digit = arg2 / divisor;

                arg2 = arg2 % divisor;
                if (digit > 0 || printed || p == base) {
                    fb = func_160014F0(fb, (u8) (digit + 0x30));
                    printed = 1;
                }
                p--;
            } while (p >= stop);
        } else if (arg1 == 2) {
            s32 exp = (arg2 & 0x7F800000) >> 23;

            if ((exp > 0 && exp < 0xFF) || (exp == 0 && (arg2 << 9) == 0)) {
                u8 buf[40];
                f32 f;

                *(s32 *) &f = arg2;
                func_16001B34(buf, D_160047E8, D_160047F0, D_160047F4, (f64) f);
                func_160012B0(arg0, buf);
            } else {
                func_160012B0(arg0, D_160047E4);
            }
        }
    }
}

void func_160012B0(s32 arg0, u8 *arg1) {
    if (arg1 && (arg0 >= (D_160038A0 << 5)) && (arg0 < 833)) {
        s32 fb = func_1600160C(arg0);
        while (*arg1 != 0) {
            fb = func_160014F0(fb, *arg1 & 0xFF);
            *arg1++;
        }
    }
}
// convert rgb to rgba16
void func_16001338(u8 arg0, u8 arg1, u8 arg2) {
    D_1600388C = ((arg0 & 0xF8) << 8) | ((arg1 & 0xF8) << 3) | ((arg2 & 0xF8) >> 2) | 1;
}

// NON-MATCHING: fill a rectangle with the current color (D_1600388C).
void func_16001390(s16 x0, s16 y0, s16 x1, s16 y1) {
    s16 width;
    s16 height;
    s16 *dst;
    s32 row;
    s32 col;

    if ((x1 < x0) || (y1 < y0) || (x0 < 0) || (y0 < 0)) {
        return;
    }

    width = x1 - x0 + 1;
    height = y1 - y0 + 1;
    if (width <= 0 || height <= 0) {
        return;
    }

    dst = (s16 *)(func_1600160C(0) + ((y0 * D_160038A8) + x0) * 2);
    for (row = 0; row < height; row++) {
        for (col = 0; col < width; col++) {
            dst[col] = D_1600388C;
        }
        dst += D_160038A8;
    }
}

// NON-MATCHING: blit an 8x8 glyph into the framebuffer.
s32 func_160014F0(s32 arg0, s32 arg1) {
    s16 *dst = (s16 *) arg0;
    s32 c = arg1 & 0xFF;
    u8 *glyph;
    s32 row;

    if (c < 0x20) {
        c = 0x20;
    }
    glyph = &D_16003CE0[(c - 0x20) * 8];
    for (row = 0; row < 8; row++) {
        u8 bits = *glyph;
        s32 col;
        for (col = 0; col < 8; col++) {
            *dst++ = (bits & 0x80) ? D_1600388C : 1;
            bits <<= 1;
        }
        glyph++;
        dst += D_160038A8 - 8;
    }
    return arg0 + 0x10;
}

// text position -> framebuffer address
s32 func_1600160C(s32 arg0) {
    s32 pos = arg0 & 0xFFE0;

    if (D_160038A8 != 0x124) {
        pos = (pos >> 2) + pos;
    }
    pos >>= 2;
    pos *= D_160038A8 << 1;
    pos += (arg0 & 0x1F) * 0x10;
    pos += D_160038A8 * 4;
    pos += 0x10;
    return D_8002AAE8[D_16003888] + pos;
}

// clear the framebuffer to 0x0001 pixels (4x-unrolled fill); retail is void
// (the sole caller, func_16000B14, ignores v0) - a returned value costs 4
// extra instructions for the merged exit and breaks the section layout
void func_16001678(void) {
    s32 fb;
    s32 end;
    s32 width;

    fb = D_8002AAE8[D_16003888];
    if (D_160038A8 == 0x124) {
        width = 0xD7;
    } else {
        width = 0x108;
    }
    end = fb + ((D_160038A8 >> 1) * width * 4);
    if ((u32) fb < (u32) end) {
        do {
            fb += 0x10;
            *(u32 *)(fb - 0x10) = 0x10001;
            *(u32 *)(fb - 0xC) = 0x10001;
            *(u32 *)(fb - 0x8) = 0x10001;
            *(u32 *)(fb - 0x4) = 0x10001;
        } while ((u32) fb < (u32) end);
    }
}

s32 func_160016F4(s32 arg0) {
    return arg0;
}
