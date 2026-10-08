# Game Node Group Collector Direct Conversion

Date: 2026-10-08

## Result

Continue the next local retained assembly identified in
[Note 1123](1123-game-effect-callback-scheduling-match-20261008.md).
Replace `func_15033E28`'s `GLOBAL_ASM` pragma with complete semantic C in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
All **23 words /92 bytes** emit directly under existing IDO 5.3 O2/g3,
with the original **frame 0** and zero raw or linked differences.

VA `0x15033E28..0x15033E84`, ROM `0x612D8..0x61334`.
Reference: [5D2C0.s](../../conker/asm/5D2C0.s) and the retained
[per-function assembly](../../conker/asm/nonmatchings/generated_5D2C0/func_15033E28.s).
Reference assembly stays untouched. No guards, filler, new data, profile,
Makefile, declaration or shared-header changes. Reuse the existing owner-local
`u8 *D_800C3EE0`; its HI16/LO16 pair remains symbolic.

This is an **assembly-to-C conversion**, not a zero-return placeholder repair.
The original assembly was already byte-exact. All 6,058 linked function bodies,
addresses and extents remain unchanged; only this 92-byte conversion record
changes from `asm` to `c`.

## Recovered Contract

1. Capture list head D_800C3EE0 once. An empty list returns 0 without
   dereferencing actor or output. Retain the redundant opening null check
   required by the retail instruction layout.
2. Each iteration reloads unsigned actor group byte +0x3B, then unsigned
   current-node group byte +0. The actor group is **not cached** across nodes:
   aliased output stores can change a later comparison.
3. Load current-node next pointer +0x54 **before** the matching-node output
   store. An output alias overwriting that field must not change this
   iteration's captured traversal pointer.
4. If groups match, append the current node pointer at `output[count]`,
   increment count, and continue through the captured next pointer. Return
   the number appended. Do not add output capacity checks, cycle limits,
   sorting, a terminator or a fresh head read absent from retail.

Signature: `s32 func_15033E28(u8 *actor, u8 **output)`.
The retail caller in [B3020.s](../../conker/asm/B3020.s), at 0x1508DF64,
passes its actor in A0 and stack+0x80 in A1, copies returned V0 to S4, then
iterates four-byte pointers from that stack array. This verifies the static
caller interface; the complete calling workflow is not executed here.

No calls or saved-register frame in the collector. Selected/retail execution
checks all saved GP/FP registers, return, complete access order and memory.
Finite mapped fixtures do not qualify cyclic lists, unbounded output storage,
count overflow, arbitrary private-frame aliases or full gameplay/hardware.

## Source Fit

[Candidate screen](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_group_collector_candidates.py):
the initial current-node `while` loop has the correct length/frame but seven
raw differences. A next-cursor loop reduces this to four. A separate captured
next pointer and current-node `for` cursor recover the full direct match,
including unconditional branch-delay cursor assignment and actor/node load order.
Twelve targeted cursor/group/postincrement forms include two direct forms;
an unnecessary byte local introduces an extra instruction rather than helping.

| Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Initial current-node loop | 23 | 0 | 7 |
| Next-cursor loop | 23 | 0 | 4 |
| Selected separate current/next cursor | 23 | 0 | 0 |
| Selected postincrement output | 23 | 0 | 0 |
| O2 without g3 | 23 | 0 | 3 |
| O1/g3 | 31 | 0x10 | 30 |
| O1 | 31 | 0x10 | 30 |

No scheduling guards needed. Sixteen source/profile forms and seven effective
compiled negatives distinguish cached group, next-after-store, wrong actor
group/next offsets, inverted comparison, counting every node and terminator
store. Ordinary alternate-profile controls compare public writes, return,
memory and saved-register ABI; their private frames/read schedules are not
asserted retail-identical. Selected-body access-order/fault checks remain strict.

## Qualification

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_group_collector_match.py), including the later stack-output check:

- **69,633 guest cases**: all 65,536 actor/node byte pairs, 4,096 eight-node
  mask/topology cases and one empty-list case. Exercise all 256 match masks,
  two physical traversal orders, two SP phases and all **23/23 words**.
  Compare an independent ordered-access reference with complete selected/
  retail GP/FP state, trace, memory, return and saved-register ABI. No hooks.
- Three lazy-storage cases and thirteen fault prefixes qualify head/actor/
  group/next/output requirements and partial writes. Five alias layouts run
  at two SP phases: live actor group, current next pointer, later node group,
  global head and current node group. Whole mapped canaries and read/store
  ordering are checked, not only the output count.
- **262,152 actual native32 complete-C executions**, with asserted four-byte
  pointers, exercise all 65,536 group-byte pairs and every eight-node match
  mask in two traversal orders, plus eight lazy/alias cases. A separate native
  reference snapshots/restores inputs, comparing every node/actor/output byte
  and global head value. Native aliases derive their byte effects from native
  pointer endianness rather than assuming guest big-endian pointer bytes.
- Actual copied owner retains **39 unchanged neighbors**, normalized pools
  and relative relocations, with zero diagnostics. Real padder emits exactly
  92 bytes, no filler or new data. Six independent entry/global links and
  eighteen executions qualify original, shifted, signed-LO-carry and high
  address bindings while keeping the global symbol relocation.
- Sixteen source/profile forms yield 72 ordinary executions and seven
  effective negatives. The selected form retains complete read/write order;
  ordinary alternate forms need not share its read schedule or private frame.
- Six additional selected/retail executions use the actual caller's stack+0x80
  output layout at two SP phases, checking empty/eight-match/mixed lists,
  complete stack/output canaries, pointer order and the absent terminator.
  This exercises the collector interface, not the complete original caller.

The first seven-test run takes **34.368s**; six pass and the alternate
next-cursor control fails a too-strong read-schedule comparison. Compare
ordinary alternate forms by public effects while retaining the selected
body's full ordered trace. The second run takes **52.862s**; six pass and O1's
0x10 private frame lacks fixture stack storage. Map bounded stack storage and
exclude only that private region from alternate-profile public comparisons.
Selected/retail full-state and fault checks remain unchanged; no production
body change. The corrected **seven pre-install tests pass in 57.702s**,
zero skips/errors/failures.

The initial audit reaches its unchanged-body/section/guard checks, then its
byte-total parser encounters the progress CSV's repeated section headers.
Validate the two exact header rows separately from all 6,042 data rows;
the corrected pre/post-install audits pass without changing the CSV format.

All **61 combined post-install tests pass in 852.236s**, zero skips/errors/
failures: seven collector, seven callback, seven delayed effect, eight
registration, seven latch, eight matrix, seven cleanup, four binding and six
scheduling checks. The additional stack-output test is added after that
process loads its seven collector checks. The final **eight collector tests
pass in 88.381s**, including all six stack-output executions. This qualifies
**62 unique focused checks across the two runs**, not a single 62-test run.
Ten shared padder/word-patch tests pass in 0.047s. Both tools checkouts pass
project checks; syntax, candidate/profile/CLI driver, whitespace and required
Graphify AST update pass. Documentation: **107 documents /3,868 relative
links /zero broken**; all eight changed tools files byte-identical in both
local copies. Final linked audit retains the exact conversion-only change.
Existing Graphify version/empty-devcontainer/large-HTML warnings do not
invalidate the updated graph.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds, retaining
existing duplicate generated_12D630 recipe warnings. The actual owner compiles
without diagnostics. Compare against `game-node-effect-callback-test/after.json`:
**6,058 symbols /6,042 retail slots /16 overflow symbols**, all bodies and
addresses/extents unchanged. `.init`, `.init_data`, `.debugger`, `.game_data`
and all **11,146 guard rows** remain unchanged, no new guards.
All 720 Game-data owners /189,088 bytes retain SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

The only conversion-row change is `func_15033E28: asm -> c`, **92 bytes**.
Converted total **5,468/6,042 (90.50%)**, bytes **1,932,276/2,256,728 (85.62%)**;
Game **4,795/5,321 (90.11%)**, bytes **1,760,840/2,072,880 (84.95%)**.
Fresh exact totals **3,379/5,468 (61.80%)**, Game **2,706/4,795 (56.43%)**;
**2,089 still different /zero drift**, unchanged because this target was
already exact assembly. Init 492/492 and Debugger 181/181 stay exact.
Root README changes aggregate conversion/matching rows only.

New ignored baseline: `conker/build/game-node-group-collector-test/after.json`.

```sh
python3 -m tools.experiments.game_node_group_collector_candidates
python3 -m tools.experiments.game_node_group_collector_candidates --profiles
python3 -m unittest tools.tests.test_game_node_group_collector_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make tools-check
```

New tools files are mirrored in mounted `tools/` and sibling `64CBFD Tools`,
alongside the previous delayed-effect/callback changes. They are **uncommitted/
unpublished**; intended GitHub links are not publication evidence. Committed
tools pin stays `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`; see
[tools ownership](../TOOLS_REPOSITORY.md). No commit/push, Claude call/workflow
setup, OGL Release build, save/configuration or runtime change this turn.

## Next Work

Next local retained compiler-generated assembly **`func_15033EC4`**:
**18 words /72 bytes**, frame **0**, VA `0x15033EC4..0x15033F0C`, ROM
`0x61374..0x613BC`. Static inventory only, no C candidate installed:

- Walk D_800C3EE0 once, reading each unsigned node group byte and capturing
  next pointer +0x54 before any byte write.
- Compare against two **full32 argument keys**, not narrowed u8 parameters.
  A match to the first writes the second key's low byte; otherwise a match
  to the second writes the first key's low byte. Other groups are untouched.
- Preserve empty-list behavior, equal-key precedence and branch-delay
  traversal lifetime. Do not add list bounds or change returned register
  behavior without inspecting the original calling interface.

Continue from the new baseline. Wider Game conversion/matching, the open
`func_15031070` resolver and complete calling-workflow/hardware/gameplay/
PC-port qualification remain open; this checkpoint does not complete the goal.
