#include <ultra64.h>
extern u8 *D_800D23C0;
extern u32 D_80087380;
extern s16 D_80087290;
extern u8 *D_800D2350;
extern u8 *D_8008FDD4;
extern s8 D_8008FD90;
extern u8 *D_800872A0;
extern s8 D_8008FD8C;
extern f32 D_8009DA5C;
extern u8 D_8008729C;
extern f32 D_8009D9CC;
extern s32 D_800D2354;
f32 func_15086D94(f32, f32, f32, f32, f32);

/* Non-matching placeholders for the text-only asm slice asm/B3020.s. */

extern s32 D_800D23B0;
extern u8 D_800CC40F[];
extern s16 D_80087294;
extern f32 D_800D2360[];
extern u8 D_800D237C[];
extern u8 D_800CC2D0[];
extern s32 D_800D2394;
extern s8 D_800D2398;
extern s8 D_800D2399;
void *func_1502B5C8(s32 *size, u32 depth, ...);
s32 func_1509BFB0();
s32 func_15085BE8();
s32 func_150888A8(u8 excludedId, u8 recordIndex, s8 alternate);

s32 func_15085B70(s32 arg0) {
    s16 *temp_v0 = (s16 *) func_1502B5C8(0, 2, 0x19, arg0);

    if (temp_v0 == 0) {
        D_80087290 = 0;
        D_80087294 = 0;
        D_800D2350 = 0;
    } else {
        D_80087290 = temp_v0[0];
        D_80087294 = temp_v0[1];
        D_800D2350 = (u8 *) temp_v0 + 4;
    }
    return func_15085BE8();
}

s32 func_15085BE8() {
    return 0;
}

s32 func_15085DA8(f32 arg0) {
    s32 i = 0;

    if (D_800D2360[0] <= arg0) {
        do {
            i++;
        } while (D_800D2360[i] <= arg0);
    }
    return D_800D237C[i];
}

s32 func_15085DF8(f32 x, f32 y, f32 z, s8 mode, s8 band) {
    s32 i;
    s32 best;
    s32 check;
    f32 dx;
    f32 dy;
    f32 dz;
    f32 distance;
    f32 minimum;

    check = 0;
    minimum = D_8009D9CC;
    if (mode == 0) {
        check = 1;
    }
    if (D_8008729C != 0xFF) {
        dx = (f32)*(s16 *)((D_800D2350 + D_8008729C * 16) + 0) - x;
        dy = (f32)*(s16 *)((D_800D2350 + D_8008729C * 16) + 2) - y;
        dz = (f32)*(s16 *)((D_800D2350 + D_8008729C * 16) + 4) - z;
        if (!check || (check && func_15086D94(x, y, z, dx, dz) < 0.0f)) {
            minimum = dx * dx + dy * dy + dz * dz + 10.0f;
        }
        D_8008729C = 0xFF;
    }
    best = 0xFF;
    for (i = 0; i < D_80087290; i++) {
        if ((D_800D2350 + (i << 4))[6] == band || band == -1) {
            if ((D_800D2350 + (i << 4))[14] == mode || mode == -1) {
                dx = (f32)*(s16 *)((D_800D2350 + (i << 4)) + 0) - x;
                dy = (f32)*(s16 *)((D_800D2350 + (i << 4)) + 2) - y;
                dz = (f32)*(s16 *)((D_800D2350 + (i << 4)) + 4) - z;
                distance = dx * dx + dy * dy + dz * dz;
                if (distance < minimum &&
                    (!check || (check && func_15086D94(x, y, z, dx, dz) < 0.0f))) {
                    minimum = distance;
                    best = i;
                }
            }
        }
    }
    D_800D2354 = (s32)sqrtf(minimum);
    return best;
}

s32 func_15086098() {
    return 0;
}

s32 func_15086364() {
    return 0;
}

f32 func_15086BD0(s32 arg0, s32 arg1) {
    u8 *first;
    u8 *second;
    f32 x;
    f32 y;
    f32 z;

    if ((arg0 == 0xFF) || (arg1 == 0xFF)) {
        return 0.0f;
    }

    first = D_800D2350 + arg0 * 16;
    second = D_800D2350 + arg1 * 16;
    x = (f32)(*(s16 *)(first + 0) - *(s16 *)(second + 0));
    y = (f32)(*(s16 *)(first + 2) - *(s16 *)(second + 2));
    z = (f32)(*(s16 *)(first + 4) - *(s16 *)(second + 4));
    return sqrtf((x * x) + (y * y) + (z * z));
}

void func_15086C70(arg0)
s32 arg0;
{
    u8 *temp_v0 = (u8 *) ((s32) D_800D2350 + arg0 * 16);
    s32 temp_v1 = *(s16 *) (temp_v0 + 4);

    func_150A3194(3, 0xB, *(s16 *) temp_v0, *(s16 *) (temp_v0 + 2), temp_v1);
}

s32 func_15086CBC(s32 arg0, f32 *arg1, f32 *arg2, f32 *arg3) {
    s32 offset;

    if (arg0 < 0 || arg0 >= D_80087290) {
        return 0;
    }
    offset = arg0 * 16;
    *arg1 = (f32) *(s16 *) (D_800D2350 + offset);
    *arg2 = (f32) *(s16 *) (D_800D2350 + offset + 2);
    *arg3 = (f32) *(s16 *) (D_800D2350 + offset + 4);
    return 1;
}

s32 func_15086D48(s32 arg0) {
    s32 temp_v0 = *(s16 *) &D_80087290;
    s32 i = 0;

    if (temp_v0 > 0) {
        do {
            if (arg0 == D_800D2350[(i * 0x10) + 7]) {
                return i;
            }
            i += 1;
        } while (i < temp_v0);
    }
    return 0xFF;
}

f32 func_15086D94(f32 x, f32 y, f32 z, f32 dx, f32 dz) {
    s32 band;
    s32 count;
    s32 i;
    s32 j;
    s32 id;
    u8 *nodes;
    u8 *first;
    u8 *second;
    u8 *cursor;
    f32 minimum;
    f32 fraction;
    f32 ax;
    f32 az;
    f32 nx;
    f32 nz;
    f32 constant;
    f32 start;
    f32 end;
    f32 a;
    f32 b;
    f32 cross_x;
    f32 cross_z;
    f32 swap;

    band = func_15085DA8(y);
    count = D_80087290;
    minimum = 100.0f;
    i = 0;
    if (i < count) {
        nodes = D_800D2350;
        do {
            first = nodes + (i << 4);
            if (first[14] == 1 && first[6] == band) {
                for (j = 0, cursor = first; j < 5; j++, cursor++) {
                    id = cursor[9];
                    if (id != 255 && i < id) {
                        second = nodes + (id << 4);
                        if (second[14] == 1) {
                            nx = (f32)(*(s16 *)(second + 4) - *(s16 *)(first + 4));
                            nz = -(f32)(*(s16 *)(second + 0) - *(s16 *)(first + 0));
                            ax = (f32)*(s16 *)(first + 0);
                            az = (f32)*(s16 *)(first + 4);
                            constant = -(ax * nx + nz * az);
                            start = x * nx + z * nz + constant;
                            a = start;
                            end = (x + dx) * nx + (z + dz) * nz + constant;
                            b = end;
                            if ((end < 0.0f && 0.0f <= start) ||
                                (start < 0.0f && 0.0f <= end)) {
                                if (end < 0.0f) {
                                    b = -end;
                                }
                                if (start < 0.0f) {
                                    a = -start;
                                }
                                swap = nx;
                                nx = -nz;
                                nz = swap;
                                fraction = a / (a + b);
                                constant = -(ax * nx + swap * az);
                                cross_x = x + fraction * dx;
                                cross_z = z + fraction * dz;
                                a = cross_x * nx + cross_z * nz + constant;
                                b = (f32)*(s16 *)(second + 0) * nx +
                                      nz * (f32)*(s16 *)(second + 4) + constant;
                                if ((0.0f < b && 0.0f < a && a <= b) ||
                                    (b < 0.0f && a < 0.0f && b <= a)) {
                                    if (fraction < minimum) {
                                        minimum = fraction;
                                    }
                                }
                            }
                        }
                    }
                }
            }
            i++;
        } while (i < D_80087290);
    }
    if (minimum <= 1.0f) {
        /* Retail returns the last crossing fraction, even if that edge was rejected. */
        return sqrtf(dx * dx + dz * dz) * fraction;
    }
    return -1.0f;
}

/* Build a closed route and allocate its player/extra record table. */
void func_150870D0(s32 key, s32 playerCount, s32 extraCount) {
    extern s8 D_800D23A8;
    extern s8 D_800D239A;
    extern void *allocate_memory(u32, s32, s32, s32);
    extern void func_15088824(u8 *);
    /* Represent six observed byte homes within the recovered scratch workspace. */
    struct {
        u8 reserved0[4];
        u8 cursor[4];
        u8 seed[4];
        u8 reservedC[20];
    } scratch;
    s32 limit;
    s32 humanLimit;
    s32 i;
    u32 offset;
    u32 length;
    u8 selected;
    s32 candidate;
    s32 neighbor0;
    s32 neighbor1;
    u8 start;
    u8 *table;
    u8 *route;
    u8 *other;
    u8 *record;

    D_800872A0 = 0;
    start = func_15086D48(key);
    scratch.seed[3] = start;
    if (start != 0xFF) {
        selected = 0xFF;
        table = D_800D2350;
        limit = (D_800D23A8 * 0xFF) & 0xFF;
        route = table + start * 0x10;
        for (i = 0; i != 5; i++) {
            candidate = route[9];
            if (candidate != 0xFF) {
                other = table + candidate * 0x10;
                if (other[0xE] == 0 &&
                    ((D_800D23A8 == 0 && other[0xF] >= limit) ||
                     (D_800D23A8 != 0 && limit >= other[0xF]))) {
                    limit = other[0xF] & 0xFF;
                    selected = candidate;
                }
            }
            route++;
        }
        /* Reuse the call-result temporaries for the stored seed pair at the gate. */
        if (selected != 0xFF) {
            neighbor0 = (u8)func_150888A8(scratch.seed[3], selected, 0);
            neighbor1 = func_150888A8(selected, scratch.seed[3], 0);
            scratch.seed[1] = neighbor0;
            scratch.seed[0] = neighbor1;
        }
        if (selected != 0xFF &&
            (neighbor1 = scratch.seed[1], neighbor0 = scratch.seed[0], neighbor0 != 0xFF) &&
            (i = (u8)neighbor1, neighbor1 != 0xFF)) {
            length = 0;
            start = scratch.seed[3];
            scratch.cursor[1] = selected;
            do {
                scratch.cursor[0] = scratch.cursor[1];
                scratch.cursor[1] = i;
                scratch.cursor[2] = i;
                i = (u8)func_150888A8(scratch.cursor[0], scratch.cursor[1], 0);
                length++;
            } while (start != scratch.cursor[0]);
            scratch.cursor[2] = i;
            D_800D2399 = extraCount;
            D_800D2398 = playerCount;
            playerCount = (s32)((u32)playerCount + (u32)extraCount);
            D_800D2394 = 0;
            D_800872A0 = allocate_memory((u32)playerCount * 0x84u, 1, 0, 0);
            if (playerCount > 0) {
                offset = 0;
                i = 0;
                do {
                    record = D_800872A0 + offset;
                    func_15088824(record);
                    record[0x2B] = neighbor0;
                    start = scratch.seed[3];
                    record[0x2D] = selected;
                    record[0x2E] = neighbor1;
                    record[0x2C] = start;
                    if (i < D_800D2398) {
                        record[0x31] = i;
                    }
                    humanLimit = D_8008FD90;
                    record[0x26] = length;
                    offset += 0x84;
                    record[0x30] = i >= humanLimit;
                    i++;
                } while (i != playerCount);
            }
            D_800D239A = 1;
        }
    }
}

/* Project an actor onto its route, update look-ahead state, then rank players. */
void func_15087350(s32 recordIndex, s32 active, f32 lookAhead) {
    extern f32 D_8009D9E0, D_8009D9E4, D_8009D9E8;
    extern f64 D_8009D9F0;
    extern f32 D_8009D9F8, D_8009D9FC;
    extern s8 D_800D2390, D_800D23A9;
    extern s32 D_800BE9E4;
    extern u16 D_800D18A0;
    extern f32 D_800D239C, D_800D23A0, D_800D23A4, D_800CC310;
    extern u8 **D_800D2104;
    extern void func_15088F30(u8 *, f32 *, f32 *, f32 *);
    extern f32 func_150498A4(f32 *, s32, f32, f32 *);
    extern f32 func_150497E0(f32 *, s32, f32);
    extern s32 func_15088A08(u8 *, f32);
    extern void func_15042D78(s32);
    extern s32 func_1508802C(u8 *, u8 *, s32);
    f32 gain;
    f32 startZ;
    f32 positionX;
    f32 positionZ;
    f32 slopeX;
    f32 slopeZ;
    f32 intercept;
    f32 error;
    f32 absoluteError;
    f32 previousError;
    f32 chordLength;
    f32 valueX;
    f32 inverse;
    f32 x[4];
    f32 y[4];
    f32 z[4];
    f32 pointZ;
    u8 *actor;
    s8 temporary;
    s8 refresh;
    s8 iterations;
    s8 again;
    u8 copy[0x84];
    s8 order[32];
    f32 scores[17];
    u32 recordOffset;
    s32 i;
    u8 *record;
    u8 *cursor;

    iterations = 0;
    if (D_800872A0 == 0) {
        return;
    }
    recordOffset = (u32)recordIndex * 0x84u;
    record = D_800872A0 + recordOffset;
    actor = D_800CC2D0 + (s8)record[0x31] * 0x32C;
    positionX = *(f32 *)(actor + 0x14);
    positionZ = *(f32 *)(actor + 0x1C);
    D_800D2390 = 0;
    if ((s8)record[0x30] == 0) {
        *(f32 *)record = 0.5f;
    } else {
        valueX = (*(f32 *)(record + 4) - *(f32 *)record) * 0.125f;
        if (D_8009D9E0 < valueX) {
            valueX = D_8009D9E0;
        }
        if (valueX < D_8009D9E4) {
            valueX = D_8009D9E4;
        }
        *(f32 *)record += valueX;
    }
    previousError = D_8009D9E8;
    gain = 0.75f;
    refresh = 1;
    do {
        again = 0;
        if (refresh != 0) {
            func_15088F30(record, x, y, z);
            slopeX = x[2] - x[1];
            slopeZ = z[2] - z[1];
            chordLength = sqrtf(slopeX * slopeX + slopeZ * slopeZ);
        }
        valueX = func_150498A4(x, 0, *(f32 *)(record + 8), &slopeX);
        pointZ = func_150498A4(z, 0, *(f32 *)(record + 8), &slopeZ);
        inverse = -1.0f / sqrtf(slopeX * slopeX + slopeZ * slopeZ);
        slopeX *= inverse;
        slopeZ *= inverse;
        *(f32 *)(record + 0xC) = slopeX;
        *(f32 *)(record + 0x10) = slopeZ;
        intercept = -(valueX * slopeX + pointZ * slopeZ);
        /* Reuse the sampled-Z carrier for the signed plane error. */
        pointZ = (slopeX * positionX + slopeZ * positionZ) + intercept;
        if (pointZ < -50.0f || 50.0f < pointZ) {
            absoluteError = pointZ;
            if (pointZ < 0.0f) {
                absoluteError = -pointZ;
            }
            if (previousError < absoluteError) {
                gain *= 0.5f;
            }
            previousError = absoluteError;
            again = 1;
            inverse = (pointZ * gain) / chordLength;
            if (inverse < -0.5f) {
                inverse = -0.5f;
            }
            if (0.5f < inverse) {
                inverse = 0.5f;
            }
            error = pointZ;
            refresh = func_15088A08(record, -inverse);
            pointZ = error;
        }
        iterations++;
        if (iterations >= 11) {
            again = 0;
        }
    } while (again != 0);
    error = pointZ;
    func_15042D78(0x80);
    *(s8 *)(record + 0x32) = *(s8 *)(record + 0x33);
    *(s8 *)(record + 0x33) = D_800BE9E4;
    *(f32 *)(record + 0x14) = (((*(f32 *)(actor + 0x2C) * slopeX +
        *(f32 *)(actor + 0x34) * slopeZ) + intercept) - error) * 4.0f / (f32)(s8)record[0x32];
    if ((s8)record[0x30] != 0) {
        bcopy(record, copy, 0x84);
        func_15088A08(copy, lookAhead + lookAhead);
        func_15088F30(copy, x, y, z);
        D_800D239C = func_150497E0(x, 0, *(f32 *)(copy + 8));
        D_800D23A0 = func_150497E0(y, 0, *(f32 *)(copy + 8));
        D_800D23A4 = func_150497E0(z, 0, *(f32 *)(copy + 8));
        if (recordIndex < D_800D2398) {
            if (active == 0) {
                valueX = (f32)((f64)D_800CC310 * D_8009D9F0);
                D_800D239C = sinf(valueX) * 300.0f + *(f32 *)(actor + 0x14);
                D_800D23A0 = *(f32 *)(actor + 0x18);
                D_800D23A4 = cosf(valueX) * 300.0f + *(f32 *)(actor + 0x1C);
            }
            *(s16 *)(D_800D2104[actor[0x13F]] + 8) = (s32)D_800D239C;
            *(s16 *)(D_800D2104[actor[0x13F]] + 10) = (s32)D_800D23A0;
            *(s16 *)(D_800D2104[actor[0x13F]] + 12) = (s32)D_800D23A4;
            *(f32 *)(actor + 0x44) = (f32)active;
            if (D_800D2390 == 1) {
                *(f32 *)(actor + 0x20) = 75.0f;
            } else if (D_800D2390 == 2) {
                *(f32 *)(actor + 0x20) = 55.0f;
            } else if (D_800D2390 == 3) {
                *(f32 *)(actor + 0x20) = 65.0f;
            }
            actor[0x21E] = 0;
        }
    } else {
        *(f32 *)record = 0.0f;
        func_15088F30(record, x, y, z);
        valueX = func_150497E0(x, 0, *(f32 *)(record + 8));
        startZ = func_150497E0(z, 0, *(f32 *)(record + 8));
        *(f32 *)record = 1.0f;
        func_15088F30(record, x, y, z);
        slopeX = func_150497E0(x, 0, *(f32 *)(record + 8)) - valueX;
        error = func_150497E0(z, 0, *(f32 *)(record + 8));
        slopeZ = error - startZ;
        chordLength = sqrtf(slopeX * slopeX + slopeZ * slopeZ);
        if (1.0f < chordLength) {
            absoluteError = 1.0f / chordLength;
            slopeX *= absoluteError;
            slopeZ *= absoluteError;
            *(f32 *)record = ((slopeX * positionX + slopeZ * positionZ) -
                (slopeX * valueX + slopeZ * startZ)) * absoluteError;
        } else {
            *(f32 *)record = 0.0f;
        }
    }
    record[0x48] = active;
    D_800D23A9 = 1;
    if ((s8)record[0x30] == 0 && record[0x48] > 0 &&
        !(D_800D18A0 & (1u << ((u32)(s8)record[0x31] & 31)))) {
        *(u32 *)(record + 0x1C) += (u32)D_800BE9E4;
    }
    if ((s8)record[0x30] >= 2 && (*(u8 **)(actor + 0x31C))[0x84] == 0) {
        func_1508802C(record, actor, 0xD);
    }
    if (recordOffset == 0) {
        recordOffset = (u32)(D_800D2398 - 1);
        cursor = D_800872A0;
        for (i = 0; i < D_800D2398; i++) {
            order[i] = i;
            scores[i] = *(f32 *)(cursor + 8) + (f32)*(s16 *)(cursor + 0x24);
            if ((s8)cursor[0x2A] != 0x7F) {
                scores[i] += D_8009D9F8 - (f32)(s8)cursor[0x2A] * 1000.0f;
            }
            if (D_800D18A0 & (1u << ((u32)(s8)cursor[0x31] & 31))) {
                scores[i] -= D_8009D9FC;
            }
            cursor += 0x84;
        }
        do {
            again = 1;
            cursor = (u8 *)scores;
            for (i = 0; i < (s32)recordOffset; i++, cursor += 4) {
                inverse = *(f32 *)cursor;
                if (inverse < *(f32 *)(cursor + 4)) {
                    temporary = order[i + 1];
                    order[i + 1] = order[i];
                    order[i] = temporary;
                    *(f32 *)cursor = scores[i + 1];
                    scores[i + 1] = inverse;
                    again = 0;
                }
            }
        } while (!again);
        for (i = 0; i < D_800D2398; i++) {
            D_800872A0[order[i] * 0x84 + 0x29] = i + 1;
        }
    }
}

/* Dispatch route records using their live actor slot and movement state. */
void func_15087CC0(void) {
    extern s8 D_800D23A9;
    extern void func_150891E8(u8 *, u8 *);
    extern void func_150896EC(u8 *, u8 *, s32);
    s32 i;
    u8 *record;
    u8 *actor;

    D_800D23A9 = 0;
    if (D_800872A0 != 0) {
        for (i = 0; i < D_800D2398; i++) {
            record = D_800872A0 + i * 0x84;
            actor = &D_800CC2D0[*(s8 *)(record + 0x31) * 0x32C];
            if (*(s32 *)(actor + 0x318) != 0) {
                if (*(s8 *)(record + 0x30) >= 2) {
                    func_150891E8(record, actor);
                } else if (record[0x48] == 0) {
                    func_150896EC(record, actor, 0);
                } else if (*(s8 *)(record + 0x49) != 0) {
                    func_150896EC(record, actor, 1);
                }
            }
        }
    }
}

void func_15087DCC(s32 arg0, s32 arg1) {
    u8 *rec;
    s32 value;

    if (D_800872A0 == 0) {
        return;
    }
    rec = (u8 *) (arg0 * 0x84 + (s32) D_800872A0);
    if (*(s8 *) (rec + 0x2F) == arg1) {
        return;
    }
    if (arg1 != 0) {
        value = func_150888A8(rec[0x2B], rec[0x2C], 1);
        rec[0x2D] = value;
        value = func_150888A8(rec[0x2C], value, 1);
        rec[0x2E] = value;
    }
    rec[0x2F] = arg1;
}

/* Keep the actor heading within the record's asymmetric wrapped-angle limits. */
void func_15087E54(s32 recordIndex, u8 *actor) {
    extern u16 func_1505A630(f32, f32, s32);
    u8 *table = D_800872A0;
    u8 *record;
    u16 target;
    u16 delta;

    if (table != 0) {
        record = table + recordIndex * 0x84;
        target = (func_1505A630(*(f32 *)(record + 0x10),
                              *(f32 *)(record + 0x0C), 0) + 0x4000);
        delta = target - *(u16 *)(actor + 0x76);
        if (delta & 0x8000) {
            if (delta < 0xDBFF) {
                *(u16 *)(actor + 0x76) = target + 0x2400;
            }
        } else {
            if (delta >= 0x2401) {
                *(u16 *)(actor + 0x76) = target - 0x2400;
            }
        }
    }
}

/* Select a wrapped heading offset from the live mode and record speed. */
void func_15087EF0(s32 recordIndex, u8 *actor) {
    extern u16 func_1505A630(f32, f32, s32);
    extern s8 D_800D23A8;
    u8 *record;
    u16 angle;
    u16 heading;

    if (D_800872A0 != 0) {
        record = D_800872A0 + recordIndex * 0x84;
        angle = func_1505A630(*(f32 *)(record + 0x10), *(f32 *)(record + 0x0C), 0);
        if (D_800D23A8 == 0) {
            if (*(f32 *)record < 0.5f) {
                heading = angle + 0x4A00;
            } else {
                heading = angle + 0x3600;
            }
        } else {
            if (*(f32 *)record >= 0.5f) {
                heading = angle + 0x4A00;
            } else {
                heading = angle + 0x3600;
            }
        }
        *(u16 *)(actor + 0x76) = heading;
    }
}

// Matched with guarded final-pointer register normalization.
void func_15087FC4(s32 arg0, s32 arg1) {
    u8 *temp_v0 = D_800872A0;

    if (temp_v0 != 0) {
        *(u8 *) (arg0 * 0x84 + (s32) temp_v0 + 0x31) = arg1;
    }
}

// Matched with guarded final-pointer register normalization.
void func_15087FEC(s32 arg0, s32 arg1) {
    u8 *temp_v0 = D_800872A0;

    if (temp_v0 != 0) {
        *(f32 *) (arg0 * 0x84 + (s32) temp_v0 + 4) = arg1 * 0.00390625f;
    }
}

extern u8 D_800CC2D0[];
extern u16 D_800D18A0;
extern u8 *D_800D154C;
extern s8 D_800C3E78;
extern s32 func_1507BB28(s32, s32);

/* Start an unblocked actor event and mark its route record active. */
s32 func_1508802C(u8 *record, u8 *actor, s32 reason) {
    u8 *state;
    s32 slot;

    state = *(u8 **)(actor + 0x31C);
    if (state[0x120] != 0) {
        return 1;
    }
    slot = (s32)((u32)actor - (u32)D_800CC2D0) / 0x32C;
    if (D_800D18A0 & (1U << slot)) {
        return 1;
    }
    state[0x84] = 1;
    *(s32 *)actor = 0xC;
    actor[0x232] = reason;
    D_800D154C = actor;
    D_800C3E78 = *(s8 *)(record + 0x31);
    *(s32 *)(actor + 0x218) = func_1507BB28(0, reason);
    *(u16 *)(actor + 0x21C) = 0;
    actor[0x125] = 0xFF;
    record[0x30] = 2;
    return 0;
}

extern u8 *D_800872A0;
extern u8 D_800CC2D0[];
extern s8 D_800D239A;
s32 func_1508802C(u8 *, u8 *, s32);

/* Dispatch a route actor's event state and stamp its sequence counter. */
s32 func_150880F8(s32 recordIndex, s32 reason) {
    u8 *record;
    u8 *actor;
    s32 result;

    result = 0;
    if (D_800872A0 == 0) {
        return 0;
    }
    record = (u8 *)((u32)recordIndex * 0x84 + (u32)D_800872A0);
    actor = (u8 *)((u32)D_800CC2D0 + (s32)*(s8 *)(record + 0x31) * 0x32C);
    if (*(s8 *)(record + 0x30) == 0) {
        result = func_1508802C(record, actor, reason);
    } else if (*(s8 *)(record + 0x30) == 1) {
        record[0x30] = 2;
        actor[0x125] = 0xFF;
    }
    record[0x2A] = D_800D239A;
    D_800D239A++;
    return result;
}

s32 func_150881CC(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    u8 *ptr;

    if (temp_v1 == 0) {
        return 0;
    }
    ptr = (u8 *) (arg0 * 0x84 + (s32) temp_v1);
    return (s32) (*(f32 *) ptr * 256.0f);
}

s32 func_15088218(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    s32 idx = arg0;
    s16 temp_a2;

    if (temp_v1 == 0) {
        return 0;
    }
    arg0 = idx * 0x84 + (s32) temp_v1;
    temp_a2 = *(s16 *) (arg0 + 0x24);
    return (s32) (*(f32 *) (arg0 + 8) * 16.0f) + (temp_a2 << 4);
}

s32 func_15088270(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    s32 idx = arg0;

    if (temp_v1 == 0) {
        return 0;
    }
    arg0 = idx * 0x84 + (s32) temp_v1;
    return (s32) *(f32 *) (arg0 + 0x14);
}

s32 func_150882B0(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    s32 idx = arg0;

    if (temp_v1 == 0) {
        return 0;
    }
    arg0 = idx * 0x84 + (s32) temp_v1;
    return *(s8 *) (arg0 + 0x27);
}

/* Pack the first matching non-self slot with its quantized separation. */
u32 func_150882E4(u32 recordIndex, u32 idOffset) {
    u8 *table = D_800872A0;
    u8 *candidate;
    u8 *record;
    s32 i;

    if (table == 0) {
        return 0x10;
    }
    record = table + recordIndex * 0x84;
    idOffset = (s32)*(s8 *)(record + 0x29) + idOffset;
    for (i = 0; i < D_800D2398; i++) {
        candidate = table + i * 0x84;
        if ((u32)(s32)*(s8 *)(candidate + 0x29) == idOffset && (u32)i != recordIndex) {
            recordIndex = (u32)(s32)*(s16 *)(record + 0x24) * 16u +
                          (u32)(s32)(*(f32 *)(record + 8) * 16.0f) -
                          (u32)(s32)*(s16 *)(candidate + 0x24) * 16u -
                          (u32)(s32)(*(f32 *)(candidate + 8) * 16.0f);
            if ((s32)recordIndex < 0) {
                recordIndex = 0u - recordIndex;
            }
            return (recordIndex << 8) | (u32)i;
        }
    }
    return 0x10;
}

/* Select the nearest strictly forward actor, optionally restricted by record tag. */
u8 *func_150883B0(s32 recordIndex, s32 direction, f32 *outValue, s32 *outTag) {
    extern f32 D_8009DA00;
    u8 *table = D_800872A0;
    u8 *record;
    u8 *actor;
    u8 *selected;
    s32 i;
    s8 excluded;
    f32 sign;
    f32 actorX;
    f32 actorZ;
    f32 x;
    f32 z;
    f32 bias;
    f32 minimum;
    f32 distance;

    if (table == 0) {
        return 0;
    }
    record = table + recordIndex * 0x84;
    if (direction >= 0) {
        sign = -1.0f;
    } else {
        sign = 1.0f;
    }
    actor = D_800CC2D0 + *(s8 *)(record + 0x31) * 0x32C;
    direction = *(s8 *)(record + 0x2F);
    actorX = *(f32 *)(actor + 0x14);
    actorZ = *(f32 *)(actor + 0x1C);
    x = *(f32 *)(record + 0x0C) * sign;
    z = *(f32 *)(record + 0x10) * sign;
    selected = 0;
    excluded = *(u8 *)(actor + 0x124) - 1;
    bias = -(x * actorX + z * actorZ);
    minimum = D_8009DA00;
    for (i = 0; i < D_800D2398; i++) {
        record = D_800872A0 + i * 0x84;
        if (*(s8 *)(record + 0x31) != excluded &&
            (direction == 0 || *(s8 *)(record + 0x2F) == direction)) {
            actor = D_800CC2D0 + *(s8 *)(record + 0x31) * 0x32C;
            actorX = *(f32 *)(actor + 0x14);
            actorZ = *(f32 *)(actor + 0x1C);
            distance = x * actorX + z * actorZ + bias;
            if (0.0f < distance && distance < minimum) {
                minimum = distance;
                *outValue = *(f32 *)record;
                *outTag = *(s8 *)(record + 0x2F);
                selected = D_800CC2D0 + *(s8 *)(record + 0x31) * 0x32C;
            }
        }
    }
    return selected;
}

s32 func_1508855C(s32 arg0) {
    u8 *temp_v1 = D_800872A0;
    s32 idx;
    s32 count;
    u8 *rec;
    s32 i;

    if (temp_v1 == 0) {
        return -1;
    }
    idx = (arg0 - (s32) D_800CC2D0) / 0x32C;
    if (idx == 0) {
        return 0;
    }
    count = D_800D2398 + D_800D2399;
    if (count < 2) {
        return -1;
    }
    rec = temp_v1 + 0x84;
    i = 1;
    do {
        if (*(s8 *) (rec + 0x31) == idx) {
            return i;
        }
        i += 1;
        rec += 0x84;
    } while (i < count);
    return -1;
}

extern u8 *D_800872A0;

/* Copy a route record while keeping the destination's identity and state. */
void func_150885EC(s32 sourceIndex, s32 destinationIndex) {
    s32 savedId;
    s32 savedState;
    u8 *table;

    table = D_800872A0;
    if (table != 0) {
        savedId = *(s8 *)((u32)table + ((u32)destinationIndex * 0x84) + 0x31);
        savedState = *(s8 *)((u32)table + ((u32)destinationIndex * 0x84) + 0x30);
        bcopy((u8 *)((u32)sourceIndex * 0x84 + (u32)table),
              table + ((u32)destinationIndex * 0x84), 0x84);
        D_800872A0[((u32)destinationIndex * 0x84) + 0x31] = savedId;
        D_800872A0[((u32)destinationIndex * 0x84) + 0x30] = savedState;
    }
}

extern u8 *D_800872A0;
extern s8 D_800D2399;
extern s8 D_800D2398;
extern s32 D_800D2394;
extern u8 D_800CC2D0[];
void func_15088824(u8 *);

/* Reserve the first free route slot and associate it with the actor. */
s32 func_1508868C(u8 *actor) {
    s32 recordIndex;
    u32 bit;
    u8 *table;

    table = D_800872A0;
    if (table == 0) {
        return -1;
    }
    bit = 1;
    for (recordIndex = 0; recordIndex < D_800D2399; recordIndex++, bit <<= 1) {
        if (((u32)D_800D2394 & bit) == 0) {
            D_800D2394 |= bit;
            recordIndex += D_800D2398;
            func_15088824((u8 *)((u32)recordIndex * 0x84 + (u32)table));
            ((u8 *)((u32)D_800872A0 + (u32)recordIndex * 0x84))[0x30] = 1;
            ((u8 *)((u32)D_800872A0 + (u32)recordIndex * 0x84))[0x31] =
                (s32)((u32)actor - (u32)D_800CC2D0) / 0x32C;
            return recordIndex;
        }
    }
    return -1;
}

void func_15088780(s32 arg0) {
    s32 idx;

    if (D_800872A0 == 0) {
        return;
    }
    idx = func_1508855C(arg0);
    ((u8 *) ((s32) D_800872A0 + idx * 0x84))[0x31] = 0;
    D_800D2394 &= ~(1 << (idx - D_800D2398));
}

s32 func_150887F8(void) {
    u8 *temp_v1 = D_800872A0;

    if (temp_v1 == 0) {
        return 0;
    }
    return temp_v1[0x46] == 0xFF;
}

void func_15088824(u8 *arg0) {
    arg0[0x2B] = 0;
    arg0[0x2C] = 0;
    arg0[0x2D] = 0;
    arg0[0x2E] = 0;
    arg0[0x28] = 0;
    *(s32 *) (arg0 + 0x1C) = 0;
    *(s32 *) (arg0 + 0x18) = 0;
    *(s32 *) (arg0 + 0x20) = -1;
    arg0[0x2F] = 0;
    *(f32 *) (arg0 + 0x8) = 0.0f;
    *(f32 *) (arg0 + 0x0) = 0.5f;
    *(f32 *) (arg0 + 0x4) = 0.5f;
    *(s16 *) (arg0 + 0x24) = 0;
    arg0[0x26] = 0;
    arg0[0x27] = 0;
    arg0[0x31] = 0;
    *(f32 *) (arg0 + 0xC) = 0.0f;
    *(f32 *) (arg0 + 0x14) = 0.0f;
    arg0[0x33] = 2;
    arg0[0x30] = 0;
    arg0[0x2A] = 0x7F;
    arg0[0x49] = 0;
    *(f32 *) (arg0 + 0x10) = 1.0f;
}

/* Prefer a non-requested neighbor class; retain the last requested-class fallback. */
s32 func_150888A8(u8 excludedId, u8 recordIndex, s8 alternate) {
    s32 excluded;
    s32 requested;
    s32 fallback;
    s32 i;
    s32 selected;
    s32 current;
    s32 candidate;
    s32 firstCandidate;
    s32 second;
    s32 kind;
    s32 secondKind;
    u8 *record;
    u8 *cursor;
    u8 *entry;
    u8 *firstEntry;
    u8 *secondEntry;

    excluded = excludedId;
    selected = 0xFF;
    fallback = 0xFF;
    if (alternate != 0) {
        requested = 1;
    } else {
        requested = 2;
    }
    record = D_800D2350 + recordIndex * 0x10;
    firstCandidate = record[9];
    if (firstCandidate != 0xFF && excluded != firstCandidate) {
        firstEntry = D_800D2350 + firstCandidate * 0x10;
        if (firstEntry[0xE] == 0) {
            if (requested != firstEntry[0xF]) {
                selected = firstCandidate & 0xFF;
            } else {
                fallback = firstCandidate & 0xFF;
            }
        }
    }
    i = 1;
    cursor = record + 1;
    current = selected;
    /* The retail loop handles the remaining four neighbors in pairs. */
    do {
        candidate = cursor[9];
        i += 2;
        if (candidate != 0xFF && excluded != candidate) {
            entry = D_800D2350 + candidate * 0x10;
            if (entry[0xE] == 0) {
                kind = entry[0xF];
                if (requested != kind) {
                    if (current == 0xFF || kind != 0) {
                        selected = candidate & 0xFF;
                        current = selected;
                    }
                } else {
                    fallback = candidate & 0xFF;
                }
            }
        }
        second = cursor[0xA];
        if (second != 0xFF && excluded != second) {
            secondEntry = D_800D2350 + second * 0x10;
            if (secondEntry[0xE] == 0) {
                secondKind = secondEntry[0xF];
                if (requested != secondKind) {
                    if (current == 0xFF || secondKind != 0) {
                        selected = second & 0xFF;
                        current = selected;
                    }
                } else {
                    fallback = second & 0xFF;
                }
            }
        }
        cursor += 2;
    } while (i != 5);
    if (current == 0xFF) {
        selected = fallback & 0xFF;
    }
    return selected;
}

/* Advance one neighbor boundary and update signed lap and bounded timer records. */
s32 func_15088A08(u8 *record, f32 delta) {
    extern s8 D_800D23A8;
    extern s8 D_800D2390;
    extern s8 D_800E0BE7;
    extern u8 D_800BE616;
    extern s16 D_800E0C10[];
    extern s32 D_800E0C18[];
    s32 step = 0;
    f32 fraction;
    s32 neighbor;
    s32 middle;
    s32 next;
    u8 *routes;
    s32 kind;
    s32 goal;
    s32 actorId;
    s32 time;
    s32 elapsed;
    s32 finish;
    s16 *best;
    s32 previousBest;

    *(f32 *)(record + 8) += delta;
    fraction = *(f32 *)(record + 8);
    if (fraction < 0.0f) {
        neighbor = record[0x2D];
        middle = record[0x2C];
        next = record[0x2B];
        record[0x2E] = neighbor;
        *(f32 *)(record + 8) = fraction + 1.0f;
        record[0x2D] = middle;
        record[0x2C] = next;
        record[0x2B] = func_150888A8(middle, next, *(s8 *)(record + 0x2F));
        step = -1;
    } else if (fraction >= 1.0f) {
        neighbor = record[0x2C];
        middle = record[0x2D];
        next = record[0x2E];
        *(f32 *)(record + 8) = fraction - 1.0f;
        record[0x2B] = neighbor;
        record[0x2C] = middle;
        record[0x2D] = next;
        record[0x2E] = func_150888A8(middle, next, *(s8 *)(record + 0x2F));
        step = 1;
        if (D_800D23A8 == 0) {
            routes = D_800D2350;
            kind = routes[record[0x2C] * 0x10 + 0xF];
            if (kind == 5) {
                D_800D2390 = 1;
                kind = routes[record[0x2C] * 0x10 + 0xF];
            }
            if (kind == 6) {
                D_800D2390 = 2;
            }
        } else {
            routes = D_800D2350;
            kind = routes[record[0x2C] * 0x10 + 0xF];
            if (kind == 7) {
                D_800D2390 = 1;
                kind = routes[record[0x2C] * 0x10 + 0xF];
            }
            if (kind == 8) {
                D_800D2390 = 2;
                kind = routes[record[0x2C] * 0x10 + 0xF];
            }
            if (kind == 9) {
                D_800D2390 = 3;
            }
        }
    }
    if (step != 0) {
        goal = D_800E0BE7;
        *(s16 *)(record + 0x24) = *(s16 *)(record + 0x24) + step;
        actorId = *(s8 *)(record + 0x31);
        *(s8 *)(record + 0x27) = *(s16 *)(record + 0x24) / *(s8 *)(record + 0x26);
        if (D_800BE616 != 0 && goal < *(s8 *)(record + 0x27)) {
            *(s8 *)(record + 0x27) = goal + 1;
        }
        if (*(s8 *)(record + 0x28) < *(s8 *)(record + 0x27)) {
            *(s8 *)(record + 0x28) = *(s8 *)(record + 0x27);
            if (actorId < D_8008FD90 && *(s8 *)(record + 0x30) == 0) {
                time = *(s32 *)(record + 0x1C);
                if (time > 0) {
                    if (goal >= *(s8 *)(record + 0x28)) {
                        best = D_800E0C10 + actorId;
                        elapsed = (u32)time - *(u32 *)(record + 0x18);
                        if (elapsed >= 32001) {
                            elapsed = 32000;
                        }
                        previousBest = *best;
                        if (previousBest <= 0 || elapsed < previousBest) {
                            *best = elapsed;
                        }
                        *(s32 *)(record + 0x20) = elapsed;
                    }
                    if (goal == *(s8 *)(record + 0x28)) {
                        finish = *(s32 *)(record + 0x1C);
                        if (finish >= 360001) {
                            finish = 360000;
                        }
                        D_800E0C18[actorId] = finish;
                    }
                }
            }
            if (goal == *(s8 *)(record + 0x28)) {
                *(u32 *)(record + 0x18) = 0u - *(u32 *)(record + 0x1C);
            } else if (*(s8 *)(record + 0x28) < goal) {
                *(s32 *)(record + 0x18) = *(s32 *)(record + 0x1C);
            }
        }
    }
    return step;
}

/* Advance past type-four route links, then place and orient the actor. */
void func_15088D58(u8 *actor) {
    extern void func_15088F30(u8 *, f32 *, f32 *, f32 *);
    extern f32 func_150498A4(f32 *, s32, f32, f32 *);
    extern f32 func_150497E0(f32 *, s32, f32);
    extern u16 func_1505A630(f32, f32, s32);
    extern f32 func_15144BC8(f32);
    extern f32 D_8009DA04;
    s32 rotation;
    f32 heading;
    f32 slopeX;
    f32 slopeZ;
    f32 x[4];
    f32 y[4];
    f32 z[4];
    s32 index;
    u8 *record;
    u8 *routes;
    u8 *neighbors;
    s32 kind;
    s32 i;
    s32 neighbor;

    index = func_1508855C((s32)actor);
    if (index >= 0) {
        record = D_800872A0 + index * 0x84;
        *(f32 *)(record + 0) = 0.5f;
        *(f32 *)(record + 4) = 0.5f;
        *(f32 *)(record + 8) = 0.5f;
        do {
            routes = D_800D2350;
            kind = 0;
            neighbors = routes + record[0x2C] * 0x10;
            for (i = 0; i < 5; i++) {
                neighbor = neighbors[i + 9];
                if (neighbor != 0xFF) {
                    if (routes[neighbor * 0x10 + 0xE] == 4) {
                        kind = routes[neighbor * 0x10 + 0xF];
                    }
                }
            }
            if (kind != 0) {
                func_15088A08(record, 1.0f);
            }
        } while (kind != 0);
        *(f32 *)(record + 8) = 0.0f;
        func_15088F30(record, x, y, z);
        *(f32 *)(actor + 0x14) = func_150498A4(x, 0, *(f32 *)(record + 8), &slopeX);
        *(f32 *)(actor + 0x18) = func_150497E0(y, 0, *(f32 *)(record + 8));
        *(f32 *)(actor + 0x1C) = func_150498A4(z, 0, *(f32 *)(record + 8), &slopeZ);
        heading = func_15144BC8((func_1505A630(*(f32 *)(record + 0x10),
            *(f32 *)(record + 0xC), 0) + 0x8000) * 0.0054931640625f);
        *(f32 *)(actor + 0x40) = heading;
        rotation = (s32)(heading * D_8009DA04) - 0x4000;
        *(s16 *)(actor + 0x7A) = rotation;
        *(s16 *)(actor + 0x78) = rotation;
        *(s16 *)(actor + 0x76) = rotation;
    }
}

/* Build four control points, using the first type-four route neighbor. */
void func_15088F30(u8 *record, f32 *xOutput, f32 *yOutput, f32 *zOutput) {
    f32 *x;
    f32 *y;
    f32 *z;
    u8 *cursor;
    u8 *table;
    u8 *route;
    u8 *other;
    s32 slot;
    s32 id;
    s32 candidate;
    s32 i;
    s32 currentX;
    s32 nextX;
    f32 speed;
    f32 deltaX;
    f32 deltaZ;

    slot = 0;
    cursor = record;
    x = xOutput;
    y = yOutput;
    z = zOutput;
    do {
        id = cursor[0x2B];
        cursor++;
        if (id != 0xFF) {
            table = D_800D2350;
            route = table + id * 0x10;
            other = route;
            for (i = 0; i < 5; i++) {
                candidate = route[i + 9];
                if (candidate != 0xFF && table[candidate * 0x10 + 0xE] == 4) {
                    other = (u8 *)((s16 *)table + candidate * 8);
                    i = 5;
                }
            }
            currentX = *(s16 *)(route + 0);
            nextX = *(s16 *)(other + 0);
            speed = *(f32 *)record;
            deltaX = (f32)(nextX - currentX);
            deltaZ = (f32)(*(s16 *)(other + 4) - *(s16 *)(route + 4));
            speed = deltaX * speed;
            *x = (f32)currentX + speed;
            *y = (f32)*(s16 *)(route + 2);
            *z = (f32)*(s16 *)(route + 4) + deltaZ * *(f32 *)record;
        } else {
            *x = (f32)(slot * 64);
            *y = 0.0f;
            *z = 0.0f;
        }
        slot++;
        x++;
        y++;
        z++;
    } while (slot != 4);
}

/* Prefer the first matching class; retain the last type match as fallback. */
u8 func_1508907C(u8 id, u8 type, u8 excluded, u8 preferred) {
    s32 i;
    u8 first;
    u8 candidate;
    u8 next;
    u8 result;
    u8 *node;
    u8 *selectedFirst;
    u8 *selected;
    u8 *selectedNext;
    u8 *cursor;

    result = 0xFF;
    if (id >= D_80087290) {
        return 0xFF;
    }
    node = D_800D2350 + id * 0x10;
    first = node[9];
    if (first != 0xFF && first != excluded &&
        ((selectedFirst = D_800D2350 + first * 0x10, selectedFirst[0xE] == type) || type == 0xFF)) {
        result = first;
        if (selectedFirst[0xF] == preferred) {
            return first;
        }
    }
    i = 1;
    cursor = node + 1;
    do {
        candidate = cursor[9];
        if (candidate != 0xFF && candidate != excluded &&
            ((selected = D_800D2350 + candidate * 0x10, selected[0xE] == type) || type == 0xFF)) {
            result = candidate;
            if (selected[0xF] == preferred) {
                return candidate;
            }
        }
        next = cursor[10];
        i += 2;
        if (next != 0xFF && next != excluded &&
            ((selectedNext = D_800D2350 + next * 0x10, selectedNext[0xE] == type) || type == 0xFF)) {
            result = next;
            if (selectedNext[0xF] == preferred) {
                return next;
            }
        }
        cursor += 2;
    } while (i != 5);
    return result;
}

/* Select the nearer route node and queue a clamped projection payload. */
void func_150891E8(u8 *record, u8 *actor) {
    extern u16 D_8008FDBC;
    extern s8 D_800D23A8;
    extern f32 D_8009DA08;
    extern f32 sqrtf(f32);
    extern void func_1512D560(u8 *, s32, void *);
    typedef struct {
        s16 x, y, z;
        u8 reserved[3];
        u8 neighbors[5];
        u8 kind;
        u8 routeClass;
    } ProjectionNode;
    u8 first;
    u8 next;
    ProjectionNode *node;
    ProjectionNode *candidateNode;
    u8 *payload;
    s32 i;
    s32 j;
    f32 currentDistance;
    f32 dx;
    f32 dz;
    f32 best;
    f32 dy;
    ProjectionNode *currentNode;
    u8 candidate;
    u8 current;
    u8 previous;
    volatile u8 preferred;
    f32 distance;
    u8 *object;
    f32 targetZ;

    i = *(s32 *)(actor + 0x318);
    if (i != 0) {
        if (D_8008FDBC & 0x40) {
            preferred = 1;
        } else {
            preferred = 0;
        }
        object = (u8 *)(u32)i;
        if (*(s8 *)(record + 0x30) == 2) {
            for (i = 0; i < D_80087290; i++) {
                node = (ProjectionNode *)D_800D2350 + i;
                if (node->kind == 5 && node->routeClass == 2) {
                    record[0x4A] = i;
                    record[0x4B] = i;
                    for (j = 0; j < 5; j++) {
                        if ((candidate = node->neighbors[j]) != 0xFF) {
                            i = D_800D23A8;
                            candidateNode = (ProjectionNode *)D_800D2350 + candidate;
                            if ((i == 0 && candidateNode->routeClass == 3) ||
                                (i != 0 && candidateNode->routeClass != 3)) {
                                record[0x4B] = candidate;
                            }
                        }
                    }
                    i = D_80087290;
                }
            }
            current = record[0x4B];
            previous = record[0x4A];
            first = current;
            best = D_8009DA08;
            do {
                node = (ProjectionNode *)D_800D2350 + current;
                next = func_1508907C(current, 0xFF, previous, preferred);
                previous = current;
                current = next;
                dx = *(f32 *)(actor + 0x14) - (f32)node->x;
                dz = *(f32 *)(actor + 0x1C) - (f32)node->z;
                distance = dx * dx + dz * dz;
                if (distance < best) {
                    best = distance;
                    record[0x4A] = previous;
                    record[0x4B] = next;
                }
            } while (first != current);
            func_1512D560(*(u8 **)(actor + 0x318), 5, 0);
            record[0x30] = 3;
        }
        current = record[0x4B];
        currentNode = (ProjectionNode *)D_800D2350 + current;
        previous = record[0x4A];
        node = (ProjectionNode *)D_800D2350 + previous;
        dx = *(f32 *)(actor + 0x14) - (f32)currentNode->x;
        dz = *(f32 *)(actor + 0x1C) - (f32)currentNode->z;
        currentDistance = dx * dx + dz * dz;
        dx = *(f32 *)(actor + 0x14) - (f32)node->x;
        dz = *(f32 *)(actor + 0x1C) - (f32)node->z;
        best = dx * dx + dz * dz;
        if (currentDistance < best) {
            record[0x4A] = current;
            record[0x4B] = func_1508907C(current, 0xFF, previous, preferred);
            node = currentNode;
            dx = *(f32 *)(actor + 0x14) - (f32)node->x;
            dz = *(f32 *)(actor + 0x1C) - (f32)node->z;
            best = currentDistance;
        }
        dy = *(f32 *)(actor + 0x18) - (f32)node->y;
        best = sqrtf(dy * dy + best);
        dx /= best;
        dy /= best;
        dz /= best;
        if (best > 1000.0f) {
            best = 1000.0f;
        }
        payload = record + 0x4C;
        *(u32 *)(payload + 0) = 0;
        *(f32 *)(payload + 0x20) = *(f32 *)(actor + 0x14);
        *(f32 *)(payload + 0x24) = *(f32 *)(actor + 0x18);
        *(f32 *)(payload + 0x28) = *(f32 *)(actor + 0x1C);
        *(f32 *)(payload + 0x14) = *(f32 *)(actor + 0x14) - dx * best;
        *(f32 *)(payload + 0x18) = *(f32 *)(actor + 0x18) - dy * best;
        targetZ = *(f32 *)(actor + 0x1C) - dz * best;
        *(u32 *)(payload + 4) = 0;
        *(f32 *)(payload + 0x30) = 30.0f;
        *(f32 *)(payload + 0x34) = 30.0f;
        *(f32 *)(payload + 0x2C) = 0.0f;
        *(f32 *)(payload + 0x1C) = targetZ;
        func_1512D560(*(u8 **)(actor + 0x318), 7, payload);
        *(f32 *)(object + 0x19C) = 30.0f;
        *(f32 *)(object + 0x1A4) = 30.0f;
        *(f32 *)(object + 0x1A0) = 30.0f;
        *(f32 *)(object + 0x1A8) = 30.0f;
    }
}

/* Queue a route stop or interpolate its six-channel spline payload. */
void func_150896EC(u8 *record, u8 *actor, s32 stop) {
    extern s8 D_800D23A8;
    extern s32 D_800BE9E4;
    extern f32 D_8009DA0C;
    extern f32 D_8009DA10;
    extern f64 D_8009DA18;
    extern void func_1512D560(u8 *, s32, void *);
    extern f32 func_150497E0(f32 *, s32, f32);
    f32 phase;
    u8 *xCursor;
    f32 *yCursor;
    f32 *zCursor;
    f32 *targetXCursor;
    f32 *targetYCursor;
    f32 *targetZCursor;
    f32 x[4];
    f32 y[4];
    f32 z[4];
    f32 targetX[4];
    f32 targetY[4];
    f32 targetZ[4];
    f32 angle;
    s32 previousValid;
    s32 i;
    u8 routeClass;
    u8 id;
    u8 next;
    u8 old;
    u8 *node;
    u8 *recordCursor;
    u8 *payload;

    node = *(u8 **)(actor + 0x318);
    if (node != 0) {
        xCursor = node;
        if (stop != 0) {
            payload = record + 0x4C;
            *(s32 *)(payload + 0x10) = 120;
            *(f32 *)(payload + 0x0C) = D_8009DA0C;
            func_1512D560(*(u8 **)(actor + 0x318), 10, payload);
            func_1512D560(*(u8 **)(actor + 0x318), 6, (void *)(u32)((u8 *)xCursor)[0x23D]);
            record[0x49] = 0;
        } else {
            if (*(s8 *)(record + 0x49) == 0) {
                routeClass = D_800D23A8 + 1;
                for (i = 0; i < D_80087290; i++) {
                    node = D_800D2350 + i * 16;
                    if (node[14] == 6 && node[15] == routeClass) {
                        record[0x44] = i;
                        i = D_80087290;
                    }
                }
                id = func_1508907C(record[0x44], 6, 255, 0);
                record[0x45] = id;
                next = func_1508907C(id, 6, record[0x44], 0);
                record[0x46] = next;
                record[0x47] = func_1508907C(next, 6, record[0x45], 0);
                *(f32 *)(record + 0x38) = *(f32 *)(actor + 0x14);
                *(f32 *)(record + 0x3C) = *(f32 *)(actor + 0x18);
                *(f32 *)(record + 0x40) = *(f32 *)(actor + 0x1C);
                *(f32 *)(record + 0x34) = 0.0f;
                func_1512D560(*(u8 **)(actor + 0x318), 5, (void *)(u32)((u8 *)xCursor)[0x23D]);
                record[0x49] = 1;
            }
            *(f32 *)(record + 0x34) += D_8009DA10 * (f32)D_800BE9E4;
            if (*(f32 *)(record + 0x34) >= 1.0f) {
                previousValid = record[0x46];
                if (previousValid == 255) {
                    *(f32 *)(record + 0x34) = 1.0f;
                } else {
                    i = record[0x47];
                    old = record[0x45];
                    record[0x45] = previousValid;
                    *(f32 *)(record + 0x34) -= 1.0f;
                    record[0x46] = i;
                    record[0x44] = old;
                    record[0x47] = func_1508907C(i, 6, previousValid, 0);
                }
            }
            previousValid = 0;
            recordCursor = record;
            xCursor = (u8 *)x;
            yCursor = y;
            zCursor = z;
            targetXCursor = targetX;
            targetYCursor = targetY;
            targetZCursor = targetZ;
            do {
                id = recordCursor[0x44];
                if (id != 255) {
                    previousValid = 1;
                    func_15086CBC(id, (f32 *)xCursor, yCursor, zCursor);
                    func_15086CBC(func_1508907C(recordCursor[0x44], 4, 255, 0),
                        targetXCursor, targetYCursor, targetZCursor);
                } else if (previousValid == 1) {
                    previousValid = 0;
                    angle = (f32)((f64)*(f32 *)(actor + 0x40) * 0.01745);
                    *(f32 *)xCursor = *(f32 *)(record + 0x38) - sinf(angle) * 500.0f;
                    *yCursor = *(f32 *)(record + 0x3C) + 180.0f;
                    *zCursor = *(f32 *)(record + 0x40) - cosf(angle) * 500.0f;
                    *targetXCursor = *(f32 *)(record + 0x38);
                    *targetYCursor = *(f32 *)(record + 0x3C) + 120.0f;
                    *targetZCursor = *(f32 *)(record + 0x40);
                } else {
                    *(f32 *)xCursor = (*(f32 *)(xCursor - 4) - *(f32 *)(xCursor - 8)) + *(f32 *)(xCursor - 4);
                    *yCursor = (yCursor[-1] - yCursor[-2]) + yCursor[-1];
                    *zCursor = (zCursor[-1] - zCursor[-2]) + zCursor[-1];
                    *targetXCursor = (targetXCursor[-1] - targetXCursor[-2]) + targetXCursor[-1];
                    *targetYCursor = (targetYCursor[-1] - targetYCursor[-2]) + targetYCursor[-1];
                    *targetZCursor = (targetZCursor[-1] - targetZCursor[-2]) + targetZCursor[-1];
                }
                targetZCursor++;
                recordCursor++;
                xCursor += 4;
                yCursor++;
                zCursor++;
                targetXCursor++;
                targetYCursor++;
            } while (targetZCursor != targetZ + 4);
            phase = *(f32 *)(record + 0x34);
            payload = record + 0x4C;
            *(f32 *)(payload + 0x14) = func_150497E0(x, 0, phase);
            *(f32 *)(payload + 0x18) = func_150497E0(y, 0, phase);
            *(f32 *)(payload + 0x1C) = func_150497E0(z, 0, phase);
            *(f32 *)(payload + 0x20) = func_150497E0(targetX, 0, phase);
            *(f32 *)(payload + 0x24) = func_150497E0(targetY, 0, phase);
            *(f32 *)(payload + 0x28) = func_150497E0(targetZ, 0, phase);
            *(u32 *)(payload + 0) = 0;
            *(u32 *)(payload + 4) = 0;
            *(f32 *)(payload + 0x30) = 30.0f;
            *(f32 *)(payload + 0x34) = 30.0f;
            *(f32 *)(payload + 0x2C) = 0.0f;
            func_1512D560(*(u8 **)(actor + 0x318), 7, payload);
        }
    }
}

void func_15089BB0() {
    D_800D23B0 = 0;
}

s32 func_15089BC0() {
    return 0;
}

s32 func_15089F9C() {
    return 0;
}

s32 func_1508A1BC() {
    return 0;
}

s32 func_1508A6FC() {
    return 0;
}

s32 func_1508B194(s32 arg0) {
    if (arg0 >= D_8008FD90) {
        return 0;
    }
    return *(s16 *) (D_8008FDD4 + arg0 * 12 + 0x70);
}

void func_1508B1D4(s32 arg0) {
    if (arg0 < D_8008FD90) {
        *(u16 *) (D_8008FDD4 + arg0 * 12 + 0x70) = 0;
    }
}

void func_1508B20C(f32 x, f32 y, f32 z, f32 radius) {
    u8 *base;
    s32 index;

    base = (u8 *)D_800D23B0;
    if (base != NULL) {
        if (*(s8 *)(base + 0x1745) < 8) {
            index = (*(s8 *)(base + 0x1745))++;
            *(s16 *)((u8 *)D_800D23B0 + index * 12 + 0x174C) = (s16)(s32)x;
            *(s16 *)((u8 *)D_800D23B0 + index * 12 + 0x174E) = (s16)(s32)y;
            *(s16 *)((u8 *)D_800D23B0 + index * 12 + 0x1750) = (s16)(s32)z;
            *(f32 *)((u8 *)D_800D23B0 + index * 12 + 0x1748) = radius * radius;
        }
    }
}

typedef struct NeighborVisitQueryB3020 {
    f32 x;
    f32 z;
    f32 threshold;
    f32 distances[8];
    s16 count;
    u8 ids[8];
    u8 visited[32];
} NeighborVisitQueryB3020;

void func_1508B2A8(u8 id, NeighborVisitQueryB3020 *query) {
    u8 *node;
    u8 *walk;
    s32 i;
    f32 x;
    f32 z;

    query->visited[id >> 3] |= 1 << (id & 3);
    node = D_800D2350 + id * 16;
    x = (f32)*(s16 *)(node + 0) - query->x;
    z = (f32)*(s16 *)(node + 4) - query->z;
    z = x * x + z * z;
    if (query->threshold < z) {
        if (query->count < 8) {
            ((u8 *)query)[query->count + 0x2E] = id;
            *(f32 *)((u8 *)query + query->count * 4 + 0xC) = z;
            (query->count)++;
        }
    } else {
        for (i = 0, walk = node; i < 5; i++) {
            id = walk[9];
            if (id != 0xFF) {
                if (!(query->visited[(u8)(id / 1) >> 3] & (1 << ((u8)(id / 1) & 3)))) {
                    func_1508B2A8(id, query);
                }
            }
            walk++;
        }
    }
}

void func_1508B3F8(void) {
    NeighborVisitQueryB3020 query;
    NeighborVisitQueryB3020 *context;
    s32 *selections;
    u8 *zone;
    u8 *actor;
    u8 *nodes;
    u8 *node;
    s32 i;
    s32 player;
    s32 ready;
    s32 root;
    s32 best;
    s32 j;
    f32 x;
    f32 y;
    f32 z;
    f32 dx;
    f32 dz;
    f32 minimum;
    u8 *ids;
    u8 *distances;
    u8 *end;
    s32 remainder;

    context = &query;
    selections = (s32 *)(D_800D23B0 + 0x55C);
    zone = (u8 *)D_800D23B0 + 0x1748;
    for (i = 0; i < D_8008FD8C; i++) {
        if (selections[i] != -1) {
            selections[i] = -2;
        }
    }
    for (i = 0; i < *(s8 *)((u8 *)D_800D23B0 + 0x1745); i++, zone += 12) {
        context->threshold = *(f32 *)(zone + 0);
        x = (f32)*(s16 *)(zone + 4);
        y = (f32)*(s16 *)(zone + 6);
        z = (f32)*(s16 *)(zone + 8);
        ready = 0;
        for (player = D_8008FD90, actor = D_800CC2D0 + player * 0x32C;
             player < D_8008FD8C; player++, actor += 0x32C) {
            dz = *(f32 *)(actor + 0x18) - y;
            if (dz < 200.0f && -100.0f < dz) {
                dx = *(f32 *)(actor + 0x14) - x;
                dz = *(f32 *)(actor + 0x1C) - z;
                if (dx * dx + dz * dz < context->threshold + 100.0f) {
                    best = 0xFF;
                    minimum = D_8009DA5C;
                    if (!ready) {
                        context->count = 0;
                        ready = 1;
                        root = func_15085DF8(x, y, z, 0, func_15085DA8(y));
                        if (root != -1) {
                            context->x = x;
                            context->z = z;
                            context->count = 0;
                            bzero(context->visited, 32);
                            func_1508B2A8((u8)root, context);
                        }
                    }
                    /* Keep the remainder-first, four-candidate retail scan. */
                    j = 0;
                    if (context->count > 0) {
                        nodes = D_800D2350;
                        remainder = context->count & 3;
                        if (remainder) {
                            do {
                                node = nodes + context->ids[j] * 16;
                                dx = (f32)*(s16 *)(node + 0) - *(f32 *)(actor + 0x14);
                                dz = (f32)*(s16 *)(node + 4) - *(f32 *)(actor + 0x1C);
                                dz = dx * dx + dz * dz;
                                if (dz < context->distances[j] && dz < minimum) {
                                    best = context->ids[j];
                                    minimum = dz;
                                }
                                j++;
                            } while (j != remainder);
                            if (j == context->count) {
                                goto selection;
                            }
                        }
                        ids = (u8 *)context + j;
                        distances = (u8 *)context + j * 4;
                        end = (u8 *)context + context->count * 4;
                        do {
                            node = nodes + ids[46] * 16;
                            dx = (f32)*(s16 *)(node + 0) - *(f32 *)(actor + 0x14);
                            dz = (f32)*(s16 *)(node + 4) - *(f32 *)(actor + 0x1C);
                            dz = dx * dx + dz * dz;
                            if (dz < *(f32 *)(distances + 12) && dz < minimum) {
                                best = ids[46];
                                minimum = dz;
                            }
                            node = nodes + ids[47] * 16;
                            dx = (f32)*(s16 *)(node + 0) - *(f32 *)(actor + 0x14);
                            dz = (f32)*(s16 *)(node + 4) - *(f32 *)(actor + 0x1C);
                            dz = dx * dx + dz * dz;
                            if (dz < *(f32 *)(distances + 16) && dz < minimum) {
                                best = ids[47];
                                minimum = dz;
                            }
                            node = nodes + ids[48] * 16;
                            dx = (f32)*(s16 *)(node + 0) - *(f32 *)(actor + 0x14);
                            dz = (f32)*(s16 *)(node + 4) - *(f32 *)(actor + 0x1C);
                            dz = dx * dx + dz * dz;
                            if (dz < *(f32 *)(distances + 20) && dz < minimum) {
                                best = ids[48];
                                minimum = dz;
                            }
                            node = nodes + ids[49] * 16;
                            dx = (f32)*(s16 *)(node + 0) - *(f32 *)(actor + 0x14);
                            dz = (f32)*(s16 *)(node + 4) - *(f32 *)(actor + 0x1C);
                            dz = dx * dx + dz * dz;
                            if (dz < *(f32 *)(distances + 24) && dz < minimum) {
                                best = ids[49];
                                minimum = dz;
                            }
                            distances += 16;
                            ids += 4;
                        } while (distances != end);
                    }
                  selection:
                    if (best != 0xFF) {
                        node = D_800D2350 + best * 16;
                        if (selections[player] != -2) {
                            *(s32 *)((u8 *)D_800D23B0 + player * 4 + 0x5C) = 1;
                        }
                        selections[player] = node[7];
                    }
                }
            }
        }
    }
    for (i = 0; i < D_8008FD8C; i++) {
        if (selections[i] < 0) {
            selections[i] = -1;
        }
    }
    *(s8 *)((u8 *)D_800D23B0 + 0x1745) = 0;
}

s32 func_1508B9BC() {
    return 0;
}

s32 func_1508BC20() {
    return 0;
}

s32 func_1508BF14() {
    return 0;
}

s32 func_1508C194(s32 arg0) {
    return 0;
}

s32 func_1508C1A4() {
    return 0;
}

s32 func_1508C5B8() {
    return 0;
}

s32 func_1508C9CC() {
    return 0;
}

s32 func_1508CA88() {
    s8 *ptr = (s8 *) D_800D23B0;
    s32 value;

    ptr[0x1703] += 1;
    ptr = (s8 *) D_800D23B0;
    value = ptr[0x1703];
    if (value >= D_8008FD90) {
        ptr[0x1703] = 0;
        value = *(s8 *) (D_800D23B0 + 0x1703);
    }
    return value;
}

s32 func_1508CAD8() {
    return 0;
}

s32 func_1508D850() {
    return 0;
}

s32 func_1508DA1C() {
    return 0;
}

s32 func_1508DAEC() {
    return 0;
}

s32 func_1508DC24() {
    return 0;
}

void func_1508E6C8() {
}

/* Return the limit for the selected route type. */
s32 func_1508E6D0(s32 type) {
    switch (type) {
        case 63: return 1800;
        case 20: return 3200;
        case 34: return 500;
        case 35: return 10000;
        case 22: return 100000;
        case 21: return 500;
        case 33: return 500;
        case 36: return 100000;
        case 25:
        case 64: return 500;
        case 9: return 5000;
        case 56: return 5000;
        case 24:
        case 65: return 100000;
        case 3: return 750;
        case 55: return 1500;
        default: return 100000;
    }
}

/* Return the mode-dependent code for the selected type. */
s32 func_1508E780(s32 type) {
    if (*(s16 *)((u8 *)D_800D23B0 + 0x16BC) != 0xB8) {
        switch (type) {
            case 20: return 0x28;
            case 63: return 0x2F;
            case 34: return 0x56;
            case 35: return 0x16;
            case 22: return 0x24;
            case 21: return 0x4B;
            case 33: return 0x58;
            case 36: return 0x63;
            case 25: return 0x57;
            case 64: return 0x21;
            case 9: return 0x1D;
            case 56: return 0x7B;
            case 57: return 0x82;
            case 55: return 0x85;
            case 24: return 0x55;
            case 65: return 0x2E;
            case 37: return 0x1060;
            default: return -1;
        }
    } else {
        switch (type) {
            case 8: return -1;
            case 1: return 0x105C;
            case 16: return 0x1019;
            case 2: return 0x1059;
        }
    }
    return -1;
}

extern u8 D_800D18A4[];
extern u16 D_800D18A2;
extern u16 D_800D18A0;
extern s32 D_800D23B0;
extern u8 D_800CC2D0[];
extern s32 D_800BE9F0;
extern s32 D_800D2E48;
extern s8 D_8008FD94;
s32 func_150859AC(s16, s32);
void func_15085710(s16, s32, s32);
void func_15062800(u8 *, u8 *);
u8 *func_1509B570(s32);
void func_15128774(u8 *, u8 *);

typedef struct { u8 bytes[0x32C]; } SlotTransferActor;
/* Transfer slot state and restore the destination actor's control fields. */
s32 func_1508E89C(s32 destinationSlot, s32 sourceSlot) {
    s32 actorIndex;
    s32 savedHalfword;
    u8 *script;
    s32 scriptOffset;
    u8 linkedSlot;
    u8 *destination;
    u32 sourceBit;
    u32 inverseDestination;

    if (D_800D18A4[destinationSlot] >= 0x33 &&
        !(D_800D18A2 & (1U << destinationSlot))) {
        inverseDestination = ~(1U << destinationSlot);
        sourceBit = 1U << sourceSlot;
        D_800D18A0 &= inverseDestination;
        D_800D18A2 |= 1U << destinationSlot;
        D_800D18A0 |= sourceBit;
        func_15085710((s16)destinationSlot, 2, func_150859AC((s16)sourceSlot, 3));
        func_15085710((s16)sourceSlot, 2, 0);
        if (*(s32 *)((u8 *)D_800D23B0 + 0x18) != 0) {
            *(s32 *)((u8 *)D_800D23B0 + 0x18) &= inverseDestination;
            *(s32 *)((u8 *)D_800D23B0 + 0x18) |= sourceBit;
        }
        if ((u8 *)D_800D23B0 + 0x9C != 0) {
            ((s32 *)((u8 *)D_800D23B0 + 0x9C))[destinationSlot] =
                ((s32 *)((u8 *)D_800D23B0 + 0x9C))[sourceSlot];
        }
        if ((u8 *)D_800D23B0 + 0x39C != 0) {
            ((s32 *)((u8 *)D_800D23B0 + 0x39C))[destinationSlot] =
                ((s32 *)((u8 *)D_800D23B0 + 0x39C))[sourceSlot];
        }
        if ((u8 *)D_800D23B0 + 0x3DC != 0) {
            ((s32 *)((u8 *)D_800D23B0 + 0x3DC))[destinationSlot] =
                ((s32 *)((u8 *)D_800D23B0 + 0x3DC))[sourceSlot];
        }
        if ((u8 *)D_800D23B0 + 0xEB0 != 0) {
            ((s32 *)((u8 *)D_800D23B0 + 0xEB0))[destinationSlot] =
                ((s32 *)((u8 *)D_800D23B0 + 0xEB0))[sourceSlot];
            if (((s32 *)((u8 *)D_800D23B0 + 0xEB0))[destinationSlot] >= 0) {
                ((s32 *)((u8 *)D_800D23B0 + 0xF70))[
                    ((s32 *)((u8 *)D_800D23B0 + 0xEB0))[destinationSlot]] = destinationSlot;
            }
        }
        ((s32 *)((u8 *)D_800D23B0 + 0x16C0))[destinationSlot] =
            ((s32 *)((u8 *)D_800D23B0 + 0x16C0))[sourceSlot];
        destination = ((SlotTransferActor *)D_800CC2D0)[destinationSlot].bytes;
        savedHalfword = *(s16 *)(*(u8 **)(destination + 0x31C) + 0x1AA);
        func_15062800(((SlotTransferActor *)D_800CC2D0)[sourceSlot].bytes, destination);
        if (D_800BE9F0 == 0x3F && destination[0x13C] >= 100) {
            linkedSlot = destination[0x13C] - 100;
            script = func_1509B570(D_800D2E48);
            if (script != 0) {
                scriptOffset = ((SlotTransferActor *)D_800CC2D0)[linkedSlot].bytes[0x3B] - 20;
                actorIndex = (SlotTransferActor *)destination - (SlotTransferActor *)D_800CC2D0;
                ((s32 *)(script + 0x24B8))[scriptOffset] = actorIndex | 0x2000;
                ((s32 *)(script + 0x24DC))[scriptOffset] = actorIndex;
            }
        }
        (*(u8 **)(destination + 0x31C))[0x84] = 0;
        destination[0x125] = 0x5A;
        *(s16 *)(*(u8 **)(destination + 0x31C) + 0x1AA) = savedHalfword;
        (*(u8 **)(destination + 0x31C))[0x1AF] = 0x40;
        func_15128774(*(u8 **)(destination + 0x318), destination);
        D_8008FD94++;
    }
    return 0;
}

s32 func_1508EB90(s32 arg0, s32 arg1, s32 arg2) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    return func_1509BFB0(1, temp_v0 | 0x2000, arg1, arg2);
}

void func_1508EBF8(s32 arg0, s32 arg1) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    func_1509BFB0(1, temp_v0 | 0x2000, 0x14, arg1);
}

void func_1508EC5C(s32 arg0, s32 arg1) {
    s32 temp_v0 = D_800CC40F[arg0 * 0x32C];

    func_1509BFB0(1, temp_v0 | 0x2000, 0x61, arg1);
}

typedef struct {
    u16 unk0;
    u16 count;
    u32 unk4;
    u16 entries[8];
} PackedPeerRow;
/* Find a different group entry in the first row containing the packed key. */
s32 func_1508ECC0(u32 group, u32 value, u16 peerGroup) {
    u32 rowIndex;
    u32 keyIndex;
    u32 peerIndex;
    u16 key;

    group = (u16)group;
    value = (u16)value;
    for (rowIndex = 0; rowIndex < D_80087380; rowIndex++) {
        for (keyIndex = 0; keyIndex < ((PackedPeerRow *)D_800D23C0)[rowIndex].count; keyIndex++) {
            key = (group << 12) + value;
            if (((PackedPeerRow *)D_800D23C0)[rowIndex].entries[keyIndex] == key) {
                for (peerIndex = 0; peerIndex < ((PackedPeerRow *)D_800D23C0)[rowIndex].count; peerIndex++) {
                    if ((((PackedPeerRow *)D_800D23C0)[rowIndex].entries[peerIndex] >> 12) == peerGroup && peerIndex != keyIndex) {
                        return ((PackedPeerRow *)D_800D23C0)[rowIndex].entries[peerIndex] & 0xFFF;
                    }
                }
                return -1;
            }
        }
    }
    return -1;
}

void func_1508EDBC(u32 arg0) {
    if (arg0 < D_80087380) {
        s32 off = arg0 * 24;

        *(u16 *) (D_800D23C0 + off + 2) = 0;
        *(u32 *) (D_800D23C0 + off + 4) = 0;
        *(u16 *) (D_800D23C0 + off) = 0;
    }
}

extern u8 *D_800D23C0;
extern u32 D_80087380;
void func_15114B94(s32);
void func_1503DDD0(s32);
void func_1508EDBC(u32);

/* Dispatch typed entries in the first matching packed row, then clear it. */
void func_1508EE0C(u16 group, u16 value) {
    u32 rowIndex;
    u32 entryIndex;
    u16 key;
    u16 packed;

    for (rowIndex = 0; rowIndex < D_80087380; rowIndex++) {
        for (entryIndex = 0; entryIndex < ((PackedPeerRow *)D_800D23C0)[rowIndex].count; entryIndex++) {
            key = (group << 12) + value;
            if (((PackedPeerRow *)D_800D23C0)[rowIndex].entries[entryIndex] == key) {
                for (entryIndex = 0; entryIndex < ((PackedPeerRow *)D_800D23C0)[rowIndex].count; entryIndex++) {
                    packed = ((PackedPeerRow *)D_800D23C0)[rowIndex].entries[entryIndex];
                    switch (packed >> 12) {
                        case 2:
                            func_15114B94(packed & 0xFFF);
                            break;
                        case 3:
                            func_1503DDD0(packed & 0xFFF);
                            break;
                    }
                }
                func_1508EDBC(rowIndex);
                return;
            }
        }
    }
}
