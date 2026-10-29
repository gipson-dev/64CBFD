#include <ultra64.h>

extern f32 D_800A2D9C;
f32 sqrtf(f32);
s32 func_1510E388(void *, void *, f32 *, f32 *);

/* Non-matching placeholders for the text-only asm slice asm/13BB20.s. */

extern u8 *D_800DBE48;
extern f32 D_800A2D50;
extern f32 D_800A2D54;
extern f32 D_800A2D58;
extern f32 D_800A2D5C;
void func_150A49F4(s32 context);
extern void func_1510E950(s32, s32, s32, s32, s32, s32, s32, f32, f32, f32,
                          f32, u16, s32, f32, f32, s32);

s32 func_1510E670() {
    return 0;
}

void func_1510E7A4(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5,
                   f32 arg6, f32 arg7, f32 arg8, f32 arg9, u16 arg10, s32 arg11,
                   f32 arg12, f32 arg13) {
    func_1510E950(arg0, arg1, 0, arg2, arg3, arg4, arg5, arg6, arg7, arg8,
                  arg9, arg10, arg11, arg12, arg13, 0);
}

void func_1510E82C(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5,
                   f32 arg6, f32 arg7, f32 arg8, f32 arg9, u16 arg10, s32 arg11) {
    func_1510E950(arg0, arg1, 0, arg2, arg3, arg4, arg5, arg6, arg7, arg8,
                  arg9, arg10, arg11, D_800A2D50, D_800A2D54, 0);
}

void func_1510E8BC(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5,
                   f32 arg6, f32 arg7, f32 arg8, f32 arg9, u16 arg10, s32 arg11,
                   s32 arg12, s32 arg13, s32 arg14) {
    func_1510E950(arg0, arg1, 0, arg2, arg3, arg4, arg5, arg6, arg7, arg8,
                  arg9, arg10, arg11, D_800A2D58, D_800A2D5C, arg14);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_13BB20/func_1510E950.s")

extern u8 D_800D3830[];
extern s32 D_800D3300;
extern f32 D_800A2D98;
void func_1510F800(s32);
s32 func_150A64C8(s16, s16, s32 *, s32);
void func_150A44F0(s32, void *, s32);
s32 func_150A43E0(s32, s32, s32, void *);

/* Return the coordinate query's scaled result, or its fallback value. */
f32 func_1510F648(f32 x, f32 y, f32 z) {
    s32 intX, intZ, value;
    f32 result;

    func_1510F800(2);
    intX = x;
    intZ = z;
    func_150A64C8(intX, intZ, &value, (s32)y);
    func_150A44F0(value, D_800D3830, 0);
    if (func_150A43E0(intX, intZ, value, D_800D3830)) {
        result = D_800D3300 * (1.0f / 256.0f);
    } else {
        result = D_800A2D98;
    }
    return result;
}

s32 func_1510F720() {
    return 0;
}

void func_1510F800(s32 context) {
    func_150A49F4(context);
}

/* Resolve the plane components and normalize their scaled length. */
void func_1510F820(void *indirectVertices, void *packedVertices,
                   f32 *directionA, f32 *directionB, f32 *unusedOutput,
                   f32 *rawA, f32 *rawB) {
    f32 first, second, length;

    func_1510E388(indirectVertices, packedVertices, &first, &second);
    length = sqrtf(first * first + second * second);
    *rawA = first;
    *rawB = second;
    length *= D_800A2D9C;
    if (length == 0.0f) {
        *directionA = 1.0f;
        *directionB = 0.0f;
    } else {
        *directionA = first / length;
        *directionB = second / length;
    }
}

/* Extract the low five bits of the incoming word. */
u32 func_1510F8CC(u32 value) {
    return value & 0x1F;
}

s32 func_1510F8D8() {
    return 0;
}

s32 func_1510FC34() {
    return 0;
}

s32 func_1510FD20() {
    return 0;
}

s32 func_1510FE30(u8 *arg0) {
    u8 *current = D_800DBE48;
    s32 index = 0;
    s16 offset;

    while (current != NULL) {
        if (current == arg0) {
            return index;
        }

        offset = *(s16 *)(current + 0xC);
        if (offset != 0) {
            current += offset;
        } else {
            offset = *(s16 *)(current + 4);
            current += offset;
            if (offset != 0) {
                index++;
            } else {
                current = NULL;
            }
        }
    }

    return 0;
}
