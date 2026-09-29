#include <ultra64.h>
extern u8 D_800C3E78;

typedef struct LookupNode15155FD4 {
    u8 pad0[8];
    struct LookupNode15155FD4 *next;
    u8 padC[4];
    u8 key;
} LookupNode15155FD4;

typedef struct {
    u8 pad0[0x140];
    LookupNode15155FD4 *head;
    u8 pad144[0x5C];
} LookupOwner15155FD4;

extern LookupOwner15155FD4 D_800DCE50[];
extern LookupOwner15155FD4 D_800DD190[];

/* Non-matching placeholders for the text-only asm slice asm/182C30.s. */

s32 func_15155FD4(s32 key);

s32 func_15155780() {
    return 0;
}

s32 func_151557FC() {
    return 0;
}

s32 func_1515589C() {
    return 0;
}

s32 func_15155CFC() {
    return 0;
}

void func_15155EF8(u8 *arg0) {
    u8 *temp_a2 = *(u8 **) (arg0 + 0x14);

    if (temp_a2 != 0) {
        func_1515F10C(temp_a2);
    }
    func_15169804(arg0);
    func_1518CA04(0xA6);
}

void func_15155F3C(void) {
    u8 *temp_v0 = (u8 *) func_15155FD4(D_800C3E78);

    if (temp_v0 != NULL) {
        u8 state = *(temp_v0 + 0x11);

        if (state == 2) {
            *(temp_v0 + 0x11) = 0;
        } else if (state == 3) {
            *(temp_v0 + 0x11) = 2;
        }
    }
}

void func_15155F90(void) {
    u8 *temp_v0 = (u8 *) func_15155FD4(D_800C3E78);

    if (temp_v0 != 0) {
        if (*(temp_v0 + 0x11) == 3) {
            *(temp_v0 + 0x11) = 1;
        }
    }
}

s32 func_15155FD4(s32 key) {
    LookupOwner15155FD4 *owner = D_800DCE50;
    LookupNode15155FD4 *node;

    do {
        node = owner->head;
        owner++;
        while (node != NULL) {
            if (node->key == key) {
                return (s32)node;
            }
            node = node->next;
        }
    } while (owner != D_800DD190);

    return 0;
}

s32 func_15156028() {
    return 0;
}
