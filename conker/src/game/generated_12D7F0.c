#include <ultra64.h>

/* Recovered C for asm/12D7F0.s; the remaining routine retains assembly. */

extern u8 D_800BE500[5], D_800DD405;
s32 func_150ADA20(void);
void func_151616D0(u8, u8, s32);
typedef struct SlotIdentifiers15100340 { u8 ids[5]; } SlotIdentifiers15100340;
extern SlotIdentifiers15100340 D_80088BC0;
/* Advance the five registered slot states for the primary view. */
void func_15100340(s32 view) {
    u32 random;
    SlotIdentifiers15100340 identifiers;
    s32 index;
    u32 chance;
    u8 *states;
    identifiers = D_80088BC0;

    if (view == 0) {
        D_800DD405++;
        states = D_800BE500;
        index = 0;
        do {
            chance = *states != 0 ? 70 : 35;
            random = (u32)func_150ADA20();
            if (random % 1000 < chance) {
                *states ^= 1;
                if (*states != 0) func_151616D0(identifiers.ids[index], 0x18, 0);
                else {
                    func_151616D0(identifiers.ids[index], 0x1C, 0);
                    func_151616D0(identifiers.ids[index], 0x17, 0);
                }
            }
            index++;
            states++;
        } while (index != 5);
    }
}

#pragma GLOBAL_ASM("asm/nonmatchings/generated_12D7F0/func_15100464.s")
