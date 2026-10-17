# Game Link Event Callback Match

Date: 2026-10-17

Continue consumer **a41b7711**, tools **e537123**, from
[Note 1488](1488-transition-burst-real-object-layout-and-guarded-match-20261017.md).
Recover **func_150CF484**, VA **150CF484..150CF530**, ROM **FC934..FC9E0**,
**172 bytes / 43 words / frame 0x18**, in generated_FC5F0.c. The complete
semantic C needs one expected-word guard for commutative branch operand order;
this is not a direct raw-compiler match or completion of the wider Game goal.

## Recovered Interface And Body

The retail pointer is entry **43** of **D_8008A8D8**, at **8008A984**. The
complete 23-word dispatcher **func_15149434** passes record, packet and a
low-byte event, ignores the callback return and restores its own frame. Use
**void(u8 *, u8 *, u8)**, not the zero-return placeholder's invented s32 result.
The removal provider **func_1516972C** takes one record pointer, not the three
incidental argument registers shown by the alternate auto-decompiled source.

Recover the word-plus-byte **LinkStateFC5F0** at record+0x28. Event zero calls
the removal provider when the first packet word matches the link value or,
only after that word comparison fails, the two identity bytes match. Read the
link byte before the packet byte. Event **0x2D** replaces either matching link
endpoint with the other packet word and its byte at packet+9 or packet+8.
Preserve the cached first word and read the replacement byte **after** the
word store: overlapping packet/link storage makes this observable. Other
events perform no record or packet loads in the emitted instructions.

The two event packet layouts are intentionally not conflated into one guessed
common struct: event-zero packet+4 is a byte, while event-0x2D packet+4 is a
word. Retain the address-based function name and a narrow descriptive comment.
No alternate-source code, speculative symbolic renaming or broad owner cleanup.

A single common link-pointer definition recovers the original pointer lifetime
and all 43 words apart from instruction **34**, offset **0x88**:
**548A0005 -> 55440005**. Decode both BNE-likely words: identical opcode,
destination, delay behavior and immediate; the equality operands A0/T2 are
swapped. The guard does not change an offset, memory access, argument, saved
register, instruction count or control-flow destination. Existing burst and
child guards and the D_800A0860 constant mapping remain unchanged.

Raw target SHA-256:
`4d9d64e0a3911e4a931a63b7ad418cb8f237dbe1f8e305038ec0586129dc49ec`.
The only binding is **R_MIPS_26 func_1516972C at +0x44**. All **24 raw/padded
owner neighbors** and all owner data/constant-pool bytes remain unchanged.

## Focused Qualification

- **6,912 three-way original/raw/guarded cases**, complete modeled memory,
  final registers, calls and ordered instruction memory accesses. Cover high
  event bits, signed word patterns, short circuiting, eight packet/link alias
  placements, both stack phases and a clobbering/mutating scripted removal
  provider. All **42 naturally reachable words** execute. Word 33 is retail's
  unreachable duplicate load; all 43 words still require literal identity.
- **406 three-way fault prefixes / 1,218 positively fired instances**, across
  20 actual faulting instruction addresses. Check complete prefix state and IO;
  do not infer portable C exception semantics from this emitted-MIPS model.
- **Nine independent original/raw/padded links**, three entry/helper address
  sets and **108 three-way cases**, with the actual R_MIPS_26 binding executed.
  Enforce four-byte input-section alignment rather than silently shifting entry.
- The **complete actual 23-word dispatcher**, **120 three-way cases**, real
  table slot and ignored return contract, including null slots and index bounds.
- Prepared native32 **O2/O0 + UBSan**, **288 disjoint typed cases per profile**,
  separate complete body/caller translation units, and **six effective controls**.
  Align the freestanding test entry's stack correctly. The emitted guest tests,
  not little-endian native tests, qualify aliases and big-endian access order.
- **Two real IDO big-endian negative bodies** positively detect widening the
  event and identity-byte comparisons. All **43 raw-word**, one binding and
  one actual expected-word padder corruption controls reject changed inputs.
- **202 protected entries / 185 distinct paths / 404 live/frozen corruption
  controls**. Historical stages stay immutable; only an exact approved latest
  successor may normalize to its verified predecessor fixtures.

The first test run exposed fixture mistakes: section addresses are not object
file offsets; the independent link needs SUBALIGN(4); word 33 is unreachable;
and the native _start needs stack realignment and the actual 288-case count.
Correct those fixtures without weakening the complete word/input/behavior
gates. The scripted removal provider is not the real destructor graph, and no
N64 hardware, MMU/CP0/FCSR, renderer or gameplay acceptance is claimed.

## First Complete Prediction

Before any production edit, reproduce the entire normal predecessor ELF and
predict the full successor: **119 changed bytes = 118 code + one symbol-size
byte**. Zero metadata differences, symbol permutations or exclusions. Source,
manifest and the two-line old-checkpoint adapter are also predicted exactly.

Expected normal ELF SHA-256:
`20b597fa44e3ebe08ddbd7b90346b56df821d3e3ca7cb4733da7e74ee8ee56d8`.
Owner source:
`3caade2a56d289fddc2d49bc85c9b529352dc9bceb3dd0af172955f2517704a9`.
Guard manifest:
`b520ef277d609c277857af840c8f0a1ac4b668abb76146a7d58b4b65e13fd083`.
Old burst checkpoint adapter:
`6284b53fdccac9b2f127ad9faf95eb7d3f5bd810c424b4727992cc360eb0cc60`.

- [x] Recover and qualify the complete semantic callback and narrow guard.
- [x] Freeze the first complete independent prediction before source edits.
- [x] Verify normal rebuild, installed suite, all data and matching progress.
- [x] Bank tools first, then consumer source/guard/docs/pin; wider Game stays open.

No Claude calls, provider/account/dependency changes, host-port or frozen
Release action, push, mirror reset or unrelated cleanup. The user confirmed
the earlier truncated-path compiler scratch file was disposable; no recovery
is needed. Compiler output paths remain separate, quoted arguments.

## Installed Bank

The normal build exits zero and all four installed artifacts equal the first
frozen prediction before strict after fixtures are created. All **nine
installed tests pass in 20.308s**, without skips, including the entire-image
gate and **twelve positively fired checkpoint controls**. Four selected
burst/child emission and guest-behavior checks pass in **33.305s**, after the
new checkpoint exists; the earlier pre-checkpoint attempt ran zero tests and
is not counted. The previous full burst/child suite receipts remain historical,
not newly run broad-suite claims. All target and prior-stage inputs re-freeze.

Game-data audit: **189,088 bytes / 720 owners / zero differing bytes or
owners**, retaining SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
The exact whole-image prediction preserves every other linked function body,
address and extent. The regenerated progress CSV is unchanged; this replaces
an existing C stub, so nominal conversion rows do not increase.

Fresh official matching: Game **2,953/4,828 (61.16%)**, total **3,626/5,501
(65.92%)**, **1,875** different, zero drift. Init **492/492** and Debugger
**181/181** remain exact. Root README changes only its two aggregate rows.
The rebuild retains pre-existing duplicate generated_12D630 recipe/compiler
warnings; no broad warning cleanup or line-ending normalization is included.

Tools **fed3c57** banks the four new qualification files and two-line old
checkpoint adapter first. Eleven shared tests pass in the active checkout
(0.055s) and mirror (six in 0.034s, five in 0.020s); tools-check and all ten
ASCII/AST parses pass. Five task-file pairs are identical. Mirror HEAD stays
**ddbdd16b**; preserve all **1,071 unrelated initial dirty hashes**, yielding
**1,076 dirty paths** after four new task files and the approved predecessor
edit. No mirror commit, reset or push.

Next: **func_150D01A0**, VA **150D01A0..150D02B4**, ROM **FD650..FD764**,
**69 words / frame 0x30**, still a zero-return stub in the same owner. Recover
its signed countdown byte, modulo-byte crossfade weights, live buffer index
and renderer-call lifetimes before considering matching credit. Wider Game
and real destructor/rendering/gameplay acceptance remain open.

Prepared-checkout commands:

```sh
python3 -m tools.experiments.game_link_event_callback
python3 -m tools.experiments.game_link_event_installation
python3 -m unittest tools.tests.test_game_link_event_callback -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
