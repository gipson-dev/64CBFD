# Game Conditional Packet Allocator Direct Match

Date: 2026-10-06. Starting checkpoint: `d9973647`.

**`func_1519E6BC` matches all 38 words / 152 bytes directly from C.**
VA 0x1519E6BC..0x1519E754, ROM 0x1CBB6C..0x1CBC04, frame 0x38.
Replace the zero-return stub in
[generated_1CA420.c](../../conker/src/game/generated_1CA420.c) with a typed
single-pointer void wrapper and 12-byte packet. Add only owner-local real
structs include/allocator/copy prototypes; correct the owner-local slot extern
from integer to byte pointer. Its existing two zeroing users are unchanged.
Existing O2/g3; no new guards/profile/shared header/metadata/symbol/data edit.

## Recovered Contract

Call retained `func_1519E688` before reading `D_800E0920`. The cleanup calls
`func_1519CF70(3)`, `func_1519CF70(4)`, then `func_15147D64(NULL, 9)`.
Each byte wrapper passes a private byte to `func_15147D64` with command six.
Callback changes to the global and source byte therefore precede the gate.
If the slot is non-null, return without reading source+0x3B or allocating.

For a null slot, install the packet's zero word at +8, object pointer at +0,
then byte from source+0x3B at +4. **Bytes +5..+7 are untouched alignment
padding**, not zero-initialized fields. Retail copies all 12 bytes on success.
Allocate with typed arguments `(300, -1, 9, 0, 4, 12, 255, 0)` through
`func_151491F4`. Publish its result to the global **even when null**, overwriting
any allocator callback mutation. On success, copy the captured packet to
result+0x28. Do not reread the source byte after allocation or zero padding.

The retained allocator wrapper forwards nine arguments to `func_15149130`,
inserting signed -1 as its fourth argument. The constructor calls
`func_15167A68(35, 0, 52, 1, 255, 1)` for this fixed flag-zero invocation.
Failure returns null. Success writes halfword 300 at +0xE, bytes FF/09/FF at
+0x10/+0x11/+0x12, flags zero at +0xD and subtype four at +0x13, then clears
16 bytes at +0x14 through SDK `bzero`. Those retained routines are not edited.

Observed guest residual V0 is the input pointer on an already occupied slot,
zero on failed allocation, and memcpy's destination on success. This is not
a new meaningful integer-return API: source remains void. The existing C
caller `func_1506FC74` in `game_981E0.c` passes `D_800D154C` and ignores the
return; other caller domains are not comprehensively qualified here.

## Compiler Controls

[Driver](../../tools/experiments/game_conditional_packet_allocator_candidates.py)
screens six forms under O2/g3, O2, O1/g3 and O1: **24 controls**, isolated
diagnostics empty. Reserved-first order, an equivalent early return, and an
explicit copy-size literal all match directly under O2/g3. The installed
reserved-first body retains `sizeof(packet)` and the original nested gate.

Field-order initialization retains 38 words/frame 0x38 but differs at six
scheduling words. A separate allocation-result local produces 36 words and
32 differences. An unused pointer local changes the O2/g3 frame to 0x40,
giving eight differences despite the same 38-word body. Plain O2 has 35/37
words and 35/36 differences. O1/g3 is oversized at 39/40 words; O1 produces
38/39 words with 29/37 differences. Every exact length/frame/difference count
is bound by tests, including overflow. No guard or alternate profile needed.

Ignored receipts: `conker/build/game-conditional-packet-allocator/` and
`conker/build/game-conditional-packet-allocator-test/`.

## Qualification

[Six tests](../../tools/tests/test_game_conditional_packet_allocator_match.py)
use an independent ordered-memory reference, actual retail/selected words,
and actual selected wrapper/retained cleanup C natively:

- **3072 opaque guest cases, two bodies**: three initial slots, four code
  bytes, four source pointers, four allocation results, four cleanup mutation
  modes, two allocation mutation modes and two stack phases.
- **3072 connected-cleanup guest cases, two bodies** execute the 13-word
  cleanup and 12-word byte wrapper, with the dispatcher and allocator opaque.
- **3072 connected-allocation guest cases, two bodies** additionally execute
  the 28-word allocator wrapper and 49-word constructor. Dispatcher, backend
  allocation, SDK bzero and memcpy remain bounded callback models, not the
  complete runtime implementations.
- Compare every non-stack byte, full external read/write/call traces, all
  helper arguments and callback-entry memory snapshots, captured packet
  bytes, residual V0 and saved GPR/FPR/SP/RA restoration. Callback models
  clobber caller-saved registers. The local oracle adds signed LB handling;
  shared instruction runners are unchanged.
- **1536 extra selected-body connected cases** sweep all 256 source-byte
  values, three initial stack/storage patterns and both stack phases.
  Compare all packet bytes, including the three unchanged padding bytes.
- All **38 wrapper + 13 cleanup + 12 byte-wrapper + 28 allocator-wrapper**
  words execute. Of the constructor's 49 words, 47 execute; the two-word
  type-95 branch at +0x34/+0x38 is impossible with the fixed flags-zero
  argument. All 140 linked words are byte-bound; **138 reachable words**
  execute. This is not a general constructor flag-domain coverage claim.
- **18432 native cases** exercise all 256 code bytes, occupied/null slots,
  cleanup mutations and allocation success/failure. Actual retained cleanup
  bodies and selected wrapper C; allocator is a typed opaque callback.
  Check pointer size four, packet size 12, code +4, zero word +8, helper
  sequence/arguments, global publication, source-byte capture, initialized
  packet fields and complete object/record footprints excluding numerical
  padding values. The copy hook transports padding but does not assign it
  a portable initial value. Freestanding 32-bit GCC, warnings as errors.
- Six compiled negative controls detect the old stub, premature gate/source
  capture, copy size eight, success-only publication and zeroed padding.

Source/record/global aliases in guest cases use private sparse mapped memory.
They are ordering diagnostics, not proof that every pointer or overlap is a
valid caller. Native pointers are bounded storage. Excludes arbitrary private
stack aliases, invalid addresses, MMIO/concurrency, complete caller domains,
hardware execution and gameplay/host adoption. No FP arithmetic is added;
saved FPR checks do not establish complete FCSR behavior.

All **71 focused post-link tests pass in 369.862 seconds**, no skips:
conditional allocator, random selector/output, queue wrapper, both actor
dimension queries, projection compiler/identity audit, descriptor shape measure,
pair clamp, indexed state-save, random timer and effect-packet regressions.

## Whole Linked Audit

NON_MATCHING ELF/progress/match-progress rebuild passes. Across **6059 slots**,
only `func_1519E6BC` changes; every address and slot size remains fixed,
including both existing global-clear users despite the extern type correction.
Init, Init data, Debugger and Game data remain byte-for-byte identical.
All **720 Game-data owners / 189088 bytes** remain retail-exact; all **10646
guard rows** retain content/order. All four retained helpers match retail.
Target SHA-256:
`cbe7d270d767eb1fa0c488f28d3581fd0597af02686b1ef347d3accf74e80115`.

Baseline and current complete owners compile independently after the normal
assembly processor, **both with empty diagnostics**. The existing duplicate
generated-recipe warning remains; no project-wide warning-free claim.

| Section | Byte-Exact Converted Functions | Drift | Different |
| --- | --- | --- | --- |
| Total | 3319 / 5462 (60.77%) | 0 | 2143 |
| Game | 2646 / 4789 (55.25%) | 0 | 2143 |
| Init | 492 / 492 (100%) | 0 | 0 |
| Debugger | 181 / 181 (100%) | 0 | 0 |

Converted counts/bytes unchanged: the old stub already counted as C.
README changes only aggregate counts. No sibling source/build/save/frozen
Release change or push. Root tools-check and Python compile checks pass.
`git diff --check` passes; 3232 relative links across 24 documents, zero broken.

## Next Work

Inspect `func_1519E970`, still a stub in `game/generated_1CBE20.c`:
37 retail words, ROM 0x1CBE20, frame 0x20. Seven incoming arguments; allocator
call `func_15167A68(38, context, 44, 1, channel, 1)`. Null returns null;
success stores two pointers, signed halfword, byte, flags one, zero word and
a final pointer at offsets +0x18/+0x1C/+0x20/+0x28/+0x10/+0x14/+0x24.
Recover argument widths, allocation capture and ordered overlapping outputs.
The retail caller in [50D80.s](../../conker/asm/50D80.s), ROM 0x55A18..0x55A74,
passes table-record+0x30 and table-record+0x20 as the two payload addresses,
then installs the returned record at owner+0x30. Their pointee types and all
caller domains still need qualification; this is pointer transport evidence,
not a float-value argument assumption based on word stores alone.
This is static inspection, not a completed recovery. Projection/pair-clamp
frames remain open; the broad Game matching goal stays active.
