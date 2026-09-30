#include <ultra64.h>
extern s32 D_8008743C[];
extern u8 *D_800D2FB0;
extern u8 D_800D2E70[];

/* Non-matching placeholders for the text-only asm slice asm/C9EC0.s. */

void func_1509CCB4();
s32 func_1509CE64();

extern u8 D_8008743A[];

typedef struct {
    s32 field0;
    s32 field4;
    u16 field8;
    u8 padA[0xA];
} GeneratedC9EC0Entry;

extern GeneratedC9EC0Entry D_80087430[];
extern GeneratedC9EC0Entry D_80088420[];

s32 func_1509CA10(register s32 arg0) {
    return D_80087430[arg0].field0;
}

u16 func_1509CA30(register s32 arg0) {
    return D_80087430[arg0].field8;
}

s32 func_1509CA50(s32 arg0) {
    return *(u16 *) (D_8008743A + arg0 * 0x14) & 0xFFF;
}

s32 func_1509CA78(register s32 arg0) {
    return D_80087430[arg0].field4;
}

s32 func_1509CA98() {
    return 0;
}

s32 func_1509CB68(void) {
    GeneratedC9EC0Entry *end = D_80088420;
    s32 count = 0;
    GeneratedC9EC0Entry *entry = D_80087430;

    do {
        if (entry[0].field0 != 0) {
            count++;
        }
        if (entry[1].field0 != 0) {
            count++;
        }
        if (entry[2].field0 != 0) {
            count++;
        }
        if (entry[3].field0 != 0) {
            count++;
        }
        entry += 4;
    } while (entry != end);

    return count;
}

s32 func_1509CBD4() {
    return 0;
}

void func_1509CC94(s32 arg0) {
    func_1509CCB4(arg0);
}

void func_1509CCB4(s32 arg0) {
    func_1509CE64(*(s32 *) ((u8 *) D_8008743C + arg0 * 20), func_1509CCB4);
}

s32 func_1509CCF4() {
    return 0;
}

// Matched with guarded loop-invariant allocation normalization.
void func_1509CDDC(s32 arg0) {
    s32 changes;
    s32 index;
    u8 *state;

    func_1509CCF4(arg0);
    do {
        changes = 0;
        state = D_800D2E70;
        index = 0;
        do {
            if (*state == 3) {
                changes += func_1509CCF4(index);
            }
            index++;
            state++;
        } while (index != 0xCC);
    } while (changes != 0);
}

s32 func_1509CE64() {
    return 0;
}

s32 func_1509CF28() {
    return 0;
}

// Matched with guarded call-argument lifetime normalization.
void func_1509D054(void) {
    u8 *temp_v0 = D_800D2FB0;

    if (temp_v0 != 0) {
        func_10004074(temp_v0);
        D_800D2FB0 = 0;
    }
}

s32 func_1509D08C() {
    return 0;
}

s32 func_1509D180() {
    return 0;
}

s32 func_1509D780() {
    return 0;
}

s32 func_1509D8FC() {
    return 0;
}

s32 func_1509DBBC() {
    return 0;
}
