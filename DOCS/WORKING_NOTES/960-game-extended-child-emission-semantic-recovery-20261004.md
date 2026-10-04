# Game Extended Child Emission Semantic Recovery

Date: 2026-10-04

## Scope And Result

Replace `func_150E93DC`'s zero-return placeholder in
`conker/src/game/generated_113D60.c` with the complete code-0x37 child callback.
Correct `func_15132A4C`'s pointer-return interface in `generated_15F680.c` and
return its constructor result. The constructor `func_1513264C` has only its
return type corrected; its three-word NULL-return body remains a placeholder.
No constructor recovery, complete effect pipeline or gameplay acceptance is claimed.

| Measurement | Retail | Recovered C |
| --- | ---: | ---: |
| Callback slot | 208 words / 832 bytes | 206 body words + two zero padding words |
| Callback stack frame | 0x128 | 0x138 |
| Aligned raw word differences | 0 | 200 |
| Pointer wrapper | 15 words / 60 bytes | All fifteen words exact |

Retail callback extent is `0x150E93DC..0x150E971C`, ROM
`0x11688C..0x116BCC`. No expected-word guards are added to either callback or
wrapper. Complete linked callback-slot SHA-256:
`e8fa58f879c32cea6d5b1df01d0b0c91d0f274c66e39e380121db942aec4a0cc`.
The wrapper extent is `0x15132A4C..0x15132A88`, frame `0x28`.

## Recovered Contract

Record+0x28 contains XYZ and the three rate/variation/progress floats. The
initial float RNG call precedes all rate, timestep and progress reads. Progress
advances by `(baseRate + sample * variation) * D_800BE9A4`. Only a strict
`progress > 1.0f` comparison enters or repeats the emission loop.

After the gate, capture `D_800A13C8` spread and `D_800A13CC` scale once.
Initialize the measured 124-byte descriptor once; retain constructor/helper
mutations to fixed fields across iterations. Its XYZ is at +0x28, flags at
+0x50, resource halfword at +0x56, and final initialized halfword at +0x74.
Retail's constructor copies 0x7C bytes to result+0x10. Descriptor holes are
not initialized, including the six tail bytes at +0x76..+0x7B.

Each iteration preserves this order:

1. Consume a discarded integer RNG call, then read the first resource byte
   `D_800A12F0[0]`. Neither resource nor scale table indexing advances.
2. Draw one float for the shared +0x08/+0x0C size, three for rotations, then
   one for +0x4C. Read their globals after the corresponding calls.
3. Consume another discarded integer RNG call, set +0x54 to 100, then draw
   two floats for +0x40/+0x48 using captured spread/scale and fresh offsets.
4. Draw two angles and a radius, then read the fresh `D_800A13E4` period.
   Invoke actual `func_151436B4(angle0 * period, angle1 * period, radius * 50)`.
5. Add parent XYZ after that helper, reset +0x61 to 8, and load record metadata
   after the helper. Call `func_15132A4C(&descriptor, 3, 0xFF, 0x1C, slot, context)`.
6. On nonnull return, copy 28 extra bytes to result+0x170. Reload progress
   after constructor/copy and subtract one even on allocation failure.

Thus one invocation consumes one initial float; each iteration consumes two
integer and ten float RNG calls. The first table byte is retail resource 7;
the first scale float is approximately 0.1. No Game data is changed.

The extra 28-byte stack region has **no retail initializer stores**. Semantic
C deliberately leaves it and descriptor holes unspecified. Do not zero it,
substitute parent extras, or treat its initial bytes as deterministic. This
retail stack-content dependence remains a qualification caveat, especially for
cross-project host synchronization and any future sanitizer-oriented work.

## Verification

`tools/tests/test_game_extended_child_emission.py` adds thirteen tests using
the actual callback, pointer wrapper, spherical helper and parent emitter.
They qualify layout, RNG order/counts, strict comparisons, captured versus live
globals, first-entry table use, signed samples, failure patterns, mutation
lifetimes, late metadata/position reads, progress reloads and the real parent
payload flowing into a separately allocated child record. Fresh standalone
IDO compilation and linking confirm the 206-word body, 0x138 frame, 200 raw
differences, full-slot hash and identity with the production slot.

The constructor is an explicit opaque allocation/descriptor fixture, not a
recovered constructor. Cos/sin are deterministic SDK boundary callbacks, not
transcendental qualification. The connected parent uses an opaque position
writer; earlier position-writer tests qualify its actual modes. Copy tests
check destination, length, nonoverlap and fences, not unspecified byte values.
Only the host fixture's callback compilation narrowly suppresses GCC
`-Wmaybe-uninitialized` for retail's untouched extra region; all other strict
warnings remain errors. No production warning suppression is introduced.

Fresh production compile, padding, relink, progress and matcher succeed.
All **145 combined tests pass in 30.051 seconds, no skips**; the thirteen new
tests also passed separately. Complete Init code (164,048 bytes), Init data
(17,376 bytes), and Game data (189,088 bytes / 720 owners) remain retail-exact.
Exact creators, wrapper and helpers, plus earlier parent/child/position-writer
recoveries, preserve their measured identities. Existing duplicate
`generated_12D630` recipe warnings and two unrelated pointer/integer warnings
in `generated_15F680.c`'s resource-owner cleanup remain unchanged.
Project tool checks, whitespace checks and all 2,719 local links in the touched
working documents pass. This is bounded host/source and static compiled-code
qualification, not full guest differential execution or natural gameplay proof.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_extended_child_emission tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_child_emission_callback tools.tests.test_game_descriptor_position_writer tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_fill_value_mask -q -f
make tools-check
git diff --check
```

## Sibling Boundary And Next

Read-only audit confirms active `64CBFDOGL/CMakeLists.txt` compiles
`recomp_out/.c`. Child `func_150E93DC` at line 731447 remains a zero-return
stub. Constructor `func_1513264C` at line 933252 and wrapper `func_15132A4C`
at line 934010 already contain recompiled bodies. Scoped production-source
search finds no named child override. Native DECOMP pointers cannot be copied
mechanically into the guest/RDRAM/recomp_context interfaces. No sibling source,
build, binary, save or frozen Release changes are included.

- [x] Recover and fit the complete code-0x37 child callback without guards.
- [x] Qualify the actual parent payload, callback, pointer wrapper and spherical helper.
- [x] Preserve full Init code/data, Game data and prior recovery identities.
- [x] Audit the separate PC source synchronization boundary.
- [x] Recover the 256-word / 1024-byte extended constructor `func_1513264C`;
  subsequently completed in [Note 961](961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md).
- [x] Qualify resource helper `func_151336A8`, also recovered in Note 961.
- [ ] Recover further loader/setup/attachment dependencies before pipeline acceptance.
- [ ] Pursue callback byte matching separately; 200 raw differences remain.
- [ ] Synchronize the child through PC guest/RDRAM interfaces.
- [ ] Qualify downstream update/rendering and natural effects.

Init remains 492 C / 47 assembly. No Init trial is adopted. Game stays 2,609
and total 3,282 byte-exact C functions, with zero instruction-address drift.
README aggregates do not change: the callback was already counted as C despite
its placeholder body. Recovery updates remain in these dedicated docs.
