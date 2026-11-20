#ifndef CONKER_GAME_MAP_TRAIL_H
#define CONKER_GAME_MAP_TRAIL_H

#include <ultra64.h>

typedef struct MapTrailPoint {
    f32 x, y, z;
} MapTrailPoint;

/* Shared 80-byte input copied by the sampled map-trail constructor. */
typedef struct MapTrailPacket {
    s16 duration;
    u8 enabled, reserved03;
    MapTrailPoint points[4];
    s8 flag;
    u8 reserved35[3];
    s32 pieces;
    f32 width, spread;
    s16 minimum, maximum;
    u8 red, green, blue, alpha, state;
    u8 reserved4D[3];
} MapTrailPacket;

/* Allocate the trail and its endpoint effects, or return NULL on failure. */
void *func_15105CE0(MapTrailPacket *packet, s32 extraBytes, u8 priority, s32 context);

#endif
