#include <ultra64.h>
#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
void func_1512DD50(struct108 *);
s32 func_1512DEA4();
/* End generated placeholder declarations. */

#ifdef __GNUC__
#define LINE_RECORD_ALIAS __attribute__((__may_alias__))
#else
#define LINE_RECORD_ALIAS
#endif
typedef struct LINE_RECORD_ALIAS { u8 kind; u8 pad01[15]; f32 x,y,z,inverse,first,second,zero28,zero2c; } LineRecord1512DD50;
typedef struct LINE_RECORD_ALIAS { u8 pad00[8]; s32 second; u8 pad0c[0x10]; u32 kind; s32 first; } LineSource1512DD50;
/* Build the inline line record from the owner's position and direction. */
void func_1512DD50(struct108 *owner) {
    f32 dx;
    /* The saved coordinate remains live across the endpoint stores. */
    volatile f32 originZ;
    f32 dy, size, originX, originY;
    LineRecord1512DD50 *record;
    struct17 vector;
    originX = owner->unk70C;
    originY = owner->unk70E;
    originZ = owner->unk710;
    size = owner->unk712;
    dx = owner->unk720 * size;
    dy = owner->unk724 * size;
    size = -dx * owner->unk72C;
    dx = owner->unk728 * dx;
    owner->unk874 = originX - dx;
    owner->unk878 = originY - dy;
    owner->unk87C = originZ - size;
    vector.unk0 = dx + dx;
    vector.unk4 = dy + dy;
    vector.unk8 = size + size;
    size = 1.0f / func_150AD930(&vector.unk0);
    record = (LineRecord1512DD50 *)&owner->unk870;
    record->inverse = size;
    record->x = size * vector.unk0;
    record->y = size * vector.unk4;
    record->z = size * vector.unk8;
    dy = (f32)((LineSource1512DD50 *)&owner->unk6FC)->first; /* Match MIPS signed conversion followed by unsigned adjustment. */
    if (((LineSource1512DD50 *)&owner->unk6FC)->first < 0) dy += 4294967296.0f;
    record->first = dy;
    dy = (f32)((LineSource1512DD50 *)&owner->unk6FC)->second;
    if (((LineSource1512DD50 *)&owner->unk6FC)->second < 0) dy += 4294967296.0f;
    record->second = dy;
    record->zero28 = 0.0f;
    record->zero2c = 0.0f;
    record->kind = ((LineSource1512DD50 *)&owner->unk6FC)->kind;
}
/* Non-matching C placeholders for asm/nonmatchings/game_15B200/func_1512DEA4.s. */
s32 func_1512DEA4() {
    return 0;
}
