#include <ultra64.h>

#include "functions.h"
/* This owner uses the display-list label as an SDK pointer, not an integer. */
#define D_800BE9D0 FrameDriverLegacyDisplayListAddress
#include "variables.h"
#undef D_800BE9D0
extern Gfx *D_800BE9D0;

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

/* Scheduler-message and display-list interfaces used by the frame driver. */
extern Gfx *D_800BE9C8, *D_800BE9CC;
extern void *D_800BEB9C;
extern u8 D_800C1060[];
extern Mtx D_80089470;
extern LookAt D_800D9B90[];
extern u8 D_800BE630[], D_800BEBA0, D_800BEAC2;
extern s32 D_800BEBA4;
s32 func_1517E1AC(void);
void func_151412BC(void);
s32 func_151E51EC(void);
void func_1501A39C(void);
void func_1510B3B0(void);
void func_1510B51C(void);
void func_1501905C(void);
void func_1515D69C(void);
s32 func_15167310(void);
void func_15018F80(s16);
Gfx *func_15019464(Gfx *, s16);
void func_15019414(void);
s32 func_15019BB8(Gfx *, s32);
s32 func_15019E60(Gfx *);
s32 func_151E84B0(s32);
s32 func_15043384(s32);
void func_150347E8(void);
void func_1502E474(void);
s32 func_15189118(s32);
s32 func_15084A18(void);
void func_15125628(void);
void func_1510D404(void);
s32 func_15114A1C(void);
s32 func_1517CFC4(void);
s32 func_1501C880(s32, s32);
s32 func_151F2CDC(void);
void func_151F2BE8(void);
void func_151F2C4C(void);

/* The capture counter is signed; the framebuffer label is indexed backward. */
extern s8 D_80082F90;
extern s32 D_8002AAEC;

/* Frame-step history, counters and the existing retail mean-factor label. */
extern u8 D_800BEA0C, D_800BE619, D_800BE61A;
extern u32 D_800BE610;
extern u32 D_800BE9AC;
extern s32 D_800BE9B0;
extern f32 D_800BE5E8[], D_800BE9B8, D_800BE9BC;
extern const f32 D_800968D0;

/* Generated placeholder declarations. */
s32 func_1501878C(void);
s32 func_15019130(void);
s32 func_150195A0(Gfx *, s16);
s32 func_150198FC(Gfx *);
s32 func_15019CC8(Gfx *, s32);
void func_15019F20(void);
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

/* Consume one scheduler message, submit its frame passes, or drain shutdown. */
s32 func_1501878C(void) {
    OSMesg message = NULL;
    s16 view;

    osRecvMesg(&D_800BEA10, &message, OS_MESG_BLOCK);
    D_8002AC60 = 0;
    D_8002AC64 = 800;
    switch (*(s16 *)message) {
        case 2:
            func_1517E1AC();
            if (D_800DC9F0 != 0) {
                func_151412BC();
            }
            (*(s16 *)&D_800BEAA8)--;
            if (D_800BE615 != 0 && *(s16 *)&D_800BEAA8 == 0) {
                func_10004074(D_800BE9C8);
                func_10004074(D_800BE9CC);
                D_800BE9C8 = NULL;
                return 0;
            }
            break;
        case 1:
            if (D_800BE615 != 0) {
                break;
            }
            func_151E51EC();
            if (D_800BE615 != 0) {
                break;
            }
            if (D_800BE614 != 0) {
                func_1501A39C();
                D_800BE614 = 0;
            }
            if (D_800D9AF0 != 0) {
                func_1510B3B0();
            }
            if (D_800D9B18 != 0) {
                func_1510B51C();
            }
            func_1501905C();
            if (D_800BEAC0 == 0 && func_15019130() == 0) {
                break;
            }
            D_800BE9D0 = (Gfx *)func_1501A680((s32)D_800BE9D0);
            func_1515D69C();
            func_15167310();
            for (view = 0; view <= D_80082FA0; view++) {
                D_80082FA4 = D_800BE630[view];
                func_15018F80((s16)D_80082FA4);
                D_800BE9D0 = func_15019464(D_800BE9D0, (s16)D_80082FA4);
            }
            if (D_800BEBA0 == 0) {
                gSPLoadUcodeEx((D_800BE9D0)++, D_800C1060, D_800BEB9C, 0x800);
                gSPClearGeometryMode((D_800BE9D0)++, G_ZBUFFER | G_SHADE | G_CULL_BOTH |
                    G_FOG | G_TEXTURE_GEN | G_TEXTURE_GEN_LINEAR | G_LOD | G_SHADING_SMOOTH);
                gSPSetGeometryMode((D_800BE9D0)++, G_ZBUFFER | G_SHADE | G_LIGHTING | G_SHADING_SMOOTH);
                gSPMatrix((D_800BE9D0)++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
                gSPLookAtX((D_800BE9D0)++, D_800D9B90 + D_800BE9C0);
                gSPLight((D_800BE9D0)++, (u8 *)(D_800D9B90 + D_800BE9C0) + 16, 1);
            }
            for (view = 0; view <= D_80082FA0; view++) {
                Gfx *savedCommands;
                savedCommands = D_800BE9D0;
                D_80082FA4 = D_800BE630[view];
                D_800BE9D0 = (Gfx *)func_1515D6D0((s32)D_800BE9D0, D_80082FA4);
                D_800BE9D0 = (Gfx *)func_150195A0(D_800BE9D0, (s16)D_80082FA4);
                if (((D_800BE9D0 - ((Gfx **)&D_800BE9C8)[D_800BE9C0]) > D_800BEBA4) ? 1 : 0) {
                    D_800BE9D0 = savedCommands;
                }
            }
            D_80082FA4 = 0;
            func_15019414();
            D_800BE9D0 = (Gfx *)func_150198FC(D_800BE9D0);
            for (view = 0; view <= D_80082FA0; view++) {
                D_80082FA4 = D_800BE630[view];
                D_800BE9D0 = (Gfx *)func_1515D6D0((s32)D_800BE9D0, D_80082FA4);
                D_800BE9D0 = (Gfx *)func_15019CC8(D_800BE9D0, D_80082FA4);
                if (D_800BEAC0 == 0 && D_80082FA0 > 0) {
                    D_800BE9D0 = (Gfx *)func_15019BB8(D_800BE9D0, D_80082FA4);
                }
            }
            D_800BE9D0 = (Gfx *)func_15019E60(D_800BE9D0);
            if (D_800BEAC0 == 0 && D_80082FA0 == 0) {
                for (view = 0; view <= D_80082FA0; view++) {
                    D_80082FA4 = D_800BE630[view];
                    D_800BE9D0 = (Gfx *)func_15019BB8(D_800BE9D0, D_80082FA4);
                }
            }
            D_800BE9D0 = (Gfx *)func_151E84B0((s32)D_800BE9D0);
            D_800BE9D0 = (Gfx *)func_15043384((s32)D_800BE9D0);
            func_150347E8();
            func_1502E474();
            func_15189118(0);
            func_15084A18();
            func_15125628();
            gDPFullSync((D_800BE9D0)++);
            gSPEndDisplayList((D_800BE9D0)++);
            func_10004674();
            func_1510D404();
            func_15114A1C();
            func_1517CFC4();
            func_1501C880(0, 1);
            D_800BE9B4 = 0;
            if (D_800BEAC0 != 0) {
                D_800BEAC2 = 2;
            } else if (D_800BEAC2 > 0) {
                D_800BEAC2--;
            }
            if (D_800BEAC1 != D_800BEAC0) {
                D_800BEAC0 = D_800BEAC1;
                if (D_800BEAC0 != 0) {
                    func_1000E2F4(1);
                    func_10011E94(1);
                    if (func_151F2CDC() != 0) {
                        func_151F2BE8();
                    }
                } else {
                    func_1000E2F4(0);
                    func_10011E94(0);
                    if (func_151F2CDC() != 0) {
                        func_151F2C4C();
                    }
                }
            }
            break;
        case 4:
            while (func_151DCFD8(1) != 0) {}
            for (;;) {}
    }
    return 1;
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

s32 func_15018E88(void *arg0, s16 arg1) {
    if (D_800BE616 == 0) {
        func_1517D7B0(&arg0, 1);
    }
    arg0 = func_151674F8(arg0, 0, arg1, 0);
    arg0 = func_151674F8(arg0, 0, arg1, 1);
    return func_15174AA4(arg0, D_800BE9F0, arg1);
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
    D_800BE9D0 = (Gfx *)D_800BE9D8[D_800BE9C0];
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

/* Append the selected view's ordered scene and overlay render passes. */
s32 func_150195A0(Gfx *commands, s16 view) {
    struct108 *state = &D_800DBFF0[view];

    if (D_800BEAC0 != 0) {
        return (s32)commands;
    }
    if (D_80084480 != 0) {
        return (s32)commands;
    }
    if (func_1517EFAC(view) != 0 || (D_800D18A0 & (1U << view)) != 0) {
        return (s32)commands;
    }
    if (D_80082FA0 > 0) {
        commands = (Gfx *)func_1510B7B4((s32)commands, view);
        commands = (Gfx *)func_1515D6D0((s32)commands, view);
        func_1510B958(view);
        gSPViewport(commands++, (view * 0x180) + D_800BE628 + (D_800BE9C0 * 0x10) + 0x40);
        commands = (Gfx *)func_1501A490((s32)commands, view, 0, 0, 0, 0);
    }
    commands = (Gfx *)func_151135C4((s32)commands, 1, view);
    if (D_800BE575 == 2) {
        commands = (Gfx *)func_151D6778((s32)commands);
    }
    commands = (Gfx *)func_151674F8(commands, 6, view, 0);
    commands = (Gfx *)func_151674F8(commands, 6, view, 1);
    commands = (Gfx *)func_15186794((s32)commands, view);
    commands = (Gfx *)func_1501A490((s32)commands, view, 0, 0, 0, 0);
    commands = func_1502BAD0(commands, 1, view);
    commands = (Gfx *)func_15035FE8((s32)commands, view);
    gSPMatrix(commands++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    if (state->unk5F0 & 1) {
        commands = (Gfx *)func_15018E88(commands, view);
        commands = (Gfx *)func_151135C4((s32)commands, 0, view);
        commands = (Gfx *)func_15018F08(commands, view);
    } else {
        commands = (Gfx *)func_15018F08(commands, view);
        commands = (Gfx *)func_151135C4((s32)commands, 0, view);
        commands = (Gfx *)func_15018E88(commands, view);
    }
    commands = (Gfx *)func_15188D00((s32)commands, 0, view);
    commands = (Gfx *)func_15188D00((s32)commands, 1, view);
    commands = func_1502BAD0(commands, 2, view);
    commands = (Gfx *)func_151674F8(commands, 2, view, 0);
    return (s32)func_151674F8(commands, 2, view, 1);
}

/* Append shared overlays and capture/redraw the disabled framebuffer. */
s32 func_150198FC(Gfx *commands) {
    if (D_800BE575 == 1) {
        commands = (Gfx *)func_151D6778((s32)commands);
    }
    if (D_80082FA0 != 0) {
        D_80082FA4 = (s32)((u32)D_80082FA0 + 1U);
        gSPViewport(commands++, ((u32)D_80082FA4 * 0x180) + D_800BE628 + 0x40);
    } else {
        gSPViewport(commands++, D_800BE628 + 0x40);
    }
    commands = (Gfx *)func_1501A490((s32)commands, 0xFF, 0, 0, 0, 0);
    if (D_800BEAC0 != 0) {
        if (D_80082F90 == 0) {
            gDPSetColorImage(commands++, G_IM_FMT_RGBA, G_IM_SIZ_16b, D_800BE620, D_800BE9C4);
            gDPSetScissor(commands++, G_SC_NON_INTERLACE, 0, 0, D_800BE620, D_800BE624);
            commands = (Gfx *)func_151D5E90((s32)commands, (&D_8002AAEC)[-(s32)D_800BE9C0], 0, 1);
            commands = (Gfx *)func_1501A680((s32)commands);
            D_80082F90 = 1;
        } else if (D_80082F90 < 5) {
            D_80082F90++;
            func_151D61B0(D_800BE9C4);
        }
        commands = (Gfx *)func_151D5E90((s32)commands, D_800BE9C4, 0, 1);
    } else {
        D_80082F90 = 0;
    }
    if (func_1517EFAC(0) == 0) {
        commands = (Gfx *)func_1517E28C((s32)commands, D_800BE9F0);
        commands = (Gfx *)func_15172F70((s32)commands);
        commands = (Gfx *)func_15181EE0((s32)commands);
    }
    commands = (Gfx *)func_1517F564((s32)commands);
    if (D_800BEAC0 == 0 && D_800BEAC1 == 0) {
        commands = (Gfx *)func_1508FD38((s32)commands);
    }
    commands = (Gfx *)func_151674F8(commands, 3, 0, 0);
    commands = (Gfx *)func_151674F8(commands, 3, 0, 1);
    return func_15096934((s32)commands);
}

// Matched with guarded frame-size and viewport-address register normalization.
s32 func_15019BB8(Gfx *arg0, s32 arg1) {
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
    return (s32)func_151674F8((void *)temp_v0, 4, sp2A, 1);
}

/* Set up a view's overlay matrices and append the category/mode-5 passes. */
s32 func_15019CC8(Gfx *commands, s32 view) {

    gSPViewport(commands++, D_800BE628 + ((u32)view * 0x180) + (D_800BE9C0 * 0x10) + 0x40);
    commands = (Gfx *)func_1501A490((s32)commands, (s16)view, 0, 0, 0, 0);
    gSPMatrix(commands++, &D_80089470, G_MTX_MODELVIEW | G_MTX_LOAD | G_MTX_NOPUSH);
    gSPMatrix(commands++, D_800BE628 + (((u32)view * 3) << 7) + (D_800BE9C0 * 0x40) + 0x100,
        G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH);
    if (D_800BE9F0 == 0x1D) {
        commands = func_1502BAD0(commands, 6, (s16)view);
    }
    commands = (Gfx *)func_151674F8(commands, 5, 0, 0);
    commands = (Gfx *)func_151674F8(commands, 5, 0, 1);
    gSPMatrix(commands++, D_800BE628 + ((((u32)view << 2) - (u32)view) << 7) + (D_800BE9C0 * 0x40) + 0x100,
        G_MTX_PROJECTION | G_MTX_LOAD | G_MTX_NOPUSH);
    /* The legacy pointer declaration labels the page-pointer table itself. */
    gSPMatrix(commands++, ((u32 *)&D_800DC2A0)[D_800BE9C0] + ((u32)view * 0x40),
        G_MTX_PROJECTION | G_MTX_MUL | G_MTX_NOPUSH);
    return (s32)commands;
}

s32 func_15019E60(Gfx *arg0) {
    if (D_80082FA0 != 0) {
        D_80082FA4 = D_80082FA0 + 1;
        gSPViewport(arg0++, (D_80082FA4 * 0x180) + D_800BE628 + 64);
    } else {
        gSPViewport(arg0++, D_800BE628 + 64);
    }
    return func_15043384(func_151E8620(func_1501A490(arg0, 0xFF, 0, 0, 0, 0)));
}

/* Update frame steps, alternating phase and the ten-sample timing mean. */
void func_15019F20(void) {
    u8 historyIndex;
    u8 divisor;
    u32 total;
    f32 sum;
    s32 i;

    divisor = D_800BEA0C;
    D_800BEA08 = D_800BE9E4;
    if (divisor != 0) {
        if (divisor == 1) {
            D_800BE9E4 = 0;
            D_800BE5E0 = 0;
            D_800BE9A4 = 0.0f;
        } else {
            total = D_800BE610 + (u32)D_800BE9E4;
            D_800BE9A4 = (f32)D_800BE9E4 / (f32)(u32)divisor;
            D_800BE9E4 = (s32)D_800BE9A4;
            D_800BE9A4 *= 0.5f;
            if (total >= divisor) {
                D_800BE9E4 = total / divisor;
                /* Retail multiplies by total here, not by the divisor. */
                D_800BE610 = total - ((u32)D_800BE9E4 * total);
            } else {
                D_800BE610 = total;
                D_800BE9E4 = 0;
            }
        }
    } else {
        D_800BE9A4 = (f32)D_800BE9E4 * 0.5f;
    }
    D_800BE5E0 &= 1;
    D_800BE5E0 += (u32)D_800BE9E4;
    D_800BE9A0 = D_800BE5E0 >> 1;
    if (D_800BE9A4 != 0) {
        D_800BE9A8 = 1.0f / D_800BE9A4;
    } else {
        D_800BE9A4 = 0.0f;
        D_800BE9A8 = 0.0f;
    }
    D_800BE9AC += D_800BE9E4;
    D_800BE9B0 = (s32)D_800BE9AC % 30;
    historyIndex = D_800BE619;
    D_800BE5E8[historyIndex] = D_800BE9A4;
    D_800BE619 = historyIndex + 1;
    if (D_800BE619 == 10) {
        D_800BE619 = 0;
    }
    if (D_800BE61A < 10) {
        D_800BE61A++;
        D_800BE9B8 = D_800BE9A4;
        D_800BE9BC = D_800BE9A8;
    } else {
        sum = 0.0f;
        for (i = 0; i < 10; i++) {
            sum += D_800BE5E8[i];
        }
        D_800BE9B8 = sum * D_800968D0;
        if (D_800BE9B8 != 0) {
            D_800BE9BC = 1.0f / D_800BE9B8;
        } else {
            D_800BE9BC = 0.0f;
        }
    }
    func_150A019C();
}
