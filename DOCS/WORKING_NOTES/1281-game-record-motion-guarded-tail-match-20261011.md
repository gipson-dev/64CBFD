# Game Record Motion Guarded Tail Match

Date: 2026-10-11. Recover complete func_1503EA54 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503EA54..0x1503EB78, ROM 0x6BF04..0x6C028: 73-word / 292-byte slot.
All 71 reachable words emit directly under the existing O2/g3 profile.
One expected-word insertion retains retail's unreachable second jr ra;
ordinary slot padding supplies its delay NOP. All 73 linked words match.
This is guarded-exact, not a full direct C match. No executed-word changes,
instruction drops, frame, calls, header or compiler-recipe changes.
Matching +1 only; conversion counts/bytes unchanged. Full Game goal active.

## Baseline And Contract

Consumer 62e7144bbf67db4d30933a24c5a496d85ac0eedc and mounted tools
73745f6e54cf7352c9e2e99e5df5b62dc6e12fea were committed at entry.
[Note 1280](1280-game-record-matrix-update-direct-match-20261011.md)
left this genuine 73-word / 71-difference target. Inspect the complete retail
body, known 171-word dispatcher caller, actual structures and owner profile
after a scoped Graphify query. Reuse IDO, structured ELF/object/pool/CSV
parsers, MIPS/native32 fixtures, post-processing and both production padders.
Codex is the single writer; zero Claude calls, no bridge or installs.

Recover void func_1503EA54(s32 slot). The known caller ignores V0; retail
has no separate status calculation and happens to retain count in V0. Only
the forward declaration changes; the dispatcher body stays unchanged.
Keep the existing 16-byte control and 104-byte record types, using local
float views where shared struct04 declares halfwords at +0x24/+0x28.

- Read initial unsigned group +0xE and unsigned count D_80098914[group].
  Cache count and the signed 32-bit D_800BE9E4 timestep converted once to
  single precision. The conversion executes even when count is zero.
- Scan 0..count-1, reloading the live record buffer each iteration. Zero
  flag +0x64 skips all type/data accesses. Otherwise read the live group
  and signed D_80084454[group][index]; only -1 integrates.
- Keep this iteration's record address across its updates. Advance float
  fields 9..14 (position/rotation +0x24..+0x38) by fields 18..23
  (rates +0x48..+0x5C) times the cached step, with separately rounded multiply
  and add. Then update vertical rate field19/+0x4C by field24/+0x60 * step.
  Position uses the old vertical rate, not the accelerated value.
- Full-word float views preserve payload width; no halfword truncation,
  integer-to-float interpretation of record words, double accumulation or
  extra half-acceleration term. Scale and flag fields remain unchanged.
- Record writes may overlap control pointer/group, count table or timestep
  in explicit guest fixtures. Buffer/group remain live on later iterations;
  count and converted timestep stay cached. These are not portable C aliases.

## Source And Unreachable Tail

Initial source with an element pointer before the flag gate emits 174 words
under O2/g3 because IDO unrolls the leaf loop. Move the element assignment
inside the active gate, inline deterministic control addressing and initialize
count before step: all first 71 retail words now emit exactly, with the
original load/store schedule, branch-likely updates and no stack accesses.
The compact diagnostic emits the identical prefix; O1 variants do not match.
No profile override, volatile forcing, dummy locals or dead source statements.

Retail adds a second return pair at +0x11C/+0x120 after the actual shared
return at +0x114/+0x118. No path reaches that extra pair. Bounded alternate
count guards, explicit returns, scalar/pointer views and offset forms do not
recover it directly. Keep this limitation explicit rather than claim 73-word
direct C or add source with an invented purpose.

Append precisely one existing-protocol guard row for generated_6B320:

| Offset | Expected / Replacement | Insertion |
| --- | --- | --- |
| +0x118 | 00000000 / 00000000, real return delay NOP | 03E00008, unreachable jr ra at +0x11C |

All relocation lists are empty. Padding supplies +0x120's NOP. Raw function
extent is 284 bytes; guarded emitted extent is 288, within the 292-byte slot.
Preserve the complete old guard byte prefix, including mixed line endings.
This follows the established duplicate-return insertion used in
[Note 720](720-game-sentinel-coordinate-distance-match-20261002.md), without
copying that routine's executed-word normalizations. Direct tail recovery
remains open. Missing-tail byte checks and stale expected words fail.

## Fresh Qualification

New tools: experiments/game_record_motion_candidates.py and
tests/test_game_record_motion_match.py. Immutable before-inputs and receipts:
conker/build/game-record-motion-match-test/.

- Twelve complete pre-install tests pass in 24.064 seconds. All twelve
  installed tests pass in 25.039 seconds. A final two-test literal-audit and
  integrity-control rerun passes in 5.854 seconds after documentation edits;
  all 4,383 relative links across seven checkpoint docs pass. Prior unchanged neighbor-suite
  receipts remain historical, not described as freshly rerun.
- The 380-case retail/raw/guarded matrix reaches all 71 executable words,
  never the dead tail. Counts 0/1/3/4/5/27/31/45/128/255, flags, signed types,
  groups, stack phases, negative/positive/zero steps, signed 32-bit extremes
  and values around 2^24 are covered. Invalid slots are mapped guest-only.
- Eight effective self-alias cases change the public buffer, group, count
  or timestep during record stores. Pointer/group reload and cached count/
  step distinguish the expected later iterations; no callback or native-alias
  claim is substituted for this emitted-instruction evidence.
- Two independently linked placements rebase four symbols with HI16/LO16
  carries in 24 cases. Raw prefixes and guarded slots retain exact addresses.
  All 41 fired fault triplets preserve memory/events/GPR/FPR state. The dead
  tail is never exercised by these paths; fault tests are not portable C
  fault semantics or hardware/FCSR proof.
- Six freshly compiled controls fail on public effects: wrong type, wrong
  flag, zero step, missing acceleration, cached buffer and live count. The
  unguarded padded slot fails the tail-byte check; a stale expected NOP is
  rejected. Stale/duplicate installs, duplicate guard successors and source/
  target/dead-tail/neighbor/extent/old-guard corruption fail effectively,
  without production mutation or baseline refresh.
- Both copied complete owners pass GLOBAL_ASM post-processing and both real
  padders. All 21 neighbors, pools, other slots/relocations, dispatcher171,
  setup141, matrix138 and assembly decomposer141 remain unchanged.
- Thirty-eight boundary cases leave unused tables/buffers unmapped for
  count-zero/flag-zero paths and cover signed zero, subnormal and overflow.
  Finite results compare to the ordered float reference. Infinity/NaN compare
  emitted forms only; no hardware NaN propagation or FCSR parity is claimed.
- Native32 O2 and O0 each pass 36,864 cases, covering every count 0..255,
  eight signed steps, three slots, type patterns and flags. Check all 26
  words of all 256 records, including skipped/unused bytes. Three controls
  fail with actual mismatch receipts. No native alias or dead-tail claim.
- Forty-eight cases execute the actual dispatcher171/setup141/predicate27/
  motion73/matrix138 chain against an independent composed reference, with
  states 1/2/3, counts 0/1/3/4, phases and negative/positive timesteps.
  Other SDK/callback boundaries remain models, not full gameplay acceptance.

Pre-install fixture fixes used the named word_patches_path API, separated
the target-only manifest from full owner history, and corrected a Path/string
expression. No production workaround, old-prefix normalization, broad source
conversion or metadata exception was used to pass qualification.

```sh
python3 -m tools.experiments.game_record_motion_candidates --profiles
python3 -m unittest tools.tests.test_game_record_motion_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Linked Audit

The manifest timestamp triggers the existing wider dependency rebuild, not
a broad source-conversion batch. It exits zero with existing source warnings
and the duplicate generated_12D630 recipe warning. Copied target owners are
diagnostic-free. Literal whole-ELF comparison changes exactly 226 bytes:
224 target-slot bytes and two size bytes, 12 -> 288. Every other byte, body,
address, extent and metadata entry remains exact; no projection/permutation.
Guard history is the original byte prefix plus only the checked insertion.
Six other inputs remain exact: progress CSV, rodata assembly, symbols,
undefined functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | d6392a89c3f3d6b935549e56ab00c0f737b51e21a6e451ff32f6d483fe4916c2 |
| Source after | e367e9c05a6fbdd714f4ea53cb88939e32a50361fb08640f67d403d5593f3d41 |
| ELF before | d0111ec67ddfe4c6b836061caaa483457e2d38ee6b582a087d45b2d5397672cd |
| ELF after | acd55ef04121c1aad24f275cdb53e7a313d3f8608317ce381b09c200105cd666 |
| Guards before | 75a00e8d566bd1f737d2d4bd2bbbc5c01eb7ec6c33f9789a422b5aa73bc1d5ed |
| Guards after | 50d69274e599b51d2cebee2e9942b09fad6a7c75f7d91a56f2666c6d823a872b |

Fresh progress: Game 2,802/4,822 (58.11%), total 3,475/5,495 (63.24%),
Init 492/492 and Debugger 181/181. Zero drift / 2,020 still different.
Matching +1 only; root README gets aggregate rows, no recovery narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools 6f16f59 first, then source/guard, note, five current indexes,
aggregate README and exact consumer gitlink. No push. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 53 recorded fingerprints
stay unchanged. Only two absent paths are copied with identical hashes;
dirty count 330 -> 332. Do not commit/reset its independent dirty history.
The target suite runs in the mounted consumer, not the standalone mirror.

Native graphify update . exits one on protective shrink refusal: 18,170
candidate nodes versus 39,949 saved. Preserve 19,398 nodes from 2,972 excluded
but still existing files; no force/purge/install. Version/empty-source warnings
are separate from compiler diagnostics. After consumer commit require fresh
terminal Rebuilt, advanced log bytes/UTC
and zero workers, not merely a launch message. Precommit log: 536,406 bytes.

Fresh live recheck: motion73/zero linked differences. Next genuine placeholder
is func_1503EB78, 74 words / 72 differences, VA 0x1503EB78..0x1503ECA0,
ROM 0x6C028..0x6C150, same owner. Inspect its complete four-argument body
and caller contract before recovery. This dead-tail guard,
earlier guards, remaining callees and deeper hardware/FCSR/renderer/gameplay
acceptance stay separate and open. No OGL Release change/build, private input/
save or active editor/debugger mutation. Keep the full Game goal active.
