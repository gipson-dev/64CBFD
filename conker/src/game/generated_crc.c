#include <ultra64.h>
#include "controller.h"

#ifdef __osContAddressCrc
#undef __osContAddressCrc
#endif
#ifdef __osContDataCrc
#undef __osContDataCrc
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/crc.s. */

u8 __osContAddressCrc(u16 addr) {
    return 0;
}

u8 __osContDataCrc(u8 *data) {
    return 0;
}
