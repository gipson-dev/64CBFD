# Note 1876: rotated origin callback direct C match

2026-10-30. `func_150CEF60`, owner `generated_FC410`, replaces its zero-return
placeholder with `void func_150CEF60(s32 unused)`. VA
`0x150CEF60..0x150CF040`, ROM `0xFC410..0xFC4F0`: all **56 words /224 bytes**
match directly from C after their nine original relocation bindings resolve.
No alignment tail, guard, insertion, omission or profile change is needed.
Tools commit: `80680620306a738ebdcfdd8d218b703b61044165`.

## Source and stack lifetime

The callback looks up object ID4, reads its float at+8 and scales it by
`D_800A0830`. It captures the angle across calls to `func_150AD78C` and
`func_150AD780`; the latter adds its phase offset and falls through into
the former's original trig implementation. It rotates point `(76,241)`
about origin `(-1,44)`, truncates the two coordinates and the late-loaded
`D_800A0834` depth into signed halfwords, and calls
`func_150A3444(2,x,y,depth)`. It finishes with `func_151749A0(5,3)`.

Its one incoming argument is the frame-layer view word, unused here. The
original caller's `FrameLayerCallback` is `void (*)(s32)` and ignores the
result. The target stores its incoming word at `SP+64`, saves RA at `SP+20`,
uses a64-byte frame, captures the angle at `SP+56`, and preserves the first
trig result at `SP+28`. No saved S registers are used.

The initial semantic source already emitted all56 words and the same arithmetic
and calls, but used frame32 and different spill offsets. Two-dimensional array
and structure layouts were explored privately. Ordering the ordinary scalar
declarations as second result, angle, geometry, first result recovers every
word directly. All original geometry variables participate in the equations;
no dummy storage or guards are introduced.

Raw C and original unresolved assembly word SHA-256:
`a19275841103bdb80e114783f6b17c14413ee1c947a8ecb2c131c3129744e751`.
Padded object SHA-256:
`44650ee8bde688944e41d22749b7a3d000e4659c0e7c762662f4829a548c7220`.
The measured helper declarations and two float externs are scoped to this
owner. Shared headers and the entire inherited guard manifest remain unchanged.

## Qualification and limits

Ignored receipts: `conker/build/game-rotated-origin-150CEF60-match/`.
`semantic_v14.py` and `private_checks_v16.py` pass; each tools copy then passes
eight fresh canonical checks plus shared tool checks. Production runs two
fresh installed checks per copy and reuses six unchanged semantic checks only
under exact input/module/artifact fingerprints.

- Guest:3,072 cases /9,216 executions, all56 words, three ordinary/global alias
  layouts, callback mutations, complete modeled state and access-trace equality.
  The angle stays captured while depth is loaded after both trig calls.
  Twenty-four extra incoming-home aliases are guest-only. Thirty access-prefix
  cuts include six branch-delay cuts. These qualify emitted order, not portable
  C faults, invalid pointers or hardware floating exception behavior.
- Rebase:72 cases over three independent GNU-linked entry/global/helper layouts,
  including low-half carry boundaries. All nine bindings are preserved.
- Caller:zero aligned direct JALs and one literal pointer at ROM `0x2317DC`,
  selector6 in the actual28-word `D_8008CD04` table. Forty-eight cases execute
  the original11-word window at `0x15174A2C..0x15174A58`, including selector0,
  enabled target dispatch, view words0/-1 and ignored return. The typed current
  parent is `func_151749F8`; earlier/later parent helpers remain bounded.
  No complete-parent execution claim is made.
- Original/current helpers:264 connected cases execute144 of151 loaded helper
  words. The lookup's28 words, trig fall-through range's73 words, setter's28
  words and phase updater's22 words are byte-identical to retail in the current
  ELF. The lookup stride is160; the output stride is52. An independent ordered
  polynomial/range-reduction reference checks the actual trig path. Reduction
  is modeled under default nearest-even rounding only. Missing-object lookup
  routes are outside the connected callback domain; no helper credit is added.
- Native32:1,024 cases per O0/O2/O3 profile, trapping UBSan, typed helper ABI,
  captured-angle/late-depth observations and object canaries. Sixteen effective
  semantic controls reject wrong IDs/offsets/providers/geometry/signs/index,
  phase, omitted phase and premature depth capture. Sixteen separately
  IDO-compiled controls are also effective. Native objects are allocated and
  nonaliasing, casts stay within representable signed-halfword values, and
  NaN payload propagation is not asserted.
- Fingerprints reject224 single-byte corruptions plus five size/binding/scope
  controls. An equivalent source with the wrong frame is rejected. Whole-image
  checks compare every byte and named definition without exclusions.
- Full owner:both neighboring functions and pools remain fixed. The actual
  three-command Make recipe reproduces the complete padded object and all
  three compact functions. Target/owner/Make diagnostics are empty.

Failed fixture receipts are retained. The first caller boundary needed virtual
code membership at its return address. A connected-helper object pool initially
overlapped the guest stack and was moved into a checked disjoint region. The
canonical input seal also caught seven stale prior-commit documentation files
in the cache; their exact Native versions were synchronized before qualification.
Production source and compiler flags were unchanged by these corrections.
Routine work used zero Claude/REA calls or dependency installs.

## Image, progress and banking

Production equals the independent literal ELF prediction:
**217 changed bytes =184 target-code bytes +one extent byte +32 metadata bytes**.
The metadata changes are two closed symbol/string permutations, preserving
every named value, size, type and binding. No offsets or sections are excluded.
All6,055 other bodies, all6,056 addresses, and189,088 Game-data bytes across720
owners remain fixed. Inventory CSV, map, linker script and guard CSV stay fixed.
All17,024 current sealed inputs are verified under declared source/output/doc
overrides. The older tools mirror preserves its2,066 inherited changed paths.

Adopted ELF SHA-256:
`75c040bc204987d47f023111b9ea825e2747a375eef7e99385f18c0ca6bc5e36`.
Actual Native ELF recount: **3,953/5,506 (71.79%)**, Game
**3,280/4,833 (67.87%)**, Init492/492 and Debugger181/181, zero drift.
The75% threshold is4,130/5,506, requiring **177** further exact functions.

Tools are committed before the consumer source/docs/pin commit. README changes
only two aggregate rows. Graphify refreshes the eleven supported changed files,
preserves the current baseline nodes and still-valid relationships, and retires
the placeholder's obsolete s32 return edges using the actual void declaration.
No full-corpus re-extraction, global clustering or centrality refresh is claimed.
The separately banked wiki cleanup and sibling host/editor state stay preserved.

Next private screen: `func_150E35DC`. Parked candidates remain uncredited. The wider
matching goal remains active. No push or pause.
