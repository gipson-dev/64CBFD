#include <ultra64.h>
#include "functions.h"
#include "variables.h"

typedef void (*GameModeCallback)(void);
extern GameModeCallback D_80082BD0;
extern GameModeCallback D_80082BD4;
extern s32 D_800DD1B0;

/* Function declarations. */
s32 func_15008870();
void func_15008930(s32 mode);
/* End function declarations. */

// loops and loops
/* Non-matching C placeholders for asm/nonmatchings/game_35D20/func_15008870.s. */
s32 func_15008870() {
    return 0;
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
