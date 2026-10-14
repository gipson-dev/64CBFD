# Game Actor Vector Mode-1 Direct Match

Verified locally: 2026-10-13. This is retail guest matching, not host-port or
full-game acceptance. Continue the wider Game goal without changing frozen
host Release artifacts, real saves, unrelated work or older mirror history.

## Target And Baseline

- Function: `func_1506A968`, owner `conker/src/game/generated_97AA0.c`.
- VA `0x1506A968..0x1506AA08`, ROM `0x97E18..0x97EB8`.
- Complete40-word /160-byte routine, frame `0x38`, ordinary O2/g3/MIPS2.
- Consumer baseline `4b63a191cda482e43725684753e3d8367767cd98`.
- Tools baseline `6d547514347e72cc93e6e5e9b9eccb6eb2fb799d`.
- Before source SHA-256
  `2693d762473eda06176457fb4bfa041c953b53258e6ca84a3c443f8bd039e422`.
- Before ELF SHA-256
  `3f55344bf1320fc76c68057c98eb1f6dfbf80489a62e084bca4a0aa97d59b33c`.

Both active trees start clean. Preserve the independently dirty older tools
mirror's HEAD ddbdd16 and455 recorded fingerprints. Baseline snapshots and
receipts remain under ignored `conker/build/game-actor-vector-mode1-match-test/`.

## Recovery

Replace only the zero-return placeholder with a void callback accepting the
actor pointer and unused second32-bit argument. Reuse the existing vector
prototype and globals; do not insert a duplicate declaration or alter an SDK
include. Keep the two actual local arrays in their retail order:

```c
void func_1506A968(u8 *actor, s32 arg1) {
    f32 position[3];
    f32 difference[3];

    position[0] = *(f32 *)(actor + 0x14);
    position[1] = *(f32 *)(actor + 0x18);
    position[2] = *(f32 *)(actor + 0x1C);
    difference[0] = *(f32 *)(D_800D1570 + 0) - *(f32 *)(D_800D1560 + 0);
    difference[1] = *(f32 *)(D_800D1570 + 4) - *(f32 *)(D_800D1560 + 4);
    difference[2] = *(f32 *)(D_800D1570 + 8) - *(f32 *)(D_800D1560 + 8);
    func_151D3480(position, difference, NULL, 1, 0xFF, 1);
}
```

The actor coordinates are raw float-bit copies. Subtraction uses the existing
global vector order. Position resides at SP+0x2C; difference at SP+0x20; RA at
SP+0x1C; incoming arguments at SP+0x38/+0x3C. There are no fabricated locals,
volatile declarations, added validity gates or instruction guards.

The frozen mode0 routine func_1506A79C and this routine differ in exactly one
instruction: word35, the JAL delay slot, is `0x24070001` for kind1 instead of
`0x00003825` for kind0. This observation selects the callback kind; it does
not replace compiling and comparing the complete mode1 routine.

All96 real source/profile forms are measured. Exact forms are plain
`order0-position-qualifier0-o2g3` and the unused-argument qualifier control
`order0-position-qualifier2-o2g3`. Select the plain form. Every profile has
frame0x38, decoded from its unique actual negative SP adjustment, not an
assumed first instruction. Plain O2 without g3 emits39 words; O1 emits56.
Swapping the two actual arrays preserves length but changes eight words and
has effective private-alias and own-fault negative controls.

## Qualified Gates

The new54-line candidate and55-line target test reuse the existing vector
compiler and qualification suite. Extend that suite only with target metadata,
baseline pins, dynamic entry defaults, kind-aware negatives/native assertions
and callback-table selection. The mode1 test binds its source module for the
class lifetime and always restores it through class cleanup.

Fresh pre-install target suite: **13 tests pass35.571s**. A same-process run
then executes mode1 shape, nine mode0 regression gates and two protected text
gates: **12 tests pass31.445s**. This verifies restoration of the temporary
binding and the shared helper's unchanged mode0 behavior.

Fresh installed suite: **17 tests pass37.209s**. This includes all13 target
gates, two protected text gates and both prior descriptor/mode0 shape checks.
The strengthened byte-accounting control subsequently passes1 check in1.662s.
Both tools copies pass ROM-free project checks and Windows byte-compilation.

- **11,904 guest cases**: all12^3 raw actor triples, finite bounded16x16
  subtraction pairs per axis, three provider behaviors and two SP phases.
  Independent reference values, full modeled state, ordered public accesses,
  call packets and complete40-word coverage agree.
- **60 alias cases**: actor/global overlap, both private vectors and incoming
  homes; aliased global symbols use independently assembled/relinked original
  and emitted routines. Retain retail's actual load/store schedule.
- **72 missing-byte prefixes**: every required actor/global float byte at both
  SP phases faults before the helper; no null-actor gate is invented.
- **Six effective semantic controls**: wrong coordinate, reversed subtraction,
  addition, swapped vectors, wrong callback kind and wrong slot. All fail both
  guest and native qualification.
- **20,736 native32 cases per profile**, O2 and O0: raw actor bits, precomputed
  bounded RNE subtraction grid, four public alias arrangements, three provider
  behaviors and every input canary. Keep warning gates, SSE/RNE, stack
  realignment and no-strict-aliasing flags.
- **15 owner neighbors**, normalized pools and relative relocations remain
  fixed. Both complete owner padders agree and preserve the direct target.
- **24 connected cases** execute the original38-word dispatcher and target.
  Its complete frozen41-word slot includes three alignment noops. Verify real
  table index7 at VA0x8008612C /ROM0x22ABEC, forwarded arguments and original
  global-vector initialization. The564-word downstream provider is a bounded
  hook, not emulated or claimed qualified here.
- **Three independent carry-boundary links**,72 semantic cases, retain complete
  words, actual HI/LO carries, JAL encoding and modeled states.
- **792 fired own-access pairs** across36 domains: all22 encoded accesses,
  both SP phases, three provider modes and six actor placements. Provider
  accesses are not counted as root accesses. Wrong-array-order cut8 is an
  effective negative; compare full prefix state and the dispatched word.
- Effective source, guard, ELF header/target/tail, prior mask, mode0 neighbor,
  prior descriptor and target symbol-name/size corruptions remain rejected.

Native proof is the bounded32-bit SSE domain, not arbitrary host/compiler
behavior. Raw copied NaN bits do not qualify NaN arithmetic. Private guest
aliases and fault prefixes establish emitted instruction order, not portable C
fault semantics, complete hardware FCSR, other rounding modes or hardware PC/BD.

## Closed Linked Audit

Before advancing any protected pin, three fresh linked-image/corruption checks
pass3.243s. Complete image equality permits only the160-byte target slot and
the exact named size change12 ->160. No metadata or section is excluded.
Exactly **124 bytes change:123 instruction bytes and one symbol-size byte**.
Every other ELF byte, named definition, layout, pool, neighbor, profile,
guard-history byte and conversion row remains fixed.

All189,088 protected Game data bytes across720 owners remain byte-exact, SHA
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

| Installed Input | SHA-256 |
| --- | --- |
| Source | `c84410d77e5e56f893997cd7de2b1ee15a6be993dc7434dafd7ee264bedffb65` |
| ELF | `9ba0f2793d2c40711359d86135f7408814827df987aae711c5dc153922ec9772` |
| Guards, unchanged | `8b3792e3d9fe28cc2aec346ee217edc66cf5e5f7190f88193c3213183a5f3661` |
| Conversion CSV, unchanged | `14d100143c0654609b3cd7d97798dbeccd52551a77ad6b4ff1f826acde91482b` |

Fresh Game **2,831/4,823 (58.70%)**, total **3,504/5,496 (63.76%)**,
different **1,992**, address drift **0**. Converted totals/bytes stay unchanged
because the false-C placeholder was already counted. Root README changes only
the two aggregate matching rows. The pre-existing generated_12D630 duplicate
recipe warning remains; no new target diagnostics, ROM or host build/launch.

Validate all nine protected text snapshots against their manifest before
archiving them and the manifest to `actor-vector-mode1-before-rebase/`. Only
then advance the independently qualified ELF snapshot and its one pin in both
tools copies. All other protected inputs and corruption controls remain fixed.

## Banking And Next Work

Tools `7f557cd8ab1951e280f8dbe061a0af04acc001d1` banks the two new files,
two scoped shared helper changes and verified text ELF pin first. The consumer
records that exact revision. The older mirror retains HEAD ddbdd16 and452 of
455 initial fingerprints: only the two shared vector files and verified text
pin change, plus two absent byte-identical files, bringing its dirty count
to457. No older-mirror commit, reset, dependency installation or push.

Direct Graphify update refuses18,839 proposed nodes versus40,617 retained,
preserving19,398 nodes from2,972 excluded-but-existing files. The existing
skill0.9.20/package0.9.26 and zero-node devcontainer warnings remain explicit.
Do not force shrink or install a different package. Record the incremental
hook and consumer post-bank receipts below.

Next `func_1506A5F0`: VA0x1506A5F0..0x1506A6FC, ROM0x97AA0..0x97BAC,
67 words /268 bytes, frame0x78, table index0. It is the remaining zero-return
placeholder in this owner. Recover its SP+0x1C mixed short/float/byte packet,
untouched padding and six global coefficients D_80099A10..D_80099A24, then the
four-slot call to func_151A6F00(packet,1,255,1). Its precise aggregate layout
and downstream read boundary still need investigation; do not infer them only
from the highest written field. This next body remains unmodified.

Reproduce from the prepared consumer under WSL:

```sh
python3 -m tools.experiments.game_actor_vector_mode1_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_vector_mode1_match \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_05_production_and_protected_data_unchanged \
  tools.tests.test_game_text_measurer_recovery.GameTextMeasurerRecoveryTests.test_06_effective_immutable_production_controls \
  tools.tests.test_game_actor_descriptor_spawn_match.GameActorDescriptorSpawnMatchTests.test_01_complete_direct_slot_two_screens_and_real_local_order \
  tools.tests.test_game_actor_vector_snapshot_match.GameActorVectorSnapshotMatchTests.test_01_complete_direct_words_profiles_and_real_frame_measurement -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
