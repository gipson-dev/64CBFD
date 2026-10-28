# 1773 - Record Sound Selection Match - 2026-10-28

The adopted Native ELF measures **3,851/5,506 exact C functions (69.94%)**,
Game **3,178/4,833 (65.76%)**, zero address drift and 1,655 different.
Only `func_1509F4E8` gains matching credit. The unchanged 75% threshold is
4,130 exact C functions, requiring **279 more**.

## Recovered routine and interface

`func_1509F4E8` in `generated_CBDB0.c` occupies VA
`0x1509F4E8..0x1509F5A8`, ROM `0xCC998..0xCCA58`: 48 words, a
56-byte frame and four bindings. HI16/LO16 at +24/+28 read the table pointer
`D_800D3098`; J26 at +100/+168 call `func_1000F568` and `func_10010F88`.
The full body emits directly from semantic C with no guards or profile change.

The recovered interface is `u16(s32 first, s32 last, u16 volume, s32 index,
u32 distance)`. The owner-local `RecordSoundEntry` has signed x/y/z and
distanceLimit fields at +0/+2/+4/+6, with stride 52. Declare this owner
interface as a pointer at `D_800D3098`; do not use the legacy array view
from the shared variables header. No shared-header repair is included.

Capture the record pointer and signed limit before sound selection. Compare
the unsigned distance against the sign-extended limit converted to u32; if
at least that bound, replace distance with limit minus one. Preserve zero
and negative limits without adding a new validation policy. The selector
receives first and the low byte of wrapped unsigned `last - first + 1`.
After selection, read the live coordinates and call the sound wrapper with
`(selected, volume, 0, 0, 0, x, y, z, distance, limit)`. Return its u16 handle.

The first private nested-call source happened to emit the same IDO words,
but left coordinate-read timing unspecified in C. The adopted source uses
an explicit selected-value statement before the coordinate arguments. This
preserves the 48-word match and gives native compilers the required order.
Canonical helper prototypes sit at file scope: block-scope prototypes
conflicted with IDO implicit declarations. All 16 neighbors remain unchanged
after the explicit declarations, including their raw bindings and pools.

## Original caller and retained helper

The complete ROM census finds one direct site, ROM `0xCC5F0` / VA
`0x1509F140`, and no target pointer literals. The original parent is
`func_1509EFF0`, still a zero-return placeholder in the same owner.
Execute these actual windows together, including the final parent return:

| Window | Purpose | Words |
| --- | --- | ---: |
| `0x1509F0B0..0x1509F0B8` | Recognized dispatch and first-argument load | 2 |
| `0x1509F128..0x1509F150` | Remaining arguments, call and return branch | 10 |
| `0x1509F238..0x1509F248` | Saved-register restoration and final return | 4 |

The retained `func_10010F88` wrapper is all 29 original words, and its current
bytes equal retail. Connected guest tests execute its argument narrowing and
forwarding to `func_10010E78`; native tests compile its actual current C.
The random selector and final voice provider stay bounded. In particular,
zero choice-span probes verify this adapter forwards zero, not that the real
selector accepts it: the retained selector performs a modulo operation.
There is no full-parent, complete voice-engine or gameplay acceptance claim.

## Complete owner and image

All 16 neighboring functions, pools and bindings remain fixed. The actual
three-command generated Make recipe uses normal O2/g3 to compile, pad and
assemble the complete 17-function owner with zero diagnostics. This owner
has no GLOBAL_ASM routines. The guard manifest remains unchanged.

Strict independent prediction permits exactly **149 changed image bytes**:
148 target code bytes and one target symbol-size byte (12 to 192), with zero
exclusions. Production reproduces that image. All 6,056 disassembly addresses,
all 6,055 other bodies, named ELF definitions, section geometry, map and
C inventory remain fixed. All 720 Game data owners /189,088 bytes remain
exact. The inherited duplicate generated_12D630 Make warning persists.

## Behavioral qualification

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production reruns two installed methods per copy; six semantic checks are
reused only after exact input, module and artifact fingerprint comparison.

- 5,104 guest cases cover all five argument words, signed limits with
  unsigned comparisons, all byte-sized inclusive choice spans, thirteen
  global-pointer aliases, ten stack/record overlaps, live home/local
  mutations and provider clobbers. All 48 words are visited; complete state
  and ordered traces agree. Guest-only stack probes are not native C claims.
- 144 cases execute all sixteen original caller/return words. Another
  80 cases execute all 29 retained sound-wrapper words with narrowed
  coordinates, distances, limits and result handles.
- Native32 O0/O2/O3 each pass 327,680 cases through the actual five-input
  function-pointer type, with trapped UBSan, whole-storage fences, every
  signed halfword limit and u16 handle, valid signed indexing, defined
  unsigned range wrap and selector mutation of coordinates/table pointer.
  All thirteen semantic negatives fail. A distance of 0x10000 explicitly
  distinguishes the signed limit from an incorrect unsigned halfword limit.
- 560 fired fault-prefix pairs preserve full state, trace, PC and delay
  context. The captured table pointer and limit storage can be unmapped
  after selection, while live coordinate reads remain required.
- Three GNU layouts pass 24 execution cases, exercising HI/LO signed carry
  and both J26 bindings. Real padder reproduction, three raw/binding
  rejection controls, four actually compiled IDO semantic negatives and
  six complete-image corruptions reject changed behavior or evidence.

## Bank and continuation

Baseline consumer `89968edd`, tools `b93ec40`. Tools are committed first as
`4264e562e9f9bb71070195a1f88eee0e996df99a`. The seal verifies 16,302 files and
303 focused inputs. Preserve all 1,760 inherited dirty paths in the older
independent tools mirror, adding only the three target modules there.
No mirror commit or push is requested. Host Release remains frozen.

| Artifact | SHA-256 |
| --- | --- |
| Adopted ELF | `7c7cfc7130d6a79f63f19d33843690a535dad6ff33628d1005516ff881a247e0` |
| Padded owner | `bb2b20dbafedfbe5763ac1754341cd1de74d2d54c0f3bb677b19e3b2079ba3d9` |
| Recovered source | `ce5f76e851e3c17ac6b74c9863de0a3cfc2eb9363ae2ea70fec2bc7192a6da85` |
| Raw original/compiler body | `8e24df1fe41a5085384d5b95e3ffe62429f204d4b132e45cf3af0a545c0efb2f` |
| Complete retail body | `5d06d24929cfc2d0ad6f3ddd12a27a814909fe108782d57d0c5b3b2c474ef45c` |
| Unchanged guard CSV | `20131e428c071ea6d2cbee21968f122274bc71fb167a2a356b3033ff5582f8b9` |

Scoped Graphify closeout refreshes eleven changed C/Markdown/tool files.
Retain all 46,001 old nodes and account for all 94,370 old relationship
contexts, retiring only the target placeholder false s32 return. Preserve
outside-scope manifest freshness and historical communities; validate the
u16 result, five parameters, two call bindings and original caller windows
without inventing a current parent call edge or full-corpus extraction.

Next inspect the 48-word `func_150A2EE4`. The remaining queue contains
1,526 placeholders, 120 semantic/other entries and nine unlocated screens;
it is triage only. Keep `func_1514E920` parked and uncredited and the 75%
goal open. Routine Claude calls: zero.

Prepared-checkout command:

```sh
python3 -m unittest tools.tests.test_game_record_range_sound_match -v
```
