#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/F3BA0.s. */

s32 func_150C6D90();
s32 func_150C68C4();

void func_150C66F0(u8 *arg0) {
    if (*(u32 *) (arg0 + 0x6C) != 0) {
        u8 *temp_v0 = *(u8 **) (arg0 + 0x6C) + 0xB0;

        *(temp_v0 + 4) = 1;
    } else {
        *(u32 *) (arg0 + 0x6C) = func_150C6D90(arg0);
    }
}

typedef struct {
    u32 opaque0;
    u8 notification;
    u8 opaque5[3];
    f32 base;
    f32 amplitude;
    f32 target;
    s16 remaining;
    s16 minimum;
    s16 range;
    u16 opaque1A;
    f32 gain;
} EmbeddedIntegerOscillator;
extern s32 D_800BE9E4;
s32 func_150ADA20(void);
f32 func_150ADA68(void);
/* Capture and clear notification, renew expired timing, then blend the signed rate. */
s32 func_150C673C(u8 *input) {
    EmbeddedIntegerOscillator *oscillator;
    s8 notified;
    oscillator = (EmbeddedIntegerOscillator *)(input + 0xB0);
    notified = 1;
    if (oscillator->notification == 0) notified = 0;
    oscillator->notification = 0;
    oscillator->remaining -= (u32)D_800BE9E4;
    if (oscillator->remaining < 0) {
        u32 randomValue;
        randomValue = (u32)func_150ADA20();
        oscillator->remaining = randomValue % (oscillator->range + 1) + oscillator->minimum;
        oscillator->target = func_150ADA68();
        oscillator->target = oscillator->target * oscillator->amplitude + oscillator->base;
    }
    *(s32 *)(input + 0x24) = (u32)(s32)((oscillator->target - (f32)*(s32 *)(input + 0x24)) * oscillator->gain) + (u32)*(s32 *)(input + 0x24);
    return notified;
}

// Retail retains the otherwise dead temp_v0 + 0x58 update before the call.
#pragma GLOBAL_ASM("asm/nonmatchings/generated_F3BA0/func_150C682C.s")

void func_150C6870(u8 *arg0) {
    u8 *owner = *(u8 **)(arg0 + 0x18);

    if (*(u32 *)(arg0 + 0x70) != 0) {
        u8 *record = *(u8 **)(arg0 + 0x70) + 0x58;

        *(record + 4) = 1;
    } else {
        *(u32 *)(arg0 + 0x70) = func_150C68C4(owner, arg0);
    }
}

s32 func_150C68C4() {
    return 0;
}

s32 func_150C6A08() {
    return 0;
}

s32 func_150C6D1C(u8 *arg0) {
    s32 result = 1;

    if (*(u8 *)(arg0 + 0x5C) == 0) {
        result = 0;
    }
    *(u8 *)(arg0 + 0x5C) = 0;
    return result;
}

s32 func_150C6D40(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x18) = 0;
    func_151346EC(arg0);
}

s32 func_150C6D68(u8 *arg0) {
    u8 *temp_v0 = *(u8 **)(arg0 + 0x58) + 0x58;

    *(s32 *)(temp_v0 + 0x18) = 0;
    func_1513470C(arg0);
}

s32 func_150C6D90() {
    return 0;
}
