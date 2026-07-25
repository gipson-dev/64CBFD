#include <os_internal.h>
#include "controller.h"
#include "siint.h"

#ifdef osPfsInit2
#undef osPfsInit2
#endif
#ifdef func_151EF504
#undef func_151EF504
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/pfsinit2.s. */

s32 osPfsInit2(OSMesgQueue *queue, OSPfs *pfs, int channel)
{
    s32 ret;
    ret = 0;
    __osSiGetAccess();
    ret = __osPfsGetStatus(queue, channel);
    __osSiRelAccess();
    if (ret != 0)
        return ret;

    pfs->queue = queue;
    pfs->channel = channel;
    pfs->status = 0;
    ERRCK(__osGetId(pfs));

    ret = osPfsChecker(pfs);
    pfs->status |= PFS_INITIALIZED;
    return ret;
}

s32 func_151EF504(OSMesgQueue *queue, int channel)
{
    s32 ret;
    OSMesg dummy;
    u8 pattern;
    OSContStatus data[MAXCONTROLLERS];

    ret = 0;
    __osPfsRequestData(CONT_CMD_REQUEST_STATUS);
    ret = __osSiRawStartDma(OS_WRITE, &__osPfsPifRam);
    osRecvMesg(queue, &dummy, OS_MESG_BLOCK);
    ret = __osSiRawStartDma(OS_READ, &__osPfsPifRam);
    osRecvMesg(queue, &dummy, OS_MESG_BLOCK);
    __osPfsGetInitData(&pattern, data);

    if (((data[channel].status & CONT_CARD_ON) != 0) &&
        ((data[channel].status & CONT_CARD_PULL) != 0)) {
        return PFS_ERR_NEW_PACK;
    }
    if ((data[channel].errno != 0) ||
        ((data[channel].status & CONT_CARD_ON) == 0)) {
        return PFS_ERR_NOPACK;
    }
    if ((data[channel].status & CONT_ADDR_CRC_ER) != 0) {
        return PFS_ERR_CONTRFAIL;
    }
    return ret;
}
