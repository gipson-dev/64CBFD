#include <ultra64.h>

/* Recovered routines and remaining placeholders from asm/76A60.s. */

/* Smooth one position and velocity toward a target, clamping overshoot. */
void func_150495B0(f32 *position, f32 target, f32 *velocity, f32 strength,
                   f32 damping, f32 deltaTime) {
    f32 difference;
    f32 direction;
    f32 next;
    f32 nextDirection;
    difference = target - *position;
    direction = difference < 0.0f ? -1.0f : 1.0f;
    difference *= strength;
    *velocity += (difference - *velocity) * damping * deltaTime;
    next = *velocity * deltaTime + *position;
    nextDirection = target < next ? -1.0f : 1.0f;
    if (nextDirection == direction) {
        *position = next;
    } else {
        *position = target;
        *velocity = 0.0f;
    }
}

s32 func_15049688() {
    return 0;
}
