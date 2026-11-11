#include <ultra64.h>

#include "functions.h"
#include "variables.h"

typedef struct { s16 x,y,z; u8 pad[10]; } BoundsVertex;
typedef struct { u8 pad0[0x16]; u16 count; u8 pad18[0x10]; BoundsVertex *vertices; f32 sx,sy,sz; u8 pad38[0x18]; u16 radius, maximum; } BoundsRecord;
extern u16 D_800BE2A0,D_800BE2A2,D_800BE2A4;

typedef struct { u8 reserved[0x72]; u8 id; u8 tail[0x2D]; } ByteIdRecordView;


/* Generated placeholder declarations. */
s32 func_150039E0();
s32 func_150045C4();
void func_150049A4(s8 *, u32, u32);
void func_15004AAC(BoundsRecord *, s32);
s32 func_15004BF0(s32 descending);
/* End generated placeholder declarations. */

/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_150039E0.s. */
s32 func_150039E0() {
    return 0;
}

// FIXME: matches but something isnt right
void func_15004574(void) {
    if (D_800DBF88 != 0xFF) {
        D_800DBF8C = D_800DBEF4[D_800DBF88].unk1C;
        D_800DBF90 = D_800DBEF4[D_800DBF88].unk28;
    }
}

void func_150045BC(void) {
}

/* Non-matching C placeholders for asm/nonmatchings/game_30E90/func_150045C4.s. */
s32 func_150045C4() {
    return 0;
}
/* Relocate vertex/data and matrix command addresses in place. */
void func_150049A4(s8 *commands, u32 dataOffset, u32 matrixOffset) {
    s32 index;
    s8 *command;
    s32 opcode;

    for (index = 0; commands[index << 3] != (s8)G_ENDDL; index++) {
        command = commands + (index << 3);
        opcode = command[0];
        switch (opcode) {
            /* Retail keeps this positive comparison after the signed load. */
            case G_DL:
                *(u32 *)(command + 4) += dataOffset;
                break;
            case G_VTX:
                *(u32 *)(command + 4) += dataOffset;
                break;
            case (s8)G_MOVEMEM:
                if ((u8)command[3] == G_MV_MATRIX) {
                    *(u32 *)(command + 4) += matrixOffset;
                }
                break;
        }
    }
}
// NON-MATCHING: not this...
void func_15004A4C(void) {
    s32 i;

    for (i = 0; i < D_800DBEF0; i++) {
        D_800DBEF8[i] = 0;
        D_800DBEFC[i] = 0;
    }
}

/* Check the scaled vertex radius and count the result. */
void func_15004AAC(BoundsRecord *record, s32 unused) {
    s32 i;
    s32 maximum = 0;
    for (i = 0; i < record->count; i++) {
        s16 vz = record->vertices[i].z;
        f32 x = record->vertices[i].x * record->sx;
        f32 y = record->vertices[i].y * record->sy;
        f32 z = vz * record->sz;
        s32 distance = z * z + (x * x + y * y);
        if (maximum < distance) maximum = distance;
    }
    if (maximum != 0) {
        s32 radius = sqrtf((f32)maximum);
        if (record->radius == 0) {
            record->radius = radius;
            record->maximum = radius;
            D_800BE2A2++;
        } else if (record->radius < radius || record->maximum < radius) {
            D_800BE2A0++;
        } else {
            D_800BE2A4++;
        }
    }
}
/* Search record byte IDs in either direction, retaining saturation fallbacks. */
s32 func_15004BF0(s32 descending) {
    s32 id;
    s32 index;
    /* After choosing direction, retain the scan boundary in the argument. */
    if (descending == 0) {
        id = 1;
        for (index = descending = D_800DBF00; index < D_800DBEF0; index++) {
            if (id == ((ByteIdRecordView *)D_800DBEF4)[index].id) {
                id++;
                index = descending - 1;
            }
            if (id >= 256) { id = 255; break; }
        }
    } else {
        descending = 255 - D_800DBF00;
        id = descending;
        for (index = 0; index < D_800DBEF0; index++) {
            if (id == ((ByteIdRecordView *)D_800DBEF4)[index].id) {
                id--;
                index = -1;
            }
            if (id <= 0) { id = descending; break; }
        }
    }
    return id;
}
void func_15004CE0(s8 *arg0, s32 arg1) {
    s32 i = 0;
    s8 *cur = arg0;
    s32 opcode;

    if (cur[0] != -0x21) {
        opcode = *(volatile s8 *)cur;
        do {
            if ((opcode == -0x24) && ((u8)cur[3] == 0xE) && (*(u32 *)(cur + 4) < 0x80000000U)) {
                *(u32 *)(cur + 4) += arg1;
            }
            i++;
            cur = (s8 *)((u32)arg0 + (i << 3));
            opcode = cur[0];
        } while (opcode != -0x21);
    }
}
