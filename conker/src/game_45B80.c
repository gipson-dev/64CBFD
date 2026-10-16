#include <ultra64.h>

#include "functions.h"
#include "variables.h"

/* Frame-coordinator interfaces recovered from their integer call sites. */
extern u8 D_800DCD27;
void func_1510D864(void);
s32 func_1509BA04(s32);
s32 func_1509BBA0(s32);
s32 func_1501E400(s32);
void func_15034F20(void);
void func_1510B690(void);
void func_1510F800(s32);
s32 func_15113180(void);
s32 func_15113E54(s32);
s32 func_15114188(void);
void func_15044A28(void);
s32 func_150242F8(s32, s32);
s32 func_1501EC38(s32);
s32 func_15020EC4(s32);
s32 func_1501E2F8(s32);
s32 func_15087CC0(void);
void func_1504ADD0(void);
s32 func_1510FC34(s32);
void func_15094EA0(s32);
s32 func_15112A80(s32);
s32 func_151749F8(s32, s32);
s32 func_15188B74(s32);
void func_1516706C(void);
s32 func_151671E8(void);
void func_1502BEE4(void);
s32 func_150A0D8C(void);
s32 func_15113218(void);
s32 func_151738C4(s32);
s32 func_1502C1A4(void);
s32 func_15113C88(void);
s32 func_150636F0(void);
s32 func_15183D28(void);
s32 func_151670C0(void);
s32 func_15177A94(void);
s32 func_151814FC(void);
void func_1517F75C(void);
void func_1517F7B4(void);
s32 func_15036148(void);
void func_1515D6C8(void);

/* Generated placeholder declarations. */
s32 func_1501878C();
s32 func_15019130(void);
s32 func_150195A0();
s32 func_150198FC();
s32 func_15019CC8();
s32 func_15019F20();
/* End generated placeholder declarations. */

void* func_151674F8(void *arg0, s32 arg1, s16 arg2, s32 arg3);

/* Helper declarations not present in functions.h. */
s32  func_1510FEA0(s32 arg0, s32 arg1);
s32  func_1517F4D8(s32 arg0, s32 arg1);
s32  func_1517F3A0(s32 arg0, s32 arg1);
s32  func_15180580(s32 arg0, s32 arg1);
s32  func_1507DB6C(s32 arg0, s32 arg1);
s32  func_1510B7B4(s32 arg0, s32 arg1);
s32  func_151135C4(s32 arg0, s32 arg1, s16 arg2);
s32  func_151D6778(s32 arg0);
s32  func_15186794(s32 arg0, s32 arg1);
Gfx *func_1502BAD0(Gfx *commands, s32 mode, s16 view);
s32  func_15035FE8(s32 arg0, s32 arg1);
s32  func_15188D00(s32 arg0, s32 arg1, s16 arg2);
s32  func_151D5E90(s32 arg0, s32 arg1, s32 arg2, s32 arg3);
s32  func_151D61B0(s32 arg0);
s32  func_1501A680(s32 arg0);
s32  func_1517E28C(s32 arg0, s32 arg1);
s32  func_15172F70(s32 arg0);
s32  func_15181EE0(s32 arg0);
s32  func_1517F564(s32 arg0);
s32  func_1508FD38(s32 arg0);
s32  func_15096934(s32 arg0);
s32  func_150A019C(void);


void func_150186D0(void) {
    func_10001444();
    func_1501A39C();
    func_151E6BFC();

    D_800BE5E0 = 1;
    D_800D18A0 = 0;
    D_800D18A2 = 0;
    D_800D18A4 = 0;
    D_800D23A9 = 0;

    while (func_1501878C() != 0) {};

    D_8002AC60 = 1;
    D_8002AC64 = 3500;
    *D_800BE728 = func_1501BBB8();

    while (func_151DCFD8(1) != 0) {};
}

// something big and interesting
/* Non-matching C placeholders for asm/nonmatchings/game_45B80/func_1501878C.s. */
s32 func_1501878C() {
    return 0;
}

void func_15018DFC(void) {
    func_150A09D0(D_800BE9E4);
    func_150619A8();
    func_1501C870();
    if (D_800BEAC0 == 0) {
        if (D_800C35EA == 1) {
            func_1502378C();
        } else {
            func_1504A730();
        }
        func_15085ABC(D_800D2340);
    }
    func_1507C370();
    func_1507C8FC();
}

void func_15018E88(void *arg0, s16 arg1) {
    if (D_800BE616 == 0) {
        func_1517D7B0(&arg0, 1);
    }
    arg0 = func_151674F8(arg0, 0, arg1, 0);
    arg0 = func_151674F8(arg0, 0, arg1, 1);
    func_15174AA4(arg0, D_800BE9F0, arg1);
}

void *func_15018F08(void *arg0, s16 arg1) {
    arg0 = func_15174B48(arg0, D_800BE9F0, arg1);
    arg0 = func_151674F8(arg0, 1, arg1, 0);
    arg0 = func_151674F8(arg0, 1, arg1, 1);

    func_1517D7B0(&arg0, 2);

    return arg0;
}

void func_15018F80(s16 arg0) {
    struct108 *sp24 = &D_800DBFF0[arg0];
    D_8003C8E0 = 0xA000000;
    if ((func_1517F40C(arg0) == 0) && (D_800BEAC0 == 0)) {
        func_1517F448(arg0);
    }
    func_1501B640(arg0);
    D_800D3674 = (sp24->unk388 < 0.0f) ? -1000 : 5000;
    func_15172D80(arg0);
    D_8003C8E0 = 0;
}

void func_1501905C(void) {
    D_800BE9D0 = D_800BE9D8[D_800BE9C0];
    *D_800BE728 = func_1501BBB8();
    func_15019F20();
    if ((D_800BEAC1 != 0) && (D_800BEAC0 == 0)) {
        func_15169040(0, 0x47);
    }
    func_1501C1B0();
    func_1501BB20();
    func_1502C380();
    if (0) {};
    func_1000D758(D_800DBFF0->unk2A4, D_800DBFF0->unk2A8, D_800DBFF0->unk2AC);
    func_10011BB8();
    if (D_800E0B94 == 2) {
        func_150ADACC(0x81280783); // 2166884227
    }
    func_10012020();
}

/* Run ordered frame/view passes, then age all software-page records. */
s32 func_15019130(void) {
    s32 view;
    u8 slot;

    func_1510D864();
    func_1509BA04(0);
    func_1509BBA0(2);
    D_800DCD27 = 0;
    func_10004250();
    func_1501E400(0);
    func_15034F20();
    func_1510B690();
    func_1510F800(0);
    func_15113180();
    if (D_800BEAC0 == 0) {
        func_15113E54(1);
    }
    if (D_800BEAC0 == 0) {
        func_15114188();
    }
    func_15044A28();
    func_15018DFC();
    func_150242F8(1, 0);
    func_1501EC38(0);
    func_150242F8(0, 0);
    func_15020EC4(0);
    func_1501E2F8(0);
    if (*(s8 *)&D_800D23A9 != 0) {
        func_15087CC0();
    }
    func_15122AE0();
    func_1504ADD0();
    func_1510F800(0);
    for (view = 0; view <= D_80082FA0; view++) {
        func_1510FC34(view);
    }
    func_1510B690();
    for (slot = 0; slot <= D_80082FA0; slot++) {
        func_15094EA0(slot);
    }
    func_15112A80(0);
    func_151749F8(D_800BE9F0, 0);
    func_1501C860();
    func_1511FC20(D_800BE9C0);
    func_15188B74(0);
    if (D_800BEAC0 == 0) {
        func_1516706C();
        func_151671E8();
    }
    func_1502BEE4();
    if (D_800BE616 == 0) {
        func_150A0D8C();
    }
    func_15113218();
    func_15188B74(1);
    func_151738C4(D_800BE9F0);
    func_1502C1A4();
    func_15113C88();
    if (D_800CC2B0 != 0) {
        func_150636F0();
    }
    if (D_800BEAC0 == 0) {
        func_15183D28();
        func_151670C0();
        func_15177A94();
    }
    if (D_800BEAC0 == 0) {
        func_151814FC();
    }
    func_1517F75C();
    func_1517F7B4();
    func_15036148();
    func_1515D6C8();

    /* The legacy pointer declaration labels this table's address, not its value. */
    for (view = 0; view < 508; view++) {
        ((u32 *)&D_80043B40)[view * 2 + 1]++;
    }
    return 1;
}

void func_15019414(void) {
    if (D_800BEAC0 == 0) {
        func_15167010();
    }
    func_1517ABB0();
    if (D_800BE616 == 0) {
        func_1508F0A4();
    }
}

/* Set up the selected view and append its enabled render passes. */
Gfx *func_15019464(Gfx *commands, s16 view) {
    func_1510B958(view);
    gSPViewport(commands++, (D_800BE628 + ((u32)view * 0x180) + (D_800BE9C0 * 0x10) + 0x40));
    commands = (Gfx *)func_1501A490((s32)commands, view, 0, 0, 0, 0);
    if (D_800BEAC0 != 0) {
        return commands;
    }
    if (D_80084480 != 0) {
        return commands;
    }
    commands = (Gfx *)func_1510FEA0((s32)commands, D_800BE9F0);
    if (func_1517EFAC(view) != 0 || (D_800D18A0 & (1U << view)) != 0) {
        return commands;
    }
    commands = (Gfx *)func_1515D6D0((s32)commands, view);
    commands = func_1510B9D0(commands, view);
    return commands;
}

/* Non-matching C placeholders for asm/nonmatchings/game_45B80/func_150195A0.s. */
s32 func_150195A0() {
    return 0;
}

/* Non-matching C placeholders for asm/nonmatchings/game_45B80/func_150198FC.s. */
s32 func_150198FC() {
    return 0;
}

// Matched with guarded frame-size and viewport-address register normalization.
void func_15019BB8(Gfx *arg0, s32 arg1) {
    s32 temp_v0;
    s16 sp2A;

    sp2A = arg1;
    gSPViewport(arg0++, (D_800BE628 + (arg1 * 0x180) + (D_800BE9C0 * 0x10) + 0x40));
    temp_v0 = func_1501A490(arg0, sp2A, 0, 0, 0, 0);
    temp_v0 = func_1517F4D8(temp_v0, arg1);
    temp_v0 = func_1517F3A0(temp_v0, arg1);
    temp_v0 = func_15180580(temp_v0, arg1);
    if (((D_800D18A0 & (1 << arg1)) != 0) || ((D_800D18A2 & (1 << arg1)) != 0)) {
        temp_v0 = func_1507DB6C(temp_v0, arg1);
    }
    temp_v0 = func_151674F8((void *)temp_v0, 4, sp2A, 0);
    func_151674F8((void *)temp_v0, 4, sp2A, 1);
}

/* Non-matching C placeholders for asm/nonmatchings/game_45B80/func_15019CC8.s. */
s32 func_15019CC8() {
    return 0;
}

void func_15019E60(Gfx *arg0) {
    if (D_80082FA0 != 0) {
        D_80082FA4 = D_80082FA0 + 1;
        gSPViewport(arg0++, (D_80082FA4 * 0x180) + D_800BE628 + 64);
    } else {
        gSPViewport(arg0++, D_800BE628 + 64);
    }
    func_15043384(func_151E8620(func_1501A490(arg0, 0xFF, 0, 0, 0, 0)));
}

/* Non-matching C placeholders for asm/nonmatchings/game_45B80/func_15019F20.s. */
s32 func_15019F20() {
    return 0;
}
