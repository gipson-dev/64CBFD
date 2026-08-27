#include <ultra64.h>
extern u16 D_800BE598[];
extern u8 D_800BE590;
extern u8 D_800CC2D0[];
extern u8 D_800BE616;
extern s32 D_800BE9F0;
extern u8 D_800D2100;
extern u8 D_800D2101;
extern s32 func_1507DF10();
extern s32 func_150ADA20();
s32 func_150843AC();

/* Non-matching placeholders for the text-only asm slice asm/AEB40.s. */

s32 func_15081690() {
    return 0;
}

s32 func_15081C20() {
    return 0;
}

s32 func_15081E0C(u8 *arg0, u16 arg1, u8 arg2) {
    if (D_800BE616 != 0) {
        return;
    }
    if (arg0[0x1CA] != 0) {
        arg0[0x1CA] = 7;
    }
    if ((arg2 == 0) || (arg1 != 0xA)) {
        func_1507DF10(arg0, arg1);
    }
}

s32 func_15081E78() {
    return 0;
}

s32 func_150825C0() {
    return 0;
}

s32 func_1508295C(s32 arg0, u8 *arg1, s32 arg2) {
    s32 start;
    s32 i;
    s32 end;

    if (arg2 != 0) {
        start = 0;
        end = D_800D2101;
    } else {
        start = D_800D2101;
        end = D_800D2100;
    }

    if (start < end) {
        i = start;
        do {
            func_150825C0(i, arg1);
            i++;
        } while (i != end);
    }
}

s32 func_150829D8(u8 *arg0) {
    return 0;
}

s32 func_15082A44() {
    return 0;
}

s32 func_150832AC() {
    return 0;
}

s32 func_15083384() {
    return 0;
}

s32 func_15083568() {
    return 0;
}

s32 func_150836CC() {
    return 0;
}

s32 func_150837D4() {
    return 0;
}

s32 func_150838EC() {
    return 0;
}

s32 func_150839B8() {
    return 0;
}

s32 func_15083AC8() {
    return 0;
}

s32 func_15083DA0() {
    return 0;
}

s32 func_15083E0C() {
    return 0;
}

s32 func_15083E90() {
    return 0;
}

s32 func_15083FB0(u8 arg0) {
    s32 temp_v0 = func_15083E90(arg0);

    if (temp_v0 != 0) {
        return (temp_v0 - (s32) D_800CC2D0) / 0x32C;
    }
    return -1;
}

s32 func_15084000(void) {
    s32 temp_v0 = func_1505EEF4();

    if (temp_v0 != 0) {
        return (temp_v0 - (s32) D_800CC2D0) / 0x32C;
    }
    return -1;
}

s32 func_15084044() {
    return 0;
}

s32 func_1508434C(u8 *arg0) {
    return 0;
}

s32 func_150843AC() {
    return 0;
}

s32 func_15084488() {
    return 0;
}

s32 func_15084558() {
    return 0;
}

s32 func_150849A0(u8 *arg0) {
    s32 temp_v1 = arg0[0x1C9];

    if (temp_v1 != 0) {
        return (*(u8 **) (arg0 + 0x2C4))[temp_v1 - 1];
    }
    return **(u8 **) (arg0 + 0x2C4);
}

s32 func_150849CC(u8 *arg0, s32 *arg1) {
    return 0;
}

s32 func_15084A18() {
    return 0;
}

s32 func_15084C30(u8 *arg0) {
    return 0;
}

s32 func_15084CB0(s32 arg0) {
    s32 count = D_800BE590;
    s32 found = 0;
    s32 i = 0;

    if (count > 0) {
        u16 *ptr = D_800BE598;

        do {
            if (arg0 == *ptr) {
                found = i;
                break;
            }
            i += 1;
            ptr += 1;
        } while (i < count);
    }
    return found;
}
