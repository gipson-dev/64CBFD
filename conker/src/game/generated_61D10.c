#include <ultra64.h>

void func_150A7A48(f32 [4][4], f32 [4][4], f32 [4][4]);
void func_150A8050(f32 [4][4], f32, f32, f32);
s32 func_150AD960(s32, s32, s32, s32);
void func_15034728(u8 *);
void guMtxF2L2(f32 [4][4], Mtx *);

s32 func_150ADA20(void);
f32 fabsf(f32);
#pragma intrinsic (fabsf)
extern s32 D_800BE9E4;
extern s16 D_800C3EF0;
extern f32 D_80097D40, D_80097D44, D_80097D48, D_80097D4C;
extern f32 D_80097D50, D_80097D54, D_80097D58, D_80097D5C;

/* Non-matching placeholders for the text-only asm slice asm/61D10.s. */

extern u8 D_800C3F00;
extern s16 D_800C3EF0;
extern f32 D_80097D60;

s32 func_15034860(u8 *output, u8 *actor, s32 first, s32 second) {
    s32 primaryIndex;
    s32 suppressed;
    s32 secondaryBias;
    s32 limit;
    s32 lower;
    s32 upper;
    s32 primaryBias;
    s32 current;
    s32 noise;
    s32 sign;
    s32 choose;
    s32 reverse;
    s32 delta;
    s16 value = actor[4];
    f32 scale;
    f32 magnitude;

    if (value == 0x70) {
        suppressed = 1;
    } else {
        suppressed = 0;
    }
    if ((u32)value == 0x7CU) {
        primaryBias = 4;
        secondaryBias = 0;
    } else {
        primaryBias = 0;
        secondaryBias = 2;
    }
    if ((u32)(delta = value) != 0x69U && (u32)delta != 0x7CU && (u32)delta != 0x87U) {
        noise = 10;
    } else {
        noise = 0;
    }
    limit = 0xFF;
    if (first != limit) {
        if (actor[0x201] == 0) {
            scale = D_80097D40;
        } else {
            scale = (f32)(u32)actor[0x201] * D_80097D44;
        }
        primaryIndex = first;
        value = (s32)((f32)(u32)actor[0x1FE] * scale * D_80097D48);
        lower = 40;
        if (!suppressed) {
            *(s16 *)output = (u32)primaryIndex * 6 + primaryBias;
            *(s16 *)(output + 2) = value;
            output += 4;
        }
        D_800C3EF0 = value;
        primaryIndex = first;
        value = (s32)((f32)(actor[0x1FE] * *(s8 *)(actor + 0x202) / limit)
            * D_80097D4C * D_80097D50);
        if (!suppressed) {
            *(s16 *)output = (u32)primaryIndex * 6 + secondaryBias;
            *(s16 *)(output + 2) = value;
            output += 4;
        }
        if (actor[4] == 0x42) {
            lower = 80;
            upper = 120;
        } else {
            upper = 60;
        }
        if (actor[0x1FF] == 0) {
            *(s8 *)(actor + 0x203) = -upper;
        } else if (actor[0x1FF] == 2) {
            *(s8 *)(actor + 0x203) = upper;
            *(s8 *)(actor + 0x202) = 0;
        } else {
            if (*(s8 *)(actor + 0x203) == 0 ||
                actor[0x1FE] == 0 || actor[0x1FE] == limit) {
                *(s8 *)(actor + 0x203) =
                    (u32)func_150ADA20() % (upper - lower) + lower;
                if (actor[0x1FE] == limit) {
                    *(s8 *)(actor + 0x203) = -*(s8 *)(actor + 0x203);
                } else if (actor[0x1FE] == 0 && noise != 0) {
                    *(s8 *)(actor + 0x202) =
                        (u32)func_150ADA20() % (noise * 2) - noise;
                }
            }
        }
        value = actor[0x1FE] + *(s8 *)(actor + 0x203);
        if (value < 0) {
            value = 0;
        } else {
            current = value >= 256 ? limit : value;
            value = current;
        }
        actor[0x1FE] = value;
        if (actor[0x1FF] == 3) {
            if (actor[0x200] >= D_800BE9E4) {
                actor[0x200] = (u32)actor[0x200] - (u32)D_800BE9E4;
            } else {
                actor[0x200] = 0;
                actor[0x1FF] = 0;
            }
        }
    }
    if (second != limit) {
        if (*(s8 *)(actor + 0x208) == 0) {
            scale = D_80097D54;
        } else {
            scale = (f32)*(s8 *)(actor + 0x208) * D_80097D58;
        }
        if (scale < 0.0f) {
            sign = -1;
        } else {
            sign = 1;
        }
        magnitude = fabsf(scale);
        delta = (s32)((f32)*(s16 *)(actor + 0x204) * magnitude * D_80097D5C);
        *(s16 *)output = (u32)second * 6 + primaryBias;
        *(s16 *)(output + 2) = -delta;
        output += 4;
        choose = 0;
        reverse = 0;
        if (actor[0x206] == 0) {
            *(s8 *)(actor + 0x209) = sign > 0 ? -60 : 60;
        } else if (actor[0x206] == 2) {
            *(s8 *)(actor + 0x209) = sign > 0 ? 60 : -60;
        } else {
            delta = *(s8 *)(actor + 0x209);
            if (delta == 0) {
                choose = 1;
            } else {
                value = *(s16 *)(actor + 0x204);
                if (sign > 0) {
                    if (value < 0 && delta < 0) {
                        reverse = 1;
                    } else if (value == 0 && delta < 0) {
                        choose = 1;
                    } else if (value == limit) {
                        reverse = 1;
                        choose = 1;
                    }
                } else {
                    if (value > 0 && delta > 0) {
                        reverse = 1;
                    } else if (value == 0 && delta > 0) {
                        choose = 1;
                    } else if (value == -255) {
                        reverse = 1;
                        choose = 1;
                    }
                }
            }
        }
        if (choose) {
            *(s8 *)(actor + 0x209) = (u32)func_150ADA20() % 20 + 40;
            *(s8 *)(actor + 0x209) = *(s8 *)(actor + 0x209) * sign;
        }
        if (reverse) {
            *(s8 *)(actor + 0x209) = -*(s8 *)(actor + 0x209);
        }
        *(s16 *)(actor + 0x204) += *(s8 *)(actor + 0x209);
        if (sign > 0) {
            value = *(s16 *)(actor + 0x204);
            if (value < 0 && *(s8 *)(actor + 0x209) < 0) {
                *(s16 *)(actor + 0x204) = 0;
            } else if (value >= 256) {
                *(s16 *)(actor + 0x204) = limit;
            }
        } else {
            value = *(s16 *)(actor + 0x204);
            if (value > 0 && *(s8 *)(actor + 0x209) > 0) {
                *(s16 *)(actor + 0x204) = 0;
            } else if (value < -255) {
                *(s16 *)(actor + 0x204) = -255;
            }
        }
        if (actor[0x206] == 3) {
            if (actor[0x207] >= D_800BE9E4) {
                actor[0x207] = (u32)actor[0x207] - (u32)D_800BE9E4;
            } else {
                actor[0x207] = 0;
                actor[0x206] = 0;
            }
        }
    }
    return (s32)output;
}

void func_15034EB4(u8 *arg0, s32 arg1, s32 arg2) {
    u8 *records;
    f32 amount;

    if (D_800C3EF0 != 0) {
        amount = (f32) D_800C3EF0 * D_80097D60 * *(f32 *) (arg0 + 0x14C);
        records = *(u8 **) (arg0 + 0x1D4);
        *(f32 *) (records + arg1 * 0x40 + 0x34) -= amount;
        if (arg2 != -1) {
            *(f32 *) (records + arg2 * 0x40 + 0x34) -= amount;
        }
    }
}

void func_15034F20(void) {
    D_800C3F00 = 0;
}

void func_15034F30(u8 *actor, u8 *record, volatile s32 mode, Mtx *input,
    u8 *volatile output, volatile s32 count, f32 pivotX, f32 pivotY, f32 pivotZ, f32 unused,
    f32 angle, f32 pointX, f32 pointY, f32 pointZ, f32 nearDistance,
    f32 farDistance, f32 opacity, s32 inputFixed, s32 outputFixed) {
    f32 reflection[4][4];
    f32 rotationMinus[4][4];
    f32 rotationPlus[4][4];
    f32 (*matrix)[4];
    u32 actorFlags;
    u8 *cursor;
    f32 converted[4][4];
    s32 i;
    s32 offset;
    s32 firstMode;
    f32 distance;

    guMtxIdentF(reflection);
    firstMode = mode;
    if (firstMode == 1) goto primary;
    offset = mode;
    if (firstMode != 0) goto secondary_check;
primary:
    {
        reflection[1][1] = -1.0f;
        i = 0;
        if (count > 0) {
        offset = 0;
        cursor = output;
        do {
            if (inputFixed != 0) {
                guMtxL2F(converted, (Mtx *)(&input[i]));
                matrix = converted;
            } else {
                matrix = (f32 (*)[4])((u8 *)input + offset);
                matrix[0][3] = 0.0f;
                matrix[1][3] = 0.0f;
                matrix[2][3] = 0.0f;
                matrix[3][3] = 1.0f;
                matrix = (f32 (*)[4])(&input[i]);
            }
            func_150A7A48(matrix, reflection, ((f32 (*)[4])cursor));
            distance = matrix[3][1];
            ((f32 (*)[4])cursor)[3][1] = distance - ((distance - pivotY) + (distance - pivotY));
            if (outputFixed != 0) {
                matrix = (f32 (*)[4])((u8 *)&((Mtx *)output)[i]);
                bcopy(matrix, converted, 64);
                guMtxF2L2(converted, (Mtx *)matrix);
            }
            offset += 64;
            cursor += 64;
            i++;
        } while (i != count);
        }
        distance = pointY - pivotY;
        if (farDistance < distance) {
            record[4] = 0;
        } else {
            firstMode = mode;
            if (distance < nearDistance) {
            if (firstMode == 0) {
                nearDistance = 10.0f;
                if (distance < nearDistance) {
                    record[4] = (u32)((opacity / nearDistance) * distance);
                } else {
                    record[4] = (u32)opacity;
                }
            } else {
                record[4] = (u32)opacity;
            }
        } else {
            record[4] = (u32)(opacity - ((opacity * (distance - nearDistance)) /
                (farDistance - nearDistance)));
        }
        }
    }
    goto finish;
secondary_check:
    if (offset != 2) return;
    {
        reflection[0][0] = -1.0f;
        func_150A8050(rotationMinus, 0.0f, -angle, 0.0f);
        func_150A8050(rotationPlus, 0.0f, angle, 0.0f);
        firstMode = count;
        i = 0;
        offset = 0;
        cursor = output;
        if (firstMode > 0) {
        do {
            if (inputFixed != 0) {
                guMtxL2F(converted, (Mtx *)(&input[i]));
                matrix = converted;
            } else {
                matrix = (f32 (*)[4])((u8 *)input + offset);
                matrix[0][3] = 0.0f;
                matrix[1][3] = 0.0f;
                matrix[2][3] = 0.0f;
                matrix[3][3] = 1.0f;
                matrix = (f32 (*)[4])(&input[i]);
            }
            bcopy(matrix, ((f32 (*)[4])cursor), 64);
            ((f32 (*)[4])cursor)[3][0] -= pivotX;
            ((f32 (*)[4])cursor)[3][1] -= pivotY;
            ((f32 (*)[4])cursor)[3][2] -= pivotZ;
            func_150A7A48(((f32 (*)[4])cursor), rotationMinus, ((f32 (*)[4])cursor));
            func_150A7A48(((f32 (*)[4])cursor), reflection, ((f32 (*)[4])cursor));
            func_150A7A48(((f32 (*)[4])cursor), rotationPlus, ((f32 (*)[4])cursor));
            ((f32 (*)[4])cursor)[3][0] += pivotX;
            ((f32 (*)[4])cursor)[3][1] += pivotY;
            ((f32 (*)[4])cursor)[3][2] += pivotZ;
            if (outputFixed != 0) {
                matrix = (f32 (*)[4])((u8 *)&((Mtx *)output)[i]);
                bcopy(matrix, converted, 64);
                guMtxF2L2(converted, (Mtx *)matrix);
            }
            offset += 64;
            cursor += 64;
            i++;
        } while (i != count);
        }
        distance = (f32)func_150AD960((s32)pivotX, (s32)pivotZ,
            (s32)pointX, (s32)pointZ);
        if (farDistance < distance) {
            record[4] = 0;
        } else if (distance < nearDistance) {
            record[4] = (u32)opacity;
        } else {
            record[4] = (u32)(opacity - ((opacity * (distance - nearDistance)) /
                (farDistance - nearDistance)));
        }
    }
finish:
    if (actor != 0) {
        actorFlags = *(u32 *)(actor + 0x9C);
        matrix = (f32 (*)[4])output;
        if (actorFlags != 0) {
            cursor = *(u8 **)(actor + 0x1D4);
            *(f32 (**)[4])(actor + 0x1D4) = matrix;
            func_15034728(actor);
            *(u8 **)(actor + 0x1D4) = cursor;
        }
    }
}

u8 *func_150356C8(void) {
    extern u8 D_800C3F08[];
    u8 val = D_800C3F00;

    if (val == 15) {
        return 0;
    }
    val++;
    D_800C3F00 = val;
    return D_800C3F08 + (val - 1) * 12;
}

s32 func_15035714() {
    return 0;
}

s32 func_15035808() {
    return 0;
}

s32 func_15035D6C() {
    return 0;
}

s32 func_15035FE8() {
    return 0;
}

s32 func_15036148() {
    return 0;
}
