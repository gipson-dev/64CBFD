#include <ultra64.h>
extern u8 D_80084064;
extern u64 D_8002BD10;
extern OSTimer D_800BE6E0;
extern OSMesgQueue D_8003B218;
extern u8 D_800BE93C[];
extern u8 D_80084060[];

/* Non-matching placeholders for the text-only asm slice asm/48FD0.s. */

void func_1501BB20(void) {
    if (D_80084064 != 0) {
        osSetTimer(&D_800BE6E0, (25 * D_8002BD10) / 1000000, 0,
            &D_8003B218, (OSMesg)6);
        D_80084064 = 0;
    }
}

s32 func_1501BBB8() {
    return 0;
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_48FD0/func_1501C010.s")

#pragma GLOBAL_ASM("asm/nonmatchings/generated_48FD0/func_1501C0F0.s")

void func_1501C17C(arg0)
u8 arg0;
{
    u8 idx = D_80084060[arg0];

    if (idx < 4) {
        D_800BE93C[idx] = 0;
    }
}

s32 func_1501C1B0() {
    return 0;
}

void func_1501C53C(void) {
    s32 i = 0;

    do {
        func_1501C17C(i & 0xFF);
        i += 1;
        i = i & 0xFF;
    } while (i < 4);
}

extern s8 D_80082BB4, D_800BE3EC;
extern u8 D_80084068;
extern OSMesgQueue D_800BE900;
extern u8 *D_800BE3F0;
s32 func_151DCFD8(s32);
s32 func_151DD460(OSMesgQueue *);
void func_150064E0(void);
s32 func_15006590(s32);
s32 func_15006BEC(s32);
void func_1500707C(s32);
void func_15007168(void);
void func_1500727C(void);
void func_15007360(void);
void func_15007440(void);
void func_15007558(void);
void func_10004074(void *);

/* Poll EEPROM work, dispatch a pending request and release its staging buffer. */
void func_1501C57C(void) {
    s32 delay;
    func_151DCFD8(0);
    if (D_80082BB4 != 0) {
        if (D_80084068 != EEPROM_TYPE_16K) {
            D_80084068 = func_151DD460(&D_800BE900);
        }
        if (D_80084068 != EEPROM_TYPE_16K) {
            switch (D_80082BB4) {
                case 1: break;
                case 2: break;
                case 3: break;
                case 4: break;
                case 5: break;
                case 6: break;
                case 7: break;
            }
            delay = 19; while (1) { if (delay <= 0) break; delay--; }
            switch (D_80082BB4) {
                case 1: func_150064E0(); break;
                case 4: func_15007168(); break;
            }
            D_80082BB4 = 0;
        } else {
            switch (D_80082BB4) {
                case 1: func_15006590(D_800BE3EC); break;
                case 2: func_15006BEC(D_800BE3EC); break;
                case 3: func_1500707C(D_800BE3EC); break;
                case 4: func_1500727C(); break;
                case 5: func_15007360(); break;
                case 6: func_15007440(); break;
                case 7: func_15007558(); break;
            }
            D_80082BB4 = 0;
            if (D_800BE3F0 != NULL) {
                func_10004074(D_800BE3F0 - 8);
                D_800BE3F0 = NULL;
            }
        }
    }
}

