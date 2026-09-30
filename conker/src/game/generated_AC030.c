#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/AC030.s. */

void func_1507EEB8(u8 arg0, u8 *arg1);
extern u8 *D_800D154C;
extern u8 *D_80086BA0[];
extern u8 *D_80086C24[];
extern u8 D_8009BBF0[];

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

s32 func_1507EEF4() {
    return 0;
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

s32 func_1507F4C0() {
    return 0;
}

s32 func_1507F54C() {
    return 0;
}

s32 func_1507F640() {
    return 0;
}

s32 func_1507FC2C() {
    return 0;
}

s32 func_1507FEA0() {
    return 0;
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
