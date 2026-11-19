#include <ultra64.h>
#include "structs.h"

/* Local camera view; the shared camera structure still leaves 0x370 opaque. */
typedef struct {
    u8 pad0[0x190];
    f32 verticalOffset;
    u8 pad194[0x1B4];
    f32 distance348;
    f32 distance34C;
    u8 pad350[0x20];
    f32 currentDistance;
    f32 desiredDistance;
    u8 pad378[0x58];
    struct127 *subject;
    u8 pad3D4[0x14];
    u8 transition;
    u8 pad3E9[0x2DF];
    u32 mode;
    u8 pad6CC[0x30];
    u32 override;
} TankCamera1319D0;

void func_15128774(TankCamera1319D0 *, struct127 *);

/* Apply Tank camera defaults and refresh its origin at low horizontal speed. */
void func_15104520(TankCamera1319D0 *camera) {
    struct127 *subject;

    if (camera->override != 0 || camera->mode == 0) {
        camera->distance348 = 117.0f;
        camera->distance34C = 117.0f;
        camera->desiredDistance = 370.0f;
        camera->verticalOffset = 77.0f;
    }
    subject = camera->subject;
    if (subject->xz_velocity < 50.0f && camera->transition == 0) {
        f32 half = 0.5f;
        f32 desired = camera->desiredDistance;
        if (half * desired < camera->currentDistance - desired) {
            func_15128774(camera, subject);
        }
    }
}
