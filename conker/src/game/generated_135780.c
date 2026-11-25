#include <ultra64.h>
#include "structs.h"

/* Recovered callbacks and remaining placeholder from asm/135780.s. */

typedef struct {
    s32 unk0;
    s32 unk4;
    u8 flags;
} EventFlags;

s32 func_151082D0() {
    return 0;
}

/* Measured phase fields within a typed record prefix; the original full object
 * extent and effective type remain unknown. */
typedef struct {
    f32 remaining;
    f32 total;
    f32 transitionWidth;
    f32 edgeWidth;
    f32 cooldown;
} PhaseParameters15108658;

typedef struct {
    u8 retained00[0x1C];
    u32 phaseFlags;
    u8 retained20[0x54];
    s8 displayState;
    u8 retained75[0x33];
    PhaseParameters15108658 phase;
} PhaseState15108658;
extern f32 D_800BE9A4, D_800A2460, D_800A2464;
f32 func_150ADA68(void);
/* Classify the timed phase, advance its cooldown, and report whether it remains active.
 * The shared callback interface supplies a scratch pointer unused by this routine.
 * Keep the cooldown edge-distance subtraction unconditional: retail executes it
 * even when the opening cooldown comparison succeeds. */
s32 func_15108658(PhaseState15108658 *record, void *scratch) {
    PhaseParameters15108658 *phase = &record->phase;
    f32 current = phase->remaining;
    f32 left = phase->total - current;

    if (current < phase->edgeWidth || left < phase->edgeWidth) {
        record->phaseFlags = 0;
    } else if (phase->remaining < phase->transitionWidth || left < phase->transitionWidth) {
        record->phaseFlags = 0x10000;
    } else {
        record->phaseFlags = 0x20000;
    }
    if (phase->cooldown != 0.0f) {
        left = 11.0f - phase->cooldown;
        if (phase->cooldown < D_800A2460 || left < D_800A2460) {
            record->phaseFlags = 0;
            record->displayState = -1;
        } else {
            record->displayState = 3;
        }
        phase->cooldown -= D_800BE9A4;
        if (phase->cooldown < 0.0f) {
            phase->cooldown = 0.0f;
            record->displayState = -1;
        }
        return 1;
    } else {
        phase->remaining -= D_800BE9A4;
        if (phase->remaining < 0.0f) {
            return 0;
        }
        if (record->phaseFlags == 0x20000 && func_150ADA68() < D_800A2464) {
            phase->cooldown = 11.0f;
        }
    }
    return 1;
}


void func_151087FC(struct126 *arg0, s32 arg1, u8 arg2) {
    EventFlags *value = (EventFlags *)((s32)arg0 + 0x28);

    if (arg2 == 0x2B) {
        value->flags |= 1;
    } else if (arg2 == 0x2C) {
        value->flags &= ~1;
    }
}
