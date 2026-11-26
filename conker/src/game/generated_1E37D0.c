#include <ultra64.h>
typedef struct {
    f32 x;
    f32 y;
    f32 z;
} ActorPosition151B6320;

typedef struct {
    ActorPosition151B6320 position;
    s16 duration;
    u16 flags;
    s32 kind;
    u8 reserved14; /* Preserved stack byte copied by the retail helper. */
    u8 count;
    u8 reserved16[2]; /* Preserved stack bytes copied by the retail helper. */
} ActorEffectRequest151B6320;

typedef struct {
    u8 *owner;
    u8 identity;
    u8 reserved05[3];
    ActorPosition151B6320 position;
    f32 velocityX;
    f32 velocityY;
    f32 lowerBound;
    f32 upperBound;
    f32 velocityZ;
    u32 reserved28; /* Retail copies this untouched stack word. */
} ActorEffectPayload151B6320;

typedef struct {
    ActorEffectPayload151B6320 payload;
    u32 layoutGap; /* Original local spacing; not part of either packet. */
    ActorEffectRequest151B6320 request;
    u32 layoutTail; /* Preserves the original 0x90-byte frame. */
} ActorEffectLocals151B6320;

u8 *func_15147A80(void *, s32, s32, s32, s32, s32, s32, s32,
    void *, u8, s32);
void *memcpy(void *, const void *, unsigned int);

extern void (*D_8008FB98[])(u8 *, s32, u8);

/* Recovered trail callbacks and remaining placeholders from asm/1E37D0.s. */

/* Snapshot one actor position and submit its retail effect packet. */
void func_151B6320(u8 *actor, u8 channel, s32 context) {
    ActorEffectLocals151B6320 locals;
    u8 *record;

    locals.request.count = 10;
    locals.request.position.x = *(f32 *)(actor + 0x14);
    locals.request.position.y = *(f32 *)(actor + 0x18);
    locals.request.position.z = *(f32 *)(actor + 0x1C);
    locals.request.duration = 300;
    locals.request.flags = 6;
    locals.payload.owner = actor;
    locals.payload.identity = actor[0x3B];
    locals.payload.position = locals.request.position;
    locals.payload.velocityX = 0.0f;
    locals.payload.velocityY = 0.0f;
    locals.payload.upperBound = -16384.0f;
    locals.payload.lowerBound = -16384.0f;
    locals.payload.velocityZ = 0.0f;
    locals.request.kind = 13;
    record = func_15147A80(&locals.request, 0x30, 0x1C, 0xB, 0xB, 0xB,
        0, 0, NULL, channel, context);
    if (record != NULL) {
        memcpy(*(void **)(record + 0x98), &locals.payload, 0x2C);
    }
}

s32 func_151B6420() {
    return 0;
}

s32 func_151B65D4() {
    return 0;
}

s32 func_151B6928() {
    return 0;
}

// Matched with guarded event/current register and return scheduling.
void func_151B70B4(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *link;
    u8 *current;
    u8 *first;
    u8 event;

    link = *(u8 **)(arg0 + 0x98);
    event = arg2;
    current = *(u8 **)link;

    if (arg2 == 0) {
        if (*(u8 **)arg1 != current) {
            return;
        }
        arg0[0x30] = 0;
        *(u16 *)(arg0 + 0x1E) |= 8;
        return;
    }

    if (event == 0x2D) {
        first = *(u8 **)arg1;
        if (first == current) {
            *(u8 **)link = *(u8 **)(arg1 + 4);
            link[4] = arg1[9];
            return;
        }
        if (*(u8 **)(arg1 + 4) == current) {
            *(u8 **)link = first;
            link[4] = arg1[8];
        }
    }
}

s32 func_151B7144() {
    return 0;
}

s32 func_151B7328() {
    return 0;
}

typedef struct {
    ActorPosition151B6320 position;
    f32 distance;
    u8 opacity;
    u8 retained11[3];
} TrailRecord151B77F4;
typedef struct { u8 retained00[0x40]; ActorPosition151B6320 position; } TrailAttached151B77F4;
typedef struct {
    TrailAttached151B77F4 *attached;
    void *link;
    u8 callback;
    u8 retained09[3];
} TrailAux151B77F4;
typedef struct {
    u8 retained00[0x10];
    ActorPosition151B6320 position;
    u8 retained1C[9];
    u8 capacity;
    u8 retained26[6];
    s8 count, tail, head;
    u8 retained2F[0x65];
    TrailRecord151B77F4 *records;
    TrailAux151B77F4 *aux;
} TrailOwner151B77F4;
extern s32 D_800BE9E4;
extern s32 (*D_8008FB90[])(void *, void *);
f32 func_15143E64(f32 *);

typedef struct { u8 *record; u8 identity; u8 retained05[3]; } TrailInputLink151B7678;

/* Both table entries accept an owner and a writable position vector. */
s32 func_151B7678(void *owner, void *position) {
    ActorPosition151B6320 *output = position;
    TrailAux151B77F4 *container = ((TrailOwner151B77F4 *)owner)->aux;
    TrailInputLink151B7678 *entry = container->link;
    u8 *record = entry->record;

    if (*(s32 *)record == 0 || entry->identity != record[0x3B]) {
        return 0;
    }
    output->x = *(f32 *)(record + 0x14);
    output->y = *(f32 *)(record + 0x18);
    output->z = *(f32 *)(record + 0x1C);
    return 1;
}

typedef struct { u8 reserved00[0x18]; f32 scaleX, scaleY; f32 rotation[3]; u8 reserved2C[0xC]; f32 translation[3]; } MatrixSource151B76CC;
typedef struct { MatrixSource151B76CC *source; } MatrixLink151B76CC;
void func_150A8050(f32 [4][4], f32, f32, f32);
void func_150A7960(f32 [4][4], f32, f32, f32, f32 *, f32 *, f32 *);
/* Transform a local offset through the linked scaled rotation and translation. */
s32 func_151B76CC(void *owner, void *output) {
    f32 matrix[4][4];
    MatrixSource151B76CC *source = ((MatrixLink151B76CC *)((TrailOwner151B77F4 *)owner)->aux->link)->source;
    func_150A8050(matrix, source->rotation[0], source->rotation[1], source->rotation[2]);
    matrix[3][0] = source->translation[0];
    matrix[3][1] = source->translation[1];
    matrix[3][2] = source->translation[2];
    matrix[0][0] *= source->scaleX; matrix[0][1] *= source->scaleX; matrix[0][2] *= source->scaleX;
    matrix[1][0] *= source->scaleY; matrix[1][1] *= source->scaleY; matrix[1][2] *= source->scaleY;
    matrix[2][0] *= source->scaleX; matrix[2][1] *= source->scaleX; matrix[2][2] *= source->scaleX;
    func_150A7960(matrix, 0.0f, 0.0f, -250.0f, &((ActorPosition151B6320 *)output)->x, &((ActorPosition151B6320 *)output)->y, &((ActorPosition151B6320 *)output)->z);
    return 1;
}

/* Append the callback's position and traveled distance to the trail ring. */
s32 func_151B77F4(TrailOwner151B77F4 *owner) {
    TrailAux151B77F4 *aux = owner->aux;
    TrailRecord151B77F4 *records = owner->records;
    ActorPosition151B6320 previous;
    f32 difference[3];
    TrailRecord151B77F4 *record;
    f32 distance;

    if (D_800BE9E4 > 0) {
        previous = owner->position;
        if (!D_8008FB90[aux->callback](owner, &owner->position)) {
            return 0;
        }
        if (aux->attached != NULL) {
            aux->attached->position = owner->position;
        }
        difference[0] = owner->position.x - previous.x;
        difference[1] = owner->position.y - previous.y;
        difference[2] = owner->position.z - previous.z;
        distance = func_15143E64(difference);
        record = &records[owner->head];
        record->position = owner->position;
        record->distance = distance;
        record->opacity = 255;
        owner->head++;
        if (owner->head == owner->capacity) owner->head = 0;
        owner->count++;
        if (owner->head == owner->tail) {
            owner->tail++;
            if (owner->tail == owner->capacity) owner->tail = 0;
            owner->count--;
        }
    }
    return 1;
}


s32 func_151B7998() {
    return 0;
}

s32 func_151B7C38() {
    return 0;
}

void func_151B82CC(u8 *arg0, s32 arg1, u8 arg2) {
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);
    void (*temp_v1)(u8 *, s32, u8) =
        D_8008FB98[*(temp_v0 + 8)];

    if (temp_v1 != 0) {
        temp_v1(arg0, arg1, arg2);
    }
}

void func_151B8318(u8 *arg0, u8 *arg1, u8 arg2) {
    u8 *container = *(u8 **)(arg0 + 0x98);
    u8 *entry = *(u8 **)(container + 4);

    if (arg2 == 0) {
        s32 value = *(s32 *)arg1;

        if (value == *(s32 *)entry || entry[4] == arg1[4]) {
            func_1516972C(arg0);
        }
    }
}

void func_151B8370(arg0, arg1)
u8 *arg0;
s32 arg1;
{
    u8 *temp_v0 = *(u8 **) (arg0 + 0x98);

    arg1 = *(s32 *) temp_v0;
    if (arg1 != 0) {
        func_1516972C(arg1);
    }
}

s32 func_151B83A0(s32 arg0) {
    func_151B8370(arg0);
    func_151478F4(arg0);
}

s32 func_151B83CC(s32 arg0) {
    func_151B8370(arg0);
    func_15147928(arg0);
}
