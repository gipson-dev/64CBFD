#include <ultra64.h>
#include "functions.h"
#include "variables.h"

extern f32 D_80085EA0, D_80085EA4, D_80085EA8, D_80085EAC;
extern f32 D_80098D70[];

/* Game's single-precision half-period reduction and sine polynomial. */
f32 cosf(f32 angle) {
    f32 absolute, reduced, squared, polynomial, periods, result;
    s32 period, raw, exponent;

    raw = *(s32 *)&angle;
    exponent = (raw >> 22) & 0x1FF;
    if (exponent < 0x136) {
        absolute = angle > 0 ? angle : -angle;
        reduced = absolute;
        periods = reduced * D_80085EA0 + 0.5f;
        period = (s32)(periods >= 0.0f ? periods + 0.5f : periods - 0.5f);
        periods = period;
        periods -= 0.5f;
        reduced = reduced - periods * D_80085EA4;
        reduced = reduced - periods * D_80085EA8;
        squared = reduced * reduced;
        polynomial = ((D_80098D70[4] * squared + D_80098D70[3]) * squared +
                      D_80098D70[2]) * squared + D_80098D70[1];
        result = reduced + (reduced * squared) * polynomial;
        if ((period & 1) == 0) {
            return result;
        }
        return -result;
    }
    if (angle != angle) {
        return D_8002C920;
    }
    return D_80085EAC;
}
