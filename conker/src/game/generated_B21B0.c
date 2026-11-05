#include <ultra64.h>
#include "structs.h"

extern struct127 D_800CC2D0[26];
extern u8 D_800D18A8;


/* Non-matching placeholders for the text-only asm slice asm/B21B0.s. */

typedef struct {
    u8 pad[0x11B];
    u8 value;
} GeneratedB21B0Target;

typedef struct {
    u8 pad[0x31C];
    GeneratedB21B0Target *target;
} GeneratedB21B0Owner;

extern u8 D_8009D954[];
extern u8 *D_80087240[];

s32 func_15084D00(u8 *arg0) {
    s32 value = arg0[4];
    s32 group;
    s32 i;

    for (group = 0; group < 7; group++) {
        for (i = 0; i < D_8009D954[group]; i++) {
            if (value == D_80087240[group][i]) {
                return D_80087240[group][0];
            }
        }
    }

    return value;
}

s32 func_15084D70() {
    return 0;
}

void func_15085410(GeneratedB21B0Owner *arg0, s32 arg1) {
    arg0->target->value = arg1;
}

u8 func_15085420(GeneratedB21B0Owner *arg0) {
    return arg0->target->value;
}

s32 func_15085430() {
    return 0;
}

s32 func_15085710() {
    return 0;
}

/* The six field labels are offset views of 0x1C-byte status records. */
typedef struct { s32 value; u8 padding[24]; } StatusWordB21B0;
typedef struct { s8 value; u8 padding[27]; } StatusSignedByteB21B0;
typedef struct { u8 value; u8 padding[27]; } StatusUnsignedByteB21B0;
extern s16 D_800D2340;
extern StatusWordB21B0 D_800D213C[], D_800D2140[], D_800D2148[];
extern StatusSignedByteB21B0 D_800D2144[], D_800D2145[];
extern StatusUnsignedByteB21B0 D_800D2146[];

/* Read one of the seven status fields; slots at least 255 return zero. */
s32 func_150859AC(s16 slot, s16 field) {
    if (slot >= 255) return 0;
    switch (field) {
        case 0: return (u16)D_800D2340 & (1u << slot);
        case 1: return D_800D213C[slot].value;
        case 2: return D_800D2140[slot].value;
        case 3: return D_800D2144[slot].value;
        case 4: return D_800D2145[slot].value;
        case 5: return D_800D2146[slot].value;
        case 6: return D_800D2148[slot].value;
    }
    /* Other selectors have the retail routine's unspecified result. */
}

/* Publish each selected player's current health to its status record. */
void func_15085ABC(s16 mask) {
    s32 slot;

    if (!D_800D18A8) {
        for (slot = 0; slot < 4; slot++) {
            if ((1 << slot) & mask) {
                func_15085710((s16)slot, 5, D_800CC2D0[slot].health);
            }
        }
    }
}
