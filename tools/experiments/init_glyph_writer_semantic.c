typedef unsigned char u8;
typedef unsigned short u16;
typedef unsigned int u32;

/* Ordinary ABI trial; the retail register interface still needs an adapter. */
u32 init_glyph_writer(u32 cursor, u32 displacement, u32 glyph, u32 font) {
    u32 first = cursor;
    u32 second = cursor + displacement;
    u32 source = font + glyph * 8;
    int row, column;
    for (row = 0; row < 8; row++) {
        u32 bits = *(volatile u8 *)source;
        for (column = 0; column < 8; column++) {
            u16 pixel = (bits & 0x80) ? 0xFFFF : 1;
            *(volatile u16 *)first = pixel;
            *(volatile u16 *)second = pixel;
            first += 2;
            second += 2;
            bits <<= 1;
        }
        source++;
        first += 0x238;
        second += 0x238;
    }
    return cursor + 16;
}
