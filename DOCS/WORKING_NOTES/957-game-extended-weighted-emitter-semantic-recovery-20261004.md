# Game Extended Weighted Emitter Semantic Recovery

Date: 2026-10-04. Starting HEAD: `db3cb66f`, clean worktree.

## Result

Replace `func_150E9178`'s zero-return placeholder in
`conker/src/game/generated_113D60.c` with its complete code-0x36 weighted
emitter body and void record-pointer interface. The recovered routine selects
a weighted descriptor, obtains a position, applies strict squared-distance
culling and allocates code-0x37 children with a partially initialized 60-byte
payload. Reuse the existing position/rate/node types and add the measured
`ExtendedEventPositionPayload113D60` layout.

The original slot is **153 words / 612 bytes**, VMA
`0x150E9178..0x150E93DC`, ROM `0x116628..0x11688C`, frame **0xF0**.
Semantic C fits **153 words with a 0xF8 frame**, with **54 raw word differences**.
No padding expansion or instruction guards are needed. This is complete
semantic recovery, **not byte-exact matching**. Matching and representation
aggregates remain unchanged; the previous placeholder already counted as C.
README therefore remains unchanged.

The pending sibling-emitter recovery from
[Note 956](956-game-child-emission-callback-recovery-and-fitting-20261004.md)
is resolved in source and bounded connected tests. Its output callback
`func_150E93DC` still has a zero-return placeholder. Do not infer a complete
guest effect pipeline or accepted gameplay from this emitter alone.

## Input And Selection Contract

The actual creator `func_150E90DC` allocates code 0x36 and copies a 12-byte
rate/variation/zero-progress payload to record+0x28. This callback first obtains
the current player's origin via `func_15144B34(D_800BE9E8)`, then draws a float
before reading rate, variation, old progress, delta-time or total weight:

```c
progress += ((rate + sample * variation) * D_800BE9A4) * D_800DCD90;
```

The original single-precision grouping is retained. Enter/repeat only while
progress is strictly greater than one. Once the first gate succeeds, capture
`D_800A13B8`, `D_800A13BC`, `D_800A13C0` and `D_800A13C4` for the output
parameter, variation, rate and squared-distance limit respectively.

Each attempt draws a fresh selection float before rereading total weight and
head `D_800DCDC4`. Multiply by total weight; while the selected node's weight
is strictly less than the target, subtract it and follow the next pointer.
Equality remains on the current node; unordered comparisons do not invent a
new traversal rule. The original path assumes a valid list; no null guard,
weight normalization, clamp or finite traversal cap is added.

Call actual `func_1514470C(node->descriptor, &child.payload.position)`, then load
the saved origin pointer's coordinates and compare
`(dx * dx + dy * dy) + dz * dz < capturedLimit`. A culled attempt still consumes
one progress unit but does not draw integer RNG, allocate or copy.

## Output Payload

The 60-byte payload begins at allocated child record+0x28:

| Relative offset | Defined retail write |
| --- | --- |
| 0x00..0x0B | Three floats from the selected position writer |
| 0x0C | Captured `D_800A13C0` |
| 0x10 | Captured `D_800A13BC` |
| 0x14 | Float zero, child progress |
| 0x18 | Captured `D_800A13B8` |
| 0x1C..0x2F | Twenty bytes with no retail initializer |
| 0x30 | Word zero |
| 0x34, 0x35 | Two byte zeros |
| 0x36, 0x37 | Two bytes with no retail initializer |
| 0x38 | Word zero |

Reset all defined non-position fields on **every in-range attempt**, before
integer RNG. Leave the 22 reserved bytes unspecified; do not memset the payload
or assert deterministic initial contents. A successful copy transfers all
sixty bytes, including the reserved regions.

Draw an unsigned integer, compute `% 13 + 5`, narrow to the original signed
halfword duration, and call:

```c
func_15149130(duration, -1, 0x37, -1, 1, 0, 60, record[0xC], record[1]);
```

The metadata bytes are loaded after RNG. Only a nonnull result receives the
sixty-byte copy at +0x28. Reload input progress after allocation/copy callbacks,
subtract one on success or failure, and repeat the strict gate. No helper
return value or allocator-success assumption is invented.

## Fresh Qualification

New `tools/tests/test_game_extended_weighted_emitter.py` contributes eleven
tests extracting the actual creator, emitter and layouts. Coverage includes
full initialized-field checks and fences, all layout offsets, nonfinite
no-head gates, multihop/zero-weight selection and equality boundaries, unsigned
duration residues, allocation failures, strict distance/accumulator boundaries,
culled consumption, callback-sensitive rate/head/weight/origin/metadata/progress
reads, captured constants and repeated tail resets.

An explicit opaque-helper mutation fixture supplies known reserved bytes and
poisons defined fields before the parent reset. This checks that defined fields
are reset while holes are forwarded unchanged; it does not assert the initial
contents of untouched stack holes or claim the real helper writes beyond XYZ.

The actual creator's payload flows into the actual emitter and creates two
children with different selections. Another connection invokes the actual
four-mode position writer, actual lookup body with all 65 raw retail pool
values, and actual spherical C helper. All modes cover success, allocation
failure and culling, with independent coordinate goldens and expected RNG counts.
Cos/sin remain deterministic SDK boundary callbacks, not transcendental tests.

Independent fresh O32 IDO compilation/link verifies the complete 153-word body,
0xF8 frame, 54 differences, zero nonzero trailing text and identity with the
fresh production slot. Raw checks preserve both 39-word creators, the 34-word
spherical helper, 27-word lookup and 13-word origin helper. Callback-table
entries confirm code 0x36 -> `func_150E9178`, code 0x37 -> `func_150E93DC`.

Fresh production compile, padding, relink, progress and matcher succeed.
All **132 combined tests pass in 24.389 seconds, no skips**; the eleven new
tests also pass separately. Complete Init code (164,048 bytes), Init data
(17,376 bytes), and Game data (189,088 bytes / 720 owners) remain retail-exact.
The prior weighted emitter (144 words / 44 differences), position writer
(179 body words / 196 differences) and child callback (219 body words /
213 differences) preserve their measured production identities.

The only build warnings are the existing duplicate `generated_12D630` recipe
warnings. Project tool, document-link and whitespace checks pass. This is
bounded host/source and static compiled-code qualification, not full guest
differential execution, every malformed/nonterminating list, arbitrary FPU
mode/NaN payload, downstream renderer proof or natural gameplay acceptance.

Complete linked emitter-slot SHA-256:
`ef319998a5e6c55e5fa3e2808e82e710c7c49d01dfaef2bb0fd50ff886ec8b24`.

```sh
make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
python3 -m unittest tools.tests.test_patch_generated_slice_ld tools.tests.test_check_game_data_layout tools.tests.test_game_extended_weighted_emitter tools.tests.test_game_child_emission_callback tools.tests.test_game_descriptor_position_writer tools.tests.test_game_weighted_event_emitter tools.tests.test_game_event_payload_creators tools.tests.test_game_event_sound_dispatch tools.tests.test_game_world_emitter_dispatch tools.tests.test_game_curve_record_update tools.tests.test_game_random_curve_record tools.tests.test_game_random_edge_emitter tools.tests.test_game_positioned_emitter_descriptor tools.tests.test_game_random_dispatch tools.tests.test_game_fixed_random_parameters tools.tests.test_init_remaining_assembly tools.tests.test_init_bitmap_fill_value_mask -q -f
make tools-check
git diff --check
```

## Sibling Boundary And Next

The read-only sibling audit confirms active `64CBFDOGL/CMakeLists.txt` still
compiles `recomp_out/.c`. Its `func_150E9178` definition at line 731135 remains
a zero-return stub. A scoped search of `src/pc`, `recomp` and CMake finds the
symbol definitions but no named override. PC source synchronization is open,
not automatically accomplished by this DECOMP recovery. No sibling file,
build, binary, real save or frozen Release changes here.

- [x] Recover the complete code-0x36 emitter and partially initialized payload.
- [x] Qualify the actual creator and all four actual position-writer modes.
- [x] Fit the complete allocation and preserve existing linked code/data gates.
- [x] Audit and document the separate host source synchronization gap.
- [x] Recover code-0x37 child `func_150E93DC`, 832 bytes / 208 words;
  subsequently completed in [Note 960](960-game-extended-child-emission-semantic-recovery-20261004.md).
- [x] Recover its extended constructor `func_1513264C` and qualify resource helper
  `func_151336A8`, subsequently completed in
  [Note 961](961-game-extended-child-constructor-and-resource-helper-recovery-20261004.md).
- [ ] Recover the deeper loader/setup/attachment dependencies.
- [ ] Pursue the emitter's 54-word matching remainder separately.
- [ ] Synchronize both recovered callbacks through the PC guest/RDRAM interfaces.
- [ ] Qualify downstream update/rendering and natural guest effects.

Init remains 492 C / 47 assembly; Game remains 2,609 and total 3,282 byte-exact
functions, with zero instruction-address drift. No compressed-ROM promotion,
runtime acceptance or push is claimed.
