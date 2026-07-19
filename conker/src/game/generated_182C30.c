#include <ultra64.h>
extern u8 D_800C3E78;

/* Non-matching placeholders for the text-only asm slice asm/182C30.s. */

s32 func_15155FD4();

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

s32 func_15155F3C() {
    return 0;
}

void func_15155F90(void) {
    u8 *temp_v0 = (u8 *) func_15155FD4(D_800C3E78);

    if (temp_v0 != 0) {
        if (*(temp_v0 + 0x11) == 3) {
            *(temp_v0 + 0x11) = 1;
        }
    }
}

s32 func_15155FD4() {
    return 0;
}

s32 func_15156028() {
    return 0;
}
