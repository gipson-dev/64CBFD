#include <os_internal.h>

typedef struct {
    u16 state;
    u16 retraceCount;
    void *framep;
    OSViMode *modep;
    u32 control;
} OSViContextMode;

extern OSViContextMode *D_8002BDE4;

void osViSetMode(OSViMode *modep) {
    u32 saveMask;

    saveMask = __osDisableInt();
    D_8002BDE4->modep = modep;
    D_8002BDE4->state = 1;
    D_8002BDE4->control = D_8002BDE4->modep->comRegs.ctrl;
    __osRestoreInt(saveMask);
}
