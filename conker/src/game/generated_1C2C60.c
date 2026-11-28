#include <ultra64.h>
#include "structs.h"
#include <string.h>
extern s32 D_800B0E58[7762];
typedef struct {
    u8 retained00[0x08];
    s16 key;
    s16 width;
    s16 height;
    s16 scaledX;
    s16 scaledY;
    u8 retained12[0x02];
    u8 active;
    u8 retained15[0x03];
    s32 link;
    s16 primary[5];
    s16 secondary0;
    s16 secondary1;
    s16 secondary2;
    s16 secondary3;
    s16 secondary4;
    u8 retained30[0x0C];
} PackedLayoutRecord15195984;


typedef struct {
    u8 pad0[0x1C];
    s16 timer;
    u8 pad1E[0xE];
    f32 value2C;
    f32 value30;
    u8 pad34[0x28];
    u8 value5C;
    u8 pad5D[0x107];
    f32 factor;
    s16 limit;
    s16 scale;
} Generated1C2C60Record;

typedef struct {
    u8 pad0[0x24];
    f32 factor;
    s16 limit;
    s16 scale;
} Generated1C2C60Params;

typedef struct {
    u8 retained00[0x34];
    f32 position[3];
    f32 endPoint[3];
    u8 retained4C[0xF4];
    f32 velocity[3];
    f32 endVelocity[3];
    f32 verticalAcceleration;
    f32 damping;
    f32 endDamping;
} DualDampedMotion15197AB4;
extern f32 D_800BE9A4;

/* Non-matching placeholders for the text-only asm slice asm/1C2C60.s. */

s32 func_1519CDB0(s32 arg0, f32 arg1, s32 arg2);

s32 func_15199980();
void func_100111C8(u16 arg0);
void func_1519C258();

extern f32 D_800A8AA4;
extern f32 D_800A8AAC;
extern f32 D_800A8AA8;
extern s32 D_800A8A40;
extern s32 D_800A8A48;
extern s32 D_800E08E0;
extern s32 D_800E08E4;
extern s32 D_800E08E8;
extern s32 D_800E08EC;
extern s32 D_800E08F0;
extern u8 D_800A8A9C[];
extern u8 *D_800E0900[];
extern s32 D_800BE9E4;
extern s32 (*D_8008F898[])(u8 *arg0);
extern s32 (*D_8008F88C[])(u8 *arg0);
extern s32 (*D_8008F8C0[])(u8 *arg0);
extern s32 (*D_8008F8B4[])(u8 *arg0);

s32 func_151957B0(s32 arg0, u8 *arg1, u8 *arg2) {
    u8 *temp_v0 = (u8 *) allocate_memory(arg0, 1, 0, 0);
    s32 temp_v1;

    if (temp_v0 != NULL) {
        *(s32 *) (temp_v0 + 4) = 0;
        temp_v1 = *(s32 *) (arg2);
        if (temp_v1 != 0) {
            *(s32 *) (temp_v0) = temp_v1;
            *(s32 *) (*(s32 *) arg2 + 4) = (s32) temp_v0;
            *(s32 *) (arg2) = (s32) temp_v0;
        } else {
            *(s32 *) (temp_v0) = 0;
            *(s32 *) (arg2) = (s32) temp_v0;
            *(s32 *) (arg1) = (s32) temp_v0;
        }
    }
    return (s32) temp_v0;
}

void func_15195824(void) {
}

void func_1519582C() {
    volatile s32 *ptr_e4 = &D_800E08E4, *ptr_ec = &D_800E08EC;

    *ptr_e4 = 0;
    D_800E08E0 = 0;
    *ptr_ec = 0;
    D_800E08E8 = 0;
    D_800E08F0 = -2;
}

/* Find a texture occurrence and count its paired tile-size commands. */
s32 func_15195868(u8 *displayList, s32 assetId, s32 occurrence, s32 *tileCount) {
    s32 index;
    s32 opcode;
    s32 next;
    s32 second;

    *tileCount = 0;
    index = -1;
    for (;;) {
        index++;
        while ((s8)G_SETTIMG != (opcode = *(s8 *)(displayList + (index << 3))) &&
               (s8)G_ENDDL != opcode) {
            index++;
        }
        if ((s8)G_ENDDL == opcode) {
            return -1;
        }
        if (D_800B0E58[assetId] == ((s32 *)displayList)[index * 2 + 1] || assetId == 0) {
            if (occurrence-- <= 0) {
                break;
            }
        }
    }
    assetId = (s8)opcode;
    while (assetId != (s8)G_SETTILESIZE) {
        index++;
        assetId = *(s8 *)(displayList + (index << 3));
    }
    next = index;
    do {
        *tileCount += 1;
        next++;
        assetId = *(s8 *)(displayList + (next << 3));
        next++;
        second = *(s8 *)(displayList + (next << 3));
    } while (assetId == (s8)G_SETTILE && second == (s8)G_SETTILESIZE);
    return index;
}

/* Allocate and initialize a record from two packed 12-bit pairs. */
PackedLayoutRecord15195984 *func_15195984(s32 key, s32 packedSize,
                                          s32 packedScale, s32 doubleSize) {
    PackedLayoutRecord15195984 *record;
    s32 index;
    s32 width;
    s32 height;

    record = (PackedLayoutRecord15195984 *)func_151957B0(
        0x3C, (u8 *)&D_800E08E8, (u8 *)&D_800E08EC);
    if (record != NULL) {
        record->link = 0;
        for (index = 0; index < 5; index++) {
            record->primary[index] = -1;
        }
        record->secondary0 = -1;
        record->secondary2 = -1;
        record->secondary3 = -1;
        record->secondary4 = -1;
        record->secondary1 = -1;
        record->key = key;
        width = ((packedSize >> 12) & 0xFFF) + 2;
        height = (packedSize & 0xFFF) + 2;
        if (doubleSize != 0) {
            width *= 2;
            height *= 2;
        }
        record->scaledX = (packedScale >> 12) & 0xFFF;
        record->scaledY = packedScale & 0xFFF;
        record->width = width;
        record->height = height;
        record->scaledX *= 8;
        record->scaledY *= 8;
        record->active = 1;
    }
    return record;
}

s32 func_15195A84(s16 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return arg0;
}


/* Register texture command indices in one of the record's five-slot arrays. */
void *func_15195AA8(s32 displayList, s32 assetId, s32 doubleSize,
                  s32 occurrence, s32 state, s32 secondary,
                  s32 field12, s32 field13) {
    s32 packedSize;
    s32 index;
    s32 searchOccurrence;
    s32 tileCount;
    s32 slot;
    s32 packedScale;
    u8 *record = NULL;

    searchOccurrence = occurrence;
    if (displayList == 0) {
        return 0;
    }
    if (occurrence == -1) {
        searchOccurrence = 0;
    }
    do {
        index = func_15195868((u8 *)displayList, assetId, searchOccurrence, &tileCount);
        if (index == -1) {
            occurrence = 0;
        } else {
            if (assetId == 0) {
                assetId = D_800E08F0;
            }
            record = (u8 *)D_800E08E8;
            packedSize = *(s32 *)((u8 *)displayList + (index << 3) + 4);
            packedScale = *(s32 *)((u8 *)displayList + (index << 3));
            while (record != NULL && *(s16 *)(record + 8) != 0) {
                record = *(u8 **)(record + 4);
            }
            if (record == NULL) {
                record = (u8 *)func_15195984(assetId, packedSize, packedScale, doubleSize);
                if (record != NULL) {
                    record[0x12] = field12;
                    record[0x13] = field13;
                    state = 0;
                } else {
                    return 0;
                }
            } else {
                index = func_15195A84(index, (s32)record, packedSize, doubleSize);
                state = 0;
            }
            if (record[0x14] < tileCount) {
                record[0x14] = tileCount;
            }
            searchOccurrence++;
            if (secondary == 0) {
                slot = state;
                while (slot < 5 && ((s16 *)(record + 0x1C))[slot] != -1) {
                    slot++;
                }
                if (slot < 5) {
                    ((s16 *)(record + 0x1C))[slot] = index;
                    record[0x30 + slot] = tileCount;
                }
            } else {
                slot = state;
                while (slot < 5 && ((s16 *)(record + 0x26))[slot] != -1) {
                    slot++;
                }
                if (slot < 5) {
                    ((s16 *)(record + 0x26))[slot] = index;
                    record[0x35 + slot] = tileCount;
                }
            }
        }
    } while (occurrence == -1);
    if (assetId == D_800E08F0) {
        D_800E08F0--;
    }
    return record;
}


/* Preserve the retail key-chain cursor and append a missing association. */
void func_15195D00(u8 *owner, s32 key, s32 index, s32 mode) {
    u8 *cursor = *(u8 **)(owner + 0x18);
    u8 *record;

    if (cursor != NULL) {
        record = cursor;
        do {
            if (*(s32 *)(record + 8) == key && *(u16 *)(record + 0xC) == index) {
                return;
            }
            /* The look-ahead cursor exits before testing the final record. */
            cursor = *(u8 **)(record + 0x10);
            if (cursor != NULL) {
                record = cursor;
                cursor = *(u8 **)(cursor + 0x10);
            }
        } while (cursor != NULL);
        cursor = (u8 *)func_151957B0(0x14, (u8 *)&D_800E08E0, (u8 *)&D_800E08E4);
        *(u8 **)(record + 0x10) = cursor;
    } else {
        cursor = (u8 *)func_151957B0(0x14, (u8 *)&D_800E08E0, (u8 *)&D_800E08E4);
        *(u8 **)(owner + 0x18) = cursor;
    }
    *(s32 *)(cursor + 8) = key;
    *(u16 *)(cursor + 0xC) = index;
    *(u8 **)(cursor + 0x10) = NULL;
    cursor[0xE] = mode;
    return;
}

extern u8 D_800BEAC0;

/* Register matching texture occurrences and return the final layout record. */
s32 func_15195DD4(s32 displayList, s32 assetId, s32 doubleSize,
                  s32 occurrence, s32 separate, s32 field12, s32 field13) {
    s32 packedSize;
    s32 index;
    s32 searchOccurrence;
    s32 tileCount;
    s32 key;
    s32 packedScale;
    /* Retail leaves this uninitialized when the first search has no match. */
    u8 *record;

    searchOccurrence = occurrence;
    if (displayList == 0) {
        return 0;
    }
    if (D_800BEAC0 != 0) {
        return 0;
    }
    if (occurrence == -1) {
        searchOccurrence = 0;
    }
    do {
        index = func_15195868((u8 *)displayList, assetId, searchOccurrence, &tileCount);
        if (index == -1) {
            occurrence = 0;
        } else {
            if (assetId == 0) {
                assetId = D_800E08F0;
            }
            key = separate ? -1 : assetId;
            record = (u8 *)D_800E08E8;
            while (record != NULL && *(s16 *)(record + 8) != key) {
                record = *(u8 **)(record + 4);
            }
            packedSize = *(s32 *)((u8 *)displayList + (index << 3) + 4);
            packedScale = *(s32 *)((u8 *)displayList + (index << 3));
            if (record == NULL) {
                record = (u8 *)func_15195984(assetId, packedSize, packedScale, doubleSize);
                if (record != NULL) {
                    record[0x12] = field12;
                    record[0x13] = field13;
                    separate = 0;
                } else {
                    return 0;
                }
            } else {
                index = func_15195A84(index, (s32)record, packedSize, doubleSize);
                separate = 0;
            }
            if (record[0x14] < tileCount) {
                record[0x14] = tileCount;
            }
            func_15195D00((u8 *)record, displayList, index, tileCount);
            searchOccurrence++;
        }
    } while (occurrence == -1);
    if (assetId == D_800E08F0) {
        D_800E08F0--;
    }
    return (s32)record;
}


/* Return the complete handle produced by the bank request helper. */
s32 func_15195FB0(u8 *arg0, s32 arg1, s32 arg2, s32 arg3, s32 arg4, s32 arg5, s32 arg6) {
    return func_15195DD4(*(s32 *) (arg0 + 0x1C), arg1, arg2, arg3, arg4, arg5, arg6);
}

/* Emit the current texture offsets, then advance and wrap the next phase. */
void func_15195FF0(s32 primaryList, s32 secondaryList) {
    s32 slot;
    u32 tileWords[8];
    u8 *record;
    u8 *association;
    u8 *nextAssociation;
    s32 u;
    s32 v;
    s32 width;
    s32 height;
    s32 initialV;
    s32 tileU;
    s32 tileV;
    s32 level;
    s32 commandIndex;
    u32 *output;
    u8 *indices;
    u8 *counts;

    record = (u8 *)D_800E08E8;
    while (record != NULL) {
        u = *(u16 *)(record + 0x0E);
        v = *(u16 *)(record + 0x10);
        width = *(s16 *)(record + 0x0A);
        height = *(s16 *)(record + 0x0C);
        tileU = u / 8 + 2;
        initialV = v / 8 + 2;
        tileV = initialV;
        level = 0;
        slot = 0;
        if (tileU >= width) {
            tileU -= width;
        }
        if (initialV >= height) {
            tileV = initialV - height;
        }
        while (level < 8 && level < record[0x14]) {
            tileWords[level] = ((u32)G_SETTILESIZE << 24) |
                ((tileU & 0xFFF) << 12) | (tileV & 0xFFF);
            level++;
            tileU /= 2;
            tileV /= 2;
        }
        width *= 8;
        height *= 8;
        if (D_800BEAC0 == 0) {
            u = (s32)((u32)u + (u32)*(s8 *)(record + 0x12) * (u32)D_800BE9E4);
            v = (s32)((u32)v + (u32)*(s8 *)(record + 0x13) * (u32)D_800BE9E4);
        }
        if (u < 0) {
            u = (s32)((u32)u + (u32)width);
        } else if (u >= width) {
            u = (s32)((u32)u - (u32)width);
        }
        if (v < 0) {
            v = (s32)((u32)v + (u32)height);
        } else if (v >= height) {
            v = (s32)((u32)v - (u32)height);
        }
        commandIndex = *(s16 *)(record + 0x1C);
        *(u16 *)(record + 0x0E) = u;
        *(u16 *)(record + 0x10) = v;
        if (commandIndex != -1) {
            indices = record;
            counts = record;
            do {
                commandIndex = *(s16 *)(indices + 0x1C);
                level = 0;
                output = (u32 *)primaryList + commandIndex * 2;
                while (level < counts[0x30]) {
                    *output = tileWords[level];
                    level++;
                    output += 4;
                }
                slot += 2;
                indices += 2;
                counts++;
            } while (slot < 10 && *(s16 *)(indices + 0x1C) != -1);
        }
        slot = 0;
        indices = record;
        counts = record;
        if (*(s16 *)(record + 0x26) != -1) {
            do {
                commandIndex = *(s16 *)(indices + 0x26);
                level = 0;
                output = (u32 *)secondaryList + commandIndex * 2;
                while (level < counts[0x35]) {
                    *output = tileWords[level];
                    level++;
                    output += 4;
                }
                slot += 2;
                indices += 2;
                counts++;
            } while (slot < 10 && *(s16 *)(indices + 0x26) != -1);
        }
        association = *(u8 **)(record + 0x18);
        while (association != NULL) {
            commandIndex = *(u16 *)(association + 0x0C);
            level = 0;
            slot = commandIndex * 8;
            while (level < association[0x0E]) {
                *(u32 *)(*(s32 *)(association + 8) + slot) = tileWords[level];
                level++;
                slot += 0x10;
            }
            nextAssociation = *(u8 **)(association + 0x10);
            association = NULL;
            if (nextAssociation != NULL) {
                association = nextAssociation;
            }
        }
        record = *(u8 **)(record + 4);
    }
}



void func_15196318(u8 *arg0, s32 arg1, s32 arg2) {
    if (arg0 != NULL) {
        arg0[0x12] = arg1;
        arg0[0x13] = arg2;
    }
}

/* Note 320: guarded words preserve retail's pointer and selector registers. */
s32 func_15196330(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s8 temp_v1 = *(s8 *) (temp_v0 + 0x65);

    if (temp_v1 != -1) {
        D_8008F898[temp_v1](arg0);
    }
    temp_v1 = *(s8 *) (temp_v0 + 0x62);
    if (temp_v1 != -1) {
        D_8008F88C[temp_v1](arg0);
    }
    func_151478F4(arg0);
}

/* Note 321: guarded words preserve retail's pointer and selector registers. */
s32 func_151963B4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    s8 temp_v1 = *(s8 *) (temp_v0 + 0x65);

    if (temp_v1 != -1) {
        D_8008F898[temp_v1](arg0);
    }
    temp_v1 = *(s8 *) (temp_v0 + 0x62);
    if (temp_v1 != -1) {
        D_8008F88C[temp_v1](arg0);
    }
    func_15147928(arg0);
}

typedef struct { f32 axis[3]; } EffectPoint15196438;
typedef struct {
    s16 lifetime;
    u16 pad02;
    f32 firstScale, secondScale;
    u8 mode, pad0D[3];
    s32 count;
    u8 matrixIndex, pad15[3];
    EffectPoint15196438 localPoint, localEnd;
    s8 scaleCallback;
    u8 field31, field32, field33;
    f32 field34, field38;
    s8 setupCallback, tickCallback, finishCallback, soundCallback;
    s8 field40, field41, field42;
    u8 pad43;
    u16 flags;
    u8 field46, field47;
    f32 field48;
    u8 field4C, pad4D[3];
    f32 field50;
    u8 field54, pad55[3];
    f32 field58;
    u8 field5C, field5D, field5E, field5F;
} EffectPreset15196438;
typedef struct {
    struct127 *owner;
    u8 ownerId, matrixIndex, kind;
    s8 scaleCallback;
    EffectPoint15196438 localPoint, localEnd, point, end;
    f32 scale, field3C, firstScale, gap44, secondScale, field4C;
    u8 field50, mode, field52, field53, field54, gap55[3];
    f32 field58, field5C;
    s8 setupCallback, tickCallback, finishCallback, soundCallback;
    s8 field64, field65;
    u16 soundHandle;
    s8 field68;
    u8 field69, field6A, gap6B;
    f32 field6C, field70;
    u8 field74, gap75[3];
    f32 field78, field7C;
    u8 field80, gap81[3];
    f32 field84, field88;
    u8 field8C, field8D, field8E, field8F;
} EffectPayload15196438;
typedef struct {
    EffectPoint15196438 point;
    s16 lifetime;
    u16 flags;
    s32 kind;
    u8 gap14, count, gap16[2];
    s32 gap18;
} EffectRequest15196438;
extern EffectPreset15196438 D_800A87A0[];
extern s32 (*D_8008F890[])(void);
extern f32 (*D_8008F870[])(s32);
extern void (*D_8008F87C[])(u8 *);
void func_15143134(f32 *, f32 *, u8 *);
u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32, void *, u8, s32);
u16 func_10010F30(s32, u16, u8, s16, u8);

/* Build a preset character effect at two transformed actor attachment points. */
u8 *func_15196438(struct127 *actor, s32 presetIndex, s32 channel, s32 context) {
    EffectRequest15196438 request;
    EffectPayload15196438 effect;
    u8 *created;
    u8 *matrix;
    EffectPreset15196438 *preset;
    EffectPayload15196438 *payload;

    if (actor == NULL) {
        return NULL;
    }
    if (actor->unk1D4 == NULL) {
        return NULL;
    }
    effect.owner = actor;
    effect.ownerId = actor->unique_id;
    effect.kind = 2;
    preset = &D_800A87A0[presetIndex];
    effect.field50 = 0;
    effect.field4C = 0.0f;
    effect.field70 = 0.0f;
    effect.field7C = 0.0f;
    effect.field88 = 0.0f;
    effect.setupCallback = preset->setupCallback;
    effect.tickCallback = preset->tickCallback;
    effect.finishCallback = preset->finishCallback;
    request.lifetime = preset->lifetime;
    effect.firstScale = preset->firstScale;
    effect.secondScale = preset->secondScale;
    effect.mode = preset->mode;
    request.count = preset->count;
    effect.matrixIndex = preset->matrixIndex;
    effect.localPoint = preset->localPoint;
    effect.localEnd = preset->localEnd;
    effect.field80 = preset->field54;
    effect.soundCallback = preset->soundCallback;
    effect.scaleCallback = preset->scaleCallback;
    effect.field52 = preset->field31;
    effect.field53 = preset->field32;
    effect.field54 = preset->field33;
    request.flags = preset->flags;
    effect.field6A = preset->field47;
    effect.field74 = preset->field4C;
    effect.field58 = preset->field34;
    effect.field5C = preset->field38;
    effect.field6C = preset->field48;
    effect.field78 = preset->field50;
    effect.field84 = preset->field58;
    effect.field64 = preset->field40;
    effect.field65 = preset->field41;
    effect.field68 = preset->field42;
    effect.field69 = preset->field46;
    effect.field8C = preset->field5C;
    effect.field8D = preset->field5D;
    effect.field8E = preset->field5E;
    effect.field8F = preset->field5F;
    if (effect.soundCallback != -1) {
        effect.soundHandle = D_8008F890[effect.soundCallback]();
    } else {
        effect.soundHandle = 0;
    }
    matrix = (u8 *)effect.owner->unk1D4 + (effect.matrixIndex << 6);
    func_15143134(effect.localPoint.axis, effect.point.axis, matrix);
    func_15143134(effect.localEnd.axis, effect.end.axis, matrix);
    request.point.axis[0] = effect.point.axis[0];
    request.point.axis[1] = effect.point.axis[1];
    request.point.axis[2] = effect.point.axis[2];
    effect.field3C = 0.0f;
    request.kind = 3;
    created = func_15147A80(&request, 0x90, 0x24, 2, 2, 2, 0, 0,
                          NULL, (u8)channel, context);
    if (created != NULL) {
        payload = (EffectPayload15196438 *)*(u8 **)(created + 0x98);
        memcpy(payload, &effect, 0x90);
        if (payload->scaleCallback != -1) {
            payload->scale = D_8008F870[payload->scaleCallback]((s32)created);
        } else {
            payload->scale = 0.0f;
        }
        if (effect.setupCallback != -1) {
            D_8008F87C[effect.setupCallback](created);
        }
    }
    return created;
}



typedef struct {
    EffectPoint15196438 point;
    f32 velocity[3];
    f32 size;
    s16 lifetime;
    s8 delay;
    u8 mark, field20, field21, gap22[2];
} EffectRecord15196748;

struct PointSoundOwner;
extern void (*D_8008F894[])(struct PointSoundOwner *);
extern void (*D_8008F89C[])(s32);
extern s32 (*D_8008F880[])(u8 *);
/* Unrecovered callee: observed arguments are (u8 *owner, s32 index). */
void func_15198110(u8 *, s32);


/* Integrate the live ring, retire expired entries and apply both mark ramps. */
s32 func_15196748(u8 *owner) {
    EffectPayload15196438 *payload;
    EffectRecord15196748 *records;
    s32 cursor;
    EffectRecord15196748 *record;
    s16 remaining;
    u8 flags;
    u8 ramp;

    payload = (EffectPayload15196438 *)*(u8 **)(owner + 0x98);
    records = (EffectRecord15196748 *)*(u8 **)(owner + 0x94);
    if (*(s8 *)(owner + 0x2C) < 2 && (payload->kind & 1)) {
        return 0;
    }
    cursor = *(s8 *)(owner + 0x2E);
    while (cursor != *(s8 *)(owner + 0x2D)) {
        cursor--;
        if (cursor < 0) {
            cursor = owner[0x25] - 1;
        }
        record = &records[cursor];
        record->velocity[1] += payload->firstScale * D_800BE9A4;
        record->point.axis[0] += record->velocity[0] * D_800BE9A4;
        record->point.axis[1] += record->velocity[1] * D_800BE9A4;
        record->point.axis[2] += record->velocity[2] * D_800BE9A4;
        record->mark = 255;
        if (record->delay > 0) {
            record->delay = (u32)(s32)record->delay - (u32)D_800BE9E4;
        } else {
            record->lifetime -= (u32)payload->field52 * (u32)D_800BE9E4;
        }
        if (record->lifetime < payload->field6A && record->field21 == 0) {
            func_15198110(owner, cursor);
        }
        record->size += payload->field58 * D_800BE9A4;
        if (record->lifetime < 0) {
            payload->kind &= ~2;
            while (cursor != *(s8 *)(owner + 0x2D)) {
                owner[0x2D] = *(s8 *)(owner + 0x2D) + 1;
                if (*(s8 *)(owner + 0x2D) == owner[0x25]) {
                    owner[0x2D] = 0;
                }
                owner[0x2C] = *(s8 *)(owner + 0x2C) - 1;
            }
            records[*(s8 *)(owner + 0x2D)].lifetime = 0;
        }
    }
    cursor = *(s8 *)(owner + 0x2D);
    flags = payload->kind;
    if (flags & 2) {
        ramp = 0;
        remaining = payload->field8C;
        do {
            records[cursor].mark = ramp;
            remaining--;
            cursor++;
            ramp += payload->field8D;
            if (cursor == owner[0x25]) {
                cursor = 0;
            }
        } while (remaining != 0 && cursor != *(s8 *)(owner + 0x2E));
        flags = payload->kind;
    }
    if (flags & 4) {
        cursor = *(s8 *)(owner + 0x2E);
        ramp = 0;
        remaining = payload->field8E;
        cursor--;
        if (cursor < 0) {
            cursor = owner[0x25] - 1;
        }
        do {
            record = &records[cursor];
            remaining--;
            cursor--;
            record->mark = (record->mark * ramp) >> 8;
            ramp += payload->field8F;
            if (cursor < 0) {
                cursor = owner[0x25] - 1;
            }
        } while (remaining != 0 && cursor != *(s8 *)(owner + 0x2E));
    }
    if (payload->field64 != -1) {
        D_8008F894[payload->field64]((struct PointSoundOwner *)owner);
    }
    if (payload->field68 != -1) {
        D_8008F89C[payload->field68]((s32)owner);
    }
    if (payload->tickCallback != -1) {
        if (D_8008F880[payload->tickCallback](owner) == 0) {
            return 0;
        }
    }
    if (*(s8 *)(owner + 0x2C) > 0) {
        *(EffectPoint15196438 *)(owner + 0x54) = records[*(s8 *)(owner + 0x2D)].point;
    } else {
        *(f32 *)(owner + 0x54) = 0.0f;
        *(f32 *)(owner + 0x58) = 0.0f;
        *(f32 *)(owner + 0x5C) = 0.0f;
    }
    return 1;
}



/* Unrecovered helper bodies: only their two observed pointer arguments are restored. */
void func_15198D88(u8 *, f32 *);
void func_151990AC(u8 *, f32 *);

/* Emit interpolated ring entries between the two transformed attachment points. */
/* Emit interpolated ring entries between the two transformed attachment points. */
/* Emit interpolated ring entries between the two transformed attachment points. */
s32 func_15196B4C(u8 *owner) {
    f32 inversePhase;
    u32 random;
    EffectPoint15196438 transformedEnd;
    f32 elapsed;
    f32 elapsedStep;
    f32 speed;
    f32 size;
    f32 xStep;
    f32 yStep;
    f32 zStep;
    f32 endXStep;
    f32 endYStep;
    f32 endZStep;
    f32 sizeStep;
    EffectPoint15196438 point;
    EffectPoint15196438 end;
    f32 speedStep;
    EffectPoint15196438 pointDifference;
    EffectPoint15196438 endDifference;
    f32 sizeDifference;
    f32 speedDifference;
    f32 zVelocity;
    EffectPoint15196438 *previousPoint, *previousEnd;
    EffectPayload15196438 *payload;
    EffectRecord15196748 *records, *record;
    u8 *matrix, *matrixBase;
    s8 selector, head;

    payload = (EffectPayload15196438 *)*(u8 **)(owner + 0x98);
    records = (EffectRecord15196748 *)*(u8 **)(owner + 0x94);
    matrixBase = (u8 *)payload->owner->unk1D4;
    if (matrixBase == 0) {
        return 0;
    }
    selector = payload->scaleCallback;
    if (selector != -1) {
        payload->gap44 = D_8008F870[selector]((s32)owner);
        matrixBase = (u8 *)payload->owner->unk1D4;
    }
    matrix = matrixBase + payload->matrixIndex * 64;
    func_15143134(payload->localPoint.axis, (f32 *)(owner + 0x10), matrix);
    func_15143134(payload->localEnd.axis, transformedEnd.axis, matrix);
    previousPoint = &payload->point;
    payload->field4C += payload->secondScale * D_800BE9A4;
    if (payload->field4C > 1.0f) {
        inversePhase = 1.0f / payload->field4C;
        elapsed = payload->field3C + D_800BE9A4;
        point = payload->point;
        previousEnd = &payload->end;
        end = payload->end;
        elapsedStep = elapsed * inversePhase;
        speed = payload->scale;
        size = payload->field5C + payload->field58 * elapsed;
        pointDifference.axis[0] = *(f32 *)(owner + 0x10) - payload->point.axis[0];
        pointDifference.axis[1] = *(f32 *)(owner + 0x14) - payload->point.axis[1];
        pointDifference.axis[2] = *(f32 *)(owner + 0x18) - payload->point.axis[2];
        endDifference.axis[0] = transformedEnd.axis[0] - payload->end.axis[0];
        endDifference.axis[1] = transformedEnd.axis[1] - payload->end.axis[1];
        endDifference.axis[2] = transformedEnd.axis[2] - payload->end.axis[2];
        sizeDifference = payload->field5C - size;
        speedDifference = payload->gap44 - speed;
        xStep = pointDifference.axis[0] * inversePhase;
        yStep = pointDifference.axis[1] * inversePhase;
        zStep = pointDifference.axis[2] * inversePhase;
        endXStep = endDifference.axis[0] * inversePhase;
        endYStep = endDifference.axis[1] * inversePhase;
        endZStep = endDifference.axis[2] * inversePhase;
        sizeStep = sizeDifference * inversePhase;
        speedStep = speedDifference * inversePhase;
        do {
            payload->field7C += payload->field78;
            if (payload->field7C > 1.0f) {
                func_15198D88(owner, transformedEnd.axis);
            }
            payload->field88 += payload->field84;
            if (payload->field88 > 1.0f) {
                func_151990AC(owner, transformedEnd.axis);
            }
            records[*(s8 *)(owner + 0x2E)].field21 = 0;
            records[*(s8 *)(owner + 0x2E)].point.axis[0] = point.axis[0];
            records[*(s8 *)(owner + 0x2E)].point.axis[1] = point.axis[1];
            records[*(s8 *)(owner + 0x2E)].point.axis[2] = point.axis[2];
            records[*(s8 *)(owner + 0x2E)].velocity[0] = (end.axis[0] - point.axis[0]) * speed;
            records[*(s8 *)(owner + 0x2E)].velocity[1] = (end.axis[1] - point.axis[1]) * speed;
            records[*(s8 *)(owner + 0x2E)].velocity[2] = (end.axis[2] - point.axis[2]) * speed;
            records[*(s8 *)(owner + 0x2E)].size = size;
            records[*(s8 *)(owner + 0x2E)].lifetime = payload->field53;
            records[*(s8 *)(owner + 0x2E)].delay = payload->field54;
            records[*(s8 *)(owner + 0x2E)].mark = 255;
            records[*(s8 *)(owner + 0x2E)].field20 = payload->field50;
            random = (u32)func_150ADA20();
            payload->field50 = payload->field50 + (random % 6U) + 3;
            record = &records[*(s8 *)(owner + 0x2E)];
            record->velocity[1] += payload->firstScale * elapsed;
            record = &records[*(s8 *)(owner + 0x2E)];
            record->point.axis[0] += record->velocity[0] * elapsed;
            record = &records[*(s8 *)(owner + 0x2E)];
            record->point.axis[1] += record->velocity[1] * elapsed;
            record = &records[*(s8 *)(owner + 0x2E)];
            zVelocity = record->velocity[2] * elapsed;
            elapsed -= elapsedStep;
            record->point.axis[2] += zVelocity;
            owner[0x2E] = *(s8 *)(owner + 0x2E) + 1;
            if (owner[0x25] == *(s8 *)(owner + 0x2E)) {
                owner[0x2E] = 0;
            }
            head = *(s8 *)(owner + 0x2D);
            owner[0x2C] = *(s8 *)(owner + 0x2C) + 1;
            if (head == *(s8 *)(owner + 0x2E)) {
                owner[0x2D] = head + 1;
                if (owner[0x25] == *(s8 *)(owner + 0x2D)) {
                    owner[0x2D] = 0;
                }
                owner[0x2C] = *(s8 *)(owner + 0x2C) - 1;
            }
            point.axis[0] += xStep;
            point.axis[1] += yStep;
            point.axis[2] += zStep;
            end.axis[0] += endXStep;
            end.axis[1] += endYStep;
            end.axis[2] += endZStep;
            speed += speedStep;
            size += sizeStep;
            payload->field4C -= 1.0f;
        } while (payload->field4C > 1.0f);
        *previousPoint = point;
        *previousEnd = end;
        payload->scale = speed;
        payload->field3C = elapsed;
    }
    return 1;
}





s32 func_15197148() {
    return 0;
}

f32 func_151979F8(s32 arg0) {
    return D_800A8AA4;
}

f32 func_15197A0C(s32 arg0) {
    return (f32) func_151422C0(0xA, &D_800A8A40, 1, 0x1F4, &D_800A8A48, 0x8CC) * D_800A8AA8;
}

f32 func_15197A68(s32 arg0) {
    return D_800A8AAC;
}

void func_15197A7C(u8 *arg0) {
    struct {
        u8 *ptr;
        u8 value;
    } temp;

    if (arg0 != NULL) {
        temp.ptr = arg0;
        temp.value = arg0[0x3B];
        func_15147D64(&temp, 8);
    }
}

/* Damp and accelerate each velocity triple, then advance its own point. */
s32 func_15197AB4(DualDampedMotion15197AB4 *motion) {
    f32 damping = motion->damping;
    f32 acceleration = motion->verticalAcceleration;
    f32 endDamping = motion->endDamping;

    motion->velocity[0] *= damping;
    motion->velocity[1] += acceleration * D_800BE9A4;
    motion->velocity[2] *= damping;
    motion->endVelocity[0] *= endDamping;
    motion->endVelocity[1] += acceleration * D_800BE9A4;
    motion->endVelocity[2] *= endDamping;
    motion->position[0] += motion->velocity[0] * D_800BE9A4;
    motion->position[1] += motion->velocity[1] * D_800BE9A4;
    motion->position[2] += motion->velocity[2] * D_800BE9A4;
    motion->endPoint[0] += motion->endVelocity[0] * D_800BE9A4;
    motion->endPoint[1] += motion->endVelocity[1] * D_800BE9A4;
    motion->endPoint[2] += motion->endVelocity[2] * D_800BE9A4;
    return 1;
}

s32 func_15197BBC(u8 *arg0) {
    Generated1C2C60Record *self = (void *) arg0;
    f32 temp_f0 = self->value30;
    f32 temp_f2 = self->factor;
    f32 temp_f12 = self->value2C;
    s16 temp_v0 = self->timer;

    self->value30 = temp_f0 - temp_f0 * temp_f2;
    self->value2C = temp_f12 - temp_f12 * temp_f2;
    if (temp_v0 < self->limit) {
        self->value5C = temp_v0 * (u32) self->scale;
    }
    return 1;
}

s32 func_15197C10() {
    return 0;
}

typedef struct {
    u8 *object;
    u8 identifier;
    u8 reserved5[3];
} BoundObjectReference;
void func_151993B4(u8 *);
void func_1516972C(u8 *);

/* Retire a matching bound object, or update its reference after replacement. */
void func_15198054(u8 *owner, s32 eventAddress, u8 command) {
    u8 *event = (u8 *)eventAddress;
    BoundObjectReference *reference = *(BoundObjectReference **)(owner + 0x98);

    if ((command == 0) || (command == 2) || (command == 8)) {
        if ((reference->object == *(u8 **)event) ||
            (reference->identifier == event[4])) {
            func_151993B4(owner);
        }
    } else if (command == 0x2D) {
        u8 *object = *(u8 **)event;
        if (object == reference->object) {
            reference->object = *(u8 **)(event + 4);
            reference->identifier = event[9];
        } else if (reference->object == *(u8 **)(event + 4)) {
            reference->object = object;
            reference->identifier = event[8];
        }
    }
}


/* Unrecovered spawn helper; only its observed two-word void ABI is known. */
void func_15198110(u8 *owner, s32 index) {
}

s32 func_15198570(u8 *owner) {
    return 0;
}

extern struct127 D_800CC2D0[26];
extern s32 D_800D121C;
extern f32 D_800A8ADC;
/* Retire ring entries whose points overlap another live actor. */
s32 func_151987CC(u8 *owner) {
    EffectPayload15196438 *payload;
    EffectRecord15196748 *records;
    struct127 *actor;
    EffectPoint15196438 point;
    s32 cursor;
    f32 width;
    f32 height;
    f32 dx;
    f32 dy;
    f32 dz;

    payload = (EffectPayload15196438 *)*(u8 **)(owner + 0x98);
    records = (EffectRecord15196748 *)*(u8 **)(owner + 0x94);
    actor = D_800CC2D0;
    do {
        if (actor->interaction_state != 0 && actor->unk65 == 0 &&
            actor->unique_id != payload->owner->unique_id) {
            cursor = *(s8 *)(owner + 0x2E);
            while (cursor != *(s8 *)(owner + 0x2D)) {
                    cursor--;
                    if (cursor < 0) {
                        cursor = owner[0x25] - 1;
                    }
                    width = actor->unkE4;
                    height = actor->unkE6;
                    point = records[cursor].point;
                    dx = point.axis[0] - actor->x_position;
                    dz = point.axis[2] - actor->z_position;
                    dy = point.axis[1] - (actor->y_position + (s16)actor->unkE8);
                    dy *= (1.0f + width / height) * 0.5f;
                    if (dx * dx + dy * dy + dz * dz < width * width + 2500.0f) {
                        while (cursor != *(s8 *)(owner + 0x2D)) {
                            (*(s8 *)(owner + 0x2D))++;
                            if (*(s8 *)(owner + 0x2D) == owner[0x25]) {
                                *(s8 *)(owner + 0x2D) = 0;
                            }
                            (*(s8 *)(owner + 0x2C))--;
                        }
                    }
            }
        }
        actor++;
    } while (actor != (struct127 *)&D_800D121C);
    return 1;
}


s32 func_1519897C(u8 *owner) {
    return 0;
}

s32 func_15198C60(void) {
    return func_10010F30(0x1AA, 0x7FFF, 0x40, 0, 0);
}

typedef struct { f32 x, y, z; u8 opaque[24]; } SoundPoint36;
typedef struct { f32 x, y, z; u8 opaque[28]; } SoundPoint40;
typedef struct PointSoundOwner {
    u8 opaque0[0x2C];
    s8 active, index;
    u8 opaque2E[0x66];
    void *points;
    u8 *audio;
} PointSoundOwner;
void func_1000F91C(u16, u16, s16, u8, s32, s16, s16, s16, s16, s16);

/* Refresh the active point's sound position using the signed point index. */
void func_15198C90(PointSoundOwner *state) {
    u8 *audio = state->audio;
    SoundPoint36 *points = state->points;
    u16 handle;

    if (state->active != 0) {
        handle = *(u16 *)(audio + 0x66);
        if (handle != 0) {
            func_1000F91C(handle, 0x7FFF, 0, 0, 0,
                          (s32)points[state->index].x, (s32)points[state->index].y,
                          (s32)points[state->index].z, 500, 5000);
        }
    }
}

void func_15198D40(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    if (*(s8 *) (arg0 + 0x2C) != 0) {
        u16 value = *(u16 *) (temp_v0 + 0x66);

        if (value != 0) {
            func_100111C8(value);
        }
    }
}

void func_15198D7C(s32 arg0) {
}

/* Unrecovered emitter helper; observed two-pointer void interface only. */
void func_15198D88(u8 *owner, f32 *point) {
}

/* Unrecovered emitter helper; observed two-pointer void interface only. */
void func_151990AC(u8 *owner, f32 *point) {
}

void func_151993B4(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    *(u16 *) (arg0 + 0x1E) &= 0xFFFD;
    *(arg0 + 0x30) = 0;
    *(temp_v0 + 6) |= 1;
    *(temp_v0 + 6) |= 4;
}

/* Note 390: guards preserve the object-ID register in these structural twins. */
void func_151993E4(u8 *arg0) {
    u8 *outer = *(u8 **) (arg0 + 0x98);
    u8 *object = *(u8 **) outer;
    s32 index = 0;
    s32 found = 0;
    u8 object_id = object[0x3B];
    u8 *id = D_800A8A9C;

    do {
        if (object_id == *id) {
            found = 1;
        } else {
            index++;
            id++;
        }
    } while ((found == 0) && (index < 6));

    if (found != 0) {
        D_800E0900[index][0x14] = 0;
    }
}

void func_1519944C(u8 *arg0) {
    u8 *outer = *(u8 **) (arg0 + 0x98);
    u8 *object = *(u8 **) outer;
    s32 index = 0;
    s32 found = 0;
    u8 object_id = object[0x3B];
    u8 *id = D_800A8A9C;

    do {
        if (object_id == *id) {
            found = 1;
        } else {
            index++;
            id++;
        }
    } while ((found == 0) && (index < 6));

    if (found != 0) {
        D_800E0900[index][0x14] = 1;
    }
}

s32 func_151994B8() {
    return 0;
}

void func_15199834(u8 *arg0) {
    struct {
        u8 *ptr;
        u8 value;
    } temp;

    if (arg0 != NULL) {
        temp.ptr = arg0;
        temp.value = arg0[0x3B];
        func_15147D64(&temp, 0x26);
    }
}

/* Retire a matching bound object, or update its reference after replacement. */
void func_1519986C(u8 *owner, s32 eventAddress, u8 command) {
    u8 *event = (u8 *)eventAddress;
    BoundObjectReference *reference = *(BoundObjectReference **)(owner + 0x98);

    if ((command == 0) || (command == 2) || (command == 0x26)) {
        if ((reference->object == *(u8 **)event) ||
            (reference->identifier == event[4])) {
            func_1516972C(owner);
        }
    } else if (command == 0x2D) {
        u8 *object = *(u8 **)event;
        if (object == reference->object) {
            reference->object = *(u8 **)(event + 4);
            reference->identifier = event[9];
        } else if (reference->object == *(u8 **)(event + 4)) {
            reference->object = object;
            reference->identifier = event[8];
        }
    }
}


s32 func_15199928(s32 arg0) {
    func_15199980(arg0);
    func_151478F4(arg0);
}

s32 func_15199954(s32 arg0) {
    func_15199980(arg0);
    func_15147928(arg0);
}

s32 func_15199980(u8 *arg0) {
    u8 *temp_v1 = *(u8 **) (arg0 + 0x98);
    s8 temp_v0 = *(s8 *) (temp_v1 + 0x39);
    void *temp_a0;

    if (temp_v0 != -1) {
        D_8008F8C0[temp_v0](arg0);
    }
    temp_v0 = *(s8 *) (temp_v1 + 0x36);
    if (temp_v0 != -1) {
        D_8008F8B4[temp_v0](arg0);
    }
    temp_a0 = *(void **)(temp_v1 + 0x148);
    if (temp_a0 != NULL) {
        func_1516972C(temp_a0);
    }
}

s32 func_15199A10() {
    return 0;
}

s32 func_15199C34() {
    return 0;
}

s32 func_1519A9A4() {
    return 0;
}

s32 func_1519B4B8() {
    return 0;
}

typedef struct {
    f32 x, y, z;
} KinematicVector;

/* Advance position from saved velocity and apply vertical acceleration. */
void func_1519BE1C(KinematicVector *position, KinematicVector *velocity,
                   f32 acceleration, f32 timestep) {
    KinematicVector saved = *velocity;
    velocity->y += acceleration * timestep;
    position->x += saved.x * timestep;
    position->y += saved.y * timestep + 0.5f * acceleration * timestep * timestep;
    position->z += saved.z * timestep;
}

void func_1519BEB8(u8 *arg0) {
    u8 *outer = *(u8 **) (arg0 + 0x98);
    u8 *object = *(u8 **) outer;
    s32 index = 0;
    s32 found = 0;
    u8 object_id = object[0x3B];
    u8 *id = D_800A8A9C;

    do {
        if (object_id == *id) {
            found = 1;
        } else {
            index++;
            id++;
        }
    } while ((found == 0) && (index < 6));

    if (found != 0) {
        D_800E0900[index][0x14] = 0;
    }
}

void func_1519BF20(u8 *arg0) {
    u8 *outer = *(u8 **) (arg0 + 0x98);
    u8 *object = *(u8 **) outer;
    s32 index = 0;
    s32 found = 0;
    u8 object_id = object[0x3B];
    u8 *id = D_800A8A9C;

    do {
        if (object_id == *id) {
            found = 1;
        } else {
            index++;
            id++;
        }
    } while ((found == 0) && (index < 6));

    if (found != 0) {
        D_800E0900[index][0x14] = 1;
    }
}

s32 func_1519BF8C(void) {
    func_10010F30(0x1AA, 0x7FFF, 0x40, 0, 0);
}

/* Refresh the active point's sound position using the signed point index. */
void func_1519BFBC(PointSoundOwner *state) {
    u8 *audio = state->audio;
    SoundPoint40 *points = state->points;
    u16 handle;

    if (state->active != 0) {
        handle = *(u16 *)(audio + 0x130);
        if (handle != 0) {
            func_1000F91C(handle, 0x7FFF, 0, 0, 0,
                          (s32)points[state->index].x, (s32)points[state->index].y,
                          (s32)points[state->index].z, 500, 5000);
        }
    }
}

void func_1519C06C(arg0, arg1)
u8 *arg0;
s32 arg1;
{
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg1 = *(u16 *) (temp_v0 + 0x130);
    if (arg1 != 0) {
        func_100111C8(arg1);
    }
}

extern f32 D_800A8AF8;
struct225 *func_151602C0(Header *, Header2 *, s32, s32, s32, s32, u8, u8, s32, u8, s32);
typedef struct { f32 first, second, third, fourth, fifth, sixth, seventh, eighth; } EffectConfig1519C09C;
/* Build a configured effect and retain its owner pointer. */
struct225 *func_1519C09C(void *owner, f32 *position, u8 a, u8 b, u8 c, u8 d, u8 priority, s32 userData) {
    struct225 *result;
    Header header;
    Header2 coords;
    void *savedOwner;
    EffectConfig1519C09C config;
    config.first = 35.0f;
    config.second = 5.0f;
    header.unk0 = 2;
    header.unk1 = 2;
    header.unk2 = 300;
    header.unk4 = 0x22;
    config.third = 110.0f;
    config.fourth = 1.0f;
    savedOwner = owner;
    config.fifth = 0.0f;
    config.sixth = 7.0f;
    config.seventh = D_800A8AF8;
    config.eighth = 127.0f;
    coords.unk0 = (s32)position[0];
    coords.unk4 = (s32)position[1];
    coords.unk8 = (s32)position[2];
    result = func_151602C0(&header, &coords, a, b, c, d, 255, 0, 0x24, priority, userData);
    if (result != 0) {
        memcpy((u8 *)result + 0x18, &config, 0x20);
        memcpy((u8 *)result + 0x38, &savedOwner, 4);
    }
    return result;
}


s32 func_1519C200(s32 arg0) {
    func_1519C258(arg0);
    func_151617C4(arg0);
}

s32 func_1519C22C(s32 arg0) {
    func_1519C258(arg0);
    func_151617E4(arg0);
}

void func_1519C258(u8 *arg0) {
    u8 *temp_v0;

    temp_v0 = *(u8 **)(*(u8 **)(arg0 + 0x38) + 0x98);
    *(s32 *)(temp_v0 + 0x148) = 0;
}

s32 func_1519C26C() {
    return 0;
}

s32 func_1519C4E4(u8 *arg0) {
    Generated1C2C60Params *params = (void *)(arg0 + 0x110);
    s32 count = D_800BE9E4;
    s32 value;

    if (count > 0) {
        do {
            *(f32 *)(arg0 + 0x2C) = *(f32 *)(arg0 + 0x2C) -
                                    *(f32 *)(arg0 + 0x2C) * params->factor;
            *(f32 *)(arg0 + 0x30) = *(f32 *)(arg0 + 0x30) -
                                    *(f32 *)(arg0 + 0x30) * params->factor;
            count--;
        } while (count > 0);
    }

    if (*(s16 *)(arg0 + 0x1C) < params->limit) {
        value = *(s16 *)(arg0 + 0x1C) * (u32)params->scale;
        if (value < arg0[0x5C]) {
            arg0[0x5C] = value;
        }
    }
    return 1;
}

s32 func_1519C56C() {
    return 0;
}

// Matched with guarded equality-operand normalization.
s32 func_1519C910(u8 *arg0, s32 arg1) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    u8 *temp_v1 = *(u8 **) temp_v0;

    arg1 = *(u16 *) (temp_v1 + 0x84);
    if (*(u32 *) (temp_v0 + 0x158) != arg1) {
        if (*(u32 *) (temp_v0 + 0x15C) != arg1) {
            return 0;
        }
    }
    return 1;
}

s32 func_1519C948(s32 arg0) {
    func_1519CDB0(arg0, 0.25f, 0x1C);
    return 0;
}

s32 func_1519C970(s32 arg0) {
    func_1519CDB0(arg0, 0.5f, 0x1D);
    return 0;
}

s32 func_1519C998(s32 arg0) {
    func_1519CDB0(arg0, 0.2f, 0x1D);
    return 0;
}

s32 func_1519C9C4() {
    return 0;
}

void func_1519CD64(u8 *arg0) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x28);

    if ((*(s32 *) (temp_v0) == 0) || (*(u8 *) (temp_v0 + 4) == 0xFF) ||
        (*(u8 *) (arg0 + 0x2C) != *(u8 *) (temp_v0 + 0x3B))) {
        *(s16 *) (arg0 + 0xE) = -1;
        *(u8 *) (arg0 + 0xD) |= 1;
    }
}

s32 func_1519CDB0(s32 arg0, f32 arg1, s32 arg2) {
    return 0;
}
