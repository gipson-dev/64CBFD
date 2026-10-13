#include <ultra64.h>

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
    if (value == 0x7C) {
        primaryBias = 4;
        secondaryBias = 0;
    } else {
        primaryBias = 0;
        secondaryBias = 2;
    }
    if ((delta = value) == 0x69 || delta == 0x7C) {
        noise = 0;
    } else {
        if (delta == 0x87) {
            noise = 0;
        } else {
            noise = 10;
        }
    }
    limit = 0xFF;
    if (first != limit) {
        if (actor[0x201] == 0) {
            scale = D_80097D40;
        } else {
            scale = (f32)(u32)actor[0x201] * D_80097D44;
        }
        lower = 40;
        delta = actor[0x1FE];
        primaryIndex = first;
        value = (s32)((f32)(u32)delta * scale * D_80097D48);
        if (!suppressed) {
            *(s16 *)output = (u32)primaryIndex * 6 + primaryBias;
            *(s16 *)(output + 2) = value;
            output += 4;
        }
        D_800C3EF0 = value;
        primaryIndex = first;
        value = (s32)((f32)(*(s8 *)(actor + 0x202) * actor[0x1FE] / limit)
            * D_80097D4C * D_80097D50);
        if (!suppressed) {
            *(s16 *)output = (u32)primaryIndex * 6 + secondaryBias;
            *(s16 *)(output + 2) = value;
            output += 4;
        }
        upper = 60;
        if (actor[4] == 0x42) {
            lower = 80;
            upper = 120;
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
            current = value < 256 ? value : limit;
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
                current = *(s16 *)(actor + 0x204);
                if (sign > 0) {
                    if (current < 0 && delta < 0) {
                        reverse = 1;
                    } else if (current == 0 && delta < 0) {
                        choose = 1;
                    } else if (current == limit) {
                        reverse = 1;
                        choose = 1;
                    }
                } else {
                    if (current > 0 && delta > 0) {
                        reverse = 1;
                    } else if (current == 0 && delta > 0) {
                        choose = 1;
                    } else if (current == -255) {
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
        delta = *(s8 *)(actor + 0x209);
        *(s16 *)(actor + 0x204) += delta;
        if (sign > 0) {
            value = *(s16 *)(actor + 0x204);
            if (value < 0 && delta < 0) {
                *(s16 *)(actor + 0x204) = 0;
            } else if (value >= 256) {
                *(s16 *)(actor + 0x204) = limit;
            }
        } else {
            value = *(s16 *)(actor + 0x204);
            if (value > 0 && delta > 0) {
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

s32 func_15034F30() {
    return 0;
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
