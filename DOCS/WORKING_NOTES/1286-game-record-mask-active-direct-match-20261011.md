# Game Record Mask Active Direct Match

Date: 2026-10-11. Recover complete func_1503F2B0 in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503F2B0..0x1503F404, ROM 0x6C760..0x6C8B4: 85 words / 340 bytes.
All 85 words emit directly from semantic C under existing O2/g3/frame 0x20.
No guards, pools, padding, drops, insertions, declarations, shared headers,
caller bodies, compiler profiles or recipes change. Matching +1 only;
converted counts/bytes unchanged. Full Game goal remains active.

## Baseline And Contract

Consumer 7eb8efd1a87cd718995e3d5c6b35126d5ba35d4b and mounted tools
c7869ae692a523713cdf15f08e396d843407cb0e were clean at entry.
[Note 1285](1285-game-record-mask-finish-direct-match-20261011.md)
left this genuine 85-word / 84-difference target. Read workflow, query
Graphify, inspect complete retail body, existing owner profile and original
callback tables. Reuse IDO, structured ELF/object/pool parsers, MIPS oracle,
native32 runner, GLOBAL_ASM processing and both production padders.
Codex is the single writer; zero Claude calls, no bridge/install/account changes.

Recover void func_1503F2B0(s32 slot), matching the dispatcher's existing
void (*D_80084448[])(s32) interface. The original active table is
func_1503EEC0, func_1503EEC0, func_1503F2B0, not func_1503F404 in row one.
Original finish table remains func_1503EFC4, func_1503F108, func_1503F16C.
Keep full-width slot, S0/RA lifetime and retail branch-likely/delay scheduling.
V0 is not a separate status calculation and the indirect caller ignores it.

- Always call preparation func_1503ECA0(slot) before reading timer or clock.
  Preparation changes to either input must be observed.
- Read live signed 32-bit D_800BE9E4 and signed control halfword +0xC,
  stride 16. Subtract, store the low 16 bits, then reload the signed stored
  halfword. Only a reloaded value <= 0 expires. Zero expires; positive
  returns without teardown, queries or flag access. A wide-result branch
  is wrong when the halfword wraps.
- On expiry call func_1503E260(slot) before all three queries. Its timer
  rewrite must survive and must not re-gate the already-selected expiry path.
- Always query func_1503EF4C(2,0,slot), (2,1,slot), (2,2,slot), in order.
  Every nonzero full-width result succeeds, including -1 and the high bit.
- Each successful query independently reloads actor +0x94 at stride 812,
  ORs 8, 4 or 2 respectively, and stores once. Failure does not touch flags.
  Teardown/query mutations remain live; unrelated bits and bytes survive.

Existing teardown89, predicate27, query30, preparation134, finish81 and
dispatcher171 are retained. Fresh linked comparisons confirm the first
three exact retail bodies before connecting them. The helper's dead zero
words and existing guards remain unchanged. Preparation/free and motion/
matrix tails are bounded test models here, not new hardware/gameplay proof.

## Fresh Qualification

Straightforward source matches on the first screen: 85 words/frame 0x20,
zero differences/pools. Compact no-unroll emits the identical body.
O1/g3 and O1 emit 92 words/frame 0x20 with 88 differences. Keep the existing
owner profile. Eleven pre-install tests pass in 22.768 seconds; eleven
installed tests pass in 29.055 seconds. After strengthening the dispatcher
matrix to 288 cases/all 26 executable predicate words, the final eleven-test
installed suite passes in 23.760 seconds. The final two literal-integrity/
corruption-control gates pass again in 7.802 seconds. Receipts:
conker/build/game-record-mask-active-match-test/.

- 986 retail/raw/padded cases cover signed halfword extrema, zero/one/two,
  zero/positive/negative/full-width clocks, wrap, both phases, all nonzero
  return combinations, all 32 flag-bit positions and mapped invalid slots.
  Execute all 85 target words. Signed32-overflow fixtures are guest-only,
  not portable C overflow claims.
- Sixteen effective callback cases mutate timer, clock and flags in
  preparation, timer/flags during teardown and flags at each query.
  Four mapped aliases qualify timer feedback into the clock word and a
  flag store becoming a later query mask. The latter distinguishes 10
  from a frozen-pair result of 14. Rebased actor alias uses a state-zero
  teardown path, avoiding an unre-based helper actor. These are emitted
  guest-order tests, not portable aliases or real allocation acceptance.
- 576 cases execute actual active85 -> teardown89 -> predicate27/query30
  with hooks removed for those bodies. State-zero, positive/expired timers,
  counts 0/3/5, both phases, both mask domains and free mutations agree
  with the independent composed reference. Reach all 85 active words and
  all 29 reachable query words; preserve helper dead words.
- Two independent links rebase six symbols with HI16/LO16 carries in 64
  cases. All 204 fired fault triplets, including actual teardown/query
  accesses, preserve complete memory/events/GPR/FPR state. No portable C
  faults, hardware or FCSR claim.
- Eight freshly compiled semantic controls fail: wrong zero expiry gate,
  unsigned timer, addition, first flag bit, one-only truth test, omitted
  teardown, selector protocol and branching on the wide result. Each
  discriminator fires; no baseline refresh or production workaround.
- Both complete copied owners are diagnostic-free, pass GLOBAL_ASM and
  both actual padders. All 21 neighbors, extents, relocations and normalized
  pools are exact. Isolated and complete-owner selected raw bodies agree.
- Literal source/whole-ELF/seven-input gates and stale/duplicate source,
  source corruption, three ELF corruptions and guard corruption controls
  pass. No metadata projection, ignored permutation or generic exception.
- 288 original-table cases execute actual dispatcher171 -> finish81 ->
  active85 -> teardown89/predicate27/query30. Cover states 1/2/3, counts
  0/1/3/33, both mask domains, positive/expired/negative clocks, phases and
  free state mutations. Reach all 26 executable predicate words.
  The original NULL teardown table is modeled explicitly. Non-skipped
  element rows execute the actual predicate. Element setup/callbacks,
  preparation/free/tails remain bounded, not complete gameplay acceptance.
- Native32 O2/O0 each pass 21,600 modeled timer/result/flag/slot/mutation
  cases plus 1,200 cases using the recovered query helper C. Compare all
  26 actor/control records and the call protocol; three native negatives
  fail with mismatch receipts. Native clocks avoid signed32 overflow.
  The halfword truncation is qualified for this GCC32 runner, not claimed
  as general portability, private-alias or physical-store/hardware proof.

Initial fixture failures were resolved before installation: duplicate symbol
keyword construction, a stale preparation address in the rebased hook, an
unre-based actor access in the alias chain, the incorrect assumed row-one
callback, missing finish timer alias and signed-byte support in the dispatcher
oracle. No production workaround or immutable-baseline refresh was used.

~~~sh
python3 -m tools.experiments.game_record_mask_active_candidates --profiles
python3 -m unittest tools.tests.test_game_record_mask_active_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit

Source-only rebuild compiles one owner and relinks, exiting zero with the
known duplicate generated_12D630 recipe warning. The target owner is
diagnostic-free. Literal whole-ELF comparison changes exactly 285 bytes:
283 target bytes and two function-size bytes (12 -> 340). Every other
ELF byte/body/address/extent/metadata/string/section/header/pool/data is
unchanged. Seven other inputs remain exact: guards, progress CSV, rodata
assembly, symbol definitions, undefined functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | eab97cc6ad4b03b8384b63bb8d9db13ceed0a84a09dfe78a1c8c15cb11c42295 |
| Source after | aa141c65ad29d29a1ff7d7b52e96d8115df088fa27b52244e610d1bfb34d69f8 |
| ELF before | 97ce8226e215f210817865fa0cd8e213da38f42849ba641cc1bb82244603be45 |
| ELF after | 407aad745988d43056465c75d3cf2ac866787e70ab431e8d316d82fdc2a5f1cc |
| Guards unchanged | 92f39fbf0bf509614ecff961e3a654e01d30c98666c3c65f224884f57102206e |

Fresh progress: Game 2,807/4,822 (58.21%), total 3,480/5,495 (63.33%),
Init 492/492 and Debugger 181/181. Zero drift / 2,015 still different.
Matching +1 only; root README receives aggregate rows, no function narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools ece87c1 and caller-coverage refinement a96b414
first, then consumer source, this note, five current indexes, aggregate
README and exact gitlink. No push. Preserve older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 63 prior hashes; copy
only two absent paths with identical hashes, dirty count 340 -> 342.
Synchronize only this-turn test copy after the caller-coverage refinement;
verify it still matches the initial tools commit before overwriting it.
Final read-only snapshot records 65 hashes, including both current copies.
Do not commit/reset independent older history. Focused suites run mounted
in the consumer, not the standalone mirror. Prior unchanged neighbor suites
are reused from Notes 1285/1284/1283/1282/1281/1280/1279/1278 on literal
unchanged evidence, not described as fresh runs.

Both native graphify update . runs exit one on protective shrink refusal:
18,213 initial and 18,221 final candidate nodes versus 39,993 saved.
Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version and
empty-source warnings remain separate from compiler diagnostics.
Require a fresh post-consumer-commit terminal Rebuilt receipt, advanced log
bytes/UTC and zero workers; launching a detached hook is not completion.

Fresh target recheck: func_1503F2B0, 85 words / zero linked differences.
Next genuine placeholder func_1503F404 has 43 slot words / 38 differences,
VA 0x1503F404..0x1503F4B0, ROM 0x6C8B4..0x6C960. Its retail body has
40 words plus three original zero tail words. It is a matrix conversion/
copy and ten-argument forwarding wrapper, not the group-one active callback.
Inspect its complete caller ABI, guMtxL2F/memcpy gate and recovered
func_1503E5F8 interface before recovery.

Existing guard removal, remaining bodies and independent SDK/hardware/
FCSR/renderer/gameplay acceptance remain separate and open. No OGL Release
build/change, private input/save or active editor/debugger mutation.
Keep the full Game goal active.
