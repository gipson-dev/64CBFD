#include <ultra64.h>
#include <PR/os_internal.h>

#include "functions.h"
#include "variables.h"

typedef struct {
    u32 inst1;
    u32 inst2;
    u32 inst3;
    u32 inst4;
} ExceptionVector;

extern ExceptionVector func_100071D0[];
extern s32 __osLeoInterrupt(void);

void __osInitialize_common(void) {
    u32 pifData;
    u32 clock = 0;

    D_800428E0 = 1;
    __osSetSR(__osGetSR() | 0x20000000);
    __osSetFpcCsr(0x01000800);

    while (__osSiRawReadIo(0x1FC007FC, &pifData) != 0) {}
    while (__osSpRawWriteIo(0x1FC007FC, pifData | 8) != 0) {}

    *(ExceptionVector *)0x80000000 = *func_100071D0;
    *(ExceptionVector *)0x80000080 = *func_100071D0;
    *(ExceptionVector *)0x80000100 = *func_100071D0;
    *(ExceptionVector *)0x80000180 = *func_100071D0;

    osWritebackDCache((void *)0x80000000, 0x190);
    osInvalICache((void *)0x80000000, 0x190);
    osMapTLBRdb();

    osPiRawReadIo(4, &clock);
    clock &= ~0xF;
    if (clock != 0) {
        osClockRate = clock;
    }
    osClockRate = osClockRate * 3 / 4;

    if (D_8000030C == 0) {
        bzero(D_8000031C, 0x40);
    }

    while ((IO_READ(PI_STATUS_REG) & (PI_STATUS_DMA_BUSY | PI_STATUS_IO_BUSY)) != 0) {}

    if ((IO_READ(0x05000508) & 0xFFFF) == 0) {
        D_8002BD20 = 1;
        __osSetHWIntrRoutine(1, __osLeoInterrupt);
    } else {
        D_8002BD20 = 0;
    }
}
