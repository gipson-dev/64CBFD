#include <ultra64.h>
#include "controller.h"
#include "osint.h"
#include "viint.h"

#ifdef osCreateViManager
#undef osCreateViManager
#endif
#ifdef viMgrMain
#undef viMgrMain
#endif

extern OSDevMgr D_8002AB70;
extern OSThread D_80036BA0;
extern OSMesgQueue D_80037DD0;
extern OSMesg D_80037DE8[5];
extern OSIoMesg D_80037E00;
extern OSIoMesg D_80037E18;
void __osTimerServicesInit(void);
void __osViInit(void);
void viMgrMain(void *arg);

void osCreateViManager(OSPri pri) {
    u32 savedMask;
    OSPri oldPri;
    OSPri myPri;

    if (D_8002AB70.active) {
        return;
    }

    __osTimerServicesInit();
    osCreateMesgQueue(&D_80037DD0, D_80037DE8, 5);
    D_80037E00.hdr.type = OS_MESG_TYPE_VRETRACE;
    D_80037E00.hdr.pri = OS_MESG_PRI_NORMAL;
    D_80037E00.hdr.retQueue = NULL;
    D_80037E18.hdr.type = OS_MESG_TYPE_COUNTER;
    D_80037E18.hdr.pri = OS_MESG_PRI_NORMAL;
    D_80037E18.hdr.retQueue = NULL;
    osSetEventMesg(OS_EVENT_VI, &D_80037DD0, &D_80037E00);
    osSetEventMesg(OS_EVENT_COUNTER, &D_80037DD0, &D_80037E18);

    oldPri = -1;
    myPri = osGetThreadPri(NULL);
    if (myPri < pri) {
        oldPri = myPri;
        osSetThreadPri(NULL, pri);
    }

    savedMask = __osDisableInt();
    D_8002AB70.active = TRUE;
    D_8002AB70.thread = &D_80036BA0;
    D_8002AB70.cmdQueue = &D_80037DD0;
    D_8002AB70.evtQueue = &D_80037DD0;
    D_8002AB70.acsQueue = NULL;
    D_8002AB70.dma = NULL;
    D_8002AB70.edma = NULL;
    osCreateThread(&D_80036BA0, 0, viMgrMain, &D_8002AB70,
                   (u8 *)D_80037DE8 - sizeof(D_80037DD0), pri);
    __osViInit();
    osStartThread(&D_80036BA0);
    __osRestoreInt(savedMask);

    if (oldPri != -1) {
        osSetThreadPri(NULL, oldPri);
    }
}

void viMgrMain(void *arg) {
    __OSViContext *vc;
    OSDevMgr *dm;
    OSIoMesg *mb;
    static u16 retrace;
    s32 first;
    u32 count;

    mb = NULL;
    first = 0;
    vc = (__OSViContext *)osPiGetDeviceType();
    retrace = vc->retraceCount;
    if (retrace == 0) {
        retrace = 1;
    }
    dm = (OSDevMgr *)arg;

    while (TRUE) {
        osRecvMesg(dm->evtQueue, (OSMesg *)&mb, OS_MESG_BLOCK);
        switch (mb->hdr.type) {
            case OS_MESG_TYPE_VRETRACE:
                __osViSwapContext();
                retrace--;
                if (retrace == 0) {
                    vc = (__OSViContext *)osPiGetDeviceType();
                    if (vc->msgq != NULL) {
                        osSendMesg(vc->msgq, vc->msg, OS_MESG_NOBLOCK);
                    }
                    retrace = vc->retraceCount;
                }

                __osViIntrCount++;
                if (first) {
                    count = osGetCount();
                    __osCurrentTime = count;
                    first = 0;
                }

                count = __osBaseCounter;
                __osBaseCounter = osGetCount();
                count = __osBaseCounter - count;
                __osCurrentTime = __osCurrentTime + count;
                break;

            case OS_MESG_TYPE_COUNTER:
                __osTimerInterrupt();
                break;
        }
    }
}
