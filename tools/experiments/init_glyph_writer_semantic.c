typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;

/* Ordinary ABI trial; the retail register interface still needs an adapter. */
u32 init_glyph_writer(u32 cursor, u32 displacement, u32 glyph, u32 font) {
    u32 first = cursor;
    u32 second = cursor + displacement;
    u32 source = font + glyph * 8;
    int row, column;
#ifdef GLYPH_COUNTDOWN
    row = 8;
    do {
#else
    for (row = 0; row < 8; row++) {
#endif
        u32 bits = *(volatile u8 *)source;
#ifdef GLYPH_COUNTDOWN
        column = 8;
        do {
#else
        for (column = 0; column < 8; column++) {
#endif
#if defined(GLYPH_SEEDED_PIXEL) || defined(GLYPH_LOW_PIXEL)
            u32 pixel = 0xFFFFFFFF;
#ifdef GLYPH_LOW_PIXEL
            if ((bits & 0x80) == 0) pixel = 1;
#else
            if ((bits & 0x80) == 0) pixel = 0x10001;
#endif
#else
            u16 pixel = (bits & 0x80) ? 0xFFFF : 1;
#endif
            *(volatile u16 *)first = pixel;
            *(volatile u16 *)second = pixel;
            first += 2;
            second += 2;
            bits <<= 1;
#ifdef GLYPH_COUNTDOWN
        } while (--column);
#else
        }
#endif
        source++;
        first += 0x238;
        second += 0x238;
#ifdef GLYPH_COUNTDOWN
    } while (--row);
#else
    }
#endif
    return cursor + 16;
}
