# Game Owner Link Setup Guarded C Match

Continue from [Note 1172](1172-game-owner-link-setup-recovery-checkpoint-20261009.md)
and the exact allocator in [Note 1173](1173-game-owner-link-allocator-direct-match-20261009.md).
Start clean at parent e9308643/tools 3b7e4c1. One Codex writer, zero Claude
calls; use the scoped [agent workflow](../AGENT_WORKFLOW.md), complete semantic
candidates and independent qualification. Keep tools committed before the
consumer pin. No push; preserve the independently dirty older tools checkout.

## Installed Result

**func_151B2348 now matches all 210 retail words from semantic C plus 25
certified GPR-only guards.** This is a guarded match, not direct compiler output.
VA 151B2348..151B2690, ROM 1DF7F8..1DFB40, 840 bytes/frame 0xA8.
Replace its genuine GLOBAL_ASM in
[generated_1DF510.c](../../conker/src/game/generated_1DF510.c).
Keep the original [scoped fragment](../../conker/asm/nonmatchings/generated_1DF510/func_151B2348.s)
and [owner assembly](../../conker/asm/1DF510.s) intact.
func_151B2690 remains genuine 176-word assembly; exact allocator151B30B0
and all other production routines are unchanged.

Real declaration order recovers the private workspace without invented padding:
captured second, captured first, pair, grouped packet/request, then created.
The addressable incoming actor home is read after the first allocation:
pair = *(u8 **)&actor + 0x28. Retail retains pair in S2; the workspace is
packet SP34/request SP64, with saved S0/S1/S2/RA at20/24/28/2C and actor homeA8.
The copy expression reads the just-stored result field in C; IDO forwards that
value through V0 with no extra guest load. Do not simplify these lifetime-sensitive
forms without repeating the complete matching and provenance gates.

Raw existing O2/g3 emits 210 words/frame168, no diagnostics or literal pools,
and only25 T6/T7 operand differences. The
[matching driver](../../tools/experiments/game_owner_link_setup_matching.py)
keeps the selected complete body and four profiles:
O2/g3 210/168/25, O2 209/168/204, O1/g3 242/152/240, O1 242/152/240
(words/frame/differences). No production profile change.

## Recovered Contract

Capture second=actor+30 pointer before first=actor+28 pointer, once before helpers.
Build three48-byte endpoint packets using one reused56-byte request.
Route2 initially uses second/second, kinds5/10, vectorsAA350/35C and distance80.
Route1 uses first/second, kinds5/5, vectorsAA320/338 and distance170.
Route0 uses first/second, kinds5/10, vectorsAA32C/344 and retains distance170.
Capture endpoint codes and coordinates before each allocation. Reuse the initially
captured endpoint pointers even when helpers mutate actor pointer fields.

Request flags0/duration1000, active1/enabled1/extra0, width5/kind3/tail0;
limits come from D_800AA380/384 once. Call
func_151B30B0(&request,0.0015f,48,255,0), using the real mixed five-argument ABI.
Acquire pair only after the first allocation and retain it thereafter.
Unconditionally store results, including NULL, at pair+18/+14/+10
(actor40/3C/38). Conditionally copy48 bytes to created+150.
Do not reread the result slot after memcpy; fixtures deliberately mutate it.
Seven packet holes remain untouched and are copied from their original retail
stack addresses. Native fixtures qualify defined fields, not native padding parity.

## Guard Certificate

Append exactly25 expected-word rows to
[the manifest](../../conker/retail_word_patches.us.csv), preserving all11,510
old rows byte-for-byte. Regions64..A4,168..1E4,25C..2C0 are straight-line,
closed T6/T7 allocation permutations. The ROM-independent transformer changes
only GPR14/15 operand fields, not opcodes, constants, offsets, instruction order,
stack addresses, branch words, floats or ABI lifetimes.
It is an involution and rejects live-in/live-out corruption controls.

Two guarded words retain exactly the original D_800AA344 HI16/LO16 relocation
uses; all22 relocation uses agree. Expected-word/relocation checks fail closed
if emitted source changes. Guard generation uses the raw object and a certified
register permutation, not a literal table of retail replacements.

## Qualification

[Nine-test suite](../../tools/tests/test_game_owner_link_setup_match.py):

- Raw length/frame/25 differences and normalized210-word equality, no isolated
  warnings/pools, complete closed-region certificate and rejected boundary
  corruptions.
- 768 guest cases/2,304 executions of original/raw/normalized bodies: three
  seeds, four endpoint aliases, eight success masks, mutations, two stack phases,
  distinct or actor/endpoint-aliased result pointers. All210 words reached;
  full public/private memory, access events and calls are identical across forms.
  All seven copied raw packet holes retain the retail stack seed.
- 32,768 native32 executions of the actual selected body: all256 code bytes,
  four aliases, mutations, eight masks and result aliases. Independently check
  defined request/packet fields, captured codes, retained limits, endpoint
  mutations, typed call ABI, conditional copies/failed stores and canaries.
  No native padding or N64 hardware/FCSR proof.
- Five compiled effective negatives: wrong route, wrong distance, wrong endpoint
  code, omitted failed-allocation store and short copy. Each completes within
  the oracle domain and fails public output/call expectations.
- Copied owner runs actual asmprocessor before/after and the actual padder;
  preserve17 neighbors, pools and relative relocations. Four existing Warning712
  messages remain identical; zero new target warnings. Isolated and owner guards
  agree. The other helper remains real original assembly.
- Four independent symbol sets/12 links,64 cases/192 executions, including
  segment and low-half carry boundaries. Original/raw/normalized traces agree;
  normalized words and all22 relocation uses match original.
- 384 connected cases/768 executions across three setup forms with the actual
  exact53-word allocator wrapper. Check real wrapper requests and copied holes.
  Common allocator/SDK calls remain bounded hooks, not full integration proof.
- 32 missing-byte cases/96 executions; original/raw/normalized fault prefixes
  agree. Local StrictSetupOracle detects missing bytes without changing shared
  oracle behavior. This is emitted guest order, not portable C or hardware faults.
- Immutable pre-install whole-ELF/guard/conversion/protected-data audit.

The first pre-install run catches only a missing-byte fixture exception mismatch;
fix the local oracle, not shared helpers. Final pre-install suite passes23.518s.
**Installed suite passes all nine tests in25.020s, zero skips.**
The guard manifest is a broad build dependency; the production rebuild therefore
recompiles other owners and passes. Existing duplicate generated_12D630 recipes
and unrelated legacy compiler warnings remain; do not call the full build warning-free.

## Linked Audit And Progress

The **entire installed ELF is byte-for-byte identical** to its immutable
pre-install baseline: all loadable code/data, headers, symbols and metadata.
The audit permits verified symbol/string ordering, but actual hashes are identical.
Protected Game data189,088 bytes/720 owners is exact, zero differences.
No neighbor suite is reported as newly rerun; the whole-ELF identity and focused
copied-owner/connected checks establish the unchanged-evidence boundary.
Old whole-ELF receipts are historical; do not silently recapture their baselines.

Guard history changes only by the25 appended rows, totaling11,535.
Progress changes exactly one row: func_151B2348 language asm to c, all other
fields/rows unchanged. Unlike the earlier placeholder recoveries, this genuinely
adds one converted function and840 converted bytes.

Fresh build/progress.csv and match-progress NON_MATCHING=1 pass.
Recompute conversion counts/bytes independently from fresh us rows, excluding
repeated headers:

| Section | Converted Functions | Converted Bytes | Byte-exact C | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,488/6,042 (90.83%) | 85.95% | 3,412/5,488 (62.17%) | 0 | 2,076 |
| Init | 492/539 (91.28%) | 92.53% | 492/492 (100%) | 0 | 0 |
| Game | 4,815/5,321 (90.49%) | 85.30% | 2,739/4,815 (56.88%) | 0 | 2,076 |
| Debugger | 181/182 (99.45%) | 99.19% | 181/181 (100%) | 0 | 0 |

Converted total bytes1,939,608/2,256,728; Game1,768,172/2,072,880.
Root README changes only aggregate rows. Detailed updates stay in docs.
The unchanged different count reflects converting an already-correct original
assembly body, not repairing an incorrect installed routine.

## Evidence And Next Work

Tools f3bb1e752c135931e11c1fa60655b1a646c6f1ce commits exactly the new driver
and suite first; parent source/docs pin that revision next. Mounted
make tools-check and older standalone check_project_tools.py pass.
Preserve all100 original older status entries, HEADddbdd16 and both tracked
dirty hashes; mirror only the two absent new files, yielding102 entries.
No independent older checkout commit/reset/push.

Validation passes67 AST/exact-mirror pairs and160 documents/4,417 relative
links, zero broken links; receipts are in the ignored doc-check.json.
Manual Graphify update exits1: refuses17,170 nodes over retained38,954 and
preserves19,398 excluded-but-existing nodes from2,972 files. Existing
version/devcontainer warnings persist; no force/reinstall/purge.
Wait for the separate parent post-commit hook before close-out. Graph receipts
are operational, not function-matching proof.

Ignored conker/build/game-owner-link-setup-match-test holds immutable baseline,
before-source/ELF/guards/progress and shape/guest/native/negative/owner/rebase/
connected/fault/audit/conversion receipts. The matching driver stores four-profile
measurements and generated guards in conker/build/game-owner-link-setup-matching.
A prepared clone without immutable pre-install history explicitly skips that
audit rather than inventing installation proof.

Ignored game-owner-link-setup-lifetimes preserves the exploratory complete bodies:
108 declaration-order forms,16 stored-slot forms,10 home-reuse forms,60 workspace
positions and10 final shape checks, plus smaller failed self-capture families.
No broad permanent fitting framework or experimental production variants are added.

Before source SHA256: 83e6cc2038b40094c0521589275f851eae341bd29325b56267bcfab9ae90ee30.
Installed source SHA256: 59723ec2982df10861f966a65c4ab016fd7eb04d2d039215f9522a55423c0044.
Before/installed ELF SHA256: 873bf0f5b6f335c423f8d577cf0e330bf522bfaf04017bffd57ec5d2b6388dde.
Protected data SHA256: 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Resume **func_151B2690**, original176-word/frame0xD8 companion setup routine.
Recover its actual request/packet contract and captured-pointer lifetimes before
fitting; use the now-exact2348 and30B0 as unchanged dependencies.
Removing the25 GPR guards is a separate future compiler-style refinement,
not an unqualified instruction-replacement batch.
Common allocator/resource/SDK/hardware/gameplay, undefined portable-C domains
and the full renderer remain open. The Game goal stays active.
No OGL/Release/save/editor changes.
