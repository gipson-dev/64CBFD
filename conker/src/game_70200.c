#include <ultra64.h>
#include "stdarg.h"

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_15043384(s32 arg0);
s32 func_15043A20(u8 *ring, s32 capacity, s32 cursor, u8 *linear, s32 count);
s32 func_15043AC8(u8 *ring, s32 capacity, s32 cursor, u8 *linear, s32 count);
s32 func_15043CA4();
/* End generated placeholder declarations. */

void func_15042D50(void) {
    D_800CBD64 = 0;
    func_15043384(0);
}

void func_15042D78(u8 arg0) {
    D_800CBD74 = arg0;
}

void func_15042ECC(s32 arg0, s32 *arg1);

/* Copy sixteen o32 variadic payload words and submit the text command. */
void func_15042D94(s32 arg0, s32 arg1, u8 arg2, s32 arg3, ...) {
    char *va;
    s32 buf[16];
    s32 i;

    D_800CBD74 = arg2;
    D_800CBD70 = arg0;
    D_800CBD72 = arg1;
    va = (char *) &arg3 + sizeof(arg3);
    for (i = 0; i < 16; i++) {
        va = (char *) (((int) va + 3) & ~3) + 4;
        buf[i] = *(s32 *) (va - 4);
    }
    func_15042ECC(arg3, buf);
}

void func_15042E3C(s32 arg0, ...) {
    va_list args;
    s32 sp24[16];
    s32 i;

    va_start(args, arg0);
    for (i = 0; i < 16; i++) {
        sp24[i] = va_arg(args, s32);
    }
    va_end(args);
    func_15042ECC(arg0, sp24);
}
/* Non-matching C placeholders for asm/nonmatchings/game_70200/func_15042ECC.s. */
void func_15042ECC(s32 arg0, s32 *arg1) {
}

void func_150432BC(f32 arg0) {
    D_800CBD80 = arg0;
}

void func_150432CC(s32 arg0, s32 arg1) {
    D_800CBD74 = D_800CBD74 | 1;
    D_800CBD74 = D_800CBD74;
    D_800CBD7C = arg1;
    D_800CBD78 = arg0;
}

void func_150432FC(s16 arg0, s16 arg1) {
    D_800CBD70 = arg0;
    D_800CBD72 = arg1;
}

void func_1504332C(u8 arg0, u8 arg1, u8 arg2, u8 arg3) {
    D_800CBD60 = arg0;
    D_800CBD61 = arg1;
    D_800CBD62 = arg2;
    D_800CBD63 = arg3;
}

/* Non-matching C placeholders for asm/nonmatchings/game_70200/func_15043384.s. */
s32 func_15043384(s32 arg0) {
    return 0;
}

void func_15043A00(struct105 *arg0, s32 arg1, s32 arg2) {
    if (arg0 != 0) {
        arg0->unk0 = arg1; // are these structs?
        arg0->unk4 = arg2;
        arg0->unkC = 0;
        arg0->unk8 = 0;
    }
}

/* Copy linear bytes into the ring and return its updated cursor. */
s32 func_15043A20(u8 *ring, s32 capacity, s32 cursor, u8 *linear, s32 count) {
    s32 chunk;

    while (count != 0) {
        chunk = capacity < (s32)((u32)cursor + (u32)count) ? (s32)((u32)capacity - (u32)cursor) : count;
        memcpy(ring + cursor, linear, chunk);
        cursor = (s32)((u32)cursor + (u32)chunk);
        linear += chunk;
        count = (s32)((u32)count - (u32)chunk);
        if (cursor >= capacity) {
            cursor = 0;
        }
    }
    return cursor;
}
/* Copy linear bytes from the ring and return its updated cursor. */
s32 func_15043AC8(u8 *ring, s32 capacity, s32 cursor, u8 *linear, s32 count) {
    s32 chunk;

    while (count != 0) {
        chunk = capacity < (s32)((u32)cursor + (u32)count) ? (s32)((u32)capacity - (u32)cursor) : count;
        memcpy(linear, ring + cursor, chunk);
        cursor = (s32)((u32)cursor + (u32)chunk);
        linear += chunk;
        count = (s32)((u32)count - (u32)chunk);
        if (cursor >= capacity) {
            cursor = 0;
        }
    }
    return cursor;
}

s32 func_15043B70(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    s32 tmp;

    while (arg3 != 0) {
        tmp = arg1 < arg2 + arg3 ? arg1 - arg2 : arg3;
        arg2 += tmp;
        arg3 -= tmp;
        if (arg2 >= arg1) {
            arg2 = 0;
        }
    }

    return arg2;
}
/* Non-matching C placeholders for asm/nonmatchings/game_70200/func_15043BB8.s. */
void func_15043BB8(struct105* arg0, void *arg1, s32 arg2) {
}

/* Non-matching C placeholders for asm/nonmatchings/game_70200/func_15043CA4.s. */
s32 func_15043CA4() {
    return 0;
}
