#include <ultra64.h>
extern u8 D_800CC406[];
extern s32 D_800C3E80[];
extern u8 D_800BE9C0;
extern s32 D_800C3E88;
extern s32 D_800C3E8C;
extern u16 D_800C3E7A;
extern u8 D_800C3E90;
extern u16 D_800C4ED0[];
extern u8 D_800CC33A[];
extern u8 D_80038080;
extern s32 D_800BE9F0;
extern u8 D_800D2040[];

typedef struct ActorDisplay58F80 {
    s32 active;
    u8 id;
    u8 state;
    u8 pad6[0x17E];
    u32 flags;
    u8 pad188[0x1A4];
} ActorDisplay58F80;

extern ActorDisplay58F80 D_800CC2D0[26];
extern Gfx D_80084160[], D_80084190[];
extern s32 D_8003C8E0;
s32 func_1506196C(ActorDisplay58F80 *actor, s32 view);
Gfx *func_1502C408();
Gfx *func_1502C974();
Gfx *func_150368C4(Gfx *commands, s32 slot, s32 view);
Gfx *func_15030E08(Gfx *commands, s32 view, s32 mode);

Gfx *func_1502BAD0(Gfx *commands, s32 mode, s16 view) {
    ActorDisplay58F80 *actor;
    s32 slot;
    s32 state;

    gSPDisplayList(commands++, D_80084160);
    actor = D_800CC2D0;
    for (slot = 0; slot != 25; slot++, actor++) {
        D_8003C8E0 = (slot & 0xFFFFFF) | 0x1000000;
        state = actor->active;
        if (state == 0) {
            continue;
        }
        state = actor->state;
        if (state == 3 || state == 5) {
            continue;
        }
        if (state == 2) {
            if (mode != 2) {
                continue;
            }
        } else if (actor->id == 255) {
            continue;
        }
        if (mode == 6) {
            if (state != 7) {
                continue;
            }
        } else if (mode == 0) {
            if (((actor->flags >> 9) & 1) == 0) {
                continue;
            }
        } else if (mode == 1) {
            if (state == 7 || state == 1) {
                continue;
            }
            if (state == 0 && func_1506196C(actor, view) < 255) {
                continue;
            }
        } else if (mode == 2) {
            if (state != 2) {
                if (state == 7 || (state != 0 && state != 1)) {
                    continue;
                }
                if (state == 0 && func_1506196C(actor, view) == 255) {
                    continue;
                }
            }
        }
        /* The filter callback can change the state used to select a renderer. */
        if (actor->state == 2) {
            commands = func_1502C408(commands, slot);
        } else {
            commands = func_1502C974(commands, slot, view, mode, 0);
            if (slot == 0) {
                commands = func_150368C4(commands, slot, view);
            }
        }
    }
    D_8003C8E0 = 0x1FFFFFF;
    if (mode == 1) {
        commands = func_15030E08(commands, view, 0);
    } else if (mode == 2) {
        commands = func_15030E08(commands, view, 1);
    } else if (mode == 6) {
        commands = func_15030E08(commands, view, 2);
    }
    gSPDisplayList(commands++, D_80084190);
    D_8003C8E0 = 0;
    return commands;
}

typedef struct ActorUpdate58F80 {
    s32 active;
    u8 id;
    u8 state;
    u8 pad6[0x5F];
    u8 predecessor;
    u8 pad66[0x3E];
    u8 signal;
    u8 padA5[0x53];
    u32 flags;
    u8 padFC[0x38];
    u8 eventA;
    u8 eventB;
    u8 pad136[0x93];
    u8 prepare;
    u8 pad1CA[0xA];
    s32 work;
    u8 pad1D8[0x24];
    u8 status;
    u8 pad1FD[0x63];
    u32 optional;
    u8 pad264[0x10];
    u8 maskId;
    u8 pad275[0xB7];
} ActorUpdate58F80;

extern u8 D_800C666F[];
s32 func_1502DF38();
s32 func_1502C608();
s32 func_1502FBE8();
s32 func_1502E4C4();
s32 func_1503A08C();
s32 func_150345E4();
s32 func_1503A830();
s32 func_1503DF48();
s32 func_1502EEF4();
s32 func_1502F264();
s32 func_1502EAFC();
s32 func_150A4B04();
s32 func_1517AD00();

void func_1502BD84(ActorUpdate58F80 *actor, s32 slot) {
    s32 state;

    state = actor->state;
    actor->work = 0;
    if (state == 5) {
        func_1502DF38(slot, 1);
        return;
    }
    if (actor->id == 255 || state == 3) {
        return;
    }
    if (state == 2) {
        func_1502C608(slot);
        return;
    }
    if (actor->prepare != 0) {
        func_1502FBE8(actor);
    }
    func_1502E4C4(slot);
    func_1502DF38(slot, 0);
    func_1503A08C(actor);
    if (actor->work == 0) {
        actor->status = 2;
    } else {
        func_150345E4(slot);
        func_1503A830(actor);
    }
    if (D_800C666F[slot * 16] != 0) {
        func_1503DF48(slot);
    }
    if (actor->active != 0) {
        func_1502EEF4(slot);
        func_1502F264(slot);
        if (actor->signal != 0) {
            func_1502EAFC(actor);
        }
        if ((actor->flags & 0x4000) != 0) {
            func_150A4B04(actor);
        }
        if (actor->optional != 0) {
            func_1517AD00(actor->eventA, actor->eventB, slot);
        }
    }
}

extern u32 D_800C3E74;
extern u8 D_800C3E70, D_800BEAC0;
extern ActorUpdate58F80 D_800D121C[];
void func_1503F964(void);
s32 func_1502F3C8();
s32 func_1502F948();
s32 func_15030468();
s32 func_1507C22C();

void func_1502BEE4(void) {
    ActorUpdate58F80 *actor;
    ActorUpdate58F80 *cursor;
    s32 slot;
    s32 maxDepth;
    s32 index;
    u8 ordered[25];
    u8 depths[25];
    s32 count;

    func_1503F964();
    D_800C3E90 = 0;
    D_800C3E74 = 0;
    maxDepth = 0;
    actor = ((ActorUpdate58F80 *)D_800CC2D0);
    do {
        if (actor->maskId != 0) {
            D_800C3E74 |= 1u << ((actor->maskId + 31) & 31);
        }
        actor++;
    } while (actor < (((ActorUpdate58F80 *)D_800CC2D0) + 25));
    bzero(depths, 25);
    slot = 0;
    actor = ((ActorUpdate58F80 *)D_800CC2D0);
    do {
        if (actor->active != 0) {
            if (actor->predecessor != 0) {
                cursor = actor;
                depths[slot] = 0;
                while (cursor->predecessor != 0) {
                    cursor = ((ActorUpdate58F80 *)D_800CC2D0) + (cursor->predecessor - 1);
                    depths[slot]++;
                }
                if (maxDepth < depths[slot]) {
                    maxDepth = depths[slot];
                }
            } else {
                func_1502BD84(actor, slot);
            }
        }
        slot++;
        actor++;
    } while (slot < 25);
    count = 0;
    if (maxDepth != 0) {
        for (slot = 1; slot <= maxDepth; slot++) {
            for (index = 0; index < 25; index++) {
                if (depths[index] == slot) {
                    ordered[count++] = index;
                }
            }
        }
        for (slot = 0; slot < count; slot++) {
            func_1502BD84(((ActorUpdate58F80 *)D_800CC2D0) + ordered[slot], ordered[slot]);
        }
    }
    func_1502F3C8();
    actor = ((ActorUpdate58F80 *)D_800CC2D0);
    do {
        if (actor->active != 0) {
            func_1502F948(actor);
        }
        actor++;
    } while (actor != D_800D121C);
    func_15030468();
    if (D_800BEAC0 == 0) {
        func_1507C22C(0);
    }
    D_800C3E70 = 0;
}

s32 func_1502C1A4() {
    return 0;
}

void func_1502C380(void) {
    D_800C3E88 = D_800C3E80[D_800BE9C0];
    D_800C3E8C = D_800C3E88;
    D_800C3E7A = 0;
}

s32 func_1502C3BC(s32 arg0) {
    s32 temp_v1 = *(D_800CC406 + arg0 * 0x32C);

    if (temp_v1 >= 0x46) {
        temp_v1 = 0xB;
    }
    return temp_v1;
}

Gfx *func_1502C408() {
    return 0;
}

s32 func_1502C608() {
    return 0;
}

s32 func_1502C6E8() {
    return 0;
}

Gfx *func_1502C974() {
    return 0;
}

s32 func_1502CC34() {
    return 0;
}

s32 func_1502CCFC() {
    return 0;
}

s32 func_1502D54C() {
    return 0;
}

s32 func_1502D630() {
    return 0;
}

s32 func_1502D824() {
    return 0;
}

s32 func_1502DB20(s32 arg0) {
    switch (arg0) {
        case 59:
        case 117:
        case 130:
        case 136:
        case 144:
        case 150:
        case 152:
        case 156:
        case 157:
        case 159:
        case 160:
        case 177:
        case 178:
        case 180:
            return D_800C4ED0[arg0] - 4;
        default:
            return D_800C4ED0[arg0];
    }
}

s32 func_1502DB84() {
    return 0;
}

s32 func_1502DF38() {
    return 0;
}

void func_1502E474(void) {
    if (D_800C3E7A != 0) {
        func_150A9984(D_800C3E80[D_800BE9C0], D_800C3E7A);
    }
    D_800C3E90 = 1;
}

s32 func_1502E4C4() {
    return 0;
}

void func_1502E9FC(s32 arg0, s32 arg1) {
}

void func_1502EA0C(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5) {
    arg0[0xA4] = 4;
    arg0[0xA5] = 0;
    arg0[0xA6] = arg5;
    arg0[0xA7] = 0xFF;
    *(u32 *) (arg0 + 0xA0) = (arg4 << 24) | (arg1 << 16) | (arg2 << 8) | arg3;
}

void func_1502EA50(u8 *arg0) {
    arg0[0xA4] = 5;
}

void func_1502EA60(u8 *arg0, s32 arg1) {
    arg0[0xA4] = 2;
    arg0[0xA5] = 0xFF;
    arg0[0xA6] = arg1;
}

void func_1502EA7C(u8 *arg0, s32 arg1) {
    arg0[0xA4] = 3;
    arg0[0xA5] = 0xFF;
    arg0[0xA6] = arg1;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_58F80/func_1502EA98.s")

s32 func_1502EAFC() {
    return 0;
}

s32 func_1502EC34() {
    return 0;
}

s32 func_1502EE8C(s32 arg0, s32 arg1) {
    s32 value = D_800CC33A[arg0 * 0x32C + arg1];
    s32 result;

    if (value < 2) {
        result = value;
    } else if (value < 4) {
        result = value - 2;
    } else {
        result = 2;
    }
    return result;
}

s32 func_1502EEF4() {
    return 0;
}

s32 func_1502F01C() {
    return 0;
}

s32 func_1502F264() {
    return 0;
}

s32 func_1502F3C8() {
    return 0;
}

s32 func_1502F490() {
    return 0;
}

s32 func_1502F948() {
    return 0;
}

s32 func_1502F9FC() {
    return 0;
}

s32 func_1502FBE8() {
    return 0;
}

// Matched with guarded sentinel allocation and fallback scheduling.
void func_1502FD70(u8 *arg0) {
    u8 index = arg0[4];
    u8 *state;
    s32 state_value;
    u8 *object;
    s32 object_value;
    s32 sentinel;
    s32 scaled;

    if ((D_80038080 == 0) && (D_800BE9F0 == 0x1D)) {
        D_800D2040[index] = 2;
        return;
    }

    state = &D_800D2040[index];
    state_value = *state;
    sentinel = 0xFF;
    if (state_value != sentinel) {
        object = *(u8 **)(arg0 + 0x144);
        if (object == NULL) {
            scaled = 3;
        } else {
            object_value = object[0x2E];
            if (object_value == sentinel) {
                return;
            }
            if (object_value == 0) {
                scaled = 3;
            } else {
                scaled = object_value * 30;
                if (state_value < scaled) {
                    *state = scaled;
                    return;
                }
                return;
            }
        }
        *state = scaled;
    }
}
