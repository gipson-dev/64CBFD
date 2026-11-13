# Camera-state callback: private two-word screen

Date: 2026-11-13. `func_15125924` remains a zero-return placeholder in
`game_14FF90.c`; **this screen is not installed or counted as a match**.
Its 82-word retail body occupies VA `0x15125924..0x15125A6C`, ROM
`0x152DD4..0x152F1C`. It has a 48-byte frame. Two original direct call sites
were found: `func_150054C4` at `0x15005718` and `func_15122C5C` at
`0x15122F50`; each passes its saved camera pointer in the delay slot. The
bounded census found no literal target address in the decompressed input;
it does not rule out computed or external calls. Neither complete caller
has been qualified in this screen.

The routine reads an optional state pointer at camera offset `0x3D4`,
truncates the float at state offset `0x1C`, and reads the byte at `0x4E`.
Camera flags at `0x2C` and `0x84` and an actor byte at `0x102` gate a call
to `func_15125490`. Based on that result and the two captured values, it
either requests state 13 and may set camera flag `0x1000`, or handles a
second flag, optionally clears a float, and updates two float fields from a
difference. The helpers are not fully qualified by this screen. The local
names below describe observations; they do not identify the game's higher
level camera behavior.

The current private C candidate uses the normal owner `-O2 -g3` profile.
It emits 82 words, the original 48-byte frame and 80 same-position words.
All four helper relocation bindings match. The other 44 raw owner functions,
constant pools and normalized diagnostics are unchanged. Two differences
swap the state-byte and truncated-float result registers:

| Offset | Raw C | Retail |
| --- | --- | --- |
| `0x28` | `9045004E` | `9043004E` |
| `0x30` | `44033000` | `44053000` |

The screened owner SHA-256 is
`bc513accdeb3727016823a3f061386769c0da0b4e9ae4f6dab113bf29e2708a7`;
the full private candidate source SHA-256 is
`49ca001f6f68c56561128e24bd74f54715fc41c5c7f9b1f8267ce72401e5750c`.

Two private expected-word guards reproduce the retail body and relocations
through the generic owner padder; 44 other padded owner functions agree.
The guard file was **not** installed. The earlier 56-byte-frame candidate is
not acceptable merely because it is close. The selected candidate's complete
source is preserved below so this finding does not depend on ignored build
files. Its function declaration would also need changing from the current
placeholder's `s32` signature to the candidate pointer/void interface, with
all affected callers and object neighbors rechecked before installation. Both
identified caller windows pass a pointer and immediately proceed without
using the return register; unknown callers remain outside that evidence.

An independent finite guest model compared retail, raw C and the private
guarded body in 2,304 non-overlapping cases per stream. It checked the
branches, public camera memory, helper arguments, and modeled helper mutations;
the original helper bodies and exceptional float conversions were not covered.
In a separate deliberately constructed camera/stack overlap sweep, all three
streams had the same modeled outcome and helper calls in 2,112 cases, but the
raw candidate changed bytes within the camera region differently in 508 cases.
Retail and guarded streams agreed. The 96 program exceptions in that sweep
were 32 identical per-stream modeled exceptions; these are not hardware fault
or full caller proofs. For example, a camera at incoming SP minus `0x800`
overlaps the two private words at camera offsets `0x7F8..0x7FF`, whose saved
values are swapped by the raw compiler allocation. Actual caller storage
provenance remains open; the test does not assert that either caller creates
this overlap.

```c
void func_15125924(struct108 *camera) {
    s32 speed;
    s32 status;
    if (camera->unk3D4 != 0) {
        speed = (s32)*(f32 *)((u8 *)camera->unk3D4 + 0x1C);
        status = ((u8 *)camera->unk3D4)[0x4E];
    } else {
        status = 0;
        speed = 0;
    }
    if (*(u32 *)((u8 *)camera + 0x2C) & 0x40) return;
    if (!(*(u32 *)((u8 *)camera + 0x84) & 0x4000) &&
        !(*(u8 **)((u8 *)camera + 0x3D0))[0x102]) return;
    if (func_15125490(camera) != 0 && speed == 0 && status == 0) {
        if (func_15123934(camera, 0x80, 1, 1, 13) &&
            !*(u32 *)((u8 *)camera + 0x6C8)) {
            func_15124B18(camera);
            *(u32 *)((u8 *)camera + 0x5F0) |= 0x1000;
        }
        return;
    }
    if (*(u32 *)((u8 *)camera + 0x2C) & 0x80) {
        func_151239CC(camera, 13);
        *(f32 *)((u8 *)camera + 0x190) = 0.0f;
    }
    if (*(u32 *)((u8 *)camera + 0x5F0) & 0x1000) {
        f32 offset = *(f32 *)((u8 *)camera + 0x2FC) -
                     *(f32 *)((u8 *)camera + 0x354);
        *(u32 *)((u8 *)camera + 0x5F0) &= ~0x1000;
        *(f32 *)((u8 *)camera + 0x344) = offset;
        *(f32 *)((u8 *)camera + 0x348) = offset;
    }
}
```

Next, recover those two instructions directly from C or establish the real
caller and helper storage contracts before using guards. Then provide durable
guest/native/fault and relocation tests, verify the exact production Make
path and full linked image, and recount only after installation. An
independent `func_150F1A00` pulse screen still has substantial loop and
register-scheduling differences; the tested rate-table layout variations did
not improve its best existing 82-word candidate.

Candidate selection caution: `func_150183D0` contains handwritten shared
entry points at `0x15018470` and `0x150184B8`, and its `func_15018500`
helper uses the caller frame and a nonstandard return-register convention.
It is not an ordinary 76-word C leaf despite appearing near the top of the
remaining-differences list.

No production source, patch manifest, linked object, ELF, or progress row
changed. The last actual recount remains Game **3,754 / 4,843 (77.51%)**,
with **121** more Game matches required for 80%.
