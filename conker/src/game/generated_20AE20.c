#include <ultra64.h>
#include "structs.h"
extern s8 D_8008FD90;
extern s8 D_8008FD8C;
extern s8 D_800E0BEB;
extern s8 D_800E0C00[];
extern u8 D_800BE616;
extern u8 D_8008FE28;
extern u8 D_800E0B98;
extern u8 D_800E0B97;
extern s32 D_800E0A90;
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
s32 func_151E530C();
s32 func_151DE85C();

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
extern s8 D_8008FE54[23];
s8 D_800E0BE0[23];
extern u8 D_800AB570[];
extern u8 D_800E0B95;

void func_151E557C(void);
void func_151E6BFC(void);
s32 func_151E55A8();
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

s32 func_151DDBA0() {
    return 0;
}

s32 func_151DDC20() {
    return 0;
}

s32 func_151DE6D4() {
    return 0;
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

s32 func_151DE85C() {
    return 0;
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

s32 func_151E22BC() {
    return 0;
}

s32 func_151E2404() {
    return 0;
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

s32 func_151E327C() {
    return 0;
}

s32 func_151E3344() {
    return 0;
}

s32 func_151E4264() {
    return 0;
}

s32 func_151E4314() {
    return 0;
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

s32 func_151E4E64() {
    return 0;
}

s32 func_151E4EE8() {
    return 0;
}

s32 func_151E5034() {
    return 0;
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

s32 func_151E51EC() {
    return 0;
}

s32 func_151E530C() {
    return 0;
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

s32 func_151E55A8() {
    return 0;
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

s32 func_151E7DC0() {
    return 0;
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
