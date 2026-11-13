# Point descriptor submission: private frame and ABI screen

Date: 2026-11-13. `func_151382E0` in `game_161520.c` remains a zero-return
placeholder; **neither private candidate is installed or counted**. Retail
occupies VA `0x151382E0..0x15138424`, ROM `0x165790..0x1658D4`, 81 words,
with a `0x70`-byte frame. An existing recovered caller, `func_15138BC0`,
passes a position, type, surface, byte group and context, ignoring the return;
see [Note 1779](1779-actor-point-effects-match-20261028.md). This observation
does not establish all possible callers or an unrestricted signed type range.

The routine reads the selected table byte at `D_800A3FE6 + type*16` and
returns early for category 2. Otherwise it fills a partially initialized
0x4c-byte descriptor and submits it to `func_15153F18`. The descriptor
contains the copied position, fixed fields, float globals and a category-1
flag. Three bytes following that flag remain uninitialized in retail; they
must not be assumed zero. Pointer/stack aliasing and helper observations need
qualification before installation.

Under the existing owner compiler profile, the candidate below uses the
helper's existing `s32` fourth parameter and emits 81 words, 77 identical at
the same offsets, with the other 63 raw owner functions, normalized constant
pools and diagnostics unchanged. The remaining differences are:

| Offset | Candidate | Retail | Meaning |
| --- | --- | --- | --- |
| `0x000` | `27BDFF88` | `27BDFF90` | Allocate `0x78` versus `0x70` |
| `0x004` | `AFA70084` | `AFA7007C` | Incoming fourth-argument save |
| `0x124` | `8FAC0088` | `8FAC0080` | Incoming fifth-argument load |
| `0x138` | `27BD0078` | `27BD0070` | Restore stack |

The local descriptor is at `sp+0x24` in both instruction streams, so changing
only those four words changes its position relative to incoming stack and may
change overlap behavior. Four expected-word patches are not a source proof.
An additional 32-way search over local `register`, `const`, integer type and
descriptor scope variations retained the `0x78` frame; none improved on 77
same-position words.

A different private candidate eliminates the `channel` local, inlines the
category table access and declares the helper's fourth parameter as `u8`.
It emits all 81 retail words with the retail frame after relocation binding.
However the actual helper definition in `generated_17CAF0.c` takes `s32`
for that parameter, so this candidate has an incompatible cross-translation-
unit declaration and is not source-qualified. A private experiment changing
the definition to `u8` changed its compiled body from 168 to 170 words,
changed existing relocations and guards, and also changed the compiled caller
`func_151DBAA8` when its declaration was corrected. This is not an isolated
or established ABI cleanup. Existing declarations elsewhere also disagree.

The owner SHA-256 was
`d905084e5b5710e33f77bc1015b0ca9a15d49360a9158d8c4a85c78cad510a31`;
the full 77-word-position candidate source SHA-256 was
`16a0299cea35deacd5d2ffff8f666f753dd11e3497746c997f1eaedd5113a653`;
the incompatible 81-word candidate source SHA-256 was
`3a528c720a9b8f37434ae08beaf42f20bfbcc9489d7ffd53a22febe999cab087`.
Private files live under ignored `conker/build/game-point-descriptor-151382e0-screen/`.
The first hash for the incompatible candidate is case-insensitive hex.

The following source is the compatible-prototype screen, preserved here
independent of disposable build artifacts. It also requires `Position161520`
from the existing owner. It is an investigation candidate, not production C:

```c
typedef struct {
    s16 value0, value2, value4, value6;
    Position161520 point;
    f32 value14, value18, value1C, value20, value24, value28;
    s16 value2C, value2E, value30, value32, value34, value36, value38, value3A;
    u8 slot, pad3D[3];
    f32 value40;
    s16 value44, value46;
    s32 word48;
} PointEffectDescriptor161520;
extern u8 D_800A3FE6[];
extern f32 D_800A4830, D_800A4834, D_800A4838, D_800A483C, D_800A4840;
void func_15153F18(PointEffectDescriptor161520 *, Position161520 *, s32, s32, s32);

/* Submit the point descriptor unless the selected effect type is disabled. */
void func_151382E0(Position161520 *position, s32 type, void *surface, u8 group, s32 context) {
    u32 channel = group;
    u8 category = D_800A3FE6[type * 16];
    PointEffectDescriptor161520 descriptor;
    if (category != 2) {
        descriptor.point = *position;
        descriptor.value14 = D_800A4830;
        descriptor.value18 = D_800A4834;
        descriptor.value1C = D_800A4838;
        descriptor.value20 = D_800A483C;
        descriptor.value24 = 4.0f;
        descriptor.value28 = 9.0f;
        descriptor.value2C = 18;
        descriptor.value2E = 7;
        descriptor.value0 = 0;
        descriptor.value2 = 255;
        descriptor.value4 = -63;
        descriptor.value6 = 78;
        descriptor.value30 = 3;
        descriptor.value32 = 3;
        descriptor.value34 = 20;
        descriptor.value36 = 30;
        descriptor.value38 = 155;
        descriptor.value3A = 100;
        descriptor.value44 = 16;
        descriptor.value46 = 15;
        descriptor.word48 = 0;
        descriptor.value40 = D_800A4840;
        descriptor.slot = category == 1 ? 1 : 0;
        func_15153F18(&descriptor, &descriptor.point, (s32)surface, channel, context);
    }
}
```

Next, find a legal source shape that emits the retail frame with the real
helper signature, or separately recover and validate the helper ABI across
its definition and every caller. Qualify caller ranges, stack aliases,
untouched bytes and fault order; then run raw/padded owner and pool checks,
guest and native tests, actual Make, strict linked-image comparison and
recount before claiming a match.
