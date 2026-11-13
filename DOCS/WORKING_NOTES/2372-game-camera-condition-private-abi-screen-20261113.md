# Game camera condition callback: private helper-ABI screen

Date: 2026-11-13. `func_150BE850` in `generated_EBD00.c` remains a
zero-return placeholder. This candidate and its guards are **not installed
or counted**. The retail body occupies VA `0x150BE850..0x150BE9AC`, ROM
`0xEBD00..0xEBE5C`, 87 words, followed by one alignment word. Entry 18 in
`D_80089670` points at it; the original `func_15130230` dispatcher passes
its first argument and ignores the callback return. Other computed or
external callers are not ruled out.

The routine makes three script-query calls, combines their results and
either requests a camera state and updates camera fields, or attempts to
leave that state. It conditionally initializes the camera before its state
request, performs further updates only when that request succeeds, and
loads the two global float constants before storing the camera fields.
The names below describe observations and are not established game names.

Under the normal generated-slice `-O2 -g3` profile, the selected C draft
emits 87 words with the retail `0x30` frame and stack slot, 81 at identical
positions. Compiler diagnostics and normalized constant pools match the
original empty owner; there are no other owner functions. Six private
expected-word guards adjust a closed floating-register allocation cycle;
both the generated and generic padders then reproduce the complete assembled
retail body and relocation bindings. The first word retains its low relocation
to `D_800A00B4`:

```csv
generated_EBD00,func_150BE850,0xf0,0xC4220000,0xC4260000,R_MIPS_LO16:D_800A00B4,R_MIPS_LO16:D_800A00B4,Normalize closed floating-register allocation cycle,,,false
generated_EBD00,func_150BE850,0xf4,0x44803000,0x44804000,,,Normalize closed floating-register allocation cycle,,,false
generated_EBD00,func_150BE850,0x104,0xE6020374,0xE6060374,,,Normalize closed floating-register allocation cycle,,,false
generated_EBD00,func_150BE850,0x10c,0xE6060190,0xE6080190,,,Normalize closed floating-register allocation cycle,,,false
generated_EBD00,func_150BE850,0x130,0x44804000,0x44805000,,,Normalize closed floating-register allocation cycle,,,false
generated_EBD00,func_150BE850,0x144,0xE6080674,0xE60A0674,,,Normalize closed floating-register allocation cycle,,,false
```

An independent guest model passed 128 non-overlapping cases per stream across
retail, raw C and both private padded bodies. It covered query-result and
camera-state paths and mocked helper mutations, while comparing public memory
and helper call arguments. This bounded check does not qualify helper bodies,
overlap/fault behavior, a native build, hardware, gameplay, or the production
image.

**Promotion remains open on the script-helper C interface.** Retail
`func_1509BE40` consumes a first argument and a variable argument list; this
callback passes three words. Its current placeholder in `game_C8950.c` is a
zero-argument old-style C definition, while this private caller uses an
unprototyped declaration. Calling that placeholder with three arguments is
not an established portable C interface. The adjacent `func_1509BFB0` is
still assembly, and its complete behavior is not newly qualified here.
Privately changing both the placeholder declaration and definition to a
variadic signature changed its compiled body from 12 to 32 bytes; a three-
fixed-argument alternative changed it to 24 bytes. The other 16 raw owner
functions, normalized constant pools and compiler diagnostics were unchanged
in each screen. Neither change is installed, and the actual caller set,
stack-home effects, padder and linked image for that helper remain untested.
Do not treat a declaration-only change or the six guards as ABI proof.

The original owner SHA-256 is `87925081c5f25def600e126b6df05d5ece1bf6b76608a9188616094aa898263c`; the full private candidate owner
`abi.c` SHA-256 is `0c02c1c6000ee0109996b5a8a61ce061ebccd304d743fca5eba0ce2c12a8b884`; the helper owner SHA-256 is `85b7d65d351e1c598b633fe633413ed5e310a2b2df8cafd19be2ded9e51fb401`.
The ignored `conker/build/game-camera-condition-150be850-screen/` directory
holds compiler, private-guard and guest receipts. The complete candidate
source is reproduced below independent of those disposable files:

```c
#include "structs.h"
extern f32 D_800A00B0, D_800A00B4;
extern u8 D_800CC335;
s32 func_1509BE40();
void func_1509BFB0();
void func_1512868C(struct108 *);
s32 func_15123934(struct108 *, s32, s32, s32, s32);
void func_151254F4(struct108 *, s32);
void func_15123070(struct108 *);
s32 func_151239CC(struct108 *, s32);

/* Update camera state from the current script conditions. */
void func_150BE850(struct108 *camera) {
    s32 value;
    s32 condition;
    f32 width;
    f32 height;
    condition = func_1509BE40(0, 0x2006, 0xB7);
    condition = func_1509BE40(0, condition | 0x2000, 0xBC);
    value = func_1509BE40(0, 0x2000, 0xBB);
    if (condition != 0 && value != -1) {
        func_1509BFB0(0, 0x400E, 1);
        if (*(s32 *)((u8 *)camera + 0x2C) != 8) {
            func_1512868C(camera);
        }
        if (func_15123934(camera, 8, 0, *(s32 *)((u8 *)camera + 0x134), 3)) {
            func_151254F4(camera, D_800CC335 - 1);
            *(u32 *)((u8 *)camera + 0x84) |= 0x1000200;
            *(s16 *)((u8 *)camera + 0x73C) = 0;
            *(u32 *)((u8 *)camera + 0x84) &= ~4;
            *(f32 *)((u8 *)camera + 0x674) = 0.0f;
        }
        width = D_800A00B0;
        height = D_800A00B4;
        *(f32 *)((u8 *)camera + 0x348) = width;
        *(f32 *)((u8 *)camera + 0x34C) = width;
        *(f32 *)((u8 *)camera + 0x374) = height;
        *(f32 *)((u8 *)camera + 0x190) = 0.0f;
        func_15123070(camera);
    } else if (func_151239CC(camera, 3)) {
        func_151254F4(camera, 0);
        *(f32 *)((u8 *)camera + 0x674) = 0.0f;
        func_1509BFB0(0, 0x400E, 0);
    }
}
```

Next, establish and qualify the real script-query C ABI across its definition
and callers, including the placeholder's changed stack-home effects, or find
a source-compatible route. Then test the bounded original dispatcher window,
aliases, access prefixes and defined-domain native behavior with negative
controls; revalidate both padders, actual Make and the full linked image
before changing production or the progress count.
