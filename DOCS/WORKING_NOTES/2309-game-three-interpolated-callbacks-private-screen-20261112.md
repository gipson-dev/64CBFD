# Three interpolated Game callbacks: private screen

**Correction:** [Note 2310](2310-game-interpolated-callback-dispatch-and-return-20261112.md) identifies the real caller and its consumed return value. The `void` candidate and tests below did not qualify that contract; use them only as historical screens.

Date: 2026-11-12. This is an **uninstalled, uncredited** investigation of
`func_1500B8F4`, `func_1500BAB8`, and `func_1500BC7C` in `game_36680.c`.
The production functions and `func_1500AF08` remain zero-return placeholders.
The last adopted checkpoint is [Note 2308](2308-game-position-interpolation-guarded-match-20261112.md): Game 3,704 / 4,840 (76.53%), 168 matches short of 80%.

The retail slots are each 113 words: VA `1500B8F4..1500BAB8` (ROM
`38DA4..38F68`), `1500BAB8..1500BC7C` (ROM `38F68..3912C`), and
`1500BC7C..1500BE40` (ROM `3912C..392F0`). Their retail bodies differ
only in the mode constant at offset `0x190`: `0x57`, `0x08`, and `0x21`.
The table at `D_8008CEB8` holds their addresses at `8008CED0`, `8008CEDC`,
and `8008CEF4`. This proves registration, not the dynamic caller or its
complete ABI. `func_1517BBAC` uses the adjacent second table member; that
observation does not establish the callers of these three callbacks.

The candidate reads three signed halfword coordinate rows and two floats per
iteration, interpolates each coordinate, and feeds the result of
`func_1500AF08` into the next call before setting the per-slot mode byte.
The presumed ABI is `(s16 count, u8 flag, s32 slot, s32 context, s32 cursor,
s16 **points)`; the first four arguments use registers and the remaining two
use the stack. Names describe observed roles, not proven gameplay meaning. The
helper itself remains a stub, so this is not evidence of working gameplay.

The current best private C shape, shown for the first mode, is below. The
other two differ only in function name and final mode. This is a screen, not
an approved source change. Its pointer declaration order affects compiler
scheduling and is not evidence of recovered original declarations.

```c
#include <ultra64.h>
extern f32 D_80095C64[][2]; extern u8 D_800DDBD0[];
s32 func_1500AF08(s32, s32, s32, s16, s16, s16, s32, u8, s32);
void func_1500B8F4(s16 count, u8 flag, s32 slot, s32 context, s32 cursor, s16 **points) {
s32 i=0; if(count != 0) { f32 *w=&D_80095C64[0][0]; do {
s16 *p2=points[2],*p1=points[1],*p0=points[0]; f32 a=w[0],b=w[1];
cursor=func_1500AF08(cursor,slot,context,(s16)((p0[0]+(p1[0]-p0[0])*a)+(p2[0]-(p0[0]+(p1[0]-p0[0])*a))*b),(s16)((p0[1]+(p1[1]-p0[1])*a)+(p2[1]-(p0[1]+(p1[1]-p0[1])*a))*b),(s16)((p0[2]+(p1[2]-p0[2])*a)+(p2[2]-(p0[2]+(p1[2]-p0[2])*a))*b),0,flag,cursor);
i++; w+=2; } while(i != count); } D_800DDBD0[slot]=0x57; }
```

An owner-level O2/g0 function-only compile emits 113 words per candidate,
64 matching retail at the same offsets; 49 differ, including four changed
relocation positions. The normal-profile primary owner preserves 79 neighboring
functions. The target profile changes other functions, so it cannot replace
the whole owner. The private owner prototype gates the typed helper declaration
under the alternate profile to avoid changing the existing helper stub.

For each function the raw best candidate passed 256 finite guest cases
(counts 0..3), 576 additional access-trace cases across six bounded pointer and
global overlap layouts, and 408 external access-cut prefixes across 18 cases.
A further 96 negative-count guest cases stopped after three helper calls;
they do not establish termination or defined native C behavior. The selected
C passed 96 finite native cases per function at O0/O2/O3; incorrect weight and
mode controls failed. These modeled tests do not establish full parent
execution, C behavior for out-of-range conversions, NaNs, hardware faults,
stack-private cuts, or full gameplay. Some guest alias layouts are outside
ordinary defined C bounds.

An earlier shape had 58 directly matching words and 55 differing words per
function. Experimental expected-word mappings normalized its private object to
retail; 24 independently rebased GNU links agreed with independently assembled
retail functions. A private shadow Make execution and independent image
prediction agreed: 1,081 changed ELF bytes, zero exclusions or address drift,
and all 189,088 protected data bytes unchanged. This is evidence about that
older private shape only; its guards were not qualified, and it was not
installed. A deliberate guest-only mode-store alias of a saved s7 stack slot
exposed a raw scheduling difference: retail and the normalized code reload the
modified saved value, whereas the raw candidate reloads before the mode store.
This alias is outside normal C array bounds, but demonstrates why positional
replacement alone does not prove source equivalence or safe scheduling. The
newer 49-word map has not received the corresponding full padding/link audit.

Private receipts and scripts currently reside in the ignored build directory
`conker/build/game-three-interpolated-callbacks-screen/`, notably
`mixed-g0-order10-results.json`, `order10-word-map.json`,
`owner_mixed_order10.py`, `guest_order10.py`, `alias_order10.py`,
`fault_order10.py`, `negative_order10.py`, `native_order10_screen.py`,
`experimental-make.json`, and `rebase_screen.py`. Build scratch may be cleaned;
the candidate and findings above are retained here independently.

Next: identify and qualify the actual first-member indirect caller and complete
argument contract; seek a closer source shape; audit each changed register,
live range, delay slot, stack access, and relocation, including negative and
exceptional boundaries; build durable tests with effective controls; qualify
both padding environments, production Make and independent full-image delta.
Only then adopt, recount, update status, and commit tools before the consumer
if tools change. Do not credit a match from a private normalized object.
