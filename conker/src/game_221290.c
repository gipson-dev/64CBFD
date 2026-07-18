#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_151F3DE0();
s32 func_151F42E8();
s32 func_151F63C4();
s32 func_151F6B28();
s32 func_151F78B4();
s32 func_151F7F60();
s32 func_151F8088(s32 arg0, s32 arg1);
s32 func_151F85C4();
s32 func_151F86B0();
/* End generated placeholder declarations. */

typedef s32 (*func_151F6FD0_ReadFunc)(s32, void *, s32, s32);

s32 func_151F8960(void *arg0, void *arg1, s32 arg2);

extern s32 D_800B06BC[];
extern s32 D_800B0734[];
extern s32 D_800B0B0C[];
extern u8 D_800AEB54[];
extern u8 D_800AEB5C[];
extern u8 D_800AEB6C[];
extern s16 D_800AEB7C[];

#define S32_AT(base, offset) (*(s32 *)((u8 *)(base) + (offset)))

/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F3DE0.s. */
s32 func_151F3DE0() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F42E8.s. */
s32 func_151F42E8() {
    return 0;
}
// NON-MATCHING: bitstream table fill lifted with raw decoder offsets
s32 func_151F4F38(void *arg0, s32 arg1, s32 arg2) {
    u8 *base;
    s32 table_offset;
    s32 sample_base;
    s32 code;
    s32 i;
    s32 j;
    s32 k;
    s32 bit_count;
    s32 group;

    base = arg0;
    table_offset = (arg1 * 4) + (arg2 * 4);
    sample_base = (arg1 * 0xF8) + (arg2 * 0xF8);
    code = S32_AT(base, 0x3C90 + table_offset);

    if ((S32_AT(base, 0x3C98 + table_offset) != 0) && (S32_AT(base, 0x3CA0 + table_offset) == 2)) {
        if (S32_AT(base, 0x3CA8 + table_offset) != 0) {
            for (i = 0; i < 8; i++) {
                bit_count = D_800AEB5C[code];
                if (bit_count != 0) {
                    S32_AT(base, 0x3D08 + sample_base + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                } else {
                    S32_AT(base, 0x3D08 + sample_base + (i * 4)) = 0;
                }
            }

            for (i = 3; i < 6; i++) {
                for (j = 0; j < 3; j++) {
                    bit_count = D_800AEB5C[code];
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = 0;
                    }
                }
            }

            for (i = 6; i < 0xC; i++) {
                for (j = 0; j < 3; j++) {
                    bit_count = D_800AEB6C[code];
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = 0;
                    }
                }
            }
        } else {
            for (k = 0; k < 2; k++) {
                for (i = D_800AEB54[k + 5]; i < D_800AEB54[k + 6]; i++) {
                    for (j = 0; j < 3; j++) {
                        bit_count = D_800AEB5C[(k * 0x10) + code];
                        if (bit_count != 0) {
                            S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                        } else {
                            S32_AT(base, 0x3D64 + sample_base + (j * 0x34) + (i * 4)) = 0;
                        }
                    }
                }
            }
        }

        for (j = 0; j < 3; j++) {
            S32_AT(base, 0x3D94 + sample_base + (j * 0x34)) = 0;
        }
    } else {
        for (k = 0; k < 4; k++) {
            if ((S32_AT(base, 0x3BF8 + (arg2 * 0x80) + (k * 4)) == 0) || (arg1 == 0)) {
                for (i = D_800AEB54[k]; i < D_800AEB54[k + 1]; i++) {
                    if (k < 2) {
                        group = 0;
                    } else {
                        group = 1;
                    }
                    bit_count = D_800AEB5C[(group * 0x10) + code];
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D08 + sample_base + (i * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D08 + sample_base + (i * 4)) = 0;
                    }
                }
            } else {
                for (i = D_800AEB54[k]; i < D_800AEB54[k + 1]; i++) {
                    S32_AT(base, 0x3E00 + (arg2 * 0xF8) + (i * 4)) = S32_AT(base, 0x3D08 + (arg2 * 0xF8) + (i * 4));
                }
            }
        }
        S32_AT(base, 0x3D60 + sample_base) = 0;
    }

    return 1;
}
// NON-MATCHING: table decoder lifted from asm with raw offsets
s32 func_151F578C(void *arg0, s32 arg1, s32 arg2) {
    u8 *base;
    s32 template_data[0x48];
    s32 decode[4];
    s32 row[4];
    s32 code;
    s32 table_class;
    s32 special_mode;
    s32 channel_kind;
    s32 has_extra;
    s32 field_a;
    s32 packed;
    s32 emitted;
    s32 i;
    s32 j;
    s32 bit_count;
    s32 mask;

    (void)arg1;

    base = arg0;
    bcopy(D_800B0B0C, template_data, 0x120);

    code = S32_AT(base, 0x3C90 + (arg2 * 4));
    field_a = S32_AT(base, 0x3CA8 + (arg2 * 4));
    channel_kind = S32_AT(base, 0x3CA0 + (arg2 * 4));
    has_extra = S32_AT(base, 0x3C98 + (arg2 * 4));
    table_class = 0;
    special_mode = 0;

    if (((S32_AT(base, 0x3BC4) != 1) && (S32_AT(base, 0x3BC4) != 3)) || (arg2 != 1)) {
        if (code < 0x190) {
            decode[0] = (code >> 4) / 5;
            decode[1] = (code >> 4) % 5;
            decode[2] = (code % 0x10) >> 2;
            decode[3] = code % 4;
            S32_AT(base, 0x3CF0 + (arg2 * 4)) = 0;
            table_class = 0;
        } else if ((code >= 0x190) && (code < 0x1F4)) {
            decode[0] = ((code - 0x190) >> 2) / 5;
            decode[1] = ((code - 0x190) >> 2) % 5;
            decode[2] = (code - 0x190) % 4;
            decode[3] = 0;
            S32_AT(base, 0x3CF0 + (arg2 * 4)) = 0;
            table_class = 1;
        } else if ((code >= 0x1F4) && (code < 0x200)) {
            decode[0] = (code - 0x1F4) / 3;
            decode[1] = (code - 0x1F4) % 3;
            decode[2] = 0;
            decode[3] = 0;
            S32_AT(base, 0x3CF0 + (arg2 * 4)) = 1;
            table_class = 2;
        }
    }

    if (((S32_AT(base, 0x3BC4) == 1) || (S32_AT(base, 0x3BC4) == 3)) && (arg2 == 1)) {
        S32_AT(base, 0x3EF8) = code % 2;
        packed = code >> 1;
        special_mode = 1;
        if (packed < 0xB4) {
            decode[0] = packed / 0x24;
            decode[1] = (packed % 0x24) / 6;
            decode[2] = (packed % 0x24) % 6;
            decode[3] = 0;
            S32_AT(base, 0x3CF0 + (arg2 * 4)) = 0;
            table_class = 0;
        } else if ((packed >= 0xB4) && (packed < 0xF4)) {
            decode[0] = ((packed - 0xB4) % 0x40) >> 4;
            decode[1] = ((packed - 0xB4) % 0x10) >> 2;
            decode[2] = (packed - 0xB4) % 4;
            decode[3] = 0;
            S32_AT(base, 0x3CF0 + (arg2 * 4)) = 0;
            table_class = 1;
        } else if ((packed >= 0xF4) && (packed < 0xFF)) {
            decode[0] = (packed - 0xF4) / 3;
            decode[1] = (packed - 0xF4) % 3;
            decode[2] = 0;
            decode[3] = 0;
            S32_AT(base, 0x3CF0 + (arg2 * 4)) = 0;
            table_class = 2;
        }
    }

    if ((has_extra != 0) && (channel_kind == 2)) {
        bcopy((u8 *)template_data + (special_mode * 0x90) + (table_class * 0x30) + (field_a * 0x10) + 0x10, row, 0x10);
    } else {
        bcopy((u8 *)template_data + (special_mode * 0x90) + (table_class * 0x30), row, 0x10);
    }

    emitted = 0;
    if ((has_extra == 0) || ((has_extra != 0) && (channel_kind != 2))) {
        for (i = 0; i < 4; i++) {
            bit_count = decode[i];
            mask = (1 << bit_count) - 1;
            for (j = 0; j < row[i]; j++) {
                if (bit_count != 0) {
                    S32_AT(base, 0x3D08 + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                } else {
                    S32_AT(base, 0x3D08 + (arg2 * 0xF8) + (emitted * 4)) = 0;
                }
                if (arg2 != 0) {
                    S32_AT(base, 0x3EFC + (emitted * 4)) = mask;
                }
                emitted++;
            }
        }
    } else if (channel_kind == 2) {
        if (field_a == 0) {
            for (i = 0; i < 4; i++) {
                bit_count = decode[i];
                mask = (1 << bit_count) - 1;
                for (j = 0; j < row[i]; j += 3) {
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D64 + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                        S32_AT(base, 0x3D98 + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                        S32_AT(base, 0x3DCC + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D64 + (arg2 * 0xF8) + (emitted * 4)) = 0;
                        S32_AT(base, 0x3D98 + (arg2 * 0xF8) + (emitted * 4)) = 0;
                        S32_AT(base, 0x3DCC + (arg2 * 0xF8) + (emitted * 4)) = 0;
                    }
                    if (arg2 != 0) {
                        S32_AT(base, 0x3F14 + (emitted * 4)) = mask;
                    }
                    emitted++;
                }
            }
        } else {
            bit_count = decode[0];
            mask = (1 << bit_count) - 1;
            for (j = 0; j < 6; j++) {
                if (bit_count != 0) {
                    S32_AT(base, 0x3D08 + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                } else {
                    S32_AT(base, 0x3D08 + (arg2 * 0xF8) + (emitted * 4)) = 0;
                }
                if (arg2 != 0) {
                    S32_AT(base, 0x3EFC + (emitted * 4)) = mask;
                }
                emitted++;
            }

            row[0] -= 6;
            emitted = 3;
            for (i = 0; i < 4; i++) {
                bit_count = decode[i];
                mask = (1 << bit_count) - 1;
                for (j = 0; j < row[i]; j += 3) {
                    if (bit_count != 0) {
                        S32_AT(base, 0x3D64 + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                        S32_AT(base, 0x3D98 + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                        S32_AT(base, 0x3DCC + (arg2 * 0xF8) + (emitted * 4)) = func_151F8960(base + 0x1C, base + 0x2020, bit_count);
                    } else {
                        S32_AT(base, 0x3D64 + (arg2 * 0xF8) + (emitted * 4)) = 0;
                        S32_AT(base, 0x3D98 + (arg2 * 0xF8) + (emitted * 4)) = 0;
                        S32_AT(base, 0x3DCC + (arg2 * 0xF8) + (emitted * 4)) = 0;
                    }
                    if (arg2 != 0) {
                        S32_AT(base, 0x3F14 + (emitted * 4)) = mask;
                    }
                    emitted++;
                }
            }
        }
    }

    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F63C4.s. */
s32 func_151F63C4() {
    return 0;
}
// NON-MATCHING: coefficient copy/remap over raw decoder buffers
s32 func_151F6970(void *arg0, s32 arg1) {
    u8 *base;
    f32 *src;
    f32 *dst;
    f32 *map_dst;
    s16 *map;
    s32 map_offset;
    s32 i;

    base = arg0;
    src = (f32 *)(base + 0x4664);
    dst = (f32 *)(base + 0x4F64);
    map_offset = (S32_AT(base, 0x3BA4) * 0xD80) + (S32_AT(base, 0x3BB4) * 0x480);
    map = (s16 *)((u8 *)D_800AEB7C + map_offset);

    i = 0;
    if ((S32_AT(base, 0x3C98 + (arg1 * 4)) != 0) && (S32_AT(base, 0x3CA0 + (arg1 * 4)) == 2)) {
        if (S32_AT(base, 0x3CA8 + (arg1 * 4)) != 0) {
            for (; i < 0x24; i++) {
                dst[i] = src[i];
            }
        }
        map_dst = dst + i;
        for (; i < 0x240; i++) {
            map_dst[map[i]] = src[i];
        }
    } else {
        for (; i < 0x240; i++) {
            dst[i] = src[i];
        }
    }

    return 1;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F6B28.s. */
s32 func_151F6B28() {
    return 0;
}

// NON-MATCHING: opaque asset-loader struct, offset overlay for first C pass
s32 func_151F6FD0(void *arg0) {
    u8 *base;
    void *read_base;
    void *read_state;
    func_151F6FD0_ReadFunc read_func;
    s32 count;
    s32 i;
    s32 j;
    s32 k;
    s32 field_size;
    s32 table_offset;
    s32 table_stride;

    base = arg0;
    if (S32_AT(base, 0x3BA4) != 0) {
        if (S32_AT(base, 0x3BC0) == 3) {
            S32_AT(base, 0x206C) = 0x11;
        } else {
            S32_AT(base, 0x206C) = 0x20;
        }
    } else if (S32_AT(base, 0x3BC0) == 3) {
        S32_AT(base, 0x206C) = 9;
    } else {
        S32_AT(base, 0x206C) = 0x11;
    }

    read_func = (func_151F6FD0_ReadFunc)S32_AT(base, 4);
    count = read_func(S32_AT(base, 0), base + S32_AT(base, 0x2068) + 0x2024, S32_AT(base, 0x206C), -1);
    if (S32_AT(base, 0x206C) != count) {
        return 0;
    }
    S32_AT(base, 0x18) += S32_AT(base, 0x206C);

    if (S32_AT(base, 0x3BC0) == 3) {
        S32_AT(base, 0x3F8C) = 1;
    } else {
        S32_AT(base, 0x3F8C) = 2;
    }
    if (S32_AT(base, 0x3BA4) != 0) {
        S32_AT(base, 0x3F90) = 2;
    } else {
        S32_AT(base, 0x3F90) = 1;
    }

    read_base = base + 0x2024;
    read_state = base + 0x2064;
    if (S32_AT(base, 0x3BA4) != 0) {
        S32_AT(base, 0x3BF4) = func_151F8960(read_base, read_state, 9);
        if (S32_AT(base, 0x3F8C) == 1) {
            func_151F8960(read_base, read_state, 5);
        } else {
            func_151F8960(read_base, read_state, 3);
        }
    } else {
        S32_AT(base, 0x3BF4) = func_151F8960(read_base, read_state, 8);
        if (S32_AT(base, 0x3F8C) == 1) {
            func_151F8960(read_base, read_state, 1);
        } else {
            func_151F8960(read_base, read_state, 2);
        }
    }

    if (S32_AT(base, 0x3BA4) != 0) {
        for (i = 0; i < S32_AT(base, 0x3F8C); i++) {
            for (j = 0; j < 4; j++) {
                S32_AT(base, 0x3BF8 + (i * 0x80) + (j * 4)) = func_151F8960(read_base, read_state, 1);
            }
        }
    }

    if (S32_AT(base, 0x3BA4) != 0) {
        field_size = 4;
    } else {
        field_size = 9;
    }

    for (i = 0; i < S32_AT(base, 0x3F90); i++) {
        for (j = 0; j < S32_AT(base, 0x3F8C); j++) {
            table_offset = (i * 4) + (j * 4);
            S32_AT(base, 0x3C78 + table_offset) = func_151F8960(read_base, read_state, 0xC);
            S32_AT(base, 0x3C80 + table_offset) = func_151F8960(read_base, read_state, 9);
            S32_AT(base, 0x3C88 + table_offset) = func_151F8960(read_base, read_state, 8);
            if (field_size != 0) {
                S32_AT(base, 0x3C90 + table_offset) = func_151F8960(read_base, read_state, field_size);
            } else {
                S32_AT(base, 0x3C90 + table_offset) = 0;
            }
            S32_AT(base, 0x3C98 + table_offset) = func_151F8960(read_base, read_state, 1);
            table_stride = (i * 0xC) + (j * 0xC);
            if (S32_AT(base, 0x3C98 + table_offset) != 0) {
                S32_AT(base, 0x3CA0 + table_offset) = func_151F8960(read_base, read_state, 2);
                S32_AT(base, 0x3CA8 + table_offset) = func_151F8960(read_base, read_state, 1);
                for (k = 0; k < 2; k++) {
                    S32_AT(base, 0x3CB0 + table_stride + (k * 4)) = func_151F8960(read_base, read_state, 5);
                }
                S32_AT(base, 0x3CB8 + table_stride) = 0;
                for (k = 0; k < 3; k++) {
                    S32_AT(base, 0x3CC8 + table_stride + (k * 4)) = func_151F8960(read_base, read_state, 3);
                }
            } else {
                S32_AT(base, 0x3CA0 + table_offset) = 0;
                S32_AT(base, 0x3CA8 + table_offset) = 0;
                for (k = 0; k < 3; k++) {
                    S32_AT(base, 0x3CB0 + table_stride + (k * 4)) = func_151F8960(read_base, read_state, 5);
                }
                S32_AT(base, 0x3CE0 + table_offset) = func_151F8960(read_base, read_state, 4);
                S32_AT(base, 0x3CE8 + table_offset) = func_151F8960(read_base, read_state, 3);
            }
            if (S32_AT(base, 0x3BA4) != 0) {
                S32_AT(base, 0x3CF0 + table_offset) = func_151F8960(read_base, read_state, 1);
            }
            S32_AT(base, 0x3CF8 + table_offset) = func_151F8960(read_base, read_state, 1);
            S32_AT(base, 0x3D00 + table_offset) = func_151F8960(read_base, read_state, 1);
        }
    }

    S32_AT(base, 0x3F7C) = D_800B06BC[(S32_AT(base, 0x3BA4) * 15) + S32_AT(base, 0x3BB0)];
    S32_AT(base, 0x3F80) = D_800B0734[(S32_AT(base, 0x3BA4) * 4) + S32_AT(base, 0x3BB4)];
    if (S32_AT(base, 0x3BA4) != 0) {
        S32_AT(base, 0x3F84) = (S32_AT(base, 0x3F7C) * 0x90) / S32_AT(base, 0x3F80);
    } else {
        S32_AT(base, 0x3F84) = (S32_AT(base, 0x3F7C) * 0x48) / S32_AT(base, 0x3F80);
    }
    S32_AT(base, 0x3F88) = (S32_AT(base, 0x3F84) + S32_AT(base, 0x3BB8)) - (S32_AT(base, 0x2068) + S32_AT(base, 0x206C));
    return 1;
}

/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F78B4.s. */
s32 func_151F78B4() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F7F60.s. */
s32 func_151F7F60() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F8088.s. */
s32 func_151F8088(s32 arg0, s32 arg1) {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F85C4.s. */
s32 func_151F85C4() {
    return 0;
}
// void *func_151F85C4(s32 arg0, s32 arg1, s32 arg2) {
//     void *sp1C;
//
//     sp1C = (void *)0x800E1880;
//     if (sp1C == 0) {
//         return NULL;
//     }
//     sp1C->unkC = -1;
//     sp1C->unk10 = -1;
//     sp1C->unk14 = -1;
//     sp1C->unk0 = arg0;
//     sp1C->unk4 = arg1;
//     sp1C->unk8 = arg2;
//     sp1C->unk201C = 0;
//     sp1C->unk2020 = 0;
//     sp1C->unk3BA0 = 0;
//     if (func_151F8088(sp1C, 0) == 0) {
//         return NULL;
//     }
//     sp1C->unk8474 = 0;
//     bzero(sp1C + 0x6A64, 0x900);
//     return sp1C;
// }

/* Non-matching C placeholders for asm/nonmatchings/game_221290/func_151F86B0.s. */
s32 func_151F86B0() {
    return 0;
}

#undef S32_AT
