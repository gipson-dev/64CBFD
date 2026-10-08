# Game Record Timer And Player-State Update Conversion

Date: 2026-10-08

## Result

Continue [Note 1130](1130-game-record-player-registration-conversion-20261008.md)
under the [focused workflow](../AGENT_WORKFLOW.md). Convert the final retained
`func_151D8A24` in [generated_205C90.c](../../conker/src/game/generated_205C90.c)
to complete semantic C. All **64 words /256 bytes**, frame **0x28**, match
retail after **four strictly checked private-byte stack-slot guards**;
**60 words emit directly** under existing IDO5.3 O2/g3. The owner now has
no GLOBAL_ASM directives. No filler, pools, data, profiles or Makefile changes.
Three local declarations recover the timer, callback table and release interface.
[205C90.s](../../conker/asm/205C90.s) and
[per-function assembly](../../conker/asm/nonmatchings/generated_205C90/func_151D8A24.s)
remain untouched. VA0x151D8A24..0x151D8B24, ROM0x205ED4..0x205FD4.

All linked instructions remain unchanged. Only this256-byte conversion row
and an exact four-row guard append change from the previous constructor baseline.

## Recovered Contract

`void func_151D8A24(u8 *record)`:

- If record[0xE] bit0 is set, subtract D_800BE9E4 from the signed16 timer at
  record+0x10, truncate/store/reload it and capture whether it is negative.
  Expiry is captured before any callback, not recomputed from later mutations.
- Read the signed byte at record+0x14. Only -1 skips dispatch; otherwise
  load D_8008FCC0[index] and call it with the captured record pointer.
- Compare fresh record[0x12] with record[0x16] after the callback. If different,
  scan four unsigned-byte players, reloading record[0x13] each iteration.
  Selected players call func_1501C17C first, then func_1501C010 with fresh
  record[0x12]. Finish by copying fresh record[0x12] to record[0x16].
- Release through func_1516972C last if the captured expiry flag was set.
  No record reads follow release. Callback changes to timer/enable byte do
  not cancel captured expiry; changes to masks/levels remain live.

Use explicit unsigned32 subtraction before signed16 truncation, avoiding
signed32 overflow without changing any emitted word. Valid native objects
are aligned; signed16 narrowing is verified on the prepared two's-complement
toolchain. Negative callback indices other than -1 are tested as guest
instruction evidence with mapped table entries, not portable C-array promises.
Native callback domains are -1 or0..127 with a controlled extended table;
that fixture is not a claim that retail's four-entry table has128 callbacks.
Actual [D_8008FCC0](../../conker/asm/data/234780.rodata.s) has the embedded-record
wrapper at index0 and three zero entries. The metadata entry at0x8008C174
points to this updater. Full dispatcher, null/arbitrary call targets, later
callee implementations, CP0 fault metadata, hardware and gameplay remain open.

## Source Fit And Guards

[Driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_record_state_update_candidates.py)
retains18 ordinary source forms plus nine effective negatives. Declaration
order, register/volatile expiry, initialization, nested player scope and
old-style parameters still leave four raw differences. Int expiry changes
the four accesses to word stores/loads; int player emits66 words/frame0x30/
63 differences, signed player66/0x30/61 and early initialized player loop
63/0x28/57. No zero-return scaffold, inline assembly or artificial local padding.

| Profile | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| O2/g3 | 64 | 0x28 | 4 |
| O2 | 64 | 0x28 | 12 |
| O1/g3 | 70 | 0x20 | 68 |
| O1 | 70 | 0x20 | 68 |

The earlier handoff's compilation puts the byte at SP+0x27. The final isolated
and complete copied owner both put it at **SP+0x26**; retail uses **SP+0x23**.
Expected-word guards at function+0x14,+0x4C,+0x8C,+0xD8 move only both stores
and both loads of this closed private byte. The frame, saved registers,
all control-flow words and seven symbolic relocations already match.
Five stale frame/access mutations are rejected. Raw executions prove the only
private differences are the old/new flag byte locations; translating those
four event addresses makes complete traces equal, with GP/FP/public state equal.
Patched executions have complete raw state/trace/memory equality with retail.
Arbitrary record aliases into the callee's private frame are not portable C
and are not asserted equivalent before normalization.

## Qualification

[Eight tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_record_state_update_match.py)
reuse Triangle/CopyOracle, ProgressReference, strict native32, owner/parser and
real padder helpers. Only the new local reference/model adds target behavior;
shared domain oracles are unchanged.

- **267,364 guest cases** cover all65,536 timer bit patterns, ten representative
  signed steps, all256 selector bytes, all256 flag/mask byte pairs and two SP
  phases. All64 words are reached. Compare independent public read/write/call
  flow and full normalized/retail GP/FP/trace/memory.
- A lazy case leaves timer, step, callback table and mask unmapped when all
  are skipped. **38 required fault prefixes** cover saves, private byte,
  timer/step, table/fields and post-callback/clear/register/free reads/stores.
  These qualify emitted instruction order, not portable C fault behavior.
- **640 mutation cases /eight modes** preserve captured expiry/owner while
  callbacks mutate timer/flag/level/mirror, clear changes the registration
  level, registration changes later masks and incoming-home writes cannot
  redirect the captured owner. Removing record storage at release proves
  there are no later record reads. Private-home cases are guest-only evidence.
- **1,607,424 actual native32 C executions** through a volatile function
  pointer cover every timer across all ten signed steps with enable/disable,
  every flag/mask pair, all level bytes,129 selector configurations and seven
  mutation modes. Pointer/int sizes4 and short2; compare all96 storage/canary
  bytes, ordered calls and unchanged timer global with independent expected
  flow. Use valid aligned objects and controlled callback/clear/register/free.
- **30 source/profile forms /168 ordinary executions /nine negatives** cover
  wrong flag bit, faulty expiry calculation, unsigned selector, wrong skip,
  cached mask/level, reversed clear/register, early release and pre-callback
  level capture. Each negative compiles and executes successfully; no
  exception counts as a behavioral negative pass. Other profiles can reread
  fields, so ordinary controls compare calls and public results, not identical
  read schedules. Strict selected/retail trace checks remain unchanged.
- Complete copied owner has **zero diagnostics**, ten unchanged neighbors,
  unchanged pools/relative relocations and an isolated-identical target.
  Real padder emits256 bytes with no filler/data. **Six independent links /
  216 executions** verify all **seven relocations**, signed-LO carries and
  high addresses against independently constructed expected words.
- **1,152 complete connections** run the actual eight-word embedded-record
  wrapper and13-word clearer with this complete64-word updater. Actual linked
  callback/metadata tables, wrapper and target match retail. The distance
  calculation, registration and release remain controlled interfaces.
- Preserve every historical hash/exact-row check. The shared history helper
  accepts only11,146,11,148 or11,152 rows, each with its strict known suffix.
  Existing constructor checks now validate the whole manifest while slicing
  only their own two rows. New target rejects four corrupted suffix rows,
  missing/extra rows and reversed suffix order; no prefix check is weakened.

Prequalification union: initial setup rejects the stale SP+0x27 assumption;
verify final isolated/copied SP+0x26 and correct expected words. Seven-test run
has five passes, two fixture failures in50.668s. Repeated fault deletion caused
KeyError, so inject each requested fault once. O1's extra field reread caused
overstrict control comparison; compare calls/public results for other profiles
and make the unsigned-selector negative choose a distinct mapped target.
Corrected03/06 pass in27.528s. Corrected history/connection08 passes in42.665s.
Exhaustive02 passes in272.088s. All eight pre gates have passing evidence;
no production defect or compiler diagnostic is hidden by these corrections.

Fresh installed **all49 target/five-neighbor tests pass in867.646s**,
zero skips/errors/failures. This includes the target's eight checks plus the
constructor, selected-player, player-mask, distance-level and embedded-callback
suites after changing the shared history helper. Ten shared padder checks
pass in0.044s. Both tools project
checks, CLI help and syntax checks in both mirrors pass. Wider unchanged
suites remain explicitly reused receipts, not fresh claims.

Reproduce the expanded suite from the source repository in WSL:

```sh
python3 -m unittest -v \
  tools.tests.test_game_record_state_update_match \
  tools.tests.test_game_record_player_registration_match \
  tools.tests.test_game_selected_player_state_match \
  tools.tests.test_game_record_player_mask_match \
  tools.tests.test_game_record_distance_level_match \
  tools.tests.test_game_record_embedded_callback_match
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

## Linked Audit And Progress

Build succeeds. Global guard CSV dependency triggers broad recompilation;
duplicate generated_12D630 recipe warnings and diagnostics in unchanged
Game/Debugger sources remain. Strict copied owner has zero diagnostics;
full build is not claimed warning-free.

Fresh audit against game-record-player-registration-test/after.json preserves
all **6,058 bodies/addresses/extents**,6,042 retail slots/16 overflow symbols,
protected sections and prior **11,148 guards**, then adds exactly four.
All720 Game-data owners /189,088 bytes retain SHA256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Exactly one conversion row changes: func_151D8A24, asm -> c,256 bytes.
Correct a copied old function name in the audit's report label; its target,
progress-row and body assertions were already checking func_151D8A24.

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,475/6,042 (90.62%) | 1,933,664/2,256,728 (85.68%) | 3,386/5,475 (61.84%) | 2,089 /0 |
| Game | 4,802/5,321 (90.25%) | 1,762,228/2,072,880 (85.01%) | 2,713/4,802 (56.50%) | 2,089 /0 |

Init492/492 and Debugger181/181 converted routines remain exact.
New ignored baseline: conker/build/game-record-state-update-test/after.json.
Compare the previous constructor baseline, not this target's own after.
Root README gets aggregates only; detailed updates remain here.

Final source SHA256:
4bd2a441bfd4d77bbc90bfa1e5f217487b11ed77274720a296b4f60d3f36f0f3.
Final progress SHA256:
4fe1fecda90ddc100983f674068e67269dae5ec5fc341371be00de6466ce9637.
Guard CSV SHA256:
2c03beead9be3da5c98d0708dffd244ad2f9d908ab1dc9e4f7983ea7f301360c.
Original owner/progress and complete receipts are retained in the ignored
game-record-state-update-test directory.

## Authorized Checkpoint

Continue "Keep commited": tools committed first at
**8e1a208bbeb5fa7b790571809c8dd7a872fe47f8**. Parent checkpoint groups this
one conversion, four guards, Note1131/progress docs and that exact tools pin.
No push requested/performed. Preserve the older independently dirty standalone
tools branch; mirror relevant fixtures without resetting, stashing or creating
duplicate divergent history. Zero Claude calls and no host Release, runtime,
saves/configuration, accounts or bridge changes.

Validate117 documents /3,976 relative links /zero broken. Twenty-three relevant
tools policy/fixture files are byte-identical between mounted and standalone
checkouts. Staged tools whitespace checks pass; mounted tools is clean after
its commit. Parent records an exact revision, not a moving branch; remote
publication is not verified.

Graphify query is scoped but does not provide this target's complete contract.
Full update refuses38,516 ->16,728 nodes and keeps19,398 nodes from2,972
excluded existing files fail-closed. Preserve graph/ignore edits; refresh
remains incomplete, separately from matching qualification.

## Next Function

[func_151D8718.s](../../conker/asm/nonmatchings/generated_204660/func_151D8718.s)
remains retained in the adjacent [owner](../../conker/src/game/generated_204660.c):
**19 words /76 bytes**, frame **0**, VA0x151D8718..0x151D8764,
ROM0x205BC8..0x205C14. Ignored next-velocity-screen.py retains complete forms:
natural and explicit-square19 words/three differences, reversed square operand
19/five, position-first20/eighteen. Zero diagnostics/pools. No installation
or behavior qualification claimed.

Mixed pointer/pointer/f32 ABI passes delta in A2, copied to F12. Capture old
velocity before updating velocity; then add oldVelocity*delta plus
D_800AB2F0*(delta*delta) to position[1], preserving rounding/grouping and
live loads after the first store. Actual constants are0.2340000123 and
0.1170000061. Two callers pass an0x1C-byte record, velocity at+0xC.
Remaining differences include F0/F2 allocation and commutative addition order.
FP exceptional/finite values, aliases/access order, caller ABI, complete owner,
independent links and connected paths remain future gates. Wider Game and
full callee/hardware/gameplay/PC-port work remains open.
