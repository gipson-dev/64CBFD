# Private record resource-cache recovery

Date: 2026-11-14. The complete private C draft of `func_15016850` now
recovers the cache builder's **84-word length**, **0x60 frame** and persistent
loader-output home at **SP+0x50**. Guest/native/caller-window qualification
passes, but the draft still differs in **76 real word positions** and uses
an extra saved S7. **No production installation, new guards or matching
credit.** The 85% goal remains active at **4,495 / 5,515 (81.50%)**, Game
**3,822 / 4,842 (78.93%)**, zero drift; **193 more matches** are needed.

Owner `conker/src/game/generated_43D00.c`, original
`conker/asm/43D00.s`; VA **0x15016850..0x150169A0**, ROM
**0x43D00..0x43E50**, **336 bytes**. Baseline consumer
`d2ce800bdb973be796f15857c6ae3f1ac7879948`, tools
`ad71ba49ede0c0a8f11085b8ba37b743cf620cb9`. Production owner remains
**0 / 3 exact**; all three functions remain placeholders.

## Recovered contract

The routine clears byte `D_800BE590`, then scans the +4 resource byte in each
**0x30-byte record** through `D_800D20FC`, bounded by byte `D_800D2100`.
It searches the accumulated **unsigned halfword IDs** at `D_800BE598` before
loading a new resource. IDs below **0xBB** call
`func_1502B7F0(&handle, 2, 18, resource)`, using the existing variadic helper
prototype's output-pointer contract. The helper return register is ignored;
the retained output pointer controls whether an entry is appended.

The handle is initialized **once before the loop**, not on each record. An
ID at or above 0xBB skips the loader and can append the previous handle. A
loader that leaves the output untouched also preserves that handle. A null
output skips insertion. Appending writes the pointer at `D_800BE5A8` first,
the halfword ID second, then increments the byte cache count. The native and
guest negative controls retain these distinctions.

The input table pointer and record count are live across loader calls. Retail
reloads them after the opaque helper; the resource byte itself is captured
before the call. Duplicate detection compares the full halfword, even when
provider mutations leave values above 255. The model does not silently narrow
those stored IDs.

The private view deliberately uses byte addressing for the 0x30-byte records.
The existing `struct258` declaration is a shorter prefix; settle the shared
pointer/view declaration before production adoption. No shared header or
neighboring source is changed for this screen.

## Source and layout boundary

The initial byte-offset `for` form emits 85 words and hoists the scaled loop
extent before the empty-list test. A guarded `do/while` form recovers the
original initial byte-count test, 84 words and the real handle home. Placing
the handle declaration after `offset, index, found` recovers SP+0x50 without
dummy locals or frame guards. Both raw neighboring functions, normalized
owner pools and compiler diagnostics remain unchanged.

The selected raw draft has **15 binding sites**, SHA-256
`f28750b1a5927c6c37fb2d5a643f8ee343d7d001649b4d81f16871ce4b062f67`.
The live Make dry run confirms the existing **O2/g3/mips2/o32** owner profile.
The draft keeps literal 48 in S7 and uses `multu` for the loop extent; retail
uses a shift/subtract sequence and saves only S0..S6. Thus matching length,
frame and handle home are insufficient for adoption.

| Saved home | Private draft | Retail |
| --- | ---: | ---: |
| S0 | SP+0x14 | SP+0x18 |
| S1 | SP+0x18 | SP+0x1C |
| S2 | SP+0x1C | SP+0x20 |
| S3 | SP+0x20 | SP+0x24 |
| S4 | SP+0x24 | SP+0x28 |
| S5 | SP+0x28 | SP+0x2C |
| S6 | SP+0x2C | SP+0x30 |
| S7 | SP+0x30 | Not saved or used |
| RA | SP+0x34 | SP+0x34 |
| Loader output | SP+0x50 | SP+0x50 |

Other logical-index, explicit-limit and branch-local limit shapes remain
ignored experiments. Disabling unrolling does not improve the selected draft.
`-Wo,-no_const_in_reg` shortens it to 70 words/frame0x48 and loses the required
layout; no profile or Makefile change is adopted. An exploratory compiler
profile helper first rejected the extra flag at asm-processor argument parsing;
the corrected private probe keeps preprocessing at O2/g3 and passes the extra
option only to IDO. Rejected probe output is not qualification evidence.

## Completed private qualification

- [x] **1,440 guest cases**, two streams, compare the independent model with
  retail and emitted C. All **84 retail words** are visited. Complete public
  memory, helper packets and byte-for-byte helper-entry snapshots include
  **1,280 cache bytes**, both record tables and both live globals.
- [x] Every one of the **256 record-count byte values**, duplicates, empty
  lists, IDs 186/187/255 and non-writing/null/writing output responses are
  included. The larger guest cache backing preserves actual table overlap:
  IDs start at cache+8 and pointers at cache+24. It does not model them as
  unrelated arrays when larger byte indices overlap those regions.
- [x] **32 guest record/cache alias cases**, two stack phases and all sixteen
  combinations of live count, table-pointer, cache-count/ID and input-byte
  mutations pass. No full private-stack or raw fault-order equivalence is
  claimed; saved-register layout still differs as shown above.
- [x] Three emitted controls reject a changed initial handle store, saved-S1
  corruption and a changed resource argument in the actual JAL delay slot.
  Each control checks its exact original word before mutation. The saved
  register control is rejected by the original return-ABI check.
- [x] **576 native32 cases per O0/O2/O3**, with explicitly asserted
  undefined-behavior trap flags, compare the complete **1,280-byte cache** and
  **768 record bytes**, final count/table selection, complete loader packets
  and loader-entry observations. Numeric halfword/pointer fields are converted
  between guest and host endianness; all padding/tail bytes are checked too.
  GNU symbol aliases provide the real cache field offsets; memory barriers
  keep those aliases visible across the native provider boundary.
- [x] Native storage is bounded to **eight cache entries / eight records**.
  Guest full-byte-count and overlapping-record cases are not presented as a
  native capacity or portable alias guarantee. Six effective C controls reject
  per-iteration handle reset, threshold inclusion, ID narrowing, lost count
  increments, cached table pointer and cached record count.
- [x] The aligned input census finds one direct call, ROM **0x4451C** / VA
  **0x1501706C**, and no literal function pointer. The authentic JAL/NOP window
  passes **64 cases per stream**, with public memory, loader packets, full
  helper-entry observations, saved registers, SP and saved FPRs checked.
  The full parent and its eventual return contract remain unqualified.
- [x] The mounted focused suite passes in **39.008 s**. Its native flag
  assertion is then re-executed at all three profiles. The isolated sibling
  suite passes in **45.397 s**, with all five task files copied byte-identically into
  an ignored overlay and no sibling source overwritten.

Reproduce on the prepared consumer:

```sh
PYTHONPATH=. CBFD_CONSUMER_ROOT=. python3 -m unittest tools.tests.test_game_resource_cache_15016850_recovery -v
```

All **812 frozen production inputs**, including **82 headers / 698 objects**,
remain exact. The production ELF stays
`0619dc2bfb3ed16c4fb1e520115f9742323fcd2f16460caf5fcde396ca96d7ad`;
the prior actual-ELF recount and README figures therefore remain applicable.
The source, guard CSV, conversion rows, Makefile and live objects are untouched.
The Note 2454 `make tools-check` receipt is reused for unchanged shared tools,
not reported as a fresh broad suite.

Sibling HEAD remains `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`, with all
**2,439 dirty paths** and status SHA-256
`a3b1d31058efd5c8483ee15ece0d00b39f54bdfce5b08a8c64838636db14e0fb`
preserved. Scoped Graphify AST merge covers five tools files, retaining all
**61,102 old IDs**, zero loss: **61,128 nodes / 114,852 links**, zero LLM
tokens. This is not full-corpus re-extraction. Routine Claude calls: zero.
Tools commit `3c8921bd6b33ce38f47ca5df41b1f4baa2b2633d` precedes the consumer documentation/pin
commit. No push; host Release remains frozen.

## Resume point

Continue the same function. Recover the seven-register save lifetime and
retail shift/subtract bound calculation before deriving any normalization.
Keep the retained-handle, full-halfword and live-provider regression controls.
Then qualify exact CFG/roles/private homes, both padders, independent rebases,
actual Make, strict whole-image prediction, production adoption and recount.
The current 812-input frozen snapshot is retained under
`conker/build/game-resource-cache-15016850-match/`; do not advance it merely
to accommodate unrelated changes. The separate common particle updater
remains private at [Note 2452](2452-game-common-particle-frame-native-and-callers-20261114.md).
