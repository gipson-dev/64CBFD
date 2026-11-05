#include <ultra64.h>

typedef struct { f32 x, y, z; } Position20A290;
typedef struct {
    s32 count;
    s32 countRange;
    Position20A290 position;
    s16 angle;
    s16 angleRange;
    s16 pitch;
    s16 pitchRange;
    f32 speed;
    f32 speedRange;
    f32 vertical;
    f32 verticalRange;
    s16 lifetime;
    s16 lifetimeRange;
    f32 scale;
    f32 scaleRange;
    f32 spread;
} Configuration20A290;
extern f32 D_800AB558, D_800AB55C, D_800AB560, D_800AB564;
extern s32 D_800AB550;
extern f32 D_800AB554;
void func_15152190(Configuration20A290 *, s32 *, f32 *, s32, f32, u8, u8, s32);

/* Copied-position burst configuration from asm/20A290.s. */

/* Submit the copied position with this burst's fixed configuration and channel. */
void func_151DCDE0(Position20A290 *position, u8 channel, s32 context) {
    Configuration20A290 packet;
    f32 scale = D_800AB558;

    packet.count = 12;
    packet.countRange = 5;
    packet.position = *position;
    packet.angle = 0;
    packet.angleRange = 255;
    packet.pitch = -64;
    packet.pitchRange = 49;
    packet.speed = 3.0f;
    packet.speedRange = 9.0f;
    packet.vertical = D_800AB55C;
    packet.verticalRange = D_800AB560;
    packet.lifetime = 25;
    packet.lifetimeRange = 20;
    packet.scale = scale;
    packet.scaleRange = scale;
    packet.spread = D_800AB564;
    func_15152190(&packet, &D_800AB550, &D_800AB554, 1, 26.0f, 0, channel, context);
}
