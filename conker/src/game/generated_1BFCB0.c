#include <ultra64.h>

/* Actor-class dispatch and row selection for asm/1BFCB0.s. */

typedef void (*ClassCallback1BFCB0)(u8 *);
extern ClassCallback1BFCB0 *D_8008F860[];
extern s32 D_800BE9F0;
s32 func_151928B0(u8 *, s32 *);
s32 func_1510F8CC(s32);

/* Dispatch the actor's class callback for its type and current world. */
void func_15192800(void *actor, s32 unused) {
    s32 row;
    s32 column;
    s32 kind;
    ClassCallback1BFCB0 callback;

    if (actor != NULL && func_151928B0(actor, &row)) {
        kind = func_1510F8CC(*(s32 *)((u8 *)actor + 0x184));
        switch (kind) {
            case 5:
                if (D_800BE9F0 == 0x14) {
                    column = 2;
                } else {
                    column = 1;
                }
                break;
            case 6:
                column = 3;
                break;
            default:
                column = 1;
                break;
        }
        callback = D_8008F860[row][column];
        if (callback != NULL) {
            callback(actor);
        }
    }
}

s32 func_151928B0(u8 *arg0, s32 *arg1) {
    s32 result = 0;

    switch (arg0[4]) {
        case 0:
        case 1:
        case 2:
        case 3:
        case 4:
            result = 1;
            *arg1 = 0;
            break;
        case 0x53:
            result = 1;
            *arg1 = 1;
            break;
    }

    return result;
}
