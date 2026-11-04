#include <ultra64.h>

#include "variables.h"

/* Recovered and remaining routines from the text-only asm slice asm/6CCB0.s. */

typedef struct {
    s16 unused0;
    s16 categoryMask;
    s16 siblingOffset;
    u16 radius;
    s16 centerX;
    s16 centerZ;
    s16 childOffset;
} SpatialMembershipNode1503F800;

extern u8 *D_800DBE48;
void func_1510F800(s32 context);

typedef struct {
    u8 pad0[0x14];
    f32 x;
    u8 pad18[0x4];
    f32 z;
    u8 pad20[0x300];
    u8 query_data;
} QueryActor;

extern u8 D_800C67F0;
extern u8 D_800C67F1;

/* Return zero only when the coordinate reaches a selected leaf. */
s32 func_1503F800(void *unusedQuery, s32 x, s32 z, s32 category, s32 unusedMode) {
    s16 centerX;
    s16 centerZ;
    s16 childOffset;
    s16 queryX;
    s16 queryZ;
    s16 offset;
    u16 radius;
    SpatialMembershipNode1503F800 *node;

    queryZ = z;
    queryX = x;
    x = queryX;
    z = queryZ;
    func_1510F800(0);
    node = (SpatialMembershipNode1503F800 *)D_800DBE48;
    if (node != NULL) {
loop:
        centerX = node->centerX;
        radius = node->radius;
        if (((centerX + radius) >= x) && (x >= (centerX - radius))) {
            centerZ = node->centerZ;
            if (((centerZ + radius) >= z) && (z >= (centerZ - radius))) {
                if (!(node->categoryMask & (1 << category))) {
                    goto miss;
                }
                childOffset = node->childOffset;
                if (childOffset != 0) {
                    offset = childOffset;
                    goto advance;
                }
                return 0;
            }
        }
        offset = node->siblingOffset;
advance:
        if (offset != 0) {
            node = (SpatialMembershipNode1503F800 *)((u8 *)node + offset);
        } else {
            node = NULL;
        }
        if (node == NULL) {
            goto miss;
        }
        goto loop;
    }
miss:
    return 1;
}

s32 func_1503F904(QueryActor *actor, s32 arg1, s32 arg2) {
    return func_1503F800(&actor->query_data, (s16)actor->x, (s16)actor->z, arg1, 1);
}

void func_1503F964(void) {
    s32 start;
    s32 index;

    if (D_800C67F0 == 0) {
        return;
    }

    start = D_800C67F1;
    index = start + 1;
    if (index >= 25) {
        index = 0;
    }

    while (index != start) {
        if (D_800CC2D0[index].unkF8 & 0x00800000) {
            D_800C67F1 = index;
            return;
        }
        index++;
        if (index >= 25) {
            index = 0;
        }
    }
}
