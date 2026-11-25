#include <ultra64.h>

/* Recovered record queries and remaining placeholders from asm/1188E0.s. */

typedef struct {
    s16 origin0;
    s16 origin1;
    s16 origin2;
    s16 radius;
    s16 heightOffset;
    u8 padA[6];
    f32 parameter10;
    u8 disabled;
    u8 flags;
    u8 pad16;
    u8 field17;
    s32 field18;
    s32 field1C;
    u32 field20;
    f32 coefficient0;
    f32 scale;
    f32 coefficient1;
    f32 coefficient2;
} GeneratedCDE80Record;

extern GeneratedCDE80Record *D_800D3098;
extern s32 D_80088AA0[];
extern s32 D_80088AB0[];
/* The float immediately following the eight-index secondary table. */
extern f32 D_80088AD0;
u8 *func_15083E90(u8);
s32 func_150A34B0(u8 *, f32 *, f32 *, f32 *);
void func_150A2864(u32, s32);
s32 func_150EBC80(u8 *, u8, s32);

s32 func_150EB484(f32 *, f32 *, f32 *);

void func_150EB430(f32 *arg0, f32 *arg1, f32 *output) {
    f32 sum[3];

    sum[0] = arg1[0] + arg0[0];
    sum[1] = arg1[1] + arg0[1];
    sum[2] = arg1[2] + arg0[2];
    func_150EB484(arg0, sum, output);
}

/* Test the priority group first, retaining its selected index across callbacks.
 * The null-context fallback marks record 76 but still returns zero. */
s32 func_150EB484(f32 *start, f32 *end, f32 *output) {
    u8 *context;
    s32 *cursor;
    s32 i;
    s32 index;

    context = func_15083E90(9);
    if (context != NULL) {
        cursor = D_80088AA0;
        for (i = 0; i < 4; i++, cursor++) {
            index = *cursor;
            if (func_150A34B0((u8 *)&D_800D3098[index], start, end, output)) {
                func_150A2864(index, 1);
                *(s32 *)(context + 0x2E8) = i + 1;
                func_150EBC80((u8 *)&D_800D3098[index], 255, 1);
                return 1;
            }
        }
        cursor = D_80088AB0;
        do {
            if (func_150A34B0((u8 *)&D_800D3098[*cursor], start, end, output)) {
                return 1;
            }
            cursor++;
        } while (cursor != (s32 *)&D_80088AD0);
    } else if (func_150A34B0((u8 *)&D_800D3098[76], start, end, output)) {
        D_800D3098[76].field18 = 1;
    }
    return 0;
}


s32 func_150EB614() {
    return 0;
}

s32 func_150EB8C4() {
    return 0;
}

s32 func_150EBC80(u8 *record, u8 effect, s32 active) {
    return 0;
}
