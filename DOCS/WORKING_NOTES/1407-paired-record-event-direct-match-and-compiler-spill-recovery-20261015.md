# Paired Record Event Direct Match And Compiler Spill Recovery

Date: 2026-10-15

## Result

Replace **func_1516F548**'s zero-return placeholder in
[`generated_19A8B0.c`](../../conker/src/game/generated_19A8B0.c) with semantic
C. All **199 words / 796 bytes** match retail directly, both raw and through
the real production padder. VA `0x1516F548`, ROM `0x19C9F8`, frame **0xF8**,
RA SP+`0xCC`. **No target guards, profile changes, inline assembly, padding
locals, shared-header edits or broad factory-interface changes.**

This finishes the compiler/private-home gap recorded in
[Note 1406](1406-paired-record-event-abi-and-candidate-rejection-20261015.md).
Preserve that note's 33 failed forms and immutable captures as historical
evidence, rather than rewriting the earlier results as successes.

## Compiler Evidence

Adapt the existing hash-gated native compiler observer to this exact target.
Each diagnostic first proves its isolated raw function/relocations equal the
complete-owner compilation, then follows the prepared compiler's own CFE,
UOPT, UGEN, assembler and driver processes through actual successful exits.
Capture and hash the producer Ucode before its consumer executes; decode
through the live compiler's opcode/type tables. All four compiler binary
fingerprints remain fixed before/after each observation.

| Source Form | CFE M Reservation | UOPT M Reservation | UGEN Locals | Final Frame |
| --- | --- | --- | --- | --- |
| Indexed saved reads / first-packet inputs | 48 | 40 | 40 | `0xF8` |
| Ordinary reads / short shift temporaries | 44 | 72 | 72 | `0x118` |
| Initial indexed form | 48 | 40 | 40 | `0xF8` |
| Repeated narrowed expressions | **No M definition** | **40** | **40** | **`0xF8`** |

UGEN's observed frame sequence is `0 -> 8 -> 208 -> final`: **8 saved bytes,
200 outgoing bytes, then the reported local reservation**. Its temporary
pool stays empty and contributes zero bytes. The extra ordinary-local frame
space is already present in UOPT's output, not a late UGEN spill hypothesis.
The ordinary form has seven register-backed M restore homes at -48..-72;
the indexed form retains the actual -4..-40 home region.

The decisive source fit removes the redundant named snapshot/shift locals
and deliberately repeats the narrowed incoming expressions. IDO performs
their cross-call reuse and creates the **ten genuine automatic spill homes**
itself, with no CFE M reservation. The first expression-only trial matches
all 199 words under the existing **-O2 -g3** profile. The final readable
production formatting/comments are separately recompiled and qualified.

The trace changes no text, function sizes, relative relocations or pools.
Normal/traced object files differ only in `.mdebug`; do not claim literal
object-file identity. Missing observation/input/exit gates and modified
frontend/optimizer captures are rejected.

The strict frame observer normally requires all 57 current inputs to equal
the predecessor. Post-install diagnostics explicitly use the exact-hash
two-path successor adapter **only to reconstruct that compiler context**.
The independent complete-image and actual current factory-chain checks use
the actual current ELF without any inverse or normalization.

## Preserved Contract

Retain all **17 physical argument positions**, including unused slots 12..14
and the live input-15 byte/input-16 word. Do not collapse the declaration to
the archive's fourteen formals. Address-based naming is retained until a
stronger semantic identity is justified.

The two unconditional **49-word func_1516D99C** packets preserve preset 13,
every constant/zero, full-word fields 19 from inputs 10/11, field-39 variants
0/6, signed coordinate/size transforms and captured byte/halfword values.
The input-15 indexed reread retains its real post-first-call incoming-home
load. Input 16 remains a live full word before each call.

The final **12-word func_1000FA64** packet retains event 7, the signed saved
coordinates, `0x36B0/1000/100`, callback **func_1000EBC4**, full-word input 3
reloaded after both factories, and three zeroes. Private Init declarations
match their actual types, including the context pointer and callback's
`struct00 *` first argument. All three real call-delay stores are tested.

The original [two caller windows](1406-paired-record-event-abi-and-candidate-rejection-20261015.md#caller-boundary)
remain qualified at their fired call boundaries with prepared FP/stack
dependencies. **Both current linked windows are still placeholders.** The
Init event/callback have their real symbol addresses and all **109/24 words
exact**, but the queue/callback themselves are not executed in this suite.
No full/current-caller, natural gameplay, hardware or audio-runtime claim.

## Verification

All **17 installed checks pass in 62.530 seconds**, exit 0:

- All **199 raw/padded words** match with zero target guard rows and the
  unchanged retail profile. All **29 owner neighbors** retain raw bytes,
  sizes, relative relocations and pools.
- **2,072 candidate/ROM pairs** compare complete literal private GPR/FPR/RAM,
  events, calls, accesses, LO/condition, writes and instruction visits across
  two stack phases and four provider modes. Every target word is visited.
  All 49/49/12 packet words, saved/private homes, live incoming-home updates,
  outgoing-home clobbers and all three call-delay stores agree.
- **1,152 fired memory-fault pairs** retain identical complete prefixes,
  including reads, stores, call effects and partial output state. Physical
  private-home writes are guest qualification probes, not portable C faults.
- Native 32-bit C at **O2 and O0, 65,536 cases each**, plus **seven effective
  source negatives** with controlled exits. The full-word capture provider
  validates source expressions, not the narrow production factory's whole
  native ABI or synthetic guest stack mutations.
- **Seven effective compiled guest controls** cover wrong tail slots, narrowed
  live context, wrong second type/width/callback and cached input-15 state.
  The unsigned-coordinate source control compiles away under this IDO owner
  context; classify it honestly as **native-only**, not a fired guest failure.
- Three independent original/C rebases verify **all 199 words**, both call
  targets and callback HI16/LO16 signed-low carry cases. Complete packet
  behavior agrees across all four provider modes at the rebased addresses.
- **128 actual-current factory/allocator pairs** connect freshly verified
  **125-word / 28-word** bodies, independent null/success allocation results
  and both initialized records. Lower allocation/registration and the final
  Init event provider remain opaque; the final packet is checked regardless
  of either factory's result.
- Four fresh compiler observations establish the reservation table above;
  all producer/consumer exits, code/pool equivalence and capture corruptions
  are checked. The observer never modifies compiler binaries.
- Both original caller windows and **all 801 original archive fingerprints**
  are freshly checked. The earlier 1,717-object coverage audit remains
  historical, not a new full recompilation claim.
- Validate the entire independent successor ELF, all **57 current input
  states**, all 57 immutable predecessor captures, source text, physical
  target/symbol/factory/allocator/event/callback/both-caller corruptions and
  exact before/after successor controls. Unknown inputs fail closed.

## Complete Image

Predict the entire **3,257,636-byte** ELF before installing/building: start
from its exact predecessor, replace the target's original 796-byte slot with
ROM bytes, and change only that symbol's size **12 -> 796**. The actual normal
build equals this prediction byte-for-byte. All **620 changed bytes** are
confined to that slot/extent. **No metadata exclusion or serialization
allowance** is needed. Canonical symbol bindings otherwise remain fixed.

All other **55 of 57 inputs** remain unchanged, including every original guard
CSV byte, progress row, profile, shared declaration, caller owner, Init source
and original/archive input. The protected data audit remains exact across
**189,088 bytes / 720 owners**, zero changed bytes/owners.

| Input | Exact Successor SHA-256 |
| --- | --- |
| ELF | `bbbaf381c3894213d5884672d9a4943961e613002d4197a7244ab22d5fa0729d` |
| Owner | `41e4fa5211a18dfc02604a09d2da67288c7356fdbcd4454740081d76d0e41f66` |

Fresh official matching report:

| Section | Byte-Exact | Still Different | Address Drift |
| --- | --- | --- | --- |
| Total | 3,574 / 5,501 (64.97%) | 1,927 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,901 / 4,828 (60.09%) | 1,927 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted counts/bytes remain unchanged. The root README changes only its
two aggregate matching rows; all function-level narrative stays in DOCS.

## Banking And Reproduction

Bank tools **2018515** first, then consumer C/docs/aggregate rows/pin. Shared
project tool checks and Windows syntax/standalone candidate checks pass.
Preserve the independently dirty older mirror HEAD **ddbdd16** and all **682
initial fingerprints**. Copy only five absent owned paths, giving **687
final dirty paths**, each new copy hash-equal to active tools. No mirror
overwrite/commit/reset/history copy, push, install, account change, real save/
configuration change, host build/launch or frozen Release operation.
No Claude call is needed this turn; the compiler evidence resolves the fit.
The pre-existing duplicate generated_12D630 Makefile recipe warnings remain;
the target C compilation itself has no diagnostics.
Eight scoped documentation files resolve **5,046 relative links, zero broken**.

The full Graphify update refuses **19,462 nodes against 41,241**, retaining
19,398 nodes from 2,972 excluded-but-present files. Preserve that fail-closed
result; await the actual incremental commit workers separately rather than
forcing a smaller graph or changing installed versions.

Prepared WSL consumer-root reproduction:

```sh
python3 -m tools.experiments.game_paired_record_event_match
python3 -m unittest tools.tests.test_game_paired_record_event_match tools.tests.test_game_paired_record_event_match_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

The frame test's exact predecessor adapter is explicit. Old uninstalled/
historical suites are not silently relabeled as current checks.

## Next Function And Full Scope

Continue **func_1516F9C4**, **49 words / 196 bytes**, VA `0x1516F9C4`,
ROM `0x19CE74`, frame `0x18`, RA SP+`0x14`, in the same owner. The source
already restores the intervening F864/F8EC/F91C/F94C/F984 routines; the next
remaining placeholder after this match is F9C4.

Retail reads the enable byte at `0x24` and value byte at `0x1F`, then keeps
the evolving value as a **signed full word** through its clamp/completion
tests. Enabled: add global step shifted by 4, clamp at 255, store one byte.
Disabled: subtract step shifted by 3, clamp at zero, store one byte; derive
both signed-halfword extents at `0x16/0x14` through the retail 32-bit
shift-by-9 / arithmetic-shift-by-8 sequence. Preserve wrap/sign behavior.
Only the disabled/zero completion path returns 1; otherwise call
**func_1516F864(record)**, then **func_1516F984(record, 0xF0)**, and return 0.
The record pointer is saved in the first helper's call delay and reloaded
before the second helper.

Do not copy the archive's premature `u8` intermediate, widened byte-field
accesses or its wrong first-helper argument (the control field rather than
the record pointer). Recover these against the 49 retail words and real
helper contracts before selecting C types. No F9C4 edit is included here.

Neither F548 nor F9C4 is an entry in the historical
[173-row obstruction queue](../ADDITIONAL_SOURCE_REVIEW_QUEUE.csv); they are
ordinary compilable-but-different Game backlog, not a reason to shrink that
queue or declare the entire additional source handled. Continue the
[full source-repair/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
inherited-stack renderer deferral and caller restorations after this bank.
The persistent whole-source/Game objective remains active and incomplete.

## Post-Bank Verification

Consumer **5a4baee1** banks the function, aggregate-only README rows, working
docs and tools **2018515** pin. All **17 post-bank checks pass in 89.417
seconds**, exit 0. The complete independent ELF, all 57 live input states,
801 archive hashes, four compiler observations, full private/fault/native/
rebase/factory/caller checks and corruption controls remain qualified.
Raw/padded C stays 199/199 exact, zero target guards and no profile changes.
Normal ELF/progress targets remain up to date; no artifact changes on rerun.

Both active checkouts are clean before this receipt edit. Recheck independent
older mirror **ddbdd16**: all **687 final fingerprints** remain fixed,
preserving every **682 initial dirty file** and all five hash-equal owned
copies. Eight docs resolve **5,046 relative links, zero broken**. The actual
captured source-commit graph workers finish at **41,253 nodes / 81,356 edges /
3,794 communities**, without forcing the refused smaller full scan.
Continue func_1516F9C4 and the complete additional-source/Game queues above.

## Next-Function Resolution

[Note 1408](1408-record-fade-callback-direct-match-and-live-dispatch-chain-20261015.md)
finishes func_1516F9C4 directly from C, all 49 words / frame 0x18, without
guards or profile changes. It also qualifies the actual current slot-3
dispatcher/helper/cleanup chain. Preserve this note's earlier measurements
and captures; the full additional-source/Game objective remains open.
