# Record Fade Callback Direct Match And Live Dispatch Chain

Date: 2026-10-15

## Result

Replace **func_1516F9C4**'s zero-return placeholder in
[`generated_19A8B0.c`](../../conker/src/game/generated_19A8B0.c) with semantic
C. All **49 words / 196 bytes** match retail directly in the first recovered
form, both raw and through the real production padder. VA `0x1516F9C4`,
ROM `0x19CE74`, frame **0x18**, RA SP+`0x14`. **No target guards, profile
changes, inline assembly, shared-header edits or padding locals.**

This follows the [Note 1407](1407-paired-record-event-direct-match-and-compiler-spill-recovery-20261015.md)
handoff. Preserve the address-based function name until a stronger semantic
identity is established. The `u8 *record` interface agrees with the actual
record callback table; the source comment explains the full-word clamp
lifetime that the archived scratch C loses.

## Recovered Semantics

Retail reads unsigned bytes at **0x24** and **0x1F**, retaining the evolving
value as a **signed full word**:

- Enabled: unless the value is already 255, add the global step shifted by 4
  with 32-bit wrap, clamp signed results above 255, then store one byte.
- Disabled: unless the value is already zero, subtract the step shifted by 3
  with 32-bit wrap, clamp signed negative results to zero, then store one byte.
  Produce both signed-halfword extents through the actual wrap/shift sequence
  `(s32)((u32)value << 9) >> 8`, storing **0x16 before 0x14**.
- Reread the control byte and return 1 only when it is zero **and the full
  working value is zero**. Otherwise call **func_1516F864(record)**, then
  **func_1516F984(record, 0xF0)**, and return 0.

The record pointer is saved in the first helper's actual call-delay store at
the incoming parameter home and reloaded before the second call. All
caller-saved GPR/FPR clobbers, LO/condition changes, outgoing-home writes and
an explicit incoming-home writer retain literal candidate/ROM equality.

Use unsigned intermediate shifts/arithmetic before signed interpretation;
do not introduce signed-overflow or negative-left-shift assumptions.
For value **8**, disabled, step **-31**, the update is the full word **256**:
the stored byte is zero, but the routine **still calls both helpers and
returns 0**. A byte-valued intermediate or byte-based completion test changes
that behavior. The native and guest negative controls both exercise it.

The additional source instead uses widened byte-field accesses, a premature
`u8` working value and the control field as the first helper's pointer.
Correct all three against retail; do not copy that archived body verbatim.

## Actual Dispatch Chain

The ignore-inclusive assembly/source/header search finds this function in
slot **3** of **D_8008CBA0**, at physical word **0x8008CBAC**. The original
table lives at ROM **0x231660**; all **nine pointers / 36 bytes** match the
actual current ELF and remain unchanged. Its source is already among the
57 frozen inputs, not an untracked new dependency.

The already-restored **func_1516D678** dispatcher uses the unsigned selector
at record+`0x23`, calls the selected function through JALR, and tests its
return against **exactly 1**. On completion it clears a non-null binding's
halfword at +4 before calling **func_1516972C**. Otherwise it advances 24.8 Y
using the current post-callback velocity and global step.

Freshly verify and execute these **eight actual current bodies / 213 words**:

| Body | Words | Role |
| --- | --- | --- |
| `func_1516D678` | 48 | Table dispatch / completion / Y update |
| `func_1516F9C4` | 49 | New fade/completion callback |
| `func_1516F864` | 34 | Packed X/Z position update |
| `func_1516F984` | 16 | Velocity scale wrapper |
| `func_1516F94C` | 14 | Two-axis velocity scale dispatch |
| `func_1516F8EC` | 12 | Packed X velocity scale |
| `func_1516F91C` | 12 | Packed Z velocity scale |
| `func_1516972C` | 28 | Record cleanup / destructor dispatch |

All linked words match retail and every body is reached. **276 paired chain
cases**, including **116 completion/cleanup cases**, compare complete
candidate/ROM private state and an independent public arithmetic/reference
model. Cover both stack phases, null/non-null bindings, cleanup type 0/1/2,
present/absent destructor pointers and bounded aliases of record fields with
the global step. The unlink hook observes the binding halfword already zero.
The normal continuation uses the helper-updated velocities/global value,
including step changes caused by the declared data aliases.

Only the lower **func_151696DC unlink** and type/default destructor providers
remain opaque, with explicit modeled effects. This is actual-current
dispatcher/callback/helper/cleanup qualification, not a staged/inverted image,
a full engine run or natural gameplay/hardware acceptance. The other callback
table entries are not automatically claimed restored.

## Verification

All **14 installed checks pass in 48.885 seconds**, exit 0:

- **49 raw/padded words**, original frame/RA lifetime, zero target guard rows
  and unchanged profile. All **29 other owner functions** retain raw bytes,
  sizes, relative relocations and pools.
- **3,072 complete private candidate/ROM pairs** across boundary/random
  values, unsigned control bytes, wrapping step values, two stack phases and
  four provider modes. Every target word is visited; compare GPR/FPR/RAM,
  events, calls, accesses, LO/condition, writes and visits, plus an independent
  public memory/call/result reference.
- **408 fired memory-fault pairs** compare complete literal prefixes.
  Model unmapped step data on the actual skip paths and missing bytes next
  to the one-byte value load. Do not interpret absent reads without reaching
  the branch/call/return gates.
- **48 bounded alias pairs** cover record displacement and overlapping
  control/extent fields with the global step. Incoming-home and store-side
  writers are explicit guest probes, not portable C or hardware claims.
- Native 32-bit C at **O2 and O0, 24,576 cases each**, covers all 256 value
  bytes, four control values, twelve step words and two public provider modes.
  Check the entire record buffer, helper pointers/scale, result and global
  effects; native arithmetic references use independent 64-bit wrap and
  low-halfword formulas.
- **Eight compiled guest and eight native semantic controls** all fire
  controlled public mismatches: early truncation, signed/wide load, wide
  store, wrong helper pointer, wrong scale, byte-only completion and wrong
  extent. No optimized-away controls are credited as guest failures.
- Three independent original/C rebases compare **all 49 words**, both call
  targets and both global-load HI16/LO16 pairs across signed-low carry cases.
  Complete private/public behavior agrees at the relocated addresses.
- The **276 actual-current chain pairs** above use current ELF bodies/table
  without any successor inverse. All **801 original archive fingerprints**
  are freshly verified; the earlier 1,717-object audit remains historical.
- Validate the independently predicted entire ELF, all **57 live input
  states**, all 57 predecessor captures, source text, target/symbol/caller/
  table/helper/cleanup physical flips, manifest and exact before/after
  successor controls. Unknown inputs fail closed.

## Whole Image And Progress

Predict the complete **3,257,636-byte** successor ELF before installation:
start from the exact predecessor, fill only the target's original 196-byte
slot with retail bytes and change that symbol's size **12 -> 196**. The
actual normal build equals the independent prediction byte-for-byte.
All **138 changed bytes** are confined to the target slot/extent, with **no
metadata exclusions or serialization allowances**. Other canonical symbol
bindings remain fixed.

Every other ELF byte and **55 of 57 inputs** stay unchanged, including all
original guards, profiles, progress rows, callback table, shared declarations
and original/archive sources. The protected data audit remains exact across
**189,088 bytes / 720 owners**, zero changed bytes/owners.

| Input | Exact Successor SHA-256 |
| --- | --- |
| ELF | `c69cafe57ac56ac04cdf3822142576314594c20a4acd85ee58913ca970b1320c` |
| Owner | `6d41e0d89501dfbf3d8842a1ad39e92126748e4bc7767047ba8e8f840a6dbddb` |

Fresh official matching report:

| Section | Byte-Exact | Still Different | Address Drift |
| --- | --- | --- | --- |
| Total | 3,575 / 5,501 (64.99%) | 1,926 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2,902 / 4,828 (60.11%) | 1,926 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Converted counts/bytes remain unchanged. The root README changes only its
two aggregate matching rows; detailed recovery narrative stays in DOCS.

## Banking And Reproduction

Bank tools **f9563ed** first, then consumer C/docs/aggregate rows/pin. Shared
project tool checks and Windows syntax/standalone candidate checks pass in
active tools and the older mirror. Preserve independent older-mirror HEAD
**ddbdd16** and all **687 initial dirty fingerprints**. Copy only four absent
owned paths, yielding **691 final paths**, each new copy hash-equal to active
tools. No overwrite, mirror commit/reset/history copy, push, install, account
change, real save/configuration change, host build/launch or frozen Release
operation. No Claude call is needed for this direct first-form fit.
Eight scoped documentation files resolve **5,052 relative links, zero broken**.

The pre-existing generated_12D630 duplicate Makefile recipe warnings remain;
the target C compiler emits no diagnostics. The full Graphify update refuses
**19,475 nodes against 41,254**, retaining 19,398 nodes from 2,972 excluded-
but-present files. Preserve that fail-closed result; await actual incremental
commit workers separately, without forcing a smaller graph or installing a
different version.

Prepared WSL consumer-root reproduction:

```sh
python3 -m tools.experiments.game_record_fade_callback
python3 -m unittest tools.tests.test_game_record_fade_callback tools.tests.test_game_record_fade_callback_installed -v
make tools-check
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
```

Older cohort suites are historical, not silently relabeled as fresh current
checks. The source/parser obstruction queues are not reduced by an ordinary
compilable-but-different callback recovery.

## Next Function

Continue **func_1516FA88**, **81 words / 324 bytes**, VA `0x1516FA88`,
ROM `0x19CF38`, frame `0xD0`, RA SP+`0xCC`, in the same owner. The function
remains a placeholder; no FA88 edit is included here.

Retail submits one complete **49-word func_1516D99C** packet from six physical
inputs. The first three incoming words are homed before signed 16-bit
coordinate extension in registers. Input 3 is stored/reloaded as a **full
word** into packet field 44; input 4 supplies the byte at incoming+`0x13`
for field 47; input 5 supplies the full word at incoming+`0x14` for field 48,
stored in the factory call delay. Preserve the opening schedule, packet
constants/zeroes and the full-word variant/context forwards. Inspect actual
callers and compare the entire packet before choosing C formal types; do not
prematurely narrow the fourth argument.

Keep the complete
[source-repair/binding/unanchored queues](1396-additional-source-commented-coverage-refresh-and-preset-handoff-20261015.md),
inherited-stack renderer deferral, remaining callback entries and caller
restorations open. This completed function does not finish the persistent
whole additional-source/Game objective, which remains active and incomplete.
