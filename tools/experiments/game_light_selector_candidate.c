#include <ultra64.h>

extern u8 *D_800DCD78;
extern u8 *D_800DBFF0;
extern u8 D_800BE9C0;
extern s8 D_800DCD30[];
extern u8 D_800DCD40[];
extern void func_1515E278(s32, s32, s32, s32, u8 *, s32, s32);
extern void func_1515E43C(s32, s32, s32, s32, u8 *, u8 *, u8 *, u8 *);
extern void func_1515EC78(u8 *, s32, u8 *, s32, s32, s32, s32);

/* Experimental: the first directional distance has no retail initializer. */
Gfx *func_1515D914(Gfx *commands, s32 slot, s32 x, s32 y, s32 z, s32 mode,
                    u8 *lightData, s32 capacity, u8 *ambientData, u8 *countOut,
                    s32 channels, u8 *history, s32 flags, u8 **nodesOut) {
    u8 ambient[3];
    u8 secondary[3];
    u8 environment[3];
    u8 extra[3];
    u8 secondaryAlpha;
    u8 environmentAlpha;
    s32 distances[11];
    u8 *selected[11];
    s16 query[3];
    s32 position[3];
    s32 distance;
    s32 found = 0;
    s32 odd;
    s32 i;
    s32 j;
    u32 slotMask;
    u8 *node;
    u8 *data;

    func_1515E278(x, y, z, channels, ambient, mode, flags);
    if (flags & 2) {
        func_1515E43C(x, y, z, channels, secondary, environment,
                      &secondaryAlpha, &environmentAlpha);
        for (i = 0; i < 3; i++) {
            s32 inverse = 255 - ambient[i];
            u8 factor = ambient[i] + ((inverse * secondaryAlpha) >> 8);
            extra[i] = (secondary[i] * factor) >> 8;
            factor = ambient[i] + ((inverse * environmentAlpha) >> 8);
            ambient[i] = (environment[i] * factor) >> 8;
        }
    }
    for (i = 0; i < 3; i++) {
        if (history != 0) {
            if (!(flags & 8)) {
                ambient[i] = (history[i] * 3 + ambient[i]) >> 2;
            }
            history[i] = ambient[i];
        }
        ambientData[i + 4] = ambient[i];
        ambientData[i] = ambient[i];
    }
    for (i = 0; i < capacity; i++) {
        distances[i] = 0x7FFFFFFF;
    }
    if (!(flags & 1)) {
        query[0] = x;
        query[1] = y;
        query[2] = z;
    } else {
        u8 *actor = D_800DBFF0 + slot * 0x9A0;
        f32 dx = *(f32 *) (actor + 0x2BC) - *(f32 *) (actor + 0x2F8);
        f32 dy = *(f32 *) (actor + 0x2C0) - *(f32 *) (actor + 0x2FC);
        f32 dz = *(f32 *) (actor + 0x2C4) - *(f32 *) (actor + 0x300);
        f32 length = sqrtf(dz * dz + (dx * dx + dy * dy));

        if (length != 0.0f) {
            f32 scale = 1000.0f / length;
            query[0] = (s32) (dx * scale + (f32) x);
            query[1] = (s32) (dy * scale + (f32) y);
            query[2] = (s32) (dz * scale + (f32) z);
        } else {
            query[0] = x;
            query[1] = y;
            query[2] = z;
        }
    }
    slotMask = 1U << ((u32) slot & 31);
    node = D_800DCD78;
    while (node != 0) {
        if (((node[0xC] & slotMask) || (flags & 0x20) || !(node[8] & 1)) &&
            (node[8] & channels) && node[9] == 0 && !(node[0xA] & slotMask)) {
            if (node[4] == 0) {
                if (*(s16 *) (node + 0xE) != -32768) {
                    position[0] = *(s16 *) (node + 0xE);
                    position[1] = *(s16 *) (node + 0x10);
                    position[2] = *(s16 *) (node + 0x12);
                } else {
                    f32 *coordinates = (f32 *) (((u32) *(u16 *) (node + 0x10) << 16) |
                                                *(u16 *) (node + 0x12));
                    position[0] = (s32) coordinates[0];
                    position[1] = (s32) coordinates[1];
                    position[2] = (s32) coordinates[2];
                }
                {
                    u32 dx = (u32) query[0] - (u32) position[0];
                    u32 dy = (u32) query[1] - (u32) position[1];
                    u32 dz = (u32) query[2] - (u32) position[2];
                    distance = (s32) ((dz * dz + dx * dx) + dy * dy);
                }
                if (!(flags & 4) && (s32) ((u32) node[0x2F] << 17) < distance) {
                    distance = 0x7FFFFFFF;
                }
            }
            for (i = 0; i < capacity - 1; i++) {
                if (distance < distances[i]) {
                    for (j = capacity - 2; j > i; j--) {
                        distances[j] = distances[j - 1];
                        selected[j] = selected[j - 1];
                    }
                    distances[i] = distance;
                    selected[i] = node;
                    if (found + 1 != capacity) {
                        found++;
                    }
                    break;
                }
            }
        }
        node = *(u8 **) node;
    }
    if (capacity != 0) {
        odd = found & 1;
        if (odd && nodesOut != 0) {
            nodesOut[found] = 0;
        }
        if (countOut != 0) {
            *countOut = (found + odd + 1) | (odd << 7);
        }
        gMoveWd(commands++, G_MW_NUMLIGHT, G_MWO_NUMLIGHT, (found + odd + 1) * 48);
    } else {
        if (countOut != 0) {
            *countOut = found;
        }
        gMoveWd(commands++, G_MW_NUMLIGHT, G_MWO_NUMLIGHT, found * 48);
    }
    if (capacity != 0) {
        data = lightData + (D_800BE9C0 * capacity + found) * 48;
        data[8] = D_800DCD30[slot * 3];
        data[9] = D_800DCD30[slot * 3 + 1];
        data[10] = D_800DCD30[slot * 3 + 2];
        if (flags & 2) {
            data[4] = extra[0];
            data[0] = extra[0];
            data[5] = extra[1];
            data[1] = extra[1];
            data[6] = extra[2];
            data[2] = extra[2];
        } else {
            data[4] = 0;
            data[0] = 0;
            data[5] = 0;
            data[1] = 0;
            data[6] = 0;
            data[2] = 0;
        }
        data -= found * 48;
        for (i = 0; i < found; i++) {
            node = selected[i];
            if (nodesOut != 0) {
                nodesOut[i] = node;
            }
            if (flags & 0x20) {
                node[0xC] |= slotMask;
            }
            if (node[4] == 0) {
                func_1515EC78(node, slot, data, x, y, z, flags);
            }
            gDma2p(commands++, G_MOVEMEM, data, 48, G_MV_LIGHT, 96 + i * 48);
            data += 48;
        }
        if (odd) {
            gDma2p(commands++, G_MOVEMEM, D_800DCD40, 48, G_MV_LIGHT, 96 + i * 48);
        }
        gDma2p(commands++, G_MOVEMEM, lightData + (D_800BE9C0 * capacity + i) * 48,
               48, G_MV_LIGHT, 96 + (i + odd) * 48);
        gDma2p(commands++, G_MOVEMEM, ambientData, 48, G_MV_LIGHT, 144 + (i + odd) * 48);
    }
    return commands;
}
