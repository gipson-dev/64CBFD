#include <ultra64.h>
s32 func_1509BE40(s32, ...);

/* Non-matching placeholders for the text-only asm slice asm/EBE60.s. */

s32 func_150BE9B0() {
    return 0;
}

s32 func_150BEAA8(s32 arg0, s32 arg1) {
    if ((arg0 == 0) || (arg0 == 1)) {
        return 0x11;
    }
    return -1;
}

s32 func_150BEACC() {
    return 0;
}

s32 func_150BEC30() {
    return 0;
}

s32 func_150BED28(s32 arg0, s32 arg1) {
    if ((arg0 == 0) || (arg0 == 1)) {
        return 0x12;
    }
    return -1;
}

s32 func_150BED4C() {
    return 0;
}

/* Update actor bits 0x1010 and 0x01000000 from event queries. */
void func_150BEEB0(void *actor) {
    if ((func_1509BE40(1, 0x4063, 6, 0x2000) != 0) || (func_1509BE40(1, 0x4001, 6, 0x9000) != 0)) {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) | 0x1010);
    } else {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) & ~0x1010);
    }
    if (func_1509BE40(1, 0x4069, 6, 0x2000) != 0) {
        (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) | 0x01000000);
        return;
    }
    (*(s32 *)((char *)(actor) + 0x84)) = (s32) ((*(s32 *)((char *)(actor) + 0x84)) & 0xFEFFFFFF);
}
