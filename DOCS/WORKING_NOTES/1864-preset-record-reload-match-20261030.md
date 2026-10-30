# 1864: Preset record routine restored from C

Verified 2026-10-30. `func_150F5340` replaces its zero-return placeholder in
[`generated_1227F0.c`](../../conker/src/game/generated_1227F0.c). All53 body
words emit directly from semantic C, with six original relocation bindings,
the original112-byte frame and three zero alignment words. No guards,
insertions, omissions, shared-header/profile/Makefile/layout changes or
guard-manifest edits are required.

Actual linked recount: **3,941/5,506 (71.58%)** total,
**3,268/4,833 (67.62%)** Game, Init492/492, Debugger181/181 and zero drift.
The75% goal remains active: **189** more to4,130/5,506. The C inventory and
progress CSV remain unchanged.

## Recovered behavior

The routine copies17 unsigned preset words from `D_800A1AB0` into a68-byte
local aggregate. The original values atROM0x246570 are6..22; the next12 bytes
are alignment, not part of the copy. For each snapshotted value, it reloads
the live `D_800D3098` pointer and calls `func_151C970C(1, recordAddress)` with
the corresponding52-byte record address. It then calls `func_1515F170(9,1)`.
The latter helper enables matching category-nine entries. The working label
“reload” describes this wrapper; instruction execution of the helpers and
their complete downstream effects are not claimed by this qualification.

The17 preset values stay snapshotted even if a helper overwrites the original
table. Conversely, changes to the record-base pointer affect the next call.
The local byte index wraps through its ordinary u8 update; its bound is17.
Declaring that index before the aggregate and using a for loop recovers the
original local address and independent opening address/count schedule.
The earlier do/while and declaration forms differed in two scheduling words
and/or the local preset home; the selected source has zero differences.

The original prologue savesS0/S1/S2/S3 atSP20/24/28/32 andRA atSP36. Its
68-byte preset starts atSP40 (0x28), in a112-byte frame. The generated aggregate
copy uses five12-byte iterations and two final word transfers. The caller uses
no input arguments, ignores the return and explicitly replacesV0 with1.
The alternate donor's64-element array and broken pointer arithmetic were not
adopted.

## Qualification

Ignored artifacts are in `conker/build/game-preset-record-reload-match/`.

- Compiler/owner: all53 raw words and six bindings match original assembly.
  The sole-function owner has no neighboring functions or pools. All selected,
  owner and actual-Make compiler diagnostics are empty. Three actual Make
  commands reproduce the qualified padded object exactly.
- Guest:512 cases /1,536 executions cover all53 reachable words, the complete
  copy, all17 submissions and final enable. There are156 interrupted-access
  prefixes,48 cases in three independently rebased layouts and30 guest aliases.
  Cases include preset mutation, live-base changes, repeated/reordered indices,
  record writes, callback clobbers and outgoing homes. Original, raw and padded
  programs agree on complete registers, memory, access traces and calls.
- Caller: the full original-ROM aligned census finds one direct JAL at
  ROM0x5289C and no function pointers. The four-word original window at
  0x150253EC in `func_1502460C` executes32 cases per program and reaches its
  boundary at0x150265B4 withV0 overwritten by1. This is a bounded window,
  not a claim of complete VM-parent execution.
- Native32:256 cases each atO0/O2/O3 pass UBSan and nine effective controls.
  Every preset word, record-base pointer, allocated record byte and all17
  helper arguments/final-enable arguments are checked. Snapshot/live-base
  negative controls fail as intended. Private-stack aliases remain guest-only.
- Full image: production ELF equals the independent full-file prediction,
  SHA-256 `4e273ade3364aeee388ead329ba155a9302bd4bba023c07ea06303492d2db6e8`.
  Exactly167 bytes change:166 target-code bytes and one symbol-size byte.
  Metadata reorderings0, exclusions0. All6,055 other disassembled bodies,
  every function address, and189,088 protected Game bytes across720 owners
  remain fixed, including the original preset storage.
- Both tools copies pass eight fresh checks and their project-tools check.
  After production, two fresh installed checks run per copy; six unchanged
  semantic checks are explicitly reused by identical module/input/artifact
  fingerprints. The16,940-file seal verifies unchanged source and objects.

Helper effects are explicit bounded models, with caller-saved clobbers and
controlled mutations. Original helper instruction execution, complete parents
and host-port/gameplay acceptance are not claimed. The source's record address
uses the provider's existing32-bit integer parameter; native tests stay inside
allocated banks. Arbitrary guest addresses and private stack mutations do not
imply portable C guarantees.

An early private receipt copied a40-byte frame label from its template. The
correction independently decoded `27BDFF90` as112 bytes, retained the old JSON,
and updated the selected receipt before any canonical checks or installation.
Neither source nor emitted instructions changed during that metadata correction.

## Banking and continuation

Tools are committed first at **2be405f763e32f81d27a8a09041927e84c752715**, then the consumer pins that exact
commit. No push is performed. Older tools-mirror edits remain preserved.
The root README changes only its two aggregate exactness rows; detailed updates
remain here and in the documentation indexes. Graphify receives a scoped
structural refresh with old-node/relationship retention and source-validated
caller/helper edges; full-corpus re-extraction is not claimed.

Next screen **func_150B6000** from the fresh live queue. Previously deferred candidates
remain private and uncredited until their complete qualification gates pass.
