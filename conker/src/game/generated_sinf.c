#include <ultra64.h>

extern const f64 D_8002C8D0[];
extern const f64 D_8002C8F8;
extern const f64 D_8002C900;
extern const f64 D_8002C908;
extern const f32 D_8002C910;
extern const f32 D_8002C920;

/* Init's SDK sine implementation; Game's sinf has a separate source owner. */
f32 __sinf(f32 x)
{
    f64 dx, xsq, poly;
    f64 dn;
    s32 n;
    f64 result;
    s32 ix, xpt;

    ix = *(s32 *)&x;
    xpt = ix >> 22;
    xpt &= 0x1FF;

    if (xpt < 0xFF) {
        dx = x;
        if (xpt >= 0xE6) {
            xsq = dx * dx;
            poly = ((D_8002C8D0[4] * xsq + D_8002C8D0[3]) * xsq +
                    D_8002C8D0[2]) * xsq + D_8002C8D0[1];
            result = dx + (dx * xsq) * poly;
            return (f32)result;
        }
        return x;
    }

    if (xpt < 0x136) {
        dx = x;
        dn = dx * D_8002C8F8;
        n = (s32)(dn >= 0.0 ? dn + 0.5 : dn - 0.5);
        dn = n;
        dx = dx - dn * D_8002C900;
        dx = dx - dn * D_8002C908;
        xsq = dx * dx;
        poly = ((D_8002C8D0[4] * xsq + D_8002C8D0[3]) * xsq +
                D_8002C8D0[2]) * xsq + D_8002C8D0[1];
        result = dx + (dx * xsq) * poly;
        if ((n & 1) == 0) {
            return (f32)result;
        }
        return -(f32)result;
    }

    if (x != x) {
        return D_8002C920;
    }
    return D_8002C910;
}
