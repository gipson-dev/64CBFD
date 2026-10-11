# Animation State Allocation Direct Match

Verified 2026-10-11. Consumer baseline
df648e82593885bacd81f2a7b9be18ff424cc811; mounted tools baseline
83ade717bd246c6a2087055d73d8064c3a485399. New tools
ed89891ded9155b6a743cdd231fb887b0f775279 committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
Previous goal turn made progress by banking the complete resource initializer.
This checkpoint finishes the next complete helper, not the wider Game goal.

## Complete Recovery And Direct Match

Recover func_150838EC, VA 0x150838EC..0x150839B8,
ROM 0xB0D9C..0xB0E68. All 51 words / 204 bytes emit directly from semantic
C with original 0x28 frame, seven relocations and no new guards or pools.
The old leaf zero-return placeholder had a 12-byte ELF symbol extent.
Signature: s32 (u8 *actor, s32 state, s32 mode, f32 scale).
Four complete retail call sites were inspected: two in AEB40.s, one in
58F80.s and one in 1C1150.s. The 58F80 caller uses the failure return;
do not recover this helper as void or an unconditional zero return.

- Save all four full incoming O32 words to their original argument homes.
  Actor identity is actor[4], a byte with no special 255 sentinel here.
- Zero D_800D1588[identity] returns zero without reading the count table;
  otherwise zero unsigned D_800C5A90[identity] also returns zero.
- Allocate 0x3E0 bytes with arguments (size, 1, 2, 0). Reload the actor
  home after the callback and store the result at actor +0x2D0 before
  testing it. NULL is stored and returns one; it is not a silent early exit.
- Success reloads that field for bzero and clears only the first 0x40
  bytes, not the entire 0x3E0 allocation. Keep the cached post-allocation
  destination pointer through this load and the call.
- After bzero, reload mode, actor, the low unsigned halfword of state and
  the raw float word from their original homes. Delegate to func_1505E650
  with (actor, stateLow16, scale, 0.0f, 0.0f, 0.0f, mode), then return zero.
  Preserve the original outgoing stack writes and restore/return schedule.

The initial all-volatile experiment emitted 53 words and 18 differences.
The plain typed body recovers the original IDO O2/g3 home/reload shape and
all 51 words directly; no forced volatile arguments or scheduling recipe.
Replace the obsolete s32 no-argument declaration, remove the stale
unrecovered-helper comment and call with scale rather than *(u32 *)&scale.
Both before/after copied owners prove this typed constructor call has the
identical complete 182-word compiler fingerprint, extent and relocations.
No constructor guards are weakened, moved or regenerated.

## Fresh Qualification

Ten final tests pass after installation (28.682 seconds). Immutable baselines
and reproducible receipts are in conker/build/game-actor-animation-allocation-test/.
Consumer make tools-check and mounted standalone check_project_tools.py pass.

- 20,481 independent-reference cases / 40,962 complete original/C guest runs:
  all identity bytes, all four return paths, two stack phases, full-width
  state/mode boundaries and ten float words, including signed zero, infinity,
  subnormal and quiet/signaling-NaN payloads. Dynamically reach all 51 retail
  words. Explicit presence-zero case accepts an unmapped count table.
  Original GP/FPR preservation and clobbered callback registers qualify.
- 43 alias cases and 2,894 fired modeled full-access fault pairs / 5,788
  failed runs compare full partial memory, ordered access events and calls.
  Qualify callback-mutated actor/state/mode/scale homes, actor/private-buffer
  aliases, table aliases into homes/actor fields, cached gates after callback
  mutations, result store before NULL check and exact 64-byte modeled clear.
  Every injected access gate fires; the SDK bzero byte stores are a bounded
  callback model, not actual SDK instruction/fault-order acceptance.
- Four return-address-corruption pairs preserve the unsafe original outcome:
  at the second stack phase, a buffer clear overwrites saved RA and both
  bodies jump to zero. Full partial memory/events/calls match the independent
  reference; do not report these as successful normal returns or exclude them.
- Nine independent original/C/padded links at three symbol sets, 12 cases /
  36 runs: both table HI16/LO16 pairs and all three JAL sites rebased across
  signed low-half carry boundaries. Independently assembled retail, compiler
  output and actual isolated production padding are identical at every link.
- Actual production preprocessing/compilation/post-processing and full
  layout padding of before/after copied owners preserves all 30 neighbors'
  bytes, extents, relocations and normalized pools, with no diagnostics.
  Existing full constructor guards still apply unchanged; the direct
  68-word initializer is preserved.
- Nine freshly compiled effective IDO negatives distinguish presence/count
  gates, allocation size, failure return, destination field, clear length,
  state narrowing, float forwarding and final mode. The wrong clear length
  is rejected by the bounded bzero contract with an explicit diagnostic.
- A separate freshly compiled numeric-float-conversion constructor negative
  fails the unchanged manifest through actual pad_c_object.py: stale overflow
  expectation at func_15083AC8+0. A fresh additional generated-owner command,
  matching this owner's Makefile route, also rejects it: patched constructor
  0x2FC bytes versus original 0x2D8 span. No false bit-to-number conversion
  is installed or hidden behind a new guard recipe.
- 120 cases / 240 runs connect the actual complete 182-word constructor,
  68-word initializer and 70-word resource transition around original/C
  allocation helpers. Confirm 30 real animation delegations per form, full
  memory/events/calls/GP/FPR equality, all four gate/result paths and raw
  scale forwarding. Deep allocators, SDK and animation/resource callbacks
  remain bounded; their full bodies/lifetime/hardware behavior is not proven.
- Native32 O2/O0 each pass 16,384 independently modeled cases, 32,768 total,
  with full state/mode words, typed raw float-bit forwarding, failed/successful
  allocations and self/offset clear aliases. Width assertions verify 32-bit
  pointers/integers/floats. One native float-forwarding negative fails.
  Private homes and guest fault order remain guest-only qualifications;
  strict aliasing is disabled as in existing decomp harnesses. No hardware
  FCSR equivalence or real allocator acceptance is inferred.
- Whole linked audit below passes with unchanged guards/conversion rows.

Fixture corrections before the final run: remove synthetic call-argument
inspection reads from the independent guest trace; use each helper's declared
ROM span instead of an incorrect common-offset assumption; keep the native
Werror gate by splitting misleading loop lines; give the wrong-length bzero
control an explicit diagnostic; explicitly qualify the corrupted RA outcome.
These were harness issues, not recovery-source regressions.
Historical unchanged-neighbor and constructor-private receipts are reused
on freshly proved byte/fingerprint equality, not called fresh suite runs.

## Installation Audit

Only 148 ELF bytes change, confined to this 204-byte slot and its 12 -> 204
ST_SIZE update. All other ELF bytes and metadata remain identical, including
the constructor despite its cleaner typed source call.
ELF 3,261,160 bytes, SHA-256
3daba354e906875443a0321b5ed5f4a95602e266246f4c45fa955245bc8df353.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
New owner 11,602 bytes, SHA-256
c3e54e75a48cb02339180676682b2c51052f169c2bbaf663683fedcd73405128.

Guard manifest stays byte-identical at 1,940,850 bytes, SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Conversion CSV stays 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Rodata, symbols and ignored undefined assignments stay byte-identical.
Linked rebuild succeeds; duplicate generated_12D630 recipe warnings remain.
Root README gets two aggregate matching rows only.

Fresh Game matching 2,782/4,821 (57.71%), total 3,455/5,494 (62.89%),
zero drift / 2,039 different: +1 matching, no new converted credit. Total
converted remains 5,494/6,043 (90.92%); Init 492/492 and Debugger 181/181
already-converted functions remain exact.

```sh
python3 -m unittest tools.tests.test_game_actor_animation_allocation -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Older standalone tools HEAD ddbdd16 stays unchanged: 269 existing dirty
entries plus two absent-only byte-identical new mirrors = 271. Protected
older helper hashes remain exact; no old paths overwritten or committed.
Native Graphify query found 33 nodes, showed 22 and explicitly truncated 11.
Native update exits 1, refusing unsafe shrink 39,658 -> 17,876 nodes and
retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve
skill 0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no
force, purge or install. Require fresh post-commit log growth/Rebuilt tail
and zero actual workers before reporting clean. No OGL/Release, saves,
editor state, private inputs or broad conversion batch changed.

## Next

Recover complete 66-word func_150836CC in the same owner,
VA 0x150836CC..0x150837D4, ROM 0xB0B7C..0xB0C84, original frame 0x30.
Its current body still returns zero. Inspect callers, the opening
func_150302F0 callback before descriptor lookup, cached record base, live
unsigned descriptor count, record type-zero filter, nullable child lookup,
signed parent-slot division and +1 comparison against child +0x65, and
optional func_15060F28(child, 0). Reuse the eight-byte descriptor recovered
for func_15083568; preserve all completed neighbors and guard fingerprints.
Timeline matching and actual allocator/SDK/resource/hardware/renderer/gameplay
acceptance remain separate open work. Keep the wider Game goal active.
