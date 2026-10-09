# Game Owner State Callback Direct Match

Continue from [Note 1170](1170-game-owner-descriptor-constructor-direct-match-20261009.md).
Start clean at parent9ea9f653991b1f6d0c7575115356f2e39738158e and tools
0353bcbe59528737408acc58bce2df3fe9034e2c. One Codex writer, zero Claude calls;
routine matching and typed-contract evidence settle this without a second opinion.
Keep authorized checkpoints committed locally, tools first/consumer pin second;
no push, no independent older tools reset or commit.

## Installed Result

**func_151B2100 directly matches all67 retail words**, frame0x38, four JAL
relocation uses, zero guards/pools/isolated diagnostics under existing O2/g3.
Replace its false12-byte zero-return placeholder with the complete268-byte
void callback in [generated_1DF510.c](../../conker/src/game/generated_1DF510.c).
VA151B2100..151B220C, ROM1DF5B0..1DF6BC; retain the complete
[original owner assembly](../../conker/asm/1DF510.s).

[Complete-body driver](../../tools/experiments/game_owner_state_candidates.py)
screens nine forms/four profiles,36 rows. Selected O2/g3 is67/frame56/zero
differences; O2 is67/56/seven; both O1 profiles are70/frame40/69 differences.
All six real-local permutations retain the direct match. Widening the captured
state byte produces two differences; positive-gate rearrangement is68/56/61.

## Correct Callee Contracts

The initial complete callback was67/frame56 but21 words different: its two
setup callees were declared s32 by their false zero-return placeholders.
Typed void(u8*) declarations recover all67 words directly. The explicit
false-return-contract control reproduces67/56/21, separating this from an
unexplained register permutation. No function-pointer cast or word guards.

Those callees use A0 as the actor and have no caller-observed return API.
Restore their complete original bodies instead of leaving declarations
incompatible with their C definitions:

| Routine | VA Extent | ROM | Original Words | Frame |
| --- | --- | --- | ---: | ---: |
| func_151B2348 | 151B2348..151B2690 | 1DF7F8 | 210 | 0xA8 |
| func_151B2690 | 151B2690..151B2950 | 1DFB40 | 176 | 0xD8 |

The scoped [2348 fragment](../../conker/asm/nonmatchings/generated_1DF510/func_151B2348.s)
and [2690 fragment](../../conker/asm/nonmatchings/generated_1DF510/func_151B2690.s)
are literal complete-body extractions, not semantic C or new C matching credit.
Their original840/704-byte slots are byte-exact in the installed ELF. Track
them as assembly, pending actual C recovery. No shared headers/profiles or
guard manifest changes; no broad unrelated assembly batch.

## Validation And State Order

Load both endpoint pointers from actor+28/+30 before validating the first.
Then lazily require each endpoint's leading word nonzero, sentinel byte4
not255, and byte3B equal to the corresponding captured descriptor byte4/C.
On the first failing gate, write signed -1 at actor+E, without helper calls.
There is no invented NULL actor/endpoint gate: original fault order matters.

For valid endpoints, retain pair=actor+28 across all helpers. Capture previous
state byteD before func_151B22F4; store its low return byte atD. Only a changed
byte calls cleanup func_151B222C. Reload state after cleanup; state1 calls
func_151B2348, then reload again. State2 or0 calls func_151B2690. This is not
an else-if after setup: setup may change state and require the alternate path.
Helpers may change endpoint pointers without changing the retained pair home.
Original savedS0/RA and private pair SP24/previous byte SP2B are preserved.

Actual callback table D_8008A4E8[0x16] at8008A540 points to151B2100.
The complete45-word func_15149264 dispatcher at15149264..15149318,
ROM176714, is already byte-exact in the installed ELF. Its source uses the
callback as void; timer D_800BE9E4 is a32-bit word, not a halfword. Disabled
selector -1 is a signed byte; negative lifetime can cause actor release.

## Qualification

[Focused suite](../../tools/tests/test_game_owner_state_match.py) covers:

- Direct67-word shape, frame, four relocations, all profiles and wrong-return
  declaration control; both restored fragments equal the complete references.
- 21,552 guest cases/43,104 executions: every old-state byte, seven return
  words including signed/high-bit truncation, four endpoint alias layouts,
  six cleanup/setup mutation pairs, both stack phases and seeded canaries.
- Independent expected public memory/call sequences, including classifier
  mutations of state and endpoint pointers. ScratchGPR/FP and four argument
  homes are clobbered after every bounded call.
- 66 executable words reached. The duplicate old-state load151B2180 is
  unreachable: the invalid branch jumps to the epilogue; the valid likely
  branch loads old state in its delay slot and jumps over this duplicate.
- 96 connected cases use the actual21-word classifier and28-word cleanup.
  A release hook rewrites a later attachment pointer, checking the cleanup
  loop's live reread. Setup/alternate/release remain bounded hooks.
- 150,528 native32 cases use the typed void callback and full actor/endpoint
  canaries, all old bytes, gates, return widths, aliases and helper mutations.
  Aligned unions back actual actor storage and the expected raw byte buffer.
- Copied production owner preserves15 other routines, pools and relative
  relocations. Actual asm-processor post-processing and padder accept all
  three intended changes. Four existing Warning712 messages remain identical;
  zero new diagnostics, isolated callback clean.
- Six compiled effective negatives: wrong sentinel/code, late previous-state
  capture, omitted cleanup, else-if alternate gate and wrong invalidation.
  Rejection requires mismatched public output or calls, not arbitrary assertions.
- Six lazy-gate cases and44 missing-byte fault pairs; original/candidate
  prefixes agree. Guest order is not portable C or hardware fault proof.
- Four independent original/candidate symbol sets/eight links/four relocation
  uses/160 cases/320 executions verify JAL regions, low-byte state and mutations.
- 672 actual45-word registered-dispatcher cases/1,344 executions cover selector
  -1/0x16, timer flags/ticks, all invalid gates, transition helpers and final
  release. Other dispatch slots and helpers are bounded, not complete gameplay.

Initial pre-install nine-test run passes53.237s. Installed nine-test suite
passes28.984s after refining metadata checks. **Final ten-test installed suite
passes64.965s, zero skips**, including the dispatcher check and local
signed-byte oracle support.
No shared oracle change. Fixture corrections preserve production behavior:
copied fragment newline, coverage aggregation, native indentation/alignment,
discriminating late-capture input, correct dispatcher tick width.

## Whole-ELF And Progress Audit

All ELF loadable bytes match the immutable previous baseline except the three
reviewed slots268/840/704 bytes. Exactly their st_size values change12 to the
retail lengths; all20,318 symbol records retain name/address/type/other/section
meaning. GNU ld reorders some symbol/string entries after the new assembly
references. Verify complete symbol multisets and string multisets, unchanged
ELF/section headers and table extents before allowing only this metadata order.
Do not claim raw ELF byte identity outside the three symbol-size words.

Protected Game data189,088 bytes/720 owners is exact, with zero differences.
All11,510 guard rows remain byte-identical. Progress CSV has exactly two
language changes, C to assembly for2348/2690, no other row/extent changes.
Conversion credit falls by two functions/1,544 bytes because false C bodies
were removed. The callback was already C-classified: one new exact C function,
not one new conversion. Assembly restorations are not counted as C matches.

| Section | Converted Functions | Converted Bytes | Byte-exact C | Drift | Different |
| --- | ---: | ---: | ---: | ---: | ---: |
| Total | 5,487/6,042 (90.81%) | 85.91% | 3,410/5,487 (62.15%) | 0 | 2,077 |
| Init | 492/539 (91.28%) | 92.53% | 492/492 (100%) | 0 | 0 |
| Game | 4,814/5,321 (90.47%) | 85.26% | 2,737/4,814 (56.86%) | 0 | 2,077 |
| Debugger | 181/182 (99.45%) | 99.19% | 181/181 (100%) | 0 | 0 |

Fresh make -C conker -j4 build/conker.us.elf progress.csv and match-progress
NON_MATCHING=1 pass. Conversion totals are independently computed from the
fresh CSV's us rows (exclude the repeated CSV headers). Existing duplicate
generated_12D630 recipe warning and four owner Warning712 calls remain.
Root README changes aggregate rows only; detailed updates stay in working docs.
Prior whole-ELF constructor/renderer/alpha/endpoint receipts are historical,
superseded by this real installation; do not recapture their old baselines.

## Evidence And Next Target

Tools d6552d0fe49111b1ef3db4c4b7f532f4f16bf29f is committed first with only
the complete candidate driver and focused ten-test suite; parent source/docs
and literal assembly fragments pin that revision next, no push. Both mounted
make tools-check and older standalone check_project_tools.py pass. Validation
passes61 AST/exact mirror pairs and157 documents/4,377 relative links,
zero broken links. Preserve all94 older checkout entries and original dirty
tracked hashes/HEADddbdd16; only two absent authored files are copied there,
producing96 entries. No older checkout commit/reset or history duplication.

Manual Graphify update finishes exit1, refusing17,149 nodes over retained
38,927 while preserving19,398 excluded-but-existing nodes from2,972 files.
Existing version/devcontainer warnings persist. No force/reinstall/purge.
Parent post-commit rebuild is a separate receipt; wait for its confirmed
process handles to finish before reporting the completed checkpoint.

Ignored conker/build/game-owner-state-test preserves original baseline.json,
before-source/elf/guards/progress and shape/guest/connected/native/owner/
negatives/faults/rebases/audit/dispatcher receipts. Driver36 rows live in
conker/build/game-owner-state/measurements.json. Missing immutable history in
a prepared clone causes an explicit audit skip, not a claimed installation proof.

Before source SHA256: cc133b478920aaea4c11130a9127437f5b2069190090d3d912f0490333fc77ce.
Installed source SHA256: 83e6cc2038b40094c0521589275f851eae341bd29325b56267bcfab9ae90ee30.
Before ELF SHA256: 5a8540f1093c566336ff4cf268c8ab6bd03d63adcbc3c47c6a72980c4a8a786a.
Installed ELF SHA256: 7a42ef3e037f2d0665e3d35bf62e4be56d6586a6508586db75702bf5cef9dd84.
Protected data SHA256: 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Next recover **func_151B2348**,210 words/frame0xA8, now genuine original
assembly with a correct void actor interface. It creates three auxiliary
records via151B30B0: stores results at pair+18/+14/+10, conditionally copies
48-byte attachment packets to result+150. Capture endpoint pointers once;
preserve distinct repeated owner-byte reads, original constant-vector copies,
packet holes/reuse and private homes SP34/SP64. The middle packet reuses
retained flags with80/170 float updates; callee mutation/allocation failure
can affect later captures. Read actual151B30B0 interface before C fitting.
Following helper151B2690 is176 words/frame0xD8 and remains original assembly.
Full renderer1514803C, handwritten register contracts, complete helper-chain
integration/hardware/gameplay and host adoption remain separate open gates.
Game goal stays active; no OGL/Release/save/editor changes.
