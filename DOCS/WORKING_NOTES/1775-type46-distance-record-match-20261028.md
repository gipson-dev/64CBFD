# 1775 - Type-0x46 Distance Record Match - 2026-10-28

The adopted Native ELF measures **3,853/5,506 exact C functions (69.98%)**,
Game **3,180/4,833 (65.80%)**, zero address drift and 1,653 different.
Only func_150C5370 gains credit. The 75% threshold remains 4,130, requiring
**277 more** exact C functions.

## Recovered routine and interface

Function func_150C5370 in generated_F2820.c occupies VA
0x150C5370..0x150C5430, ROM 0xF2820..0xF28E0: 48 retail words and a
48-byte frame. Its interface returns Type46DistanceRecord* and accepts a
const Type46DistancePayload* plus u32 extraBytes. Shared headers stay fixed.

The 36-byte payload contains two three-float positions followed by twelve
opaque attribute bytes. The caller sets byte flags among those attributes;
they are not nine floating-point values. The record embeds this payload at
+0x18, has active/state words at +0x10/+0x14, a distance float at +0xC0,
and totals 0xC8 bytes. Local names describe the recovered accesses.

Call func_15167A68(0x46,0,wrapped extraBytes+0xC8,1,0xFF,1), returning NULL
on failure. Success copies all 36 payload bytes, subtracts corresponding
coordinates from the copied record, calls func_15143E64 with the three
stack deltas, writes the returned distance and words 1/0, and returns the
allocation. Size arithmetic wraps explicitly before conversion to s32;
tests do not claim the real heap accepts every wrapped request.

| Call offset | Symbol | Purpose |
| --- | --- | --- |
| +48 | func_15167A68 | Type-0x46 allocation and initialization |
| +84 | memcpy | Copy the complete payload |
| +144 | func_15143E64 | Three-component length |

## Narrow instruction normalization

The normal O2/g3 compiler emits 47 words. Twenty-five private source-shape
screens did not remove the remaining layout difference. Eight expected-word
and relocation-checked rows derive the closed transformation:

- +64 increments the failure branch displacement for the inserted word.
- +96/+100/+104 rotate two independent loads ahead of the stack-address setup.
- +152/+160/+164/+168 rename the saved result pointer from V0 to V1.
- The +168 row inserts move V0,V1 after the stores, shifting the unchanged
  four-word epilogue and producing the proper 192-byte symbol extent.

All three J26 bindings retain their symbols and offsets. No whole-body
replacement or shared padder change is used. Existing guard CSV bytes are
preserved exactly, with eight rows appended. The raw compiler C passes
memory, return and call equivalence independently of these guards; only
the normalized form claims complete register/PC/fault-prefix agreement.

## Original caller and retained helpers

The complete ROM census finds one direct site: VA 0x1514D604 /ROM 0x17AAB4,
in func_1514D564 (generated_179F30), and no pointer literals. The current
parent remains an unchanged zero-return placeholder and receives no credit.

Tests execute all 58 original parent words across 24 cases. The original
setup builds a stack payload using retained constants and actor positions,
passes twenty extra bytes, tests failure, copies the complete extension to
result+0xC8, calls func_1514EC1C(result,actor,0x15), and reaches the final
return. Original attribute and extension padding bytes are preserved.

The factory (28 words), list initializer (20), memcpy (11), and vector length
(12) are all already exact against ROM. All 71 retained words execute in
24 connected cases with both empty and existing list heads. The raw C and
normalized target also run inside that actual chain and parent. Only the
heap allocation and final event provider remain bounded. Finite single-
precision cases validate the real sqrt.s sequence. No gameplay, full parent
C, arbitrary host overlap, or hardware FCSR acceptance is claimed.

## Qualification and image

Both tools copies pass eight fresh canonical methods and shared tools checks.
Production reruns two installed methods per copy and reuses six semantic
methods only after exact module, input and artifact fingerprint comparison.

- 1,042 guest cases cover unsigned size boundaries, NULL/success, opaque
  float bits, provider changes to input homes and saved record pointers,
  and 18 record/input/stack overlaps. All 48 retail words execute.
- Native32 O0/O2/O3 each pass 16,384 cases, four effective wrong-C controls,
  trapped UBSan, actual pointer ABI/layout assertions and complete record
  fences. Native allocation/copy/length providers remain bounded.
- 420 fired access-prefix pairs agree in full state, ordered traces, PC and
  delay context. Unmapped data verifies allocation failure skips input reads.
- Three real GNU layouts pass 48 guest cases, preserving all J26 targets.
  Sixteen stale-word/relocation guard controls, three raw-body/binding
  controls, four actually compiled IDO semantic controls and six complete-
  image corruption controls all reject changed behavior or evidence.

The complete fifteen-function owner preserves fourteen neighbors, pools and
bindings. Its actual three-command Make recipe has zero compiler diagnostics.
The inherited generated_12D630 duplicate-recipe warning is unchanged.
Production reproduces an independent strict prediction of **145 changed
bytes**: 144 target-code bytes and one symbol-size byte (12 to 192), with
zero exclusions. All 6,056 addresses, 6,055 other linked bodies, named ELF
definitions, section geometry, map and C inventory stay fixed. All 720 Game
data owners /189,088 bytes remain exact.

## Bank and continuation

Predecessor consumer 77d02002 and tools df938bc1. Tools are committed first
as 1e78e1a68e2429de22a848b4a9cdf4c1076c07fc. The seal verifies 16,316 files
and 316 focused inputs. Preserve all 1,766 inherited dirty paths in the
older independent tools mirror, adding only three target modules there.
No mirror commit or push. The host Release remains frozen.

| Artifact | SHA-256 |
| --- | --- |
| Adopted ELF | 4864adb61bffe5db611326f30fbfbeb58ffeb48181776576ee3f430bc86fe712 |
| Padded owner | 36655f667de0fe26cb634da6256488129543ce331067cca7bd0f43c48bfc8636 |
| Recovered source | 2111c2ddbf671d33f0d10da50bf7aa2fc6e6dd6c6979da9dcfc7f1d083d72b90 |
| Raw compiler body | b8563717a8415ce49f3da1b428262c960ba486965bba16c1d0643d79bfec6f0b |
| Normalized/original raw body | a29e54256512b8e35e0cc03c4ba8522098e08c667abf3b5ab5377eeb213a4210 |
| Complete retail body | 21997deab3c52015d274c17374428641b94d4d866b248e7e6fec914a3d596f6c |
| Appended guard CSV | de278c88aaf2aba65667bd3422814c947b7da4db616b190b388450c185486278 |

Scoped Graphify closeout refreshes eleven changed C/Markdown/tool sources.
Retain the 46,097 prior nodes and validate old relationship contexts,
retiring only the obsolete placeholder return type with source evidence.
Validate the recovered pointer return, two parameters and three helper calls;
record original caller evidence without inventing a current parent call edge.
Preserve outside-scope manifest freshness and historical communities; this
is not full-corpus re-extraction.

Next inspect the 48-word func_15107A20. The queue contains 1,524 placeholders,
120 semantic/other entries and nine unlocated screens, for triage only.
Keep func_1514E920 parked and uncredited and the 75% goal active. Routine
Claude calls: zero.

Prepared-checkout command: python3 -m unittest tools.tests.test_game_type46_distance_record_match -v.
