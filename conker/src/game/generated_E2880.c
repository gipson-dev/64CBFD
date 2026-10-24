#include <ultra64.h>
#include "structs.h"

/* Non-matching placeholders for the text-only asm slice asm/E2880.s. */

s32 func_151D2B4C();

s32 func_150B53D0() {
    return 0;
}

s32 func_150B54A8() {
    return 0;
}

void func_150B57C4(s32 arg0) {
    func_151D2B4C(6);
}

s32 func_150B57E8(s32 arg0) {
    func_150B57C4(arg0);
    func_1514933C(arg0);
}

s32 func_150B5814(s32 arg0) {
    func_150B57C4(arg0);
    func_15149368(arg0);
}

typedef struct {
    s32 value;
    u8 tag;
} OwnerReference;

void func_1516972C(struct102 *owner);

/* Event packets use different layouts for removal and link replacement. */
void func_150B5840(struct260 *owner, s32 pairAddress, u8 command) {
    u8 *packet = (u8 *)pairAddress;
    OwnerReference *link;
    s32 first, current;

    link = (OwnerReference *)((u8 *)owner + 0x28);
    if (command == 0) {
        first = *(s32 *)packet;
        if (first == link->value || link->tag == packet[4]) {
            func_1516972C((struct102 *)owner);
        }
    } else {
        if (command == 0x2D) {
            current = link->value;
            first = *(s32 *)packet;
            if (first == current) {
                link->value = *(s32 *)(packet + 4);
                link->tag = packet[9];
            } else if (*(s32 *)(packet + 4) == current) {
                link->value = first;
                link->tag = packet[8];
            }
        }
    }
}
