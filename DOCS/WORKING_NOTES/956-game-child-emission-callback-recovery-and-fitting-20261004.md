# Game Child Emission Callback Recovery And Fitting

Date: 2026-10-04. Starting HEAD: `65fec413`.

## Result

Finish the preserved `func_150E8D5C` recovery in
`conker/src/game/generated_113D60.c`. The former zero-return placeholder is
now the complete code-0x34 child-emission callback, with a void record-pointer
interface. The measured descriptor is 0x70 bytes and uses the existing shared
`vertex` type. Correct the local constructor/wrapper pointer signatures in
`generated_15D730.c` without changing their O32 argument representation.

The interrupted ternary-based version emitted 225 words and failed the
224-word slot check. Expressing the two independent low-bit flag choices as
`(word & 1) << 7` and `(word & 1) << 6` preserves the RNG sequence and flag
values while reducing the body to **219 words / 876 bytes**, frame **0x120**.
The original slot is **224 words / 896 bytes**, frame **0x108**, VMA
`0x150E8D5C..0x150E90DC`, ROM `0x11620C..0x11658C`.

Five padding words preserve the following function's address. The full slot
has **213 raw word differences**; no guards are added. This is complete
semantic recovery, **not byte-exact matching**. Representation/matching
aggregates and README remain unchanged because the placeholder already counted
as C and was already non-matching.

The child-placeholder gate from
[Note 953](953-game-descriptor-position-writer-and-weighted-chain-recovery-20261004.md)
and the one-word build gate from
[Note 954](954-init-resume-conversion-decision-and-interrupted-game-build-20261004.md)
are resolved in source, bounded tests and a fresh production link. Downstream
record update/rendering, guest effect acceptance and PC-port synchronization
are separate unfinished work.

## Recovered Contract

The input is the 24-byte position/rate payload at record+0x28 emitted by the
weighted parent `func_150E8B1C`. Draw one initial float before reading the
payload rates, old accumulator or `D_800BE9A4`:

```c
progress += (baseRate + sample * variation) * D_800BE9A4;
```

Unlike the parent, the child has no total-weight multiplier. Enter/repeat only
while progress is strictly greater than one. Capture bonus `D_800A1390` and
angular period `D_800A1394` once after the first successful gate.

Each attempt, including failed allocation, consumes four integer RNG draws
and six float draws, in retail order:

1. Integer low four bits plus forty: the same signed-halfword size at +0x0A/+0x22.
2. Unsigned integer modulo 119 plus 100: byte +0x1B.
3. Float times **59**, plus 80: identical scales at +0x28/+0x2C.
4. Float and freshly loaded `D_800A1398/139C/13A0`: parameter +0x24.
5. Clear only flag bits 0xC0, then two integer low-bit choices for 0x80/0x40.
6. Reset the six per-attempt color/event bytes; draw both angles and radius.
7. Call actual `func_151436B4` with captured period and radius `sample * 20`.
8. Add parent coordinates loaded after the spherical helper returns.
9. Draw the sixth float and freshly read `D_800A13A4/13A8/13AC` for +0x4C.
10. Read record slot/context bytes +0x0C/+1, submit through `func_15130374`.
11. On nonnull result, copy exactly four captured bonus bytes to result+0xA8.
12. Reload the accumulator after submit/copy callbacks and subtract one,
    regardless of allocation success; test the strict repeat gate again.

Descriptor fixed fields are initialized once, not once per iteration.
Reserved bytes +0x5C..0x5F and +0x64..0x6F have no retail initializer: do not
zero them or claim deterministic values. The retained core constructor copies
the complete descriptor, including those unspecified bytes.

`func_15130280` remains original assembly, not a new C recovery. Its mode-zero
path requests class 0x2B and payload size `requestedBytes + 0xA8`, copies the
0x70-byte descriptor to result+0x10, and returns the allocated address or null.
The actual C wrapper passes a null optional third argument. All 61 constructor
words, 18 `func_15130374` words and 12 `func_151303BC` words remain raw retail-exact
after their local pointer declarations are corrected.

## Qualification

New `tools/tests/test_game_child_emission_callback.py` extracts the actual
production child body, descriptor/payload layouts, typed wrapper and spherical
helper. Thirteen tests cover:

- Layout, every initialized descriptor field and bounded output fences.
- Unsigned RNG residues, negative/high-bit words and all four flag combinations.
- Strict gate boundaries, repeated emissions and mixed allocation failures.
- Initial callback mutations before rate, delta-time and snapshot reads.
- Fresh per-sample scalar globals versus captured bonus/angular period.
- Live parent coordinates after math, but metadata after the last float draw.
- Constant descriptor fields surviving constructor mutations, per-loop fields
  resetting, and flag mutations between clear and OR preserving unrelated bits.
- Accumulator reload after submission or bonus-copy mutation, including failure.
- Signed/out-of-range scale and radius samples without invented clamps.
- Bounded nonfinite rate cases that fail the strict gate, without extra callbacks.
- Actual weighted parent copying its child payload, then actual child consuming it.
- Retail callback/literal contracts, unspecified holes and absence of guards.
- Independent fresh IDO compilation/link, production-slot identity and raw
  constructor/wrapper/helper/adjacent-creator byte checks.

The spherical C body is real; cos/sin are deterministic SDK boundary callbacks,
not transcendental accuracy tests. The typed C wrapper is real; the assembly
core's allocation/copy boundary is modeled, not executed as guest instructions.
The new weighted-parent connection uses a position-writer fixture; Note 953's
separate connected tests exercise the actual writer/lookup/spherical chain.
No full guest differential execution, every NaN payload/FPU mode, unbounded
positive-infinity loop, downstream rendering or whole-game proof is claimed.

Fresh production compile, padding, relink, progress and matcher pass. The only
build warnings are the existing duplicate `generated_12D630` recipe warnings.
The combined suite now includes the thirteen child tests and eight bitmap
right-shift tests: **121 tests pass in 21.320 seconds, no skips**. Project tool,
document-link and whitespace checks pass.

| Fresh linked evidence | Result |
| --- | --- |
| Complete Init code | 164,048 bytes retail-exact |
| Complete Init data | 17,376 bytes retail-exact |
| Game data | 189,088 bytes / 720 owners retail-exact |
| Child callback | 219 body / 224 slot words, 0x120 frame, 213 differences |
| Constructor / wrappers | 61 / 18 / 12 words raw retail-exact |
| Spherical helper / both creators | 34 / 39 / 39 words raw retail-exact |
| Weighted parent | 144 words / 0xC8 frame / 44 differences preserved |
| Position writer | 179 body / 218 slot words / 196 differences preserved |
| Match totals | Game 2,609 / total 3,282 exact; zero address drift |

Complete child-slot SHA-256:
`5804b8b394d8f1474e6e974134cb15f9c9db4a9c56f63df710ec7a71087a2f34`.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_child_emission_callback tools.tests.test_game_descriptor_position_writer tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_fill_value_mask -q -f
make tools-check
git diff --check
```

## Sibling Boundary And Next

Read-only audit finds that the active `64CBFDOGL/CMakeLists.txt` still compiles
`recomp_out/.c`, whose `func_150E8D5C` definition at line 730597 remains a
zero-return stub. A scoped search of `src/pc`, `recomp` and CMake finds its
symbol-table entries but no named override. PC-port source synchronization is
therefore an open task; this DECOMP fix is not automatically inherited by the
host build. No sibling source, build, binary or frozen Release changes here.

- [x] Finish the complete child body and resolve the one-word fitting failure.
- [x] Qualify actual C callback/helper/wrapper connections and raw adjacent bytes.
- [x] Freshly relink and preserve all Init code/data and physical Game data.
- [x] Remove the child-placeholder/build gate from current documentation.
- [x] Recover sibling callback `func_150E9178`: resolved by
  [Note 957](957-game-extended-weighted-emitter-semantic-recovery-20261004.md),
  153 C words, 54 differences; code-0x37 child remains unfinished.
- [ ] Pursue child/weighted-parent/position-writer byte matching separately.
- [ ] Synchronize the PC-port child implementation through its guest/RDRAM API.
- [ ] Qualify downstream record update/rendering and natural guest effects.

Init's 47 retained assembly entries and all existing conversion gates remain
unchanged. No compressed-ROM promotion, real-save mutation, runtime acceptance
or push is claimed.
