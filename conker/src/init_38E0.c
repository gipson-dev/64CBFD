#include <ultra64.h>

#include "functions.h"
#include "variables.h"


s32 func_100038E0(void) {
    D_80038070 = 0xBC000C02;
    D_80038074 = 0x4040;
    *(volatile u16 *)0xBC000C02 = 0x4040;
    return 0xBC000C02;
}

s32 func_1000390C(void) {
    return 0;
}
