#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_1000A420(s32 arg0, s32 arg1, s32 arg2, f32 arg3, s32 arg4,
                  s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 *arg9,
                  s32 *argA, s32 *argB);
s32 func_1000A750(s32 arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4,
                  s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9,
                  s32 *argA, s32 *argB, s32 *argC);
s32 func_1000B060(f32 arg0, f32 arg1, s32 arg2);
/* End generated placeholder declarations. */

void func_1000E40C(s32, s32);
s32 func_150AD960(s32, s32, s32, s32);
s32 func_150AD9A0(s32, s32, s32);

s32 func_1000A420(s32 arg0, s32 arg1, s32 arg2, f32 arg3, s32 arg4,
                  s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 *arg9,
                  s32 *argA, s32 *argB) {
    f64 angle;
    s32 attenuation;
    f32 direction;
    s32 panFlags;
    s16 pan;
    s8 rotatedPan;
    s32 distance;

    panFlags = 128;
    if ((arg7 & 0x8000) != 0) {
        arg7 &= 0x7FFF;
        distance = func_150AD960(arg4, arg6, 0, 0);
    } else {
        distance = func_150AD9A0(arg4, arg5, arg6);
    }

    attenuation = 0x7FFF - (((arg8 - distance) << 15) / (arg8 - arg7));
    if (attenuation >= 401) {
        if (arg9 != NULL) {
            if (func_150AD960(arg0, arg2, 0, 0) >= 31) {
                direction = sqrtf((f32)((arg0 * arg0) + (arg2 * arg2)));
                if (D_8002C200 < direction) {
                    direction = arg0 / direction;
                }
                angle = func_150487E0(direction) * D_8002C208;
                pan = angle;
                if (arg2 > 0) {
                    if (pan < 0) {
                        pan = -128 - pan;
                    } else {
                        pan = 128 - pan;
                    }
                }
                rotatedPan = pan + (arg3 * D_8002C210);
                if ((rotatedPan >= 96) || (rotatedPan < -96)) {
                    pan = 0;
                } else if (rotatedPan >= 32) {
                    pan = 95 - rotatedPan;
                } else if (rotatedPan < -32) {
                    pan = -95 - rotatedPan;
                } else {
                    panFlags = 0;
                    pan = rotatedPan + rotatedPan;
                }
                *arg9 = (pan + 64) | panFlags;
            } else {
                *arg9 = 64;
            }
        }

        if ((0x7FFF - (((arg8 - distance) << 15) / (arg8 - arg7))) < 0) {
            attenuation = 0;
        }
        if (attenuation >= 0x8000) {
            attenuation = 0x7FFF;
        }
        *argA = attenuation;
    } else {
        *argA = 0;
    }

    if (argB != NULL) {
        *argB = distance;
    }
    return distance;
}

typedef struct {
    s16 x;
    s16 y;
    s16 z;
    s16 pad;
} PathPoint;

s32 func_1000A750(s32 arg0, s32 arg1, s32 arg2, s32 arg3, f32 arg4,
                  s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9,
                  s32 *argA, s32 *argB, s32 *argC) {
    PathPoint *points;
    PathPoint *point;
    f32 direction[3];
    f32 offset[3];
    f32 projection;
    f32 length;
    s32 count;
    s32 closestIndex;
    s32 closestDistance;
    s32 previousDistance;
    s32 nextDistance;
    s32 distance;
    s32 dx;
    s32 dy;
    s32 dz;
    s32 index;
    s32 segmentIndex;
    s32 retry;
    s16 pathX;
    s16 pathY;
    s16 pathZ;

    count = (*(u8 **)&D_800D2108)[arg0];
    if (count == 0) {
        return 0;
    }

    points = ((PathPoint **)D_800D2104)[arg0];
    closestIndex = -2;
    closestDistance = 0x7FFFFFFF;
    previousDistance = 0x7FFFFFFF;
    nextDistance = 0;

    for (index = 0; index < count; index++) {
        point = &points[index];
        dx = arg5 - point->x;
        dy = arg6 - point->y;
        dz = arg7 - point->z;
        distance = (dx * dx) + (dy * dy) + (dz * dz);

        if (distance < closestDistance) {
            closestIndex = index;
            previousDistance = index == 0 ? 0x7FFFFFFF : nextDistance;
            closestDistance = distance;
        } else if (index == closestIndex + 1) {
            nextDistance = distance;
        }
    }

    point = &points[closestIndex];
    pathX = point->x;
    pathY = point->y;
    pathZ = point->z;

    if ((count >= 2) && (closestDistance >= 0x6D61)) {
        segmentIndex = closestIndex;
        if ((closestIndex >= count - 1) || (previousDistance < nextDistance)) {
            segmentIndex--;
        }

        point = &points[segmentIndex];
        direction[0] = points[segmentIndex + 1].x - point->x;
        direction[1] = points[segmentIndex + 1].y - point->y;
        direction[2] = points[segmentIndex + 1].z - point->z;
        offset[0] = arg5 - point->x;
        offset[1] = arg6 - point->y;
        offset[2] = arg7 - point->z;

        projection = func_150AD900(direction, offset);
        retry = projection < 0.0f;
        length = func_150AD930(direction);
        length *= length;
        if (length < projection) {
            retry = 1;
        }

        if (retry != 0) {
            if (previousDistance < nextDistance) {
                segmentIndex++;
            } else {
                segmentIndex--;
            }

            point = &points[segmentIndex];
            direction[0] = points[segmentIndex + 1].x - point->x;
            direction[1] = points[segmentIndex + 1].y - point->y;
            direction[2] = points[segmentIndex + 1].z - point->z;
            offset[0] = arg5 - point->x;
            offset[1] = arg6 - point->y;
            offset[2] = arg7 - point->z;
            projection = func_150AD900(direction, offset);
            length = func_150AD930(direction);
            length *= length;
        }

        if (length != 0.0f) {
            if (projection < length) {
                func_15049148((struct17 *)direction, projection / length,
                              (struct17 *)direction);
            }
            point = &points[segmentIndex];
            pathX = point->x + direction[0];
            pathY = point->y + direction[1];
            pathZ = point->z + direction[2];
        }
    }

    return func_1000A420(pathX - arg1, pathY - arg2, pathZ - arg3, arg4,
                         pathX - arg5, pathY - arg6, pathZ - arg7, arg8,
                         arg9, argA, argB, argC);
}
s32 func_1000B060(f32 arg0, f32 arg1, s32 arg2) {
    s16 phi_a1;
    f32 sp18;
    s16 temp_t8;
    f64 temp_f6;
    s8 temp_t9;
    s16 phi_v1_2;

    sp18 = sqrtf((arg0 * arg0) + (arg1 * arg1));
    if (D_8002C214 < sp18) {
        sp18 = arg0 / sp18;
    }
    phi_a1 = 128;
    temp_f6 = func_150487E0(sp18) * D_8002C218;
    phi_v1_2 = temp_f6;
    if (0.0f < arg1) {
        temp_t8 = temp_f6;
        if ((s32)temp_t8 < 0) {
            phi_v1_2 = (s16)(-128 - temp_t8);
        } else {
            phi_v1_2 = (s16)(128 - temp_t8);
        }
    }
    temp_t9 = phi_v1_2 + arg2;
    phi_v1_2 = temp_t9;
    if ((phi_v1_2 >= 96) || (phi_v1_2 < -96)) {
        phi_v1_2 = 0;
    } else if ((s32)phi_v1_2 >= 32) {
        phi_v1_2 = (s16)(0x5F - phi_v1_2);
    } else if ((s32)phi_v1_2 < -32) {
        phi_v1_2 = (s16)(-0x5F - phi_v1_2);
    } else {
        phi_v1_2 += phi_v1_2;
        phi_a1 = 0;
    }
    return (phi_v1_2 + 64) | phi_a1;
}
