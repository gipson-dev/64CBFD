#include <ultra64.h>
#include "functions.h"
#include "variables.h"

/* Game's single-precision small-angle and full-period sine paths. */
f32 sinf(f32 angle) {
    f32 reduced, squared, polynomial, periods, result;
    s32 period, raw, exponent;

    raw = *(s32 *)&angle;
    exponent = (raw >> 22) & 0x1FF;
    if (exponent < 0xFF) {
        reduced = angle;
        if (exponent >= 0xE6) {
            squared = reduced * reduced;
            polynomial = ((D_80098D90[4] * squared + D_80098D90[3]) * squared +
                          D_80098D90[2]) * squared + D_80098D90[1];
            result = reduced + (reduced * squared) * polynomial;
            return result;
        }
        return angle;
    }
    if (exponent < 0x136) {
        reduced = angle;
        periods = reduced * D_80085EB0;
        period = (s32)(periods >= 0.0f ? periods + 0.5f : periods - 0.5f);
        periods = period;
        reduced = reduced - periods * D_80085EB4;
        reduced = reduced - periods * D_80085EB8;
        squared = reduced * reduced;
        polynomial = ((D_80098D90[4] * squared + D_80098D90[3]) * squared +
                      D_80098D90[2]) * squared + D_80098D90[1];
        result = reduced + (reduced * squared) * polynomial;
        if ((period & 1) == 0) {
            return result;
        }
        return -result;
    }
    if (angle != angle) {
        return D_8002C920;
    }
    return D_80085EBC;
}
