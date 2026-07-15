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

// reverted to GLOBAL_ASM 2026-07-15: 1 word short of retail (a loop-exit
// condition codegen quirk - retail materializes "i<16" into a register
// with a separate slti before the branch, tried both a plain for-loop and
// a do-while, neither reproduced it) - the deficit alone is enough to
// cascade into breaking already-matched functions elsewhere in this file
// (confirmed: func_16000424/func_16000058/func_16000000 regressed with
// this enabled, back to 0 diffs with it reverted). Draft below is
// otherwise logically correct including the func_16001044 float-mode
// calls, which now work correctly since func_16001B34's calling
// convention was fixed this session - only this loop's exact shape is
// missing.
// void func_16000590(void *arg0) {
//     s32 s2 = *(s32 *) ((u8 *) arg0 + 0x12C);
//     s32 bits;
//     s32 pos = 0x2C;
//     s32 i;
//     s32 v0;
//     s32 s4 = 0;
//     s32 val;
//     u8 *s3;
//
//     func_160012B0(3, D_160047A4);
//     func_16001044(0xA, 0, s2);
//
//     bits = (u32) s2 >> 12;
//     for (i = 0; i < 6; i++) {
//         if (bits & 1) {
//             func_160012B0(pos, D_16003B30[i]);
//             pos += 0x20;
//         }
//         bits >>= 1;
//     }
//
//     if (D_16003B28 == 1) {
//         pos = 0xC3;
//         v0 = 0x4C;
//     } else {
//         v0 = 0x6C;
//         s4 = 0x10;
//     }
//     val = s4;
//     s3 = (u8 *) arg0 + v0 * 4;
//     for (i = 0; i < 0x10; i++) {
//         func_160012B0(pos, D_160047AC);
//         func_16001044(pos + 2, 1, val);
//         func_16001044(pos + 5, 2, *(s32 *) (s3 + 4));
//         s3 += 8;
//         pos += 0x20;
//         val += 1;
//     }
// }
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_16000590.s")

// reverted to GLOBAL_ASM 2026-07-15: 1 word short of retail (calls the
// still-reverted func_16001044), part of the same drift investigation as
// func_16000590/func_16001044 above. Draft below believed correct.
// void func_160006CC(void *arg0) {
//     s32 sp3C = D_16003B48; // dead value, always overwritten below - kept for matching
//     u8 *label = (u8 *) &sp3C;
//     u8 *entry = D_160037F0;
//     s32 pos = 0x123;
//
//     func_16001338(0xC0, 0xC0, 0xFF);
//     label[0] = D_160037F0[0];
//     do {
//         label[1] = entry[1];
//         func_160012B0(pos, label);
//         pos += 3;
//         func_16001044(pos, 0, ((s32 *) arg0)[entry[2] + 1]);
//         pos += 0xD;
//         label[0] = entry[3];
//         entry += 3;
//     } while (label[0] != 0);
// }
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_160006CC.s")
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_1600078C.s")
// NON-MATCHING: close but still some stuff to figure out
// void func_1600078C(void) {
//     s32 temp_s0;
//     u8 range_prefix;
//     u32 temp_s2;
//     s32 temp_s5;
//     s32 phi_s1;
//     u32 *phi_s2;
//     u32 phi_s5;
//     s32 i;
//
//     temp_s0 = D_1600389C->unkF4;
//     func_16001338(0, 255, 0); // green
//     func_160012B0(11, &D_160047B0);
//     temp_s2 = (D_16003B4C * 4) + temp_s0;
//     if (((temp_s2 & 3) == 0) && (temp_s2 >= 0x80000000U) && (temp_s2 < 0x80800001U)) {
//         if (D_16003B4C == 0) {
//             func_16001338(255, 0, 0); // red
//             phi_s5 = &D_8002D4B0;
//         } else {
//             temp_s5 = &D_8002D4B0 - 0x2B50; // 11088 ?
//             if ((temp_s2 >= temp_s5) && (temp_s2 < (temp_s5 + 0x400))) {
//                 func_16001338(128, 128, 255); // purple
//                 phi_s5 = temp_s5;
//             } else if ((temp_s2 >= (u32) &D_8002D8B0) && (temp_s2 < ((u32)&D_8002D8B0 + 0x4000))) {
//                 func_16001338(255, 128, 128); // light red
//                 phi_s5 = temp_s5;
//             } else {
//                 func_16001338(255, 255, 255);
//                 phi_s5 = temp_s5;
//             }
//         }
//         phi_s1 = 97; // "a"
//         phi_s2 = temp_s2;
//         for (i = 0; i < 22; i++) {
//             func_16001044(phi_s1, 0, phi_s2);
//             func_160012B0(phi_s1 + 8, &D_160047BC);
//             range_prefix = (*phi_s2 >> 24);
//             if (range_prefix == 0x80) {                   // 0x80000000
//                 func_16001338(128, 128, 255);
//             } else if (range_prefix == 0x15) {            // 0x15000000
//                 func_16001338(255, 0, 0);
//             } else if (range_prefix == 0x16) {            // 0x16000000
//                 func_16001338(128, 255, 128);
//             } else if (range_prefix == 0x10) {            // 0x10000000
//                 func_16001338(255, 0, 0);
//             } else {
//                 func_16001338(255, 255, 255);
//             }
//             func_16001044(phi_s1 + 0xC, 0, *phi_s2);
//             func_160012B0(phi_s1 + 0x16, &D_160047C0);
//             func_16001338(255, 255, 255);
//             func_16001044(phi_s1 + 0x16, 1, *phi_s2);
//             if (((u32) phi_s2 >= phi_s5) && ((u32) phi_s2 < (phi_s5 + 0x400))) {
//                 func_16001338(128, 128, 0xFF);
//             } else if (((u32) phi_s2 >= (u32) &D_8002D8B0) && ((u32) phi_s2 < ((u32)&D_8002D8B0 + 0x4000))) {
//                 func_16001338(255, 128, 128);
//             } else {
//                 func_16001338(255, 255, 255);
//             }
//             phi_s1 += 0x20;
//             phi_s2 += 4;
//         }
//     }
// }

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
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_16000B14.s")
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_16000F8C.s")
// NON-MATCHING: lots to figure out
// void func_16000F8C(s32 arg0, f32 arg1) {
//     struct165 tmp;
//     s32 temp_v1;
//     u32 temp_t9;
//
//     if ((arg0 >= (D_160038A0 << 5)) && (arg0 < 833)) {
//         tmp.unk18 = arg1;
//         temp_v1 = *(s32*)&tmp.unk18;
//         temp_t9 = (u32) (temp_v1 & 0x7F800000) >> 0x17;
//         if ((temp_t9 == 0) || (temp_t9 >= 0x255U)) {
//             if ((temp_v1 * 2) != 0) {
//                 func_160012B0(arg1, &D_160047D0); // arg0,
//                 return;
//             }
//         }
//         func_16001B34(&arg0, &tmp.unk0, &D_160047D4, &D_160047DC, &D_160047E0); // , (f64) arg1
//         func_160012B0(arg0, &tmp.unk0);
//     }
// }

// draw a number at a screen position: mode 0=hex, 1=decimal, 2=float
void func_16001044(s32 arg0, s32 arg1, s32 arg2) {
    s32 sp78[10];
    s32 fb;
    s32 i;

    for (i = 0; i < 10; i++) {
        sp78[i] = D_16003B50[i];
    }

    if (arg0 >= (D_160038A0 << 5) && arg0 < 0x341) {
        fb = func_1600160C(arg0);
        if (arg1 == 0) {
            s32 i;
            fb += 0x70;
            for (i = 0; i < 8; i++) {
                s32 nibble = arg2 & 0xF;
                s32 c = (nibble < 10 ? nibble : nibble + 7) + 0x30;
                fb = func_160014F0(fb, c);
                arg2 = arg2 >> 4;
                fb -= 0x10;
            }
        } else if (arg1 == 1) {
            s32 printed = 0;
            s32 *p;

            if (arg2 < 0) {
                fb = func_160014F0(fb, '-');
                arg2 = -arg2;
            }
            p = &sp78[9];
            do {
                s32 divisor = *p;
                s32 digit = arg2 / divisor;
                arg2 = arg2 % divisor;
                if (digit > 0 || printed || p == sp78) {
                    fb = func_160014F0(fb, digit + 0x30);
                    printed = 1;
                }
                p--;
            } while (p >= sp78);
        } else if (arg1 == 2) {
            u32 exp = ((u32) arg2 & 0x7F800000) >> 23;
            if ((exp > 0 && exp < 0xFF) || (exp == 0 && (arg2 << 9) == 0)) {
                u8 buf[40];
                f32 f = *(f32 *) &arg2;
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

// fill a rectangle with the current color (D_1600388C) - reverted to
// GLOBAL_ASM 2026-07-15: converted version was 6 words short of retail
// (missing its remainder-then-4x-unrolled fill pattern, same idiom class
// as func_160014F0), which cascaded into breaking several already-matched
// functions' data-symbol addresses elsewhere in this file. No existing
// caller, so low value / high risk to leave half-converted - revisit with
// the unrolled-loop idiom worked out properly before re-attempting.
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_16001390.s")
// reverted to GLOBAL_ASM 2026-07-15: 1 word short of retail (missing
// retail's exact unrolled-inner-loop shape, same idiom class as
// func_16001390 above - a plain unrolled attempt made it worse, not
// better, see WORKING_NOTES). Called by func_160012B0/func_16001678
// (both already-matched) - blit an 8x8 glyph into the framebuffer,
// returning the position of the next glyph.
// s32 func_160014F0(s32 arg0, s32 arg1) {
//     s16 *dst = (s16 *) arg0;
//     s32 c = arg1 & 0xFF;
//     u8 *glyph;
//     s32 row;
//
//     if (c < 0x20) {
//         c = 0x20;
//     }
//     glyph = &D_16003CE0[(c - 0x20) * 8];
//     for (row = 0; row < 8; row++) {
//         u8 bits = *glyph;
//         s32 col;
//         for (col = 0; col < 8; col++) {
//             *dst++ = (bits & 0x80) ? D_1600388C : 1;
//             bits <<= 1;
//         }
//         glyph++;
//         dst += D_160038A8 - 8;
//     }
//     return arg0 + 0x10;
// }
#pragma GLOBAL_ASM("asm/nonmatchings/debugger/debugger/func_160014F0.s")

// splat into framebuffer
s32 func_1600160C(s32 arg0) {
    s32 pos = arg0 & 0xFFE0;

    if (D_160038A8 != 0x124) {
        pos = (pos >> 2) + pos;
    }
    return D_8002AAE8[D_16003888] + ((D_160038A8 * 2) * (pos >> 2)) + ((arg0 & 0x1F) * 0x10) + (D_160038A8 * 4) + 0x10;
}

// contains delay slot
u32 func_16001678(void) {
    s32 fb;
    s32 end;
    s32 width;

    fb = D_8002AAE8[D_16003888];
    if (D_160038A8 == 0x124) {
        width = 0xD7;
    } else {
        width = 0x108;
    }
    end = fb + (((u32) D_160038A8 >> 1) * width * 4);
    if ((u32) fb < (u32) end) {
        do {
            fb += 0x10;
            *(u32 *)(fb - 0x10) = 0x10001;
            *(u32 *)(fb - 0xC) = 0x10001;
            *(u32 *)(fb - 0x8) = 0x10001;
            *(u32 *)(fb - 0x4) = 0x10001;
        } while ((u32) fb < (u32) end);
        return fb;
    }
    return fb + 0x10;
}

s32 func_160016F4(s32 arg0) {
    return arg0;
}
