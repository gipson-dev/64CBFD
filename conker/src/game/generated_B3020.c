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
s32 func_150888A8();

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
    f32 minimum;
    f32 fraction;
    f32 ax;
    f32 az;
    f32 nx;
    f32 nz;
    f32 constant;
    f32 start;
    f32 end;
    f32 swap;

    band = func_15085DA8(y);
    count = D_80087290;
    minimum = 100.0f;
    if (count > 0) {
        nodes = D_800D2350;
        for (i = 0; i < count; i++) {
            first = nodes + i * 16;
            if (first[14] == 1 && first[6] == band) {
                for (j = 0; j < 5; j++) {
                    id = first[j + 9];
                    if (id != 255 && i < id) {
                        second = nodes + id * 16;
                        if (second[14] == 1) {
                            nx = (f32)(*(s16 *)(second + 4) - *(s16 *)(first + 4));
                            nz = -(f32)(*(s16 *)(second + 0) - *(s16 *)(first + 0));
                            ax = (f32)*(s16 *)(first + 0);
                            az = (f32)*(s16 *)(first + 4);
                            constant = -(ax * nx + nz * az);
                            start = x * nx + z * nz + constant;
                            end = (x + dx) * nx + (z + dz) * nz + constant;
                            if ((end < 0.0f && 0.0f <= start) ||
                                (start < 0.0f && 0.0f <= end)) {
                                if (end < 0.0f) {
                                    end = -end;
                                }
                                if (start < 0.0f) {
                                    start = -start;
                                }
                                swap = nx;
                                nx = -nz;
                                nz = swap;
                                fraction = start / (start + end);
                                constant = -(ax * nx + swap * az);
                                start = (x + fraction * dx) * nx +
                                        (z + fraction * dz) * nz + constant;
                                end = (f32)*(s16 *)(second + 0) * nx +
                                      nz * (f32)*(s16 *)(second + 4) + constant;
                                if ((0.0f < end && 0.0f < start && start <= end) ||
                                    (end < 0.0f && start < 0.0f && end <= start)) {
                                    if (fraction < minimum) {
                                        minimum = fraction;
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
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

s32 func_15087CC0() {
    return 0;
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
        value = func_150888A8(rec[0x2C], value & 0xFF, 1);
        rec[0x2E] = value;
    }
    rec[0x2F] = arg1;
}

s32 func_15087E54() {
    return 0;
}

s32 func_15087EF0() {
    return 0;
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

s32 func_150882E4() {
    return 0;
}

s32 func_150883B0() {
    return 0;
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

s32 func_150888A8() {
    return 0;
}

s32 func_15088A08() {
    return 0;
}

s32 func_15088D58() {
    return 0;
}

s32 func_15088F30() {
    return 0;
}

s32 func_1508907C() {
    return 0;
}

s32 func_150891E8() {
    return 0;
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
