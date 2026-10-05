# Game Light Selector Candidate Fitting And Connected Frame Witness

Date: 2026-10-05. Starting HEAD: `1437bfe0`.

## Result And Decision

Resume the full 601-word `func_1515D914` candidate left before the Init
assessment. This function is a light selector/emitter, not simply the
"transform" placeholder described in earlier renderer handoffs.

Bank its complete experimental C body, emitted-code/native qualification and
new connected-caller rejection witness. **Do not replace the production
placeholder yet.** The no-unroll profile now fits, but a concrete connected
counterexample makes the caller-frame gate observable rather than hypothetical.

The recovered renderer `func_1510B9D0` has a 0xB8 frame versus retail's 0x98.
For a first eligible directional light, the selector reads an uninitialized
caller-relative distance word. Identical initial physical stack bytes can
therefore produce count 1 on retail and count 3 on the candidate path, with
a sixteen-byte final display-list cursor difference. A positional-first
control agrees. Fitting the callee and preserving its caller-relative load
do not establish connected frame equivalence.

The starting dirty files were the full candidate, its qualification module
and the bounded renderer-oracle extension. These are reviewed and banked
together here; no unrelated production or Init changes are included.

## Complete Candidate Contract

`tools/experiments/game_light_selector_candidate.c` recovers all fourteen
arguments of the original entry at `0x1515D914`, ROM `0x18ADC4`:

```c
Gfx *func_1515D914(Gfx *commands, s32 slot, s32 x, s32 y, s32 z,
                 s32 mode, u8 *lightData, s32 capacity, u8 *ambientData,
                 u8 *countOut, s32 channels, u8 *history, s32 flags,
                 u8 **nodesOut);
```

The light-buffer argument is a pointer, not the scalar interpretation in the
current production caller's legacy local declaration. This note does not
change that declaration or count the experimental interface as adopted.

The body preserves:

- Ambient helper arguments, optional secondary/environment RGB mixing and
  byte-narrowed alpha factors; optional three-quarter history interpolation.
- Repeated ambient RGB stores at offsets four then zero, leaving padding alone.
- The actor-position delta, `sqrtf(dz*dz + (dx*dx + dy*dy))`, 1000/length
  scale, signed coordinate truncation and zero-length fallback.
- Low-five-bit slot mask, linked-node traversal, selected/channel/disabled/
  exclusion gates, signed-halfword positions and packed float-pointer positions.
- Low-word squared-distance wrapping, signed radius rejection, stable strict
  less-than insertion and capacity-minus-one reservation for the auxiliary light.
- Single count-byte store, odd padding bit, optional node outputs and null pad.
- Page-dependent 48-byte light records, signed direction bytes, optional node
  marking, positional emitter callbacks and repeated late page reloads.
- The actual SDK count/DMA packet macros, odd padding source, auxiliary and
  ambient packets, zero-capacity path and returned display-list cursor.

The helper algorithms `1515E278`, `1515E43C` and `1515EC78` remain production
placeholders. Their fixture outputs and mutations are explicit callback
models, not actual implementations or natural rendering acceptance.

## Fresh Profile Fitting

The candidate source is unchanged during qualification. A six-profile screen
compiles that complete source, not a smaller substitute body. The first three
rows below receive the complete paired corpus; other rows are size screens
only. O2 and O2 no-unroll also pass a separate 168 initial-seed screen, not
full qualification; O1/g3 receives no such seed credit.
All compiler logs are empty.

| Profile | Body bytes / words | Complete text bytes | Frame bytes | Qualification |
| --- | ---: | ---: | ---: | --- |
| O2/g3 | 2444 / 611 | 2448 | 344 / 0x158 | Full finite corpus; body 40 bytes over retail |
| O1 | 2900 / 725 | 2912 | 272 / 0x110 | Full finite corpus; does not fit |
| O2/g3 no-unroll | 2212 / 553 | 2224 | 344 / 0x158 | Full finite corpus; fits complete text |
| O2 | 2428 / 607 | 2432 | 344 / 0x158 | Screen only; body 24 bytes over |
| O2 no-unroll | 2196 / 549 | 2208 | 344 / 0x158 | Screen only; smaller but not fully qualified |
| O1/g3 | 2916 / 729 | 2928 | 272 / 0x110 | Screen only; does not fit |

Retail owns 2404 bytes / 601 words with a 312-byte / 0x138 frame. Complete
qualified no-unroll text is 180 bytes below that slot, including twelve bytes
of standalone trailing padding. Body and complete-text extents are measured
separately. No production compiler override or word guard is added.

Qualified complete instruction hashes:

```text
O2/g3           be6bbb5a8e4181391a0436cbcfd74bbf079302e2541957c12be4ce03c5957f68
O1              d7d69b72a577328f17e6c68e0e2ecd5c80d1f852558f8e2e1aeded62fc34e4e0
O2/g3 no-unroll  6176b7f3d6b6a18e6f047028631f598df1beb926fe333475feeae6b4f422d4cc
```

The tracked test's `PROFILES`, compiler/link recipe and identity assertions
reproduce the qualified rows. The six-profile screen's flags, objects and
`matrix.json` remain ignored under `conker/build/game-light-selector-profile-screen/`.

## Initial Distance And Connected Witness

Retail `0x1515DC80` loads `t3` from `0xB4(sp)` in its 0x138 frame:
**entry SP minus 0x84**. Positional nodes recompute that distance; directional
nodes carry the previous value. A first eligible directional node can thus
depend on the incoming stack word. Zero initialization is not a faithful fix:
the retained negative control changes retail's selected count and cursor.

All three qualified profiles actually read the same entry-SP-minus-0x84 word
in the 168 poison/slot/page/capacity products. Seven independent word seeds
include zero, one, INT_MAX, signed-negative values and distinct byte patterns.
This is emitted-instruction evidence, not C-standard definedness or proof
for arbitrary aliases, helper behavior or upstream stack layouts.

The new witness executes the actual retail renderer/selector and the current
linked C renderer with each complete candidate callee. It preserves the
actual caller SP, outgoing argument cells and incoming physical stack memory.
Other renderer/light callbacks remain explicitly modeled. It does not reuse
the standalone selector's fixed entry SP as a substitute for caller state.

| Path | Renderer frame | Physical distance address with fixture SP 0x40000 | Seed | Count / final cursor |
| --- | ---: | ---: | ---: | --- |
| Retail renderer + selector | 0x98 | 0x3FEE4, entry renderer SP - 0x11C | INT_MAX | 1 / 0x20070 |
| C renderer + candidate selector | 0xB8 | 0x3FEC4, entry renderer SP - 0x13C | 1 | 3 / 0x20080 |

The difference is reproduced in all three profiles and also reverses when
the two seeds are swapped. Selected-node marking differs as well. Replacing
the first node with a positional node makes complete visible memory and the
final cursor agree, because the distance is recomputed before directional use.
These are **twelve connected paired witnesses/controls**, not twelve positive
equivalence cases. A passing rejection test proves the divergence was detected.

Resolve the caller-frame dependence or establish an authoritative real-input
domain that rules it out before promotion. Do not silently initialize distance
to zero, discard first-directional cases, or claim standalone success closes
the connected ABI. The candidate deliberately retains the uninitialized local;
that remains an explicit C-indeterminacy boundary, not a portable host solution.

## Qualification And Coverage

**All 109 final combined checks pass in 362.455 seconds, exit zero, no skips.**
The preceding 107-check run also passed in 358.727 seconds; the final run adds
the connected caller-frame witness and the static duplicate-entry check,
then repeats the whole corpus. These repeated runs are not additional cases.
The final dedicated receipt reports complete qualification and an unchanged
candidate source hash. Project tool, whitespace and checkpoint-link checks pass.

The three-profile corpus has **17410 completed standalone pairs per profile**,
52230 executions total, without crediting repeated qualification runs:

- 6144 empty-list capacity/flag/slot/page products.
- 3840 positional/filter/tie/float-pointer list products.
- 4608 optional-output and callback-mutation products.
- 90 defined mixed positional/directional cases.
- 168 first-directional seeded-stack cases.
- 1920 zero/finite actor-vector and wide-coordinate truncation products.
- 640 signed-wrapping distance and preselected-channel-gate products.

Visible memory, callback argument/order snapshots, returned cursor, saved
registers and output fences are checked. Models mutate pages after ambient
setup and between positional emitters, and mutate nodes/head after selection.
Stack scratch bytes are not normalized into visible memory equality or treated
as original frame identity. Arbitrary ordered access equality is not claimed.

The actual candidate body and extracted SDK macros also pass **192 strict
32-bit native cases derived from retail fixture outputs**, checking packets,
light/ambient/history buffers, selected nodes, node marks and fences. Cases
have an eligible positional node first. Scoped warning suppression covers
intentional uninitialized candidate locals; this is not general indeterminate
C or first-directional native acceptance. Helper algorithms remain models.

Collected coverage is 599 / 601 retail words, 601 / 611 O2/g3 body words,
717 / 725 O1 words and 543 / 553 no-unroll words. The two retail exclusions
at `1515DC50` and `1515E078` are duplicated words after unconditional-branch
delay slots, with no direct entry targets; the new static-entry check pins
that fact. Two optimized C duplicates are likewise unvisited. Eight additional
C words are SDK signed-division negative-offset corrections, not exercised
by nonnegative offsets in the qualified capacity domain. Do not claim all
instructions or invalid-input behavior were executed.

Checks cover capacities 0..11, four ordinary player slots, finite floating
inputs, explicit colors/alphas and fixed model fences. They do not establish
arbitrary capacity/slot safety, all aliases, FCSR/exception behavior, actual
helper results, private-stack provenance, real hardware, RSP/RDP submission
or pixels. Production remains the original zero-return C placeholder.

```sh
python3 -m unittest tools.tests.test_game_light_selector_candidate tools.tests.test_game_viewport_renderer tools.tests.test_game_viewport_command_helper tools.tests.test_game_palette_updater tools.tests.test_game_queued_segment_writer tools.tests.test_game_dual_matrix_emitter tools.tests.test_pad_generated_pc16 tools.tests.test_pad_c_object_word_patches tools.tests.test_check_game_data_layout tools.tests.test_init_remaining_assembly tools.tests.test_init_decompressor_slot_ledger tools.tests.test_init_startup_thread_contract -q -f
make tools-check
```

The candidate's ignored `conker/build/game-light-selector-candidate/qualification.json`
requires all fourteen successful methods, exact per-profile counts, 192 native
cases, 168 seed cases, twelve connected witnesses and an unchanged source hash.
It records `adopted: false`. Existing Init code/data, Debugger code and Game
data are checked separately against checksum-verified retail; this is an
existing-artifact audit, not a production relink.

## Next And Sibling Boundary

- [x] Recover the complete experimental light-selector/emitter body and fourteen arguments.
- [x] Find and fully qualify a fitting no-unroll profile without narrowing the algorithm.
- [x] Pin the actual caller-relative seed read and reject zero initialization.
- [x] Add zero-vector/wrapping/preselected products and retail-derived native outputs.
- [x] Demonstrate the connected caller-frame counterexample and positional control.
- [ ] Resolve the renderer/selector stack-lifetime gate before production adoption.
- [ ] Recover actual ambient/secondary/positional emitter helpers separately.
- [ ] Qualify actual downstream submission and natural light presentation.

Read-only sibling audit finds `func_1515D914` at `recomp_out/.c:1049919`,
its retained `CONKER_LIGHTCALL1D` diagnostics and original epilogue through
`0x1515E274`. Scoped host src/CMake search finds no named override for this
selector or the ambient/positional helpers. No generated host transplant,
sibling source/build, save or frozen Release changes are made.

Production owners, profiles, guards and README aggregates remain unchanged.
Init still has 492 C / 47 ASM entries. No new production conversion, fresh
relink, full decoder corpus, ROM promotion, push or broad-goal completion.
