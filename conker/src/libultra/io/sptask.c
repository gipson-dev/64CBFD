#include <ultra64.h>

extern OSTask D_80036B60;

#define VIRTUAL_TO_PHYSICAL(ptr)          \
    if ((ptr) != NULL) {                  \
        (ptr) = (void *)osVirtualToPhysical(ptr); \
    } (void)0

OSTask *_VirtualToPhysicalTask(OSTask *intp) {
    OSTask *tp = &D_80036B60;

    bcopy(intp, tp, sizeof(OSTask));
    VIRTUAL_TO_PHYSICAL(tp->t.ucode);
    VIRTUAL_TO_PHYSICAL(tp->t.ucode_data);
    VIRTUAL_TO_PHYSICAL(tp->t.dram_stack);
    VIRTUAL_TO_PHYSICAL(tp->t.output_buff);
    VIRTUAL_TO_PHYSICAL(tp->t.output_buff_size);
    VIRTUAL_TO_PHYSICAL(tp->t.data_ptr);
    VIRTUAL_TO_PHYSICAL(tp->t.yield_data_ptr);
    return tp;
}

void osSpTaskLoad(OSTask *intp)
{

    OSTask *tp;
    tp = _VirtualToPhysicalTask(intp);
    if (tp->t.flags & OS_TASK_YIELDED)
    {
        tp->t.ucode_data = tp->t.yield_data_ptr;
        tp->t.ucode_data_size = tp->t.yield_data_size;
        intp->t.flags &= ~OS_TASK_YIELDED;
        if (tp->t.flags & OS_TASK_LOADABLE)
          tp->t.ucode = (u64 *)IO_READ((u32)intp->t.yield_data_ptr + OS_YIELD_DATA_SIZE - 4);
    }
    osWritebackDCache(tp, sizeof(OSTask));
    __osSpSetStatus(SP_CLR_YIELD | SP_CLR_YIELDED | SP_CLR_TASKDONE | SP_SET_INTR_BREAK);
    while (__osSpSetPc(SP_IMEM_START) == -1)
        ;

    while (__osSpRawStartDma(1, (SP_IMEM_START - sizeof(*tp)), tp,
                 sizeof(OSTask)) == -1)
        ;

    while (__osSpDeviceBusy())
        ;

    while (__osSpRawStartDma(1, SP_IMEM_START, tp->t.ucode_boot,
                 tp->t.ucode_boot_size) == -1)
        ;
}

void osSpTaskStartGo(OSTask *tp) {
    while(__osSpDeviceBusy())
        ;
    __osSpSetStatus(SP_SET_INTR_BREAK | SP_CLR_SSTEP | SP_CLR_BROKE | SP_CLR_HALT);
}
