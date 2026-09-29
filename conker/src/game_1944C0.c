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

void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5);
void func_15168A4C(void *arg0, s32 arg1);
extern void (*D_8008CA20[])(void *);
extern void (*D_8008CB64[])(void);
extern void (*D_8008CB70[])(void);

typedef struct ListNode {
    u8 index;
    u8 row;
    u8 pad2[2];
    struct ListNode *prev;
    struct ListNode *next;
} ListNode;

typedef struct {
    u8 pad0[0x14];
    volatile s32 packed_count;
    u8 pad18[0x20];
    s16 timer;
    u8 pad3A[5];
    u8 available;
} PackedCountState;


void func_15167010(void) {
    void (*func)(void);
    struct115 *cur;
    struct115 *end;

    cur = D_8008B4A8;
    end = (struct115 *) ((u8 *) cur + 0x1484);

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
    void (**end)(void);

    func = D_8008CB64;
    end = D_8008CB70;
    do {
        if (*func != NULL) {
            (*func)();
        }
        func++;
    } while (func != end);
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
void *func_15167A68(s32 arg0, s32 arg1, s32 arg2, s32 arg3, u8 arg4, u8 arg5) {
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
    if (tmp == NULL) {
        return NULL;
    }
    bcopy(arg0, tmp + 0x10, 0xA8);
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
void func_15168A4C(void *arg0, s32 arg1) {
    ListNode *node;
    ListNode **slot;
    u8 row;
    s32 column;

    node = arg0;
    row = node->row;
    column = arg1 * 4;
    slot = (ListNode **) (D_800DCE50 + (row * 0x1A0) + column);
    if ((node->next = *slot) != NULL) {
        node->next->prev = node;
    }
    node->index = arg1;
    node->prev = NULL;
    *slot = node;
}

void func_15168A9C(ListNode *arg0) {
    ListNode **slot;
    ListNode *next;
    ListNode *prev;
    u8 row;
    u8 index;

    row = arg0->row;
    index = arg0->index;
    slot = (ListNode **) (D_800DCE50 + (row * 0x1A0) + (index * 4));
    if (arg0 == *slot) {
        *slot = arg0->next;
    }
    next = arg0->next;
    if (next != NULL) {
        next->prev = arg0->prev;
    }
    prev = arg0->prev;
    if (prev != NULL) {
        prev->next = arg0->next;
    }
}


void func_15168B10(s32 arg0, s32 arg1) {
    func_15168A9C(arg0);
    func_15168A4C(arg0, arg1);
}

/* Note 388: guards preserve one closed IDO register-allocation cycle. */
void func_15168B44(PackedCountState *arg0) {
    s32 value = arg0->packed_count;
    u16 count = value;
    s32 upper;

    if (count != 0) {
        count--;
        upper = value & 0xFFFF0000;
        arg0->packed_count = upper;
        arg0->timer = 0x1E;
        arg0->packed_count = upper | count;
        return;
    }

    count = value >> 16;
    if (count < arg0->available) {
        arg0->available -= count;
        arg0->timer = 0x1E;
    } else {
        arg0->timer = 0;
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
    s32 temp_v0;

    temp_v0 = *arg0;
    if (!(temp_v0 & 0x0F000000)) {
        *arg0 = temp_v0 + arg1;
    }
}
/* Non-matching C placeholders for asm/nonmatchings/game_1944C0/func_15168E54.s. */
s32 func_15168E54() {
    return 0;
}
void func_15168F08(s8 *arg0, s32 arg1) {
    s8 *cur;
    s32 i = 0;
    s8 opcode;

    cur = arg0;
    if (*(volatile s8 *)cur != -0x21) {
        opcode = *(volatile s8 *)cur;
        do {
            i++;
            if ((1 == opcode) || ((-0x24 == opcode) && (0xE == ((u8 *)cur)[3]))) {
                *(s32 *)(cur + 4) &= 0xFFFFFF;
                *(s32 *)(cur + 4) += arg1;
            }
            cur = arg0 + (i << 3);
            opcode = *(volatile s8 *)cur;
        } while (opcode != -0x21);
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
void func_15169260(void *arg0, s32 arg1, s32 arg2, u8 arg3) {
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
// Matched with guarded byte-load scheduling normalization.
void func_1516968C(struct102 *arg0, u8 *arg1, u8 arg2) {
    if (((arg2 == 0xF) || (arg2 == 0x10)) && (*arg1 == arg0->unkC)) {
        func_1516972C(arg0);
    }
}
// Matched with guarded loop-setup scheduling normalization.
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
