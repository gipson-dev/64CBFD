#ifdef INIT_DECODE_GUEST
typedef unsigned char uint8_t;
typedef unsigned short uint16_t;
typedef unsigned int uint32_t;
typedef signed int int32_t;
#else
#include <stdint.h>
#include <stddef.h>
#endif

#include "init_decompressor_frame.h"

/* Isolated recovery candidate. Not linked into production; caller owns bounds. */
#if defined(INIT_DECODE_CACHE_BUILDER) && INIT_DECODE_CACHE_BUILDER != 1 && INIT_DECODE_CACHE_BUILDER != 2
#error Unsupported builder cache mode
#endif
#if defined(INIT_DECODE_PACKED_ENTRY) && !defined(INIT_DECODE_ALIGNED_ENTRY)
#error Packed entry mode requires word-aligned entries
#endif
#if defined(INIT_DECODE_BYTE_PARENT) && !defined(INIT_DECODE_FRAME_BACKED)
#error Byte parent addressing requires physical frame tables
#endif
#if defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE != 1 && INIT_DECODE_CACHE_DYNAMIC_CODE != 2 && INIT_DECODE_CACHE_DYNAMIC_CODE != 3
#error Unsupported dynamic code lookup mode
#endif
#if defined(INIT_DECODE_BUILDER_SYMBOL_CURSOR) && INIT_DECODE_BUILDER_SYMBOL_CURSOR != 1 && INIT_DECODE_BUILDER_SYMBOL_CURSOR != 2
#error Unsupported builder symbol cursor mode
#endif

typedef struct {
    uint8_t operation;
    uint8_t bits;
    uint16_t value;
} InitDecodeFields;

#ifdef INIT_DECODE_ALIGNED_ENTRY
typedef union {
    uint32_t alignment;
    InitDecodeFields fields;
} InitDecodeEntry;
#define ENTRY_OPERATION(e) ((e)->fields.operation)
#define ENTRY_BITS(e) ((e)->fields.bits)
#define ENTRY_VALUE(e) ((e)->fields.value)
#else
typedef InitDecodeFields InitDecodeEntry;
#define ENTRY_OPERATION(e) ((e)->operation)
#define ENTRY_BITS(e) ((e)->bits)
#define ENTRY_VALUE(e) ((e)->value)
#endif

typedef struct {
    uint8_t lead;
    InitDecodeEntry entry;
} InitDecodeEntryProbe;

#ifdef INIT_DECODE_GUEST
#define FIELD_OFFSET(member) ((uint32_t)&((InitDecodeFields *)0)->member)
#else
#define FIELD_OFFSET(member) offsetof(InitDecodeFields, member)
#endif
uint32_t init_decode_entry_layout[] = {
    sizeof(InitDecodeEntry), sizeof(InitDecodeEntryProbe) - sizeof(InitDecodeEntry),
    FIELD_OFFSET(operation), FIELD_OFFSET(bits), FIELD_OFFSET(value)
};
#undef FIELD_OFFSET

typedef struct {
    const uint8_t *input;
    uint8_t *output;
    InitDecodeEntry *workspace;
    uint32_t reservoir;
    int32_t bits;
    int32_t produced;
    int32_t limit;
    uint32_t allocated;
#ifdef INIT_DECODE_FRAME_BACKED
    InitDecodeFrame *frame;
    uint32_t workspaceAddress;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
    uint32_t abiSaved[6];
    uint32_t abiFpr[12];
    uint32_t abiDirty;
#endif
#else
    uint32_t counts[17];
    uint32_t tables[17];
    uint32_t sorted[288];
    uint32_t offsets[17];
    uint32_t lengths[320];
#endif
} InitDecodeState;

#ifdef INIT_DECODE_FRAME_BACKED
#define COUNTS(s) ((s)->frame->counts)
#define SORTED(s) ((s)->frame->sorted)
#define OFFSETS(s) ((s)->frame->offsets)
#define LENGTHS(s) ((s)->frame->staging.lengths)
#define SET_TABLE(s, level, index) \
    ((s)->frame->tables[level] = (s)->workspaceAddress + 4 * (index))
#define TABLE_INDEX(s, level) (((s)->frame->tables[level] - (s)->workspaceAddress) >> 2)
#define CODE_ROOT(s) ((s)->frame->literalRoot)
#define LITERAL_ROOT(s) ((s)->frame->literalRoot)
#define DISTANCE_ROOT(s) ((s)->frame->distanceRoot)
#define CODE_BITS(s) ((s)->frame->literalBits)
#define LITERAL_BITS(s) ((s)->frame->literalBits)
#define DISTANCE_BITS(s) ((s)->frame->distanceBits)
#define FIXED_LITERAL_ROOT(s) ((s)->frame->staging.fixed.literalRoot)
#define FIXED_DISTANCE_ROOT(s) ((s)->frame->staging.fixed.distanceRoot)
#define FIXED_LITERAL_BITS(s) ((s)->frame->staging.fixed.literalBits)
#define FIXED_DISTANCE_BITS(s) ((s)->frame->staging.fixed.distanceBits)
#else
#define COUNTS(s) ((s)->counts)
#define SORTED(s) ((s)->sorted)
#define OFFSETS(s) ((s)->offsets)
#define LENGTHS(s) ((s)->lengths)
#define SET_TABLE(s, level, index) ((s)->tables[level] = (index))
#define TABLE_INDEX(s, level) ((s)->tables[level])
#define CODE_ROOT(s) (codeRoot)
#define LITERAL_ROOT(s) (literalRoot)
#define DISTANCE_ROOT(s) (distanceRoot)
#define CODE_BITS(s) (codeBits)
#define LITERAL_BITS(s) (literalBits)
#define DISTANCE_BITS(s) (distanceBits)
#define FIXED_LITERAL_ROOT(s) (root)
#define FIXED_DISTANCE_ROOT(s) (root)
#define FIXED_LITERAL_BITS(s) (bits)
#define FIXED_DISTANCE_BITS(s) (bits)
#endif

#ifdef INIT_DECODE_GUEST
uint32_t init_decode_guest_sizes[] = {sizeof(InitDecodeEntry), sizeof(InitDecodeState)};
#define FRAME_OFFSET(member) ((uint32_t)&((InitDecodeFrame *)0)->member)
uint32_t init_decode_guest_frame_layout[] = {
    sizeof(InitDecodeFrame), FRAME_OFFSET(counts), FRAME_OFFSET(tables),
    FRAME_OFFSET(sorted), FRAME_OFFSET(offsets), FRAME_OFFSET(staging),
    FRAME_OFFSET(staging.fixed.literalRoot), FRAME_OFFSET(staging.fixed.literalBits),
    FRAME_OFFSET(staging.fixed.distanceRoot), FRAME_OFFSET(staging.fixed.distanceBits),
    FRAME_OFFSET(literalRoot), FRAME_OFFSET(distanceRoot), FRAME_OFFSET(literalBits),
    FRAME_OFFSET(distanceBits), FRAME_OFFSET(wrapperReturn), FRAME_OFFSET(savedS),
    FRAME_OFFSET(dispatcherReturn), FRAME_OFFSET(streamReturn), FRAME_OFFSET(finalBlock),
    FRAME_OFFSET(savedWorkspace), FRAME_OFFSET(savedFp), FRAME_OFFSET(savedGp),
    FRAME_OFFSET(entryReturn), FRAME_OFFSET(padA84)
};
#undef FRAME_OFFSET
#endif

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
#ifdef INIT_DECODE_FLAT_BITS
    while (s->bits < (int32_t)width) {
        s->reservoir |= (uint32_t)*s->input++ << (s->bits & 31);
        s->bits += 8;
    }
    value = s->reservoir & ((1u << (width & 31)) - 1);
    s->reservoir >>= width & 31;
    s->bits -= width;
#else
    need_bits(s, width);
    value = s->reservoir & low_mask(width);
    drop_bits(s, width);
#endif
    return value;
}

#ifdef INIT_DECODE_CACHE_BUILDER
#define BUILD_COUNTS cachedCounts
#if INIT_DECODE_CACHE_BUILDER == 1
#define BUILD_SORTED cachedSorted
#else
#define BUILD_SORTED SORTED(s)
#endif
#define BUILD_OFFSETS cachedOffsets
#else
#define BUILD_COUNTS COUNTS(s)
#define BUILD_SORTED SORTED(s)
#define BUILD_OFFSETS OFFSETS(s)
#endif

#ifdef INIT_DECODE_CACHE_WORKSPACE
#define BUILD_WORKSPACE cachedWorkspace
#else
#define BUILD_WORKSPACE (s->workspace)
#endif

#ifdef INIT_DECODE_LOCAL_ALLOCATED
#define BUILD_ALLOCATED allocated
#define BUILD_COMMIT_ALLOCATION (s->allocated = allocated)
#else
#define BUILD_ALLOCATED (s->allocated)
#define BUILD_COMMIT_ALLOCATION ((void)0)
#endif

#ifdef INIT_DECODE_BUILDER_ALLOCATION_TABLE
#define BUILD_NEW_TABLE table
#else
#define BUILD_NEW_TABLE next
#endif

#ifdef INIT_DECODE_PACKED_ENTRY
#define BUILD_ENTRY_OPERATION entryOperation
#define BUILD_ENTRY_BITS entryBits
#else
#define BUILD_ENTRY_OPERATION ENTRY_OPERATION(&entry)
#define BUILD_ENTRY_BITS ENTRY_BITS(&entry)
#endif

#ifdef INIT_DECODE_BOUNDED_BUILDER_SHIFTS
#define BUILD_SHIFT(width) ((uint32_t)(width))
#define BUILD_LOW_MASK(width) ((1u << BUILD_SHIFT(width)) - 1)
#else
#define BUILD_SHIFT(width) ((width) & 31)
#define BUILD_LOW_MASK(width) low_mask(width)
#endif

int init_decode_build(InitDecodeState *s, const uint32_t *lengths,
                      uint32_t count, uint32_t simple, const uint16_t *bases,
                      const uint8_t *extras, uint16_t *root, uint32_t *rootBits) {
    uint32_t min, max, width, available, incomplete, code, symbolIndex;
    uint32_t bits, remaining, levelBits, size = 0, table = 0, next;
    uint16_t value = (uint16_t)s->reservoir;
    uint16_t *link = root;
    int32_t level = -1, consumed;
#ifdef INIT_DECODE_BUILDER_HISTOGRAM_CURSOR
    const uint32_t *lengthCursor;
#endif
#ifdef INIT_DECODE_BUILDER_SYMBOL_CURSOR
    uint32_t *symbolCursor;
#if INIT_DECODE_BUILDER_SYMBOL_CURSOR == 1
    uint32_t *symbolEnd;
#else
    uint32_t symbolsLeft;
#endif
#endif
#ifdef INIT_DECODE_LOCAL_ALLOCATED
    uint32_t allocated;
#endif
#ifdef INIT_DECODE_CACHE_WORKSPACE
    InitDecodeEntry *cachedWorkspace;
#endif
#ifdef INIT_DECODE_CACHE_BUILDER
    uint32_t *cachedCounts, *cachedOffsets;
#if INIT_DECODE_CACHE_BUILDER == 1
    uint32_t *cachedSorted;
#endif
#endif
    if (count == 0) {
        return 1;
    }
#ifdef INIT_DECODE_CACHE_WORKSPACE
    cachedWorkspace = s->workspace;
#endif
#ifdef INIT_DECODE_CACHE_BUILDER
    cachedCounts = COUNTS(s);
#if INIT_DECODE_CACHE_BUILDER == 1
    cachedSorted = SORTED(s);
#endif
    cachedOffsets = OFFSETS(s);
#endif
    for (bits = 0; bits <= 16; bits++) {
        BUILD_COUNTS[bits] = 0;
    }
#ifdef INIT_DECODE_BUILDER_HISTOGRAM_CURSOR
    lengthCursor = lengths;
    do {
        BUILD_COUNTS[*lengthCursor++]++;
    } while (lengthCursor != lengths + count);
#else
    for (symbolIndex = 0; symbolIndex < count; symbolIndex++) {
        BUILD_COUNTS[lengths[symbolIndex]]++;
    }
#endif
    if (BUILD_COUNTS[0] == count) {
        *root = 0;
        *rootBits = 0;
        return 0;
    }
#ifdef INIT_DECODE_BOUNDED_LENGTH_SCAN
    /* The all-zero return leaves at least one populated bucket in 1..16. */
    for (min = 1; BUILD_COUNTS[min] == 0; min++) {}
    for (max = 16; BUILD_COUNTS[max] == 0; max--) {}
#else
    for (min = 1; min < 16 && BUILD_COUNTS[min] == 0; min++) {}
    for (max = 16; max && BUILD_COUNTS[max] == 0; max--) {}
#endif
    width = *rootBits;
    if (width < min) width = min;
    if (width > max) width = max;
    *rootBits = width;
    available = 1u << min;
    for (bits = min; bits < max; bits++) {
        available = (available - BUILD_COUNTS[bits]) << 1;
    }
    incomplete = available - BUILD_COUNTS[max];
    BUILD_COUNTS[max] = available;
    BUILD_OFFSETS[1] = 0;
#ifdef INIT_DECODE_BUILDER_OFFSET_SUM
    available = 0;
    for (bits = 1; bits < max; bits++) {
        available += BUILD_COUNTS[bits];
        BUILD_OFFSETS[bits + 1] = available;
    }
#else
    for (bits = 1; bits < max; bits++) {
        BUILD_OFFSETS[bits + 1] = BUILD_OFFSETS[bits] + BUILD_COUNTS[bits];
    }
#endif
    for (symbolIndex = 0; symbolIndex < count; symbolIndex++) {
        bits = lengths[symbolIndex];
        if (bits != 0) BUILD_SORTED[BUILD_OFFSETS[bits]++] = symbolIndex;
    }
    BUILD_OFFSETS[0] = 0;
#ifdef INIT_DECODE_FRAME_BACKED
    s->frame->tables[0] = 0;
#endif
    code = 0;
#ifdef INIT_DECODE_BUILDER_SYMBOL_CURSOR
    symbolCursor = BUILD_SORTED;
#if INIT_DECODE_BUILDER_SYMBOL_CURSOR == 1
    symbolEnd = symbolCursor + count;
#else
    symbolsLeft = count;
#endif
#else
    symbolIndex = 0;
#endif
    consumed = -(int32_t)width;
#ifdef INIT_DECODE_LOCAL_ALLOCATED
    allocated = s->allocated;
#endif
    for (bits = min; bits <= max; bits++) {
        remaining = BUILD_COUNTS[bits];
        while (remaining != 0) {
#ifdef INIT_DECODE_PACKED_ENTRY
            uint8_t entryOperation, entryBits;
            uint32_t packed;
#else
            InitDecodeEntry entry;
#endif
            while ((int32_t)bits > consumed + (int32_t)width) {
                uint32_t ceiling, slots, scan;
                level++;
                consumed += width;
                ceiling = max - consumed;
                if (ceiling > width) ceiling = width;
                levelBits = bits - consumed;
                slots = 1u << BUILD_SHIFT(levelBits);
                if (slots > remaining) {
                    slots -= remaining;
                    scan = bits;
                    /* Retail increments even when already at the ceiling. */
                    levelBits++;
                    while (levelBits < ceiling) {
                        slots <<= 1;
                        scan++;
                        if (BUILD_COUNTS[scan] >= slots) break;
                        slots -= BUILD_COUNTS[scan];
                        levelBits++;
                    }
                }
                size = 1u << BUILD_SHIFT(levelBits);
                BUILD_NEW_TABLE = BUILD_ALLOCATED + 1;
                *link = BUILD_NEW_TABLE;
#ifdef INIT_DECODE_BUILDER_ALLOCATION_TABLE
                link = &ENTRY_VALUE(&BUILD_WORKSPACE[table - 1]);
#else
                link = &ENTRY_VALUE(&BUILD_WORKSPACE[BUILD_ALLOCATED]);
#endif
                *link = 0;
#ifndef INIT_DECODE_BUILDER_ALLOCATION_TABLE
                table = next;
#endif
                SET_TABLE(s, level, table);
                if (level != 0) {
                    InitDecodeEntry *parent;
                    BUILD_OFFSETS[level] = code;
#ifdef INIT_DECODE_BYTE_PARENT
                    parent = (InitDecodeEntry *)((uint8_t *)BUILD_WORKSPACE +
                        ((s->frame->tables[level - 1] - s->workspaceAddress) & ~3u) +
                        ((code >> BUILD_SHIFT(consumed - (int32_t)width)) << 2));
#else
                    parent = &BUILD_WORKSPACE[TABLE_INDEX(s, level - 1) +
                        (code >> BUILD_SHIFT(consumed - (int32_t)width))];
#endif
                    ENTRY_OPERATION(parent) = levelBits + 16;
                    ENTRY_BITS(parent) = width;
                    ENTRY_VALUE(parent) = BUILD_NEW_TABLE;
                    value = BUILD_NEW_TABLE;
                }
#ifdef INIT_DECODE_BUILDER_ALLOCATION_TABLE
                BUILD_ALLOCATED = table + size;
#else
                BUILD_ALLOCATED += size + 1;
#endif
                BUILD_COMMIT_ALLOCATION;
            }
            BUILD_ENTRY_OPERATION = 99;
            BUILD_ENTRY_BITS = bits - consumed;
#ifdef INIT_DECODE_BUILDER_SYMBOL_CURSOR
#if INIT_DECODE_BUILDER_SYMBOL_CURSOR == 1
            if (symbolCursor != symbolEnd) {
                uint32_t symbol = *symbolCursor++;
#else
            if (symbolsLeft != 0) {
                uint32_t symbol = *symbolCursor++;
                symbolsLeft--;
#endif
#else
            if (symbolIndex < count) {
                uint32_t symbol = BUILD_SORTED[symbolIndex++];
#endif
                /* Retail classifies even stale sorted words with signed SLT. */
                if ((int32_t)symbol < (int32_t)simple) {
#ifdef INIT_DECODE_BUILDER_SIMPLE_OPERATION
                    BUILD_ENTRY_OPERATION = 15 + ((int32_t)symbol < 256);
#else
                    BUILD_ENTRY_OPERATION = (int32_t)symbol < 256 ? 16 : 15;
#endif
                    value = symbol;
                } else {
                    BUILD_ENTRY_OPERATION = extras[symbol - simple];
                    value = bases[symbol - simple];
                }
            }
#ifdef INIT_DECODE_PACKED_ENTRY
#if defined(INIT_DECODE_GUEST) || (defined(__BYTE_ORDER__) && __BYTE_ORDER__ == __ORDER_BIG_ENDIAN__)
            packed = ((uint32_t)entryOperation << 24) | ((uint32_t)entryBits << 16) | value;
#elif defined(__BYTE_ORDER__) && __BYTE_ORDER__ == __ORDER_LITTLE_ENDIAN__
            packed = entryOperation | ((uint32_t)entryBits << 8) | ((uint32_t)value << 16);
#else
#error Native byte order is required for packed entry mode
#endif
#else
            ENTRY_VALUE(&entry) = value;
#endif
            next = code >> BUILD_SHIFT(consumed);
#ifdef INIT_DECODE_CACHE_LEAF_TABLE
            if (next < size) {
                InitDecodeEntry *leafTable = BUILD_WORKSPACE + table;
                uint32_t stride = 1u << BUILD_SHIFT(bits - consumed);
                do {
#ifdef INIT_DECODE_PACKED_ENTRY
                    leafTable[next].alignment = packed;
#else
                    leafTable[next] = entry;
#endif
                    next += stride;
                } while (next < size);
            }
#else
            for (; next < size; next += 1u << BUILD_SHIFT(bits - consumed)) {
#ifdef INIT_DECODE_PACKED_ENTRY
                BUILD_WORKSPACE[table + next].alignment = packed;
#else
                BUILD_WORKSPACE[table + next] = entry;
#endif
            }
#endif
            next = 1u << BUILD_SHIFT(bits - 1);
#ifdef INIT_DECODE_BUILDER_CODE_TOGGLE
            do {
                code ^= next;
                if (code & next) break;
                next >>= 1;
            } while (next != 0);
#else
            while (code & next) {
                code ^= next;
                next >>= 1;
            }
            code ^= next;
#endif
#ifdef INIT_DECODE_PARENT_ASCENT_CURSOR
            {
                const uint32_t *offsetCursor = BUILD_OFFSETS + level;
                while ((code & BUILD_LOW_MASK(consumed)) != *offsetCursor) {
                    offsetCursor--;
                    level--;
                    consumed -= width;
                }
            }
#else
            while ((code & BUILD_LOW_MASK(consumed)) != BUILD_OFFSETS[level]) {
                level--;
                consumed -= width;
            }
#endif
            remaining--;
        }
    }
    return incomplete != 0 && max != 1;
}

#undef BUILD_COUNTS
#undef BUILD_SORTED
#undef BUILD_OFFSETS
#undef BUILD_WORKSPACE
#undef BUILD_ALLOCATED
#undef BUILD_COMMIT_ALLOCATION
#undef BUILD_NEW_TABLE
#undef BUILD_ENTRY_OPERATION
#undef BUILD_ENTRY_BITS
#undef BUILD_SHIFT
#undef BUILD_LOW_MASK

#ifdef INIT_DECODE_ABI_FPR_SHADOW
static void abi_capture(InitDecodeState *s, uint32_t literals, uint32_t distances) {
    uint32_t i;
    s->abiFpr[0] = literals;
    s->abiFpr[1] = distances;
    for (i = 0; i < 6; i++) s->abiFpr[i + 2] = s->abiSaved[i];
    s->abiFpr[8] = s->workspaceAddress;
    s->abiFpr[9] = (uint32_t)s->input;
    s->abiFpr[10] = s->bits;
    s->abiFpr[11] = s->reservoir;
    s->abiDirty = 0xFFF;
}
#endif

static InitDecodeEntry *lookup(InitDecodeState *s, uint32_t root, uint32_t width) {
#ifdef INIT_DECODE_LOOP_LOOKUP
#ifdef INIT_DECODE_LOOKUP_FIRST_REFILL
    InitDecodeEntry *entry;
    need_bits(s, width);
    for (;;) {
        entry = &s->workspace[root + (s->reservoir & low_mask(width))];
        if (ENTRY_OPERATION(entry) <= 16 || ENTRY_OPERATION(entry) == 99) return entry;
        width = ENTRY_OPERATION(entry) - 16;
        drop_bits(s, ENTRY_BITS(entry));
        need_bits(s, width);
        root = ENTRY_VALUE(entry);
    }
#else
    InitDecodeEntry *entry = 0;
    for (;;) {
        need_bits(s, width);
        entry = &s->workspace[(entry ? ENTRY_VALUE(entry) : root) +
            (s->reservoir & low_mask(width))];
        if (ENTRY_OPERATION(entry) <= 16 || ENTRY_OPERATION(entry) == 99) return entry;
        width = ENTRY_OPERATION(entry) - 16;
        drop_bits(s, ENTRY_BITS(entry));
    }
#endif
#else
    InitDecodeEntry *entry;
    need_bits(s, width);
    entry = &s->workspace[root + (s->reservoir & low_mask(width))];
    while (ENTRY_OPERATION(entry) > 16 && ENTRY_OPERATION(entry) != 99) {
        width = ENTRY_OPERATION(entry) - 16;
        drop_bits(s, ENTRY_BITS(entry));
        need_bits(s, width);
        entry = &s->workspace[ENTRY_VALUE(entry) + (s->reservoir & low_mask(width))];
    }
    return entry;
#endif
}

int init_decode_compressed(InitDecodeState *s, uint32_t literalRoot,
                           uint32_t distanceRoot, uint32_t literalBits,
                           uint32_t distanceBits) {
    int32_t produced = s->produced;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
    s->abiSaved[0] = 0x8002C0C0u;
    s->abiSaved[4] = produced;
#endif
    for (;;) {
        InitDecodeEntry *entry = lookup(s, literalRoot, literalBits);
        uint32_t operation = ENTRY_OPERATION(entry);
        uint32_t length, distance;
        int32_t source, end;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
        s->abiSaved[5] = s->workspaceAddress + 4 * (entry - s->workspace);
#endif
        if (operation == 99) return 1;
        drop_bits(s, ENTRY_BITS(entry));
        if (operation == 16) {
            s->output[produced++] = ENTRY_VALUE(entry);
#ifdef INIT_DECODE_ABI_FPR_SHADOW
            s->abiSaved[4] = produced;
#endif
            continue;
        }
        if (operation == 15) {
            s->produced = produced;
            return 0;
        }
        length = ENTRY_VALUE(entry) + take_bits(s, operation);
#ifdef INIT_DECODE_ABI_FPR_SHADOW
        s->abiSaved[2] = length;
#endif
        entry = lookup(s, distanceRoot, distanceBits);
#ifdef INIT_DECODE_ABI_FPR_SHADOW
        s->abiSaved[5] = s->workspaceAddress + 4 * (entry - s->workspace);
#endif
        if (ENTRY_OPERATION(entry) == 99) return 1;
        drop_bits(s, ENTRY_BITS(entry));
        distance = ENTRY_VALUE(entry) + take_bits(s, ENTRY_OPERATION(entry));
        source = (uint32_t)produced - distance;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
        s->abiSaved[3] = source;
#endif
        end = (uint32_t)produced + length;
        if (end >= s->limit) return 1;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
        s->abiSaved[4] = end;
#endif
        while (produced != end) s->output[produced++] = s->output[source++];
    }
}

int init_decode_stored(InitDecodeState *s) {
    uint32_t length, inverse;
    int32_t end, produced = s->produced;
    drop_bits(s, s->bits & 7);
    length = take_bits(s, 16);
#ifdef INIT_DECODE_STORED_SHARED_LENGTHS
    inverse = (~take_bits(s, 16)) & 0xFFFF;
    if (length != inverse) {
        s->bits += 16;
        return 1;
    }
#else
    need_bits(s, 16);
    inverse = (~s->reservoir) & 0xFFFF;
    s->reservoir >>= 16;
    if (length != inverse) return 1;
    s->bits -= 16;
#endif
    end = (uint32_t)produced + length;
    if (end >= s->limit) return 1;
    while (produced != end) s->output[produced++] = take_bits(s, 8);
    s->produced = end;
    return 0;
}

void init_decode_fixed_tables(InitDecodeState *s) {
#ifdef INIT_DECODE_FIXED_LENGTH_CURSOR
    uint32_t *cursor;
#endif
#ifdef INIT_DECODE_FRAME_BACKED
    uint32_t i;
    FIXED_LITERAL_BITS(s) = 7;
#else
    uint16_t root;
    uint32_t i, bits = 7;
#endif
    s->allocated = 0;
#ifdef INIT_DECODE_FIXED_LENGTH_CURSOR
    cursor = LENGTHS(s);
    do { *cursor++ = 8; } while (cursor != LENGTHS(s) + 144);
    do { *cursor++ = 9; } while (cursor != LENGTHS(s) + 256);
    do { *cursor++ = 7; } while (cursor != LENGTHS(s) + 280);
    do { *cursor++ = 8; } while (cursor != LENGTHS(s) + 288);
#else
    for (i = 0; i < 288; i++) {
        LENGTHS(s)[i] = i < 144 ? 8 : i < 256 ? 9 : i < 280 ? 7 : 8;
    }
#endif
    init_decode_build(s, LENGTHS(s), 288, 257, lengthBase, lengthExtra,
                      &FIXED_LITERAL_ROOT(s), &FIXED_LITERAL_BITS(s));
    for (i = 0; i < 30; i++) LENGTHS(s)[i] = 5;
    FIXED_DISTANCE_BITS(s) = 5;
    init_decode_build(s, LENGTHS(s), 30, 0, distanceBase, distanceExtra,
                      &FIXED_DISTANCE_ROOT(s), &FIXED_DISTANCE_BITS(s));
}

#ifdef INIT_DECODE_CACHE_DYNAMIC_LENGTHS
#define DYNAMIC_LENGTHS cachedLengths
#else
#define DYNAMIC_LENGTHS LENGTHS(s)
#endif

#ifdef INIT_DECODE_DYNAMIC_CURSOR
#define DYNAMIC_MORE (cursor < end)
#define DYNAMIC_STORE(value) (*cursor++ = (value))
#define DYNAMIC_OVERFLOW ((uint32_t)(end - cursor) < repeats)
#else
#define DYNAMIC_MORE (i < total)
#define DYNAMIC_STORE(value) (DYNAMIC_LENGTHS[i++] = (value))
#define DYNAMIC_OVERFLOW (i + repeats > total)
#endif

int init_decode_dynamic(InitDecodeState *s) {
    uint32_t packed = take_bits(s, 14);
    uint32_t literals = (packed & 31) + 257;
    uint32_t distances = ((packed >> 5) & 31) + 1;
    uint32_t transmitted = ((packed >> 10) & 15) + 4;
#ifndef INIT_DECODE_FRAME_BACKED
    uint32_t codeBits = 7, literalBits = 9, distanceBits = 6;
    uint16_t codeRoot, literalRoot, distanceRoot;
#endif
    uint32_t i, symbol, previous = 0, repeats, total = literals + distances;
#ifdef INIT_DECODE_SEED_DISTANCE_ROOT
    InitDecodeEntry *lastCodeEntry = s->workspace;
#endif
#ifdef INIT_DECODE_DYNAMIC_CURSOR
    uint32_t *cursor, *end;
#endif
#ifdef INIT_DECODE_CACHE_DYNAMIC_LENGTHS
    uint32_t *cachedLengths;
#endif
#if defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 1
    uint32_t cachedCodeWidth, cachedCodeMask;
    InitDecodeEntry *cachedCodeTable;
#elif defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 2
    uint32_t cachedCodeMask;
#endif
    if (literals >= 287 || distances >= 31) return 1;
#ifdef INIT_DECODE_CACHE_DYNAMIC_LENGTHS
    cachedLengths = LENGTHS(s);
#endif
    for (i = 0; i < transmitted; i++) DYNAMIC_LENGTHS[lengthOrder[i]] = take_bits(s, 3);
    for (; i < 19; i++) DYNAMIC_LENGTHS[lengthOrder[i]] = 0;
#ifdef INIT_DECODE_FRAME_BACKED
    CODE_BITS(s) = 7;
#endif
#ifdef INIT_DECODE_ABI_FPR_SHADOW
    s->abiSaved[1] = 19;
    abi_capture(s, literals, distances);
#endif
    init_decode_build(s, DYNAMIC_LENGTHS, 19, 19, 0, 0, &CODE_ROOT(s), &CODE_BITS(s));
#if defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 1
    cachedCodeWidth = CODE_BITS(s);
    cachedCodeMask = low_mask(cachedCodeWidth);
    cachedCodeTable = &s->workspace[CODE_ROOT(s)];
#elif defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 2
    cachedCodeMask = low_mask(CODE_BITS(s));
#endif
#ifdef INIT_DECODE_DYNAMIC_CURSOR
    cursor = DYNAMIC_LENGTHS;
    end = cursor + total;
#else
    i = 0;
#endif
    while (DYNAMIC_MORE) {
        InitDecodeEntry *entry;
#if defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 1
        need_bits(s, cachedCodeWidth);
        entry = &cachedCodeTable[s->reservoir & cachedCodeMask];
#elif defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 2
        need_bits(s, CODE_BITS(s));
        entry = &s->workspace[CODE_ROOT(s) + (s->reservoir & cachedCodeMask)];
#elif defined(INIT_DECODE_CACHE_DYNAMIC_CODE) && INIT_DECODE_CACHE_DYNAMIC_CODE == 3
        need_bits(s, CODE_BITS(s));
        entry = &s->workspace[CODE_ROOT(s) +
            (s->reservoir & ((1u << (CODE_BITS(s) & 31)) - 1))];
#else
        need_bits(s, CODE_BITS(s));
        entry = &s->workspace[CODE_ROOT(s) + (s->reservoir & low_mask(CODE_BITS(s)))];
#endif
#ifdef INIT_DECODE_SEED_DISTANCE_ROOT
        lastCodeEntry = entry;
#endif
        drop_bits(s, ENTRY_BITS(entry));
        symbol = ENTRY_VALUE(entry);
        if (symbol < 16) {
            DYNAMIC_STORE(previous = symbol);
            continue;
        }
#ifdef INIT_DECODE_DYNAMIC_SHARED_REPEATS
        repeats = take_bits(s, symbol == 16 ? 2 : symbol == 17 ? 3 : 7);
        repeats += 3 + ((symbol > 17) << 3);
#else
        if (symbol == 16) {
            repeats = take_bits(s, 2) + 3;
        } else if (symbol == 17) {
            repeats = take_bits(s, 3) + 3;
        } else {
            repeats = take_bits(s, 7) + 11;
        }
#endif
        if (DYNAMIC_OVERFLOW) return 1;
#ifdef INIT_DECODE_DYNAMIC_REPEAT_VALUE
        if (symbol != 16) previous = 0;
#ifdef INIT_DECODE_DYNAMIC_CURSOR
        {
            uint32_t *repeatEnd = cursor + repeats;
            /* Repeat codes request at least three slots; overflow was checked. */
            do { DYNAMIC_STORE(previous); } while (cursor != repeatEnd);
        }
#else
        while (repeats--) DYNAMIC_STORE(previous);
#endif
#else
        while (repeats--) DYNAMIC_STORE(symbol == 16 ? previous : 0);
        if (symbol != 16) previous = 0;
#endif
    }
#ifdef INIT_DECODE_ABI_FPR_SHADOW
    s->abiSaved[0] = lastCodeEntry - s->workspace;
    s->abiSaved[1] = symbol < 16 ? symbol : 0;
    s->abiSaved[2] = previous;
    s->abiSaved[3] = low_mask(CODE_BITS(s));
    s->abiSaved[4] = total;
    s->abiSaved[5] = CODE_ROOT(s);
    abi_capture(s, literals, distances);
#endif
#ifdef INIT_DECODE_FRAME_BACKED
#ifdef INIT_DECODE_SEED_DISTANCE_ROOT
    DISTANCE_ROOT(s) = (uint16_t)(lastCodeEntry - s->workspace);
#endif
    LITERAL_BITS(s) = 9;
#endif
    if (init_decode_build(s, DYNAMIC_LENGTHS, literals, 257, lengthBase, lengthExtra,
                          &LITERAL_ROOT(s), &LITERAL_BITS(s))) return 1;
#ifdef INIT_DECODE_FRAME_BACKED
    DISTANCE_BITS(s) = 6;
#endif
    if (init_decode_build(s, DYNAMIC_LENGTHS + literals, distances, 0,
                          distanceBase, distanceExtra, &DISTANCE_ROOT(s), &DISTANCE_BITS(s))) return 1;
    return init_decode_compressed(s, LITERAL_ROOT(s), DISTANCE_ROOT(s),
                                  LITERAL_BITS(s), DISTANCE_BITS(s));
}

#undef DYNAMIC_LENGTHS
#undef DYNAMIC_MORE
#undef DYNAMIC_STORE
#undef DYNAMIC_OVERFLOW

int init_decode_stream(InitDecodeState *s, InitDecodeEntry *fixedWorkspace) {
    uint32_t header;
    int status;
    s->produced = 0;
    s->reservoir = 0;
    s->bits = 0;
    do {
        header = take_bits(s, 3);
        s->allocated = 0;
#ifdef INIT_DECODE_STREAM_MASKED_DISPATCH
        switch (header & 6) {
#else
        switch ((header >> 1) & 3) {
#endif
        case 0:
            status = init_decode_stored(s);
            break;
#ifdef INIT_DECODE_STREAM_MASKED_DISPATCH
        case 2: {
#else
        case 1: {
#endif
            InitDecodeEntry *workspace = s->workspace;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
            uint32_t address = s->workspaceAddress;
            s->workspaceAddress = (uint32_t)fixedWorkspace;
#endif
            s->workspace = fixedWorkspace;
            init_decode_compressed(s, 1, 626, 7, 5);
            s->workspace = workspace;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
            s->workspaceAddress = address;
#endif
            status = 0;
            break;
        }
#ifdef INIT_DECODE_STREAM_MASKED_DISPATCH
        case 4:
#else
        case 2:
#endif
            status = init_decode_dynamic(s);
            break;
        default:
            status = 2;
            break;
        }
        if (status) return status;
    } while (!(header & 1));
#ifdef INIT_DECODE_STREAM_BYTE_REWIND
    if (s->bits >= 8) {
        uint32_t unread = (uint32_t)s->bits >> 3;
        s->bits &= 7;
        s->input -= unread;
    }
#else
    while (s->bits >= 8) {
        s->bits -= 8;
        s->input--;
    }
#endif
    return 0;
}

#ifdef INIT_DECODE_PACKED_HEADER
#pragma pack(1)
typedef struct {
    uint32_t opening;
} InitDecodeHeader;
typedef struct {
    uint8_t lead;
    InitDecodeHeader header;
} InitDecodeHeaderProbe;
#pragma pack()
#ifdef INIT_DECODE_GUEST
uint32_t init_decode_header_layout[] = {
    sizeof(InitDecodeHeader), (uint32_t)&((InitDecodeHeaderProbe *)0)->header
};
#endif
#endif

int init_decode_core(InitDecodeState *s, InitDecodeEntry *fixedWorkspace,
                     uint32_t inputAddress, uint32_t outputAddress,
                     uint32_t workspaceAddress) {
#if defined(INIT_DECODE_PACKED_HEADER) && defined(INIT_DECODE_GUEST)
    const volatile InitDecodeHeader *header = (const volatile InitDecodeHeader *)s->input;
    uint32_t opening = header->opening;
#else
    const volatile uint8_t *header = s->input;
    uint32_t opening = ((uint32_t)header[0] << 24) | ((uint32_t)header[1] << 16) |
                       ((uint32_t)header[2] << 8) | header[3];
#endif
    int32_t distance = inputAddress - outputAddress;
#ifdef INIT_DECODE_ABI_FPR_SHADOW
#ifdef INIT_DECODE_ABI_SEED_CURSOR
    const uint32_t *source = s->frame->savedS;
    uint32_t *destination = s->abiSaved;
    do { *destination++ = *source++; } while (destination != s->abiSaved + 6);
#else
    uint32_t i;
    for (i = 0; i < 6; i++) s->abiSaved[i] = s->frame->savedS[i];
#endif
    s->abiDirty = 0;
#endif
#ifdef INIT_DECODE_FRAME_BACKED
    s->workspaceAddress = workspaceAddress;
#endif
    s->input += (opening >> 16) == 0x1172 ? 2 : 4;
    s->limit = 0x70000000;
    if (distance > 0) s->limit = distance;
    distance = workspaceAddress - outputAddress;
    if (distance >= 0 && distance < s->limit) s->limit = distance;
    if (init_decode_stream(s, fixedWorkspace)) return 0;
    return s->produced;
}
