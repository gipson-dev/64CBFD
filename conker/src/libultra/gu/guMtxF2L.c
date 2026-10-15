#include <ultra64.h>
#include "functions.h"
#include "variables.h"

/* Original unrolled converter: cvt.w.s follows the current FCSR rounding mode. */
#pragma GLOBAL_ASM("asm/nonmatchings/libultra/gu/guMtxF2L/guMtxF2L.s")
