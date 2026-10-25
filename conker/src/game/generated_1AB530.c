#include <ultra64.h>
#include "structs.h"

/* C recoveries and remaining non-matching routines from asm/1AB530.s. */

/* Complete private view; the shared struct162 stops before byte 0x30. */
typedef struct ListRecord1AB530 {
    u8 opaque0[0xC];
    f32 valueC;
    f32 value10;
    u8 opaque14[0x10];
    struct ListRecord1AB530 *next;
    s16 state28;
    u16 sample2A;
    u8 opaque2C[2];
    u8 flags2E;
    u8 first2F;
    u8 second30;
    u8 opaque31[3];
} ListRecord1AB530;

extern ListRecord1AB530 *D_800DDD64;
s32 allocate_memory(s32, s32, s32, s32);

extern s32 D_800BE620, D_800BE624;
extern s32 D_800BE9C4;

/* Append through the captured tail link and initialize only the owned fields. */
struct162 *func_1517E080(s32 first, s32 second) {
    ListRecord1AB530 *node;
    ListRecord1AB530 **link;

    node = D_800DDD64;
    if (node != NULL) {
        while (node->next != NULL) {
            node = node->next;
        }
        link = &node->next;
    } else {
        link = &D_800DDD64;
    }
    node = (ListRecord1AB530 *)allocate_memory(0x34, 1, 0, 1);
    if (node == NULL) {
        return NULL;
    }
    *link = node;
    node->next = NULL;
    node->state28 = 0;
    node->flags2E = 0;
    node->value10 = 0.0f;
    node->valueC = 0.0f;
    node->first2F = first;
    node->second30 = second;
    return (struct162 *)node;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_1AB530/func_1517E134.s")

/* Sample the current RGBA16 image at each in-bounds record position. */
void func_1517E1AC(void) {
    ListRecord1AB530 *node = D_800DDD64;

    while (node != NULL) {
        if (node->valueC >= 0.0f && node->valueC < D_800BE620 &&
            node->value10 >= 0.0f && node->value10 < D_800BE624) {
            node->sample2A = ((u16 *)D_800BE9C4)[(s32)node->valueC + (s32)node->value10 * D_800BE620];
        }
        node = node->next;
    }
}

s32 func_1517E28C() {
    return 0;
}

s32 func_1517E4A8() {
    return 0;
}

Gfx *func_1517EA4C(Gfx *arg0) {
    gDPPipeSync(arg0++);
    gDPSetCombine(arg0++, 0xFFB3FF, 0xFF65FEFF);
    gDPSetOtherMode(arg0++, 0x2C0F, 0x504344);
    return arg0;
}

s32 func_1517EAAC() {
    return 0;
}

s32 func_1517EC1C() {
    return 0;
}
