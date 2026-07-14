#include <ultra64.h>
#include "controller.h"

#include "functions.h"
#include "variables.h"

void func_160018BC(void);

// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
s32 func_16001700(void) {
    s32 sp24;
    u8 *fill;
    s32 s0;
    u32 target;

    if (__osContLastCmd != 1) {
        func_160018BC();
        func_160019A8(1, &__osContPifRam);
        s0 = 0;
        target = osGetCount() + 0x30D40;
        if (osGetCount() < target) {
            do {
                s0 = func_160016F4(s0);
            } while (osGetCount() < target);
        }
        func_160016F4(s0);
    }

    fill = (u8 *) &__osContPifRam;
    do {
        fill += 4;
        *(u32 *)(fill - 4) = 0xFF;
    } while (fill < (u8 *) &__osContLastCmd);

    D_80042A4C = 0;
    sp24 = func_160019A8(0, &__osContPifRam);
    __osContLastCmd = 1;
    s0 = 0;
    target = osGetCount() + 0xC3500;
    if (osGetCount() < target) {
        do {
            s0 = func_160016F4(s0);
        } while (osGetCount() < target);
    }
    func_160016F4(s0);
    return sp24;
}
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_16001830(OSContPad *arg0) {
    __OSContReadFormat *var_v0;
    s32 var_v1;

    var_v0 = (__OSContReadFormat *) &__osContPifRam;
    var_v1 = 0;
    if ((s32) __osMaxControllers > 0) {
        do {
            arg0->errno = (var_v0->rxsize & CHNL_ERR_MASK) >> 4;
            if (!arg0->errno) {
                arg0->button = var_v0->button;
                arg0->stick_x = var_v0->stick_x;
                arg0->stick_y = var_v0->stick_y;
            }
            var_v1 += 1;
            var_v0 = (__OSContReadFormat *)((u8 *) var_v0 + 8);
            arg0 = (OSContPad *)((u8 *) arg0 + 6);
        } while (var_v1 < (s32) __osMaxControllers);
    }
}
// builds the PIF controller-read command block (osContStartReadData equivalent)
// NON-MATCHING: ported from ects_proto (ECTS ROM build), not yet byte-verified for us
void func_160018BC(void) {
    u8 *fill;
    s32 n;
    s32 i;
    __OSContReadFormat template;
    __OSContReadFormat *dest;

    fill = (u8 *) &__osContPifRam;
    do {
        fill += 4;
        *(u32 *)(fill - 4) = 0;
    } while (fill < (u8 *) &__osContLastCmd);

    __osContPifRam.pifstatus = 1;
    template.dummy = 0xFF;
    template.txsize = 1;
    template.rxsize = 4;
    template.cmd = 1;
    template.button = 0xFFFF;
    template.stick_x = -1;
    template.stick_y = -1;

    n = __osMaxControllers;
    dest = (__OSContReadFormat *) &__osContPifRam;
    i = 0;
    if (n > 0) {
        do {
            i += 1;
            dest += 1;
            *(dest - 1) = template;
        } while (i < n);
    }
    *(u8 *) dest = 0xFE;
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
