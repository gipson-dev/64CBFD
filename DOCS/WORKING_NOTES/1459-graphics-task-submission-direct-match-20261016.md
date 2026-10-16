# Graphics Task Submission Direct Match

Date: 2026-10-16. Consumer predecessor **2eea677e**, tools predecessor
**34c77ae**. Continue the target queued in
[Note 1458](1458-viewport-initializer-direct-match-20261016.md).

## Recovered Contract

func_1501C880 in conker/src/game/generated_49D30.c emits **239 words / 956
bytes directly from C**, VA **0x1501C880..0x1501CC3C**, ROM
**0x49D30..0x4A0EC**. Retain the existing **O2/g3/no-unroll profile**, original
**0x28 frame**, S0/RA homes and cached row capacity at **SP+0x24**. No new
instruction guards, padding or private pools.

```c
void func_1501C880(s32 unused, s32 swapBuffers);
```

Use the existing SDK **OSScTask**, OSTask, OSScMsg and Gfx types and real
graphics macros rather than importing opaque word-field assignments:

- Compute the signed command capacity from the wrapping 32-bit row-address
  difference, before selecting the page's 0x60-byte task record. Clear only
  its next pointer; preserve all untouched state, padding and task fields.
- Validate the current command count. An out-of-range cursor calls the real
  two-row initializer and emits full sync/end commands at its published end.
  A second check reserves **400 commands**, with ordered sync/end stores and
  a fresh row-base load. Keep the original cached capacity across callbacks.
- Publish the command pointer and eight-byte-rounded byte count, then call
  func_1501CC3C with no interpreted arguments or return value. Its unrecovered
  legacy s32 declaration is retained until the provider is restored.
- Populate the boot/selected microcode, stack, output and yield fields in
  their original order. Use **OS_TASK_LOADABLE (4)**, not OS_TASK_DP_WAIT (2),
  and the SDK data/yield sizes. Do not initialize the untouched ucode_size.
- Set RSP/RDP/last-task flags, optional swap and dirty-view bits. The swap
  flag is a **full word**, and view-count addition/shift uses unsigned word
  arithmetic. Clear the dirty byte only on that branch.
- Publish the queue/message/framebuffer pointers, flush cache, submit with
  **OS_MESG_BLOCK**, optionally XOR the live page with one, and increment the
  live signed-halfword counter with retail's narrowing behavior.

The alternate-source game_49D30.c, SHA-256
**de86733aea5f3ec2399ae312d9d38dc1ad324be04d6568b4c75b82dec007356d**,
has an auto-decompiled non-matching draft. Its address roles help navigation,
but some typed pointer expressions scale offsets twice. It is not imported
or credited as byte-exact C. The source archive remains read-only; this is an
independently compiled SDK/retail recovery.

## Source Fit And Caller Cleanup

The first complete typed source is **238 words / frame 0x28 / 184
differences**. Naming the real remaining-capacity value restores retail's
fallback arithmetic/address sequence and yields **239 / 0x28 / 22**.
Reading capacity before task selection recovers the opening load schedule
and temporary allocation: **239 / 0x28 / zero differences**. Moving it only
before the next-pointer clear still leaves 20 differences; a named byte-span
carrier changes the frame to 0x48 and is rejected. No frame/home guards.

Final raw object SHA-256:
**c59f51258bcc79b0ba9e4c28f4b1559e366f4cf01f2bf8d7fc6144d34a251ad2**.
Pin all **64 relocation bindings**. All **56 no-unroll owner neighbors**
retain literal raw words/bindings.

Correct the actual frame driver's prototype to void and reverse its
equivalent byte comparison operand order. Nine post-call V0/V1 words now
emit their old guarded replacements directly. Remove exactly those nine
obsolete func_1501878C guards, with no new guards or other CSV-byte changes:
**0x558, 0x55C, 0x568, 0x588, 0x58C, 0x590, 0x598, 0x59C, 0x5B0**.
The comparison reversal also preserves the old commutative branch word at
0x5A8, so no replacement guard is needed there.

Caller raw SHA changes only from
**891ed2b97a7d62cd4862c65ce530b933b33f3ebd8858baafd7df5dc0e5f3b178** to
**a829527cf77c7e22c8d5f7a9f0c7c35854ffedffdc01a8d797677849cdc743e3**.
The complete binding-map fingerprint stays identical. Fifteen other raw
caller functions and **all sixteen normally padded caller functions** stay
identical. Four pre-existing caller Warning 712 messages are identical after
normalizing only the scratch filename; they were not fixed or suppressed.
The guard CSV's **298 CRLF lines** are preserved, not silently normalized.

## Qualification

All **nine pre-installation tests pass in 83.785s**. After installation and
the normal dependency rebuild, all **12 final tests pass in 92.616s**:

```sh
python3 -m unittest tools.tests.test_game_graphics_task_submit \
  tools.tests.test_game_graphics_task_submit_native \
  tools.tests.test_game_graphics_task_submit_installed -v
python3 -m tools.experiments.game_graphics_task_submit --prelink
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- **1,656 three-way guest cases** compare the independent ordered
  reference, full literal RAM/GPR/FPR banks, calls/events, accesses and delay
  state. All **239 root words** execute. Exercise normal and negative/small
  capacities, inclusive boundaries, unaligned byte counts, both pages,
  full-word swap flags, view-count overflow and counter wrap.
- **72 three-way positive callback cases** cover live page/task/program/view/counter changes
  and the capacity cached across a row-table mutation. Separate guest-only
  tests add **12 three-way cases** with initial high pages 128/255 and wrapping
  32-bit command addresses.
- **864 native32 cases each at O2 and O0**, UBSan and no fwrapv, use separate
  typed caller/body/provider units and the actual two-row C emitter. Explicit
  eight-byte SDK alignment proves **OSScTask size 96, list offset 24, msgQ 88,
  msg 92, OSScMsg 32 and Gfx 8**. Compare all **10,761 public words and
  canaries**, with endian normalization by known lanes and only explicitly
  declared pointer fields. No arbitrary data is treated as a pointer.
- Six native controls return actual output/protocol mismatches: no page
  flip, 399-command reserve, inclusive reset, halfword swap flag, reloaded
  rather than cached capacity, and a cached task pointer. Compiler failures,
  sanitizer traps, signals and unmapped accesses never count as controls.
- Execute all **61 real two-row helper words**, verified against frozen
  ELF/ROM, with **1,136 fired three-way connected memory-fault prefixes**.
  These are literal instruction-cut states, not hardware exception behavior.
- GNU-assemble the complete original **239-word root and 412-word caller**.
  **16 actual caller cuts** check A0 zero, delay-slot A1 one, the real post-call
  flag load and byte clear. Do not infer a complete frame-loop execution.
- Three original GNU and three independently linked C rebases compare all
  239 words with HI/LO carries. Reject every raw word, all 64 bindings plus
  an extra, private pools, stale source/caller anchors and **81** retired-
  guard field corruptions.

Cache, blocking queue and microcode-loader providers remain explicitly bounded.
Callback mutations are contracts, not natural runtime observations. No RCP,
cache-coherency, scheduler, gameplay, host-port or frozen Release acceptance.
Zero Claude calls: compiler, SDK, retail and local tests settle this routine.

## First Image Prediction

Reproduce the predecessor independently, then predict every **3,257,636 ELF
bytes** before installation. Exactly **800 bytes** change: **731 code bytes**,
**two size bytes** for extent **12 -> 956**, and **67 metadata bytes**.
Constrain exactly three symbol/string permutations with unchanged named
definitions: D_800BEAD8/D_800BE9F8, D_800BEAD4/D_800BE9F4 and the three-record
D_800CBE10/D_800A0758/.L15028860_game_data cycle. No metadata exclusions.

First predicted ELF SHA-256:
**5ae0082dd77652314c8e63569a43439a330d133b749907fa5db2d5b76fe41d9e**.
Source owner:
**3e02c9bf76ce42ee32ab9ea3be3783175a6e82472d08818797e166496c6d899d**.
Caller owner:
**de6b587a3966b174777e1d038378db6da3a918e77ba4151a3d54058185d6a012**.
Guard CSV:
**51b90c3096acac693bec4d4bd249154d8429c8d2045cb767c02e87318b280bb7**.

## Installation Gates

- [x] Install only the qualified source, caller comparison/prototype and nine guard removals; all three working files equal the first prediction.
- [x] Finish the normal dependency rebuild and require the entire ELF to equal the first prediction. All 695 compiler invocations / 687 padder invocations complete; existing warnings remain, not a warning-free build claim.
- [x] Pass all 12 final focused/installed tests, all 134 input gates, exact successor/corruption checks and protected data audit.
- [x] Measure official progress and update root README aggregate rows only.
- [x] Bank tools first, then the consumer pin/docs, preserving the older dirty tools mirror; no push.

The entire normal ELF equals the first predicted SHA above, with all **130
other inputs unchanged**. The Makefile stays identical and all non-retired
guard bytes stay identical. Protected data remains **189,088 bytes / 720
owners / zero differences**. Installed source/caller/guard/helper/image/
metadata corruptions and both fixture stages reject unknown successors.

Fresh official matching: Game **2,936/4,828 (60.81%)**, total **3,609/5,501
(65.61%)**, still different **1,892**, zero drift. Init stays **492/492**,
Debugger **181/181**. Fresh conversion rows remain **5,501/6,044 functions /
86.04% bytes**; the old stub already counted as C.

Tools **44ac318be4bed48bb542e9e7c6c00516cfa0fc56** banks all seven files
before the consumer pin. Both copies pass seven Windows AST checks and eleven
shared padder tests: active **0.030s + 0.023s**, older mirror **0.030s + 0.019s**.
Consumer tools-check passes. Preserve older mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **921** initial dirty-file
hashes and **928** final dirty paths. All seven task-file pairs match; do not
commit/reset that mirror. No push, host-port change or frozen Release action.

Next: **func_1501CC3C**, still a zero-return stub in the same owner:
**97 words / 388 bytes / frame 0x30**, VA **0x1501CC3C..0x1501CDC0**, ROM
**0x4A0EC..0x4A270**. Recover its microcode selection, four DMA loads and
live data-pointer publication. Qualify the provider interface and this already
matched caller again instead of assuming a prototype change is neutral.
Keep timing's **141 differences**, wider Game/additional-source work and full
gameplay acceptance separately open.
