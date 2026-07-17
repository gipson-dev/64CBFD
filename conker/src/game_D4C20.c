#include <ultra64.h>

#include "functions.h"
#include "variables.h"


// handwritten memset?
void func_150A7770(u8 *arg0, u8 arg1, s32 arg2) {
    do {
        *arg0++ = arg1;
    } while (--arg2 != 0);
}
