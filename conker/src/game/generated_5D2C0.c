#include <ultra64.h>
typedef struct {
    u8 *actor;
    u8 group;
} NodeCleanupPacket;
u8 *func_15083E90(s32);
s32 func_15033BDC();
void func_1000FD38(s32 (*)(), u8 *, u8 *);
void func_15100180(u8 *);
void func_151616D0(s32, s32, NodeCleanupPacket *);
void func_15147D64(NodeCleanupPacket *, s32);
void func_151494E0(NodeCleanupPacket *, s32);
void func_151BD7F4(u8 *);
void func_151D4668(u8 *);
void func_151D747C(u8 *);
void func_151027E8(u8 *);
void func_151001B4(u8 *);
void func_15163BE8(u8 *, s32, s32);
void func_150D3360(u8 *, s32, s32);
void func_150D5440(u8 *, s32, s32);
void func_151BD828(u8 *, s32, s32);
void func_151D74B0(u8 *, s32, s32, s32, s32);
s32 func_150859AC(s32, s32);
extern s32 D_80090228;
extern s32 D_8009022C;
void func_1503F5B8(u8 *, s32, s32, f32, f32, s32);
extern u8 D_800BE9C0;
extern u8 *D_800C3EE0;
extern u8 D_800C35EA;
extern s32 D_800BE9E4;
extern s32 D_800902BC[];
extern s32 D_800902FC[];
extern f32 D_80097B68;

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
    u8 *current;
    u8 *next;
    s32 result;

    if (arg0[0x3B] == 0) {
        return 0;
    }

    current = D_800C3EE0;
    result = 0;
    if (current != 0) {
        do {
            next = *(u8 **) (current + 0x54);
            if (arg0[0x3B] == current[0]) {
                func_15030158(current, 0);
                result = 1;
            }
            current = next;
        } while (current != 0);
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

/* Complete non-matching recovery; byte-match boundary in Working Note 1107. */
s32 func_15031070(u8 *node, u8 *actor, Mtx **primary, Mtx **secondary) {
    u8 *attachment;
    u8 *parent;

    attachment = *(u8 **)(node + 0x48);
    if (attachment != 0) {
        if (attachment[0x3F6] == 0) {
            return 0;
        }
        *primary = ((Mtx **)(attachment + 0x3E8))[D_800BE9C0];
        *secondary = ((Mtx **)(*(u8 **)(node + 0x48) + 0x3E0))[D_800BE9C0];
    } else if (*(u8 **)(node + 0x34) != 0) {
        *primary = *(Mtx **)(node + 0x34) + D_800BE9C0;
        *secondary = node[2] + *(Mtx **)(actor + 0x1D4);
    } else if (*(u16 *)(node + 0x1E) != 0) {
        parent = (u8 *)func_1503195C(actor, *(u16 *)(node + 0x1E), 0);
        if (parent == 0) {
            return 0;
        }
        if (func_15031070(parent, actor, primary, secondary) == 0) {
            return 0;
        }
        *primary += *(u16 *)(node + 0x20);
        return 1;
    } else {
        *primary = *(Mtx **)(actor + 0x1D4);
        *primary += node[2];
        *secondary = *primary;
    }
    return 1;
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

s32 func_1503195C(u8 *actor, s32 key, u32 ordinal) {
    u32 group = actor[0x3B];
    u8 *current;
    u8 *next;

    if (group == 0) {
        return 0;
    }
    current = D_800C3EE0;
    if (current != 0) {
        do {
            next = *(u8 **)(current + 0x54);
            if (group == current[0] && key == current[6]) {
                if (ordinal != 0) {
                    ordinal--;
                } else {
                    return (s32)current;
                }
                current = next;
            } else {
                current = next;
            }
        } while (current != 0);
    }
    return 0;
}

s32 func_150319CC(s32 arg0, u8 *arg1) {
    u8 *node;
    u8 *next;

    if (arg1 != 0) {
        node = D_800C3EE0;
        if (node != 0) {
            u8 type = arg1[0x3B];

            do {
                next = *(u8 **) (node + 0x54);
                if (type == node[0]) {
                    if (arg0 == node[6]) {
                        return (s32) node;
                    }
                }
                node = next;
            } while (next != 0);
        }
    }
    node = D_800C3EE0;
    if (node != 0) {
        do {
            next = *(u8 **) (node + 0x54);
            if (arg0 == node[6]) {
                return (s32) node;
            }
            node = next;
        } while (next != 0);
    }
    return 0;
}

void func_15031A50(u8 *node, u8 *actor) {
    u8 *state;

    switch (node[1]) {
        case 0x37:
            func_151001B4(actor);
            break;
        case 0x5A:
            state = *(u8 **)(actor + 0x31C);
            if (state != 0) {
                *(u16 *)(state + 0x1A6) += 0xAA;
            }
            break;
        case 0x90:
            *(u32 *)(actor + 0x9C) |= 0x70;
            break;
        case 0x8F:
            *(u32 *)(actor + 0x9C) |= 0xE00;
            break;
        case 0x49:
            func_15163BE8(actor, 0xFF, 1);
            break;
        case 0x5D:
            func_150D3360(actor, 0xFF, 1);
            func_150D5440(actor, 0xFF, 1);
            break;
        case 0x3D:
            func_151BD828(actor, 0xFF, 1);
            break;
        case 0x1D:
            func_151D74B0(actor, 0, 2, 0xFF, 1);
            break;
        case 0x85:
        case 0x5E:
            *(u32 *)(actor + 0x9C) |= 0x6000;
            break;
        case 0x8D:
            if (func_150859AC(0, 6) < 100) {
                *(s16 *)(node + 0x18) = D_80090228;
            } else {
                *(s16 *)(node + 0x18) = D_8009022C;
            }
            break;
        case 0x82:
            func_151D74B0(actor, 6, -1, 0xFF, 1);
            break;
    }
}

void func_15031C14(u8 *node) {
    u8 *actor;
    NodeCleanupPacket first;
    NodeCleanupPacket second;
    u8 *state;
    /* Preserve the retail private pointer home across the paired callbacks. */
    NodeCleanupPacket *volatile packet;

    actor = func_15083E90(node[0]);
    if (actor == 0) {
        return;
    }
    switch (node[1]) {
        case 0x5A:
            state = *(u8 **)(actor + 0x31C);
            if (state != 0) {
                *(u16 *)(state + 0x1A6) -= 0xAA;
            }
            break;
        case 0x90:
            *(u32 *)(actor + 0x9C) &= ~0x70;
            break;
        case 0x8F:
            *(u32 *)(actor + 0x9C) &= ~0xE00;
            break;
        case 0x37:
        case 0x4B:
        case 0x4C:
            func_1000FD38(func_15033BDC, node, actor);
            if (node[1] == 0x37) {
                func_15100180(actor);
            }
            break;
        case 0x49:
            first.actor = actor;
            first.group = actor[0x3B];
            func_151616D0(0x10, 0x29, &first);
            break;
        case 0x5D:
            second.actor = actor;
            second.group = actor[0x3B];
            packet = &second;
            func_15147D64(&second, 0x2E);
            func_151494E0(packet, 0x2F);
            break;
        case 0x3D:
            func_151BD7F4(actor);
            break;
        case 0x1A:
        case 0x1B:
        case 0x5F:
        case 0x65:
        case 0x66:
            func_151D4668(actor);
            break;
        case 0x1D:
        case 0x82:
            func_151D747C(actor);
            break;
        case 0x85:
        case 0x5E:
            *(u32 *)(actor + 0x9C) &= ~0x6000;
            break;
    }
    switch (node[6]) {
        case 0x16:
        case 0x63:
        case 0x89:
            func_151027E8(actor);
            func_151D4668(actor);
    }
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

s32 func_150331B8(u8 *node, u8 *actor) {
    u8 *source;
    u8 *attachment;
    s32 index;

    source = *(u8 **)(actor + 0x2D0);
    attachment = *(u8 **)(node + 0x48);
    if (attachment == 0) {
        return 0;
    }
    index = *(s32 *)(actor + 0x2E4) & 0xFF;
    if (index != 0xFF) {
        func_1503F5B8(attachment, 0, index, 1.0f, 0.0f, 1);
    }
    if (source != 0) {
        *(f32 *)(*(u8 **)(node + 0x48) + 8) = *(f32 *)(source + 8);
        attachment = *(u8 **)(node + 0x48);
        if (*(f32 *)(attachment + 0x18) <= *(f32 *)(attachment + 8)) {
            *(f32 *)(attachment + 8) = *(f32 *)(attachment + 0x18) - 1.0f;
        }
    }
    return 0;
}

s32 func_1503327C(u8 *node, u8 *actor) {
    u8 *attachment;

    attachment = *(u8 **)(node + 0x48);
    if (attachment == 0) {
        return 0;
    }
    if ((*(u16 *)(attachment + 4) & 0x8000) != 0x8000) {
        func_1503F5B8(attachment, 0, 0, 1.0f, 0.0f, 1);
        attachment = *(u8 **)(node + 0x48);
    }
    if (*(f32 *)(attachment + 0x18) - 1.0f <= *(f32 *)(attachment + 8)) {
        return 1;
    }
    return 0;
}

s32 func_15033328(u8 *arg0, u8 *arg1) {
    s32 result = 0;

    /* Retail swimming-attachment lifetime callback (15033328..150333A7). */
    if (D_800C35EA == 1) {
        return result;
    }
    if (arg1[0xAD] == 0 && *(f32 *)(arg1 + 0x118) < *(f32 *)(arg1 + 0x180)) {
        if (D_800BE9E4 < *(s32 *)(arg0 + 0x38)) {
            *(s32 *)(arg0 + 0x38) -= D_800BE9E4;
            return result;
        } else {
            return 1;
        }
    } else {
        *(s32 *)(arg0 + 0x38) = 30;
    }
    return result;
}

s32 func_150333A8(u8 *arg0, u8 *arg1) {
    u8 *attached;
    f32 reference;

    if (D_800C35EA == 1) {
        return 0;
    }

    if (arg1[0xAD] != 0) {
        attached = *(u8 **)(arg1 + 0x31C);
        if (attached != NULL) {
            attached[0x11A] = 0;
        }
        return 1;
    }

    reference = *(f32 *)(arg1 + 0x118);
    if ((reference == D_80097B68) ||
        !(*(f32 *)(arg1 + 0x18) < reference + 300.0f)) {
        arg0[3] = 0xFF;
    } else {
        arg0[3] = 0;
    }
    return 0;
}

s32 func_15033440(u8 *arg0, u8 *arg1) {
    switch (arg0[1]) {
        case 0x27:
        case 0x35:
            if (arg1[5] == 5) {
                arg0[2] = 0;
                *(s16 *) (arg0 + 0x22) += D_800BE9E4 * 0xAAA;
            }
            break;
        case 0x29:
            if (arg1[5] == 5) {
                arg0[2] = 0;
            }
            break;
    }
    return 0;
}

s32 func_150334B8() {
    return 0;
}

s32 func_150335C8() {
    return 0;
}

s32 func_1503378C(u8 *arg0, u8 *arg1) {
    u16 temp_v0 = *(u16 *)(arg1 + 0x84);

    if (arg0[1] == 0x11) {
        if ((temp_v0 == 0x3E) || (temp_v0 == 0x3D) ||
                (temp_v0 == 0x41) || (temp_v0 == 0xD9) ||
                (temp_v0 == 0x138) || (temp_v0 == 0x139)) {
            return 0;
        }
    }
    return 1;
}

s32 func_150337E4(u8 *arg0, s32 arg1) {
    *(s32 *) (arg0 + 0x38) += D_800BE9E4;
    if (*(s32 *) (arg0 + 0x38) >= 0x10) {
        *(s32 *) (arg0 + 0x38) = 0;
        *(s32 *) (arg0 + 0x3C) = *(s32 *) (arg0 + 0x3C) ^ 1;
    }
    *(s16 *) (arg0 + 0x18) = D_800902FC[*(s32 *) (arg0 + 0x3C)];
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

#pragma GLOBAL_ASM("asm/nonmatchings/generated_5D2C0/func_15033E28.s")

s32 func_15033E84(u8 *arg0) {
    u8 *node = D_800C3EE0;

    if (node != 0) {
        u8 type = arg0[0x3B];
        u8 *next;

        do {
            next = *(u8 **) (node + 0x54);

            if (type == node[0]) {
                return (s32) node;
            }
        } while ((node = next) != 0);
    }
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_5D2C0/func_15033EC4.s")

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
    u8 *ptr;

    if (D_800C35EA == 1) {
        return 0;
    }
    ptr = *(u8 **) (arg1 + 0x31C);
    if (ptr != 0) {
        u8 type = ptr[0x78];

        if ((type != 0xC) && (type != 0x16)) {
            if (ptr[0x11A] != 3) {
                ptr[0x11A] = 0;
                return 1;
            }
        }
    }
    return 0;
}
