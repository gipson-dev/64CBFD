#include <ultra64.h>
#include "controller.h"

#include "functions.h"
#include "variables.h"

void func_160018BC(void);

// synchronous controller poll for the crash debugger: packs and sends the
// PIF read command, busy-waiting on osGetCount instead of the OS event
// queue (the debugger can't rely on the scheduler after a crash)
s32 func_16001700(void) {
    s32 ret;
    u8 *fill;
    u8 *end;
    s32 t;
    u32 timeout;

    if (__osContLastCmd != CONT_CMD_READ_BUTTON) {
        func_160018BC();
        func_160019A8(OS_WRITE, &__osContPifRam);
        t = 0;
        timeout = osGetCount() + 0x30D40;
        while (osGetCount() < timeout) {
            t = func_160016F4(t);
        }
        func_160016F4(t);
    }

    t = 0;
    do {
        ((u32 *) &__osContPifRam)[t] = CONT_CMD_NOP;
        t++;
    } while (t < ARRLEN(__osContPifRam.ramarray) + 1);
    __osContPifRam.pifstatus = 0;
    ret = func_160019A8(OS_READ, &__osContPifRam);
    __osContLastCmd = CONT_CMD_READ_BUTTON;
    t = 0;
    timeout = osGetCount() + 0xC3500;
    while (osGetCount() < timeout) {
        t = func_160016F4(t);
    }
    func_160016F4(t);
    return ret;
}
// __osContGetReadData - retail is compiled from the stock libultra source
// (by-value struct copy through a stack temp, which is what generates the
// lwl/lwr pairs), not the ects_proto pointer-walk shape
void func_16001830(OSContPad *data) {
    u8 *ptr;
    __OSContReadFormat requestformat;
    s32 i;

    ptr = (u8 *) &__osContPifRam;
    for (i = 0; i < __osMaxControllers; i++, ptr += sizeof(requestformat), data++) {
        requestformat = *(__OSContReadFormat *) ptr;
        data->errno = CHNL_ERR(requestformat);
        if (data->errno == 0) {
            data->button = requestformat.button;
            data->stick_x = requestformat.stick_x;
            data->stick_y = requestformat.stick_y;
        }
    }
}
// __osPackReadData - retail is compiled from the stock libultra source (the
// template struct lives on the stack and is copied per controller with
// swl/swr); note the zero-fill covers the full OSPifRam (16 words including
// pifstatus), one word more than stock libultra's ramarray-only loop
void func_160018BC(void) {
    u8 *ptr;
    __OSContReadFormat readformat;
    s32 i;

    ptr = (u8 *) &__osContPifRam;
    for (i = 0; i < ARRLEN(__osContPifRam.ramarray) + 1; i++) {
        ((u32 *) &__osContPifRam)[i] = 0;
    }
    __osContPifRam.pifstatus = CONT_CMD_EXE;
    readformat.dummy = CONT_CMD_NOP;
    readformat.txsize = CONT_CMD_READ_BUTTON_TX;
    readformat.rxsize = CONT_CMD_READ_BUTTON_RX;
    readformat.cmd = CONT_CMD_READ_BUTTON;
    readformat.button = 0xFFFF;
    readformat.stick_x = -1;
    readformat.stick_y = -1;
    for (i = 0; i < __osMaxControllers; i++) {
        *(__OSContReadFormat *) ptr = readformat;
        ptr += sizeof(__OSContReadFormat);
    }
    *ptr = CONT_CMD_END;
}

// another __osSiDeviceBusy function
s32 func_16001984()
{
    register u32 stat = IO_READ(SI_STATUS_REG);
    if (stat & (SI_STATUS_DMA_BUSY | SI_STATUS_RD_BUSY))
        return 1;
    return 0;
}

// very similar to __osSiRawStartDma
s32 func_160019A8(s32 direction, void *dramAddr) {
    if ((s32)dramAddr & 3) { // what is this checking?
        return -1;
    }
    if (func_16001984()) {
        return -1;
    }

    if (direction == OS_WRITE) {
        osWritebackDCache(dramAddr, 64);
    }

    IO_WRITE(SI_DRAM_ADDR_REG, osVirtualToPhysical(dramAddr));

    if (direction == OS_READ) {
        IO_WRITE(SI_PIF_ADDR_RD64B_REG, 0x1FC007C0);
    } else {
        IO_WRITE(SI_PIF_ADDR_WR64B_REG, 0x1FC007C0);
    }
    if (direction == OS_READ) {
        osInvalDCache(dramAddr, 64);
    }

    return 0;
}

void func_16001A64(void) {
}

s32 func_16001A6C(f32 arg0) {
    s32 tmp = *(s32*) &arg0;

    if ((tmp * 2) == 0) {
        return 0;
    }
    tmp = (tmp & 0x7F800000) >> 0x17;
    if ((tmp <= 0) || (tmp >= 255)) {
        return 1;
    }
    return 0;
}
