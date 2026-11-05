#include <ultra64.h>

extern u8 D_800DF7D0[];
extern s16 *D_800DF9B8[];
extern s32 *D_800E0148[];

void func_1510D630(s16 *);
void func_100043B4(s32 *, u32);

void *func_1502B6BC(s32 *, s32, s32 *, s32, ...);
s32 func_1510CE60(void *, s32, s32, s32, s32 *);
void func_15168E54(void *, void *);

/* Non-matching placeholders for the text-only asm slice asm/1B9DB0.s. */

/* Load a cached resource on first use and retain its saturating byte count. */
s32 func_1518C900(s32 kind) {
    s32 *resource;
    u8 *count = &D_800DF7D0[kind];

    if (*count == 0) {
        resource = func_1502B6BC(NULL, 0, NULL, 2, 9, kind);
        if (resource == NULL) {
            return 0;
        }
        func_1510CE60((void *)resource[0], 0, 1, 0x3E,
                      (s32 *)&D_800DF9B8[kind]);
        func_15168E54((void *)resource[0], resource);
        D_800E0148[kind] = resource;
    } else {
        resource = D_800E0148[kind];
    }
    if (*count != 0xFF) {
        (*count)++;
    }
    return resource[0];
}

void func_1518CA04(s32 arg0) {
    if (arg0 == 0x1E4) {
        return;
    }

    if ((D_800DF7D0[arg0] != 0) && (--D_800DF7D0[arg0] == 0)) {
        func_1510D630(D_800DF9B8[arg0]);
        func_100043B4(D_800E0148[arg0], 4);
    }
}
