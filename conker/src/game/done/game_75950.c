#include <ultra64.h>
#include "functions.h"
#include "variables.h"

// undo intrinsic
#pragma function sqrtf

#define PI 3.1415927410125732f

f32 func_150484A0(f32 arg0, f32 arg1) {
    f32 ret;
    f32 temp;

    if (arg0 == 0.0f) {
        if (arg1 >= 0.0f) {
            ret = 0.0f;
        } else {
            ret = D_80098DE0;
        }
    } else if (arg1 == 0.0f) {
        if (arg0 > 0.0f) {
            ret = D_80098DE4;
        } else {
            ret = D_80098DE8;
        }
    } else {
        ret = sqrtf((arg0 * arg0) + (arg1 * arg1));
        if (arg1 < arg0) {
            ret = func_15048360(arg1 / ret);
            if (arg0 < 0.0f) {
                ret = D_80098DEC - ret;
            }
        } else {
            temp = D_80098DF0 - func_15048360(arg0 / ret);
            ret = temp;
            if (arg1 < 0.0f) {
                ret = D_80098DF4 - temp;
            }
            if (ret < 0.0f) {
                ret += D_80098DF8;
            }
        }
    }
    return ret;
}
