#include <ultra64.h>
u8 *func_151407D0(void *, s32, u8 *, u8, u8, u8, u8, s8, u8, s32);
void *memcpy(void *, const void *, size_t);


/* Non-matching placeholders for the text-only asm slice asm/1B74A0.s. */

/* Set source subtype 0x0B, create the object, and copy its runtime block. */
u8 *func_15189FF0(u8 *descriptor, u8 *source, const void *runtime,
                  u8 kind, u8 mode, u8 first, u8 variant) {
    u8 *result;

    source[0x58] = 0x0B;
    result = func_151407D0(source, 0x80, descriptor, kind, mode, first, variant, -1, 0xFF, 1);
    if (result != NULL) {
        memcpy(result + 0x170, runtime, 0x20);
        goto return_created;
    }
    goto return_null;
return_created:
    return result;
return_null:
    return NULL;
}

s32 func_1518A094() {
    return 0;
}

s32 func_1518A214() {
    return 0;
}

s32 func_1518A2E8(u8 *arg0, u8 *arg1) {
    if (*(*(u8 **) (arg0 + 0x188) + 0x6A) != 0) {
        *(u32 *) (arg0 + 0x58) &= ~2;
        *arg1 = 0;
    } else {
        *arg1 = 1;
    }
    return 1;
}

s32 func_1518A324(u8 *arg0, u8 *arg1) {
    if (*(*(u8 **) (arg0 + 0x188) + 0x6F) == 0) {
        *(u32 *) (arg0 + 0x58) &= ~2;
        *arg1 = 0;
    } else {
        *arg1 = 1;
    }
    return 1;
}

// Matched with guarded commutative branch operand normalization.
void func_1518A360(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *temp_v0 = arg0 + 0x170;

    if (arg2 == 0x2D) {
        s32 temp_v1 = *(s32 *)arg1;
        s32 temp_a2 = *(s32 *)(temp_v0 + 0x18);

        if (temp_v1 == temp_a2) {
            *(s32 *)(temp_v0 + 0x18) = *(s32 *)(arg1 + 4);
            temp_v0[0x1D] = arg1[9];
        } else if (*(s32 *)(arg1 + 4) == temp_a2) {
            *(s32 *)(temp_v0 + 0x18) = temp_v1;
            temp_v0[0x1D] = arg1[8];
        }
    }
}
