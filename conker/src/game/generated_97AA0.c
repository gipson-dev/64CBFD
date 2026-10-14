#include <ultra64.h>

typedef struct {
    u8 *object;
    u8 selector;
} ObjectSelector97AA0;

typedef struct {
    u32 first, second;
} PayloadPair97AA0;
typedef struct {
    ObjectSelector97AA0 target;
    PayloadPair97AA0 payload;
} ActorPayload97AA0;
typedef char ActorPayloadSize97AA0[(sizeof(ActorPayload97AA0) == 16) ? 1 : -1];

void *func_15149130(s16, s8, s8, s8, u8, u8, s32, u8, s32);
void *memcpy(void *, const void *, unsigned int);

/* Non-matching placeholders for the text-only asm slice asm/97AA0.s. */

extern s32 D_800CC260;
extern u8 D_800CC2D0[];
s32 func_15137610(u8 *, u8 *, u8 *, s32, u8, s32);

extern u8 D_800D1560[];
extern u8 D_800D1570[];

s32 func_1506A5F0() {
    return 0;
}

s32 func_1506A6FC(s32 arg0, s32 arg1) {
    func_150E0348(arg0, 0xFF, 1);
}

void func_1506A724(s32 arg0, s32 arg1) {
    func_151BB61C(arg0, D_800D1560, D_800D1570, 0xFF, 1);
}

void func_1506A760(s32 arg0, s32 arg1) {
    func_151BBA9C(arg0, D_800D1560, D_800D1570, 0xFF, 1);
}

s32 func_1506A79C() {
    return 0;
}

s32 func_1506A83C(s32 arg0, s32 arg1) {
    func_151BC104(arg0, 0xFF, 1);
}

s32 func_1506A864() {
    return 0;
}

s32 func_1506A968() {
    return 0;
}

void func_1506AA08(s32 arg0, s32 arg1) {
    func_151B7144(arg0, 0xFF, 1);
    func_151B6320(arg0, 0xFF, 1);
}

void func_1506AA48(u8 *actor, const PayloadPair97AA0 *data) {
    u8 *created;
    ActorPayload97AA0 packet;

    packet.target.object = actor;
    packet.target.selector = actor[0x3B];
    packet.payload = *data;
    created = func_15149130(10, 7, 0x23, -1, 1, 0x21, sizeof(packet), 0xFF, 1);
    if (created != NULL) {
        memcpy(created + 0x28, &packet, sizeof(packet));
    }
}

void func_1506AAE0(s32 arg0, s32 arg1) {
    s32 mask = D_800CC260;
    u8 *actor = D_800CC2D0;

    while (mask != 0) {
        if (mask & 1) {
            func_15137610(actor, D_800D1560, D_800D1570, 0, 0xFF, 1);
        }
        mask >>= 1;
        actor += 0x32C;
    }
}

void func_1506AB7C(s32 arg0, u8 *arg1) {
    func_15103E40(arg0, *(s32 *)arg1, arg1 + 4, 1,
                  *(s32 *)(arg1 + 0x10), 0xFF, 1);
}

void func_1506ABC4(s32 arg0, u8 *arg1) {
    func_15103E40(arg0, *(s32 *)arg1, arg1 + 4, 2,
                  *(s32 *)(arg1 + 0x10), 0xFF, 1);
}

void func_1506AC0C(u8 *arg0, s32 arg1) {
    ObjectSelector97AA0 record;

    record.object = arg0;
    record.selector = arg0[0x3B];
    func_151B7328(&record, 0, 8, 0xFF, 1);
}

void func_1506AC58(s32 arg0, u8 arg1) {
    func_151CEAAC(arg0, 0, 1, 0xFF, 1);
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_97AA0/func_1506AC8C.s")
