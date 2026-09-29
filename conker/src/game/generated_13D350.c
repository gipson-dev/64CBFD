#include <ultra64.h>
void func_150A8050(f32 [4][4], f32, f32, f32);
void func_150A7A48(f32 [4][4], f32 [4][4], f32 [4][4]);
typedef struct {
    u8 pad0[0xBC];
    f32 mtx[4][4];
    u8 padFC[0x84];
} Record13D350;
extern Record13D350 *D_800BE628;
extern s32 D_800DBEF0;
extern u8 *D_800DBEF4;
extern s32 *D_800DBF94;

/* Non-matching placeholders for the text-only asm slice asm/13D350.s. */

s32 func_1510FEA0() {
    return 0;
}

void func_151102CC(f32 arg0[4][4], f32 arg1, f32 arg2, f32 arg3) {
}

void func_15110360(s32 arg0, f32 arg1[4][4], f32 arg2, f32 arg3, f32 arg4) {
    func_151102CC(arg1, arg2, arg3, arg4);
    func_150A7A48(arg1, D_800BE628[arg0].mtx, arg1);
}

s32 func_151103C8() {
    return 0;
}

s32 func_15110544() {
    return 0;
}

s32 func_15110600() {
    return 0;
}

s32 func_151106A8() {
    return 0;
}

s32 func_151108C4() {
    return 0;
}

s32 func_15110CFC() {
    return 0;
}

s32 func_1511172C() {
    return 0;
}

s32 func_15111858() {
    return 0;
}

s32 func_15111AF4() {
    return 0;
}

s32 func_15112520() {
    return 0;
}

s32 func_15112A80() {
    return 0;
}

s32 func_15113180() {
    return 0;
}

s32 func_15113218() {
    return 0;
}

s32 func_151135C4() {
    return 0;
}

s32 func_151137D4() {
    return 0;
}

s32 func_15113C88() {
    return 0;
}

s32 func_15113E54() {
    return 0;
}

s32 func_15114050(u8 *arg0, s32 arg1) {
    if (arg0[0x4F] & 0x80) {
        if (arg1 == -1) {
            return 1;
        }
        if (D_800DBF94[(arg0 - D_800DBEF4) / 0xA0] & (1 << arg1)) {
            return 1;
        }
    }
    return 0;
}

s32 func_151140C4() {
    return 0;
}

s32 func_15114188() {
    return 0;
}

s32 func_15114348() {
    return 0;
}

s32 func_1511473C() {
    return 0;
}

void func_151148A8(f32 arg0[4][4], f32 arg1[3]) {
    f32 temp[4][4];

    func_150A8050(arg0, 0.0f, arg1[1], 0.0f);
    func_150A8050(temp, arg1[0], 0.0f, arg1[2]);
    func_150A7A48(temp, arg0, arg0);
}

s32 func_1511490C() {
    return 0;
}

u8 *func_151149AC(u8 arg0) {
    s32 offset;
    s32 i;
    u8 *base;
    u8 *record;

    if (arg0 == 0) {
        return NULL;
    }

    i = 0;
    if (D_800DBEF0 > 0) {
        base = D_800DBEF4;
        offset = 0;
        record = base;
        do {
            if (record[0x72] == arg0) {
                return offset + base;
            }
            i++;
            offset += 0xA0;
            record += 0xA0;
        } while (i < D_800DBEF0);
    }
    return NULL;
}

s32 func_15114A1C() {
    return 0;
}

s32 func_15114B94() {
    return 0;
}

extern s32 func_15114CC4();

#pragma GLOBAL_ASM("asm/nonmatchings/generated_13D350/func_15114CC4.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_13D350/func_15114D24.s")

void func_15114F04(s32 arg0, s32 arg1, s32 arg2) {
    func_1001001C(func_15114CC4, arg0, 0, arg1, arg2);
}

s32 func_15114F44() {
    return 0;
}
