#include <ultra64.h>

/* Partially recovered text-only slice asm/197C20.s. */

s32 func_1516A770(u8 *arg0) {
    s32 count = 1;

    while (*arg0 != 0) {
        if (*arg0 == 0xBD) {
            *arg0 = 0;
            count++;
        }
        arg0++;
    }

    return count;
}

s32 func_1516A7B0() {
    return 0;
}

s32 func_1516AA70() {
    return 0;
}

s32 func_1516B6BC() {
    return 0;
}

typedef struct {
    u8 *text;
    u32 reserved;
} TextBankEntry;
typedef struct {
    u32 flags;
    union { u32 index; u8 *text; } value;
} TextSegmentSource;
extern TextBankEntry *D_800DD254;
extern TextBankEntry *D_800DD258;

/* Select bank 0/1 or direct text (2), then advance across zero-separated text runs. */
u8 *func_1516C878(TextSegmentSource *source, s32 segment, s16 bank) {
    s32 current;
    u8 *text;

    switch (bank) {
        case 0:
            text = D_800DD254[source->value.index].text;
            break;
        case 1:
            text = D_800DD258[source->value.index].text;
            break;
        case 2:
            text = source->value.text;
            break;
    }
    for (current = 0; current < segment; current++) {
        while (*text != 0) {
            text++;
        }
        while (*text == 0) {
            text++;
        }
    }
    return text;
}

s32 func_1516C934() {
    return 0;
}

s32 func_1516CC58() {
    return 0;
}

s32 func_1516D0CC() {
    return 0;
}

void func_1516D2E0(u8 *arg0) {
    if (arg0 != 0) {
        if (*arg0 == 0x51) {
            *(*(u8 **) (arg0 + 0x10) + 8) = 0;
            func_1516972C(arg0);
            *(arg0 + 0x15) = 0;
        }
    }
}

void func_1516D328(u8 *arg0) {
    u8 *temp_v0;

    if (arg0 != 0) {
        if (*arg0 == 0x51) {
            temp_v0 = *(u8 **) (arg0 + 0x10);
            *(u32 *) temp_v0 |= 0x100;
            temp_v0 = *(u8 **) (arg0 + 0x10);
            *(u32 *) temp_v0 &= ~0x400;
            *(arg0 + 0x20) = *(*(u8 **) (arg0 + 0x10) + 8);
        }
    }
}

u8 *func_1516D378(u8 *arg0) {
    u8 *temp_v1;

    if ((arg0 != 0) && (*arg0 == 0x51)) {
        temp_v1 = *(u8 **) (arg0 + 0x10);
        *(u32 *) temp_v1 |= 0x100;
        temp_v1 = *(u8 **) (arg0 + 0x10);
        *(u32 *) temp_v1 &= ~0x400;
        return arg0;
    }
    return 0;
}

u8 *func_1516D3C4(u8 *arg0) {
    u8 *temp_v1;

    if ((arg0 != 0) && (*arg0 == 0x51)) {
        temp_v1 = *(u8 **) (arg0 + 0x10);
        *(u32 *) temp_v1 |= 0x500;
        return arg0;
    }
    return 0;
}
