#include <ultra64.h>
extern u8 *D_800C3EE0;
extern u8 D_800C35EA;
extern s32 D_800BE9E4;
extern s32 D_800902BC[];
extern s32 D_800902FC[];

/* Non-matching placeholders for the text-only asm slice asm/5D2C0.s. */

s32 func_1503195C();

s32 func_15030310();

s32 func_1502FE10() {
    return 0;
}

s32 func_1502FFD8() {
    return 0;
}

s32 func_15030158() {
    return 0;
}

void func_150302F0(register s32 arg0, register s32 arg1) {
    func_15030310(arg0, arg1, 0xFF);
}

s32 func_15030310() {
    return 0;
}

s32 func_150303E4(u8 *arg0) {
    u8 *temp_v0;
    s32 result = 0;

    if (arg0[0x3B] != 0) {
        temp_v0 = D_800C3EE0;
        if (temp_v0 != 0) {
            do {
                if (arg0[0x3B] == temp_v0[0]) {
                    func_15030158(temp_v0, 0);
                    result = 1;
                }
                temp_v0 = *(u8 **) (temp_v0 + 0x54);
            } while (temp_v0 != 0);
        }
    }
    return result;
}

s32 func_15030468() {
    return 0;
}

s32 func_15030AF4() {
    return 0;
}

s32 func_15030D54() {
    return 0;
}

s32 func_15030E08() {
    return 0;
}

s32 func_15030F94() {
    return 0;
}

s32 func_15031070() {
    return 0;
}

s32 func_150311C4() {
    return 0;
}

void func_1503192C(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    u8 *temp_v0 = (u8 *) func_1503195C(arg0, arg1, arg3);

    if (temp_v0 != 0) {
        temp_v0[3] = arg2;
    }
}

s32 func_1503195C(u8 *arg0, s32 arg1, s32 arg2) {
    u8 *node;
    u8 type;

    type = arg0[0x3B];
    if (type == 0) {
        return 0;
    }
    node = D_800C3EE0;
    if (node == 0) {
        return 0;
    }
    do {
        if (type == node[0]) {
            if (arg1 == node[6]) {
                if (arg2 == 0) {
                    return (s32) node;
                }
                arg2 = arg2 - 1;
            }
        }
        node = *(u8 **) (node + 0x54);
    } while (node != 0);
    return 0;
}

s32 func_150319CC(s32 arg0, u8 *arg1) {
    u8 *node;

    if (arg1 != 0) {
        node = D_800C3EE0;
        if (node != 0) {
            u8 type = arg1[0x3B];

            do {
                if (type == node[0]) {
                    if (arg0 == node[6]) {
                        return (s32) node;
                    }
                }
                node = *(u8 **) (node + 0x54);
            } while (node != 0);
        }
    }
    node = D_800C3EE0;
    if (node != 0) {
        do {
            if (arg0 == node[6]) {
                return (s32) node;
            }
            node = *(u8 **) (node + 0x54);
        } while (node != 0);
    }
    return 0;
}

s32 func_15031A50() {
    return 0;
}

s32 func_15031C14() {
    return 0;
}

s32 func_15031E2C(u8 *arg0, s32 arg1) {
    s32 temp_v1 = *(s32 *) (arg0 + 0x38);
    s32 idx = temp_v1;
    s32 val;

    if (idx >= 3) {
        idx = 5 - idx;
    }
    val = D_800902BC[idx];
    temp_v1 = temp_v1 + 1;
    *(s32 *) (arg0 + 0x38) = temp_v1;
    *(s16 *) (arg0 + 0x18) = val;
    if (temp_v1 >= 6) {
        *(s32 *) (arg0 + 0x38) = 0;
    }
    return 0;
}

s32 func_15031E7C() {
    return 0;
}

s32 func_15031FC8() {
    return 0;
}

s32 func_150331B8() {
    return 0;
}

s32 func_1503327C() {
    return 0;
}

s32 func_15033328(u8 *arg0, u8 *arg1) {
    return 0;
}

s32 func_150333A8() {
    return 0;
}

s32 func_15033440(u8 *arg0, u8 *arg1) {
    return 0;
}

s32 func_150334B8() {
    return 0;
}

s32 func_150335C8() {
    return 0;
}

s32 func_1503378C(u8 *arg0, u8 *arg1) {
    return 0;
}

s32 func_150337E4(u8 *arg0, s32 arg1) {
    s32 temp_v0 = *(s32 *) (arg0 + 0x38) + D_800BE9E4;
    s32 idx;

    *(s32 *) (arg0 + 0x38) = temp_v0;
    if (temp_v0 >= 0x10) {
        *(s32 *) (arg0 + 0x38) = 0;
        *(s32 *) (arg0 + 0x3C) = *(s32 *) (arg0 + 0x3C) ^ 1;
    }
    idx = *(s32 *) (arg0 + 0x3C);
    *(s16 *) (arg0 + 0x18) = D_800902FC[idx];
    return 0;
}

s32 func_15033838() {
    return 0;
}

s32 func_150339C8() {
    return 0;
}

s32 func_15033AD8() {
    return 0;
}

s32 func_15033BDC() {
    return 0;
}

s32 func_15033E00(s32 arg0, u8 *arg1) {
    if (arg1[5] == 3) {
        return 1;
    }
    return 0;
}

s32 func_15033E28(u8 *arg0, u8 **arg1) {
    u8 *node = D_800C3EE0;
    s32 count = 0;

    if (node != 0) {
        do {
            if (arg0[0x3B] == node[0]) {
                arg1[count] = node;
                count = count + 1;
            }
            node = *(u8 **) (node + 0x54);
        } while (node != 0);
    }
    return count;
}

s32 func_15033E84(u8 *arg0) {
    u8 *node = D_800C3EE0;

    if (node != 0) {
        u8 type = arg0[0x3B];

        do {
            if (type == node[0]) {
                return (s32) node;
            }
            node = *(u8 **) (node + 0x54);
        } while (node != 0);
    }
    return 0;
}

s32 func_15033EC4(s32 arg0, s32 arg1) {
    return 0;
}

s32 func_15033F0C(u8 *arg0, u8 *arg1) {
    u8 *ptr;

    if (D_800C35EA == 1) {
        return 0;
    }
    ptr = *(u8 **) (arg1 + 0x31C);
    if (ptr != 0) {
        if (ptr[0x78] != 9) {
            if (ptr[0x11A] != 3) {
                ptr[0x11A] = 0;
                return 1;
            }
        }
    }
    return 0;
}

s32 func_15033F70(u8 *arg0, u8 *arg1) {
    return 0;
}
