# Point Sound Position Direct C Match

Date: 2026-10-24. Consumer predecessor `ef8e89b9`; tools predecessor
`aece1985`. Qualification tools committed first as
`a6facec1558224fb67ef5649ace6d930d76d0ea3`. No push requested/performed.

## Recovered Routines

Both routines live in `conker/src/game/generated_1C2C60.c` and replace
three-word / twelve-byte no-argument zero-return placeholders. Each complete
176-byte / 44-word routine emits directly from semantic C, frame 48,
one `R_MIPS_26` binding at +0x98 to `func_1000F91C`. No instruction guards,
inserted instructions, folded words or compiler-profile changes.

| Function | VA Span | ROM Span | Point Stride | Audio Handle |
| --- | --- | --- | --- | --- |
| `func_15198C90` | `0x15198C90..0x15198D40` | `0x1C6140..0x1C61F0` | 36 | +0x66 |
| `func_1519BFBC` | `0x1519BFBC..0x1519C06C` | `0x1C946C..0x1C951C` | 40 | +0x130 |

Span ends are exclusive. Raw compiler C hashes, in table order:

`97ed7189afd09500658d82adf49faae8dd7821438042fe3f41c6699befd127e3`

`04a4e79ffeaa13decb6fac3302b8df595749b87e0a2df3466ab3ae777dc4a8a9`

Resolved/retail hashes:

`a93b6e7bde2edb86e0e84b1eedf5fba6784ab59a7e0e9bdd639f88c918a531db`

`1074538162e4c6155b13f098145108200a7c3d760b81854016f753570638ba13`

Recover the void callback interface with a local typed owner view: signed
active/index bytes at +0x2C/+0x2D, points at +0x94 and audio data at +0x98.
Use distinct complete 36/40-byte point records; their first three fields are
float XYZ, while the remaining bytes remain opaque. These are local views,
not a claim to recover the full parent subsystem's shared types.

For every nonzero active byte, including signed-negative values, read the
unsigned halfword handle. If nonzero, use the signed point index to submit
XYZ converted through signed word to the helper's real short parameters.
Other arguments are handle, 32767, zero/zero/zero, near 500 and far 5000.
The inactive path ignores both pointees; a zero handle ignores the points.
Do not add dereferences or change either gate to a positive-only comparison.

Preserve the actual helper declaration:
`void(u16, u16, s16, u8, s32, s16, s16, s16, s16, s16)`.
Using inline `points[state->index].x/y/z` expressions and the original local
declaration order recovers retail's evaluation/allocation schedule. A
separate point local left ten word differences; capturing active left twenty.
Do not hide those differences with an unprototyped or word-parameter helper.

## Caller And Audio Boundaries

The aligned retail scan finds one literal registration per routine, at
ROM 0x234354 / 0x23437C, corresponding to VA 0x8008F894 / 0x8008F8BC.
No direct JAL sites reference either root. Qualify registered entry zero
and the signed -1 disabled-selector paths using the original windows
`0x15196A40..0x15196A78` and `0x15199B88..0x15199BB0`.
The first window must include its selector load at 0x15196A40, not start
at 0x15196A44 with an unseeded selector register. Across 48 phases,
preserve complete state and the actual indirect owner argument. The larger
C parents remain placeholders, and the full table extents are not proven.

Retained Init `func_1000F91C` already matches all 46 words at ROM
0xF91C..0xF9D4. Execute its actual guest body connected to both roots,
and compile its existing semantic C into the native fixture unchanged.
Check the ten-argument contract, signed-short coordinates, original output
home and four ordered parameter submissions. The lower attenuation service
`func_1000F6B8` and parameter service `func_1000F85C` remain bounded providers.
Verify command 8's scaled value, command 4's low seven pan bits, command
256's high pan bit and command 16's zero value; do not infer audibility,
full attenuation behavior or hardware acceptance from these probes.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips and zero reused checks. Primary/mirror
pre-install: 28.744s / 28.281s; installed: 29.641s / 29.057s.
Both shared project tools checks exit zero. Reuse existing MIPS, float,
native32, fault/frame, source-span, relocation and padder helpers.

- 13,312 guest phases cover every signed-byte index, every active byte,
  zero/nonzero handles, provider mutations and both stack phases. Visit all
  88 root words; compare independent expected calls/public memory as well
  as complete original-versus-C state and events.
- 416 ordered-alias phases include point data overlapping outgoing homes.
  Model stores and float reads in emitted order, including Z before the
  near/far stores. These are guest alias/order checks, not portable C
  promises about unrelated object or stack aliases.
- Twenty guest-only invalid/out-of-range FP phases reuse the established
  MIPS conversion model. No native invalid float-to-integer conversion or
  hardware FCSR behavior is claimed.
- Native32 O0/O2/O3 with trap UBSan covers 1,048,576 selected cases per
  optimization and twelve effective defined wrong-C controls per routine.
  Use complete typed owner/point arrays with centered in-bounds indexing
  and allocated audio storage; check opaque bytes and legal mutations.
  Finite float values are signed-word representable. Wrong unsigned/next
  indices remain physically in bounds, so controls do not rely on UB.
- The first reduced native control set accidentally made low-byte X
  truncation indistinguishable. Expanding negative controls across all 256
  indices supplies effective witnesses; every final control is rejected.
  Keep the original helper prototype, strict diagnostics and UBSan intact.
- 1,440 connected helper phases visit all 46 retained setter words with
  bounded attenuation/pan responses and caller-clobbered state. Native
  attenuation fixtures keep signed multiplication representable; the
  wrapping large-scale witness is guest-only.
- Eighteen independent GNU links cover original, qualified padded and actual
  Make objects at three placements. Pass 144 rebase phases, 640 fired root
  access-fault prefixes and ten effective strict-image corruption controls.
  Fault comparisons include complete state, PC and delay origin; they are
  not portable C fault semantics.

## Production And Preservation

Seal 15,938 initial native files and add the two owned tools files in both
copies: 15,942 files / 28 focused inputs, covering all 1,454 linker objects.
Verify every native/cache static input and non-target object. Only the
target C source, padded object and ELF receive audited manifest overrides.
Use checked native streams rather than DrvFS project reads.

Actual shadow Make executes the ordinary three commands with IDO
`-O2 -g3`; all 69 compact owner functions and the entire padded object
equal independent qualification. Preserve all 67 other owner functions,
their pools and diagnostics. Isolated selected routines have no diagnostics.
The inherited duplicate generated_12D630 Make recipe warning remains;
this is not a claim of a warning-free complete build.

Production Make exits zero in 0.560s and reproduces the independently
predicted complete image and qualified object. Exactly 253 ELF bytes
change: 251 target-code bytes and two symbol-size bytes, updating both
twelve-byte extents to 176. No metadata reordering or exclusions. Preserve
all other 6,053 bodies, all 6,055 addresses and protected Game data:
720 owners / 189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The full historical guard CSV is byte-identical, SHA-256
`b34cd973e3296eaa713abdba47414885e1855bdac1bc9f72efa5b65cbf979f2d`.

After both fresh installed suites, audit all 15,942 native entries before
and after adopting the generated outputs. Recapture the actual adopted ELF
and independently recount that stream; do not infer the aggregate by +2.

Installed ELF SHA-256:
`722cbc9e2520db992ef0b045f2c6bb22aba24fba8051b7b3bf1d4d1d5b8075f8`.
Installed target object SHA-256:
`3cfd69b18bc712878bb5e3e69d6c391b9b6fa377007659941aaa6d468e7225aa`.

Preserve all 1,598 pre-existing older-mirror dirty paths, statuses, hashes
and HEAD. Add only the two owned tools files there, leaving 1,600 dirty
paths; do not reset or commit that independent mirror. Host Release,
saves, configuration, private inputs, providers and dependencies are untouched.

## Measured Progress And Resume

| Section | Byte-exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,770 / 5,505 (68.48%) | 0 | 1,735 |
| Game | 3,097 / 4,832 (64.09%) | 0 | 1,735 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Remove exactly the two installed routines from the live-ELF-pinned queue.
Remaining source screens: 1,605 simple placeholders, 121 semantic/other
definitions and nine parser-unlocated entries. These are triage categories,
not qualification. `func_1510D8C0` already has `Gfx *` C missed by the
simple parser; its private screen and `func_1518C850` remain uncredited.
Continue the remaining 44-word queue, keeping the 862-word
`func_1508CAD8` owner stub separate.

The 75% target remains 4,129 exact C functions: 359 more, goal incomplete.
Root README changes only its two aggregate matching rows. Retain normal
post-commit Graphify worker receipts and audit all eight changed-file
hashes/mtimes/membership plus retention of the 43,923 old nodes. Do not
claim old-edge retention, full-corpus re-extraction or forge a commit stamp.

Ignored evidence: `conker/build/game-point-sound-position/qualified/`.
Tools: `tools/experiments/game_point_sound_position.py` and
`tools/tests/test_game_point_sound_position.py`.
