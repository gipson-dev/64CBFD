# Game Record Mask Finish Direct Match

Date: 2026-10-11. Recover complete func_1503F16C in
conker/src/game/generated_6B320.c, replacing its zero-return placeholder.
VA 0x1503F16C..0x1503F2B0, ROM 0x6C61C..0x6C760: 81 words / 324 bytes.
All 81 words emit directly from semantic C under existing O2/g3/frame 0x20.
No guards, pools, padding, drops, insertions, shared headers, caller bodies,
compiler profiles or recipes change. Add only the required local byte-array
declaration for the existing D_800C666C timer alias.
Matching +1 only; converted counts/bytes unchanged. Full Game goal active.

## Baseline And Contract

Consumer ba884742602d00194b30db78d8dc898c6a6063e8 and mounted tools
4cc212194cbf3d1932c201e26cc0dd17ae0a9e95 were clean at entry.
[Note 1284](1284-game-record-random-vertical-rate-direct-match-20261011.md)
left this genuine 81-word / 80-difference target. Query Graphify, inspect the
complete routine, group-2 finish table, existing query helper and owner
profile. Reuse IDO, structured ELF/object/pool parsers, StateOracle/native32,
GLOBAL_ASM processing and both real padders. Codex is the single writer;
zero Claude calls, no bridge, installs or account changes.

Recover void func_1503F16C(s32 slot), consistent with the existing
void (*D_8008443C[])(s32) interface. Original finish entries are
func_1503EFC4, func_1503F108 and func_1503F16C. The dispatcher calls the
group-2 finish after setup, then writes state 1 and invokes the active row.
V0 has no separate status calculation and is ignored.

- Store timer 300 to D_800C666C + slot*16 before any query.
- Always call func_1503EF4C(2,0,slot), (2,1,slot), (2,2,slot) in that order.
  Treat every nonzero full-width return as success, not only one.
- First success reloads actor +0x94, ORs 0x40, stores it, then ANDs ~0x200
  and stores again. Second success independently reloads flags, ORs 0x80,
  stores, then ANDs ~0x100 and stores again.
- Third success independently reloads flags and clears 0x400 with one store.
  Failed queries do not touch flags. Preserve all unrelated bits and bytes.
- Keep the existing 812-byte actor stride, cached full-width slot, S0/RA,
  0x20 frame and branch/call-delay scheduling.

The complete 30-word func_1503EF4C is already linked-exact and retained.
It reads D_8008446C[group][row] pairs: zero first/second masks are wildcards;
nonzero masks require intersection with control words +4/+8 respectively.
Short-circuit the second domain when the first fails. Original helper has
one unreachable zero-result word at +0x6C, preserved unchanged.

## Fresh Qualification

The straightforward body matches all words on the first screen. Compact
no-unroll is identical; O1 variants emit 114 words/frame 0x18 with 108/109
differences. Keep the existing owner profile. Twelve pre-install tests pass
in 23.167 seconds; twelve installed tests pass in 16.723 seconds. The final
two literal-integrity/control gates pass again in 9.067 seconds. Receipts:
conker/build/game-record-mask-finish-match-test/.

- 900 retail/raw/padded cases cover all three result combinations, nonzero
  1/-1/0x80000000 returns, both phases, all 32 relevant flag-bit combinations,
  arbitrary preserved/high bits and mapped invalid slots. All 81 words execute.
  Verify each intermediate flag store, not just the final word.
- Eighteen effective callbacks rewrite live flags or the timer at each call.
  Later flag accesses see those values; timer is written once before calls
  and is not reset after mutations. Query arguments/order remain exact.
- 200 cases execute the actual 30-word mask helper over zero/wildcard/high-bit/
  full masks and two control domains. Reach all 29 executable words; the dead
  helper word never runs.
- Four effective aliases feed flag changes into a later pair query or the
  control-mask word. These are mapped guest tests with exact emitted order,
  not portable native aliases or actual N64 allocation acceptance.
- Two independent links rebase three target symbols with HI/LO carries in
  32 cases. All 100 fired fault triplets, including actual helper accesses,
  preserve complete memory/events/GPR/FPR state. No portable C faults/FCSR
  or hardware claim.
- Five freshly compiled semantic controls fail: wrong timer, selector, clear
  mask, one-only truth test and third update direction. Selector corruption
  fires the checked call protocol. A collapsed-store control has the same
  final flags but fails the original access/store trace.
- Both copied complete owners are diagnostic-free, pass GLOBAL_ASM processing
  and both production padders. All 21 neighbors/extents/relocations/pools
  remain exact, including dispatcher171, query30, rate45 and collision134.
- Literal source/ELF/seven-input checks and stale/duplicate install, source,
  three ELF and old-guard corruption controls pass. No baseline refresh,
  metadata projection or generic exception.
- 48 cases execute actual dispatcher171 -> predicate27 -> group-2 finish81
  -> query30 against the independent composed reference, with states 2/3,
  counts 0/1/3/5, phases and control-mask combinations. Active callbacks and
  motion/matrix tails remain boundary models, not full gameplay acceptance.
- Native32 O2/O0 each pass 6,144 result/bit/slot/mutation cases, checking all
  actor and control words. Three native controls fail with mismatch receipts.
  Both profiles additionally pass 300 cases using the recovered helper C body,
  with two mask domains and zero/high/full pair values. Native tests do not
  claim intermediate physical stores, private aliases or hardware/FCSR parity.

~~~sh
python3 -m tools.experiments.game_record_mask_finish_candidates --profiles
python3 -m unittest tools.tests.test_game_record_mask_finish_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
~~~

## Linked Audit

Source-only rebuild compiles the changed owner and relinks, exiting zero
with the known duplicate generated_12D630 recipe warning. Target owner is
diagnostic-free. Literal full-ELF comparison changes exactly 274 bytes:
272 target bytes and two size bytes (12 -> 324). Every other ELF byte,
body/address/extent, metadata record/string, section/header, pool and data
is exact. No metadata permutation or exception, including the timer alias.
Seven other inputs remain identical: guards, progress CSV, rodata assembly,
symbols, undefined functions, retail layout and Makefile.

Protected data: 189,088 bytes / 720 owners, zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

| Input | SHA-256 |
| --- | --- |
| Source before | 5516cd7c1641d54e312dcc5e6bbf0496f6b6dead96e22390a015c7213c1dbf36 |
| Source after | eab97cc6ad4b03b8384b63bb8d9db13ceed0a84a09dfe78a1c8c15cb11c42295 |
| ELF before | 2eba14a881b78db16bee6505b484a7484720777acf4ba8599ae6ef1f085002d1 |
| ELF after | 97ce8226e215f210817865fa0cd8e213da38f42849ba641cc1bb82244603be45 |
| Guards unchanged | 92f39fbf0bf509614ecff961e3a654e01d30c98666c3c65f224884f57102206e |

Fresh progress: Game 2,806/4,822 (58.19%), total 3,479/5,495 (63.31%),
Init 492/492 and Debugger 181/181. Zero drift / 2,016 still different.
Matching +1 only; README gets aggregate rows, no function narrative.

## Checkpoint And Next Body

Consumer, mounted and older standalone shared checks and native py_compile
pass. Bank mounted tools c7869ae first, then source, this note, five current indexes,
aggregate README and exact consumer gitlink. No push. Older sibling HEAD
ddbdd16b53ce60b054fb6e11bf0649a41f48375a and all 61 recorded hashes remain
unchanged. Copy only two absent paths with identical hashes; dirty count
338 -> 340. Final read-only snapshot records 63 hashes, including the two
identical new copies. Do not commit/reset independent older history. Target suites
run in the mounted consumer, not the standalone mirror. Prior unchanged
rate/collision/impulse/motion/matrix/setup suites are reused from Notes
1284/1283/1282/1281/1280/1279 on unchanged evidence, not called fresh runs.

Native graphify update . exits one on protective shrink refusal: 18,205
candidate nodes versus 39,985 saved. Preserve 19,398 nodes from 2,972
excluded but still existing files; no force/purge/install. Version/empty-source
warnings stay separate from compiler diagnostics. After consumer commit require a fresh
terminal Rebuilt receipt, advanced log bytes/UTC and zero workers.
Precommit log: 539,025 bytes. Launch alone is not completion.

Fresh recheck: func_1503F16C 81 words / zero linked differences. Next genuine
placeholder is func_1503F2B0, 85 words / 84 differences, VA
0x1503F2B0..0x1503F404, ROM 0x6C760..0x6C8B4, same owner. Its original
caller body already appears in Note 1278's teardown/query qualification;
inspect that evidence and the full active-callback contract before recovery.

Existing guard removal, remaining callbacks and independent SDK/hardware/
FCSR/renderer/gameplay acceptance remain separate and open. No OGL Release
build/change, private input/save or active editor/debugger mutation.
Keep the full Game goal active.
