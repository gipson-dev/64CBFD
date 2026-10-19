# Actor State Tick Complete Match

Date: 2026-10-19. Consumer predecessor: `959a89de`; tools predecessor: `cdcece5`.
Tools checkpoint: `f48f2f9`, committed before the consumer source/guards/docs/pin.

## Installed Result

Complete **func_1508A6FC** now matches **678 words/2,712 bytes**, including its
288-byte frame, VA `1508A6FC..1508B194`, ROM `B7BAC..B8644`. This closes the
remaining frame/cached-timer/schedule boundary in
[Note 1619](1619-actor-state-tick-direct-draw-homes-and-cursor-lifetimes-20261019.md),
following the complete semantic recovery and donor-width audit in
[Note 1615](1615-actor-state-tick-recovery-and-layout-boundary-20261019.md).

The original name, recovered `s32(void)` changed-slot-mask interface and concise
purpose comment are retained. The complete body advances actor timers, state
transitions and steering, including its category-B9 score rendering. Its 39
real locals and nineteen directly recovered homes remain; no shared header,
dummy storage, volatile, physical-register binding, instruction array or new
compiler profile is introduced. The unrecovered same-owner `func_1508CAD8`
retains an old-style declaration locally to avoid conflicting with its stub;
isolated/native qualification uses its recovered six-argument call contract.

**This is not a compiler-only match.** Complete semantic C emits 678 words,
frame 288, with 344 aligned raw differences. The checked complete source-origin
recipe produces all 678 retail words. The 344 appended expected-word guard
rows are fixed-length replacements, with no insert-after or omit CSV flags.
Every preceding manifest byte is preserved; original assembly is untouched.

## Complete Origins And Lifetimes

[Layout recipe](../../tools/experiments/game_actor_state_tick_layout.py)
retains **675 unique source origins**, derives **three forms**, and omits
**three pure instructions**. Every one of the **311 source memory instructions**
is retained exactly once. All **62 relocation entries** move with their source
origins. Raw words/bindings and complete normalized output are fingerprinted;
the normalizer is pure and does not read the ROM or any other file.

Nine remaining frame mappings close the cursor/anonymous-save boundary:

| Role | Raw SP Offset | Retail SP Offset |
| --- | --- | --- |
| Reset cursor | A4 | 84 |
| Status cursor | FC | 60 |
| Band cursor | 9C | 5C |
| Timer row | 70 | 7C |
| Cooldown row | 68 | 74 |
| State row | 60 | 6C |
| Event row | 5C | 68 |
| Event-byte call save | 58 | 64 |
| Draw-actor call save | 114 | 8C |

Already exact action-row SP+54, draw-index SP+A0, actor-action SP+104 and the
seventeen earlier scalar/table homes are not displaced. The actual timer
read remains; the post-reset access uses the retained current-row home rather
than reloading the mutable table-base home. Both previously failing cached-row
aliases now agree, while the raw source remains an effective negative.

The three omissions are redundant scaled-slot origin 390, timer-row ADDU
origin 398 and the coalesced started-result MOVE at origin 422. None accesses
memory. The three derived forms are the checked actor-pointer bias and two
delay NOPs from an existing source NOP. The recipe restores the late started
flag's A2 lifetime, opening header/private stores, loop cleanup, byte-only -50
immediate form, temporary register roles and rescheduled branch entries. Five
explicit branch-entry overrides target the first instructions of their moved
blocks. Eight scheduling islands and lifetime-scoped operand mappings are
checked against complete source/output fingerprints, not applied speculatively.

## Fresh Qualification

[Layout tests](../../tools/tests/test_game_actor_state_tick_layout.py) and
[integration tests](../../tools/tests/test_game_actor_state_tick_integration.py)
pass all **15 pre-install checks in 58.271s primary / 22.612s mirror**. The
fresh installed runs pass all **15 in 47.365s primary / 35.872s mirror**, with
zero skips, failures or errors. Each copy independently qualifies the selected
complete body; mirror imports are verified before redirecting consumer inputs.

- All 262 completed fixtures compare the independent state-machine reference
  and literal retail/normalized GPR/FPR/private memory, ordered reads/stores,
  calls/events, visits, executed instructions, provider counters and HI/LO.
- Fifty-eight effective frame-alias pairs cover 29 roles in both stack phases.
  Eighteen wrong-layout controls reject nine old slots after their requested
  mutations fire. Negative runs may reach unmapped guest accesses only after
  the requested mutation; those faults are not silently accepted successes.
- Twelve full-word actor-action aliases retain upper bits across ACTION.
  Two fired timer-table aliases close the retained-row readback boundary.
- All 876 requested model instruction-access cuts fire with equal literal
  prefix state. Observer/provider accesses are excluded from cut gates. These
  are memory-access-prefix tests, not hardware exception emulation.
- All 678 individual raw-word and 62 binding mutations reject stale input.
  Four disabled recipe components and actual-padder/image mutations reject
  incorrect transformations. The normalizer rejects accidental file access.
- Independent textual original assembly assembled by GNU matches normalized
  unlinked bytes and bindings. Original/normalized/raw code is linked under
  three maps, including 7FFC/8000 HI/LO carry boundaries and independently
  rebased helper calls: 27 completed runs. Original/normalized literal state
  agrees; raw C agrees on ordinary public behavior, not the known frame alias.
- Fifty-seven native32 fixtures pass O0/O2/O3 with UBSan on the function
  extracted from the actual installed owner. Three compiled semantic negatives
  remain effective; the separate signed-overflow control fires SIGILL -4.

Fixtures visit **660/678 retail words**, not complete instruction, FCSR,
hardware, caller/helper-chain or gameplay coverage. Native tests exclude
deliberate guest-frame aliases. Byte identity and these bounded behavioral
receipts do not claim PC-port adoption or gameplay acceptance.

## Production Proof

[Integration](../../tools/experiments/game_actor_state_tick_integration.py)
qualifies both complete owner profiles, preserving all 72 other bodies and
normalized pools. Actual padding keeps all 73 owner addresses and 72 other
extents fixed; the target's logical symbol size changes from 12 to 2,712 bytes.
Primary and mirror separately reproduce the unchanged seven-command Make
recipe, existing normal-profile overrides and identical first linked image.

The actual N64 build succeeds and exactly reproduces the strict prediction:
**2,183 changed ELF bytes: 2,124 target-code bytes and 59 metadata bytes**.
Metadata changes are two target-size bytes and 57 bytes in two closed existing
symbol/string-order groups, not arbitrary metadata drift. Named definitions
stay identical except the target size. The guarded left rotations involve
`D_8009DA20`, `.L15032B30_game_data`, `D_8009D590`, and separately `D_800872E0`,
`D_8008CEB0`. Disabling those exact groups or corrupting metadata is rejected.

All **6,056 other function bodies**, all **6,057 function addresses** and
**189,088 protected Game-data bytes across 720 owners** remain fixed. Makefile,
progress CSV, ROM and original assembly stay byte-identical. The shared guard
manifest causes a broad object rebuild, not a broad source conversion. The
build log retains existing duplicate recipes and unrelated compiler/assembler
warnings; this is not a warning-free-build claim.

Fresh recount: **Game 3,018/4,832 (62.46%)**, **overall 3,691/5,505 (67.05%)**,
1,814 different and zero address drift. Init 492/492 and Debugger 181/181 stay
exact. Owner **70/73 exact**. Conversion stays 5,505/6,044 (91.08%), 86.08%
bytes. Root README changes only its two matching aggregate rows.

```text
Source:     be56a04b3aa3c7b1d3f2b1d03e8da6170f79c6ba5ca430cffd392a832963feb8
Manifest:   c1b76ce25dbd18ca06aee817299da8588024ba0e48006a7ca20aabb6dffe4a15
ELF:        51a5f15b5a0834290ea21451d45c3d24d8327930c92a1d8337c0c72f81c82948
Raw C:      9fa41b55435921115dfe029d37b330f90b787329f0b8b83dfb3630a3b242ffd9
Bindings:   449c7456ea2d4a9f6df7e195bbe27a810b6d08ececef40ca52232167582f4a49
Normalized: a7b81de694c806ad2ca87ce823c3ebc8bfeb6ec23f432ecddaafdc7ec33d1fff
```

Only four absent task files are copied into the independent tools mirror.
Its HEAD `ddbdd16b` and every one of **1,444 older dirty leaf hashes/statuses**
are preserved; final dirty paths 1,448. No mirror commit/reset/stash/clean,
push, host/frozen Release, save, dependency or advisory-agent operation.

Ignored receipts live under
`conker/build/game-actor-state-tick/lifetimes/homes/draw/match/`: layout tests,
separate integration/mirror owner/Make/first-link and installed runs, complete
predecessor snapshots, production log/audit and fresh progress/remaining-owner
report. The consumer commit hook refreshes Graphify; retain and audit its
before graph, including excluded-but-existing historical nodes, when banking.

## Next Function

Continue **func_15086364**, 539 words/2,156 bytes, frame **0x600**,
VA `15086364..15086BD0`, ROM `B3814..B4080`. Production remains a 12-byte
zero-return C stub with **522 classified differences**. Read its entire retail
routine and callers to recover byte argument widths, large local workspace,
return contract and helper lifetimes before installing anything. The other
owner nonmatches are `func_1508CAD8` (862 words/818 differences) and
`func_1508DC24` (681 words/661 differences). Keep the wider Game goal active.
