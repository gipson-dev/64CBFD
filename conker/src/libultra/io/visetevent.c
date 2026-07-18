#include <os_internal.h>

typedef struct {
    u16 state;
    u16 retraceCount;
    void *framep;
    OSViMode *modep;
    u32 control;
    OSMesgQueue *msgq;
    OSMesg msg;
} OSViContextEvent;

extern OSViContextEvent *D_8002BDE4;

void osViSetEvent(OSMesgQueue *mq, OSMesg msg, u32 retraceCount) {
    register u32 saveMask;

    saveMask = __osDisableInt();
    D_8002BDE4->msgq = mq;
    D_8002BDE4->msg = msg;
    D_8002BDE4->retraceCount = retraceCount;
    __osRestoreInt(saveMask);
}
