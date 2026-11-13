#include <ultra64.h>

extern s8 D_80087260, D_8008FD8C, D_8008FD90, D_800BE3DF;
extern u8 D_80087270[], D_800BE618, D_800D23A8, D_800E0B94;
extern u8 D_800D2E40, D_800BE3E0, D_800E0B99, D_800E0BB1;
extern s16 D_8008FDBC;
extern s32 D_8008FD94;
extern u32 D_800E9D00;
void func_1501C730(s32, s32, s32, s32, s32);
void func_151E7EF8(void);

extern u8 D_800C35EA;
s32 func_151F2CDC(void);
void func_151F2D6C(s32, s32);
#include "structs.h"
extern s8 D_8008FD90;
extern s8 D_8008FD8C;
extern s8 D_800E0BEB;
extern s8 D_800E0C00[];
extern u8 D_800BE616;
extern s8 D_8008FE28;
extern u8 D_800E0B98;
extern u8 D_800E0B97;
extern s32 D_800E0A90;
extern s32 D_80000300;
extern s32 D_800E0AF0;
extern u8 D_800E0B96;
extern u8 D_8008FD74;
extern s8 D_8008FE30;
extern u8 D_8008FD80;
extern u8 D_8008FD84;
typedef struct {
    struct127 *unk0;
    struct127 *unk4;
    struct127 *unk8;
    struct127 *unkC;
} Unk800E0BA0;
extern Unk800E0BA0 D_800E0BA0;
extern u8 D_80084060[];

typedef struct {
    f32 scale;
    s8 y_offset;
    u8 object_id;
    u8 setup_id;
    u8 pad7;
} Unk800AB57C;

typedef struct {
    s16 x;
    s16 y;
    s16 z;
    u8 unk6;
    u8 pad7;
} Unk800AB940;

extern Unk800AB57C D_800AB57C[];
extern Unk800AB940 D_800AB940[];
extern u8 *D_800D20FC;
extern struct127 D_800CC2D0[];
extern u8 **D_800E0BD8;

/* Non-matching placeholders for the text-only asm slice asm/20AE20.s. */

s32 func_151E43DC();
void func_151E530C(void);
void func_151DE85C(void);
void func_1501D348(s32 scene, s32 sequence, s32 slot, s32 hook, s32 parameter);

extern s16 D_800E0B9A;
extern u8 D_800E0B94;

extern s8 D_8008FDC8;
extern s32 D_8008FDD8;
extern u8 D_800E0A8C;
extern u8 D_800E0B94;
extern u8 D_800E0BD3;
extern s32 D_800E0BD4;

extern u8 D_800D2E40;
extern u8 D_800D2E43;
extern u8 D_8008FDA4;
extern u8 D_800BEAC1;
extern s16 D_8008FDCC;
extern s16 D_800E0A80;
extern s32 D_800BE9E4;
extern s32 D_800E0A88;
extern s8 D_800E0BE9;
extern s8 *D_8008FDD4;
typedef struct {
    f32 unk0;
    f32 unk4;
    f32 unk8;
    f32 unkC;
    f32 unk10;
    f32 unk14;
    f32 unk18;
    f32 unk1C;
    s16 unk20;
    u8 pad22[8];
    u8 unk2A;
    u8 unk2B;
    u8 pad2C[0x12];
    u8 unk3E;
    u8 unk3F;
    u8 pad40;
    u8 unk41;
    u8 pad42;
    u8 unk43;
    u8 unk44;
} StatusReset20AE20;
extern s8 D_8008FE54[23];
s8 D_800E0BE0[28]; // Persisted settings span; reset initializes the first 23 bytes.
extern u8 D_800AB570[];
extern u8 D_800E0B95;

extern s8 D_800AB690[];
extern s8 *D_80082BBC;
void func_150076A0(void);

void func_151E557C(void);
void func_151E6BFC(void);
void func_151E55A8(void);
s32 func_1517EFDC(void);
s32 func_15082A44(u8 *, s32, s32, s32, s32);
void func_15083384(struct127 *, u8);
void func_1505E650(struct127 *, u16, f32, f32, f32, f32, s32);

void func_151DD970(void) {
    s32 i;

    for (i = 0; i < 23; i++) {
        D_800E0BE0[i] = D_8008FE54[i];
    }
}

s32 func_151DD9E4() {
    return 0;
}

s32 func_151DDB94(s32 arg0) {
    return ~arg0;
}

void func_151DDBA0(void) {
    D_800D2E40 = 0;
    func_1501C730(6, 0x1D, 0, 0, 1);
    D_800E0B94 = 3;
    D_8008FDA4 = 0;
    D_800BEAC1 = 0;
    func_151E557C();
    func_1000F1A8();
    func_1000E934();
    D_8008FD8C = 1;
    D_8008FD90 = 1;
}

s32 func_151DDC20() {
    return 0;
}

/* Advance the boot-logo phase and request the opening scene. */
void func_151DE6D4(void) {
    s32 timer;

    func_151E530C();
    D_800CC2D0[0].unk25C |= 0x200;
    D_800CC2D0[0].y_position = 1000.0f;
    if (D_80000300 == 0) {
        D_800E0A90 = 0;
    }
    timer = D_800E0A90;
    if ((timer >= 0x14B) && (D_800E0B9A & 0x8000)) {
        if (timer < 0x1E0) {
            timer = D_800E0A90 = 0x1E0;
        }
        if ((timer >= 0x259) && (timer < 0x2D0)) {
            timer = D_800E0A90 = 0x2D0;
        }
    }
    if (timer >= 0x349) {
        D_8008FE28 = 2;
        D_800E0B94 = 1;
        D_800D2E40 = 0;
        func_1501C730(6, 0x21, 0, 0, 1);
        D_800E0B96 = 0xFF;
    }
}

void func_151DE7D4(void) {
    D_800E0A90 = 0;
    D_800E0B97 = 0;
    D_800E0B98 = 0;
    D_800E0A8C = 0;
    D_8008FE28 = 2;
    func_151DE85C();
}

void func_151DE81C(void) {
    D_8008FD74 = 4;
    D_800E0B96 = 0;
    if (D_8008FE30 == 0) {
        func_1500764C();
    }
}

void func_151DE85C(void) {
    D_800D2E40 = 0;
    func_1501C730(6, 0x1D, 0, 0, 1);
    D_800E0B94 = 3;
    D_8008FD80 = 1;
    D_8008FE28 = 2;
    D_8008FDA4 = 0;
    D_8008FDD4[0x3E] = 0;
    D_8008FDD4[0x2B] = 5;
    D_8008FDD4[0x2C] = D_8008FDD4[0x2B];
}

void func_151DE8E8() {
}

s32 func_151DE8F0() {
    return 0;
}

s32 func_151DF1BC() {
    return 0;
}

s32 func_151DF574() {
    return 0;
}

s32 func_151DFF38() {
    return 0;
}

s32 func_151E0424() {
    return 0;
}

s32 func_151E09DC() {
    return 0;
}

s32 func_151E0B70() {
    return 0;
}

s32 func_151E1214() {
    return 0;
}

s32 func_151E1744() {
    return 0;
}

void func_151E2284(void) {
    D_8008FD80 = 3;
    func_151E530C();
    func_151E43DC();
    D_8008FD80 = 0;
}


/* Load the selected menu record, then validate the active settings. */
s32 func_151E22BC(void) {
    s32 index;
    s8 *record;
    s8 value;
    u8 clamped;
    index=D_800AB690[D_8008FDD4[0x42]*10];
    record=D_80082BBC+index*10;
    clamped=(u8)record[3];
    if (clamped>=5) { record[3]=4; clamped=4; }
    if (clamped<0) record[3]=0; /* Retain retail's redundant signed check. */
    value=record[1];
    if (value<=0) { record[1]=1; value=record[1]; }
    D_800E0BE0[2]=value;
    value=record[2];
    D_800E0BE0[0xb]=0;
    D_800E0BE0[3]=value;
    D_800E0BE0[0x10]=record[3];
    D_800E0BE0[0x11]=record[4];
    switch(index) {
    case 0: D_800E0BE0[4]=record[5]; break;
    case 1: case 2: D_800E0BE0[0xd]=record[5];D_800E0BE0[0xe]=record[6];break;
    case 5: D_800E0BE0[0x11]=0;D_800E0BE0[0x12]=record[5];break;
    case 7: D_800E0BE0[0x12]=record[5];break;
    case 8: case 9: D_800E0BE0[7]=record[5];value=record[6];D_800E0BE0[0x11]=1;D_800E0BE0[3]=2;D_800E0BE0[0x13]=value;break;
    }
    D_800E0BE0[0x16]=record[8];
    D_800E0BE0[6]=record[9];
    return func_151DD9E4();
}


/* Copy the selected menu settings into its ten-byte record, then submit it. */
void func_151E2404(void) {
    s32 index;
    volatile s8 *source;
    s8 *record;

    source = D_800E0BE0;
    index = D_800AB690[D_8008FDD4[0x42] * 10];
    record = D_80082BBC + index * 10;
    record[0] = 0;
    record[1] = source[2];
    record[2] = source[3];
    record[3] = source[0x10];
    record[4] = source[0x11];
    switch (index) {
        case 0:
            record[5] = source[4];
            break;
        case 1:
        case 2:
            record[5] = source[0xD];
            record[6] = source[0xE];
            break;
        case 5:
        case 7:
            record[5] = source[0x12];
            break;
        case 8:
        case 9:
            record[5] = source[7];
            record[6] = source[0x13];
            break;
    }
    record[8] = source[0x16];
    record[9] = source[6];
    func_150076A0();
}

s32 func_151E24F0() {
    return 0;
}

s32 func_151E2834() {
    return 0;
}

s32 func_151E30C4() {
    return 0;
}

/* Reset scene flags, submit the saved transition, then run the integrity check. */
void func_151E327C(void) {
    D_80087260 = 3;
    if (D_800E9D00 & 0x200) {
        D_80087260 = 0x33;
    }
    D_80087270[0] = 0;
    D_8008FD8C = 1;
    D_8008FD90 = 1;
    /* Retail changes only the first representation byte of this word. */
    *(s8 *)&D_8008FD94 = 1;
    D_8008FDBC = 0;
    *(s8 *)&D_800BE618 = 1;
    D_800D23A8 = 0;
    D_800E0B94 = 0;
    D_800D2E40 = 0;
    func_1501C730(6, D_800BE3DF, D_800BE3E0, 0, 1);
    D_800E0B99 = 1;
    *(s8 *)&D_800E0BB1 = 1;
    func_151E7EF8();
}

s32 func_151E3344() {
    return 0;
}

/* Consume the one-shot flag or advance the callback/audio transition state. */
void func_151E4264(void) {
    if (D_8008FD80 != 0) {
        D_8008FD80 = 0;
        return;
    }
    func_151E530C();
    if (((s16) D_800E0B9A != 0) || (D_800C35EA != 1)) {
        if ((D_800C35EA == 1) && (func_151F2CDC() == 1)) {
            func_151F2D6C(0, 0x2DE0);
        }
        D_800E0B94 = 7;
        D_800E0A88 = (s32)func_151E2834;
        D_8008FD74 = 8;
    }
}

typedef struct {
    s16 scene;
    s8 sequence;
    s8 alternateSequence;
} MenuSceneChoice20AE20;
extern s8 D_800AB692[];
extern MenuSceneChoice20AE20 D_800AB7A4[];

/* Start the selected menu scene, or use the fallback transition. */
void func_151E4314(void) {
    s32 choiceIndex;
    s32 sequence;
    MenuSceneChoice20AE20 *choice;

    choiceIndex = D_800AB692[D_8008FDD4[0x42] * 10];
    if (choiceIndex >= 0) {
        if (D_800E0C00[0]) {
            choice = &D_800AB7A4[choiceIndex];
            sequence = choice->alternateSequence;
        } else {
            choice = &D_800AB7A4[choiceIndex];
            sequence = choice->sequence;
        }
        func_1501D348(choice->scene, sequence, 0, 0, 0);
        D_8008FD80 = 1;
        D_800E0B94 = 5;
        D_8008FD8C = 1;
        D_8008FD90 = 1;
    } else {
        func_151E2834();
    }
}

s32 func_151E43DC() {
    return 0;
}

s32 func_151E4BD8() {
    return 0;
}

void func_151E4DC4() {
    D_800E0B94 = 10;
}

void func_151E4DD8() {
    if (D_800E0B9A & 0x8020) {
        D_800E0B94 = 4;
    }
}

void func_151E4E00(void) {
    D_8008FDCC = 0;
    func_151E557C();
    D_800E0B94 = 3;
    D_8008FDA4 = 0;
    D_8008FD80 = 0;
    D_800D2E40 = 0;
    func_1501C730(6, 0x1D, 0, 0, 1);
}

void func_151E4E64(void) {
    func_151E530C();
    func_151E55A8();

    if (D_800E0A90 >= 0x4B1) {
        D_800E0B9A |= 0x8000;
    }
    if (D_800E0B9A != 0) {
        D_800E0B94 = 7;
        D_800E0A88 = (s32)func_151E4E00;
        D_8008FD74 = 8;
    }
}

extern f32 D_8008FDD0, D_800DDDC8, D_800DDDD8;
extern f32 D_800ABA2C, D_800ABA30, D_800ABA34;
/* Update the scene fade and dispatch its completion callback. */
void func_151E4EE8(void) {
    u8 alpha = D_800E0B96;
    D_8008FDD0 = 1.0f - ((f32)alpha / 255.0f);
    if (D_8008FD74 == 255) {
        if (D_800DDDC8 > D_800ABA2C) {
            D_800E0B96 = alpha + (u32)D_800BE9E4;
            alpha = D_800E0B96;
            if (alpha < 0x55) {
                D_800DDDD8 = D_800ABA30;
            } else {
                D_800DDDD8 = D_800ABA34;
            }
        }
        if (D_800DDDC8 < 1.0f || alpha < 0x6E) {
            return;
        }
    } else if (alpha != 255) {
        s32 next = (s32)(alpha + (u32)D_800BE9E4 * D_8008FD74);
        if (next >= 256) {
            next = 255;
        }
        D_800E0B96 = next;
        return;
    }
    D_800E0B96 = 255;
    D_8008FD74 = 8;
    D_8008FDD0 = 1.0f;
    ((void (*)(void))D_800E0A88)();
}

void func_151E5034(void) {
    ((StatusReset20AE20 *)D_8008FDD4)->unk0 = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unk4 = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unk2B = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk20 = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk3E = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk3F = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk41 = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk43 = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk44 = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk10 = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unk2A = 0;
    ((StatusReset20AE20 *)D_8008FDD4)->unk14 = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unk18 = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unk1C = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unkC = 0.0f;
    ((StatusReset20AE20 *)D_8008FDD4)->unk8 = 0.0f;
}

void func_151E50C8(void) {
    s32 i;

    for (i = 0; i < 23; i++) { D_800E0BE0[i] = D_8008FE54[i]; }

    D_800E0A90 = 0;
    func_151E6BFC();

    if (D_8008FDD4 == NULL) {
        D_8008FDD4 = (s8 *)&D_800E0AF0;
        func_151E5034();

        if ((D_8008FDD4[0x3E] == 1) ^ 0) {
            D_8008FDD4[0x2C] = D_800AB570[D_8008FDD4[0x2C]];
        }
    }

    func_15017790();
    D_800E0B94 = 11;
    D_800D2E40 = 0;
    func_1501C730(6, 0x25, 0, 0, 1);
    D_800E0B95 = D_800E0B94;
}

extern s32 D_8003C8E0;
extern u8 D_800E0BDC;
extern u16 D_800BE930;
extern void (*D_8008FDEC[])(void);
void func_15042D78(u8);
s32 func_151E6964();

/* Run the live mode callback and account for time outside mode 7. */
void func_151E51EC(void) {
    u8 previous = D_800E0B94;

    D_8003C8E0 = 0x08000000;
    D_800E0BDC = 255;
    func_15042D78(0x81);
    D_800E0B9A = D_800BE930;
    if (D_8008FE28 != 0) {
        D_8008FE28--;
        D_800E0B9A = 0;
    }
    if (D_800E0B94 == 0) {
        func_151E6964(2);
    } else if (D_800E0B94 == 8) {
        func_151E6964(4);
    } else {
        func_151E6964(1);
    }
    D_8008FDEC[D_800E0B94]();
    if (D_800E0B94 != 7) {
        D_800E0A90 = (u32)D_800E0A90 + (u32)D_800BE9E4;
        if (D_800E0B94 != previous) {
            D_800E0B95 = previous;
            D_800E0A90 = 0;
        }
    }
    D_8003C8E0 = 0;
}

/* Decay the status intensity, then derive a replacement from an active record. */
void func_151E530C(void) {
    s32 intensity;
    s8 *record;

    if (D_800E0B94 != 2) {
        if (D_800E0B96 != 0) {
            intensity = (s32)((u32)D_800E0B96 - (u32)D_800BE9E4 * D_8008FD74);
            if (intensity < 0) {
                intensity = 0;
            }
            D_800E0B96 = intensity;
        }
        record = D_8008FDD4;
        if (record != NULL && record[0x2B] == 0 &&
            *(f32 *)(record + 0xC) > 0.0f && *(f32 *)(record + 8) > 0.5f) {
            intensity = (s32)((*(f32 *)(record + 8) - 0.5f) * 524.0f);
            if (intensity >= 256) {
                intensity = 255;
            }
            D_800E0B96 = intensity;
        }
    }
}

s32 func_151E53E8() {
    return 0;
}

void func_151E557C(void) {
    D_80084060[0] = 0;
    D_80084060[1] = 1;
    D_80084060[2] = 2;
    D_80084060[3] = 3;
}

void func_151E55A8(void) {
    s32 direction = D_800E0B98;
    s32 offset;
    s32 position;

    if (direction == 0) {
        offset = D_800BE9E4 << 3;
    } else {
        offset = (-D_800BE9E4) << 3;
    }

    position = D_800E0B97;
    position += offset;
    if (position >= 0x100) {
        position = 0x1FE - position;
        D_800E0B98 = direction ^ 1;
    } else if (position < 0) {
        position = -position;
        D_800E0B98 = direction ^ 1;
    }
    D_800E0B97 = position;
}

void func_151E562C(void) {
    if (D_800E0A8C != 0) {
        D_800E0A8C = 0;
    }
}

s32 func_151E564C() {
    return D_8008FDC8;
}

s32 func_151E565C() {
    return 0;
}

s32 func_151E5F64(s32 arg0) {
    s8 temp_v1;

    if ((D_800BE616 != 0) || (D_800E0B94 != 0)) {
        temp_v1 = D_800E0C00[arg0];
        if (temp_v1 < 0) {
            temp_v1 = 0;
        }
        return temp_v1;
    }
    return arg0;
}

s32 func_151E5FAC(void) {
    if (D_800E0BEB != 0) {
        s8 temp_v1 = D_8008FD8C;

        if (temp_v1 >= 5) {
            return D_8008FD90;
        }
        return temp_v1;
    }
    return D_8008FD90;
}

s32 func_151E5FF4() {
    return 0;
}

s32 func_151E6964() {
    return 0;
}

void func_151E6BFC(void) {
    D_800E0BD3 = 0;
    D_800E0BD4 = 0;
    D_8008FDD8 = 0;
}

s32 func_151E6C1C() {
    return 0;
}

extern u8 D_8008FFB0[][6];
extern f32 D_800ABA8C;
u8 *func_151149AC(u8);

/* Mark the two status-selected actors for mode 2, using live state after each lookup. */
void func_151E7DC0(void) {
    s32 index;
    u8 key;
    u8 *actor;

    if (*(f32 *)(D_8008FDD4 + 8) < D_800ABA8C && D_8008FDD4[0x3E] == 0) {
        return;
    }
    for (index = 0; index < 2; index++) {
        if (D_8008FDD4[0x3E] == 0) {
            key = D_8008FFB0[index][D_8008FDD4[0x2C]];
        } else {
            key = D_8008FFB0[index][0];
        }
        actor = func_151149AC(key);
        if (actor != NULL) {
            *(s32 *)(actor + 0x80) = 2;
        }
    }
}

void func_151E7E9C(void) {
    if (D_800E0BE9 == 2) {
        func_10017870(1);
        return;
    }
    if (D_800E0BE9 == 0) {
        func_10017870(2);
        return;
    }
    func_10017870(4);
}

void func_151E7EF8(void) {
    s32 *ptr;
    s32 *end;
    s32 checksum;

    func_151E7E9C();
    ptr = (s32 *) func_151DDC20;
    end = (s32 *) func_151DE7D4;
    checksum = 0;
    while (ptr < end) {
        checksum += *ptr;
        ptr++;
    }
    if (checksum != 0xBFC924E3) {
        *(s32 *) osSpTaskLoad = 0;
    }
}

void func_151E7F60(s32 arg0, s32 arg1) {
    struct127 **slot;
    struct127 *object;
    Unk800AB57C *object_entry;
    Unk800AB940 *position_entry;
    u8 *descriptor;
    s32 descriptor_index;
    s32 object_index;
    s32 position_index;
    s32 object_id;

    slot = &D_800E0BA0.unk0 + arg0;
    if (*slot != NULL) {
        func_15060F28(*slot, 1);
    }

    descriptor_index = func_15083E0C((arg0 + 0x10) & 0xFF);
    object_entry = &D_800AB57C[arg1];
    descriptor = D_800D20FC + descriptor_index * 0x30;
    object_id = object_entry->object_id;
    position_index = arg0;
    if (D_8008FDD4[0x2C] == 7) {
        position_index++;
    }
    position_entry = &D_800AB940[position_index];

    descriptor[4] = object_id;
    *(s16 *)(descriptor + 6) = position_entry->x;
    *(s16 *)(descriptor + 8) = position_entry->y;
    *(s16 *)(descriptor + 8) += object_entry->y_offset;
    *(s16 *)(descriptor + 0xA) = position_entry->z;
    descriptor[0xC] = position_entry->unk6;
    if (object_id == 0x53) {
        descriptor[0xD] = 0x24;
    } else {
        descriptor[0xD] = 0xE;
    }

    object_index = func_15082A44(descriptor, descriptor_index, 0, 0, 0);
    if (object_index != 0) {
        object = &D_800CC2D0[object_index - 1];
        *slot = object;
        object->unk5 = 7;
        object->unk2F8 |= 3;
        object->xz_scale = object->y_scale = object_entry->scale;

        if ((object->id == 0) || (object->id == 0x80)) {
            object->unk31C = (struct126 *)allocate_memory(0x1C0, 1, 0, 0);
            bzero(object->unk31C, 0x1C0);
        }
        if (object_id == 0x3B) {
            *(u8 *)&object->pad68 = arg0 + 1;
        }
        func_15083384(object, object_entry->setup_id);
        func_1505E650(object, 0xF, 1.0f, 0.0f, 0.0f, 0.0f, 0);
    }
}

void func_151E81EC(void) {
    D_800E0BA0.unkC = D_800E0BA0.unk8 = D_800E0BA0.unk0 = D_800E0BA0.unk4 = 0;
    D_8008FD84 = 0;
}

void func_151E8214(void) {
    if (D_800E0B94 != 8) {
        if (func_1517EFDC() == 0) {
            D_800E0A90 = 0;
        }

        if (D_800E0A90 >= 0xA1) {
            D_8008FDCC = 0;
            D_800E0B94 = 8;
            D_8008FD8C = 1;
            D_8008FD90 = 1;
            D_8008FDA4 = 0;
            D_800E0A80 = -2;
            D_800E0A90 = 0;
            D_800D2E43 = 1;
        }
    }
}

void func_151E82B8(void) {
    s32 index;

    func_151E530C();
    index = D_800E0A80;

    if (-1 == index) {
        if (D_800E0A90 >= 0x79) {
            D_800E0B94 = 9;
            D_800E0A90 = 0;
            D_8008FDCC = 0xFF;
            D_800E0A80 = 0;
            func_1501C730(6, 0x1D, 0, 0, 1);
            return;
        }
    }

    if (index == -2) {
        D_800E0A80 = 0;
    }

    if (D_800E0A90 < 0x1BE) {
        return;
    }
    index = D_800E0A80;
    if (index < 0) {
        return;
    }

    while (D_800E0BD8[index][0] != 0x2A) {
        D_800E0A80 = index + 1;
        index = D_800E0A80;
    }
    D_800E0A80 = index + 1;
    if (D_800E0BD8[D_800E0A80][0] == 0x3D) {
        D_800E0A80 = -1;
    }
    D_800E0A90 = 0;
}

void func_151E83E8(void) {
    if (D_800E0A80 == 0) {
        D_800E0A80 = -1;
        func_1501D348(0x1D, 6, 0, 0, 0);
    }

    func_151E530C();
    if (func_1517EFDC() == 0) {
        D_800E0A90 = 0;
    }

    if (D_800E0A90 >= 0x65) {
        func_151E5034();
        D_8008FDA4 = 0;
        D_800E0B94 = 1;
        D_800E0A90 = 0;
        D_800D2E40 = 0;
        func_1501C730(6, 0x21, 0, 0, 1);
    }
}
