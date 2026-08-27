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

void func_16000590(void *arg0) {
    register u8 *var_s5 = arg0;
    u32 var_s2;
    s32 var_s0;
    s32 var_s1;
    s32 var_v0;
    s32 var_s4 = 0;
    register u32 *var_s3;

    var_s2 = *(u32 *) (var_s5 + 0x12C);
    func_160012B0(3, D_160047A4);
    func_16001044(0xA, 0, var_s2);

    var_s2 = var_s2 >> 12;
    var_s0 = 0x2C;
    var_s1 = 0;
    var_s3 = D_16003B30;
    do {
        if (var_s2 & 1) {
            func_160012B0(var_s0, (u8 *) var_s3[var_s1]);
            var_s0 += 0x20;
        }
        var_s1 += 1;
        var_s2 >>= 1;
    } while (var_s1 < 6);

    var_s1 = 0;
    var_s0 = 0xC3;
    if (D_16003B28 == 1) {
        var_v0 = 0x4C;
    } else {
        var_v0 = 0x6C;
        var_s4 = 0x10;
    }
    var_s3 = (u32 *) (var_s5 + var_v0 * 4);
    do {
        func_160012B0(var_s0, D_160047AC);
        func_16001044(var_s0 + 2, 1, var_s1 + var_s4);
        func_16001044(var_s0 + 5, 2, var_s3[1]);
        var_s1 += 1;
        var_s3 += 2;
        var_s0 += 0x20;
    } while (var_s1 < 0x10);
}

typedef struct {
    s32 value;
} DebugLabel;

void func_160006CC(void *arg0) {
    struct {
        DebugLabel label;
    } storage;
    u8 *label;
    u8 *entry;
    s32 pos;
    register s32 next;

    storage.label = *(DebugLabel *)&D_16003B48;
    label = (u8 *)&storage.label;
    pos = 0x123;
    entry = D_160037F0;
    func_16001338(0xC0, 0xC0, 0xFF);
    next = *(u8 *)(u32)D_160037F0;
    do {
        label[0] = next;
        label[1] = entry[1];
        func_160012B0(pos, label);
        {
            u8 index = entry[2];
            pos += 3;
        func_16001044(pos, 0, ((s32 *) arg0)[index + 1]);
        }
        pos += 0xD;
        next = entry[3];
        entry += 3;
    } while (next != 0);
}

// NON-MATCHING: close but still some stuff to figure out
void func_1600078C(void) {
    register s32 temp_s0;
    u8 range_prefix;
    register s32 phi_s1;
    register u32 phi_s2;
    register u32 phi_s3;
    register u32 phi_s5;
    register s32 i;
    s32 dead_flag = 0;

    temp_s0 = *(s32 *) ((u8 *) D_1600389C + 0xF4);
    func_16001338(0, 255, 0);
    func_160012B0(11, &D_160047B0);
    phi_s2 = (D_16003B4C * 4) + temp_s0;
    if (((phi_s2 & 3) == 0) && (phi_s2 >= 0x80000000U) && (phi_s2 < 0x80800001U)) {
        if (D_16003B4C == 0) {
            func_16001338(255, 0, 0);
            phi_s5 = (u32)&D_8002D4B0;
        } else {
            phi_s5 = (u32)&D_8002D4B0;
            if ((phi_s2 >= phi_s5) && (phi_s2 < (phi_s5 + 0x400))) {
                func_16001338(128, 128, 255);
            } else if ((phi_s2 >= (u32) &D_8002D8B0) && (phi_s2 < ((u32)&D_8002D8B0 + 0x4000))) {
                func_16001338(255, 128, 128);
            } else {
                func_16001338(255, 255, 255);
            }
        }
        phi_s1 = 97;
        i = 0;
        do {
            func_16001044(phi_s1, 0, phi_s2);
            func_160012B0(phi_s1 + 8, &D_160047BC);
            phi_s3 = *(u32 *) phi_s2;
            range_prefix = (phi_s3 >> 24);
            if (range_prefix == 0x80) {
                func_16001338(128, 128, 255);
            } else if (range_prefix == 0x15) {
                func_16001338(255, 0, 0);
            } else if (range_prefix == 0x16) {
                func_16001338(128, 255, 128);
            } else if (dead_flag != 0) {
                func_16001338(9, 9, 9);
                func_16001338(9, 9, 9);
            } else if (dead_flag != 0) {
                func_16001338(8, 8, 8);
                func_16001338(8, 8, 8);
            } else if (dead_flag != 0) {
                func_16001338(7, 7, 7);
                func_16001338(7, 7, 7);
            } else if (dead_flag != 0) {
                func_16001338(6, 6, 6);
                func_16001338(6, 6, 6);
            } else if (dead_flag != 0) {
                func_16001338(5, 5, 5);
                func_16001338(5, 5, 5);
            } else if (dead_flag != 0) {
                func_16001338(4, 4, 4);
                func_16001338(4, 4, 4);
            } else if (dead_flag != 0) {
                func_16001338(3, 3, 3);
                func_16001338(3, 3, 3);
            } else if (range_prefix == 0x10) {
                func_16001338(255, 0, 0);
            } else {
                func_16001338(255, 255, 255);
            }
            func_16001044(phi_s1 + 0xC, 0, phi_s3);
            func_160012B0(phi_s1 + 0x16, &D_160047C0);
            func_16001338(255, 255, 255);
            func_16001044(phi_s1 + 0x16, 1, phi_s3);
            if ((phi_s2 >= phi_s5) && (phi_s2 < (phi_s5 + 0x400))) {
                func_16001338(128, 128, 0xFF);
            } else if ((phi_s2 >= (u32) &D_8002D8B0) && (phi_s2 < ((u32)&D_8002D8B0 + 0x4000))) {
                func_16001338(255, 128, 128);
            } else {
                func_16001338(255, 255, 255);
            }
            phi_s1 += 0x20;
            phi_s2 += 4;
        } while (++i != 22);
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

// agP: local prototypes (missing from functions.h; void returns matter for IDO temp allocation)
void func_16003650(void);
void func_16001700(void);
void func_16001830(struct263 *);

// called from func_10007DAC
// NON-MATCHING: mips-to-c cleaned skeleton, converted for raw-progress accounting.
// agR: dead f64 phantom local; IDO reserves its 8-byte chunk at 0x48(sp), giving the
// retail 0x50 frame with firstPass@0x40 / arg0-spill@0x50. Produces no code.
// agR: DOMINO SOLVED (286/286, 8 diffs from 63 / 108). Two rules found:
// (1) the else `one = (maskedPc != 0)` MUST sit BEFORE the `maskedPc &= ~0x1000`
// redef so the sltu reads maskedPc's HOME a1 -> uopt writes the web home t1
// directly (`sltu t1,zero,a1`). Reading the redef's pending temp t4 (any def
// placed after the redef) makes the sltu take a temp + `move home,temp` and the
// full a2/a3/t0/t1 displacement domino returns (verified). (2) the arm def
// `one = (arg0->unk11C != 0)` must read pc's reg t2, NOT arg0's t8: a t8 read
// perturbs uopt's temp freelist and flips a systematic t8<->t9 swap through
// the whole loop + do-while (~38 diffs). With both: one home = t1 (retail reg),
// hasOddPage a2, 38AC a3, 392C t0, t3 = &D_16003AF0 hoisted, `sw t1,0(t3)`
// loop stores, beqzl shapes - all retail.
// Remaining 8 (structural for a non-const web): [53,56,65] pc in t2 not t1
// (one-web reserves t1 from the arm def @c04; pc lives c00-c18 and retail had
// no web there - li remats); [60] `sltu t1,zero,t2` vs `li t1,1` (li defs
// const-fold, so a compute def is unavoidable); [70,71,74,75] preheader order -
// the a1-reading sltu must precede the redef's `move a1,t4`, so it lands at c2c
// where retail has `and t4`, while retail's dep-free li sits last @c48.
// Dead ends: mixed li+sltu defs (flow-sensitive SCCP remats, 289 words), loop
// bound via D_16003A2C symbol (breaks rotation), explicit pc local (+1 frame
// word), decl reorder (no effect).
// agR: SESSION 3 EXHAUSTIVE LI-HUNT (still 8 diffs; floor analysis below).
// Goal was retail's `li t1,1` defs @c04+c48 with the t1 web intact (4x loop
// `sw t1,0(t3)`, 2x sb t1) and NO per-use remat. EVERY const provenance folds
// and remats (292/200-diff cascade: loop stores become per-site beq+li+lui+sw,
// &D_16003888 s1-hoist dies, whole-function rotation):
//  (1) s32 literals both arms; (2) direct const stores (no `one` var, 108
//  diffs); (3) path-condition exprs (`(pc&0xFF000000)==0x15000000` per arm) -
//  uopt has NO path sensitivity, stays runtime (+3 words + rotation);
//  (4) memory provenance `one = firstPass` (firstPass==1 in slot 64(sp)) -
//  uopt const-props THROUGH stack slots and remats; (5) `register s32 one`;
//  (6) s8 one (narrow types fold too); (7) `one = (&D_16003AF0 != 0)` - cfe
//  folds address-vs-null; (8) `one = pc - pc + 1` - cfe folds x-x.
// MIXED defs both orders: li-then/slut-else = 287w (web li t3@c04 + remat li
// t1 for the c10 sw = double-li, pc stays t2); slut-then/li-else = 289w (pc
// DOES get t1! one=t2, loop remats). KEY REMAT RULE learned: remat is
// flow-sensitive per-use at BLOCK boundaries - same-block use (c10 sw) reads
// the web even with a const def; any use in a different block (the loop)
// remats per-site, and IDO never LICM-hoists a const materialization into a
// preheader. uopt webs are linear-disjoint: one[c04..w170] and pc[53..c18]
// can NEVER share t1 in our builds, yet retail shares (its li-def "web" is
// not allocation-constrained) - this sharing is the unreachable part.
// SCHEDULING map: dep-free sltu (pc-read else-def) floats EARLY (c24), not
// last like retail's dep-free li (only pure consts sink to c48); reading the
// redef's NEW value = domino (sltu takes temp, hasOddPage a2->a3, 27 diffs);
// savedPc copy materializes `or`+2 words; reading the compare temp (t9)
// extends its life across the beq -> rotation. FLOOR = 8 diffs: [53,56,65]
// pc home (needs t1/t1 sharing), [60] li form, [70,71,74,75] the single c2c
// sltu displacement (fixes itself if the def ever moves past the preheader
// head). All 8 trace to ONE root: retail's const-li web defs. NOTE: else-path
// one is EXACTLY 1 (pc&0xFF000000==0x15000000 implies maskedPc!=0); then-path
// diverges only when arg0->unk11C == 0 exactly (one=0 vs retail 1).

s32 func_16000B14(struct118 *arg0) {
    f64 dphantom;
    s32 state = 0;
    s32 firstPass = 1;
    s32 maskedPc;
    s32 one;
    s32 hasOddPage;
    s32 temp_bde;
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

    if ((arg0->unk11C & 0xFF000000) != 0x15000000) {
        one = (arg0->unk11C != 0);
        D_16003AF0 = one;
    } else {
        maskedPc = arg0->unk11C & ~0xFFF;
        hasOddPage = maskedPc & 0x1000;
        one = (maskedPc != 0);
        maskedPc = maskedPc & ~0x1000;
        D_16003AF0 = 0;
        for (i = 0; i < 32; i += 4) {
            if ((maskedPc == D_160039AC[i + 0]) && ((hasOddPage ? D_1600392C[i + 0] : D_160038AC[i + 0]) & 2)) {
                D_16003AF0 = one;
            }
            if ((maskedPc == D_160039AC[i + 1]) && ((hasOddPage ? D_1600392C[i + 1] : D_160038AC[i + 1]) & 2)) {
                D_16003AF0 = one;
            }
            if ((maskedPc == D_160039AC[i + 2]) && ((hasOddPage ? D_1600392C[i + 2] : D_160038AC[i + 2]) & 2)) {
                D_16003AF0 = one;
            }
            if ((maskedPc == D_160039AC[i + 3]) && ((hasOddPage ? D_1600392C[i + 3] : D_160038AC[i + 3]) & 2)) {
                D_16003AF0 = one;
            }
        }
    }

    if ((((u32)D_8003C8E0 >> 24) & 0xFF) == 0xC) {
        arg0 = (struct118 *)&D_80031AE0;
    }
    temp_bde = D_8002BDE0[1];
    if (temp_bde == D_8002AAE8[1]) {
        D_16003888 = one;
    }
    D_1600389C = arg0;
    D_160038A4 = 0;
    if ((arg0->unk120 == 0x20) && (arg0->unk11C == (s32)func_150AD770)) {
        D_160038A4 = one;
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
    if ((arg0->unk120 == 0x20) && (D_160038A4 == 0)) {
        arg0->unk11C += 4;
        return 1;
    }
    return 0;
}

// NON-MATCHING: lots to figure out
void func_16000F8C(s32 arg0, f32 arg1) {
    struct F8Storage {
        u8 tmp[0x2C];
        union {
            f32 f;
            s32 i;
        } value;
    };
    struct F8Storage storage;

    if ((arg0 >= (D_160038A0 << 5)) && (arg0 < 833)) {
        s32 temp_v1;
        storage.value.f = arg1;
        temp_v1 = storage.value.i;
        if ((((u32)(temp_v1 & 0x7F800000) >> 0x17) == 0) ||
            (((u32)(temp_v1 & 0x7F800000) >> 0x17) >= 0xFFU)) {
            if ((temp_v1 * 2) != 0) {
                func_160012B0(arg0, &D_160047D0);
                return;
            }
        }
        func_16001B34(storage.tmp, &D_160047D4, &D_160047DC, &D_160047E0, (f64) arg1);
        func_160012B0(arg0, storage.tmp);
    }
}

// draw a number at a screen position: mode 0=hex, 1=decimal, 2=float
typedef struct {
    s32 v[10];
} Table1044; // for the divisor-table block copy below

// NEARLY MATCHING (151/155 words, ~35 real diffs)
void func_16001044(s32 arg0, s32 arg1, s32 arg2) {
    s32 fb;
    s32 i;
    s32 printed;
    s32 *p;
    s32 *base;
    s32 *stop;
    s32 sp78[10];
    s32 exp;
    s32 divisor;
    f32 f;
    u8 buf[36];

    *(Table1044 *) sp78 = *(const Table1044 *) D_16003B50;

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
                func_160014F0(fb, c);
                arg2 = arg2 >> 4;
                fb -= 0x10;
            }
        } else if (arg1 == 1) {
            s32 digit;

            if (arg2 < 0) {
                fb = func_160014F0(fb, '-');
                arg2 = -arg2;
            }
            printed = 0;
            stop = sp78;
            base = sp78;
            p = &sp78[9];
            do {
                divisor = *p;
                digit = arg2 / divisor;

                arg2 = arg2 % divisor;
                if (digit > 0 || printed || p == base) {
                    fb = func_160014F0(fb, (u8) (digit + 0x30));
                    printed = 1;
                }
                p--;
            } while (p >= stop);
        } else if (arg1 == 2) {
            exp = (arg2 & 0x7F800000) >> 23;

            if ((exp > 0 && exp < 0xFF) || (exp == 0 && (arg2 << 9) == 0)) {
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
            fb = func_160014F0_wide(fb, *arg1 & 0xFF);
            *arg1++;
        }
    }
}
// convert rgb to rgba16
void func_16001338(u8 arg0, u8 arg1, u8 arg2) {
    D_1600388C = ((arg0 & 0xF8) << 8) | ((arg1 & 0xF8) << 3) | ((arg2 & 0xF8) >> 2) | 1;
}

// NON-MATCHING: fill a rectangle with the current color (D_1600388C).
void func_16001390(s16 x0, s16 y0, register s16 x1, s16 y1) {
    s16 *dst;

    if ((x1 < x0) || (y1 < y0)) {
        return;
    }
    if ((x0 < 0) || (y0 < 0)) {
        return;
    }

    x1++;
    y1++;
    dst = (s16 *)func_1600160C(0);
    dst += x0 + (y0 * D_160038A8);
    x1 -= x0;
    y1 -= y0;
    if (y1 > 0) {
        do {
            s32 count = x1;
            if (x1 > 0) {
                do {
                    *dst++ = D_1600388C;
                    count--;
                } while (count != 0);
            }
        } while ((y1 -= 1, dst += D_160038A8 - x1, y1) > 0);
        }
}

// NON-MATCHING: blit an 8x8 glyph into the framebuffer.
s32 func_160014F0(s32 arg0, u8 arg1) {
    s16 *dst = (s16 *) arg0;
    s32 color;
    s32 c;
    u8 *glyph;
    s32 row;
    s32 col;
    u16 bits;

    color = D_1600388C;
    c = arg1;
    if (arg1 < 0x20) {
        c = 0x20;
    }
    col = 0;
    row = 0, glyph = D_16003CE0 + ((c - 0x20) << 3);
    for (; row < 8; row++, glyph++, dst += D_160038A8 - 8) {
        col = 0;
        bits = *glyph;
        do {
            *dst++ = (u16)((bits & 0x80) ? (color & 0xFFFF) : 1);
            bits <<= 1;
            col++;
        } while (col < 8);
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
