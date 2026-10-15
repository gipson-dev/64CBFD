#include <ultra64.h>
#include "structs.h"

extern s32 (*D_8008CBA0[])(u8 *record);
void func_1516972C(struct102 *record);

typedef struct ByteTable11_19A8B0 {
    u8 values[11];
} ByteTable11_19A8B0;

extern ByteTable11_19A8B0 D_8008CBC4;
extern ByteTable11_19A8B0 D_8008CBD0;
extern ByteTable11_19A8B0 D_8008CBDC;
extern ByteTable11_19A8B0 D_8008CBE8;
void func_1516F864(u8 *record);
void func_1516F94C(u8 *record, u32 scale);

extern s32 D_800BE9E4;
extern u8 D_800DD2A0;
extern u8 D_800CC2D4[];
extern u8 D_800A6E00[];
extern u8 D_800A6E0C[];

void *func_15167A68(s32, s32, s32, s32, u8, u8);
struct PositionScaleRecord71820;
struct PositionScaleRecord71820 *func_150448D0(s32, s32, s32, s32, s32, s32,
                                               s32, s16 *, s16 *);

/* Non-matching placeholders for the text-only asm slice asm/19A8B0.s. */

s32 func_1516D400() {
    return 0;
}

/* Initialize a packed record and optionally bind its position/scale fields. */
void func_1516D4E8(
    s16 arg0, s16 arg1, s16 arg2, u8 arg3, u8 arg4, u8 arg5,
    u8 arg6, u8 arg7, u8 arg8, u8 arg9, u8 arg10, u8 arg11,
    u8 arg12, u8 arg13, u8 arg14, u8 arg15, u8 arg16, u8 arg17,
    u8 arg18, u8 arg19, u8 arg20, u8 arg21, u8 arg22, s16 arg23,
    s16 arg24, u8 arg25, s16 arg26, s32 arg27, s32 arg28, u8 arg29,
    s32 arg30) {
    u8 *record;
    s32 kind;

    if (arg27 != 0) {
        kind = 0x67;
    } else {
        kind = 0x12;
    }
    record = func_15167A68(kind, arg30, 0x34, 0, arg29, 1);
    if (record != NULL) {
        *(s16 *)(record + 0xE) = arg0;
        *(s16 *)(record + 0x10) = arg1;
        *(s16 *)(record + 0x12) = arg2;
        record[0x1A] = arg3;
        record[0x1B] = arg4;
        record[0x1C] = arg5;
        record[0x1D] = arg6;
        record[0x1E] = arg7;
        record[0x1F] = arg8;
        record[0x20] = arg9;
        record[0x21] = arg10;
        record[0x22] = arg11;
        record[0x23] = arg12;
        *(s16 *)(record + 0x14) = arg23;
        *(s16 *)(record + 0x16) = arg24;
        record[0x24] = arg25;
        *(s16 *)(record + 0x18) = arg26;
        record[0x25] = 0;
        record[0x26] = arg13;
        record[0x27] = arg14;
        record[0x28] = arg15;
        record[0x29] = arg16;
        record[0x2A] = arg17;
        record[0x2B] = arg18;
        record[0x2C] = arg19;
        record[0x2D] = arg20;
        record[0x2E] = arg21;
        record[0x2F] = arg22;
        if (arg28 != 0) {
            *(struct PositionScaleRecord71820 **)(record + 0x30) = func_150448D0(
                -1, 0, arg28, 0x14, 0x14, 0x14, 0,
                (s16 *)(record + 0xE), (s16 *)(record + 0x14));
            return;
        }
        *(struct PositionScaleRecord71820 **)(record + 0x30) = NULL;
    }
}

/* Dispatch the packed record; remove only on 1, otherwise advance 24.8 Y.
 * Three expected-word guards preserve the final temporary and operand order. */
void func_1516D678(u8 *record) {
    s32 value = record[0x24];
    u8 *binding;
    s32 fixed;

    if (value != 0) {
        value = (s32)((u32)value - (u32)D_800BE9E4);
        if (value < 0) {
            value = 0;
        }
        record[0x24] = value;
    }
    if (D_8008CBA0[record[0x23]](record) == 1) {
        binding = *(u8 **)(record + 0x30);
        if (binding != NULL) {
            *(s16 *)(binding + 4) = 0;
        }
        func_1516972C((struct102 *)record);
        return;
    }
    value = *(s16 *)(record + 0x10);
    value = value * 256;
    value += record[0x25];
    fixed = (s32)((u32)value + (u32)(s32)*(s16 *)(record + 0x18) * (u32)D_800BE9E4);
    *(s16 *)(record + 0x10) = (s32)fixed >> 8;
    record[0x25] = fixed;
}

s32 func_1516D738() {
    return 0;
}

/* Initialize a packed 0x4C-byte record; cap arg41 for the alternate kind.
 * Six expected-word guards preserve two independent load/store schedules. */
void func_1516D99C(
    s16 arg0, s16 arg1, s16 arg2, u8 arg3, u8 arg4, u8 arg5,
    u8 arg6, u8 arg7, u8 arg8, u8 arg9, u8 arg10, u8 arg11,
    u8 arg12, u8 arg13, u8 arg14, u8 arg15, u8 arg16, u8 arg17,
    u8 arg18, u8 arg19, u8 arg20, u8 arg21, u8 arg22, u8 arg23,
    u8 arg24, u8 arg25, u8 arg26, s16 arg27, s16 arg28, s16 arg29,
    s16 arg30, u16 arg31, u8 arg32, u8 arg33, u8 arg34, u8 arg35,
    s16 arg36, u16 arg37, u16 arg38, u8 arg39, u8 arg40, u8 arg41,
    u8 arg42, u8 arg43, s32 arg44, u8 arg45, u8 arg46, s32 arg47,
    s32 arg48) {
    s32 kind;
    u8 *record;

    if (arg44 != 0) {
        kind = 0x66;
    } else {
        kind = 0x11;
    }
    /* The flag stays a word at the caller ABI; read its big-endian low byte. */
    record = func_15167A68(kind, arg48, 0x4C, 0, ((u8 *)&arg47)[3], 1);
    if (record != NULL) {
        *(s16 *)(record + 0xE) = arg0;
        *(s16 *)(record + 0x10) = arg1;
        *(s16 *)(record + 0x12) = arg2;
        *(s16 *)(record + 0x14) = arg27;
        *(s16 *)(record + 0x16) = arg28;
        *(s16 *)(record + 0x18) = arg29;
        *(s16 *)(record + 0x1A) = arg30;
        record[0x24] = arg3;
        record[0x25] = arg4;
        record[0x26] = arg5;
        record[0x27] = arg6;
        record[0x28] = arg7;
        record[0x2A] = arg9;
        record[0x2B] = arg10;
        record[0x2C] = arg11;
        record[0x29] = arg8;
        record[0x2D] = arg12;
        record[0x2E] = arg13;
        record[0x2F] = arg14;
        record[0x30] = arg15;
        record[0x31] = arg16;
        record[0x32] = arg17;
        record[0x33] = arg18;
        record[0x34] = arg19;
        record[0x35] = arg20;
        record[0x36] = arg21;
        record[0x37] = arg22;
        record[0x38] = arg23;
        record[0x39] = arg24;
        record[0x3A] = arg25;
        *(u16 *)(record + 0x20) = arg31;
        record[0x3C] = arg31;
        record[0x3B] = arg26;
        record[0x3D] = arg32;
        record[0x3E] = arg33;
        record[0x3F] = arg34;
        record[0x40] = arg35;
        *(s16 *)(record + 0x1C) = arg36;
        *(u16 *)(record + 0x1E) = arg37;
        *(u16 *)(record + 0x22) = arg38;
        record[0x42] = 0;
        record[0x41] = arg39;
        record[0x43] = arg40;
        if (arg44 != 0 && arg41 >= 4) {
            arg41 = 3;
        }
        record[0x44] = arg41;
        record[0x45] = arg42;
        record[0x46] = arg43;
        record[0x47] = arg45;
        record[0x48] = arg46;
    }
}

s32 func_1516DB90() {
    return 0;
}

/* Split packed signed coordinates; forward arg1/arg4 as words and two low bytes. */
void func_1516E778(u32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4) {
    func_1516D99C(
        (s16)(arg0 >> 16), (s16)(arg0 & 0xFFFF), 0, (u8)arg2, 0, 0, 0, 0,
        0, 0, 0, 0, 4, 0, 0, 0,
        0xFF, 0xFF, 0xFF, 0, 8, 8, 1, 0,
        0, 0, 0, 0x155, 0x155, 0x155, 0x155, arg1,
        0x1E, 0, 0xFF, 0x28, 0x168, 0x18, 0x21, 4,
        0, 1, 0, 0, 0, 0, 0, (u8)arg3, arg4);
}

/* Fade intensity, grow both extents and interpolate the selected RGB ramp.
 * Five guards retain the start register; two preserve the unreachable return. */
s32 func_1516E8CC(u8 *record) {
    u8 *color = record;
    s32 value = record[0x1F];
    s32 phase;
    u8 *time = record;
    s32 start;
    f32 weight;
    f32 complement;

    if (record[0x24] != 0) {
        if (value != 0xFF) {
            value = (s32)((u32)value + ((u32)D_800BE9E4 << 5));
            if (value >= 0x100) {
                value = 0xFF;
            }
            record[0x1F] = value;
        }
    } else if (value != 0) {
        value = (s32)((u32)value - ((u32)D_800BE9E4 << 4));
        if (value < 0) {
            value = 0;
        }
        record[0x1F] = value;
    }
    if (record[0x24] == 0 && value == 0) {
        return 1;
    }
    value = *(s16 *)(record + 0x14);
    value = (s32)((u32)value + (u32)D_800BE9E4 * 10);
    *(s16 *)(record + 0x16) = value;
    *(s16 *)(record + 0x14) = value;
    phase = record[0x24];
    if (record[0x24] == 0) {
        phase += record[0x1F] >> 5;
    } else {
        phase += 8;
    }
    start = time[0x26];
    value = start;
    if (start < start + 8) {
        time = D_800A6E00 + start;
        do {
            if (phase >= *time) {
                weight = (f32)(phase - *time) / (f32)(time[-1] - *time);
                complement = 1.0f - weight;
                color = D_800A6E0C + value * 3;
                record[0x1C] = (u32)((f32)(u32)color[0] * complement + (f32)(u32)color[-3] * weight);
                record[0x1D] = (u32)((f32)(u32)color[1] * complement + (f32)(u32)color[-2] * weight);
                record[0x1E] = (u32)((f32)(u32)color[2] * complement + (f32)(u32)color[-1] * weight);
                break;
            }
            value++;
            time++;
        } while (value < color[0x26] + 8);
    }
    return 0;
}

/* Fade intensity and scale both extents; report completion.
 * Three relocation-aware guards retain the retail operand-load schedule. */
s32 func_1516ECAC(u8 *record) {
    s32 value = record[0x1F];
    s32 scale;
    s32 base;

    if (record[0x24] != 0) {
        if (value != 0xFF) {
            value = (s32)((u32)value + ((u32)D_800BE9E4 << 7));
            if (value >= 0x100) {
                value = 0xFF;
            }
            record[0x1F] = value;
        }
    } else if (value != 0) {
        value = (s32)((u32)value - (u32)D_800BE9E4 * record[0x26]);
        if (value < 0) {
            value = 0;
        }
        record[0x1F] = value;
    }
    if (record[0x24] == 0 && value == 0) {
        return 1;
    }
    base = record[0x2D] | (record[0x2C] << 8);
    scale = (s32)((u32)base * (u32)value);
    scale >>= 7;
    *(s16 *)(record + 0x16) = scale;
    *(s16 *)(record + 0x14) = scale;
    return 0;
}

/* Create the type-0x3A actor preset; preserve word arguments and the low flag byte. */
void func_1516ED68(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    u8 type = D_800CC2D4[(u32)arg0 * 0x32C];

    if (type == 0x3A) {
        func_1516D99C(
            5, 0, 0, 4, 0, 0xFF, 0xFF, 0xFF,
            0, 0, 0, 0, 2, 0, 0, 0,
            0, 0, 0, 8, 0, 0, 0, 0,
            0, 0, 0, 0x124, 0x124, 0, 0, arg1,
            0, 0, arg0, 0xC, 0, 0, 0x81, 2,
            0, 1, 0, 0, 0, 5, 0, (u8)arg2, arg3);
    }
}

/* Consume a qualifying slot counter before creating its effect preset.
 * Expected-word guards preserve retail index reuse and temporary allocation. */
void func_1516EED4(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    if (arg0 < 4 && (s32)(&D_800DD2A0)[arg0] >= arg1) {
        (&D_800DD2A0)[arg0] = 0;
        func_1516D99C(
            0, 0, 0, 4, 0, 0xFF, 0xFF, 0xFF,
            0, 0, 0, 0, 2, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0x200, 0x200, 0, 0, 0x1E,
            0, 0, arg0, 0x14, 0, 0, 0x81, 8,
            0, 1, 0, 0, 0, 0xC, 0, (u8)arg2, arg3);
    }
}

/* Snapshot the preset tables, fade a full word, then update motion and size.
 * Live tail operands retain the frame; guards normalize temporary scheduling. */
s32 func_1516F024(u8 *record) {
    s32 step;
    s32 coefficient;
    s32 value;
    s32 extent;
    s32 index;
    ByteTable11_19A8B0 scales = D_8008CBC4;
    ByteTable11_19A8B0 growth = D_8008CBD0;
    ByteTable11_19A8B0 limits = D_8008CBDC;
    ByteTable11_19A8B0 fades = D_8008CBE8;
    s32 limit;

    index = record[0x2C];
    value = record[0x1F];

    if (record[0x24] != 0) {
        limit = limits.values[index];
        if (value != limit) {
            value = (s32)((u32)value + ((u32)D_800BE9E4 << 4));
            if (value > limit) {
                value = limit;
            }
            record[0x1F] = value;
        }
    } else if (value != 0) {
        value = (s32)((u32)value - (u32)D_800BE9E4 * fades.values[index]);
        if (value < 0) {
            value = 0;
        }
        record[0x1F] = value;
    }
    if (record[0x24] == 0 && value == 0) {
        return 1;
    }
    func_1516F864(record);
    step = D_800BE9E4;
    coefficient = growth.values[index];
    extent = (s32)((u32)*(s16 *)(record + 0x14) + (u32)step * coefficient);
    *(s16 *)(record + 0x16) = extent;
    *(s16 *)(record + 0x14) = extent;
    if (index == 3) {
        *(s16 *)(record + 0x18) = 0x64;
    }
    func_1516F94C(record, scales.values[index]);
    return 0;
}

/* Preset 0x2D: forward arg0/arg1/arg3 as words; only arg2 narrows. */
void func_1516F1C0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    func_1516D99C(
        2, 0, 0, 0x2D, 0, 0xFF, 0xFF, 0xFF,
        0, 0, 0, 0, 2, 0, 0, 0,
        0, 0, 0, 1, 0, 0, 0, 0,
        0, 0, 0, 0x50, 0x50, 0, 0, arg1,
        0xA, 0xA, arg0, 0x3C, 0, 0, 0x81, 4,
        0, 1, 0, 0, 0, 4, 2, (u8) arg2, arg3);
}

/* Preset 0x2B twice: snapshot the first input byte; retain word forwards.
 * Indexed reads preserve the live fifth input and saved snapshot home. */
void func_1516F2F8(s32 arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    s32 firstType;

    firstType = (u8)arg0;
    func_1516D99C(
        3, 0, 0, 0x2B, 0, 0xFF, 0xFF, 0xFF,
        0, 0, 0, 0, 2, 0, 0, 0,
        0, 0, 0, 2, 0, 0, 0, 0,
        0, 0, 0, 0x50, 0x50, 0, 0, arg1,
        4, 4, firstType, 0x10, 0, 0, 0x81, 4,
        0, 1, 0, 0, 0, 1, 0, (u8)arg4, arg5);
    func_1516D99C(
        3, 0, 0, 0x2B, 0, 0xFF, 0xFF, 0xFF,
        0, 0, 0, 0, 2, 0, 0, 0,
        0, 0, 0, 3, 0, 0, 0, 0,
        0, 0, 0, 0x50, 0x50, 0, 0, 7,
        4, 4, (&firstType)[0], arg2, 0, 0, 0x81, 5,
        0, 1, 0, 0, 0, 1, arg3, (u8)(&arg4)[0], arg5);
}

s32 func_1000EBC4(struct00 *arg0, s32 arg1, s32 arg2, s32 arg3);
u16 func_1000FA64(u16 arg0, s16 arg1, s16 arg2, s16 arg3, s32 arg4,
                 u16 arg5, s16 arg6, s32 arg7, void *arg8,
                 s32 arg9, s32 argA, s32 argB);

/* Submit two preset-13 records, then event 7 with the live full-word context.
 * Slots 12..14 are unused, but retain the caller's arg15/arg16 positions.
 * Repeated narrowed expressions preserve IDO's shared values and spill homes. */
void func_1516F548(s32 arg0, s32 arg1, s32 arg2, s32 arg3,
                   s32 arg4, s32 arg5, s32 arg6, s32 arg7,
                   s32 arg8, s32 arg9, s32 arg10, s32 arg11,
                   s32 arg12, s32 arg13, s32 arg14, s32 arg15, s32 arg16) {
    func_1516D99C(
        (s16)arg0, (s16)arg1, (s16)arg2, 13, 0, 0x67, 0x17, 13,
        0, 0, 0x12, 0, 2, (u8)arg4, 0, (u8)arg6,
        0, 0, 0, arg10, 0, 0, 0, 0, 0, 0, 0,
        (s16)((s32)((u32)arg7 << 12) / 4096),
        (s16)((s32)((u32)arg7 << 12) / 4096),
        (s16)((s32)((u32)arg8 << 12) / 4096),
        (s16)((s32)((u32)arg8 << 12) / 4096),
        (u16)arg3, (u8)arg9, 20, 255, 16, (s16)arg5,
        200, 1, 0, 0, 1, 0, 0, 0, 0, 0, (u8)arg15, arg16);
    func_1516D99C(
        (s16)arg0, (s16)arg1, (s16)arg2, 13, 0, 0x67, 0x17, 13,
        0, 0, 0x12, 0, 2, (u8)arg4, 0, (u8)arg6,
        0, 0, 0, arg11, 0, 0, 0, 0, 0, 0, 0,
        (s16)((s32)((u32)arg7 << 12) / 4096),
        (s16)((s32)((u32)arg7 << 12) / 4096),
        (s16)((s32)((u32)arg8 << 12) / 4096),
        (s16)((s32)((u32)arg8 << 12) / 4096),
        (u16)arg3, (u8)arg9, 20, 255, 16, (s16)arg5,
        200, 1, 6, 0, 1, 0, 0, 0, 0, 0, (u8)(&arg15)[0], arg16);
    func_1000FA64(7, (s16)arg0, (s16)arg1, (s16)arg2,
                 0x36B0, 1000, 100, (s32)func_1000EBC4, (void *)arg3, 0, 0, 0);
}

// Matched with guarded packed fixed-point register allocation.
void func_1516F864(u8 *arg0) {
    s32 position;
    s32 velocity = *(s8 *) (arg0 + 0x26);

    velocity = (velocity << 8) + *(arg0 + 0x27);
    position = (*(s16 *) (arg0 + 0xE) << 8) + *(arg0 + 0x2A);
    position += velocity * D_800BE9E4;
    *(s16 *) (arg0 + 0xE) = position >> 8;
    *(arg0 + 0x2A) = position;

    velocity = *(s8 *) (arg0 + 0x28);
    velocity = (velocity << 8) + *(arg0 + 0x29);
    position = (*(s16 *) (arg0 + 0x12) << 8) + *(arg0 + 0x2B);
    position += velocity * D_800BE9E4;
    *(s16 *) (arg0 + 0x12) = position >> 8;
    *(arg0 + 0x2B) = position;
}

// Matched with guarded packed-byte temporary register normalization.
void func_1516F8EC(u8 *arg0, u32 arg1) {
    s32 val = *(s8 *) (arg0 + 0x26);

    val = (val << 8) + *(arg0 + 0x27);
    val = val * arg1;
    *(s8 *) (arg0 + 0x26) = (val >> 8) >> 8;
    *(arg0 + 0x27) = val >> 8;
}

// Matched with guarded packed-byte temporary register normalization.
void func_1516F91C(u8 *arg0, u32 arg1) {
    s32 val = *(s8 *) (arg0 + 0x28);

    val = (val << 8) + *(arg0 + 0x29);
    val = val * arg1;
    *(s8 *) (arg0 + 0x28) = (val >> 8) >> 8;
    *(arg0 + 0x29) = val >> 8;
}

void func_1516F94C(u8 *arg0, u32 arg1) {
    func_1516F8EC(arg0, arg1);
    func_1516F91C(arg0, arg1);
}

// Matched by preserving the scaled field's source-level lifetime.
void func_1516F984(u8 *arg0, u32 arg1) {
    s32 val;

    func_1516F94C(arg0, arg1);
    val = *(s16 *) (arg0 + 0x18);
    val = val * arg1;
    val = val >> 8;
    *(s16 *) (arg0 + 0x18) = val;
}

/* Keep the clamp value full-width; narrow only the stored record fields. */
s32 func_1516F9C4(u8 *record) {
    s32 extent;
    s32 value = record[0x1F];

    if (record[0x24] != 0) {
        if (value != 255) {
            value = (s32)((u32)value + ((u32)D_800BE9E4 << 4));
            if (value >= 256) {
                value = 255;
            }
            record[0x1F] = value;
        }
    } else {
        if (value != 0) {
            value = (s32)((u32)value - ((u32)D_800BE9E4 << 3));
            if (value < 0) {
                value = 0;
            }
            record[0x1F] = value;
        }
        extent = (s32)((u32)value << 9) >> 8;
        *(s16 *)(record + 0x16) = extent;
        *(s16 *)(record + 0x14) = extent;
    }
    if (record[0x24] == 0 && value == 0) {
        return 1;
    }
    func_1516F864(record);
    func_1516F984(record, 0xF0);
    return 0;
}

s32 func_1516FA88() {
    return 0;
}

s32 func_1516FBCC() {
    return 0;
}

s32 func_1516FD50() {
    return 0;
}

s32 func_1516FE1C() {
    return 0;
}

s32 func_15170034() {
    return 0;
}

s32 func_151700D8() {
    return 0;
}

s32 func_15170500() {
    return 0;
}

s32 func_151707E0() {
    return 0;
}

s32 func_151709B4() {
    return 0;
}
