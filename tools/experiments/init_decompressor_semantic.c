#include <stdint.h>

/* Isolated recovery candidate. Not linked into production; caller owns bounds. */
typedef struct {
    uint8_t operation;
    uint8_t bits;
    uint16_t value;
} InitDecodeEntry;

typedef struct {
    const uint8_t *input;
    uint8_t *output;
    InitDecodeEntry *workspace;
    uint32_t reservoir;
    int32_t bits;
    int32_t produced;
    int32_t limit;
    uint32_t allocated;
    uint32_t counts[17];
    uint32_t tables[17];
    uint32_t sorted[288];
    uint32_t offsets[17];
    uint32_t lengths[320];
} InitDecodeState;

static const uint16_t lengthBase[31] = {
    3,4,5,6,7,8,9,10,11,13,15,17,19,23,27,31,35,43,51,59,67,83,99,115,
    131,163,195,227,258,0,0
};
static const uint8_t lengthExtra[31] = {
    0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,0,99,99
};
static const uint16_t distanceBase[30] = {
    1,2,3,4,5,7,9,13,17,25,33,49,65,97,129,193,257,385,513,769,1025,
    1537,2049,3073,4097,6145,8193,12289,16385,24577
};
static const uint8_t distanceExtra[30] = {
    0,0,0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13
};
static const uint8_t lengthOrder[19] = {
    16,17,18,0,8,7,9,6,10,5,11,4,12,3,13,2,14,1,15
};

static uint32_t low_mask(uint32_t width) {
    return (1u << (width & 31)) - 1;
}

static void need_bits(InitDecodeState *s, int32_t width) {
    while (s->bits < width) {
        s->reservoir |= (uint32_t)*s->input++ << (s->bits & 31);
        s->bits += 8;
    }
}

static void drop_bits(InitDecodeState *s, uint32_t width) {
    s->reservoir >>= width & 31;
    s->bits -= width;
}

static uint32_t take_bits(InitDecodeState *s, uint32_t width) {
    uint32_t value;
    need_bits(s, width);
    value = s->reservoir & low_mask(width);
    drop_bits(s, width);
    return value;
}

int init_decode_build(InitDecodeState *s, const uint32_t *lengths,
                      uint32_t count, uint32_t simple, const uint16_t *bases,
                      const uint8_t *extras, uint16_t *root, uint32_t *rootBits) {
    uint32_t min, max, width, available, incomplete, code, symbolIndex;
    uint32_t bits, remaining, levelBits, size = 0, table = 0, next;
    uint16_t value = (uint16_t)s->reservoir;
    uint16_t *link = root;
    int32_t level = -1, consumed;
    if (count == 0) {
        return 1;
    }
    for (bits = 0; bits <= 16; bits++) {
        s->counts[bits] = 0;
    }
    for (symbolIndex = 0; symbolIndex < count; symbolIndex++) {
        s->counts[lengths[symbolIndex]]++;
    }
    if (s->counts[0] == count) {
        *root = 0;
        *rootBits = 0;
        return 0;
    }
    for (min = 1; min < 16 && s->counts[min] == 0; min++) {}
    for (max = 16; max && s->counts[max] == 0; max--) {}
    width = *rootBits;
    if (width < min) width = min;
    if (width > max) width = max;
    *rootBits = width;
    available = 1u << min;
    for (bits = min; bits < max; bits++) {
        available = (available - s->counts[bits]) << 1;
    }
    incomplete = available - s->counts[max];
    s->counts[max] = available;
    s->offsets[1] = 0;
    for (bits = 1; bits < max; bits++) {
        s->offsets[bits + 1] = s->offsets[bits] + s->counts[bits];
    }
    for (symbolIndex = 0; symbolIndex < count; symbolIndex++) {
        bits = lengths[symbolIndex];
        if (bits != 0) s->sorted[s->offsets[bits]++] = symbolIndex;
    }
    s->offsets[0] = 0;
    code = 0;
    symbolIndex = 0;
    consumed = -(int32_t)width;
    for (bits = min; bits <= max; bits++) {
        remaining = s->counts[bits];
        while (remaining != 0) {
            InitDecodeEntry entry;
            while ((int32_t)bits > consumed + (int32_t)width) {
                uint32_t ceiling, slots, scan;
                level++;
                consumed += width;
                ceiling = max - consumed;
                if (ceiling > width) ceiling = width;
                levelBits = bits - consumed;
                slots = 1u << (levelBits & 31);
                if (slots > remaining) {
                    slots -= remaining;
                    scan = bits;
                    /* Retail increments even when already at the ceiling. */
                    levelBits++;
                    while (levelBits < ceiling) {
                        slots <<= 1;
                        scan++;
                        if (s->counts[scan] >= slots) break;
                        slots -= s->counts[scan];
                        levelBits++;
                    }
                }
                size = 1u << (levelBits & 31);
                next = s->allocated + 1;
                *link = next;
                link = &s->workspace[s->allocated].value;
                *link = 0;
                table = next;
                s->tables[level] = table;
                if (level != 0) {
                    InitDecodeEntry *parent;
                    s->offsets[level] = code;
                    parent = &s->workspace[s->tables[level - 1] +
                        (code >> ((consumed - (int32_t)width) & 31))];
                    parent->operation = levelBits + 16;
                    parent->bits = width;
                    parent->value = next;
                    value = next;
                }
                s->allocated += size + 1;
            }
            entry.operation = 99;
            entry.bits = bits - consumed;
            if (symbolIndex < count) {
                uint32_t symbol = s->sorted[symbolIndex++];
                if (symbol < simple) {
                    entry.operation = symbol < 256 ? 16 : 15;
                    value = symbol;
                } else {
                    entry.operation = extras[symbol - simple];
                    value = bases[symbol - simple];
                }
            }
            entry.value = value;
            next = code >> (consumed & 31);
            for (; next < size; next += 1u << ((bits - consumed) & 31)) {
                s->workspace[table + next] = entry;
            }
            next = 1u << ((bits - 1) & 31);
            while (code & next) {
                code ^= next;
                next >>= 1;
            }
            code ^= next;
            while ((code & low_mask(consumed)) != s->offsets[level]) {
                level--;
                consumed -= width;
            }
            remaining--;
        }
    }
    return incomplete != 0 && max != 1;
}

static InitDecodeEntry *lookup(InitDecodeState *s, uint32_t root, uint32_t width) {
    InitDecodeEntry *entry;
    need_bits(s, width);
    entry = &s->workspace[root + (s->reservoir & low_mask(width))];
    while (entry->operation > 16 && entry->operation != 99) {
        width = entry->operation - 16;
        drop_bits(s, entry->bits);
        need_bits(s, width);
        entry = &s->workspace[entry->value + (s->reservoir & low_mask(width))];
    }
    return entry;
}

int init_decode_compressed(InitDecodeState *s, uint32_t literalRoot,
                           uint32_t distanceRoot, uint32_t literalBits,
                           uint32_t distanceBits) {
    int32_t produced = s->produced;
    for (;;) {
        InitDecodeEntry *entry = lookup(s, literalRoot, literalBits);
        uint32_t operation = entry->operation;
        uint32_t length, distance;
        int32_t source, end;
        if (operation == 99) return 1;
        drop_bits(s, entry->bits);
        if (operation == 16) {
            s->output[produced++] = entry->value;
            continue;
        }
        if (operation == 15) {
            s->produced = produced;
            return 0;
        }
        length = entry->value + take_bits(s, operation);
        entry = lookup(s, distanceRoot, distanceBits);
        if (entry->operation == 99) return 1;
        drop_bits(s, entry->bits);
        distance = entry->value + take_bits(s, entry->operation);
        source = (uint32_t)produced - distance;
        end = (uint32_t)produced + length;
        if (end >= s->limit) return 1;
        while (produced != end) s->output[produced++] = s->output[source++];
    }
}

int init_decode_stored(InitDecodeState *s) {
    uint32_t length, inverse;
    int32_t end, produced = s->produced;
    drop_bits(s, s->bits & 7);
    length = take_bits(s, 16);
    need_bits(s, 16);
    inverse = (~s->reservoir) & 0xFFFF;
    s->reservoir >>= 16;
    if (length != inverse) return 1;
    s->bits -= 16;
    end = (uint32_t)produced + length;
    if (end >= s->limit) return 1;
    while (produced != end) s->output[produced++] = take_bits(s, 8);
    s->produced = end;
    return 0;
}

void init_decode_fixed_tables(InitDecodeState *s) {
    uint16_t root;
    uint32_t i, bits = 7;
    s->allocated = 0;
    for (i = 0; i < 288; i++) {
        s->lengths[i] = i < 144 ? 8 : i < 256 ? 9 : i < 280 ? 7 : 8;
    }
    init_decode_build(s, s->lengths, 288, 257, lengthBase, lengthExtra, &root, &bits);
    for (i = 0; i < 30; i++) s->lengths[i] = 5;
    bits = 5;
    init_decode_build(s, s->lengths, 30, 0, distanceBase, distanceExtra, &root, &bits);
}

int init_decode_dynamic(InitDecodeState *s) {
    uint32_t packed = take_bits(s, 14);
    uint32_t literals = (packed & 31) + 257;
    uint32_t distances = ((packed >> 5) & 31) + 1;
    uint32_t transmitted = ((packed >> 10) & 15) + 4;
    uint32_t codeBits = 7, literalBits = 9, distanceBits = 6;
    uint16_t codeRoot, literalRoot, distanceRoot;
    uint32_t i, symbol, previous = 0, repeats, total = literals + distances;
    if (literals >= 287 || distances >= 31) return 1;
    for (i = 0; i < transmitted; i++) s->lengths[lengthOrder[i]] = take_bits(s, 3);
    for (; i < 19; i++) s->lengths[lengthOrder[i]] = 0;
    init_decode_build(s, s->lengths, 19, 19, 0, 0, &codeRoot, &codeBits);
    i = 0;
    while (i < total) {
        InitDecodeEntry *entry;
        need_bits(s, codeBits);
        entry = &s->workspace[codeRoot + (s->reservoir & low_mask(codeBits))];
        drop_bits(s, entry->bits);
        symbol = entry->value;
        if (symbol < 16) {
            s->lengths[i++] = previous = symbol;
            continue;
        }
        if (symbol == 16) {
            repeats = take_bits(s, 2) + 3;
        } else if (symbol == 17) {
            repeats = take_bits(s, 3) + 3;
        } else {
            repeats = take_bits(s, 7) + 11;
        }
        if (i + repeats > total) return 1;
        while (repeats--) s->lengths[i++] = symbol == 16 ? previous : 0;
        if (symbol != 16) previous = 0;
    }
    if (init_decode_build(s, s->lengths, literals, 257, lengthBase, lengthExtra,
                          &literalRoot, &literalBits)) return 1;
    if (init_decode_build(s, s->lengths + literals, distances, 0,
                          distanceBase, distanceExtra, &distanceRoot, &distanceBits)) return 1;
    return init_decode_compressed(s, literalRoot, distanceRoot, literalBits, distanceBits);
}

int init_decode_stream(InitDecodeState *s, InitDecodeEntry *fixedWorkspace) {
    uint32_t header;
    int status;
    s->produced = 0;
    s->reservoir = 0;
    s->bits = 0;
    do {
        header = take_bits(s, 3);
        s->allocated = 0;
        switch ((header >> 1) & 3) {
        case 0:
            status = init_decode_stored(s);
            break;
        case 1: {
            InitDecodeEntry *workspace = s->workspace;
            s->workspace = fixedWorkspace;
            init_decode_compressed(s, 1, 626, 7, 5);
            s->workspace = workspace;
            status = 0;
            break;
        }
        case 2:
            status = init_decode_dynamic(s);
            break;
        default:
            status = 2;
            break;
        }
        if (status) return status;
    } while (!(header & 1));
    while (s->bits >= 8) {
        s->bits -= 8;
        s->input--;
    }
    return 0;
}

int init_decode_core(InitDecodeState *s, InitDecodeEntry *fixedWorkspace,
                     uint32_t inputAddress, uint32_t outputAddress,
                     uint32_t workspaceAddress) {
    const volatile uint8_t *header = s->input;
    uint32_t opening = ((uint32_t)header[0] << 24) | ((uint32_t)header[1] << 16) |
                       ((uint32_t)header[2] << 8) | header[3];
    int32_t distance = inputAddress - outputAddress;
    s->input += (opening >> 16) == 0x1172 ? 2 : 4;
    s->limit = 0x70000000;
    if (distance > 0) s->limit = distance;
    distance = workspaceAddress - outputAddress;
    if (distance >= 0 && distance < s->limit) s->limit = distance;
    if (init_decode_stream(s, fixedWorkspace)) return 0;
    return s->produced;
}
