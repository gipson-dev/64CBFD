# 1975 - Linked-state refresh recovered as a guarded byte match

`func_151A084C` now matches all **55 retail words**, with its natural **48-byte
frame** and **two expected-word guards for one closed private pointer spill**.
Production Make and the independent Native ELF recount confirm
**4,042/5,507 (73.40%)**, Game **3,369/4,834 (69.69%)**, zero address drift and
1,465 still different. Exactly one match is added. The 75% threshold is 4,131:
**89 more** matches are needed; the wider goal remains active.

## Behavior and recovered interface

Owner `generated_1CC440`, source `conker/src/game/generated_1CC440.c`, VA
`0x151A084C..0x151A0928`, ROM `0x1CDCFC..0x1CDDD8`.
Restore `void func_151A084C(struct260 *entry)`, matching the existing
`D_8008A4E8` callback type and actual dispatch route. Keep the partial shared
`struct260` definition unchanged; use byte/pointer views for the linked fields
beyond its known prefix, and its existing `unkD`/`unkE` members for invalidation.

Capture the state pointer from entry +0x28, its actor from state +0x18, and the
four-word output base at state +0x58. Set a byte invalid flag when the actor's
first word is zero or state byte +0x1C differs from actor byte +0x3B. Identity
is still read when the actor is inactive. Invalid paths skip actor word +0x1D4.

For a valid actor with a nonzero +0x1D4 word, set invalid and call
`func_1519F1C8(state, modeByte)`. Reload the mode byte from entry +0x2C after
that call: mode 6 stores the returned word into the captured first output;
other modes store it into the captured third output. The helper may replace
the linked state or change mode, so preserve the old output base while reading
mode live. A returned zero still follows the same invalidation path.

When invalid, call `func_151A0928(entry)`, then set entry's signed halfword +0xE
to -1 and OR bit zero into its live flags byte +0xD. The real cleanup helper
reads the **current** linked state and mode, clearing its second output for
mode 6 or fourth output otherwise. A first-output store may itself alias the
entry mode byte; both subsequent cleanup reads must retain their retail order.
A valid actor with zero +0x1D4 performs no refresh or invalidation. Mapped entry,
state and actor objects are preconditions; no new null-state/actor gate is added.

## Compiler recovery and the closed spill pair

Initial semantic C emitted 55 words with a 56-byte frame. Removing the redundant
cached state local restored the 48-byte frame. A branch-local result and the
direct byte truth test `if (invalid)` recover the 55-word retail control flow
and register allocation. Alternative declaration/scoping and pointer views are
retained in the stage; they are measured source screens, not compiler-causality
claims. The proper `struct260 *` argument needs no extra cached byte-pointer local.

The final raw C differs only at offsets **0x68** and **0x8C**:

| Offset | Raw C | Retail | Meaning |
| --- | --- | --- | --- |
| 0x68 | `AFA80024` | `AFA80028` | Spill output base T0 at SP+0x28 instead of SP+0x24 |
| 0x8C | `8FA80024` | `8FA80028` | Reload the same T0 value from that slot |

Both addresses are within the original frame. One store and its corresponding
reload move together; neither instruction changes a public object access,
argument, register lifetime or control-flow edge. Two narrowly scoped CSV rows
require the exact old words and no relocations. All preexisting guard bytes are
preserved. No frame padding, physical register binding, inline assembly, compiler
profile change or shared-tool edit is introduced.

Raw isolated C payload SHA-256:
`90346cf34a47d6b39bef66ac3ae745f5ccb063d16dbd5cce01a7c63a50b700d9`.
The two call relocations are `func_1519F1C8` at +0x70 and `func_151A0928` at +0xAC.
All 55 normalized words and both bindings equal independently assembled retail
code. All 55 emit; **54 execute**, with the duplicate store at +0xA0 unreachable.

## Qualification evidence and bounds

- **16,128 guest cases / 48,384 executions** cover three independent GNU link
  layouts and original, normalized-C and raw-C roots. All 256 mode bytes,
  active-word boundaries, identity gates, resource availability, full returned
  words, helper mutations, stack phases and output/mode aliases are covered.
  Raw C agrees with an independent public-memory/call reference; normalized C
  agrees with the original's complete bounded GPR/FPR/HI/LO, memory, calls and
  access traces. Raw private stack memory is deliberately not claimed equal.
- **85 access-prefix pairs** compare complete original/normalized bounded state.
  Six sparse executions omit the resource word on invalid paths or omit mode
  and output mappings on the valid unavailable path. This qualifies guest
  instruction ordering, not portable C fault behavior or real hardware.
- Native32 **O0/O2/O3 each pass 2,816 cases / 25,344 executions**, with UBSan,
  all 1,472 public bytes checked, native-endian word writes, live link/mode
  changes and the output/mode alias. Eight effective controls reject ignoring
  the inactive gate, wrong identity byte, cached mode, skipping zero-result
  invalidation, wrong selected output, omitted cleanup, overwritten flags and
  an inverted resource gate. The retained cleanup C body is used directly.
- The original **10-word `func_151A0928`** equals its retained production slot.
  **634 connected executions** visit every helper word and check the live
  state/mode selection. The larger refresh helper `func_1519F1C8` is modeled
  with its actual two-slot byte-mode interface, returned word, caller-saved
  clobbers and mutations; its complete implementation is not qualified here.
- A complete aligned ROM census finds no direct JAL/J and one pointer at ROM
  **0x22EFD4 / VA 0x8008A514**, index **11** in `D_8008A4E8`. The existing table
  type is `void (*)(struct260 *)`. The original **45-word `func_15149264`** is
  equal to its retained body. **2,688 cases / 5,376 executions** connect every
  parent word, the actual table cell, each root and original cleanup helper.
  Entry flags, signed halfword timers, subtraction/wrapping, post-callback timer
  reload, destructor selection and a destructor changing the timer are checked.
  The callback's result is unused. These are the target's index-11 routes;
  other callbacks are not qualified. Lower destructor and free providers remain
  stubs, with arguments, ordering and bounded mutations checked.
- Full raw and padded owners preserve **38 neighbors**, all **six GLOBAL_ASM
  functions**, normalized pools, and **zero owner diagnostics before and after**.
  The actual **five-command** mixed-owner Make recipe reproduces the qualified
  padded object. The initial preparation incorrectly selected the root padder's
  layout-file API and assumed a three-command recipe; inspection corrected both
  before successful qualification. Existing unrelated duplicate-recipe warnings
  remain recorded in the full production log.
- Both tools copies pass **five target tests and shared checks before and after
  installation**. A malformed private scope screen, missing census transfer and
  omitted object binding in the public-test refactor were corrected; failed and
  successful receipts remain in the stage. Routine work uses **zero Claude calls**.

## Production preservation and continuation

The independent whole-image prediction starts from frozen ELF
`82be01b39fa42cbc62f1ec773ca0e38b838018630dd35b3631cc0acd03f93a20`.
It replaces only the 220-byte target slot and changes its symbol extent from
**12 to 220 bytes**. Private and actual production links equal this prediction
literally, with **zero exclusions**. All **6,052 function addresses**, **6,051
other bodies**, named definitions except the declared extent, ELF length,
normalized map and Makefile remain fixed. All **189,088 protected Game data
bytes across 720 owners** remain exact.

Every one of the **17,705 prior sealed inputs** was reviewed after actual Make.
Only the intended source, two-row guard append, owner object and ELF changed
before documentation. No dependent-object change is excluded. Native's actual
ELF recount independently confirms exactly one additional match.

Production ELF SHA-256:
`2d4f55fb3eb0eb90fb9d5cf829d92ea1771b03b1d2529a3f22bb8a8ba0c7f3af`.

Stage `conker/build/game-linked-state-refresh-151A084C-match/` retains frozen
inputs, **29 immutable preparation-artifact pins**, private/public test receipts,
original assembly object, actual Make commands/objects, prediction, production
and Native recounts, seal, scoped graph proof and handoff. Four new public tools
modules cover source/image gates, guest/cleanup/dispatcher execution, native
controls and integration tests. The graph refresh extracts thirteen changed
files with zero LLM tokens, preserving old nodes and valid edge occurrences while
archiving the obsolete integer return-type edge. No full-corpus extraction or
reclustering is claimed. Root README changes only aggregate rows. Commit tools
before consumer; no push. Original assembly, unrelated mirror work, private
candidates, archives and frozen host Release remain preserved.

Next ordinary unmatched C target from the actual production inventory:
**`func_1518BBF4`**, 55 words/frame48 in `generated_1B8F40`. Inspect its captured
argument, saved-register lifetimes, row/list traversal, signed global traversal
index and cleanup helper before proposing a body. Its original null-gated outer
path and inner condition leave unreachable instructions that must be accounted
for, not silently omitted. It has not been screened or credited here. Other
parked candidates and historical whole-image fixtures require explicit rebasing
before reuse. The wider 75% objective remains active.
