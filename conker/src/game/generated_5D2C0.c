#include <ultra64.h>
extern f32 D_800970DC;
void func_1503F5B8(u8 *, s32, s32, f32, f32, s32);
void func_1505E060(u8 *);
extern s32 D_800902D0;
extern s32 D_800902D4;
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

s32 func_15031E7C(u8 *node, u8 *actor) {
    u8 *source;
    Gfx *commands;
    f32 factor;
    s32 index;
    s32 remaining;

    source = *(u8 **)(actor + 0x2D0);
    if (source == 0) {
        return 0;
    }
    commands = *(Gfx **)*(u8 **)(node + 0x24);
    if (commands == 0) {
        return 0;
    }
    if (*(u16 *)(actor + 0x84) == 0x55) {
        factor = 1.0f;
    } else if (*(u16 *)(actor + 0x84) == 0x56) {
        factor = 0.0f;
    } else if (0.0f <= *(f32 *)(source + 8) && *(f32 *)(source + 8) <= 120.0f) {
        factor = *(f32 *)(source + 8) * D_800970DC;
        factor = 1.0f - factor;
    } else {
        factor = 0.0f;
    }
    index = 0;
    remaining = 4;
    do {
        remaining--;
        while (*(s8 *)&commands[index] != (s8)G_SETTILESIZE) {
            index++;
        }
        if (remaining != 0) {
            index++;
        }
    } while (remaining != 0);
    commands[index].words.w0 = _SHIFTL(G_SETTILESIZE, 24, 8) | _SHIFTL(2, 12, 12) |
        ((s32)(25.0f * factor + 2.0f) & 0xFFF);
    return 0;
}

s32 func_15031FC8(u8 *node, u8 *actor) {
    u8 *source;
    s32 choice;
    u8 *attachment;
    f32 *end_field;
    f32 *current_field;
    s32 old_flags;
    s32 model;
    s32 type;
    s32 copy_state;
    f32 limit;

    source = *(u8 **)(actor + 0x2D0);
    attachment = *(u8 **)(node + 0x48);
    choice = -1;
    if (attachment == 0) {
        return 0;
    }
    old_flags = *(u16 *)(attachment + 4) & ~0x8000;
    copy_state = 1;
    model = actor[4];
    type = *(u16 *)(actor + 0x84);
    switch (model) {
        case 0x58:
            if (node[1] == 0x9B) {
                node[2] = 0x12;
            }
            switch (type) {
                case 0x27: choice = 3; break;
                case 0x28: choice = 4; break;
                case 2: choice = 1; break;
                case 3: choice = 0; break;
                default:
                    choice = 0;
                    if (node[1] == 0x9B) {
                        choice = 3;
                    }
                    break;
            }
            break;
        case 0x5B:
            choice = 0;
            break;
        case 0x5A:
        case 0x74:
        case 0x7A:
            if (*(s32 *)(actor + 0x2E8) != 0) {
                *(s16 *)(node + 0x18) = D_800902D4;
            } else {
                *(s16 *)(node + 0x18) = D_800902D0;
            }
            switch (type) {
                case 0x6: choice = 0x7; break;
                case 0x26:
                case 0x27: choice = 0xF; break;
                case 0x1:
                case 0x2A: choice = 0x3; break;
                case 0x0: choice = 0x5; break;
                case 0x3: choice = 0x6; break;
                case 0x7: choice = 0x2; break;
                case 0xA: choice = 0x4; break;
                case 0xF:
                case 0x1E: choice = 0x8; break;
                case 0x13: choice = 0xD; break;
                case 0x4: choice = 0x9; break;
                case 0x5: choice = 0xA; break;
                case 0x10: choice = 0xB; break;
                case 0x8: choice = 0x10; break;
                case 0x14: choice = 0xE; break;
                case 0x15: choice = 0xE; break;
                case 0x50: choice = 0x13; break;
                case 0x51: choice = 0x14; break;
                default: choice = 6; break;
            }
            break;
        default:
            switch (node[1]) {
                case 0x9E:
                    node[2] = 9;
                    *(u16 *)(node + 0x1E) = 0x41;
                    *(u16 *)(node + 0x20) = 1;
                    switch (type) {
                        case 0x1D6: choice = 1; break;
                        case 0x1D7: choice = 2; node[2] = 0x13; break;
                        case 0x257: choice = 4; node[2] = 0x13; break;
                        case 0x275: choice = 5; node[2] = 0x13; break;
                        case 0x1D8: choice = 3; break;
                    }
                    copy_state = 0;
                    if (node[2] == 0x13) {
                        *(u16 *)(node + 0x1E) = 0;
                    }
                    break;
                case 0x9B:
                    choice = 0;
                    if (actor[5] == 5) {
                        node[2] = 0;
                    } else if (model == 0x8B) {
                        node[2] = 6;
                        switch (type) {
                            case 0xC: choice = 6; break;
                            case 0x13: choice = 7; break;
                        }
                    } else {
                        node[2] = 9;
                        switch (type) {
                            case 0x22E: choice = 5; break;
                            case 0x1B7: choice = 1; break;
                            case 0x1B8: choice = 2; break;
                        }
                    }
                    break;
                case 0x9F:
                    choice = 0;
                    if (actor[5] == 5) {
                        node[2] = 0;
                    } else if (model == 0xB5) {
                        node[2] = 0x12;
                        switch (type) {
                            case 0x34: choice = 1; break;
                            case 0x35: choice = 2; break;
                            case 0x36: choice = 3; break;
                            case 0x37: choice = 4; break;
                        }
                    } else {
                        node[2] = 9;
                    }
                    break;
                case 0x9C:
                    choice = 8;
                    break;
                case 0x9D:
                    choice = 0;
                    if (actor[5] == 5) {
                        node[2] = 0;
                    } else if (model == 0x8B) {
                        node[2] = 6;
                        switch (type) {
                            case 0x13:
                            case 0x20: choice = 4; break;
                            case 0x22: choice = 3; break;
                        }
                    } else {
                        node[2] = 9;
                        switch (type) {
                            case 0x21C: choice = 1; break;
                            case 0x241: choice = 2; break;
                        }
                    }
                    break;
                case 0x9A:
                    switch (model) {
                        case 0x87:
                            node[2] = 0x12;
                            switch (type) {
                                case 1: choice = 1; break;
                                case 5: choice = 2; break;
                                default: choice = 0; break;
                            }
                            break;
                        case 0x99:
                            node[2] = 0x15;
                            switch (type) {
                                case 0x14: choice = 0x3; break;
                                case 0x15: choice = 0x4; break;
                                case 0x16: choice = 0x5; break;
                                case 0x17: choice = 0x6; break;
                                case 0x18: choice = 0x7; break;
                                case 0x1A: choice = 0x8; break;
                                case 0x1B: choice = 0x9; break;
                                case 0x1C: choice = 0xA; break;
                                case 0x1D: choice = 0xB; break;
                                case 0x1E: choice = 0xC; break;
                                case 0x1F: choice = 0xD; break;
                                case 0x20: choice = 0xE; break;
                                case 0x21: choice = 0xF; break;
                                case 0x22: choice = 0x10; break;
                                case 0x23: choice = 0x11; break;
                                default: choice = 0; break;
                            }
                            break;
                    }
                    break;
                case 0x8D:
                    switch (type) {
                        case 0x323: choice = 1; break;
                        case 0x324: choice = 2; break;
                        default: choice = 0; break;
                    }
                    break;
                case 0x8E:
                    switch (type) {
                        case 0xB4: choice = 0; break;
                        case 0xB6: choice = 1; break;
                        case 0xB5: choice = 2; break;
                        case 0xDD: choice = 3; break;
                        case 0xDE: choice = 3; break;
                        default: return 1;
                    }
                    break;
                case 0x8F:
                case 0x90:
                    switch (type) {
                        case 0xB9: choice = 0x1; break;
                        case 0xAE: choice = 0x2; break;
                        case 0xDA: choice = 0x3; break;
                        case 0x104: choice = 0x4; break;
                        case 0x107: choice = 0x5; break;
                        case 0x10B: choice = 0x6; break;
                        case 0x11E: choice = 0x7; break;
                        case 0x11F: choice = 0x8; break;
                        case 0x134: choice = 0x9; break;
                        case 0x135: choice = 0xA; break;
                        case 0x136: choice = 0xB; break;
                        case 0x13B: choice = 0xD; break;
                        case 0x13C: choice = 0xE; break;
                        case 0x145: choice = 0xF; break;
                        case 0x146: choice = 0x10; break;
                        case 0x141: choice = 0x11; break;
                        case 0x147: choice = 0x12; break;
                        case 0x14B: choice = 0x16; break;
                        case 0x14A: choice = 0x15; break;
                        case 0x149: choice = 0x14; break;
                        case 0x148: choice = 0x13; break;
                        case 0x151: choice = 0x18; break;
                        case 0x17F: choice = 0x1A; break;
                        case 0x180: choice = 0x1B; break;
                        case 0x181: choice = 0x1C; break;
                        case 0x182: choice = 0x1D; break;
                        case 0x186: choice = 0x1E; break;
                        case 0x187: choice = 0x1F; break;
                        case 0x189: choice = 0x20; break;
                        case 0x18C: choice = 0x21; break;
                        case 0x18D: choice = 0x22; break;
                        case 0x18E: choice = 0x23; break;
                        case 0x1A0: choice = 0x24; break;
                        case 0x1A3: choice = 0x25; break;
                        case 0x1B3: choice = 0x26; break;
                        case 0x1B4: choice = 0x27; break;
                        case 0x1B5: choice = 0x28; break;
                        case 0x1B6: choice = 0x29; break;
                        case 0x1B7: choice = 0x2A; break;
                        case 0x1B8: choice = 0x2B; break;
                        case 0x1BD: choice = 0x2C; break;
                        case 0x1BE: choice = 0x2D; break;
                        case 0x1BF: choice = 0x2E; break;
                        case 0x1C0: choice = 0x2F; break;
                        case 0x1C1: choice = 0x30; break;
                        case 0x1C2: choice = 0x31; break;
                        case 0x1C3: choice = 0x32; break;
                        case 0x1C4: choice = 0x33; break;
                        case 0x1C5: choice = 0x34; break;
                        case 0x1C6: choice = 0x35; break;
                        case 0x1C7: choice = 0x36; break;
                        case 0x1C8: choice = 0x37; break;
                        case 0x1C9: choice = 0x38; break;
                        case 0x1CA: choice = 0x39; break;
                        case 0x1D1: choice = 0x3A; break;
                        case 0x1D2: choice = 0x3B; break;
                        case 0x1D3: choice = 0x3C; break;
                        case 0x1D5: choice = 0x3D; break;
                        case 0x1D9: choice = 0x3E; break;
                        case 0x1DA: choice = 0x3F; break;
                        case 0x1DB: choice = 0x40; break;
                        case 0x1E3: choice = 0x41; break;
                        case 0x1E4: choice = 0x42; break;
                        case 0x1E5: choice = 0x43; break;
                        case 0x1E6: choice = 0x44; break;
                        case 0x1E7: choice = 0x45; break;
                        case 0x1E8: choice = 0x47; break;
                        case 0x1E9: choice = 0x44; break;
                        case 0x1F0: choice = 0x48; break;
                        case 0x1F1: choice = 0x49; break;
                        case 0x1F2: choice = 0x4A; break;
                        case 0x201: choice = 0x4B; break;
                        case 0x202: choice = 0x4D; break;
                        case 0x203: choice = 0x4E; break;
                        case 0x204: choice = 0x4F; break;
                        case 0x200: choice = 0x50; break;
                        case 0x205: choice = 0x51; break;
                        case 0x208: choice = 0x52; break;
                        case 0x209: choice = 0x53; break;
                        case 0x20A: choice = 0x54; break;
                        case 0x20B: choice = 0x55; break;
                        case 0x20C: choice = 0x56; break;
                        case 0x211: choice = 0x57; break;
                        case 0x212: choice = 0x58; break;
                        case 0x216: choice = 0x59; break;
                        case 0x217: choice = 0x5A; break;
                        case 0x218: choice = 0x5B; break;
                        case 0x219: choice = 0x5C; break;
                        case 0x21A: choice = 0x5D; break;
                        case 0x21B: choice = 0x5E; break;
                        case 0xA8: choice = 0x5F; break;
                        case 0x1FD: choice = 0x4C; break;
                        case 0x228: choice = 0x62; break;
                        case 0x22E: choice = 0x63; break;
                        case 0x22F: choice = 0x64; break;
                        case 0x232: choice = 0x61; break;
                        case 0x220: choice = 0x60; break;
                        case 0x23A: choice = 0x65; break;
                        case 0x23B: choice = 0x66; break;
                        case 0x24D: choice = 0x6E; break;
                        case 0x21C: choice = 0x6F; break;
                        case 0x241: choice = 0x70; break;
                        case 0x23C: choice = 0x67; break;
                        case 0x24B: choice = 0x6D; break;
                        case 0x24A: choice = 0x6C; break;
                        case 0x249: choice = 0x6B; break;
                        case 0x248: choice = 0x6A; break;
                        case 0x246: choice = 0x69; break;
                        case 0x245: choice = 0x68; break;
                        case 0x25C: choice = 0x71; break;
                        case 0x25D: choice = 0x72; break;
                        case 0x25E: choice = 0x73; break;
                        case 0x260: choice = 0x74; break;
                        case 0x266: choice = 0x77; break;
                        case 0x267: choice = 0x78; break;
                        case 0x268: choice = 0x79; break;
                        case 0x26A: choice = 0x7A; break;
                        case 0x26B: choice = 0x7B; break;
                        case 0x26C: choice = 0x7C; break;
                        case 0x26D: choice = 0x7D; break;
                        case 0x275: choice = 0x7E; break;
                        case 0x1D6: choice = 0x7F; break;
                        case 0x1D7: choice = 0x86; break;
                        case 0x1D8: choice = 0x85; break;
                        case 0x276: choice = 0x80; break;
                        case 0x277: choice = 0x81; break;
                        case 0x278: choice = 0x82; break;
                        case 0x265: choice = 0x76; break;
                        case 0x27F: choice = 0x83; break;
                        case 0x280: choice = 0x84; break;
                        case 0x281: choice = 0x87; break;
                        case 0x282: choice = 0x88; break;
                        case 0x290: choice = 0x89; break;
                        case 0x291: choice = 0x8A; break;
                        case 0x292: choice = 0x8B; break;
                        case 0x293: choice = 0x8C; break;
                        case 0x294: choice = 0x8D; break;
                        case 0x295: choice = 0x8E; break;
                        case 0x298: choice = 0x8F; break;
                        case 0x29A: choice = 0x90; break;
                        case 0x29B: choice = 0x91; break;
                        case 0x29C: choice = 0x92; break;
                        case 0x29D: choice = 0x93; break;
                        case 0x2A9: choice = 0x94; break;
                        case 0x2AA: choice = 0x95; break;
                        case 0x2AC: choice = 0x96; break;
                        case 0x2AD: choice = 0x97; break;
                        case 0x2AE: choice = 0x98; break;
                        case 0x2AF: choice = 0x99; break;
                        case 0x2B0: choice = 0x9A; break;
                        case 0x2B2: choice = 0x9B; break;
                        case 0x2B3: choice = 0x9C; break;
                        case 0x2B4: choice = 0x9D; break;
                        case 0x2B5: choice = 0x9E; break;
                        case 0x2B6: choice = 0x9F; break;
                        case 0x2B8: choice = 0xA0; break;
                        case 0x2B9: choice = 0xA1; break;
                        case 0x2BA: choice = 0xA2; break;
                        case 0x2BB: choice = 0xA3; break;
                        case 0x2BC: choice = 0xA4; break;
                        case 0x2BD: choice = 0xA5; break;
                        case 0x2BE: choice = 0xA6; break;
                        case 0x2BF: choice = 0xA7; break;
                        case 0x2C0: choice = 0xA8; break;
                        case 0x2C1: choice = 0xA9; break;
                        case 0x2C4: choice = 0xAA; break;
                        case 0x2CF: choice = 0xAB; break;
                        case 0x2DA: choice = 0xAC; break;
                        case 0x2DB: choice = 0xAD; break;
                        case 0x2DD: choice = 0xAE; break;
                        case 0x2DC: choice = 0xAF; break;
                        case 0x2D9: choice = 0xB0; break;
                        case 0x2DF: choice = 0xB1; break;
                        case 0x2E0: choice = 0xB2; break;
                        case 0x2E1: choice = 0xB3; break;
                        case 0x2E2: choice = 0xB4; break;
                        case 0x2E3: choice = 0xB5; break;
                        case 0x2EC: choice = 0xB6; break;
                        case 0x2ED: choice = 0xB7; break;
                        case 0x2EE: choice = 0xB8; break;
                        case 0x2EF: choice = 0xB9; break;
                        case 0x2F0: choice = 0xBA; break;
                        case 0x2F1: choice = 0xBB; break;
                        case 0x2F8: choice = 0xBC; break;
                        case 0x2F9: choice = 0xBD; break;
                        case 0x301: choice = 0xBE; break;
                        case 0x304: choice = 0xBF; break;
                        case 0x305: choice = 0xC0; break;
                        case 0x306: choice = 0xC1; break;
                        case 0x307: choice = 0xC2; break;
                        case 0x308: choice = 0xC3; break;
                        case 0x309: choice = 0xC4; break;
                        case 0x30A: choice = 0xC5; break;
                        case 0x30B: choice = 0xC6; break;
                        case 0x30C: choice = 0xC7; break;
                        case 0x30D: choice = 0xC8; break;
                        case 0x30E: choice = 0xC9; break;
                        case 0x30F: choice = 0xCA; break;
                        case 0x314: choice = 0xCB; break;
                        case 0x315: choice = 0xCC; break;
                        case 0x316: choice = 0xCD; break;
                        case 0x317: choice = 0xCE; break;
                        case 0x318: choice = 0xCF; break;
                        case 0x319: choice = 0xD0; break;
                        case 0x31C: choice = 0xD1; break;
                        case 0x31D: choice = 0xD2; break;
                        case 0x31E: choice = 0xD3; break;
                        case 0x320: choice = 0xD4; break;
                        case 0x31F: choice = 0xD5; break;
                        case 0x321: choice = 0xD6; break;
                        case 0x322: choice = 0xD7; break;
                        case 0x323: choice = 0xD8; break;
                        case 0x324: choice = 0xD9; break;
                        case 0x326: choice = 0xDA; break;
                        case 0x327: choice = 0xDB; break;
                        case 0x328: choice = 0xDC; break;
                        case 0x32B: choice = 0xDD; break;
                        case 0x32C: choice = 0xDE; break;
                        case 0x32D: choice = 0xDF; break;
                        case 0x32E: choice = 0xE0; break;
                        case 0x32F: choice = 0xE1; break;
                        case 0x330: choice = 0xE2; break;
                        case 0x331: choice = 0xE3; break;
                        case 0x332: choice = 0xE4; break;
                        case 0x333: choice = 0xE5; break;
                        case 0x334: choice = 0xE6; break;
                        case 0x335: choice = 0xE7; break;
                        case 0x345: choice = 0xE8; break;
                        case 0x347: choice = 0xEA; break;
                        case 0x348: choice = 0xEB; break;
                        case 0x349: choice = 0xEC; break;
                        case 0x34A: choice = 0xED; break;
                        case 0x34B: choice = 0xEE; break;
                        case 0x34C: choice = 0xEF; break;
                        case 0x34D: choice = 0xF0; break;
                        case 0x240: choice = 0xE9; break;
                        default: choice = 0; break;
                    }
                    break;
                case 0x83:
                    switch (type) {
                        case 0x5E: choice = 0; break;
                        case 0x5F:
                        case 0xFA: choice = 1; break;
                        case 0x60: choice = 2; break;
                        case 0xB3: choice = 3; break;
                        default: return 1;
                    }
                    break;
                case 0x85:
                    if (type == 0x13E) {
                        choice = 5;
                    } else if (type == 0x13F) {
                        choice = 4;
                    } else if (type == 0x7C) {
                        choice = 2;
                    } else {
                        choice = 0.0f < *(f32 *)(actor + 0x3C) ? 1 : 0;
                    }
                    break;
                case 0x88:
                    switch (type) {
                        case 0x11: choice = 0; break;
                        case 0x26: choice = 1; break;
                        default: choice = 2; break;
                    }
                    break;
                case 0x98:
                    if (model == 0x8B) {
                        node[2] = 6;
                        choice = 5;
                    } else {
                        switch (type) {
                            case 0x12C: choice = 0; break;
                            case 0x12D: choice = 3; break;
                            case 0x142: choice = 4; break;
                            case 0x12E:
                            case 0x358: choice = 2; break;
                            case 0x2AA: choice = 6; break;
                            default: return 1;
                        }
                    }
                    break;
                case 0x87:
                    switch (type) {
                        case 0x172: choice = 0; break;
                        case 0x174: choice = 2; break;
                        case 0x17A: choice = 3; break;
                        case 0x171:
                        case 0x173: choice = 1; break;
                        default: return 1;
                    }
                    break;
                case 0x89:
                    if (actor[5] == 5) {
                        choice = 3;
                        node[2] = 0;
                    } else {
                        switch (type) {
                            case 0x49: choice = 0; node[2] = 9; break;
                            case 0x47: choice = 1; node[2] = 9; break;
                            case 0x81: choice = 2; node[2] = 0x13; break;
                            default: return 1;
                        }
                    }
                    break;
                case 0x91:
                    if (actor[5] == 5) {
                        node[2] = 0;
                        choice = *(f32 *)(actor + 0x24) == 0.0f ? 3 : 0;
                    } else {
                        node[2] = 0xE;
                        switch (type) {
                            case 0x12: choice = 2; break;
                            case 0x10: choice = 1; break;
                            default: choice = 4; break;
                        }
                    }
                    break;
            }
            break;
    }
    if (choice != -1) {
        func_1503F5B8(*(u8 **)(node + 0x48), 0, choice, 0.0f, 0.0f, 1);
    }
    if (source != 0) {
        attachment = *(u8 **)(node + 0x48);
        if (choice == old_flags && *(s16 *)(source + 0x3C) == 0x3FF) {
            func_1505E060(attachment);
            attachment = *(u8 **)(node + 0x48);
        } else {
            attachment = *(u8 **)(node + 0x48);
        }
        *(f32 *)(attachment + 8) = *(f32 *)(source + 8);
        attachment = *(u8 **)(node + 0x48);
        if (copy_state != 0) {
            if (*(s8 *)(attachment + 0x39) != 0 || attachment[0x215] == 0) {
                *(s16 *)(attachment + 0x3A) = *(s16 *)(source + 0x3A);
                *(s16 *)(*(u8 **)(node + 0x48) + 0x3C) = *(s16 *)(source + 0x3C);
                attachment = *(u8 **)(node + 0x48);
            }
        }
        end_field = (f32 *)(attachment + 0x18);
        current_field = (f32 *)(attachment + 8);
        limit = *end_field - 1.0f;
        if (limit <= *current_field) {
            *current_field = limit;
        }
    }
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

s32 func_150334B8(u8 *node, u8 *actor) {
    Gfx *commands;
    s32 remaining;
    s32 shift;
    s32 index;
    s32 first;
    s32 last;
    s32 original_s;
    s32 original_t;
    s32 span_s;
    s32 span_t;
    s32 wrapped_s;
    s32 wrapped_t;

    commands = 0;
    remaining = 0;
    shift = 0;
    if (node[1] == 0x37) {
        commands = *(Gfx **)*(u8 **)(node + 0x24);
        remaining = 4;
        shift = -100;
    }
    if (commands != 0) {
        index = 0;
        if (remaining != 0) {
            do {
                remaining--;
                while (*(s8 *)&commands[index] != (s8)G_SETTILESIZE) {
                    index++;
                }
                if (remaining != 0) {
                    index++;
                }
            } while (remaining != 0);
        }
        first = commands[index].words.w0;
        last = commands[index].words.w1;
        span_s = ((last >> 12) & 0xFFF) + 2;
        original_s = wrapped_s = ((first >> 12) & 0xFFF) + shift;
        original_t = wrapped_t = first & 0xFFF;
        if (original_s >= span_s) {
            wrapped_s = original_s - span_s;
        }
        if (wrapped_s < 0) {
            wrapped_s += span_s;
        }
        span_t = (last & 0xFFF) + 2;
        if (original_t >= span_t) {
            wrapped_t = original_t - span_t;
        }
        if (wrapped_t < 0) {
            wrapped_t += span_t;
        }
        commands[index].words.w0 = _SHIFTL(G_SETTILESIZE, 24, 8) |
            _SHIFTL(wrapped_s, 12, 12) | (wrapped_t & 0xFFF);
    }
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
