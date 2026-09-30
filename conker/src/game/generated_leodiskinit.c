#include <ultra64.h>
#include "controller.h"

extern OSPiHandle D_80043AC0;
extern OSPiHandle *D_80043B34;
extern OSPiHandle *D_8002AB6C;

#ifdef osLeoDiskInit
#undef osLeoDiskInit
#endif

/* Recovered from the retail libultra disk initializer. */

OSPiHandle *osLeoDiskInit(void) {
    u32 saveMask;

    D_80043AC0.type = DEVICE_TYPE_64DD;
    D_80043AC0.baseAddress = PHYS_TO_K1(PI_DOM2_ADDR1);
    D_80043AC0.latency = 3;
    D_80043AC0.pulse = 6;
    D_80043AC0.pageSize = 6;
    D_80043AC0.relDuration = 2;

    IO_WRITE(PI_BSD_DOM2_LAT_REG, D_80043AC0.latency);
    IO_WRITE(PI_BSD_DOM2_PWD_REG, D_80043AC0.pulse);
    IO_WRITE(PI_BSD_DOM2_PGS_REG, D_80043AC0.pageSize);
    IO_WRITE(PI_BSD_DOM2_RLS_REG, D_80043AC0.relDuration);
    bzero(&D_80043AC0.transferInfo, sizeof(__OSTranxInfo));

    saveMask = __osDisableInt();
    D_80043AC0.next = D_8002AB6C;
    D_8002AB6C = &D_80043AC0;
    D_80043B34 = &D_80043AC0;
    __osRestoreInt(saveMask);

    return &D_80043AC0;
}
