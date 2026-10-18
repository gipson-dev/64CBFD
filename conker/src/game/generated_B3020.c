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

s32 func_150870D0() {
    return 0;
}

s32 func_15087350() {
    return 0;
}

/* Dispatch route records using their live actor slot and movement state. */
void func_15087CC0(void) {
    extern s8 D_800D23A9;
    extern void func_150891E8(u8 *, u8 *);
    extern s32 func_150896EC();
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

#pragma GLOBAL_ASM("asm/nonmatchings/generated_B3020/func_1508802C.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_B3020/func_150880F8.s")

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

#pragma GLOBAL_ASM("asm/nonmatchings/generated_B3020/func_150885EC.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_B3020/func_1508868C.s")

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
    extern s32 func_15088F30();
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

s32 func_15088F30() {
    return 0;
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

s32 func_150896EC() {
    return 0;
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

s32 func_1508E6D0() {
    return 0;
}

s32 func_1508E780() {
    return 0;
}

s32 func_1508E89C() {
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

s32 func_1508ECC0() {
    return 0;
}

void func_1508EDBC(u32 arg0) {
    if (arg0 < D_80087380) {
        s32 off = arg0 * 24;

        *(u16 *) (D_800D23C0 + off + 2) = 0;
        *(u32 *) (D_800D23C0 + off + 4) = 0;
        *(u16 *) (D_800D23C0 + off) = 0;
    }
}

s32 func_1508EE0C() {
    return 0;
}
