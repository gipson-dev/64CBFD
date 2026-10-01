#include <ultra64.h>

#include "functions.h"
#include "variables.h"

void func_10002E50(void *arg0) {
    OSIoMesg *message;
    OSMesg event;
    OSMesg access;
    OSDevMgr *manager;
    s32 result;

    manager = arg0;
    message = NULL;
    result = 0;

    while (1) {
        osRecvMesg(manager->cmdQueue, (OSMesg *)&message, OS_MESG_BLOCK);
        switch (message->hdr.type) {
        case OS_MESG_TYPE_DMAREAD:
            if (D_8003A572 != 0) {
                D_8003A575 = 1;
                osStopThread((OSThread *)&D_80035910);
                D_8003A575 = 0;
            }
            D_8003A573 = 1;
            osRecvMesg(manager->acsQueue, &access, OS_MESG_BLOCK);
            result = manager->dma(OS_READ, message->devAddr,
                                  message->dramAddr, message->size);
            break;

        case OS_MESG_TYPE_DMAWRITE:
            osRecvMesg(manager->acsQueue, &access, OS_MESG_BLOCK);
            result = manager->dma(OS_WRITE, message->devAddr,
                                  message->dramAddr, message->size);
            break;

        case OS_MESG_TYPE_EDMAREAD:
            osRecvMesg(manager->acsQueue, &access, OS_MESG_BLOCK);
            result = manager->edma(message->piHandle, OS_READ,
                                   message->devAddr, message->dramAddr,
                                   message->size);
            break;

        case OS_MESG_TYPE_EDMAWRITE:
            osRecvMesg(manager->acsQueue, &access, OS_MESG_BLOCK);
            result = manager->edma(message->piHandle, OS_WRITE,
                                   message->devAddr, message->dramAddr,
                                   message->size);
            break;

        case OS_MESG_TYPE_LOOPBACK:
            osSendMesg(message->hdr.retQueue, (OSMesg)message,
                       OS_MESG_NOBLOCK);
            result = -1;
            break;

        default:
            result = -1;
            break;
        }

        if (result == 0) {
            osRecvMesg(manager->evtQueue, &event, OS_MESG_BLOCK);
            osSendMesg(message->hdr.retQueue, (OSMesg)message,
                       OS_MESG_NOBLOCK);
            osSendMesg(manager->acsQueue, NULL, OS_MESG_NOBLOCK);
            if (message->hdr.type == OS_MESG_TYPE_DMAREAD) {
                D_8003A573 = 0;
            }
        }
    }
}
