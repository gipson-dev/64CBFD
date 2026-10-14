#include <ultra64.h>
#include "functions.h"
#include "variables.h"

typedef void (*GameModeCallback)(void);
extern GameModeCallback D_80082BD0;
extern GameModeCallback D_80082BD4;
extern s32 D_800DD1B0;

/* Function declarations. */
void func_15008930(s32 mode);
/* End function declarations. */

/* Clear the selected column range in both 104-entry rows. */
void func_15008870(s32 mode) {
    s32 lo;
    s32 hi;
    s32 row;
    s32 i;

    lo = 0;
    hi = 0x68;
    if (mode == 1) {
        hi = 0x65;
    } else if (mode == 2) {
        lo = 0x65;
    }

    for (row = 0; row != 2; row++) {
        for (i = lo; i < hi; i++) {
            *(s32 *) (D_800DCE50 + row * 0x1A0 + i * 4) = 0;
        }
    }
}
void func_15008930(s32 mode) {
    GameModeCallback *selected;
    GameModeCallback *cursor;
    s32 count;
    s32 index;

    if (mode == 1) {
        selected = &D_80082BD0;
        count = 1;
    } else if (mode == 2) {
        selected = &D_80082BD4;
        count = 1;
    } else {
        count = 0;
    }
    index = 0;
    if (count > 0) {
        cursor = selected;
        do {
            (*cursor)();
            index++;
            cursor++;
        } while (index != count);
    }
    D_800DD1B0 = -1;
}
