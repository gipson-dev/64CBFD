typedef unsigned char u8;
typedef short s16;

#if !defined(HOST_TEST) && (SHAPE >= 12 && SHAPE <= 24)
typedef char GuestAddressWidth[(sizeof(unsigned long) == 4) ? 1 : -1];
#if SHAPE == 21 || SHAPE == 22
typedef char GuestMaskWidth[(sizeof(unsigned int) == 4) ? 1 : -1];
#endif
#endif

#ifdef HOST_TEST
u8 *D_8003BE70;
u8 *D_8003BE7C;
s16 D_8003BE78;
#else
extern u8 *D_8003BE70;
extern u8 *D_8003BE7C;
extern s16 D_8003BE78;
#endif

#if (SHAPE == 23 || SHAPE == 24) && !defined(HOST_TEST)
typedef struct {
    u8 *start;
    unsigned long reserved4;
    s16 count;
    s16 reservedA;
    u8 *end;
} InitBitmapRecord;
extern volatile InitBitmapRecord bitmapRecord;
const unsigned long init_bitmap_record_layout[] = {
    sizeof(InitBitmapRecord),
    (unsigned long)&((InitBitmapRecord *)0)->start,
    (unsigned long)&((InitBitmapRecord *)0)->count,
    (unsigned long)&((InitBitmapRecord *)0)->end,
    sizeof(((InitBitmapRecord *)0)->count)
};
#if SHAPE == 24
#define BITMAP_START record->start
#define BITMAP_END record->end
#define BITMAP_COUNT record->count
#else
#define BITMAP_START bitmapRecord.start
#define BITMAP_END bitmapRecord.end
#define BITMAP_COUNT bitmapRecord.count
#endif
#else
#define BITMAP_START D_8003BE70
#define BITMAP_END D_8003BE7C
#define BITMAP_COUNT D_8003BE78
#endif

/* Isolated scheduling trial; no production owner or instruction guards. */
#if SHAPE == 4 || SHAPE == 5
u8 *func_10005BE0(void) {
#else
void func_10005BE0(void) {
#endif
#if SHAPE == 6 || SHAPE == 7
    int value = 0xFF;
#elif SHAPE == 19
    unsigned int value = 0xFF;
#elif SHAPE == 21 || SHAPE == 22
    unsigned int value = ~0u;
#endif
#if SHAPE == 24 && !defined(HOST_TEST)
    volatile InitBitmapRecord *record = &bitmapRecord;
#endif
#if SHAPE >= 12 && SHAPE <= 24
    unsigned long cursor = (unsigned long)BITMAP_START;
    unsigned long end = (unsigned long)BITMAP_END;
#if SHAPE == 13
    unsigned long remaining = end - cursor;
#elif SHAPE == 18
    unsigned long difference;
#endif
#elif SHAPE == 8
    u8 *cursor = D_8003BE70;
    u8 *end = D_8003BE7C;
#else
    volatile u8 *cursor = D_8003BE70;
    volatile u8 *end = D_8003BE7C;
#endif
#if SHAPE == 9
    volatile u8 *stop = end + 1;
#endif
    int bits;
#if SHAPE == 2
    int again;
#endif
#if SHAPE == 1 || SHAPE == 4 || SHAPE == 5 || SHAPE == 8
    do {
        *cursor = 0xFF;
    } while (cursor++ != end);
#elif SHAPE == 2
    do {
        *cursor = 0xFF;
        again = cursor != end;
        cursor++;
    } while (again);
#elif SHAPE == 3
    for (;;) {
        *cursor = 0xFF;
        if (cursor == end) break;
        cursor++;
    }
#elif SHAPE == 6 || SHAPE == 7
    do {
        *cursor = value;
    } while (cursor++ != end);
#elif SHAPE == 9
    do {
        *cursor++ = 0xFF;
    } while (cursor != stop);
#elif SHAPE == 10
    /* Valid nonwrapping intervals only; do not compare unrelated C pointers. */
    do {
        *cursor = 0xFF;
    } while ((unsigned long)cursor++ < (unsigned long)end);
#elif SHAPE == 11
    do {
        *cursor++ = 0xFF;
    } while ((unsigned long)cursor <= (unsigned long)end);
#elif SHAPE == 12 || SHAPE == 23 || SHAPE == 24
    /* Guest o32 unsigned arithmetic preserves the wrapping address domain. */
    do {
        *(volatile u8 *)cursor = 0xFF;
    } while (cursor++ != end);
#elif SHAPE == 13
    do {
        *(volatile u8 *)cursor++ = 0xFF;
    } while (remaining-- != 0);
#elif SHAPE == 14
    /* Separate the final store so comparison needs no old-cursor temporary. */
    while (cursor != end) {
        *(volatile u8 *)cursor = 0xFF;
        cursor++;
    }
    *(volatile u8 *)cursor = 0xFF;
#elif SHAPE == 15
    /* Put the update only on the taken back edge, not the exit edge. */
    goto fill;
advance:
    cursor++;
fill:
    *(volatile u8 *)cursor = 0xFF;
    if (cursor != end) goto advance;
#elif SHAPE == 16 || SHAPE == 17
    /* Keep the count reload and mask inside the equality exit region. */
    for (;;) {
        *(volatile u8 *)cursor = 0xFF;
        if (cursor == end) {
            bits = D_8003BE78 & 7;
            if (bits) {
#if SHAPE == 16
                /* Equality makes the cursor the final-byte address. */
                *(volatile u8 *)cursor = (2u << (bits - 1)) - 1;
#else
                *(volatile u8 *)end = (2u << (bits - 1)) - 1;
#endif
            }
            return;
        }
        cursor++;
    }
#elif SHAPE == 18
    /* Test late zero-comparison folding without a saved Boolean or old cursor. */
    do {
        *(volatile u8 *)cursor = 0xFF;
        difference = cursor - end;
        cursor++;
    } while (difference);
#elif SHAPE == 19
    /* Reuse the fill value for a low-bit mask, without a second constant. */
    do {
        *(volatile u8 *)cursor = value;
    } while (cursor++ != end);
#elif SHAPE == 20
    /* Compare the updated cursor directly instead of retaining its old value. */
    cursor--;
    do {
        cursor++;
        *(volatile u8 *)cursor = 0xFF;
    } while (cursor != end);
#elif SHAPE == 21 || SHAPE == 22
    /* Trial an unsigned all-ones word for fill and complemented mask generation. */
    do {
        *(volatile u8 *)cursor = value;
    } while (cursor++ != end);
#else
#error Unknown SHAPE
#endif
#if SHAPE != 16 && SHAPE != 17
    bits = BITMAP_COUNT & 7;
#if SHAPE == 7
    if (bits--) {
#elif SHAPE == 19 || SHAPE == 21
    if (bits) {
#else
    if (bits) {
        bits--;
#endif
#if SHAPE == 6 || SHAPE == 7
        value = 2;
        value <<= bits;
        value--;
        *end = value;
#elif SHAPE == 19
        value >>= 8 - bits;
        *(volatile u8 *)end = value;
#elif SHAPE == 21
        value = ~(value << bits);
        *(volatile u8 *)end = value;
#elif (SHAPE >= 12 && SHAPE <= 15) || SHAPE == 18 || SHAPE == 20 || SHAPE == 22 || SHAPE == 23 || SHAPE == 24
        *(volatile u8 *)end = (2u << bits) - 1;
#else
        *end = (2u << bits) - 1;
#endif
    }
#if SHAPE == 4
    return (u8 *)cursor;
#elif SHAPE == 5
    return (u8 *)end + 1;
#endif
#endif
}

#ifdef HOST_TEST
int main(void) {
    u8 buffer[4104];
    int counts[] = {0, -32768, -8, -7, -1, 107, 235, 243, 251, 259, 267, 362, 32767};
    int index, count, size, i, pass, expected;
    for (index = 0; index < 77; index++) {
        count = index < 64 ? index + 1 : counts[index - 64];
        size = count > 0 ? (count + 7) >> 3 : 1;
        for (i = 0; i < 4104; i++) buffer[i] = 0xA5;
        D_8003BE70 = buffer + 3;
        D_8003BE7C = buffer + size + 2;
        D_8003BE78 = count;
        for (pass = 0; pass < 2; pass++) {
#if SHAPE == 4 || SHAPE == 5
            if (func_10005BE0() != buffer + size + 3) return 4;
#else
            func_10005BE0();
#endif
            for (i = 0; i < 4104; i++) {
                expected = i >= 3 && i < size + 3 ? 0xFF : 0xA5;
                if ((count & 7) && i == size + 2) expected = (1 << (count & 7)) - 1;
                if (buffer[i] != expected) return 1;
            }
        }
    }
    D_8003BE70 = (u8 *)&D_8003BE78;
    D_8003BE7C = D_8003BE70 + 1;
    D_8003BE78 = 8;
#if SHAPE == 4 || SHAPE == 5
    if (func_10005BE0() != D_8003BE70 + 2) return 5;
#else
    func_10005BE0();
#endif
    if (D_8003BE70[0] != 0xFF || D_8003BE70[1] != 0x7F) return 2;
    D_8003BE70 = (u8 *)&D_8003BE7C;
    D_8003BE7C = D_8003BE70 + 3;
    D_8003BE78 = 3;
#if SHAPE == 4 || SHAPE == 5
    if (func_10005BE0() != D_8003BE70 + 4) return 6;
#else
    func_10005BE0();
#endif
    for (i = 0; i < 4; i++) {
        if (D_8003BE70[i] != (i == 3 ? 7 : 0xFF)) return 3;
    }
    return 0;
}
#endif
