# Game Address Record Allocator Direct Match

Date: 2026-10-06. Starting checkpoint: `83645ca5`.

**`func_1519E970` matches all 37 words / 148 bytes directly from C.**
VA 0x1519E970..0x1519EA04, ROM 0x1CBE20..0x1CBEB4, frame 0x20.
Replace the false zero-return stub in
[generated_1CBE20.c](../../conker/src/game/generated_1CBE20.c) with a typed
seven-argument pointer-returning allocator and local 44-byte record view.
Add only the accurately typed owner-local allocator prototype. Existing
O2/g3; no new guards/profile/shared header/symbol/metadata/data edits.

## Recovered Contract

Arguments: signed 16-bit lifetime, owner pointer, unsigned byte mode,
two payload addresses, unsigned byte channel, and signed 32-bit context.
Call retained `func_15167A68(38, context, 44, 1, channel, 1)`.
On null allocation, return null without record stores. Success stores:
first address +0x18, second +0x1C, lifetime halfword +0x20, mode byte +0x28,
flags word one +0x10, state word zero +0x14, owner pointer +0x24, then returns
the allocated record. Header and alignment bytes outside these stores remain
owned by the allocator or untouched; do not zero them in the wrapper.

The typed source assigns owner before flags/state. IDO's existing scheduling
then emits the retail load and late owner store exactly. Assigning owner last
in source produces six different words despite the correct frame/body length.
This is source-shape recovery, not instruction patching. Native qualification
checks ordinary-memory values/footprints, not a portable host instruction order.

The retained 28-word allocator calls Init heap allocation with
`func_10003C6C(44, 1, 1, 0, 1)`. Success writes context's low byte at +1,
calls `func_15168A4C(record, 38)`, then writes channel at +0xC.
The 20-word list inserter reads the fresh row byte and head at
`D_800DCE50 + row*0x1A0 + 38*4`; it writes the old head into node+8, sets a
non-null head's previous pointer to node, writes index 38 at +0, clears node's
previous pointer at +4, then publishes node as the list head. These routines
and the underlying Init heap implementation are not edited.

The retail caller in [50D80.s](../../conker/asm/50D80.s), ROM 0x55A18..0x55A74,
passes table-record+0x30 and +0x20 addresses, owner from its current record,
mode zero and context zero, then installs the returned pointer at owner+0x30.
This confirms pointer transport and a meaningful pointer return. Payload
pointee formats and full caller execution remain outside this checkpoint.

## Compiler Controls

[Driver](../../tools/experiments/game_address_record_allocator_candidates.py)
screens **12 forms / four profiles = 48 controls**, isolated diagnostics empty.
Owner-before-flags and its equivalent byte-view mode form match directly under
O2/g3. The fully typed owner-before-flags form is installed. The initial
owner-last form, raw fields, explicit size and register-result controls retain
37 words/frame 0x20 but have six differences. Byte-view mode alone does not
fix those six words. Wide lifetime/mode/channel each introduces an additional
argument-home load difference; flags-first has 14 differences.

The nested-success form has 35 words/20 differences under O2/g3. Plain O2
has 35/37 words and 10..30 differences, never exact. O1/g3 and O1 overflow
at 40/43/46 words, with frames 0x28 or 0x30. Tests bind every exact length,
frame and difference count, including oversized tails. No guard or profile
change is needed.

Ignored receipts: `conker/build/game-address-record-allocator/` and
`conker/build/game-address-record-allocator-test/`.

## Qualification

[Six tests](../../tools/tests/test_game_address_record_allocator_match.py)
compare selected/retail words with an independent ordered-memory reference:

- **1152 opaque guest cases, two bodies**: eight argument bundles spanning
  signed-halfword and raw-pointer boundaries/high bits, six context patterns,
  success/failure, three existing head states, callback mutations and two
  stack phases. Capture complete allocator arguments and callback-entry bytes.
- **1152 connected-allocator guest cases, two bodies** additionally execute
  the retained 28-word allocator. Heap and list insertion are bounded models.
- **1152 fully connected guest cases, two bodies** execute allocator and actual
  20-word list inserter. Heap remains a bounded callback. Verify null, old-head
  and self-head linking, fresh row-byte reads and the post-insertion channel.
- Compare every non-stack byte, full external read/write/call traces,
  callback-entry snapshots, pointer return and saved GPR/FPR/SP/RA lifetimes.
  Callback models clobber caller-saved registers and can change source bytes,
  current head and destination fields before initialization. Shared guest
  runners are unchanged; all **37 + 28 + 20 = 85 words** execute.
- **65536 extra selected-body fully connected cases** cover every lifetime
  halfword and every mode/channel byte pair, with unrelated high bits in all
  three incoming argument words. Vary both stack phases, pointer patterns,
  valid row zero/one, head state and heap mutations. Every halfword is stored
  on a successful allocation; this is not just an input sweep through failure.
- **131072 native cases** execute every halfword/mode/channel pair once with
  success and once with failure. Actual selected wrapper, retained allocator
  and list-inserter C; heap is a typed callback. Check record size 44,
  pointer size four, field offsets and actual 12-byte ListNode layout. Compare
  both 128-byte record buffers, old-head buffer, all 832 table bytes and source
  bytes, including untouched header/alignment/canary bytes.
- The native fixture adds one explicit `u8 *` cast to the retained allocator's
  Init heap call: the actual Init API returns a 32-bit integer address. The
  cast preserves that ABI under the checked 32-bit host compiler and allows
  warnings-as-errors; no production helper change or 64-bit host claim.
- Six compiled negative controls detect the stub, size 0x28, flags zero,
  wrong second pointer, incremented lifetime and incremented channel.

`variables.h` declares the head table as two 0x1A0-byte rows. Guest context
patterns with low byte 255 are **sparse mapped diagnostics**, not claims of
valid table indexes or portable out-of-bounds C. Native full context words
have low byte zero/one. Self-head states are alias/order diagnostics, not a
claim of a valid allocation into an already occupied node. Pointer bit patterns
are stored without dereference. Excludes arbitrary private-stack aliases,
invalid-memory access, MMIO/concurrency, all caller domains, hardware execution
and gameplay/host adoption. No FP arithmetic is introduced; FPR lifetime checks
do not establish complete FCSR behavior.

All **77 focused post-link tests pass in 468.864 seconds, no skips**. The suite
includes the allocator, conditional packet, RNG/selector, actor queue and both
dimension wrappers, projection audit, shape volume, pair clamp, indexed state,
random reload timer and effect packet tests. All new compiler controls and the
expanded 131072-case native fixture pass.

## Whole Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. Across **6059 slots**,
only `func_1519E970` changes; all addresses and slot sizes remain fixed.
Init, Init data, Debugger and Game data remain byte-for-byte identical.
All **720 Game-data owners / 189088 bytes** remain retail-exact; all **10646
guard rows** retain content/order. Both retained helpers match retail.
Target SHA-256:
`a554b21b6d9a18bcdb644e3a36d882ec0201774ef2f1796dced5ec12c00c0f59`.

Baseline and current complete owners compile independently after the normal
assembly processor, **both with empty diagnostics**. The existing duplicate
generated-recipe warning remains; no project-wide warning-free claim.

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3320 / 5462 (60.78%) | 0 | 2142 |
| Game | 2647 / 4789 (55.27%) | 0 | 2142 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes unchanged: the stub already counted as C. README
changes only aggregates. Root tools-check, Python compile checks and diff-check
pass. All **3244 relative links across 25 documents** resolve, zero broken.
No sibling source/build/save/frozen Release change or push.

## Next Work

Inspect `func_1519EA78`, still a stub in this owner: 69 retail words,
ROM 0x1CBF28, frame 0x70. Five incoming arguments; the third arrives as float
bits in A2. Capture three source words, unsigned-halfword selector, byte
channel and context, then submit a complete 60-byte configuration packet and
two scalar addresses to `func_15152190`. Recover exact layout/constants and
pointer/float ABI before installation. This is static inspection, not a new
recovery or runtime acceptance claim. Projection/pair-clamp frame work remains
open; the broad Game matching goal stays active.
