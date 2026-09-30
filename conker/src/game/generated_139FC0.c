#include <ultra64.h>
extern u8 D_800D9ED8[];
extern s8 D_800BC448[];
extern s32 D_800D9F58;
extern s32 D_800D9F5C;
extern u8 D_800D9F68[];
s32 func_10004074();
void func_1510D694(s32 arg0);
void func_1510D720(s32 arg0);

/* Non-matching placeholders for the text-only asm slice asm/139FC0.s. */

s32 func_1510CB10() {
    return 0;
}

s32 func_1510CDB8() {
    return 0;
}

s32 func_1510CE60() {
    return 0;
}

s32 func_1510D0EC() {
    return 0;
}

s32 func_1510D374() {
    return 0;
}

s32 func_1510D404() {
    return 0;
}

void func_1510D608(s32 arg0, s32 arg1) {
    s8 *temp_v0 = D_800BC448 + arg0;
    s8 temp_v1 = *temp_v0;

    if (temp_v1 != 0) {
        *temp_v0 = (temp_v1 & 0x40) | arg1;
    }
}

void func_1510D630(s16 *arg0) {
    s16 *allocation = arg0;
    s32 count = allocation[0];
    s16 *entry = allocation + 1;

    if (count > 0) {
        s16 *end = allocation + count + 1;

        do {
            func_1510D694(*entry);
            entry++;
        } while (end != entry);
    }

    func_10004074(allocation);
}

/* Decrement an indexed activity count and finalize its zero transition. */
void func_1510D694(s32 arg0) {
    u8 *entry;
    u8 value;

    if (D_800BC448[arg0] != 0) {
        entry = &D_800D9F68[arg0];
        value = *entry;
        if (value != 0) {
            *entry = value - 1;
            if (*entry == 0) {
                if (arg0 < D_800D9F58) {
                    D_800D9F58 = arg0;
                }
                if (arg0 > D_800D9F5C) {
                    D_800D9F5C = arg0;
                }
                func_1510D608(arg0, 3);
            }
        }
    }
}

/* Finalize the corresponding countdown transition into state two. */
void func_1510D720(s32 arg0) {
    u8 *entry;
    u8 value;

    if (D_800BC448[arg0] != 0) {
        entry = &D_800D9F68[arg0];
        value = *entry;
        if (value != 0) {
            *entry = value - 1;
            if (*entry == 0) {
                if (arg0 < D_800D9F58) {
                    D_800D9F58 = arg0;
                }
                if (arg0 > D_800D9F5C) {
                    D_800D9F5C = arg0;
                }
                func_1510D608(arg0, 2);
            }
        }
    }
}

s32 func_1510D7AC() {
    return 0;
}

extern u8 D_800D9ED0;

void func_1510D864(void) {
    D_800D9ED0 = 0;
}

void func_1510D874(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    s32 temp_v0 = D_800D9ED0;

    if (temp_v0 < 8) {
        u8 *slot = D_800D9ED8 + temp_v0 * 16;

        *(s32 *) slot = arg0;
        *(s32 *) (slot + 4) = arg1;
        *(s32 *) (slot + 8) = arg2;
        *(slot + 0xC) = arg3;
        *(slot + 0xD) = arg4;
        D_800D9ED0 = temp_v0 + 1;
    }
}

s32 func_1510D8C0() {
    return 0;
}
