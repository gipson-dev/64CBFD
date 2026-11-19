#include <ultra64.h>

typedef struct {
    s32 fixedHeight;
    u32 *offsets;
    u8 *vertices;
    s32 unusedC;
} HeightCandidate131A90;
extern HeightCandidate131A90 D_800D3300[];
extern f32 D_800A2370;
void func_1510F800(s32);
s32 func_150A3A70(s32 x, s32 z);


/* Original no-op and constant-return callbacks from asm/131A90.s. */

void func_151045E0(s32 arg0, s32 arg1, s32 arg2) {
}

s32 func_151045F4(s32 arg0, s32 arg1) {
    return 1;
}

void func_15104608(f32 arg0, f32 arg1, s32 arg2, s32 arg3) {
}

s32 func_15104620(s32 arg0, s32 arg1) {
    return 1;
}

/* Return the nearest height from upward-facing terrain query triangles. */
s32 func_15104634(f32 x, f32 z, f32 targetHeight, f32 *heightOut) {
    f32 edgeX, value;
    s32 accepted[24];
    f32 vertexX[3];
    f32 vertexZ[3];
    s16 *vertex;
    s32 hits, acceptedCount, i, j, nearest;
    f32 reference, orientation;

    func_1510F800(0);
    hits = func_150A3A70((s32)x, (s32)z);
    if (hits == 0) {
        return 0;
    }
    acceptedCount = 0;
    for (i = 0; i < hits; i++) {
        for (j = 0; j < 3; j++) {
            vertex = (s16 *)(D_800D3300[i].vertices + D_800D3300[i].offsets[j]);
            vertexX[j] = vertex[0];
            vertexZ[j] = vertex[2];
        }
        value = vertexZ[1] - vertexZ[0];
        edgeX = vertexX[0] - vertexX[1];
        reference = -(value * vertexX[0] + vertexZ[0] * edgeX);
        orientation = value * vertexX[2] + vertexZ[2] * edgeX + reference;
        if (orientation > 0.0f) {
            accepted[acceptedCount++] = i;
        }
    }
    if (acceptedCount == 0) {
        return 0;
    }
    nearest = -1;
    /* Reuse the edge/orientation temporaries for distance and its running minimum. */
    orientation = D_800A2370;
    for (i = 0; i < acceptedCount; i++) {
        j = accepted[i];
        value = D_800D3300[j].fixedHeight * (1.0f / 256.0f) - targetHeight;
        if (value < 0.0f) {
            value = -(D_800D3300[j].fixedHeight * (1.0f / 256.0f) - targetHeight);
        }
        if (value < orientation || nearest == -1) {
            orientation = value;
            nearest = j;
        }
    }
    *heightOut = D_800D3300[nearest].fixedHeight * (1.0f / 256.0f);
    return 1;
}
