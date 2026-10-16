#include <ultra64.h>

/* Legacy callers pass the same six word-sized arguments and cursor result. */
#define func_1501A490 ViewScissorLegacyWordSignature
#include "functions.h"
#undef func_1501A490
#define D_800968E0 ViewInitLegacyFactorWord
#include "variables.h"
#undef D_800968E0

/* Keep the retail float factor distinct from the legacy integer declaration. */
extern const f32 D_800968E0;
s32 allocate_memory(s32 size, s32 tag, s32 pool, s32 flags);
void func_150006E0(s32 category);
void func_1510B070(s32 mode);

typedef struct {
    u8 padding0[0xC];
    f32 extentX, extentY;
    u8 padding14[0x10];
    f32 top, bottom, left, right;
    u8 padding34[0x38];
    f32 baseFovX, baseFovY;
    u8 padding74[0x10C];
} ViewProjection476D0;
extern f32 D_800968F4, D_800968F8, D_800968FC;
void func_1510B128(s32 index, f32 offsetX, f32 offsetY, f32 scale, f32 fallback);
#define VIEW_PROJECTIONS_476D0 ((ViewProjection476D0 *)D_800BE628)

void func_1501B0A0(s32 index, s32 reference);
void func_1501B22C(s32 index);

extern s32 D_800BE9C8[];
extern Gfx D_8002C930[];

void func_1501AF44(f32 *ulx, f32 *uly, f32 *lrx, f32 *lry);

/* Generated placeholder declarations. */
void func_1501A220(s32 viewCount, s32 projectionMode);
void func_1501A39C(void);
s32 func_1501A764();
s32 func_1501A8C0(s32 arg0, s32 arg1, s32 arg2, s32 arg3);
s32 func_1501AE94(s32 arg0);
/* End generated placeholder declarations. */

/* Allocate view state, round the single-view height and initialize projections. */
void func_1501A220(s32 viewCount, s32 projectionMode) {
    u32 slots;
    s32 index;
    f32 height;
    f32 scaledHeight;
    s32 rounded;

    D_80082FA0 = viewCount;
    if (viewCount == 0) {
        slots = 1;
    } else {
        slots = (u32)viewCount + 2;
    }
    D_800BE628 = allocate_memory((s32)(slots * sizeof(ViewProjection476D0)), 1, 1, 0);
    D_800BE62C = allocate_memory((s32)(slots * 16), 1, 1, 0);
    if (D_80082FA0 == 1) {
        height = (f32)D_800BE63C[0] - 2.0f;
        scaledHeight = height * D_800968E0;
        rounded = (s32)scaledHeight;
        D_800BE6B8 = (f32)(rounded - rounded % 4) / height;
    }
    func_150006E0(D_800BE9F0);
    for (index = 0; index <= (viewCount = D_80082FA0); index = (s32)((u32)index + 1)) {
        func_1501A8C0(index, viewCount, 1023, 0);
    }
    if (viewCount != 0) {
        func_1501A8C0(index, 0, 1023, 0);
    }
    D_800BE617 = 1;
    D_800BE614 = 1;
    D_800BE635 = 0;
    func_1510B070(projectionMode);
}
/* Initialize both display-list rows and publish their command cursors. */
void func_1501A39C(void) {
    s32 *input;
    s32 *output;
    u32 viewportOffset;
    Gfx *commands;

    input = D_800BE9C8;
    output = D_800BE9D8;
    viewportOffset = 0;
    do {
        commands = (Gfx *)*input;
        gSPSegment(commands++, 0, 0);
        gSPSegment(commands++, 0, 0);
        gSPDisplayList(commands++, D_8002C930);
        gDPSetDepthImage(commands++, D_800BE9C4);
        gSPViewport(commands++, (u32)D_800BE628 + viewportOffset + 0x40);
        input++;
        *output++ = (s32)commands;
        viewportOffset += 0x10;
    } while (output != &D_800BE9E0);
}

/* Append pipe sync and the selected view's clipped scissor rectangle. */
s32 func_1501A490(Gfx *commands, s16 view, s32 unused2, s32 unused3, s32 bottomLimit, s32 mode) {

    gDPPipeSync(commands++);
    if (view == 0xFF) {
        gDPSetScissor(commands++, mode, 2, 0, (f32)(s32)((u32)D_800BE620 - 2), (f32)D_800BE624);
    } else {
        f32 left;
        f32 right;
        f32 top;
        f32 bottom;

        left = VIEW_PROJECTIONS_476D0[view].left;
        right = VIEW_PROJECTIONS_476D0[view].right;
        top = VIEW_PROJECTIONS_476D0[view].top;
        if (bottomLimit != 0) {
            bottom = (f32)bottomLimit < VIEW_PROJECTIONS_476D0[view].bottom ? (f32)bottomLimit : VIEW_PROJECTIONS_476D0[view].bottom;
        } else {
            bottom = VIEW_PROJECTIONS_476D0[view].bottom;
        }
        func_1501AF44(&left, &top, &right, &bottom);
        gDPSetScissor(commands++, mode, left, top, right, bottom);
    }
    return (s32)commands;
}

Gfx *func_1501A680(Gfx *arg0) {
    gDPSetColorImage(arg0++, G_IM_FMT_RGBA, G_IM_SIZ_16b, D_800BE620, D_8002AAE8[D_800BE9C0]);
    return arg0;
}

Gfx *func_1501A6CC(Gfx *arg0, s32 a, s32 b, s32 c, s32 d) {
    if (a < 3) {
        a = 2;
    }
    if (b <= 0) {
        b = 0;
    }
    if (c >= (D_800BE620 - 2)) {
        c = D_800BE620 - 2;
    }
    if (d >= D_800BE624) {
        d = D_800BE624;
    }

    gDPFillRectangle(arg0++, a, b, c, d);
    return arg0;
}

void func_150A7A00(f32 arg0, f32 arg1, s32 arg2, f32 arg3, f32 arg4, f32 arg5, f32* arg6, f32* arg7, f32* arg8, f32* arg9);
/* Non-matching C placeholders for asm/nonmatchings/game_476D0/func_1501A764.s. */
s32 func_1501A764() {
    return 0;
}
// void func_1501A764(s16 arg0, f32 arg1, f32 arg2, f32 arg3, f32 *arg4, f32 *arg5, f32 *arg6) {
//     f32 sp34;
//     f32 sp30;
//     f32 sp2C;
//     f32 sp28;
//     struct140 *temp_v0_2;
//
//     func_150A7A00(arg1, arg2, &D_800D9D10 + (arg0 << 6), arg1, arg2, arg3, &sp34, &sp30, &sp2C, &sp28);
//     sp28 = 1.0f / sp28;
//     // temp_v1 = arg0 * 0x180;
//     temp_v0_2 = &D_800BE628[arg0];
//     // sp28 = temp_f8;
//     *arg4 = (((temp_v0_2->unkC + 5.0f) * sp34 * sp28) + temp_v0_2->unk34);
//     temp_v0_2 = &D_800BE628 [arg0];
//     *arg5 = (temp_v0_2->unk38 - ((temp_v0_2->unk10 + 5.0f) * sp30 * sp28));
//     temp_v0_2 = &D_800BE628[arg0].unk50[D_800BE9C0];  // (D_800BE9C0 * 0x10);
//     *arg6 = (((f32) temp_v0_2->unk4C + (sp2C * sp28 * (f32) temp_v0_2->unk44)) * 32.0f);
// }

/* Non-matching C placeholders for asm/nonmatchings/game_476D0/func_1501A8C0.s. */
s32 func_1501A8C0(s32 arg0, s32 arg1, s32 arg2, s32 arg3) {
    return 0;
}

s32 func_1501AE94(s32 arg0) {
    f32 maxX = D_800BE620 - 2.0f;
    f32 maxY = D_800BE624;
    f32 *record = (f32 *)((u8 *)D_800BE628 + (u32)arg0 * 0x180);

    if ((record[11] < 2.0f) || (maxX < record[12])) {
        return 0;
    }
    if ((record[9] < 0.0f) || (maxY < record[10])) {
        return 0;
    }
    return 1;
}

/* Clamp rectangle edges to the current framebuffer bounds. */
void func_1501AF44(f32 *ulx, f32 *uly, f32 *lrx, f32 *lry) {
    f32 ulxValue;
    f32 lrxValue;
    f32 ulyValue;
    f32 lryValue;
    f32 ulxMax;
    f32 lrxMax;
    f32 ulyMax;
    f32 lryMax;
    f32 ulxClamped;
    f32 lrxClamped;
    f32 ulyClamped;
    f32 lryClamped;

    ulxValue = *ulx;
    if (ulxValue < 2.0f) {
        *ulx = 2.0f;
    } else {
        ulxMax = (f32) D_800BE620 - 2.0f;
        if (ulxMax < ulxValue) {
            ulxClamped = ulxMax;
        } else {
            ulxClamped = ulxValue;
        }
        *ulx = ulxClamped;
    }
    lrxValue = *lrx;
    if (lrxValue < 2.0f) {
        *lrx = 2.0f;
    } else {
        lrxMax = (f32) D_800BE620 - 2.0f;
        if (lrxMax < lrxValue) {
            lrxClamped = lrxMax;
        } else {
            lrxClamped = lrxValue;
        }
        *lrx = lrxClamped;
    }
    ulyValue = *uly;
    if (ulyValue < 0.0f) {
        *uly = 0.0f;
    } else {
        ulyMax = (f32) D_800BE624;
        if (ulyMax < ulyValue) {
            ulyClamped = ulyMax;
        } else {
            ulyClamped = ulyValue;
        }
        *uly = ulyClamped;
    }
    lryValue = *lry;
    if (lryValue < 0.0f) {
        *lry = 0.0f;
        return;
    }
    lryMax = (f32) D_800BE624;
    if (lryMax < lryValue) {
        lryClamped = lryMax;
    } else {
        lryClamped = lryValue;
    }
    *lry = lryClamped;
}

/* Transfer the reference viewport's projection into this view's FOV offsets. */
void func_1501B0A0(s32 index, s32 reference) {
    f32 halfX, halfY, tangentX, tangentY, extentX, extentY, offsetX, offsetY;

    halfX = VIEW_PROJECTIONS_476D0[index].baseFovX * D_800968F4;
    halfY = VIEW_PROJECTIONS_476D0[index].baseFovY * D_800968F4;
    tangentX = sinf(halfX) / cosf(halfX);
    tangentY = sinf(halfY) / cosf(halfY);
    extentX = ((s32 *)&D_800BE638)[reference] / (tangentX + tangentX);
    extentY = ((s32 *)&D_800BE650)[reference] / (tangentY + tangentY);
    offsetX = func_150484A0(VIEW_PROJECTIONS_476D0[index].extentX, extentX) *
              D_800968F8 - VIEW_PROJECTIONS_476D0[reference].baseFovX;
    offsetY = func_150484A0(VIEW_PROJECTIONS_476D0[index].extentY, extentY) *
              D_800968FC - VIEW_PROJECTIONS_476D0[reference].baseFovY;
    func_1510B128(index, offsetX, offsetY, 1.0f, 0.0f);
}

/* Build the selected view's four half-FOV side-plane normals. */
void func_1501B22C(s32 index) {
    struct259 *view = (struct259 *)(index * 0x180 + (char *)D_800BE628);
    f32 value, verticalCosine, horizontalCosine, negativeVerticalCosine;
    f32 halfVertical, verticalAngle, horizontalValue;

    value = view->unk74 * 0.5f;
    horizontalValue = -value;
    halfVertical = view->unk78 * 0.5f;
    horizontalValue *= D_80096900;
    horizontalCosine = cosf(horizontalValue);
    horizontalValue = sinf(horizontalValue);
    view->unk9C = horizontalValue;
    view->unk90 = horizontalValue;
    horizontalCosine = -horizontalCosine;
    view->unk88 = -horizontalCosine;
    view->unk94 = horizontalCosine;
    view->unk98 = 0.0f;
    view->unk8C = 0.0f;
    verticalAngle = halfVertical * D_80096904;
    verticalCosine = cosf(verticalAngle);
    value = sinf(verticalAngle);
    negativeVerticalCosine = -verticalCosine;
    value = -value;
    view->unkA0 = 0.0f;
    view->unkB0 = -negativeVerticalCosine;
    view->unkA8 = value;
    view->unkB4 = value;
    view->unkAC = 0.0f;
    view->unkA4 = negativeVerticalCosine;
}
