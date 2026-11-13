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

f32 func_15048A70(f32 current, f32 target);
f32 fabsf(f32 value);
#pragma intrinsic (fabsf)
void func_15048758(f32 *value);
/* Smooth a wrapped angle and its velocity, clamping a near-target overshoot. */
void func_15049688(f32 *angle, f32 target, f32 *velocity, f32 strength,
                   f32 damping, f32 deltaTime) {
    f32 difference = func_15048A70(*angle, target);
    f32 magnitude = fabsf(difference);
    f32 direction = difference < 0.0f ? -1.0f : 1.0f;
    f32 current = *velocity;
    *velocity = current + (difference * strength - current) * damping * deltaTime;
    if (magnitude < 10.0f) {
        f32 nextDifference = func_15048A70(*velocity * deltaTime + *angle, target);
        f32 nextDirection = nextDifference < 0.0f ? -1.0f : 1.0f;
        if (direction != nextDirection) {
            *angle = target;
            *velocity = 0.0f;
            goto done;
        }
    }
    *angle += *velocity * deltaTime;
done:
    func_15048758(angle);
}
