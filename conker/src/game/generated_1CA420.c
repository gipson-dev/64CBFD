#include <ultra64.h>
#include "structs.h"
void func_1516972C(struct102 *);

typedef struct { u8 *owner; u8 identity; u8 opaque5[3]; } PayloadOwnerLink;
typedef struct { u8 *before; u8 *after; u8 before_identity; u8 after_identity; u8 opaqueA[2]; } PayloadOwnerLinkEvent;
#include "structs.h"
void func_1519E688(void);

/* Non-matching placeholders for the text-only asm slice asm/1CA420.s. */

extern u8 *D_800E0920;
struct260 *func_151491F4(s16, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, u32);
/* Retail copies the three untouched alignment bytes after code. */
typedef struct {
    u8 *object;
    u8 code;
    s32 reserved;
} Packet1CA420;
s32 func_1514933C();

void func_1519CF70(u8 arg0) {
    u8 value[1];

    value[0] = arg0;
    func_15147D64(value, 6);
}

void func_1519CFA0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 6) |= 1;
    *(temp_v0 + 6) |= 4;
}

void func_1519CFD0(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    func_1514EDF0(arg0, *(s32 *) temp_v0);
    func_151478F4(arg0);
}

void func_1519D000(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    func_1514EDF0(arg0, *(s32 *) temp_v0);
    func_15147928(arg0);
}

s32 func_1519D030() {
    return 0;
}

s32 func_1519D240() {
    return 0;
}

s32 func_1519D454() {
    return 0;
}

s32 func_1519D9F4() {
    return 0;
}

s32 func_1519E1F4() {
    return 0;
}

typedef struct {
    u8 *owner;
    u8 reserved4;
    u8 matrixIndex;
    u8 reserved6[2];
    f32 point[3];
} MatrixPointBinding;
void func_15143134(f32 *, f32 *, u8 *);

/* Transform the bound point, then interpolate each coordinate from the origin. */
s32 func_1519E304(MatrixPointBinding *binding, f32 *output,
                 f32 x, f32 y, f32 z, f32 amount) {
    f32 transformed[3];
    u8 (*matrices)[64] = *(u8 (**)[64])(binding->owner + 0x1D4);

    if (matrices == NULL) {
        return 0;
    }
    func_15143134(binding->point, transformed,
                  matrices[binding->matrixIndex]);
    output[0] = (transformed[0] - x) * amount + x;
    output[1] = (transformed[1] - y) * amount + y;
    output[2] = (transformed[2] - z) * amount + z;
    return 1;
}

/* Reset the effect group and start both presets with their controller. */
void func_1519E3BC(u8 *actor, s16 duration, u8 slot, s32 context) {
    func_1519E688();
    /* Promote the slot explicitly at the legacy builder boundary. */
    func_1519D030(actor, 3, 300, 0, (u32)slot, context);
    func_1519D030(actor, 4, 300, 0, (u32)slot, context);
    func_151491F4(duration, 6, -1, 1, 3, 0, slot, context);
}

s32 func_1519E464() {
    return 0;
}

/* Retarget the payload owner link or release its matching actor. */
void func_1519E570(struct260 *owner, s32 eventAddress, u8 command) {
    PayloadOwnerLink *link = (PayloadOwnerLink *)((u8 *)owner + 0x28);
    PayloadOwnerLinkEvent *event = (PayloadOwnerLinkEvent *)eventAddress;

    if (command == 0) {
        if (link->owner == event->before || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else if (command == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    }
}

void func_1519E61C(u8 *arg0, s32 arg1, u8 arg2) {
    if ((arg2 == 0) || (arg2 == 9)) {
        func_1516972C((struct102 *)arg0);
    }
}

void func_1519E65C(u8 arg0) {
    func_1519CF70(3);
    func_1519CF70(4);
}

void func_1519E688(void) {
    func_1519CF70(3);
    func_1519CF70(4);
    func_15147D64(0, 9);
}

void func_1519E6BC(u8 *arg0) {
    Packet1CA420 packet;

    func_1519E688();
    if (D_800E0920 == NULL) {
        packet.reserved = 0;
        packet.object = arg0;
        packet.code = arg0[0x3B];
        D_800E0920 = (u8 *)func_151491F4(0x12C, -1, 9, 0, 4, 12, 0xFF, 0);
        if (D_800E0920 != NULL) {
            memcpy(D_800E0920 + 0x28, &packet, sizeof(packet));
        }
    }
}

s32 func_1519E754() {
    return 0;
}

/* Retarget the payload link, or release this record and clear the global. */
void func_1519E818(struct260 *owner, s32 eventAddress, u8 command) {
    PayloadOwnerLink *link = (PayloadOwnerLink *)((u8 *)owner + 0x28);
    PayloadOwnerLinkEvent *event = (PayloadOwnerLinkEvent *)eventAddress;
    s32 code = command;

    if (command == 0) {
        u8 *current = link->owner;
        u8 *first = event->before;
        if (current == first || link->identity == ((u8 *)event)[4]) {
            func_1516972C((struct102 *)owner);
            D_800E0920 = NULL;
        }
    } else if (code == 0x2D) {
        u8 *current = link->owner;
        if (current == event->before) {
            link->owner = event->after;
            link->identity = event->after_identity;
        } else if (current == event->after) {
            link->owner = event->before;
            link->identity = event->before_identity;
        }
    }
}

s32 func_1519E8CC(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x28));
    func_1514933C(arg0);
}

s32 func_1519E8F8(u8 *arg0) {
    func_1514EDF0(arg0, *(s32 *)(arg0 + 0x28));
    func_15149368(arg0);
}

void func_1519E924(u8 *arg0) {
    D_800E0920 = 0;
    func_1514933C(arg0);
}

void func_1519E948(u8 *arg0) {
    D_800E0920 = 0;
    func_15149368(arg0);
}
