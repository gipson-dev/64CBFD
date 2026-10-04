# Game Descriptor Position Writer And Weighted Chain Recovery

Date: 2026-10-04. Starting HEAD: `d191ef8e`, clean worktree.

## Result

Replace `func_1514470C`'s zero-return placeholder in `src/game_16EE20.c`
with its complete four-mode descriptor-position writer. Recover the
`void (void *descriptor, void *output)` interface and update the two current
callers' local declaration in `generated_113D60.c`. Both discard the old
provisional integer result; retail paths do not provide a consistent return
value. Keep shared `struct134` declarations unchanged because that provisional
layout does not accurately describe all fields this routine reads.

The original allocation is **218 words / 872 bytes**, VMA
`0x1514470C..0x15144A74`, ROM `0x171BBC..0x171F24`, with a 0x98 frame.
Semantic C emits **179 words / 716 bytes with a 0x78 frame**; established
padding preserves the full slot and next entry. There are **196 raw word
differences across the full slot**, including padding. No instruction guards
are added. This is full semantic recovery, **not a byte-exact match**.

The position-placeholder/uninitialized-child-coordinate gate from
[Note 950](950-game-weighted-event-emitter-semantic-recovery-20261004.md)
is resolved in source and the bounded connected tests below. The child callback
`func_150E8D5C` was still a placeholder at this checkpoint; that source gate is
now resolved by [Note 956](956-game-child-emission-callback-recovery-and-fitting-20261004.md).
The complete effect pipeline remains unqualified: downstream update/rendering,
guest gameplay and host synchronization are separate from these recoveries.

Representation and matching aggregates are unchanged because the replaced
placeholder was already counted as C and the replacement is not byte-exact.
README therefore remains unchanged: Init 492 C / 47 assembly; Game 2,609 and
total 3,282 exact, zero instruction-address drift.

## Descriptor Contract

Offsets are measured directly from retail loads and stores, not inferred from
the existing provisional structure names:

| Descriptor offset | Access | Use |
| --- | --- | --- |
| `0x00`, `0x02`, `0x04` | Signed halfword | Base coordinates, loaded at each output store |
| `0x06`, `0x08`, `0x0A` | Signed halfword converted to float | Width/radial extent, height, depth snapshots |
| `0x15` | Byte, low two bits | Sampling mode |
| `0x24`, `0x28`, `0x2C`, `0x30` | Float | Four transform-coefficient snapshots |

The three dimensions and four coefficients are captured before any RNG/helper
callback. The selected mode is not reread after callbacks. Base coordinates
remain live until output writes, so helper-induced base changes are observed.
All paths write three floats at output offsets 0, 4 and 8. No descriptor clamp,
null guard, angle/radius restriction or invented failure return is added.

### Mode 0: Radial And Height Sampling

1. Draw a float sample and multiply by the captured signed width.
2. Draw integer RNG and retain its low byte as the angle.
3. Obtain X from `func_151423D8((u8)(angle - 0x40)) * radius`.
4. Draw another float sample and multiply by captured height for Y.
5. Obtain Z from `func_151423D8(angle) * radius`.
6. Apply the captured transform and add the live base coordinates.

This is a uniform radial-length sample, not a new area-uniform distribution.
The lookup helper is the existing actual C routine, backed by the retail
65-entry `D_8009A220` pool; the phase subtraction wraps as an unsigned byte.

### Mode 2: Rectangular Sampling

Three float draws produce X, Y and Z in original single-precision grouping:

```c
x = sample0 * (width + width) - width;
y = sample1 * height;
z = sample2 * (depth + depth) - depth;
transformed = y * coefficient24 + z * coefficient28;
outX = baseX + (x * coefficient30 + transformed * coefficient2C);
outY = baseY + (y * coefficient28 - z * coefficient24);
outZ = baseZ + (transformed * coefficient30 - x * coefficient2C);
```

Mode 0 uses the same transform. The recovered C shares it after the two sampling
branches; retail duplicates it. That control-flow/lifetime difference, smaller
frame and register allocation are substantive matching work, not a few
independent scheduling words eligible for broad normalization.

### Mode 1: Spherical Helper

Draw all three float samples first. Then load `D_800A56A0`, retail ROM
`0x24A160`, word `0x40C90FDB` (float 6.2831854820251465), and call the existing
`func_151436B4(sample0 * period, sample1 * period, sample2 * width, &point)`.
Add the live signed base coordinates to the helper's three outputs. The helper
already has a semantic C body and remains raw byte-exact; it was not replaced
as another placeholder. Its cos/sin calls remain ordinary SDK boundaries.

### Mode 3: Direct Base Coordinates

Copy the three signed halfwords as floats. No RNG, table lookup or spherical
helper is called, irrespective of the upper six flag bits.

## Fresh Qualification

New `tools/tests/test_game_descriptor_position_writer.py` contributes eleven
tests covering:

- All 256 flag bytes and all four modes, independent coordinate goldens and
  output fences; all three coordinates replace sentinel storage.
- Integer-angle byte narrowing and cardinal quadrants through the actual lookup
  body and bit-preserved retail table values.
- Signed negative/extreme dimensions and negative/out-of-range RNG samples,
  without replacing retail behavior with clamping.
- Nontrivial captured transforms and exact single-precision golden outputs.
- Callback mutations proving dimensions/coefficients/mode are snapshots while
  bases reload after callbacks.
- Period loading after the third sample and stable helper arguments despite
  later period mutation, through the actual spherical C body.
- Infinity/NaN propagation classifications; no claim of every NaN payload or
  floating-point exception/rounding mode.
- The actual weighted emitter calling the actual writer, lookup and spherical
  helper: all modes, allocation success/failure, distance culling, exact
  RNG counts, accumulator consumption, child metadata/payload and fences.
- Independent O32 IDO compile/link: 179 words, 0x78 frame, 196 full-slot raw
  differences, zero trailing text and identical fresh production-slot bytes.
- Exact retail slot/frame, pool value, recovered void declaration and no guards.
- Seven selected production helpers/neighbors compared directly to raw ROM.

The spherical tests use explicit deterministic cos/sin boundary callbacks,
not a replacement trig implementation or a claim of SDK transcendental accuracy.
The connected tests mock allocator/copy/origin and RNG boundaries, not the
position writer. Host arithmetic uses 32-bit fixtures, SSE single precision and
disabled contraction. These are bounded C contract tests plus linked-machine
code checks, **not full MIPS differential execution or gameplay acceptance**.
Descriptor/output overlap, concurrent mutation and the full hardware FCSR
domain are not qualified by these fixtures.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_descriptor_position_writer tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_init_remaining_assembly -q -f
make tools-check
git diff --check
```

Fresh production compile, padding, assembly and full relink succeed. Existing
duplicate-recipe and unrelated owner-TU pointer-type warnings remain; the
standalone writer compile is warning-clean. Full existing Init code/data and
Game data are verified against checksum-validated retail by the combined audit:

| Artifact | Fresh result |
| --- | --- |
| Init code / data | All 164,048 / 17,376 bytes exact |
| Game data | All 189,088 bytes / 720 owners exact |
| Position writer | 218-word padded slot, 179-word body, 196 differences |
| Weighted emitter | Original 144-word body / 0xC8 frame, 44 differences unchanged |
| Pointer-selection wrapper | All 16 words exact |
| Lookup / spherical helper | All 27 / 34 words exact |
| `15144598`, `15144A74`, `15144AA8`, `15144B34` | All 37 / 13 / 35 / 13 words exact |
| Earlier creators / timer / dispatcher / world dispatcher | Retained exact-byte checks pass |

**All 100 combined tests pass in 16.552 seconds, no skips**, after adding the
connected culling/failure checks and production/standalone identity assertion.
Project tool checks pass. The eleven writer tests also pass separately.

SHA-256 of the complete new linked position-writer slot:
`bd43a4ff851b5766c8b092d30acc1df5210244ec379120975184c68200182792`.

## Sibling Source Boundary

A read-only `64CBFDOGL` source audit confirms its CMake input `recomp_out/.c`
already contains the original instruction-recompiled `func_1514470C`, including
the 0x98 frame and all three output stores in each mode. No plain-C transplant
into its `recomp_context`/RDRAM implementation is needed for this restoration.
This is source/build-input evidence only: no host binary freshness, build or
runtime acceptance is inferred, and no sibling file or frozen Release changed.

## Checkpoint And Next

- [x] Restore all four sampling modes and three output stores from semantic C.
- [x] Recover the void interface without inventing a result to force registers.
- [x] Qualify actual weighted caller/writer/helper connections and callback timing.
- [x] Fit the original allocation and preserve physical data/exact neighbors.
- [x] Remove the position-placeholder gate from the current handoff.
- [x] Recover code-0x34 child callback `func_150E8D5C`: resolved by Note 956,
  219 C words / 0x120 frame in the 224-word slot; still non-matching.
- [x] Recover sibling callback `func_150E9178`: resolved by
  [Note 957](957-game-extended-weighted-emitter-semantic-recovery-20261004.md).
- [ ] Pursue byte matching of the position writer and weighted emitter separately.
- [ ] Qualify actual guest effect behavior only after the connected callbacks exist.

No compressed-ROM promotion, sibling source transplant/build, Release change,
real-save modification, hardware/gameplay claim or push is made. Init's remaining
assembly ownership and fitting decisions stay unchanged.
