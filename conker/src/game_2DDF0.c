#include <ultra64.h>

#include "functions.h"
#include "variables.h"

extern u16 D_800D9E70[];
extern u8 D_800D9E88[], D_800D9E98[], D_800D9EA8[];
extern u8 D_800D9EB4[], D_800D9EB8[];
extern u8 D_800D9EB7, D_800D9EC4;
extern u8 D_800A2CE8[], D_800A2CEC[], D_800A2D04[];


void func_15000940(s32);

/* Initialize four palette-state rows from the selected RGB presets. */
void func_15000940(s32 unused) {
    u8 *selectors;
    u8 *first;
    u8 *second;
    u8 *third;
    u16 *zeroHalf;
    u8 *firstOut;
    u8 *secondOut;
    u8 *thirdOut;
    u8 *zeroByte;
    u8 *common;
    u16 *halfCursor;
    u8 *firstCursor;
    u8 *firstSource;
    u8 *secondCursor;
    u8 *secondSource;
    u8 *thirdSource;
    u8 *thirdCursor;
    u8 *zeroCursor;
    u8 thirdValue;
    u8 firstValue;
    u8 secondValue;

    selectors = D_800A2CD0[D_800B0DF0->unk29];
    first = &D_800A2CE8[selectors[0] * 3];
    second = &D_800A2CEC[selectors[1] * 3];
    third = &D_800A2D04[selectors[2] * 3];
    zeroHalf = D_800D9E70;
    firstOut = D_800D9E88;
    secondOut = D_800D9E98;
    thirdOut = D_800D9EA8;
    zeroByte = D_800D9EB8;

    do {
        common = D_800D9EB4;
        halfCursor = zeroHalf;
        firstCursor = firstOut;
        firstSource = first;
        secondCursor = secondOut;
        secondSource = second;
        thirdSource = third;
        thirdCursor = thirdOut;
        zeroCursor = zeroByte;

        do {
            thirdValue = *thirdSource++;
            firstValue = *firstSource++;
            secondValue = *secondSource++;

            *halfCursor++ = 0;
            *zeroCursor++ = 0;
            *common++ = thirdValue;
            *thirdCursor++ = thirdValue;
            *firstCursor++ = firstValue;
            *secondCursor++ = secondValue;
        } while (common != &D_800D9EB7);
        zeroByte += 3;
        zeroHalf += 3;
        firstOut += 3;
        secondOut += 3;
        thirdOut += 3;
    } while (zeroByte != &D_800D9EC4);
}
