#include <ultra64.h>
extern s32 D_80082FA4;
extern u8 *D_800BE628;
extern u8 D_800BE9C0;
extern f32 D_8009DEC0;
extern f32 D_800380A0, D_800380A4;
extern f32 D_800D2C70, D_800D2C74, D_800D2C78, D_800D2C7C;
extern f32 D_800D2C80, D_800D2C84, D_800D2C88;
extern u8 D_800D2DA8, D_800D2DA9, D_800D2DAA, D_800D2DAB;
extern u8 D_800BE9A0;
extern f32 D_800D2CA8[][4][4];
extern f32 D_800D9B20;
void func_150A7A00(f32 matrix[4][4], f32 x, f32 y, f32 z,
                   f32 *outX, f32 *outY, f32 *outZ, f32 *outW);
s32 func_1509563C(f32 x, f32 y, f32 z, f32 *screenX, f32 *screenY,
                   f32 *depth, f32 *divisor, f32 maximum);

typedef struct {
    u8 prefix[0xC];
    f32 scaleX, scaleY;
    f32 flatScaleX, flatScaleY;
    f32 projectedScaleX, projectedScaleY;
    f32 clipTop, clipBottom, clipLeft, clipRight;
    f32 translateX, translateY;
    u8 padding3C[4];
    Vp viewports[20];
} ProjectedViewFrame95760;

s32 func_15095A90(s32, s32, f32, f32, f32, s32, s32, s32, s32);
void func_15095B08(s32, f32, f32, f32, s32, s32 *);
extern s32 D_800D2CA0;
extern u8 D_800873D0[];

typedef struct {
    u32 unk0;
    u8 unk4;
    u8 pad5;
    u16 unk6;
    u16 unk8;
    u8 unkA;
    u8 unkB;
} structC1D70Source;

typedef struct {
    u32 unk0;
    u16 unk4;
    u16 unk6;
    u8 unk8;
    u8 unk9;
    u8 unkA;
    u8 padB;
} structC1D70Descriptor;

typedef struct {
    s16 coordinates[3];
    s16 extentX, extentY;
    u8 alpha;
    u8 animationStep;
    u8 animationFrame;
    u8 flipFlags;
    u8 paddingE[2];
    structC1D70Descriptor *descriptor;
} ProjectedPacket95B08;

s32 func_15095D34(Gfx *, ProjectedPacket95B08 *, s32, s32, s32);

extern structC1D70Descriptor D_800D2C90;

void func_15095060(structC1D70Source *, s32, u8 *);
s32 func_150950D4(s32, structC1D70Descriptor *, s32, s32, s32, s32, s32, s32, s32, s32);

/* Non-matching placeholders for the text-only asm slice asm/C1D70.s. */

s32 func_15095D34();

s32 func_150948C0() {
    return 0;
}

s32 func_1509499C() {
    return 0;
}

s32 func_15094AB8() {
    return 0;
}

s32 func_15094EA0() {
    return 0;
}

u32 *func_15094F40(u32 *arg0) {
    u32 *temp_v1 = arg0;

    arg0 += 2;
    temp_v1[0] = 0xDE000000;
    temp_v1[1] = (u32) D_800873D0;
    D_800D2CA0 = 0;
    return arg0;
}

s32 func_15094F70(s32 arg0, structC1D70Source *arg1, s32 arg2, u8 *arg3,
                  s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    func_15095060(arg1, arg2, arg3);
    return func_150950D4(arg0, &D_800D2C90, arg4, arg5, 0, arg6, arg7,
                         0x100, 0x100, arg8);
}

s32 func_15094FE8(s32 arg0, structC1D70Source *arg1, s32 arg2, u8 *arg3,
                  s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9,
                  s32 arg10) {
    func_15095060(arg1, arg2, arg3);
    return func_150950D4(arg0, &D_800D2C90, arg4, arg5, 0, arg6, arg7,
                         arg8, arg9, arg10);
}

void func_15095060(structC1D70Source *arg0, s32 arg1, u8 *arg2) {
    structC1D70Descriptor *descriptor;
    u32 value;

    descriptor = &D_800D2C90;
    if (arg2 != NULL) {
        *(structC1D70Descriptor **) (arg2 + 0x10) = descriptor;
    }

    value = arg0->unk0;
    if (value < 0x10000000) {
        descriptor->unk0 = value;
    } else {
        descriptor->unk0 = ((u32 *) value)[arg1 >> 8];
    }

    descriptor->unk4 = arg0->unk6;
    descriptor->unk6 = arg0->unk8;
    descriptor->unk8 = arg0->unkA;
    descriptor->unk9 = arg0->unkB;
    descriptor->unkA = arg0->unk4;
}

s32 func_150950D4(s32 arg0, structC1D70Descriptor *arg1, s32 arg2, s32 arg3,
                  s32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8, s32 arg9) {
    return 0;
}

/* Clip transformed coordinates, then map both outputs before either store. */
s32 func_1509563C(f32 x, f32 y, f32 z, f32 *screenX, f32 *screenY,
                   f32 *depth, f32 *divisor, f32 maximum) {
    f32 transformedW;
    f32 inverse;
    f32 valueX;
    f32 valueY;
    ProjectedViewFrame95760 *view;

    func_150A7A00(D_800D2CA8[D_80082FA4], x, y, z, screenX, screenY, depth, divisor);
    transformedW = *divisor;
    if (maximum <= transformedW || transformedW <= D_800D9B20) {
        return 0;
    }
    inverse = 1.0f / transformedW;
    view = (ProjectedViewFrame95760 *)D_800BE628 + D_80082FA4;
    valueX = *screenX;
    valueY = *screenY;
    valueX = (view->scaleX + 5.0f) * valueX * inverse + view->translateX;
    valueY = view->translateY - (view->scaleY + 5.0f) * valueY * inverse;
    *screenX = valueX;
    *screenY = valueY;
    return 1;
}

/* Project a signed coordinate packet, set depth, then draw its screen-space form. */
Gfx *func_15095760(Gfx *output, s16 *packet) {
    f32 screenX;
    f32 screenY;
    f32 depth;
    f32 divisor;

    if (func_1509563C(packet[0], packet[1], packet[2],
                      &screenX, &screenY, &depth, &divisor, 4000.0f) == 0) {
        return output;
    }
    gDPPipeSync(output++);
    gDPSetPrimDepth(output++, (s32)(((depth / divisor) * ((ProjectedViewFrame95760 *)D_800BE628)[D_80082FA4].viewports[D_800BE9C0].vp.vscale[2] + ((ProjectedViewFrame95760 *)D_800BE628)[D_80082FA4].viewports[D_800BE9C0].vp.vtrans[2]) * 32.0f), 0);
    return (Gfx *)func_15095A90((s32)output, (s32)packet, screenX, screenY, divisor, 1, 0, 0, 0);
}

/* Project the packet, update visibility, then emit unsigned primitive depth. */
Gfx *func_150958B0(Gfx *output, s16 *packet, s32 *visible) {
    f32 screenX;
    f32 screenY;
    f32 depth;
    f32 divisor;
    f32 scale;
    Gfx *command;

    if (func_1509563C(packet[0], packet[1], packet[2],
                      &screenX, &screenY, &depth, &divisor, 4000.0f) == 0) {
        *visible = 0;
        return output;
    }
    func_15095B08((s32)packet, screenX, screenY, divisor, 1, visible);
    if (*visible != 0) {
        scale = D_8009DEC0;
        command = output++;
        command->words.w0 = 0xE7000000;
        command->words.w1 = 0;
        command = output++;
        command->words.w0 = 0xEE000000;
        command->words.w1 = (u32)((depth / divisor) * scale + scale) << 16;
    }
    return output;
}

void func_15095A48(s32 arg0, s32 arg1, f32 arg2, f32 arg3) {
    func_15095A90(arg0, arg1, arg2, arg3, 4096.0f, 0, 0, 0, 0);
}

s32 func_15095A90(s32 arg0, s32 arg1, f32 arg2, f32 arg3, f32 arg4, s32 arg5, s32 arg6, s32 arg7, s32 arg8) {
    s32 active;

    func_15095B08(arg1, arg2, arg3, arg4, arg5, &active);
    if (active != 0) {
        arg0 = func_15095D34((Gfx *)arg0, (ProjectedPacket95B08 *)arg1, arg6, arg7, arg8);
    }
    return arg0;
}

/* Scale the packet rectangle, test viewport overlap, and publish draw inputs. */
void func_15095B08(s32 packetAddress, f32 x, f32 y, f32 divisor, s32 projected, s32 *visible) {
    ProjectedPacket95B08 *packet = (ProjectedPacket95B08 *)packetAddress;
    ProjectedViewFrame95760 *view;
    structC1D70Descriptor *descriptor;
    s32 extentX;
    s32 extentY;
    f32 scaleX;
    f32 scaleY;
    f32 inverse;
    f32 width;
    f32 height;

    *visible = 0;
    extentX = packet->extentX;
    if (extentX != 0) {
        extentY = packet->extentY;
        if (extentY != 0) {
            scaleX = D_800380A0;
            scaleY = D_800380A4;
            scaleX = (f32)extentX * scaleX;
            scaleY = (f32)extentY * scaleY;
            if (projected != 0) {
                view = (ProjectedViewFrame95760 *)D_800BE628 + D_80082FA4;
                scaleX *= view->projectedScaleX;
                scaleY *= view->projectedScaleY;
            } else {
                view = (ProjectedViewFrame95760 *)D_800BE628 + D_80082FA4;
                scaleX *= view->flatScaleX;
                scaleY *= view->flatScaleY;
            }
            descriptor = packet->descriptor;
            inverse = 1.0f / divisor;
            width = (f32)(u32)descriptor->unk4 * scaleX * inverse;
            height = (f32)(u32)descriptor->unk6 * scaleY * inverse;
            x -= width * 0.5f;
            y -= height * 0.5f;
            if (view->clipLeft <= x + width && x < view->clipRight &&
                view->clipTop <= y + height && y < view->clipBottom) {
                *visible = 1;
            }
            D_800D2C70 = scaleX;
            D_800D2C74 = scaleY;
            D_800D2C78 = x;
            D_800D2C7C = y;
            D_800D2C80 = divisor;
            D_800D2C84 = width;
            D_800D2C88 = height;
        }
    }
}

s32 func_15095D0C(s32 arg0, s32 arg1) {
    func_15095D34((Gfx *)arg0, (ProjectedPacket95B08 *)arg1, 0, 0, 0);
}

/* Emit a scissored textured rectangle, then advance the packet animation byte. */
s32 func_15095D34(Gfx *output, ProjectedPacket95B08 *packet, s32 sOffset, s32 insetTOffset, s32 widthAdjust) {
    structC1D70Descriptor *descriptor;
    f32 width = D_800D2C70;
    f32 height = D_800D2C74;
    f32 left = D_800D2C78;
    f32 top = D_800D2C7C;
    f32 divisor = D_800D2C80;
    s32 integerScaleX = (s32)width;
    s32 integerScaleY = (s32)height;
    s32 stepS;
    s32 stepT;
    s32 integerX;
    s32 integerY;
    s32 textureS;
    s32 textureT;
    s32 fractionalT;
    s32 animationDelta;
    s32 flipFlags;

    if (insetTOffset != 0) {
        D_800D2C84 -= (width + width) / divisor;
        D_800D2C88 -= (height + height) / divisor;
        left += width / divisor;
        top += height / divisor;
    }
    width = D_800D2C84;
    height = D_800D2C88;
    if (width < 2.0f) {
        width = 2.0f;
    }
    stepS = (s32)((u32)(s32)divisor << 10) / integerScaleX;
    stepT = (s32)((u32)(s32)divisor << 10) / integerScaleY;
    integerX = (s32)left;
    if (D_800D2DAB == 0) {
        gDPSetPrimColor(output++, 1, 0, D_800D2DA8, D_800D2DA9, D_800D2DAA, packet->alpha);
    }
    integerY = (s32)top;
    textureS = (s32)((u32)(s32)(((32.0f - (left - (f32)integerX) * 32.0f) * divisor) /
        (f32)integerScaleX) + (u32)sOffset + 0x2000u);
    flipFlags = packet->flipFlags;
    fractionalT = (s32)(((32.0f - (top - (f32)integerY) * 32.0f) * divisor) / (f32)integerScaleY);
    textureT = (s32)((u32)fractionalT + (u32)insetTOffset + 0x2000u);
    if (flipFlags != 0) {
        if (flipFlags & 1) {
            stepS = (u16)(0u - (u32)stepS);
            textureS = (packet->descriptor->unk4 + 255) << 5;
        }
        if (flipFlags & 2) {
            stepT = (u16)(0u - (u32)stepT);
            textureT = (s32)((u32)((packet->descriptor->unk6 + 255) << 5) - (u32)fractionalT);
        }
    }
    gSPScisTextureRectangle(output++, (s32)((u32)integerX << 2), (s32)((u32)integerY << 2),
        (s32)((u32)((s32)((f32)widthAdjust + width - 1.0f) + integerX) << 2),
        (s32)((u32)((s32)(height - 1.0f) + integerY) << 2), 0, textureS, textureT, stepS, stepT);

    descriptor = packet->descriptor;
    if (descriptor->unkA != 0) {
        animationDelta = packet->animationStep * D_800BE9A0;
        if (descriptor->unkA & 0x80) {
            if (packet->animationFrame & 0x80) {
                packet->animationFrame -= animationDelta;
                if (!(packet->animationFrame & 0x80)) {
                    packet->animationFrame = (packet->animationFrame + animationDelta) & 0x7F;
                }
            } else {
                packet->animationFrame += animationDelta;
                if (packet->animationFrame >= ((descriptor->unkA & 0x7F) << 3)) {
                    packet->animationFrame = (packet->animationFrame - animationDelta) | 0x80;
                }
            }
        } else {
            packet->animationFrame += animationDelta;
            if (packet->animationFrame >= (descriptor->unkA << 3)) {
                packet->animationFrame -= descriptor->unkA << 3;
            }
        }
    }
    return (s32)output;
}

s32 func_1509629C() {
    return 0;
}

u8 *func_15096934(u8 *arg0) {
    extern u32 D_80087408;
    extern u8 D_800D2DAB;
    u8 *ptr = arg0;

    *(u32 *) (ptr + 0) = 0xde000000;
    *(u32 *) (ptr + 4) = (u32) &D_80087408;
    arg0 = arg0 + 8;
    D_800D2DAB = 0;
    return arg0;
}
