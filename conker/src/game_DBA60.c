#include <ultra64.h>
s32 func_1509BE40(s32, ...);

#include "functions.h"
#include "variables.h"

/* Generated placeholder declarations. */
s32 func_150AE790();
void func_150AEB9C(u8 *);
/* End generated placeholder declarations. */

void func_150AE5B0(struct108 *arg0) {
    if ((D_800D2E4C->unk4 & 0x80) == 0) {
        if (func_1509BE40(0, 0x2000, 0xBB) != -1) {
            if (func_15123934(arg0, arg0->unk2C, 0, arg0->unk134, 8) != 0) {
                arg0->unk84 |= 0x1000000;
                func_151254F4(arg0, D_800CC335 - 1);
            }
        } else if (func_151239CC(arg0, 8) != 0) {
            func_151254F4(arg0, 0);
        }
    }
    arg0->unk84 &= -0x4001;
    if ((D_800D2E4C->unk1 & 4) == 0) {
        if (func_1509BE40(1, 0x2000, 0x95, func_1509BE40(0, 0x2014, 0xB7) | 0x2000) != 0) {
            arg0->unk84 |= 0x1000000;
            if (((arg0->unk2C & 1) != 0) && (func_15123934(arg0, arg0->unk2C, 0, arg0->unk134, 0) != 0)) {
                arg0->unk1B4 = 3;
                arg0->unk84 &= -5;
                func_15124B18(arg0);
            }
        } else if (func_151239CC(arg0, 0) != 0) {
            func_15124B18(arg0);
            arg0->unk84 &= 0xFEFFFFFF;
        }
    }
    if (func_1509BE40(1, 0x4082, 6, 0x9000) != 0) {
        arg0->unk84 |= 0x10000;
    } else {
        arg0->unk84 &= 0xFFFEFFFF;
    }
}


/* Non-matching C placeholders for asm/nonmatchings/game_DBA60/func_150AE790.s. */
s32 func_150AE790() {
    return 0;
}
typedef struct { u8 kind; u8 pad; s16 lifetime; } ChecksumRecordEntry;
extern s32 D_800886E0;
extern ChecksumRecordEntry *D_800886E4;
extern u32 D_15001B08[];
extern void func_15001A08(void);
/* Check the code window, then create a record for each configured entry. */
void func_150AEB9C(u8 *owner) {
    u32 checksum;
    u32 *cursor;
    s32 i;
    ChecksumRecordEntry *entry;
    u8 *record;
    if (owner != 0) {
        checksum = 0;
        cursor = (u32 *)func_15001A08;
        while ((u32)cursor < (u32)D_15001B08) {
            checksum = (checksum ^ *cursor++) << 1;
        }
        if (checksum != 0xB4E42D60U) {
            *(u32 *)(D_800DCE50 + 0x8C) = 0;
            *(u32 *)(D_800DCE50 + 0x22C) = 0;
        }
        for (i = 0; i < D_800886E0; i++) {
            entry = &D_800886E4[i];
            record = (u8 *)func_151491F4(entry->lifetime, 0, -1, 1, 0x27, 8, 0xff, 0);
            if (record == 0) break;
            *(u8 **)(record + 0x28) = owner;
            record[0x2C] = owner[0x3B];
            record[0x2D] = D_800886E4[i].kind;
        }
    }
}


void func_150AECCC(struct42 *arg0) {
    arg0->unk96 = arg0->unk96 + (arg0->unk94 * D_800BE9E4);
    if (arg0->unk96 >= 0x1401) {
        arg0->unk96 = 0x1400;
    }
    arg0->unk9E = arg0->unk9E - ((s32) arg0->unk96 >> 8);
    arg0->unkA4 = arg0->unkA4 + D_800BE9E4;
    if (arg0->unkA4 >= 0x1A) {
        arg0->unkA4 = 0x19;
    }
}

void func_150AED4C(struct114 *arg0) {
    arg0->unk34 += arg0->unk14 * D_800BE9E4;
    if (arg0->unk2A < arg0->unk34) {
        arg0->unk3A = 70;
        arg0->unk34 = arg0->unk2A;
    }
    arg0->unk36 = arg0->unk34;
}

// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_150AED9C(struct202 *arg0) {
    u8 *p;
    s32 val;

    p = (u8 *) arg0->unk98;
    val = arg0->unk1C * 8;
    if (val >= 0x100) {
        val = 0xFF;
    }
    p[0x1B] = val;
    if ((u8) val < 0) {
        return 0;
    }
    return 1;
}

s32 func_150AEDD8(struct202 *arg0) {
    if (arg0->unk1C < 0x20) {
        arg0->unk28 = arg0->unk1C * 8;
    }
    return 1;
}

/* Only the inline link's identity word and saved key are exposed. */
typedef struct {
    s32 value;
    u8 key;
} InlineOwnerIdentityDBA60;

/* Retarget the inline owner link, or release the owner for a matching event. */
void func_150AEDF8(struct260 *record, s32 eventAddress, u8 command) {
    u8 *owner = (u8 *)record;
    InlineOwnerIdentityDBA60 *state = (InlineOwnerIdentityDBA60 *)(owner + 0x28);
    u8 *event = (u8 *)eventAddress;
    s32 code = command;

    if (command == 0x2D) {
        s32 current = state->value;
        s32 first = *(s32 *)event;
        if (first == current) {
            state->value = *(s32 *)(event + 4);
            state->key = event[9];
        } else if (*(s32 *)(event + 4) == current) {
            state->value = first;
            state->key = event[8];
        }
    } else if (code == 0) {
        if (*(s32 *)event == state->value || state->key == event[4]) {
            func_1516972C((struct102 *)owner);
        }
    }
}
