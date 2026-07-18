#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_151670C0();
s32 func_151671E8();
s32 func_15167310();
s32 func_151674F8();
s32 func_15167B44();
s32 func_15167C58();
s32 func_15167E0C();
s32 func_15168118();
s32 func_1516865C();
s32 func_15168870();
s32 func_15168C4C();
s32 func_15168E54();
s32 func_15168F84();
/* End generated placeholder declarations. */

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, s32 arg5);
void func_15168A4C(void *arg0, u8 arg1);
extern void (*D_8008CA20[])(void *);
extern void (*D_8008CB64[])(void);


// NON-MATCHING: not hugely far away
void func_15167010(void) {
    void (*func)(void);
    struct115 *cur;
    struct115 *end;

    cur = D_8008B4A8;
    end = (struct115 *) ((u8 *) D_8008B4A8 + 0x1484);

    while (cur < end) {
        func = (void (*)(void)) cur->unk18;
        if (func != NULL) {
            func();
        }
        cur++;
    }
}

void func_1516706C(void) {
    void (**func)(void);

    for (func = D_8008CB64; func < &D_8008CB64[3]; func++) {
        if (*func != NULL) {
            (*func)();
        }
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_151670C0.s. */
s32 func_151670C0() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_151671E8.s. */
s32 func_151671E8() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15167310.s. */
s32 func_15167310() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_151674F8.s. */
s32 func_151674F8() {
    return 0;
}
void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, s32 arg5) {
    u8 *ret;

    ret = func_10003C6C(arg2, 1, arg3, 0, arg5);
    if (ret != NULL) {
        ret[1] = arg1;
        func_15168A4C(ret, arg0);
        ret[0xC] = arg4;
    }

    return ret;
}

void func_15167AD8(void *arg0, u8 arg1, s32 arg2) {
    u8 *tmp;

    tmp = func_15167A68(3, arg2, 0x28, 0, arg1, 1);
    if (tmp != NULL) {
        bcopy(arg0, tmp + 0x10, 0x18);
        tmp[0x23] = 0xFF;
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15167B44.s. */
s32 func_15167B44() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15167C58.s. */
s32 func_15167C58() {
    return 0;
}
void func_15167D84(void *arg0, s32 arg1, s32 arg2, s8 arg3, u8 arg4, s32 arg5) {
    u8 *tmp;
    s32 kind;

    if (arg1 == 0) {
        kind = 5;
    } else {
        kind = 0x42;
    }

    tmp = func_15167A68(kind, arg5, arg2 + 0x50, 0, arg4, 1);
    if (tmp != NULL) {
        bcopy(arg0, tmp + 0x10, 0x38);
        tmp[0x48] = arg3;
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15167E0C.s. */
s32 func_15167E0C() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168118.s. */
s32 func_15168118() {
    return 0;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_1516865C.s. */
s32 func_1516865C() {
    return 0;
}
void *func_15168800(void *arg0, u8 arg1, s32 arg2) {
    u8 *tmp;

    tmp = func_15167A68(0xE, arg2, 0xB8, 1, arg1, 1);
    if (tmp != NULL) {
        bcopy(arg0, tmp + 0x10, 0xA8);
    }
    return tmp;
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168870.s. */
s32 func_15168870() {
    return 0;
}
// NON-MATCHING: only differs from us by the jal target address of func_15168B10
// (not yet confirmed byte-matching itself) - this function's own code is verified
// byte-identical otherwise.
void func_15168A2C(s32 arg0) {
    func_15168B10(arg0, 0);
}
void func_15168A4C(void *arg0, u8 arg1) {
    void **slot;
    void *next;

    slot = (void **) (D_800DCE50 + (*((u8 *) arg0 + 1) * 0x1A0) + (arg1 * 4));
    next = *slot;
    *(void **) ((u8 *) arg0 + 8) = next;
    if (next != NULL) {
        *(void **) ((u8 *) next + 4) = arg0;
    }
    *((u8 *) arg0) = arg1;
    *(void **) ((u8 *) arg0 + 4) = NULL;
    *slot = arg0;
}

void func_15168A9C(void *arg0) {
    void **slot;
    void *next;
    void *prev;

    slot = (void **) (D_800DCE50 + (*((u8 *) arg0 + 1) * 0x1A0) + (*((u8 *) arg0) * 4));
    if (arg0 == *slot) {
        *slot = *(void **) ((u8 *) arg0 + 8);
    }
    next = *(void **) ((u8 *) arg0 + 8);
    if (next != NULL) {
        *(void **) ((u8 *) next + 4) = *(void **) ((u8 *) arg0 + 4);
    }
    prev = *(void **) ((u8 *) arg0 + 4);
    if (prev != NULL) {
        *(void **) ((u8 *) prev + 8) = *(void **) ((u8 *) arg0 + 8);
    }
}


void func_15168B10(s32 arg0, s32 arg1) {
    func_15168A9C(arg0);
    func_15168A4C(arg0, arg1);
}

void func_15168B44(void *arg0) {
    s32 *packed = (s32 *) ((u8 *) arg0 + 0x14);
    s32 value = *packed;
    u16 count = value;

    if (count != 0) {
        *packed = (value & 0xFFFF0000) | ((count - 1) & 0xFFFF);
        *(s16 *) ((u8 *) arg0 + 0x38) = 0x1E;
        return;
    }

    count = value >> 16;
    if (count < *((u8 *) arg0 + 0x3F)) {
        *((u8 *) arg0 + 0x3F) -= count;
        *(s16 *) ((u8 *) arg0 + 0x38) = 0x1E;
    } else {
        *(s16 *) ((u8 *) arg0 + 0x38) = 0;
    }
}

void func_15168BAC(void *arg0) {
    u8 idx = *((u8 *) arg0 + 0xE4);

    if (idx != 0) {
        D_8008CA20[idx](arg0);
    }
}

void func_15168BE4(void *arg0, u8 arg1, s32 arg2) {
    void *tmp;

    if (*(s32 *) ((u8 *) arg0 + 0x40) != 0) {
        tmp = func_15167A68(0x10, arg2, 0xF0, 1, arg1, 1);
        if (tmp != NULL) {
            bcopy(arg0, (u8 *) tmp + 0x90, 0x60);
        }
    }
}

/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168C4C.s. */
s32 func_15168C4C() {
    return 0;
}
void func_15168E34(s32 *arg0, s32 arg1) {
    if ((*arg0 & 0xF000000) == 0) {
        *arg0 += arg1;
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168E54.s. */
s32 func_15168E54() {
    return 0;
}
void func_15168F08(u8 *arg0, s32 arg1) {
    u8 *cur;

    for (cur = arg0; cur[0] != 0xDF; cur += 8) {
        if ((cur[0] == 1) || ((cur[0] == 0xDC) && (cur[3] == 0xE))) {
            *(s32 *)(cur + 4) = (*(s32 *)(cur + 4) & 0xFFFFFF) + arg1;
        }
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168F84.s. */
s32 func_15168F84() {
    return 0;
}
// NON-MATCHING: only differs from us by the jal target address of the still-non-matching
// func_15169070 - this function's own code is verified byte-identical otherwise.
void func_15169040(s32 arg0, u8 arg1) {
    func_15169070(0, 0x68, arg0, arg1);
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_15169070(s32 arg0, s32 arg1, s32 arg2, u8 arg3) {
    u8 pad[16]; // Load-bearing stack padding: matches retail's 0x58-byte frame.
    s32 col;
    u8 *row;
    u8 *slot;
    struct115 *cur;
    void *node;

    func_15143D18(&arg0, &arg1, 2, 0x68);
    if (arg0 < arg1) {
        col = arg0 * 4;
        cur = &D_8008B4A8[arg0];
        do {
            row = D_800DCE50;
            slot = D_800DCE50 + col;
            do {
                if (cur->unk1C != NULL) {
                    node = *(void **) slot;
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = *(void **) ((u8 *) node + 8);
                            func_1516968C(node, arg2, arg3);
                            cur->unk1C(node, arg2, arg3);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                } else {
                    node = *(void **) slot;
                    D_800DD190++;
                    if (node != NULL) {
                        do {
                            D_800DD198[D_800DD190] = *(void **) ((u8 *) node + 8);
                            func_1516968C(node, arg2, arg3);
                            node = D_800DD198[D_800DD190];
                        } while (node != NULL);
                    }
                    D_800DD190--;
                }
                row += 0x1A0;
                slot += 0x1A0;
            } while (row != (u8 *) &D_800DD190);
            col += 4;
            cur += 1;
        } while (col < arg1 * 4);
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15169260.s. */
void func_15169260(s32 arg0, s32 arg1, s32 arg2, u8 arg3) {
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_1516944C.s. */
void func_1516944C(s32 arg0, s32 arg1, u8 arg2) {
}

void func_151695F0(void *arg0, u8 arg1) {
    struct {
        void *ptr;
        u8 tag;
    } tmp;

    tmp.ptr = arg0;
    tmp.tag = ((u8 *) arg0)[0x3B];
    func_15169040((s32) &tmp, arg1);
}

void func_1516962C(s32 arg0, void *arg1, u8 arg2) {
    struct {
        void *ptr;
        u8 tag;
    } tmp;

    tmp.ptr = arg1;
    tmp.tag = ((u8 *) arg1)[0x3B];
    func_1516944C(arg0, (s32) &tmp, arg2);
}

s32 func_15169668(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    D_800D2DAB = 1;
    return arg0;
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
// NON-MATCHING (logic verified, 2 words left): only the two lbu operands of
// the equality are swapped - retail loads *arg1 before arg0->unkC; cfe
// canonicalizes the comparison so both source operand orders emit the
// a0-based load first. The u8 arg2 prologue and lbu unkC (struct102.unkC
// split to u8) already match retail exactly. Tried guarded one-local and
// two-local byte loads; both force source load order but allocate v0/v1 and
// increase the diff count.
void func_1516968C(struct102 *arg0, u8 *arg1, u8 arg2) {
    if (((arg2 == 0xF) || (arg2 == 0x10)) && (*arg1 == arg0->unkC)) {
        func_1516972C(arg0);
    }
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
// NON-MATCHING (logic verified, 2 words left): indexed array form keeps arg0
// in a0 and slot in a1 like retail. Remaining difference is only the scheduling
// of `i = 0` vs `slots = D_800DD198` around the positive-count branch.
// Tried (2026-07-16): moving `i = 0` after slots and between count/slots -
// both reorders regress to 11 diffs (register allocation flips); the
// delay-slot choice is a scheduler coin-flip, not source order.
void func_151696DC(void *arg0) {
    s8 i;
    s8 count;
    void **slots;

    i = 0;
    count = D_800DD190;
    slots = D_800DD198;
    if (count > 0) {
        do {
            if (arg0 == slots[i]) {
                slots[i] = *(void **) ((u8 *) arg0 + 8);
            }
            i++;
        } while (i < count);
    }
}

void func_1516972C(struct102 *arg0) {
    void (*func)(struct102 *arg0);
    func_151696DC(arg0);

    if (arg0->unk0 >= 2) {
        func = D_8008B4D0[arg0->unk0].unk0;
        if (func != NULL) {
            func(arg0);
            return;
        }
        func_15169804(arg0);
    }
}

void func_1516979C(struct102 *arg0) {
    void (*func)(struct102 *arg0);

    func_151696DC(arg0);
    func = D_8008B4D4[arg0->unk0].unk0;
    if (func != NULL) {
        func(arg0);
        return;
    }
    func_15169824(arg0);
}

void func_15169804(struct102 *arg0) {
    func_15168B10(arg0, 1);
}

void func_15169824(struct102 *arg0) {
    func_15168A9C(arg0);
    func_10004074(arg0);
}

/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15169850.s. */
void func_15169850(s32 arg0, u8 arg1, s32 arg2, s32 arg3, s32 arg4) {
}
