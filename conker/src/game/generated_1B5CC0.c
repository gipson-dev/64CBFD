#include <ultra64.h>
extern u8 *D_800DF7C8;

/* Non-matching placeholders for the text-only asm slice asm/1B5CC0.s. */

s32 func_15188810() {
    return 0;
}

s32 func_1518894C() {
    return 0;
}

typedef struct ListNode15188A58 ListNode15188A58;

struct ListNode15188A58 {
    u8 pad0[0xC];
    ListNode15188A58 *next;
};

void func_15188A58(ListNode15188A58 *arg0, ListNode15188A58 *arg1) {
    ListNode15188A58 *temp_v0;
    ListNode15188A58 *temp_v1;

    arg0->next = 0;
    temp_v0 = *(ListNode15188A58 **)arg1;
    if (temp_v0 == 0) {
        *(ListNode15188A58 **)arg1 = arg0;
    } else {
        arg1 = temp_v0->next;
        temp_v1 = temp_v0;
        if (arg1 != 0) {
            do {
                temp_v1 = arg1;
                arg1 = arg1->next;
            } while (arg1 != 0);
        }
        temp_v1->next = arg0;
    }
}

void func_15188A9C(s32 arg0) {
    u8 *ptr = D_800DF7C8;

    if (ptr != 0) {
        do {
            if (arg0 == *(s32 *) (ptr + 0x10)) {
                *(u16 *) (ptr + 6) = 0;
            }
            ptr = *(u8 **) (ptr + 0xC);
        } while (ptr != 0);
    }
}

s32 func_15188AD0() {
    return 0;
}

s32 func_15188B74() {
    return 0;
}

s32 func_15188D00() {
    return 0;
}

s32 func_15188E48() {
    return 0;
}

s32 func_15188F84() {
    return 0;
}

s32 func_15189118() {
    return 0;
}

s32 func_151895A4(u8 *arg0) {
    u8 *temp_a2 = arg0;

    func_100043B4(*(s32 *)(temp_a2 + 8), 2);
}

s32 func_151895CC(u8 *arg0) {
    u8 *temp_a2 = arg0;

    func_100043B4(*(s32 *)(temp_a2 + 8), 2);
}

s32 func_151895F4() {
    return 0;
}

s32 func_151897A4() {
    return 0;
}

void func_151898C0(s32 arg0, s32 arg1) {
    u8 *ptr = D_800DF7C8;

    if (ptr != 0) {
        do {
            if (arg0 == *(s32 *) (ptr + 0x10)) {
                *(s32 *) (ptr + 0x14) = arg1;
                return;
            }
            ptr = *(u8 **) (ptr + 0xC);
        } while (ptr != 0);
    }
}
