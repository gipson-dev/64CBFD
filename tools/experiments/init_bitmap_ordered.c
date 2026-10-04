typedef unsigned char u8;
typedef short s16;

#ifdef HOST_TEST
u8 *D_8003BE70;
u8 *D_8003BE7C;
s16 D_8003BE78;
#else
extern u8 *D_8003BE70;
extern u8 *D_8003BE7C;
extern s16 D_8003BE78;
#endif

/* Isolated scheduling trial; no production owner or instruction guards. */
#if SHAPE >= 4
u8 *func_10005BE0(void) {
#else
void func_10005BE0(void) {
#endif
    volatile u8 *cursor = D_8003BE70;
    volatile u8 *end = D_8003BE7C;
    int bits;
#if SHAPE == 2
    int again;
#endif
#if SHAPE == 1 || SHAPE == 4 || SHAPE == 5
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
#else
#error Unknown SHAPE
#endif
    bits = D_8003BE78 & 7;
    if (bits) {
        bits--;
        *end = (2u << bits) - 1;
    }
#if SHAPE == 4
    return (u8 *)cursor;
#elif SHAPE == 5
    return (u8 *)end + 1;
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
#if SHAPE >= 4
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
#if SHAPE >= 4
    if (func_10005BE0() != D_8003BE70 + 2) return 5;
#else
    func_10005BE0();
#endif
    if (D_8003BE70[0] != 0xFF || D_8003BE70[1] != 0x7F) return 2;
    D_8003BE70 = (u8 *)&D_8003BE7C;
    D_8003BE7C = D_8003BE70 + 3;
    D_8003BE78 = 3;
#if SHAPE >= 4
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
