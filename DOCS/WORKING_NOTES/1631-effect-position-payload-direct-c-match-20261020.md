# Effect Position Payload Direct C Match

Date: 2026-10-20. Consumer predecessor: `27aecb1e`; tools predecessor:
`67c13be`. Tools checkpoint **db39e84** is committed first. No push.
This finishes the isolated draft from
[Note 1630](1630-effect-payload-spawn-direct-c-match-20261020.md).
The wider **75% total C-matching goal stays active**. Both the preceding and
current goal turns make measured matching progress.

## Installed Result

Replace the false zero-return `func_150F10D4` body in
[generated_11C2B0.c](../../conker/src/game/generated_11C2B0.c) with its complete
purpose-commented C routine, retaining its original name.
VA **150F10D4..150F1170**, ROM **11E584..11E620**.
All **39 words / 156 bytes / frame 88** emit directly from the existing
**IDO O2/g3** profile, with **two original call bindings, zero new guards and
no compiler/profile/Makefile changes**.

The recovered interface is `void(void *source)`. Its 24-byte payload holds:

| Offset | Field |
| --- | --- |
| 0 | Source pointer |
| 4 | Source byte from 3B |
| 5..7 | Three locally unwritten reserved bytes |
| 8 | Zero float |
| 12, 16, 20 | Three captured float words from source + 14/18/1C |

All defined fields are captured before the effect factory executes. The final
Z-word store is the factory JAL's delay instruction, not a post-call read.
The factory request is `(300, -1, 0x4C, -1, 0, 0x3A, 24, 0xFF, 1)`; only
successful allocation copies all 24 bytes to result + 28. Preserve saved S0 as
the source through both calls and restore the incoming S0 at return.

The reserved bytes are intentionally not initialized. They are copied retail
payload bytes, not dummy frame storage. Native tests constrain only defined
fields; guest tests also constrain their actual stack representation.

## Caller And Provider Scope

A complete pristine scan of every US Init/Game/Debugger function span finds
one direct JAL: **func_15071764 at 15071788**. The existing 31-word C wrapper
uses frame 56, reloads the actor from SP+34 for the call, does not consume the
target's return value, and restores SP before JR with a NOP delay instruction.

Add the explicit opaque-pointer prototype to
[game_981E0.c](../../conker/src/game_981E0.c).
All **328 raw and padded caller-owner functions**, pools, addresses and extents
remain fixed. Caller diagnostics are unchanged after filename/line-number
normalization; the recovered target compiles without diagnostics.

Tests execute the original wrapper with the recovered target and optional
original 11-word memcpy connected below it. Bounded lookup, initialization,
factory and follow-up contracts distinguish null lookup, factory failure,
initialization before capture, factory mutation after capture and follow-up
after the target even when allocation fails. These contracts are not complete
executions of those upstream providers.

Reuse the established nine-argument factory wire declaration, preserving its
linked implementation. As recorded in Note 1630, that older implementation
still uses a pointer-typed payload-size representation. This recovery does
not refactor it or claim whole-provider ISO C type consistency.

## Fresh Qualification

[The integration helper](../../tools/experiments/game_effect_position_payload.py)
reuses the existing compiler, object parser, independently assembled original,
padder, linker and protected-data audits.
[Eight tests](../../tools/tests/test_game_effect_position_payload.py) reuse the
existing MIPS oracle rather than adding an interpreter.

**Eight pre-install and eight installed tests pass in both tools copies**,
with zero errors, failures or skips:

| Stage | Primary | Standalone Tools Mirror |
| --- | ---: | ---: |
| Pre-install | 25.587s | 22.783s |
| Installed | 10.135s | 9.056s |

- **144 cases / 576 modeled phases** compare independently described public
  accesses/calls/output and literal complete modeled GPR/FPR/condition/HI/LO,
  private/public RAM, histories and instruction visits. **512 phases actually
  enter the target**; the other 64 take the wrapper's null-lookup path.
  All **39 target words** execute across the corpus.
- Byte boundaries, signed zeros, finite extremes and guest-only nonfinite
  coordinate bit patterns are covered. Factory mutations prove early capture
  of all three coordinates, including the delay-slot Z store.
- **128 phases execute the original wrapper**, covering both lookup paths,
  initialization/follow-up mutations and success/failure allocation.
- **288 phases configure original memcpy; 160 actually enter its instruction
  stream**. Assert those fired entries separately. The independent forward-copy
  reference and both copy routes agree, including actor-output aliases and
  private payload overlaps at +1/-1.
- Fired physical writes alter the source incoming home and the three payload
  reserved bytes. S0 must retain the actual source; copied padding must reflect
  the private write. These physical probes remain guest-only.
- **82 native32 cases** pass O0/O2/O3 with trap UBSan and contraction disabled.
  Inputs have real typed float subobjects at 14/18/1C and an actual byte at 3B.
  The native harness includes the existing C wrapper, valid nonoverlapping
  local-payload copies, defined-field decoding and output fences. Reserved
  byte values and nonfinite FPU behavior are not asserted natively.
- **Eight compiled semantic negatives** fail with the expected mismatch:
  late position capture, wrong X, wrong Z, wrong flags, wrong payload size,
  short copy, wrong destination or suppressed successful copy.
- **Four guest negative phases** reject explicitly zeroed reserved bytes or
  a removed original S0 restore. The latter is only a test instruction
  mutation; no production assembly is altered.
- **Three independent GNU code/helper rebases**, with moved argument buffers,
  pass **24 additional phases** against the independently assembled original.
  Both R_MIPS_26 bindings remain intact; there are no invented data bindings.
- **Eight strict-image negative controls** reject altered headers, target or
  neighboring bytes, symbol size, truncation and appended bytes.
- Both tools copies agree on the two task files. All four Python copies parse;
  both existing project-tools checks pass.

The source domain requires valid aligned readable coordinate fields, a readable
source byte and valid factory/copy buffers. Hardware FCSR/MMU, indirect consumers,
complete provider/gameplay execution, portable-C private overlaps and specific
unwritten-byte values, and host-port acceptance remain separate.

## Actual Build And Linked Audit

Preserve all **43 other raw and padded target-owner functions** and pools.
The actual expanded Make shadows execute **eight productive commands** across
target/caller with the normal O2/g3 flags. Their raw/padded objects agree with
the independent qualification. The existing duplicate generated_12D630 recipe
warning remains; do not describe the full build as warning-free.

The production build exits zero and exactly reproduces the independent image:

- **120 changed ELF bytes**: **119 instruction bytes**, **one target-size byte**.
  Only this symbol grows from **12 to 156**; there are **zero metadata exclusions**.
- All **6,056 other linked bodies**, all **6,057 addresses**, and all
  **189,088 protected Game-data bytes / 720 owners** stay fixed.
- Original ROM/assembly, the complete guard manifest, Makefile and progress CSV
  stay byte-identical. This replaces already-counted C, not a conversion row.
- Installed suites audit the strict live source/caller/ELF first, then use frozen
  predecessor fixtures. Historical input pins are not rewritten to accept new C.
- Unchanged neighbor suites are reused through exact whole-image preservation;
  they are not represented as freshly rerun broad suites. No Claude call was
  needed for this routine's bounded, directly checkable recovery.

## Counts And Next Target

Fresh matcher: **Game 3,023/4,832 (62.56%)**,
**overall 3,696/5,505 (67.14%)**, **1,809 different / zero drift**.
Init remains 492/492 exact; Debugger remains 181/181 exact.
The current 75% threshold is **4,129**, requiring **433 further exact matches**.
Recompute if the converted-C denominator changes. Root README gets aggregate
rows only; details stay in this note and concise indexes.

The refreshed ELF-pinned source-shape queue contains **1,674 zero-return
placeholders, 126 semantic/other entries and nine unlocated entries**. Those
are triage categories, not ABI or semantic acceptance.

Next screened short recovery: **func_151A499C**, generated_1D0840,
VA **151A499C..151A4A38**, ROM **1D1E4C..1D1EE8**.
Its first semantic 32-byte extended-payload draft has the correct **39 words /
frame 80**, but **nine real word differences**. It is **not installed and earns
no credit**. Plain arguments give the best screen; source-volatile controls
regress to 18 differences. Recover scheduling/argument homes, copied reserved
bytes, the global float binding and the eight-argument factory/caller contract
before full qualification. Keep func_15070C40 and the 862-word func_1508CAD8
owner stub queued.

## Preservation And Receipts

Preserve all **1,474 pre-existing mirror paths/statuses/hashes** and HEAD
`ddbdd16b`; only two absent task files are added, leaving **1,476 dirty paths**.
No mirror commit/reset/stash/clean, push, dependency/compiler installation,
second advisory writer, host/frozen Release operation or save/config changes.
The confirmed disposable compiler scratch file needs no recovery; path
handling was already corrected in the preceding work.

```text
Raw C code: 07112109b9fb830d0de3fcdfdadabde121c2e82ddd52e5777dd1667aef37970c
Linked ELF: 290324d2321ae5c5c86610133e6a5e4a561aef0fda2f50b84e86a09a58009e00
Guards:     7ca8a25f8ea41d9e2e4a795281619c21048f5c24b252d48a9367eb5cd5e36e76
```

Ignored receipts under `conker/build/game-effect-position-payload/qualified/`
hold primary/mirror tests, native negatives, independent GNU objects/rebases,
owner/caller/Make/first-link/live/data audits, production log, fresh progress/
75%-queue, mirror preservation and post-commit graph closeout.
The next non-installable screen is under
`conker/build/game-effect-extended-payload/screen/`.
The wider 75% objective stays active, not complete.
