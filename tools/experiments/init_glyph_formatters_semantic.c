typedef unsigned char u8;
typedef unsigned int u32;

extern volatile u32 D_8002AAE8[2];
extern u8 D_8002AC84[];
u32 init_glyph_writer(u32, u32, u32, u32);

/* Result cells belong to the trial caller, not retail framebuffer storage. */
int init_glyph_hex(u32 position, u32 value, u32 *result) {
    u32 first = D_8002AAE8[0];
    u32 second, cursor;
    int count = 8;
    if (!first) return 0;
    second = D_8002AAE8[1];
    if (!second) return 0;
    position += 9;
    cursor = first + (position & 0xFFE0) * 146 + (position & 31) * 16 + 0x4A0;
    do {
        u32 index = (value & 15) + 9;
        value >>= 4;
        cursor = init_glyph_writer(cursor - 32, second - first, index, (u32)D_8002AC84);
    } while (--count);
    result[0] = cursor;
    return 1;
}

int init_glyph_string(u32 position, u32 text, u32 *result) {
    u32 first = D_8002AAE8[0];
    u32 second, cursor;
    int character;
    if (!first) return 0;
    second = D_8002AAE8[1];
    if (!second) return 0;
    cursor = first + (position & 0xFFE0) * 146 + (position & 31) * 16 + 0x4A0;
    character = *(volatile signed char *)text;
    while (character) {
        int index = character;
        if (index >= 65) index -= 7;
        index -= 39;
        if (index < 0) index = 0;
        text++;
        cursor = init_glyph_writer(cursor, second - first, index, (u32)D_8002AC84);
        character = *(volatile signed char *)text;
    }
    result[0] = cursor;
    result[1] = text;
    return 1;
}
