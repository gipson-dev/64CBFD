#include <ultra64.h>
#include "controller.h"

#ifdef osMotorStop
#undef osMotorStop
#endif
#ifdef osMotorStart
#undef osMotorStart
#endif
#ifdef _MakeMotorData
#undef _MakeMotorData
#endif
#ifdef osMotorInit
#undef osMotorInit
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/motor.s. */

s32 osMotorStop(OSPfs *arg0) {
    return 0;
}

s32 osMotorStart(OSPfs *arg0) {
    return 0;
}

s32 _MakeMotorData() {
    return 0;
}

s32 osMotorInit(OSMesgQueue *arg0, OSPfs *arg1, int arg2) {
    return 0;
}
