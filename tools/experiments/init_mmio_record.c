typedef unsigned int u32;
typedef unsigned short u16;

typedef struct {
    u32 address;
    u16 value;
} InitMmioRecord;

typedef char GuestAddressWidth[(sizeof(void *) == 4) ? 1 : -1];
typedef char GuestWordWidth[(sizeof(u32) == 4) ? 1 : -1];
typedef char GuestHalfWidth[(sizeof(u16) == 2) ? 1 : -1];

const u32 init_mmio_record_layout[] = {
    sizeof(InitMmioRecord),
    (u32)&((InitMmioRecord *)0)->address,
    (u32)&((InitMmioRecord *)0)->value
};

#if MMIO_SHAPE == 1
extern u32 D_80038070;
extern u16 D_80038074;
#elif MMIO_SHAPE == 2 || MMIO_SHAPE == 3
extern volatile InitMmioRecord D_80038070;
#else
#error Unknown MMIO_SHAPE
#endif

/* An isolated record-view hypothesis, not a production type declaration. */
void func_100038E0(void) {
#if MMIO_SHAPE == 1
    *(volatile u32 *)&D_80038070 = 0xBC000C02;
    *(volatile u16 *)&D_80038074 = 0x4040;
    *(volatile u16 *)0xBC000C02 = 0x4040;
#elif MMIO_SHAPE == 2
    D_80038070.address = 0xBC000C02;
    D_80038070.value = 0x4040;
    *(volatile u16 *)0xBC000C02 = 0x4040;
#elif MMIO_SHAPE == 3
    volatile InitMmioRecord *record = &D_80038070;
    volatile u16 *target = (volatile u16 *)0xBC000C02;
    record->address = (u32)target;
    record->value = 0x4040;
    *target = 0x4040;
#endif
}
