#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef union { u16 checksum; u8 bytes[0x70]; } SaveBlock33990;
extern SaveBlock33990 D_800BE2F0;
extern u8 D_800BE2F2;
extern u8 D_800BE2F3;
extern u8 D_800BE35A[28];
extern s8 D_800E0BE0[28];
extern s8 D_800E0BFC[];
extern u8 D_8002AC5C;
extern OSMesgQueue D_800BE900;
s32 func_151DCEF0(OSMesgQueue *, s32, void *, s32);

s32 func_151DD3A0(OSMesgQueue *, u8, u8 *, s32);
s32 func_151DD4E0(OSMesgQueue *, u8, u8 *);

/* Generated placeholder declarations. */
s32 func_15006590();
s32 func_15006BEC();
void func_1500707C(s32 slot);
s32 func_15007168();
void func_1500727C(void);
void func_15007360(void);
s32 func_15007440();
void func_15007558(void);
/* End generated placeholder declarations. */

void func_150064E0(void) {
    s32 i = 0;
    func_15017790();

    do {
        D_800C3A60[i++] = 0;
    } while (i < 69);

    D_800BE3DF = 24;
    D_800BE3E8 = 0;
    D_800D2E45 = 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15006590.s. */
s32 func_15006590() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15006BEC.s. */
s32 func_15006BEC() {
    return 0;
}
/* Erase both EEPROM blocks for every matching signed slot ID; ignore write errors. */
void func_1500707C(s32 slot) {
    s32 i;
    s8 *entry;
    s32 block;
    s32 status;

    for (i = 0; i < 8; i++) {
        *((u8 *)D_800BE358 + i) = 0xFF;
    }
    osWritebackDCacheAll();
    if (D_8002AC5C == 0) {
        entry = (s8 *)&D_800BE3D8;
        for (i = 0; i != 4; i++) {
            if (slot == *entry) {
                block = (i << 4) + 4;
                status = func_151DD4E0(&D_800BE900, (u8)block, D_800BE358);
                func_151DD4E0(&D_800BE900, (u8)(block + 1), D_800BE358);
            }
            entry++;
        }
    }
}
// requires jump table
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15007168.s. */
s32 func_15007168() {
    return 0;
}
/* Read the save block and dispatch its checksum-mismatch handler. */
void func_1500727C(void) {
    u16 checksum;
    s32 index;

    func_151DD3A0(&D_800BE900, 0x44, D_800BE2F0.bytes, 0x70);
    checksum = D_800BE2F2;
    checksum = (checksum << 2) + 0xCC;
    checksum += D_800BE2F3 << 3;
    for (index = 4; index < 104; index++) {
        checksum += D_800BE2F0.bytes[index] << (index & 3);
    }
    if (checksum != D_800BE2F0.checksum) {
        func_15007168();
    }
}
/* Recompute the weighted checksum and submit the save block when enabled. */
void func_15007360(void) {
    u16 checksum;
    volatile s32 result;
    s32 index;

    checksum = D_800BE2F2;
    checksum = (checksum << 2) + 0xCC;
    checksum += D_800BE2F3 << 3;
    for (index = 4; index < 104; index++) {
        checksum += D_800BE2F0.bytes[index] << (index & 3);
    }
    D_800BE2F0.checksum = checksum;
    if (D_8002AC5C == 0) {
        result = func_151DCEF0(&D_800BE900, 0x44, &D_800BE2F0, 0x70);
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_33990/func_15007440.s. */
s32 func_15007440() {
    return 0;
}
/* Copy the settings payload, checksum it, and queue the 32-byte EEPROM record. */
void func_15007558(void) {
    u16 checksum;
    volatile s32 result;
    s32 index;
    s8 *settings;
    u8 *record;

    record = D_800BE358 + 2;
    settings = D_800E0BE0;
    do {
        *record++ = *settings++;
    } while ((u32)settings < (u32)D_800E0BFC);
    checksum = 0xCC;
    record = D_800BE35A;
    index = 2;
    do {
        checksum += *record++ << (index++ & 3);
    } while (index < 30);
    *(u16 *)D_800BE358 = checksum;
    if (D_8002AC5C == 0) {
        result = func_151DCEF0(&D_800BE900, 0, D_800BE358, 32);
    }
}

void func_15007644(void) {
}

void func_1500764C(void) {
    D_80082BB4 = (u8)6;
    D_800BE3EC = (u8)0;
}

void func_15007668(void) {
    D_80082BB4 = (u8)7;
    D_800BE3EC = (u8)0;
}

void func_15007684(void) {
    D_80082BB4 = (u8)4;
    D_800BE3EC = (u8)0;
}

void func_150076A0(void) {
    D_80082BB4 = (u8)5;
    D_800BE3EC = (u8)0;
}

void func_150076BC(s32 arg0) {
    if (arg0 < 0) {
        func_150064E0();
    }
    if ((arg0 >= 0) && (arg0 < 4) && (D_800BE616 == 0)) {
        D_80082BB4 = (u8)1;
        D_800BE3EC = arg0;
    }
}

void func_15007718(s32 arg0) {
    if ((arg0 >= 0) && (arg0 < 3) && (D_800BE616 == 0)) {
        D_80082BB4 = (u8)2;
        D_800BE3EC = arg0;
    }
}

void func_15007750(s32 arg0) {
    if ((arg0 >= 0) && (arg0 < 3)) {
        D_80082BB4 = (u8)3;
        D_800BE3EC = arg0;
    }
}

/* Reset inline record sentinels, the pointed-to bytes and local selection bytes. */
void func_15007778(void) {
    s32 i;
    u8 *cursor;

    D_800BE3F8.unk8 = -1;
    D_800BE3F8.unk18 = -1;
    D_800BE3F8.unk28 = -1;
    D_800BE3F8.unkE = -1;
    D_800BE3F8.unk1E = -1;
    D_800BE3F8.unk2E = -1;
    D_800BE3DC = -1;
    D_800BE3DE = 0;
    D_80082BC0 = 1;

    i = 0;
    for (;;) {
        ((u8 *)D_800D2E4C)[i++] = 0;
        if (i >= 27) {
            break;
        }
    }

    cursor = D_800D2E60;
    do {
        *cursor++ = 0;
    } while (cursor < D_800D2E60 + 9);

    D_800BE3D8.byte0 = D_800BE3D8.byte1 = D_800BE3D8.byte2 = D_800BE3D8.byte3 = -1;
}
