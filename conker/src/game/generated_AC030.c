#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/AC030.s. */

extern u8 D_800B85A4[];
void func_1505E650(u8 *, u16, f32, f32, f32, f32, s32);

void func_1507EEB8(u8 arg0, u8 *arg1);
extern u8 *D_800D154C;
extern u8 *D_80086BA0[];
extern u8 *D_80086C24[];
extern u8 D_8009BBF0[];
extern s32 D_800BE9F0;
extern s32 D_800BE9E4;
extern u8 D_800C35EA;
void func_1507FF94(u8 *);

s32 func_150ADA20(void);

void func_1507EB80(u8 *arg0, s32 *arg1, u8 arg2) {
    if (*arg1 + 1 < 0x28) {
        arg0[*arg1] = arg2;
        *arg1 = *arg1 + 1;
    }
}

void func_1507EBB8(u8 *arg0, s32 *arg1, s32 arg2) {
    u8 *source = D_80086C24[arg2];
    s32 length = D_8009BBF0[arg2];

    if (*arg1 + length < 0x28) {
        bcopy(source, arg0 + *arg1, length);
        *arg1 += length;
    }
}

s32 func_1507EC38() {
    return 0;
}

void func_1507EE58(u8 arg0, u8 *arg1) {
    func_1507EEB8(arg0, arg1);
    if (arg0 == 0x11) {
        func_1507EEB8(0x12, arg1);
    } else if (arg0 == 0x12) {
        func_1507EEB8(0x11, arg1);
    }
}

void func_1507EEB8(u8 arg0, u8 *arg1) {
    s32 i;

    for (i = 4; i > 0; i--) {
        arg1[i] = arg1[i - 1];
    }
    arg1[0] = arg0;
}

/* Advance the captured player byte-state using a fresh random threshold. */
void func_1507EEF4(void) {
    u8 *state = *(u8 **)(D_800D154C + 0x31C) + 0x58;
    s32 threshold;

    if (state[0xC] == 0) {
        state[0xC] = 1;
        state[0xD] = 0;
    } else if (state[0xC] == 1) {
        func_150ADA20();
        if (state[0xD] >= 3) {
            state[0xC] = 2;
            state[0xD] = 0;
        }
    } else {
        threshold = (func_150ADA20() & 3) + 8;
        if (state[0xD] >= threshold) {
            state[0xC] = 1;
            state[0xD] = 0;
        }
    }
}

void func_1507EFA0(s32 arg0, u8 *arg1) {
    s32 i = 4;
    u8 *ptr = arg1 + 4;

    for (; i >= 0; i--) {
        if (arg0 == *ptr) {
            *ptr = 0;
            return;
        }
        ptr--;
    }
}

s32 func_1507EFD0() {
    return 0;
}

s32 func_1507F454(void) {
    u8 *state;
    s32 sequence;
    s32 value;

    state = *(u8 **)(D_800D154C + 0x31C) + 0x58;
    sequence = state[4];
    if (sequence == 0) {
        return 1;
    }

    state[5]++;
    value = D_80086BA0[sequence][state[5]];
    if (value == 0) {
        state[4] = 0;
        state[5] = 0;
        return 1;
    }
    return 0;
}

s32 func_1507F4C0(s32 arg0) {
    s32 base;

    if (arg0 == 0) {
        base = 180;
        arg0 = 60;
    } else {
        if (D_800BE9F0 == 0x31) {
            return 0;
        }
        base = 0;
        if (arg0 == 1) {
            base = 60;
            arg0 = 60;
        } else {
            arg0 = 30;
        }
    }

    return (func_150ADA20() % (u32) arg0) + base;
}

/* Start the actor animation selected for its current slot. */
void func_1507F54C(u8 *actor) {
    s32 animation;

    if (actor[0x13C] >= 100) {
        switch (D_800B85A4[actor[0x13C] * 0x32C]) {
        case 0x57:
            animation = 0x115;
            break;
        case 0x8C:
            animation = 0x1A5;
            break;
        case 0xA8:
        case 0xA9:
            animation = 0x1AF;
            break;
        case 0x89:
        case 0xBA:
            animation = 0x1FA;
            break;
        default:
            animation = 0xD8;
            break;
        }
        func_1505E650(actor, animation, 1.0f, 4.0f, 0.0f, 0.0f, 0);
    } else {
        func_1505E650(actor, 0xF, 1.0f, 3.0f, 0.0f, 0.0f, 0);
    }
}

s32 func_1507F640() {
    return 0;
}

s32 func_1507FC2C() {
    return 0;
}

/* Advance or reset an actor's child state, then finish its update. */
void func_1507FEA0(u8 *actor) {
    u8 *child = *(u8 **)(actor + 0x31C);
    u8 *state = child + 0x58;
    u8 countdown;
    s32 timer;
    s32 tick;
    u16 count;

    if (child == NULL || actor[0x127] == 0xFF) {
        return;
    }
    countdown = actor[0x13A];
    if (countdown != 0) {
        actor[0x13A] = countdown - 1;
    }
    if (state[0] == 1 && D_800C35EA != 1) {
        tick = D_800BE9E4;
        count = *(u16 *)(state + 2);
        if (count < 0xFFFF - tick) {
            *(u16 *)(state + 2) = count + tick;
        }
    } else {
        *(u16 *)(state + 2) = 0;
        state[4] = 0;
        state[5] = 0;
        state[0xC] = 0;
        state[0xD] = 0;
    }
    child = *(u8 **)(actor + 0x31C);
    timer = *(s16 *)(child + 0x66);
    if (timer != 0) {
        tick = D_800BE9E4;
        if (tick < timer) {
            *(s16 *)(child + 0x66) = timer - tick;
        } else {
            func_1507FF94(actor);
            child = *(u8 **)(actor + 0x31C);
            *(s16 *)(child + 0x66) = 0;
        }
    }
    func_1507FC2C(actor);
}

void func_1507FF94(u8 *arg0) {
    struct {
        u8 *target;
        u8 code;
    } rec;
    void *volatile rec_ptr;

    rec.target = arg0;
    rec.code = *(arg0 + 0x3B);
    rec_ptr = &rec;
    func_15191B8C(&rec, 0xD);
    func_151494E0(rec_ptr, 0xD);
}

s32 func_1507FFD8() {
    return 0;
}
