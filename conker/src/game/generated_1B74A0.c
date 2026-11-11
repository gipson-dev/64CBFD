#include <ultra64.h>

typedef s32 (*SubtypeCallback1B74A0)(u8 *, u8 *, s32);
extern SubtypeCallback1B74A0 D_8008D5A0[];
u8 *func_15083E90(s32);
void func_150A7960(f32 *, f32, f32, f32, f32 *, f32 *, f32 *);

extern f32 D_800A73C0,D_800A73C4,D_800A73C8;
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

/* Update attached points and honor the selected subtype callback. */
s32 func_1518A094(u8 *object) {
    u8 *context = object + 0x170;
    u8 *resource;
    u8 *matrix;
    u8 enabled[8];
    s8 subtype;
    if (*(u8 **)(object + 0x188) == 0) {
        resource = func_15083E90(context[0x1D]);
        *(u8 **)(context + 0x18) = resource;
        if (resource == 0) return 0;
    }
    resource = *(u8 **)(context + 0x18);
    if (*(u32 *)resource == 0 || context[0x1D] != resource[0x3B]) goto invalid;
    subtype = *(s8 *)(context + 0x1E);
    if (subtype != -1) {
      if (!D_8008D5A0[subtype](object, &enabled[7], subtype)) return 0;
      if (!enabled[7]) return 1;
      resource = *(u8 **)(context + 0x18);
    }
    matrix = *(u8 **)(resource + 0x1D4);
    if (matrix != 0) {
        matrix += context[0x1C] * 64;
        func_150A7960((f32 *)matrix, *(f32 *)(context + 0), *(f32 *)(context + 4), *(f32 *)(context + 8), (f32 *)(object + 0x34), (f32 *)(object + 0x38), (f32 *)(object + 0x3C));
        func_150A7960((f32 *)matrix, *(f32 *)(context + 0xC), *(f32 *)(context + 0x10), *(f32 *)(context + 0x14), (f32 *)(object + 0x40), (f32 *)(object + 0x44), (f32 *)(object + 0x48));
        *(u32 *)(object + 0x58) |= 2;
        *(u32 *)(object + 0x58) &= ~4;
        return 1;
    } else {
        *(u32 *)(object + 0x58) &= ~2;
    }
    goto success;
invalid:
    return 0;
success:
    return 1;
}

/* Apply the descriptor subtype's scale/color and report its active gate. */
s32 func_1518A214(u8 *object, u8 *enabled) {
    switch (*(u8 *)(*(u8 **)(object + 0x188) + 0x68) - 15) {
    default: {
        f32 scale = D_800A73C0;
        f32 *attributes = (f32 *)(object + 0x110);

        attributes[6] = scale;
        attributes[7] = scale;
        object[0x2A] = 0;
        object[0x29] = 0;
        object[0x28] = 255;
        *enabled = 1;
        break;
    }
    case 0:
        *(u32 *)(object + 0x58) &= ~2;
        *enabled = 0;
        break;
    case 1: {
        f32 scale = D_800A73C4;
        f32 *attributes = (f32 *)(object + 0x110);

        attributes[6] = scale;
        attributes[7] = scale;
        object[0x2A] = 0;
        object[0x29] = 0;
        object[0x28] = 128;
        *enabled = 1;
        break;
    }
    case 2: {
        f32 scale = D_800A73C8;
        f32 *attributes = (f32 *)(object + 0x110);

        attributes[6] = scale;
        attributes[7] = scale;
        object[0x2A] = 0;
        object[0x29] = 0;
        object[0x28] = 255;
        *enabled = 1;
        break;
    }
    }
    return 1;
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
