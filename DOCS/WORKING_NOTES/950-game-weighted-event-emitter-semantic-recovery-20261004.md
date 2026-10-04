# Game Weighted Event Emitter Semantic Recovery

Date: 2026-10-04. Starting HEAD: `b6eefb75`, clean tracked checkout.

Checkpoint review: the same 82-test suite passes again in 14.279 seconds with
no skips. The production make target is up to date, and a fresh matcher reports
the unchanged totals below. This rerun is not another rebuild or qualification
of the still-placeholder position writer. Bank this semantic recovery with its
explicit runtime gate, separately from the subsequent Init audit/trial.

## Result

Replace `func_150E8B1C`'s zero-return placeholder with its complete weighted
event-emission body and recover its `void (u8 *record)` interface. The compiled
body fits all 144 retail words with the original 0xC8 frame, but **44 raw words
still differ**. No instruction guards are added. This is semantic recovery,
not a byte-exact match or a runtime-ready effect pipeline.

Ten new tests qualify the recovered caller and the actual creator/updater
connection through explicit helper boundaries. All 82 combined tests pass,
and a fresh production rebuild/link succeeds without address drift. Full Init
code/data, Game data and previously exact neighbors remain intact.

Aggregate matching counts stay Game 2,609 / total 3,282 exact, 2,181 different.
Representation counts also stay unchanged: the replaced placeholder was
already counted as C. README aggregates therefore require no change.

## Retail Callback And Record Contract

The physical callback table `D_8008A4E8[0x33]` at `0x8008A5B4`, ROM
`0x22F074`, contains `func_150E8B1C`. Its next entry, code 0x34, contains
`func_150E8D5C`. The allocator stores its third argument in record byte 0x11;
the existing update dispatcher uses that byte to select this callback table.
Thus [Note 949](949-game-event-payload-creators-and-connected-dispatch-match-20261004.md)'s
first creator selects this emitter; its emitted children select the next
still-unrecovered callback. This does not qualify that child updater.

For this callback, the creator's twelve bytes at record+0x28 are:

| Offset | Recovered use |
| --- | --- |
| `0x28` | Base rate |
| `0x2C` | Float-RNG rate multiplier |
| `0x30` | Emission accumulator |

The existing generic payload field names remain shared with code 0x36, whose
updater has not yet been recovered. This note establishes their use for 0x33,
not their universal meaning for every event kind.

1. Obtain the current-player origin pointer from `func_15144B34(D_800BE9E8)`.
2. Draw a float RNG sample, then read the payload rates and accumulate
   `((base + sample * multiplier) * D_800BE9A4) * D_800DCD90` in original
   single-precision grouping/order. The initial payload reads occur after RNG.
3. Only while the accumulator is **strictly greater than 1.0**, draw another
   float sample and scale it by the freshly loaded total weight `D_800DCD90`.
4. Reload list head `D_800DCDC4`. While node weight is strictly less than the
   sample, subtract that weight and follow the next pointer. Equality selects
   the current node, including a zero-weight first node when the sample is zero.
5. Fill the selected position through `func_1514470C`, then read the origin's
   coordinates and compute `(dx*dx + dy*dy) + dz*dz`.
6. If squared distance is **strictly below** the captured limit, build a
   24-byte child payload, draw unsigned lifetime `RNG % 13 + 5` (5..17), and
   allocate using code 0x34. Only success copies to child record+0x28.
7. Reload and decrement the parent accumulator by one on every iteration,
   including culled positions and allocation failures, then retest `> 1.0`.

The list node's first word is a **descriptor pointer, not an integer ID**.
Retail `func_1514470C` dereferences that descriptor's signed halfword fields.
The local O32 node contract is descriptor pointer at +0, opaque word +4,
float weight +8 and next pointer +0xC, sixteen bytes total.

Adding its explicit pointer-input prototype also refines the local
`D_800D9A20` declaration to a pointer array for the existing selection wrapper.
All sixteen raw words of `func_150E6ED8` remain retail-exact after this change.
The shared position helper's currently declared integer result is ignored;
no success gate or result interpretation is invented here.

## Child Payload And Timing

`EventPositionPayload113D60` contains the selected three-float position followed
by three parameter floats, 24 bytes total. Before the emission loop, snapshot:

| Pool | Word | Role here |
| --- | --- | --- |
| `D_800A1384` | `0x3F85F40A` | Second child parameter |
| `D_800A1388` | `0x3EA25D8D` | First child parameter |
| `D_800A138C` | `0x4A45C100` | Squared-distance limit, 3,240,000 |

The third child parameter is positive zero. Child-updater meanings for the
first two parameters remain unassigned. The complete allocator arguments are:

```text
(s16 lifetime, s8 -1, s8 0x34, s8 -1, u8 1,
 u8 0, s32 24, u8 record[0xC], s32 record[1])
```

Draw the lifetime in a separate statement **before** reading the slot/context
bytes. The initial single allocator expression allowed the host compiler to
load those bytes before RNG, failing the mutation fixture. Explicit sequencing
restores the retail order and reduces the standalone mismatch from 53 to 46
words. Reusing the sampling temporary instead of keeping a redundant target
scalar then restores the frame from 0xD0 to 0xC8 and leaves 44 differences.
An intermediate declaration-only reorder did not improve the measurements.

The final 144-word body retains all control-flow behavior without a broad
normalization batch. Remaining differences include saved-register allocation,
initial address/scheduling choices, float-register allocation and child-stack
placement. No claim that they are only independent scheduling words is made.

Final linked-body SHA-256:
`e7be4237d5fe90c7581ac913539001c5b38b07fc59a1025bd2896afda8239ff9`.

## Qualification

`tools/tests/test_game_weighted_event_emitter.py` extracts the actual production
creator, emitter and layouts. Its host fixtures check:

- Initial arithmetic order, strict no-emission gates and finite/nonfinite cases
  that do not access a list head.
- Weighted equality boundaries, multi-hop traversal, zero-weight selection,
  unsigned lifetime residues/boundaries and allocation failures.
- Strict accumulator and squared-distance gates; culled attempts still consume
  accumulator units but do not draw integer RNG or allocate.
- Rate reads after the first float callback, live head/weight reloads after each
  later sample, and preserved pre-loop parameter/limit snapshots.
- Origin coordinate loads after position filling, progress reload after allocator
  mutation, and slot/context loads after integer RNG mutation.
- The actual first creator's retail rate payload flowing into this updater and
  emitting two children with distinct weighted selections.
- Independent expected metadata/rates, all child payload bytes and surrounding
  fences, instead of deriving expectations from the same output storage.
- Retail callback/pool/helper/call contracts and no guards for this function.
- Independent O32 IDO link: complete 144-word slot, 0xC8 frame, 44 differences,
  no nonzero trailing text, and 12/16/24-byte payload/node layout checks.

These are bounded host contract tests plus static retail/compiled-code checks,
**not guest differential execution of all 144 instructions** or complete-domain
proof. Unbounded positive-infinity accumulation and malformed list chains are
not qualified. No defensive null, weight clamp or loop cap is added to retail
behavior merely to make fixtures terminate.

```sh
python3 -m unittest tools.tests.test_game_weighted_event_emitter -v -f
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters -q -f
python3 tools/check_game_data_layout.py conker/build/conker.us.elf
make tools-check
git diff --check
```

**82 combined tests pass in 20.614 seconds, no skips.** Fresh compile, padding,
production relink and matcher pass; only the existing `generated_12D630`
duplicate-recipe warnings remain. Independent raw ELF/ROM checks after validating
ROM SHA-1 against YAML confirm:

- Complete Init code: 164,048 bytes exact; Init data: 17,376 bytes exact.
- Complete physical Game data: 189,088 bytes / 720 owners exact.
- Existing pointer-selection wrapper: sixteen words exact.
- Both curve routines, world dispatcher and retained 111/49/237-word owners exact.
- Existing 27-word creator, 28-word timer and 84-word dispatcher exact.
- Both recently restored 39-word creators still exact.
- New emitter: original 144-word slot/frame, 44 raw word differences, no drift.

## Runtime Gate And Next Step

**Original checkpoint gate, now resolved by
[Note 953](953-game-descriptor-position-writer-and-weighted-chain-recovery-20261004.md):**
`func_1514470C` was a zero-return C placeholder in
[game_16EE20.c](../../conker/src/game_16EE20.c). It did not fill the requested
position. At that checkpoint, invoking the recovered emitter through the
incomplete guest pipeline could read an uninitialized child position. This
note's original fixtures use an explicit position-writer stub; Note 953's
connected tests now exercise the actual writer and its two C helpers instead.

The writer has a complete semantic body. The code-0x34 child updater
`func_150E8D5C` is now also recovered and connected to the parent's payload in
[Note 956](956-game-child-emission-callback-recovery-and-fitting-20261004.md).
Sibling callback `func_150E9178` and downstream record update/rendering remain
unfinished. Byte matching of the emitter, writer and child are separate open
tasks; no runnable/accepted guest effect chain is claimed.

No compressed-ROM or host-port promotion is warranted by this checkpoint.
No sibling build, Release modification, real-save change, gameplay acceptance
or push is claimed. Init's remaining assembly gates stay unchanged.
