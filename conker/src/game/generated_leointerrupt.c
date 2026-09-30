#include <ultra64.h>
#include "controller.h"
#include "piint.h"
#include "osint.h"

extern OSPiHandle *D_80043B34;
extern OSIntMask D_8002BD1C;
extern __OSEventState D_80042910[OS_NUM_EVENTS];
extern OSThread *D_8002BDF8;
extern OSThread *func_10007A24(OSThread **queue);
extern void func_100079D8(OSThread **queue, OSThread *thread);

#ifdef __osLeoInterrupt
#undef __osLeoInterrupt
#endif
#ifdef __osLeoAbnormalResume
#undef __osLeoAbnormalResume
#endif
#ifdef __osLeoResume
#undef __osLeoResume
#endif

/* Non-matching C placeholders for C:/Users/grego/OneDrive/Desktop/.vscode/64CBFD/conker/asm/libultra/io/leointerrupt.s. */

s32 __osLeoInterrupt() {
    return 0;
}

void __osLeoResume(void);

void __osLeoAbnormalResume(void) {
    __OSTranxInfo *info = &D_80043B34->transferInfo;
    u32 pi_stat;

    pi_stat = IO_READ(PI_STATUS_REG);
    while (pi_stat & PI_STATUS_IO_BUSY) {
        pi_stat = IO_READ(PI_STATUS_REG);
    }
    IO_WRITE(LEO_BM_CTL, info->bmCtlShadow | LEO_BM_CTL_RESET);
    pi_stat = IO_READ(PI_STATUS_REG);
    while (pi_stat & PI_STATUS_IO_BUSY) {
        pi_stat = IO_READ(PI_STATUS_REG);
    }
    IO_WRITE(LEO_BM_CTL, info->bmCtlShadow);
    __osLeoResume();
    IO_WRITE(PI_STATUS_REG, PI_STATUS_CLR_INTR);
    D_8002BD1C |= OS_IM_PI;
}

void __osLeoResume(void) {
    __OSEventState *es = &D_80042910[OS_EVENT_PI];
    OSMesgQueue *mq = es->messageQueue;
    s32 last;

    if ((mq == NULL) || MQ_IS_FULL(mq)) {
        return;
    }

    last = (mq->first + mq->validCount) % mq->msgCount;
    mq->msg[last] = es->message;
    mq->validCount++;

    if (mq->mtqueue->next != NULL) {
        func_100079D8(&D_8002BDF8, func_10007A24(&mq->mtqueue));
    }
}
