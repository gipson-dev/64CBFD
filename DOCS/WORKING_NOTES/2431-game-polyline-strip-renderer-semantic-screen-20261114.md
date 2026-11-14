# Game polyline strip renderer semantic screen

Date: 2026-11-14. Target: `func_151A7D6C`, the remaining zero-return
placeholder in `conker/src/game/generated_1D4E00.c`.

This is a **private, uninstalled and uncredited candidate**. Tools commit
`5503794` preserves its complete semantic C body and reproducible tests.
Production source, guard manifest, conversion rows and linked ELF remain
unchanged from the qualified radial ground-emitter checkpoint in
[Note 2430](2430-game-radial-ground-emitter-direct-match-20261114.md).

## Measured source and interface

The retail body occupies `0x151A7D6C..0x151A8340`, ROM
`0x1D521C..0x1D57F0`: **373 words / 1,492 bytes**, with a **0xC8-byte frame**.
There is no alignment tail before `func_151A8340`.

The candidate uses the normal O2/g3 compiler profile, emits 373 words with
the original 0xC8 frame, and produces no diagnostics. Relocation-aware
comparison finds **216 exact words and 157 different words**. Its named
relocation locations and bindings equal the original assembled routine.
All 22 other owner functions and normalized pools remain unchanged.

```c
Gfx *func_151A7D6C(Gfx *output, DirectionStripState151A7D6C *state, s16 view);
```

The local renderer view gives the fields their measured widths and offsets:
signed 16-bit count at 0x12, byte flags at 0x1C, four unsigned color bytes
at 0x24, float width at 0x28, pointer to 24-byte direction vertices at
0x64, 16-byte cache at 0x6C, and signed 32-bit allocation-size slot at 0x7C.
Native layout assertions check the 0x80-byte view and key member offsets.
The existing updater's local type and production declarations are untouched.

Flag bit two gates rendering. The routine asks `func_151D5D60` for the
cached vertex buffer using the narrowed signed view, and returns the
original display-list cursor if the gate is clear or allocation fails.
On success it obtains the camera position, initializes the synchronization
byte, snapshots `count - 1`, and submits the texture, combine, color,
mode and geometry-state helper calls in their original order.

The geometry begins with the first transformed point minus the snapshotted
last transformed point. `func_15145548` receives the endpoint, that delta,
camera pointer, output closest point and parameter pointer. The cross product
of the delta and camera-to-closest-point ray supplies the strip offset.
A zero squared magnitude selects three zeros; otherwise width divided by
the square root scales all three components.

Each segment emits left-plus-offset, left-minus-offset,
right-minus-offset and right-plus-offset vertices. Coordinates truncate to
signed integers and then enter the signed 16-bit vertex fields. Texture
coordinates span 0..960, colors are all 255 and flags are zero. The three
commands load four vertices and emit triangles `(0,1,2)` and `(0,2,3)`.
The signed 16-bit loop indices advance while re-reading the owner count.

## Caller and behavior evidence

The prepared ROM contains no aligned direct JAL to this function. Its one
aligned literal pointer is at ROM `0x230894`; the corresponding loaded
data entry is `0x8008BDD4`. This is descriptor base `0x8008B4A8` plus
`45 * 52 + 8`, the rendering slot for record type **0x2D**. This agrees
with the existing `func_151A7950` allocation type.

Two authentic indirect-dispatch windows in `func_151674F8` execute through
the table entry and then the complete retail or candidate callee:
`0x151677D8..0x15167800` and `0x15167894..0x151678B8`. Sixteen cases check
the output/owner/view interface, signed view narrowing, the caller's
linked-list update in the delay slot, and the returned output cursor.
These windows do not qualify the complete rendering dispatcher lifecycle.

The independent ordinary-RAM geometry model passes **375 cases** against
both original and raw C streams, reaching every one of the 373 instructions.
Cases cover gates, allocation success/failure, counts -1/0/1/2/5, curved,
collinear and coincident points, signed view values, signed/zero widths,
and helper-visible changes to counts, flags, colors, width, point-array
pointer, camera position and rendering globals. The cached last index
and live later fields are checked separately. Providers clobber caller-save
registers, floating registers, HI/LO and outgoing argument homes.

Eight additional guest cases cover an overlapping vertex/display-list
buffer and a vertex buffer in the caller's stack storage. These are narrow
alias checks; private callee-home redirects and unrestricted aliases remain
open.

Native 32-bit C passes **195 cases in each of six profiles**: O0/O2/O3,
each with strict and disabled strict aliasing. The harness uses SSE float
arithmetic, disabled contraction, standard excess precision, trapping
UBSan and float-cast overflow checks. It verifies helper arguments and
order, projection inputs, all 32 vertex slots, all 64 display-list slots,
owner fields/padding, camera and rendering globals. Pointer-valued command
words are normalized to guest addresses for comparison.

All eight deliberate source mistakes are detected in each native profile:
wrong active gate, wrong endpoint index, reversed cross-product Y,
wrong width scale, wrong texture span, reversed second triangle winding,
cached loop count and signed color interpretation. Curved fixtures make
the endpoint control discriminating; the signed-color control uses a
channel whose high bit is set. Fixture address mappings keep camera,
output, vertex and guest-stack storage distinct unless explicitly aliased.

The projection, allocation and rendering helpers are modeled providers.
The projection provider uses a fixed quarter-segment result. This is not
coupled execution of those helper bodies, unrestricted floating-point/FCSR
qualification, hardware rendering or gameplay acceptance.

## Reproduction and retained boundaries

From the prepared consumer root under WSL:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_direction_strip_151a7d6c_screen -v
make tools-check
```

The suite compiles the current owner and the proposal only in the ignored
target build directory. It asserts that the production placeholder remains,
checks the raw body fingerprint, and proves production source/ELF/guard/
conversion-row fingerprints do not change during the screen.

The final mounted suite passes in 22.741 seconds. The sibling-tools overlay
suite passes in 50.778 seconds; all four tested overlay files have the same
hashes as the committed mounted files. The sibling retains its 2,439 dirty
paths at `ddbdd16`, with identical before/after status digests. No sibling
files were copied over or committed. Project tool checks pass.

Raw candidate body SHA-256:
`2dbcf5d06e42583aeec00dd7a6ddb273a4888f04e5555c0d5fd1605678331280`.
The complete private proposed owner source hashes to
`576a5f53fc53d85bb6c6de54f76b57664a1faf8643f9c1030e97c486cfd5674c`.

Graphify was queried before analysis. The normal scoped update filtered
out the submodule files, so an explicit AST-only extraction/merge indexed
the four tools files. The merge retained all **60,152** existing IDs and
produced **60,182 nodes / 113,421 links**, with no lost nodes. Global fuzzy
deduplication was disabled after a pre-write retention check rejected it.
This is a four-file update, not a full-corpus re-extraction.

## Remaining matching work

1. Resolve or precisely justify the remaining 157 words. The current
   differences include private local homes, temporary register roles,
   the two independent render-table loads and loop-tail scheduling.
   Examples of raw versus retail stack homes are cursor C4/C0, delta
   B8/B4, closest AC/A8, camera 9C/8C, magnitude 98/88, sync 97/87,
   last index 94/84 and projection parameter 90/78. The saved-register
   frame and all 373 word positions already have the correct extent.
2. Qualify private-home aliases, access boundaries and any proposed
   normalization. Run both padders and independent rebases, including
   relocation carry boundaries, before installing anything. No guard
   rows or padded candidate have been adopted by this screen.
3. After those gates pass, perform actual Make, the independent strict
   whole-image prediction, all affected-object/address/data/header/guard
   audits, fresh production recount, documentation and tools-first commits.

The production checkpoint remains total **4,477 / 5,516 (81.16%)**,
Game **3,804 / 4,843 (78.55%)**, Init **492 / 492**, Debugger **181 / 181**,
with zero address drift and 1,039 still different. **212** further total
matches are needed for 85%. This candidate adds no match credit. The 85%
goal remains active; the next action is the matching work above.
