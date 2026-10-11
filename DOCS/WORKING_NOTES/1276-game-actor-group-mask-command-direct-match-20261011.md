# Game Actor Group Mask Command Direct Match

Date: 2026-10-11. Recover complete func_1503DE70 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503DE70..0x1503DF0C, ROM 0x6B320..0x6B3BC: 39 words / 156 bytes.
All 39 retail words now emit directly from semantic C, with no word guards,
instruction drops, profile changes or handwritten assembly. Matching +1;
conversion counts unchanged. Keep the full Game matching goal active.

## Baseline And Interface

Consumer cf10ccbd8cb97497755869e8be004cce3a46e852 and mounted tools
36adf10b4be3a9887b11b9d5ace57d9f64d4a2f2 were clean at entry.
[Note 1275](1275-game-third-resource-loader-exit-scheduling-and-drop-removal-20261011.md)
left this as the next genuine unmatched body, not another already-exact
neighbor. Query native Graphify, inspect all 39 retail words, current owner
and actual caller source, then reuse existing IDO, ELF/CSV/pool parsers,
MIPS oracle, native32 runner, assembly processor and both real padders.
Zero Claude calls; local measurements resolve this routine directly.

Recover void func_1503DE70(struct127 *actor, s32 group, s32 entry).
Retail neither establishes a return status nor consumes the helper's V0.
All three current C callers ignore that register:

- func_1507DB44 forwards the incoming actor/group with entry -1.
- func_150772E8 reads D_800D154C / unsigned D_800D1890 and submits entry -1.
- func_1507A270 reads those globals and sign-extends D_800D1891 to s8.

Derive the signed slot by subtracting the actor-table address and dividing by
sizeof(struct127), 0x32C, with truncation toward zero. For entry != -1, read
D_8008446C[group], then both words of its eight-byte mask pair before calling
func_1503DF0C(slot, group, first, second). For -1, bypass the table entirely
and submit two all-bit masks. Preserve the full group/entry/slot words and
existing 32-bit guest address casts; add no bounds, pointer or mask gates.
Mapped invalid guest arguments do not establish portable C behavior.

The unchanged actual 15-word helper ORs both existing record masks, stores
the low group byte at +0xE and marker two at +0xF. Both existing mask words
are loaded before either store. Wrapper mask pairs may alias those fields or
their neighbor; both incoming masks must already be captured before writes.

## Direct Source Shape

The initial flat word-index expressions compile to 39 words / six differences:
one temporary-allocation cycle, not a semantic or length defect. Expressing
each table element as s32 (*)[2] recovers the eight-byte pair shape and all
39 words directly under both the production O2/g3 profile and the no-unroll
diagnostic profile. Equivalent byte-pair/byte-word diagnostics also match.
A local pair pointer gives 39 / 14; the flat pointer-difference form stays
39 / 6. Fourteen initial shape/profile measurements, no broad conversion batch.
No alternative profile or volatile experiment is installed.

The measured frame 0x18, RA +0x14, incoming actor/entry homes +0x18/+0x20,
signed divisions, both branch exits and second-mask call-delay load all emit
directly. Add only the compatible local void helper prototype before its use.
No caller, shared header, global declaration/type, recipe, layout, guard,
retail assembly or preserved GLOBAL_ASM body is changed.

## Fresh Qualification

New tools: experiments/game_actor_group_mask_candidates.py and
tests/test_game_actor_group_mask_match.py. Immutable inputs, sources, objects
and receipts are ignored under conker/build/game-actor-group-mask-match-test/.

- Ten pre-install tests pass in 12.561 seconds. Ten installed tests pass in
  12.128 seconds; add strict literal-audit controls and pass eleven in 16.776
  seconds. Refine one source-corruption control to work in either installation
  state and rerun that affected test: one passes in 1.857 seconds. Production
  candidate/source fingerprints do not change during these test refinements.
- The 2,160-case full-word guest matrix compares retail/raw/padded forms and
  reaches all 39 wrapper and 15 actual helper words. Include signed stride
  boundaries, negative deltas, extreme words, groups above byte range and
  entries other than the sole -1 sentinel. Invalid values are mapped fixtures.
- Seventy-two sentinel/alias cases preserve both live mask loads and actual
  helper access order, including pair offsets +4/+8/+12 into the destination.
  Sentinel tests have no group-pointer mapping and perform no table read.
- Three independently linked HI16/LO16/call placements pass 72 guest cases
  with a hook that clobbers caller-saved GPRs. Actual helper execution is
  independently qualified at its retail address, not claimed for those hooks.
- All 112 actually fired original/raw/padded fault-prefix comparison pairs
  agree on registers, LO, events and memory, including private frame accesses.
  This is guest instruction-order evidence, not portable C fault semantics.
- Four fresh semantic mutations fail effectively: wrong actor stride,
  wrong sentinel comparison, wrong second mask and wrong all-bit mask.
- Two source, three instruction/neighbor/extent, one guard and two stale
  installer corruptions are rejected by effective controls. No production
  inputs are mutated, historical baselines refreshed or audit exceptions added.
- Native32 O2/O0 each pass 196,608 valid-fixture cases and nine aliases,
  exercising all unsigned group-byte / signed entry-byte combinations and
  all 26 actor slots, with actual helper C and complete record-array checks.
  A second-mask mutation fails. No invalid-native-pointer, exhaustive full
  word-domain, portable64, emulator, hardware or gameplay claim.
- Freshly compile all three actual caller C bodies: all 8/12/13 words match
  retail and current linked bodies. The complete 324-case caller chain runs
  retail/raw wrapper plus actual helper with both hooks removed, reaches all
  33 caller, 39 wrapper and 15 helper words, and preserves signed byte input.
- Both complete copied owners compile without warnings, preserve all 21
  neighbors and normalized pools, then pass both real padding routes.
  This owner includes GLOBAL_ASM func_1503E5F8: perform the actual production
  post-processing step before padding. The initial missing-function padder
  failure was a harness omission, corrected without a production change.
  Cache the unchanged isolated padded link; the first uncached sweep was
  intentionally interrupted, not counted as a passing test receipt.

```sh
python3 -m tools.experiments.game_actor_group_mask_candidates --profiles
python3 -m unittest tools.tests.test_game_actor_group_mask_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

## Literal Audit And Checkpoint

The full rebuild exits zero. Exactly 127 ELF bytes change: 126 inside this
156-byte slot and one function-size byte, from 12 to 156. Every other ELF
byte, function body/address/extent, symbol name/value and metadata entry is
unchanged. No normalization/projection exceptions. All seven other assignment
inputs are literal exact: guards, conversion CSV, rodata assembly, symbols,
undefined functions, layout and Makefile. Protected data: 189,088 bytes /
720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | ba7ca1c269efca89aa7fd0b81d13403e032927a1d4e67f8238df80e72435a03f |
| Source after | b8430ca27296d5711b518bc5610a56e48618d16cd4285c2bf15418b16ebd67dc |
| ELF before | 9f2c45ce2994dafadbaa9bce9c640e61852b6f2ebf4d2a34a41d1d1438bbcb25 |
| ELF after | 43c9d060b98cb1f8662d6d8e34f84eb9497cf0dfc4be19843595a03a422fac2f |
| Guards unchanged | 2c86d53acedfcb94ac1e3fcd03bab86a3b0854c6813f07dfb080f415b26255a7 |

Fresh match-progress: Game 2,797/4,822 (58.00%), total 3,470/5,495 (63.15%),
Init 492/492 and Debugger 181/181. Zero drift, 2,025 still different. Matching
+1 only; conversion counts/bytes unchanged. Root README changes only its
two aggregate matching rows; function narrative remains here and in indexes.

Consumer, mounted and older tools shared checks pass. Both new paths pass
native py_compile. Bank mounted tools 3b4d8ecc89567eddf33a5edf3141dedbf055c553
first, then source, this note, five concise indexes, aggregate README and
consumer gitlink. Older sibling HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a
and all 43 recorded fingerprints stay unchanged. Copy only two absent paths
with identical hashes: dirty count 320 -> 322. Do not commit/reset/push that
independently dirty history. Function qualification ran in the mounted
consumer, not standalone. Keep both active checkouts committed; no push.

Native graphify update . exits one on protective shrink refusal: 18,124
candidate nodes versus 39,904 saved. It preserves 19,398 nodes from 2,972
excluded-but-existing files; no force, purge or install. Version/empty-source
warnings remain separate from compiler diagnostics. The unchanged duplicate
generated_12D630 Makefile recipe warning remains. After consumer commit,
verify fresh hook terminal Rebuilt plus advanced log bytes/UTC and zero
workers, not merely the background launch.

## Next Game Body

Live linked recheck: this wrapper 39 / zero differences, helper 15 / zero.
Skip that already-exact helper. Next func_1503DF48 remains a placeholder with
171 words / 168 linked differences: VA 0x1503DF48..0x1503E1F4,
ROM 0x6B3F8..0x6B6A4, same generated_6B320 owner. Recover its complete
record-state dispatcher and callee interfaces before installing another body.
Its full remaining behavior is not qualified by this wrapper's tests.

Keep the third-loader's two final scheduling guards, parent/pair guard removal
and deeper SDK/allocator/heap/hardware/renderer/gameplay as separate open work.
No OGL Release build/change, real save or private-input mutation, or active
editor/debugger change. No unbounded completion claim: full Game goal active.
