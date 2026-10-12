#include <ultra64.h>
#include "variables.h"
extern f32 D_80098918;
extern f32 D_8009891C;
f32 func_150AD930(f32 *);
void func_15049148(struct17 *, f32, struct17 *);
void func_150AD8B0(f32 *, f32 *, f32 *);
f32 func_150AD900(f32 *, f32 *);
f32 func_150487E0(f32);
f32 func_150AD780(f32);
f32 func_150484A0(f32, f32);
extern u8 D_800C3E90;
void *memcpy(void *, const void *, unsigned int);
extern u8 D_800C666C[];
extern f32 D_80098928;
extern f32 D_8009892C;
void func_1510F800(s32);
s32 func_1510F8D8(s32, s32, s32, s32);
void func_1503EB78(struct04 *, f32, f32, s32);
extern f32 D_80098920;
extern f32 D_80098924;
s32 func_150ADA20(void);
extern u8 D_800CC364[];
extern s32 *D_8008446C[];
void func_1503DF0C(s32, s32, s32, s32);
extern u8 D_800C6664[];
extern u8 D_800C6668[];
extern u8 D_80098914[];
extern s8 *D_80084454[];
extern void (*D_80084430[])(struct04 *, s32);
extern void (*D_8008443C[])(s32);
extern void (*D_80084448[])(s32);
s32 allocate_memory(s32, s32, s32, s32);
s32 func_1503E1F4(s32, s32);
void func_1503E3C4(s32, s32, s32, struct04 *, s32);
void func_150499A0(f32 [4][4], f32 [4][4]);
void func_150A7A48(f32 [4][4], f32 [4][4], f32 [4][4]);
void func_1503E5F8(f32 [4][4], f32 *, f32 *, f32 *, f32 *, f32 *, f32 *, f32 *, f32 *, f32 *);
void func_1503EA54(s32);
void func_1503E82C(s32);
void func_150A7DA0(f32 [4][4], u32, u32, u32);
void func_150A8050(f32 [4][4], f32, f32, f32);
void func_150A7CB0(u32 *, u32, u32, u32);
void func_15043EC8(f32 [4][4], f32, f32, f32, f32, f32, f32);
extern u8 *D_80084460[];
void func_10004074(void *);

/* Non-matching placeholders for the text-only asm slice asm/6B320.s. */

void func_1503DE70(struct127 *actor, s32 group, s32 entry) {
    if (entry != -1) {
        func_1503DF0C(((s32)actor - (s32)D_800CC2D0) / (s32)sizeof(struct127),
            group, ((s32 (*)[2])D_8008446C[group])[entry][0], ((s32 (*)[2])D_8008446C[group])[entry][1]);
    } else {
        func_1503DF0C(((s32)actor - (s32)D_800CC2D0) / (s32)sizeof(struct127),
            group, -1, -1);
    }
}

void func_1503DF0C(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    struct106 *ptr = &D_800C6660[arg0];

    ptr->unk4 |= arg2;
    ptr->unk8 |= arg3;
    ((u8 *) ptr)[0xE] = arg1;
    ptr->unkF = 2;
}

void func_1503DF48(s32 slot) {
    struct106 *record = &D_800C6660[slot];
    struct04 *element;
    struct04 *buffer;
    s8 *types;
    s32 state = record->unkF;
    s32 count;
    s32 index;

    if (state == 2) {
        D_800CC2D0[slot].unk74 |= 0x80;
        state = 3;
        if (D_800CC2D0[slot].unk1D4 == NULL) {
            return;
        }
    }
    if (state == 3) {
        count = D_80098914[((u8 *)record)[0xE]];
        if (record->unk0 == 0) {
            buffer = (struct04 *)allocate_memory(count * sizeof(struct04), 1, 0, 0);
            if (buffer == NULL) {
                return;
            }
            record->unk0 = (s32)buffer;
            for (index = 0; index < count; index++) {
                buffer[index].unk64 = 0;
            }
        }
        types = D_80084454[((u8 *)record)[0xE]];
        for (index = 0; index < count; index++) {
            switch (types[index]) {
            case -2:
                break;
            default:
                element = (struct04 *)record->unk0 + index;
                if (func_1503E1F4(index, slot) != 0 && element->unk64 == 0) {
                    func_1503E3C4(slot, index, 0, element, 0);
                    D_80084430[((u8 *)record)[0xE]](element, slot);
                    element->unk64 = 1;
                }
                break;
            }
        }
        D_8008443C[((u8 *)record)[0xE]](slot);
        state = 1;
        record->unkF = 1;
    }
    if (state == 1) {
        D_80084448[((u8 *)record)[0xE]](slot);
        if (record->unkF != 0) {
            func_1503EA54(slot);
            func_1503E82C(slot);
        }
    }
}

s32 func_1503E1F4(s32 bit, s32 index) {
    if (bit < 0x20) {
        if ((D_800C6660[index].unk4 & (1 << bit)) != 0) {
            return 1;
        }
    } else if ((D_800C6660[index].unk8 & (1 << bit)) != 0) {
        return 1;
    }

    return 0;
}

void func_1503E260(s32 slot) {
    struct106 *record = &D_800C6660[slot];
    u8 *bits;
    s32 count;
    s32 index;

    if (record->unkF != 0) {
        bits = D_80084460[((u8 *)record)[0xE]];
        if (bits != NULL) {
            count = D_80098914[((u8 *)record)[0xE]];
            for (index = 0; index < count; index++) {
                if (bits[index] != 255 && func_1503E1F4(index, slot) != 0) {
                    D_800CC2D0[slot].unk94 |= 1U << bits[index];
                }
            }
        }
        record->unkF = 0;
        if (record->unk0 != 0) {
            func_10004074((void *)record->unk0);
        }
        record->unk0 = 0;
        D_800CC2D0[slot].unk74 &= ~0x80;
    }
}

void func_1503E3C4(s32 slot, s32 index, s32 offset, struct04 *record, s32 absolute) {
    s32 type;
    f32 matrix[4][4];
    f32 inverse[4][4];
    struct127 *actor;
    f32 x;
    f32 y;
    f32 z;
    f32 length;

    actor = &D_800CC2D0[slot];
    bcopy((f32 (*)[4][4])actor->unk1D4 + (index + offset), matrix, sizeof(matrix));
    if (absolute != 0) {
        type = -1;
    } else {
        type = D_80084454[((u8 *)&D_800C6660[slot])[0xE]][index];
    }
    if (type != -1) {
        func_150499A0(((f32 (*)[4][4])actor->unk1D4)[type], inverse);
        matrix[1][3] = 0.0f;
        matrix[0][3] = 0.0f;
        matrix[2][3] = 0.0f;
        matrix[3][3] = 1.0f;
        func_150A7A48(matrix, inverse, matrix);
    }
    func_1503E5F8(matrix, &((f32 *)record)[0], &((f32 *)record)[1], &((f32 *)record)[2],
        &((f32 *)record)[3], &((f32 *)record)[4], &((f32 *)record)[5], &((f32 *)record)[6], &((f32 *)record)[7], &((f32 *)record)[8]);
    ((f32 *)record)[9] = ((f32 *)record)[0];
    ((f32 *)record)[10] = ((f32 *)record)[1];
    ((f32 *)record)[11] = ((f32 *)record)[2];
    ((f32 *)record)[12] = ((f32 *)record)[3];
    ((f32 *)record)[13] = ((f32 *)record)[4];
    ((f32 *)record)[14] = ((f32 *)record)[5];
    ((f32 *)record)[15] = ((f32 *)record)[6];
    ((f32 *)record)[16] = ((f32 *)record)[7];
    ((f32 *)record)[17] = ((f32 *)record)[8];
    x = ((f32 *)record)[9] - actor->x_position;
    y = ((f32 *)record)[10] - actor->y_position - 30.0f;
    z = ((f32 *)record)[11] - actor->z_position;
    length = sqrtf(x*x + y*y + z*z);
    if (length == 0.0f) {
        length = 1.0f;
    }
    length = 1.0f / length;
    ((f32 *)record)[18] = x * length;
    ((f32 *)record)[19] = y * length;
    ((f32 *)record)[20] = z * length;
}

void func_1503E5F8(f32 input[4][4], f32 *x, f32 *y, f32 *z,
    f32 *rx, f32 *ry, f32 *rz, f32 *sx, f32 *sy, f32 *sz) {
    f32 matrix[4][4];
    f32 cross[4];
    f32 (*row)[4];
    f32 (*middle)[4];
    f32 length;
    f32 factor;
    f32 fallback;
    f32 angleX;
    f32 angleY;
    f32 angleZ;

    bcopy(input, matrix, sizeof(matrix));
    *x = matrix[3][0];
    *y = matrix[3][1];
    *z = matrix[3][2];
    fallback = D_80098918;
    middle = matrix + 1;
    for (row = matrix; row < matrix + 3; row++) {
        length = func_150AD930(*row);
        if (length == 0.0f) {
            length = fallback;
        }
        if (row == matrix) {
            *sx = length;
        } else if (row == middle) {
            *sy = length;
        } else {
            *sz = length;
        }
        func_15049148((struct17 *)row, 1.0f / length, (struct17 *)row);
    }
    func_150AD8B0(matrix[1], matrix[2], cross);
    if (func_150AD900(matrix[0], cross) < 0.0f) {
        *sx = -*sx;
        *sy = -*sy;
        *sz = -*sz;
        for (row = matrix; row != matrix + 3; row++) {
            (*row)[0] = -(*row)[0];
            (*row)[1] = -(*row)[1];
            (*row)[2] = -(*row)[2];
        }
    }
    angleY = func_150487E0(-matrix[0][2]);
    if (func_150AD780(angleY) != 0.0f) {
        angleX = func_150484A0(matrix[1][2], matrix[2][2]);
        angleZ = func_150484A0(matrix[0][1], matrix[0][0]);
    } else {
        angleX = func_150484A0(matrix[1][0], matrix[1][1]);
        angleZ = 0.0f;
    }
    factor = D_8009891C;
    *rx = angleX * factor;
    *ry = angleY * factor;
    *rz = angleZ * factor;
}

void func_1503E82C(s32 slot) {
    s32 count;
    f32 (*destination)[4];
    s8 *types;
    s32 index;
    s32 type;
    f32 matrix[4][4];

    if (D_800CC2D0[slot].unk1D4 != NULL) {
        struct04 *element;
        count = D_80098914[((u8 *)&D_800C6660[slot])[0xE]];
        types = D_80084454[((u8 *)&D_800C6660[slot])[0xE]];
        for (index = 0; index < count; index++) {
            switch (types[index]) {
            case -2:
                break;
            default:
                element = (struct04 *)D_800C6660[slot].unk0 + index;
                if (element->unk64 != 0) {
                    destination = ((f32 (*)[4][4])D_800CC2D0[slot].unk1D4)[index];
                    type = D_80084454[((u8 *)&D_800C6660[slot])[0xE]][index];
                    if (type != -1) {
                        func_150A7DA0(matrix, ((u32 *)element)[9], ((u32 *)element)[10], ((u32 *)element)[11]);
                        func_150A7A48(matrix, ((f32 (*)[4][4])D_800CC2D0[slot].unk1D4)[type], matrix);
                        element = (struct04 *)D_800C6660[slot].unk0 + index;
                        func_150A8050(destination, ((f32 *)element)[12], ((f32 *)element)[13], ((f32 *)element)[14]);
                        func_150A7A48(destination, matrix, destination);
                        element = (struct04 *)D_800C6660[slot].unk0 + index;
                        func_150A7CB0((u32 *)matrix, element->unk3C, element->unk40, element->unk44);
                        func_150A7A48(matrix, destination, destination);
                    } else {
                        func_150A8050(destination, ((f32 *)element)[12], ((f32 *)element)[13], ((f32 *)element)[14]);
                        element = (struct04 *)D_800C6660[slot].unk0 + index;
                        func_15043EC8(destination, ((f32 *)element)[15], ((f32 *)element)[16], ((f32 *)element)[17],
                            ((f32 *)element)[9], ((f32 *)element)[10], ((f32 *)element)[11]);
                    }
                }
                break;
            }
        }
    }
}

void func_1503EA54(s32 slot) {
    s32 count = D_80098914[((u8 *)&D_800C6660[slot])[0xE]];
    f32 step = D_800BE9E4;
    s32 index;
    struct04 *element;

    for (index = 0; index < count; index++) {
        if (((struct04 *)D_800C6660[slot].unk0)[index].unk64 != 0 && D_80084454[((u8 *)&D_800C6660[slot])[0xE]][index] == -1) {
            element = (struct04 *)D_800C6660[slot].unk0 + index;
            ((f32 *)element)[9] += ((f32 *)element)[18] * step;
            ((f32 *)element)[10] += ((f32 *)element)[19] * step;
            ((f32 *)element)[11] += ((f32 *)element)[20] * step;
            ((f32 *)element)[12] += ((f32 *)element)[21] * step;
            ((f32 *)element)[13] += ((f32 *)element)[22] * step;
            ((f32 *)element)[14] += ((f32 *)element)[23] * step;
            ((f32 *)element)[19] += ((f32 *)element)[24] * step;
        }
    }
}

void func_1503EB78(struct04 *record, f32 horizontal, f32 vertical, s32 mode) {
    s32 mask;
    f32 scales[3];
    s32 bias;
    s32 index;

    if (mode != 0) {
        mask = 0x80;
        bias = 0x7F;
    } else {
        mask = 0xFF;
        bias = 0;
    }
    horizontal *= D_80098920;
    vertical *= D_80098920;
    scales[0] = horizontal;
    scales[2] = horizontal;
    scales[1] = vertical;
    for (index = 0; index < 3; index++) {
        ((f32 *)record)[18 + index] *= ((func_150ADA20() & mask) + bias) * scales[index] + 2.0f;
    }
    for (index = 0; index < 3; index++) {
        ((f32 *)record)[21 + index] = ((func_150ADA20() & 0xFF) - 0x80) * 0.03125f;
    }
    ((f32 *)record)[24] = D_80098924;
}

void func_1503ECA0(s32 slot) {
    struct106 *control;
    struct04 *element;
    s32 count;
    s32 index;
    f32 height;
    f32 angularDamping;
    f32 linearDamping;

    func_1510F800(0);
    control = &D_800C6660[slot];
    count = D_80098914[((u8 *)control)[0xE]];
    index = 0;
    if (count > 0) {
        angularDamping = D_80098928;
        linearDamping = D_8009892C;
        do {
            if (((struct04 *)control->unk0)[index].unk64 != 0) {
                element = (struct04 *)control->unk0 + index;
                if (D_80084454[((u8 *)control)[0xE]][index] == -1 &&
                        ((f32 *)element)[24] != 0.0f) {
                    height = func_1510F8D8((s32)((f32 *)element)[9],
                        (s32)((f32 *)element)[10], (s32)((f32 *)element)[11], 0) + 5;
                    if (((f32 *)element)[10] < height) {
                        ((f32 *)element)[10] = height;
                        if (((f32 *)element)[19] < -4.0f) {
                            ((f32 *)element)[18] *= linearDamping;
                            ((f32 *)element)[19] *= -0.5f;
                            ((f32 *)element)[20] *= linearDamping;
                            ((f32 *)element)[21] *= -1.0f;
                            ((f32 *)element)[22] *= angularDamping;
                            ((f32 *)element)[23] *= -1.0f;
                        } else {
                            ((f32 *)element)[23] = 0.0f;
                            ((f32 *)element)[22] = 0.0f;
                            ((f32 *)element)[21] = 0.0f;
                            ((f32 *)element)[24] = 0.0f;
                            ((f32 *)element)[20] = 0.0f;
                            ((f32 *)element)[19] = 0.0f;
                            ((f32 *)element)[18] = 0.0f;
                        }
                    }
                }
            }
            index++;
        } while (index != count);
    }
}

void func_1503EEB8() {
}

s32 func_1503EEC0(s32 index) {
    struct106 *entry;
    s32 value;

    func_1503ECA0(index);
    entry = &D_800C6660[index];
    value = *(s16 *)((u8 *)entry + 0xC) - D_800BE9E4;
    *(s16 *)((u8 *)entry + 0xC) = value;

    if (value <= 0) {
        func_15060F28(&D_800CC2D0[index], 1);
    }
}

s32 func_1503EF4C(s32 arg0, s32 arg1, s32 arg2) {
    s32 *base;
    s32 *entry;
    s32 first;
    s32 entry_offset;
    s32 mask_offset;

    base = D_8008446C[arg0];
    entry_offset = arg1 * 8;
    mask_offset = arg2 * 0x10;
    entry = (s32 *) ((u8 *) base + entry_offset);
    first = entry[0];

    if (first == 0 ||
            (*(s32 *) (D_800C6664 + mask_offset) & first) != 0) {
        s32 second = entry[1];

        if (second == 0 ||
                (*(s32 *) (D_800C6668 + mask_offset) & second) != 0) {
            return 1;
        }
    }
    return 0;
}

void func_1503EFC4(s32 slot) {
    struct106 *control = &D_800C6660[slot];
    s32 count;
    s32 index;

    *(s16 *)((u8 *)control + 0xC) = 120;
    count = D_80098914[((u8 *)control)[0xE]];
    for (index = 0; index < count; index++) {
        ((f32 *)((struct04 *)control->unk0 + index))[19] = (s32)((u32)func_150ADA20() % 20) - 5;
    }
}

void func_1503F078(struct04 *arg0, s32 arg1) {
    func_1503EB78(arg0, 2.0f, 2.0f, 0);
}

void func_1503F0AC(struct04 *arg0, s32 arg1) {
    func_1503EB78(arg0, 1.0f, 2.0f, 1);
}

void func_1503F0D8(struct04 *arg0, s32 arg1) {
    func_1503EB78(arg0, 2.06f, 3.0f, 1);
}

void func_1503F108(s32 arg0) {
    struct106 *entry = &D_800C6660[arg0];

    *(s16 *) ((u8 *) entry + 0xC) = 0x8C;
    *(s32 *) (D_800CC364 + arg0 * sizeof(struct127)) = 6;
    *(f32 *) (entry->unk0 + 0x1EC) = 10.0f;
}

void func_1503F16C(s32 slot) {
    *(s16 *)(D_800C666C + slot * 0x10) = 300;
    if (func_1503EF4C(2, 0, slot) != 0) {
        D_800CC2D0[slot].unk94 |= 0x40;
        D_800CC2D0[slot].unk94 &= ~0x200;
    }
    if (func_1503EF4C(2, 1, slot) != 0) {
        D_800CC2D0[slot].unk94 |= 0x80;
        D_800CC2D0[slot].unk94 &= ~0x100;
    }
    if (func_1503EF4C(2, 2, slot) != 0) {
        D_800CC2D0[slot].unk94 &= ~0x400;
    }
}

void func_1503F2B0(s32 slot) {
    struct106 *control;

    func_1503ECA0(slot);
    control = &D_800C6660[slot];
    *(s16 *)((u8 *)control + 0xC) -= D_800BE9E4;
    if (*(s16 *)((u8 *)control + 0xC) <= 0) {
        func_1503E260(slot);
        if (func_1503EF4C(2, 0, slot) != 0) {
            D_800CC2D0[slot].unk94 |= 8;
        }
        if (func_1503EF4C(2, 1, slot) != 0) {
            D_800CC2D0[slot].unk94 |= 4;
        }
        if (func_1503EF4C(2, 2, slot) != 0) {
            D_800CC2D0[slot].unk94 |= 2;
        }
    }
}

void func_1503F404(void *input, f32 *x, f32 *y, f32 *z,
    f32 *rx, f32 *ry, f32 *rz, f32 *sx, f32 *sy, f32 *sz) {
    f32 matrix[4][4];

    if (D_800C3E90 != 0) {
        guMtxL2F(matrix, (Mtx *)input);
    } else {
        memcpy(matrix, input, sizeof(matrix));
    }
    func_1503E5F8(matrix, x, y, z, rx, ry, rz, sx, sy, sz);
}
