#include <ultra64.h>

typedef struct {
    u32 words[9];
} CapturePayload1A11B0;

typedef struct {
    f32 x, y, z;
    u8 state;
    u8 pad0D[3];
    CapturePayload1A11B0 payload;
    s8 callback;
    u8 pad35[3];
    s32 value;
} CaptureRequest1A11B0;

extern CaptureRequest1A11B0 D_800DD348[];
extern CaptureRequest1A11B0 D_800DD3FC[];

/* Non-matching placeholders for the text-only asm slice asm/1A11B0.s. */

s32 func_15173D00() {
    return 0;
}

s32 func_151742EC() {
    return 0;
}

/* Queue a position and optional payload in the first unused capture record. */
s32 func_151745F0(f32 x, f32 y, f32 z, const CapturePayload1A11B0 *payload,
                 s8 callback, s32 value) {
    CaptureRequest1A11B0 *request = D_800DD348;

loop:
    {
        if (request->state == 0) {
            request->x = x;
            request->y = y;
            request->z = z;
            request->state = 3;
            request->callback = callback;
            request->value = value;
            if (payload != NULL) {
                request->payload = *payload;
            }
            return 0;
        }
        request++;
    }
    if (request == D_800DD3FC) {
        return 1;
    }
    goto loop;
}
