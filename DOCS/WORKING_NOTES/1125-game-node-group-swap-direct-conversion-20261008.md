# Game Node Group Swap Direct Conversion

Date: 2026-10-08

## Result

Apply the user's [Codex/Claude workflow](../AGENT_WORKFLOW.md) and finish the
next retained assembly from [Note 1124](1124-game-node-group-collector-direct-conversion-20261008.md).
Replace `func_15033EC4`'s pragma with complete semantic C in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c).
All **18 words /72 bytes**, **frame 0**, emit directly under existing IDO
5.3 O2/g3, with zero raw/linked differences and no guards, filler, new data,
profile, header or Makefile changes. Reference assembly stays untouched.

VA `0x15033EC4..0x15033F0C`, ROM `0x61374..0x613BC`.
References: [5D2C0.s](../../conker/asm/5D2C0.s) and
[retained assembly](../../conker/asm/nonmatchings/generated_5D2C0/func_15033EC4.s).
Original assembly was already exact: this increases C conversion, not a
reduction in still-different routines. Every linked body remains unchanged.

## Recovered Contract

- Capture D_800C3EE0 once. Empty head performs no node access.
- Read each unsigned group byte and capture next pointer +0x54 before any
  store. Only capture the current link: future links remain live after
  earlier writes. Do not pre-cache the whole list or reload global head.
- Compare against two full32 keys. Matching first writes second's low byte;
  otherwise matching second writes first's low byte. Equal keys keep first
  precedence. Non-matching groups and other node bytes stay untouched.
- Signature `void func_15033EC4(s32 first, s32 second)`. The retail caller
  in [func_15062800.s](../../conker/asm/nonmatchings/game_83300/func_15062800.s)
  loads two unsigned actor bytes +0x3B, saves four argument words, and calls
  at 0x15062950. Its seven-word prefix starts 0x1506293C /ROM 0x8FDEC.
  Continuation ignores V0. Retail V0 ends zero, but that is emitted
  instruction evidence, not a portable return-value promise for void C.

The selected `firstKey` local recovers register allocation, not proof of the
original variable names/declarations. Source captures next before group;
IDO emits retail group-before-next, both before the store. Fault-prefix
checks qualify emitted instructions, not portable C fault-order semantics.
Do not add capacity/cycle limits, node validation or extra stores.

## Source Fit And Qualification

[Candidate driver](https://github.com/gipson-dev/64CBFD-Tools/blob/master/experiments/game_node_group_swap_candidates.py):
initial group-first C is 18 words/frame0 with nine differences. Next-first
reduces to six; combining captured first key and next-first gives direct zero.

| Form | Words | Frame | Raw Differences |
| --- | ---: | ---: | ---: |
| Initial group-first | 18 | 0 | 9 |
| Initial next-first | 18 | 0 | 6 |
| Selected cached-first /next-first | 18 | 0 | 0 |
| For cursor /explicit store casts | 18 | 0 | 0 |
| O2 without g3 | 18 | 0 | 3 |
| O1/g3 and O1 | 28 | 0x10 | 26 |

[Eight focused tests](https://github.com/gipson-dev/64CBFD-Tools/blob/master/tests/test_game_node_group_swap_match.py)
reuse existing complete-body MIPS/native32, owner, relocation and padding
helpers rather than creating another execution engine:

- **114,945 guest cases**: 65,536 byte-key pairs, 43,264 full32 key/group
  cases, 6,144 mask/topology/SP-phase cases and one empty head. All **18/18
  words** reached. Independent ordered reference and complete selected/
  retail GP/FP, access trace, memory and saved ABI agree; no hooks.
- One lazy head case, ten required-read fault prefixes and three mutable
  aliases at two SP phases: head-owning node, overlapping records, and an
  earlier group store changing a future next pointer. Partial stores and
  canaries qualify. Arbitrary/read-only hardware mappings are not claimed.
- **16,951,557 actual native32 C executions** through a volatile function
  pointer: 16,777,216 exhaustive byte-key/group triples, 43,264 full32 cases,
  131,072 mask/topology cases and five lazy/alias cases. Assert four-byte
  pointers/ints; compare all node/header/alias buffer bytes against a separate
  reference. Native pointer aliases use native byte order, not guest endian.
- Seventeen source/profile forms, 80 ordinary executions, seven effective
  compiled negatives: narrowed keys, independent branches, signed group,
  wrong group/next offsets, halfword stores and rereading the second test.
  Alternate forms compare public effects/ABI, not private schedules or void
  V0. Selected-body full-state/order checks stay strict.
- Copied owner: **39 unchanged neighbors**, normalized pools and relative
  relocations preserved, zero diagnostics. Real padder emits exactly 72 bytes,
  no filler/data. Six independent entry/global links and eighteen executions
  cover shifts, signed-LO carry and high bindings. HI/LO stays symbolic.
- **50 actual caller-prefix/callee executions**: retail unsigned key loads,
  four stack saves and JAL delay execute with the complete selected/retail
  callee at two SP phases. Synthetic exit boundary follows the prefix;
  complete calling workflow/hardware/gameplay is not claimed.

Initial eight-test run: seven pass, one fixture compilation failure, 50.569s.
Batch-zero-only keys/permutation/locals were declared in the other seven
native batches under strict `-Werror`. Move only those declarations into
batch zero; no production-body change or weakened assertion. Corrected
**eight pre-install tests pass in 98.473s**. All **eight post-install tests
pass in 48.169s**, zero skips/errors/failures. Ten shared padder/word-patch
tests pass in 0.045s. Project checks in both tools copies, syntax, complete
driver, profiles and CLI help pass.

## Linked Audit And Progress

`make -C conker -j4 build/conker.us.elf progress.csv` succeeds, with existing
duplicate generated_12D630 recipe warnings. Owner compiles without diagnostics.
Pre/post audit against `game-node-group-collector-test/after.json` confirms
**6,058 bodies/addresses/extents unchanged**, 6,042 retail slots/16 overflow
symbols. `.init`, `.init_data`, `.debugger`, `.game_data`, all 720 Game-data
owners /189,088 bytes and **11,146 guard rows** unchanged. Game-data SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Validate 6,042 conversion data rows and two exact repeated headers. The only
row change is `func_15033EC4: asm -> c`, 72 bytes. Fresh match-progress:

| Section | Converted | Converted Bytes | Byte-Exact | Different /Drift |
| --- | --- | --- | --- | --- |
| Total | 5,469/6,042 (90.52%) | 1,932,348/2,256,728 (85.63%) | 3,380/5,469 (61.80%) | 2,089 /0 |
| Game | 4,796/5,321 (90.13%) | 1,760,912/2,072,880 (84.95%) | 2,707/4,796 (56.44%) | 2,089 /0 |

Init 492/492 and Debugger 181/181 stay exact. New ignored baseline:
`conker/build/game-node-group-swap-test/after.json`. README aggregates only.

## Workflow Record And Limits

Source HEAD `b794defbbfa846d7dfa2e2939b904a2f15583fd2`. Parent/index tools pin
remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`. At turn start the mounted
tools HEAD had independently advanced to `35dd106864aed4f7772e8f826b9fdb6af2b1fcb1`;
preserve that pre-existing unstaged pin difference and `.gitignore` edits.
Standalone tools HEAD remains ddbdd16. This turn does not change any HEAD/pin.
Mirror the qualified swap driver/test and short tools-agent pointer locally;
own changes are uncommitted. Remote publication of 35dd106 is not verified.

Claude budget 0 /attempted 0 /completed 0. No packet or answer: direct compiler,
assembly and test evidence resolve the question. Installed local CLI help is
verified, but paid review, authentication/billing and automation enforcement
remain untested. Use [four templates](../AGENT_PROMPTS.md) when justified.

Reuse Note1124's prior neighbor-suite receipts, including 61 combined tests
and eight strengthened collector tests: these were **not rerun this turn**.
Fresh copied-owner checks and full linked audit establish unchanged bodies,
data, profiles, guards and helpers. Fresh focused/shared gates qualify this
direct conversion without repeating the prior broad suite. Any unexpected
audit change or shared/semantic edit would require wider regression.

Required `graphify update .` attempted. Existing ignore-rule changes reduced
the corpus; Graphify refuses to replace 38,427 nodes with 16,660 and retains
old graph. Do not force overwrite or undo user's ignore changes. Graph refresh
is incomplete; matching and linked-audit evidence are independently valid.
No commit/push, OGL Release, save/configuration or live-runtime operation.

Documentation validation: **111 documents /3,896 relative links /zero broken**.
Eleven relevant tools policy/fixture files are byte-identical between mounted
and standalone copies. Source and both tools checkouts pass whitespace checks;
the source check reports the pre-existing `.gitignore` CRLF-to-LF notice.

## Next Work

This owner now has no GLOBAL_ASM pragmas. Next small compiler-generated Game
candidate: **func_151D8BE0**, retained in
[generated_205C90.c](../../conker/src/game/generated_205C90.c), **8 words /32
bytes**, frame 0x18, VA 0x151D8BE0..0x151D8C00, ROM 0x206090..0x2060B0.
Retail calls func_151D8C00 with original A0 and A1=A0+0x18 in the JAL delay.
Static inventory only; recover its actual caller/return contract before C.
Wider Game matching, func_15031070 resolver and full calling/runtime/port
qualification remain open. This checkpoint does not complete the goal.
