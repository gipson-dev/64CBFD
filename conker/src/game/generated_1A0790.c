#include <ultra64.h>

/* Non-matching placeholders for the text-only asm slice asm/1A0790.s. */

typedef struct {
    u16 fallbackValue;
    u16 selectedValue;
    u8 retained04[0x36];
    s16 firstRange;
    s16 secondRange;
    s16 thirdRange;
    s16 fourthRange;
    u8 red;
    u8 green;
    u8 blue;
    u8 alpha;
    s8 value;
} Generated1A0790State;

typedef struct {
    u8 red;
    u8 green;
    u8 blue;
    u8 alpha;
    s16 firstRange;
    s16 secondRange;
    s16 thirdRange;
    s16 fourthRange;
    u16 selectedValue;
    u16 fallbackValue;
} EnvironmentSnapshot151732E0;

extern Generated1A0790State *D_800B0DF0;
extern EnvironmentSnapshot151732E0 D_8008CC70;
extern s8 D_800DD2E0;
s32 func_151733E4();

/* Snapshot the live environment and select its initial provider row. */
void func_151732E0(s32 context) {
    s16 secondRange;
    s8 selection;

    secondRange = D_800B0DF0->secondRange;
    if ((D_800B0DF0->fourthRange == secondRange) && (secondRange == 0)) {
        D_800B0DF0->fourthRange = 100;
    }
    D_8008CC70.red = D_800B0DF0->red;
    D_8008CC70.green = D_800B0DF0->green;
    D_8008CC70.blue = D_800B0DF0->blue;
    D_8008CC70.alpha = D_800B0DF0->alpha;
    D_8008CC70.firstRange = D_800B0DF0->firstRange;
    D_8008CC70.secondRange = D_800B0DF0->secondRange;
    D_8008CC70.thirdRange = D_800B0DF0->thirdRange;
    D_8008CC70.fourthRange = D_800B0DF0->fourthRange;
    D_8008CC70.selectedValue = D_800B0DF0->selectedValue;
    D_8008CC70.fallbackValue = D_800B0DF0->fallbackValue;
    if (D_800B0DF0->value != -1) {
        D_800DD2E0 = 1;
        selection = D_800B0DF0->value;
        func_151733E4(selection, selection, context, 0, -1);
        return;
    }
    D_800DD2E0 = 0;
    func_151733E4(0, 0, context, 0, -1);
}

s32 func_151733D8(s32 arg0, s32 arg1) {
    return arg0;
}

s32 func_151733E4() {
    return 0;
}

extern u8 *D_800DBFF0;
extern u8 D_800DD2E4[], D_800DBEA8[];
/* Retail consumes five 32-bit arguments; the provider C body remains a placeholder. */
s32 func_151733E4();
/* Publish the selected three-byte state after updating its provider. */
void func_151738C4(s32 context) {
    u8 *state;

    if (D_800B0DF0->value == -1) {
        if (*(u32 *)(D_800DBFF0 + 0x5F0) & 1) {
            func_151733E4(6, 6, context, 0, -1);
            D_800DBEA8[0] = D_800DD2E4[0];
            D_800DBEA8[1] = D_800DD2E4[1];
            D_800DBEA8[2] = D_800DD2E4[2];
        } else {
            func_151733E4(0, 0, context, 0, -1);
            state = (u8 *)D_800B0DF0;
            D_800DBEA8[0] = state[5];
            D_800DBEA8[1] = state[6];
            D_800DBEA8[2] = state[7];
        }
    }
}

s8 func_15173994(s32 arg0) {
    return D_800B0DF0->value;
}
