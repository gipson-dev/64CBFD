#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/CDE80.s. */

typedef struct {
    s16 origin0;
    s16 origin1;
    s16 origin2;
    u8 pad6[0xF];
    u8 flags;
    u8 pad16;
    u8 field17;
    s32 field18;
    s32 field1C;
    s32 field20;
    f32 coefficient0;
    f32 scale;
    f32 coefficient1;
    f32 coefficient2;
} GeneratedCDE80Record;

extern GeneratedCDE80Record *D_800D3098;
extern s32 D_800D3094;
extern struct108 *D_800DBFF0;
extern f32 D_8009F5A0;
extern f32 D_8009F5A4;

typedef struct {
    u8 pad0[0xC];
    f32 angle0;
    f32 angle1;
    u8 pad14[0x10];
    f32 cosine0;
    f32 sine0;
    f32 cosine1;
    f32 sine1;
} GeneratedCDE80TrigRecord;

typedef GeneratedCDE80Record GeneratedCDE80Plane;

f32 func_150AD780(f32);
f32 func_150AD78C(f32);

s32 func_150A09D0() {
    return 0;
}

void func_150A0D14(GeneratedCDE80TrigRecord *record) {
    f32 angle;

    angle = record->angle0 * D_8009F5A0;
    record->cosine0 = func_150AD78C(angle);
    record->sine0 = func_150AD780(angle);

    angle = record->angle1 * D_8009F5A4;
    record->cosine1 = func_150AD78C(angle);
    record->sine1 = func_150AD780(angle);
}

s32 func_150A0D8C() {
    return 0;
}

s32 func_150A1040(register s32 arg0) {
    return arg0 + 0x400;
}

s32 func_150A104C() {
    return 0;
}

s32 func_150A11C4() {
    return 0;
}

s32 func_150A1DA0(struct127 *arg0, s32 arg1, s32 arg2) {
    return 0;
}

u16 func_1000FA64(u16,s16,s16,s16,s32,u16,s16,s32,void*,s32,s32,s32);
/* Submit an inactive record sound before publishing its active state. */
void func_150A23E4(GeneratedCDE80Record *record) {
    s32 extra;
    s32 mode;
    if (record->field20 == 0) {
        extra = 0;
        mode = 8;
        if ((record->flags & 3) == 0) extra = 0x8000;
        if (record->field17 >> 7) mode = 0x108;
        func_1000FA64((u32)record->field1C >> 16,
            record->origin0, record->origin1, record->origin2,
            (record->field17 & 0x7F) * 327,
            record->field18 | extra, record->field1C & 0xFFFF, 0, 0, 0, mode, 0);
        record->field20 = 1;
    } else {
        record->field20 = 1;
    }
}

s32 func_15183290(s32,s32,s32,u8,s32,s32,s32,s32,s32,s32,s32);

/* Submit eligible records, then publish the live service result or phase floor. */
void func_150A24C0(GeneratedCDE80Record *record, s32 selector) {
    u32 state;
    s32 result;
    s32 property;
    s16 parameter18;
    u8 parameter1A, parameter1C, parameter1D;
    s32 parameter20;
    s16 secondOrigin;
    u8 *bytes = (u8 *)record;
    if (selector != 255) {
        state = (u32)record->field1C;
        if ((state & 255) == 0 || record->field17 == 9) {
            property = record->field18;
            parameter18 = *(s16 *)(bytes + 0x18);
            parameter1A = bytes[0x1A];
            parameter1C = bytes[0x1C];
            parameter1D = bytes[0x1D];
            parameter20 = record->field20;
            secondOrigin = record->origin1;
            result = func_15183290(record->origin0,
                secondOrigin + (parameter1D << 4), record->origin2,
                property & 255, record->field17,
                *(s16 *)(bytes + 6), selector, parameter18,
                parameter1A, parameter1C, parameter20);
            if (result != -1 && record->field17 != 9) {
                record->field1C = (((u32)result << 8) | 0xF0) |
                    ((u32)record->field1C & 0xFFFF0000);
            }
        } else {
            result = (s32)(state & 255);
            if (result < 2) result = 2;
            record->field1C = (state & 0xFFFFFF00) | (u32)result;
        }
    }
}

s32 func_150A25D4() {
    return 0;
}

void func_15172E7C(struct127 *, s32, s32);

/* Dispatch eligible records using the live table and count after each helper. */
void func_150A278C(struct127 *actor) {
    u32 index;

    if (((u8 *)actor)[0x65] == 0) {
        for (index = 0; index < (u32)D_800D3094; index++) {
            if ((D_800D3098[index].flags >> 2) == 8 &&
                func_150A1DA0(actor, (s32)&D_800D3098[index], 0) == 0) {
                func_15172E7C(actor, D_800D3098[index].field17,
                             D_800D3098[index].field18);
            }
        }
    }
}

extern u64 D_800D30F0[];
extern u64 D_800D3270[];

/* Set a resource status byte and clear its bit from each active-set row. */
void func_150A2864(u32 identity, s32 status) {
    u64 *row;
    u32 word;
    u64 shift;

    identity &= 0xFFF;
    if (identity < (u32)D_800D3094) {
        ((u8 *)&D_800D3098[identity])[0x14] = status;
    }
    if (status == 1) {
        for (shift = identity & 0x3F, word = identity >> 6, row = D_800D30F0; ; ) {
            row[word] = row[word] & ~(1ULL << shift);
            row += 3;
            if (row == D_800D3270) break;
        }
    }
}

/* Update optional word/byte parameters and clear field 0x1C. */
void func_150A2940(u32 identity, s32 value, s32 kind) {
    identity &= 0xFFF;
    if (identity < (u32)D_800D3094) {
        if (value != -1) D_800D3098[identity].field18 = value;
        if (kind != -1) D_800D3098[identity].field17 = kind;
        D_800D3098[identity].field1C = 0;
    }
}

/* Query a record through the actor mask or collision provider. */
s32 func_150A29C8(u32 actorIndex, u32 identity) {
    extern u16 D_800D2340;
    extern struct127 D_800CC2D0[];
    identity &= 0xFFF;
    if ((u32)D_800D3094 < identity) return 1;
    if ((u32)actorIndex < 16 && (D_800D2340 & (1 << actorIndex))) {
        if ((((u64 (*)[3])D_800D30F0)[actorIndex][identity >> 6] >>
              (identity & 0x3F)) & 1) {
            return 0;
        } else {
            return 1;
        }
    }
    return func_150A1DA0(&D_800CC2D0[actorIndex],
                          (s32)&D_800D3098[identity], 1);
}

/* Return the first listed record active for this actor, or -1. */
s32 func_150A2AEC(s32 actorIndex, s32 count, s32 *identities) {
    extern u16 D_800D2340;
    extern struct127 D_800CC2D0[];
    s32 i;
    u32 identity;
    if ((u32)actorIndex < 16 && (D_800D2340 & (1 << actorIndex))) {
        for (i = 0; i < count; i++) {
            identity = identities[i] & 0xFFF;
            if (identity < (u32)D_800D3094 &&
                ((((u64 (*)[3])D_800D30F0)[actorIndex][identity >> 6] >>
                  (identity & 0x3F)) & 1)) {
                return identity;
            }
        }
    } else {
        for (i = 0; i < count; i++) {
            identity = identities[i] & 0xFFF;
            if (identity < (u32)D_800D3094 &&
                func_150A1DA0(&D_800CC2D0[actorIndex],
                              (s32)&D_800D3098[identity], 1) == 0) {
                return identity;
            }
        }
    }
    return -1;
}

/* Original active-actor volume occupancy; OGL Note 640. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_CDE80/func_150A2CA4.s")

/* Original view-volume query; OGL Note 545. */
#pragma GLOBAL_ASM("asm/nonmatchings/generated_CDE80/func_150A2D84.s")

// Matched with guarded floating-point allocation and scheduling normalization.
s32 func_150A2E4C(GeneratedCDE80Plane *plane, f32 value0, f32 value1,
                   f32 value2) {
    volatile s16 *origin;
    f32 factor0;
    f32 factor2;
    f32 result;

    origin = &plane->origin0;
    value0 = value0 - origin[0];
    value1 = value1 - origin[1];
    value2 = value1 - origin[2];

    factor2 = plane->coefficient2;
    factor0 = plane->coefficient1;
    result = value2 * factor2 + value0 * factor0;
    factor2 = plane->scale;
    factor0 = plane->coefficient0;
    result = result * factor2 - value1 * factor0;
    if (result <= 0.0f) {
        return 1;
    }
    return 0;
}

extern struct127 D_800CC2D0[26];

/* Test a masked volume selector against the selected actor position. */
s32 func_150A2EE4(s32 actorIndex, s32 selector) {
    selector &= 0xFFF;
    if ((u32)D_800D3094 < (u32)selector) {
        return 1;
    }
    if ((D_800D3098[selector].flags & 3) == 3) {
        return func_150A2E4C(&D_800D3098[selector], D_800CC2D0[actorIndex].x_position,
                            D_800CC2D0[actorIndex].y_position, D_800CC2D0[actorIndex].z_position);
    }
    return 0;
}

/* Test a masked volume selector against the selected view position. */
s32 func_150A2FA4(s32 viewIndex, s32 selector) {
    struct108 *view;

    view = &D_800DBFF0[viewIndex];
    selector &= 0xFFF;
    if ((u32)D_800D3094 < (u32)selector) {
        return 1;
    }
    if ((D_800D3098[selector].flags & 3) == 3) {
        return func_150A2E4C(&D_800D3098[selector], view->unk2F8, view->unk2FC, view->unk300);
    }
    return 0;
}

/* Test whether a class-3 record of this subtype accepts the position. */
s32 func_150A3058(s32 subtype, s16 x, s16 y, s16 z) {
    u32 index;
    struct127 query;
    s32 offset;
    query.x_position = x;
    query.y_position = y;
    query.z_position = z;
    query.old_x_position = x;
    query.unk180 = y;
    query.old_y_position = y;
    query.old_z_position = z;
    for (index = 0, offset = 0; index < (u32)D_800D3094; index++, offset += 0x34) {
        if ((((u8 *)D_800D3098)[offset + 0x14] == 0) &&
            ((((u8 *)D_800D3098)[offset + 0x15] >> 2) == 3) &&
            (((u8 *)D_800D3098)[offset + 0x17] == subtype)) {
            if (func_150A1DA0(&query, offset + (u32)D_800D3098, 0) == 0) return 1;
        }
    }
    return 0;
}

/* Find the first matching record accepted by the position query. */
GeneratedCDE80Record *func_150A3194(s32 kind, s32 subtype, s32 x, s32 y, s32 z) {
    u32 index;
    struct127 query;
    s32 offset;

    query.x_position = x;
    query.y_position = y;
    query.z_position = z;
    query.old_x_position = x;
    query.unk180 = y;
    query.old_y_position = y;
    query.old_z_position = z;

    for (index = 0, offset = 0; index < (u32)D_800D3094; index++, offset += 0x34) {
        if ((((u8 *)D_800D3098)[offset + 0x14] == 0) &&
            ((((u8 *)D_800D3098)[offset + 0x15] >> 2) == kind) &&
            (((u8 *)D_800D3098)[offset + 0x17] == subtype)) {
            if (func_150A1DA0(&query, offset + (s32)D_800D3098, 0) == 0) {
                return (GeneratedCDE80Record *)(offset + (s32)D_800D3098);
            }
        }
    }
    return NULL;
}

s32 func_150A32B4(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct127 query;

    query.x_position = arg1;
    query.y_position = arg2;
    query.z_position = arg3;
    query.old_x_position = arg1;
    query.unk180 = arg2;
    query.old_y_position = arg2;
    query.old_z_position = arg3;

    if (func_150A1DA0(&query, arg0, 0) == 0) {
        return 1;
    }
    return 0;
}

void func_150A3330(s32 arg0, s32 *arg1, s32 *arg2, s32 *arg3, s32 *arg4) {
    *arg1 = D_800D3098[arg0].field17;
    *arg2 = D_800D3098[arg0].field18;
    *arg3 = D_800D3098[arg0].field1C;
    *arg4 = D_800D3098[arg0].field20;
}

/* Update the selected byte and word fields of a 0x34-byte record. */
void func_150A3398(s32 index, u16 mask, s32 value17, s32 value18, s32 value1C, s32 value20) {
    if (mask & 1) {
        D_800D3098[index].field17 = value17;
    }
    if (mask & 2) {
        D_800D3098[index].field18 = value18;
    }
    if (mask & 4) {
        D_800D3098[index].field1C = value1C;
    }
    if (mask & 8) {
        D_800D3098[index].field20 = value20;
    }
}

void func_150A3444(s32 index, s16 arg1, s16 arg2, s16 arg3) {
    D_800D3098[index].origin0 = arg1;
    D_800D3098[index].origin1 = arg2;
    D_800D3098[index].origin2 = arg3;
}

s32 func_150A3504();

s32 func_150A34B0(u8 *arg0) {
    if (arg0[0x14] == 1) {
        return 0;
    }
    if ((arg0[0x15] & 3) == 0) {
        return func_150A3504(arg0);
    }
    return 0;
}

s32 func_150A3504() {
    return 0;
}
