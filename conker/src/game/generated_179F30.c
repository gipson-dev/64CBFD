#include <ultra64.h>
s32 func_151ACA60(u8 *, f32, s32);
extern u8 *D_800D2E4C;
void func_15083568(u8 *, s32, f32, s32);
extern s32 D_800BE9F0;

/* Non-matching placeholders for the text-only asm slice asm/179F30.s. */

void func_1500EE18();

s32 func_1514F194();
void func_1514DCAC();
s32 func_1516972C();
s32 func_1515F10C();
s32 func_1514E920();
s32 func_1514E89C();
s32 func_15158BD0();
s32 func_1514EC1C(s32 arg0, s32 arg1, s32 arg2);
s32 func_1515BE50(void *arg0, s32 arg1, u8 arg2, s32 arg3);
extern u8 D_800A5920[];
extern u8 D_800A5988[];
extern f32 D_800A5E5C;

typedef struct {
    u8 *object;
    u8 unique_id;
    u8 pad5;
    u16 size;
} GameObjectRequest;

typedef struct {
    s32 unk0;
    f32 unk4;
    u8 *object;
    u8 unique_id;
    u8 padD[3];
    f32 parameter;
    s16 count;
    s16 size;
    u8 mode;
    u8 pad19[3];
} GameObjectSpawnRequest;

typedef struct GameListNode {
    u8 pad0[0x10];
    s32 unk10;
    struct GameListNode *next;
    struct GameListNode *prev;
    s16 unk1C;
} GameListNode;

typedef struct {
    u8 pad0[9];
    u8 enabled;
} GameObjectState;

typedef struct {
    u8 pad0[0x14];
    GameObjectState *state;
} GameObjectWithState;

s32 func_1514CA80() {
    return 0;
}

s32 func_1514D15C() {
    return 0;
}

s32 func_1514D310() {
    return 0;
}

s32 func_1514D3B0() {
    return 0;
}

s32 func_1514D4B8() {
    return 0;
}

s32 func_1514D564() {
    return 0;
}

s32 func_1514D64C() {
    return 0;
}

void func_1514D96C(s32 arg0) {
}

s32 func_1514D978() {
    return 0;
}

void func_1514D9F4(u8 *arg0) {
    u8 *temp;

    func_1514D978(arg0);
    temp = (u8 *) func_151ACA60(arg0, 20.0f, 0);
    func_1514EC1C(temp, arg0, 0x14);
}

void func_1514DA38(u8 *arg0) {
    u8 *result;
    s32 payload[7];

    payload[5] = 0;
    payload[6] = 0;
    payload[0] = 0;
    payload[1] = 0;
    payload[2] = 0;
    payload[3] = 0;
    result = (u8 *) func_15158BD0(arg0, 1, sizeof(payload));
    if (result != 0) {
        memcpy(result + 0x58, payload, sizeof(payload));
        func_1514EC1C((s32) result, (s32) arg0, 0x13);
    }
}

s32 func_1514DAA4() {
    return 0;
}

void func_1514DB18(u8 *arg0) {
    u8 *temp_v0 = (u8 *) func_15158BD0(arg0, 1, 0);

    if (temp_v0 != 0) {
        func_1514EC1C(temp_v0, arg0, 0x13);
    }
}

void func_1514DB58(s32 arg0) {
}

void func_1514DB64(u8 *arg0) {
    if (D_800BE9F0 == 0x14) {
        func_151B2060(arg0);
    }
}

void func_1514DB98(u8 *arg0) {
    func_1514F194(arg0);
}

s32 func_1514DBB8() {
    return 0;
}

void func_1514DC38(s32 arg0) {
    func_1500EE18(arg0, 0xFF, 1);
}

s32 func_1514DC5C(s32 arg0) {
    func_151D0F60(arg0, 0, 0xFF, 1);
}

void func_1514DC84(u8 *arg0) {
    *(u32 *)(arg0 + 0x94) |= 2;
}

void func_1514DC98(u8 *arg0) {
    *(u32 *)(arg0 + 0x94) |= 0x710;
}

void func_1514DCAC(arg0)
u8 *arg0;
{
    *(s32 *) (arg0 + 0x9C) = 0x6000;
    func_15083568(arg0, 0x23, 1.0f, 0);
    func_15083568(arg0, 0x44, 1.0f, 0);
}

void func_1514DCF4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x31C);

    if (temp_v0 != 0) {
        *(temp_v0 + 0x94) = 1;
    }
    func_15083568(arg0, 0x17, 1.0f, 0);
}

void func_1514DD2C(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DD4C(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DD6C(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DD8C(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DDAC(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DDCC(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DDEC(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DE0C(u8 *arg0) {
    func_1514DCAC(arg0);
}

void func_1514DE2C(s32 arg0) {
}

void func_1514DE38(s32 arg0) {
}

void func_1514DE44(s32 arg0) {
}

void func_1514DE50(u8 *arg0) {
    if (*(D_800D2E4C + 0x11) & 8) {
        func_1514DCAC(arg0);
    }
}

void func_1514DE88(s32 arg0) {
}

s32 func_1514DE94() {
    return 0;
}

void func_1514DFD0(u8 *arg0) {
    s32 ret = func_15083FB0(9);

    *(arg0 + 0x65) = ret + 1;
    *(arg0 + 0x101) |= 0x34;
}

s32 func_1514E00C() {
    return 0;
}

s32 func_1514E194() {
    return 0;
}

s32 func_1514E31C() {
    return 0;
}

s32 func_1514E508() {
    return 0;
}

s32 func_1514E5B8() {
    return 0;
}

s32 func_1514E668() {
    return 0;
}

s32 func_1514E718() {
    return 0;
}

void func_1514E7C8(s32 arg0) {
    s32 temp_v0 = func_1518D1C0(arg0, 7, 0, 1, 0xFF, 1, D_800A5920);

    func_1514EC1C(temp_v0, arg0, 0xF);
}

void func_1514E824(s32 arg0) {
}

void func_1514E830(u8 *arg0) {
    func_1516972C(arg0);
}

s32 func_1514E850(s32 arg0) {
    func_1518E308(arg0);
    func_1516972C(arg0);
}

void func_1514E87C(u8 *arg0) {
    func_1515F10C(arg0);
}

s32 func_1514E89C() {
    return 0;
}

s32 func_1514E920() {
    return 0;
}

void func_1514E9DC(u8 *arg0, s32 arg1) {
    func_1514E920(arg0, arg1);
}

void func_1514E9FC(u8 *arg0, s32 arg1, s32 arg2) {
    func_1514E89C(arg0, arg1, arg2);
}

s32 func_1514EA1C() {
    return 0;
}

void func_1514EB6C(u8 *arg0, s32 arg1, s32 arg2) {
    func_1514E89C(arg0, arg1, arg2);
}

s32 func_1514EB8C(s32 arg0, s32 arg1, s32 arg2) {
    return 1;
}

s32 func_1514EBA4() {
    return 0;
}

s32 func_1514EC1C(s32 arg0, s32 arg1, s32 arg2) {
    return 0;
}

s32 func_1514ECE0(GameListNode *node, s16 key, GameListNode **result) {
    s32 found = 0;
    GameListNode *current = node;

    while ((current != NULL) && (found == 0)) {
        node = current->next;
        if (current->unk1C == key) {
            found = 1;
        } else {
            current = node;
        }
    }

    if (result != NULL) {
        *result = current;
    }

    return found;
}

s32 func_1514ED3C(GameListNode *node, s32 key, GameListNode **result) {
    s32 found = 0;
    GameListNode *current = node;

    while ((current != NULL) && (found == 0)) {
        node = current->next;
        if (current->unk10 == key) {
            found = 1;
        } else {
            current = node;
        }
    }

    if (result != NULL) {
        *result = current;
    }

    return found;
}

s32 func_1514ED8C(GameListNode *node, u8 *owner) {
    s32 object;

    if (node == *(GameListNode **)(owner + 0x2F4)) {
        *(GameListNode **)(owner + 0x2F4) = node->next;
    }
    if (node->next != NULL) {
        node->next->prev = node->prev;
    }
    if (node->prev != NULL) {
        node->prev->next = node->next;
    }

    object = node->unk10;
    func_1516972C(node);
    return object;
}

s32 func_1514EDF0() {
    return 0;
}

void func_1514EE70(u8 *arg0) {
    GameObjectRequest request;

    request.object = arg0;
    request.unique_id = arg0[0x3B];
    request.pad5 = 0;
    request.size = 0x12C;
    func_1514EC1C(func_1515BE50(&request, 0, 0xFF, 1), (s32) arg0, 0x16);
}

s32 func_1514EECC() {
    return 0;
}

void func_1514F110(u8 *arg0) {
    func_1514F194(arg0);
}

s32 func_1514F130(GameObjectWithState *arg0, s32 arg1, s32 arg2) {
    switch (arg1) {
        case 0xD:
            arg0->state->enabled = 0;
            break;
        case 0xE:
            arg0->state->enabled = 1;
            break;
        default:
            return func_1514E89C(arg0, arg1, arg2);
    }

    return 1;
}

s32 func_1514F194() {
    return 0;
}

s32 func_1514F308() {
    return 0;
}

s32 func_1514F3CC() {
    return 0;
}

void func_1514F44C(s32 arg0) {
    s32 temp_v0 = func_1518D1C0(arg0, 5, 0, 1, 0xFF, 1, D_800A5988);

    func_1514EC1C(temp_v0, arg0, 0xD);
}

s32 func_1514F4A8(s32 arg0) {
    func_151D74B0(arg0, 1, -1, 0xFF, 1);
}

s32 func_1514F4D8(s32 arg0) {
    func_151D74B0(arg0, 2, 1, 0xFF, 1);
}

void func_1514F508(s32 arg0) {
    func_151D74B0(arg0, 3, 0, 0xFF, 1);
}

s32 func_1514F538(s32 arg0) {
    func_151D74B0(arg0, 4, -1, 0xFF, 1);
}

s32 func_1514F568(s32 arg0) {
    func_150C4120(arg0, -1, 0xFF, 1);
}

void func_1514F590(u8 *arg0) {
    func_1501175C(arg0, 0xFF, 1);
    func_15011A78(arg0, 0xFF, 1);
}

s32 func_1514F5CC(u8 *arg0) {
    GameObjectSpawnRequest request;

    request.unk0 = 0;
    request.unk4 = 0.0f;
    request.object = arg0;
    request.unique_id = arg0[0x3B];
    request.parameter = D_800A5E5C;
    request.count = 20;
    request.size = 0x12C;
    request.mode = 4;
    func_150C0AC0(&request, 0xFF, 1);
}
