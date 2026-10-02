#include <ultra64.h>
extern u8 D_800BE9C0;
extern u8 D_80089470[];
extern u8 D_800DCC10[];
extern s32 D_80082FA0;
void func_100043B4(s32 *, u32);

typedef struct {
    u8 pad0[0x104];
    s32 entries[4];
    s32 trailing;
} ResourceOwner183640;

/* Non-matching placeholders for the text-only asm slice asm/183640.s. */

s32 func_151D5E30();
s32 func_15157DEC();
void func_15169260(s32, s32, s32, u8);
s32 func_15156190(s32 arg0, u8 arg1, s32 arg2, s32 arg3, s32 arg4);
extern u8 D_800A6060[];

s32 func_15156190(s32 arg0, u8 arg1, s32 arg2, s32 arg3, s32 arg4) {
    return 0;
}

void func_15156388(s32 arg0, u8 arg1, s32 arg2) {
    func_15156190(arg0, arg1, arg2, 0xFF, 0);
}

s32 func_151563B8() {
    return 0;
}

s32 func_151564F8() {
    return 0;
}

s32 func_151568F8() {
    return 0;
}

s32 func_15156B54() {
    return 0;
}

s32 func_15156D24() {
    return 0;
}

void func_15156F94(u8 *arg0) {
    func_151D5E30(arg0 + 0x88, arg0);
}

s32 func_15156FB8(s32 arg0) {
    func_15156F94(arg0);
    func_15169804(arg0);
}

s32 func_15156FE4(s32 arg0) {
    func_15156F94(arg0);
    func_15169824(arg0);
}

s32 func_15157010(s32 arg0, s32 arg1, f32 arg2, s32 arg3, s32 arg4,
                   s32 arg5, u8 arg6, s32 arg7) {
    return 0;
}

void func_151571C4(ResourceOwner183640 *arg0) {
    s32 i;

    for (i = 0; i <= D_80082FA0; i++) {
        if (arg0->entries[i]) {
            func_100043B4(arg0->entries[i], 4);
        }
    }
    if (arg0->trailing != NULL) {
        func_100043B4(arg0->trailing, 4);
    }
}

void func_15157248(u8 *arg0) {
    func_151571C4(arg0);
    func_1518CA04(*(s32 *) (arg0 + 0x18));
    func_1503F7B8(*(s32 *) (arg0 + 0x68));
    func_15169804(arg0);
}

void func_1515728C(u8 *arg0) {
    func_151571C4(arg0);
    func_1518CA04(*(s32 *) (arg0 + 0x18));
    func_1503F7B8(*(s32 *) (arg0 + 0x68));
    func_15169824(arg0);
}

s32 func_151572D0() {
    return 0;
}

s32 func_15157420() {
    return 0;
}

s32 func_15157860(u8 *arg0) {
    struct {
        u8 pad[0x7C];
        f32 matrices[1][4][4];
    } *ptr = (void *) arg0;

    guMtxIdentF(ptr->matrices[D_800BE9C0]);
    return 1;
}

/* Note 533: descriptor-copy allocation wrapper. */
s32 func_15157898(s32 arg0, void *arg1, s32 arg2, f32 arg3, s32 arg4,
                   s32 arg5, u8 *arg6, u8 arg7, s32 arg8) {
    s32 result;

    result = func_15157010(arg0, arg2, arg3, arg4, arg5,
                           (s32) (arg6 + 0x38), arg7, arg8);
    if (result == 0) {
        return 0;
    }
    memcpy((void *) (result + 0x120), arg1, 0x38);
    return result;
}

s32 func_15157918() {
    return 0;
}

s32 func_15157AA8() {
    return 0;
}

void func_15157D88(u8 *arg0, s32 arg1, u8 arg2) {
    func_15169850(arg1, arg2, (s32) (arg0 + 0x4C), (s32) (arg0 + 0x50), (s32) arg0);
}

s32 func_15157DC8(u8 *arg0) {
    func_15157DEC(arg0, arg0 + 0x120);
    return 1;
}

s32 func_15157DEC() {
    return 0;
}

Gfx *func_15157F80(Gfx *arg0, s32 arg1, s32 arg2, s32 arg3, u8 *arg4) {
    gSPMatrix(arg0++, D_80089470, 2);
    gSPMatrix(arg0++, D_800DCC10 + arg2 * 0x40, 6);
    *arg4 = 1;
    return arg0;
}

s32 func_15157FE8() {
    return 0;
}

void func_15158078(s32 arg0, u8 arg1) {
    func_15169260((s32) D_800A6060, 3, arg0, arg1);
}
