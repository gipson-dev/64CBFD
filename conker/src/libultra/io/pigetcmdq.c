#include <os_internal.h>

extern OSDevMgr D_8002AB50;

OSMesgQueue *osPiGetCmdQueue(void) {
    if (!D_8002AB50.active) {
        return 0;
    }
    return D_8002AB50.cmdQueue;
}
