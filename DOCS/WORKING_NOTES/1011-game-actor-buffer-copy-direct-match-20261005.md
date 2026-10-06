# Game Actor Buffer Copy Direct Match

Date: 2026-10-05. Starting HEAD: `bc3a8ae0`, the banked
[actor-reference coordinate phase](1010-game-actor-reference-coordinate-phase-match-20261005.md).

## Recovery And Match

Recover **`func_1502F948`**, the post-pass helper called by `func_1502BEE4`.
Its complete **45-word / 180-byte** slot at **0x1502F948..0x1502F9FC**,
ROM **0x5CDF8**, now matches retail. Frame: **0x28**. Linked SHA-256:
`6453250c820339049c21dc029171201bae554c734b61fdbe8d89d4f9a096aaf6`.

This is **direct default IDO output**, not a guard-normalized match. No word
patch, insertion, omission, compiler-profile override or handwritten body
is added. The recovered `void(ActorCopy58F80 *)` signature replaces the
false zero-return placeholder. Its caller receives an explicit layout-view
cast; the caller's linked bytes do not change. The experiment driver's
production-source identity binding tracks that cast without altering its
isolated selected/recovery bodies.

The separate 0x32C-byte view names only ID byte +4, flags word +0xF8,
source pointer +0x1D4, destination buffer +0x1D8 and state word +0x264.
Existing display, update and coordinate views are preserved.
The view sits after the dispatcher definition, leaving its contiguous
declaration/source-identity block intact. An initial corpus run detected
that inserting the view inside that block broke the identity assertion;
moving the view preserves the test without changing any linked slot.

## Retail Contract

1. In order, test flag bit **0x4000**, nonzero state +0x264 and nonnull
   source +0x1D4. Each failed gate short-circuits later field reads. This
   helper itself does not test the actor's active word.
2. Cache the unsigned ID byte in a full-word local across allocation.
   Existing nonnull buffers skip the allocator but still copy, including
   when the size is zero.
3. If the buffer is null, read unsigned `D_800C4ED0[cachedId]`, multiply
   by 64 and call `allocate_memory(size, 1, 1, 2)`. The restored wrapper
   calls `func_10003C6C(size, 1, 1, 0, 2)`; its fifth argument is at SP+0x10.
4. Store the returned address word to +0x1D8 **even on allocation failure**.
   That store overwrites any buffer value written by a callback. A null
   return skips the copy; it does not retry or retain the callback's buffer.
5. For an existing buffer or successful allocation, freshly reload source,
   buffer and the size-table halfword, but use the **cached ID**. Call
   `bcopy(source, buffer, freshSize << 6)`. Do not cache the size/source
   across allocation or reload the ID instead of restoring its word home.
6. Do not recheck flags/state after allocation, skip zero-length calls,
   introduce extra validation or change overlapping-copy semantics. Restore
   saved S0, RA and SP through the original epilogue.

The size calculation is unsigned-halfword based: 0x8000 and 0xFFFF become
2097152 and 4194240 bytes. These large values are ABI-only cases; no large
memory-copy execution is claimed by the bounded fixtures.

## Compiler Controls

The driver screens seven forms:

| Form | Body Words | Frame | Differences |
| --- | ---: | ---: | ---: |
| Selected signed word ID | 45 | 0x28 | 0 |
| Unsigned word ID | 45 | 0x28 | 0 |
| Multiply size by 64 | 45 | 0x28 | 0 |
| Byte ID positive control | 45 | 0x28 | 2 |
| Reload ID after allocation, negative control | 44 | 0x20 | 25 |
| Omit state gate, negative control | 42 | 0x28 | 36 |
| Cache size across allocation, negative control | 40 | 0x28 | 31 |

The selected compiler run has no diagnostics. The byte-local control is
semantically equivalent but does not reproduce the retail full-word spill
and restore. Each negative control is also rejected by a behavioral case,
not merely by counting instruction differences.

## Qualification Boundaries

The focused module compares retail, direct selected output and the byte-ID
positive control in **13461 completed three-way guest cases**:

- 12288 flag/state/source/existing-buffer/ID/stack-phase cases, covering
  all 256 ID bytes, zero-size calls and both O32 stack phases.
- Six unsigned high-halfword allocation-failure ABI cases and three
  unmapped-later-field checks proving gate short-circuit reads.
- 640 allocator-mutation cases, changing ID, old-ID size entry, source,
  callback buffer and flags/state independently, with success/failure.
- 480 connections to the actual **11-word allocator wrapper** and
  **196-word SDK `bcopy`** slot, checking 0/64/128/192/256-byte copies,
  source alignment 0..7, equal pointers and forward/backward overlap.
- Four actual-wrapper mutation/failure connections and 40 existing-buffer
  SDK connections that must not invoke allocation.

All **45 target retail words** execute across these cases. The bounded SDK
connections reach **118 / 196 words**; the other SDK paths are not claimed
as covered. A local oracle extension implements signed LB and nonoverflowing
ADD for these paths, leaving shared oracle behavior unchanged. Complete
external memory/events and saved GPR/SP restoration are compared; actual
copy results are checked against a pre-copy snapshot reference.

The native freestanding 32-bit C fixture checks layout/unsigned-size ABI,
**163840** independent-reference cases comparing the whole actor record,
arena, size table and callback log, plus **16384** gate/storage-preservation
cases. Native pointers stay within the fixture arena. The wrapper's heap
core is an opaque callback with volatile-register clobbers and controlled
mutations; this is not actual heap-core or full gameplay qualification.
No new connected full actor-pass claim is made; existing caller/selector/
dispatcher/coordinate-phase regressions remain required.

## Linked Audit And Progress

The before/after audit covers **6060 slots**: only `func_1502F948` changes,
with no added/deleted slots, address moves or length changes. Caller
`func_1502BEE4` stays at **109 differing words**, hash
`c32708201e59edf73b9986867a0afa76d7a8da115d8a38d0f703cbaa85422758`.
Previously banked display scan, dispatcher and coordinate-phase hashes
remain unchanged.

The patch CSV is unchanged: **10622 unique rows**, SHA-256
`b805f4aada0d4273b2af4ba67424da07de5bfc41e766449f29893b4b63bf011b`.
There are no `func_1502F948` or caller guards added. Complete Init code
**164048 bytes**, Init data/rodata **17376 bytes**, Debugger **19800 bytes**
and Game data **189088 bytes / 720 owners** remain retail-exact.
Build/progress/match-progress pass. The final focused copy/coordinate-phase/
caller/dispatcher run passes **41 tests in 173.674 seconds, no skips**.
The complete actor, viewport, resource, matching and object/data-tool corpus
passes **343 tests in 690.045 seconds, no skips**. Its fresh Game-data
extraction subprocess waited on Windows/WSL filesystem I/O and then finished
normally; no test was removed, skipped or restarted to bypass that wait.
`make tools-check` and whitespace checks pass. All **2955** checked relative
links resolve across the nine current/working-note/README documents.

| Section | Exact Linked C Functions | Address Drift | Still Different |
| --- | ---: | ---: | ---: |
| Total | 3304 / 5463 (60.48%) | 0 | 2159 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 2631 / 4790 (54.93%) | 0 | 2159 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

README changes only the aggregate exact/different counts. Conversion counts,
47 retained Init ASM routines and sibling sources/builds/saves/frozen Release
are unchanged. No host transplant or push is made.

## Reproduction And Next

```powershell
wsl python3 -m tools.experiments.game_actor_buffer_copy_candidates
wsl make -C conker NON_MATCHING=1 build/conker.us.elf progress match-progress -j4
wsl python3 -m unittest tools.tests.test_game_actor_buffer_copy_match tools.tests.test_game_actor_attachment_phase_match tools.tests.test_game_actor_update_pass_match tools.tests.test_game_actor_update_dispatch_match -q -f
wsl make tools-check
git diff --check
```

Next connected semantic recovery: **`func_1502F490`**, still a placeholder,
as of this checkpoint. The subsequent complete C recovery and mandatory
matrix-tail assembly restoration are recorded in
[Note 1012](1012-game-actor-triangle-remap-semantic-recovery-and-matrix-tail-restoration-20261005.md).

Original handoff:

302 words / frame 0x138. Preserve its five-argument actor/X/Y/Z/joint ABI.
The known zero-table return is not evidence for its nonzero-table paths.
Work in this order:

1. Recover the ID/joint-indexed three address lookups and unsigned interval
   scan using tables `D_800C6070`, `D_800D19A0`, `D_800C5EF8` and
   `D_800C5C08`. Preserve count exhaustion, three-bit completion and end
   exclusivity before any actor-buffer access.
2. Recover the null-buffer/source gates and two three-point transform sets:
   +0x1D8 buffer first, freshly loaded +0x1D4 source second. Each calls
   `func_150A7960` with a 64-byte matrix index, three signed-halfword-to-float
   coordinates and three output pointers, **seven arguments** in total.
   That callee's original 40-word, frame-free slot is also still a C
   placeholder in `generated_D4E10.c`. Qualify its real retail instructions
   in connected traces, or recover it explicitly; do not mistake an opaque
   transform callback for complete production behavior. It reads float
   matrix columns and groups each axis as `(m0*x + m4*y) + (m8*z + m12)`.
3. Preserve the float operation order, two zero-denominator -100.0f paths,
   ordered [0,1] rejection tests and final X/Y/Z read/modify/store order.
   Qualify aliasing, live callbacks and finite edge cases before asserting
   complete semantic parity; FCSR/traps/legacy NaN behavior remain explicit
   hardware-model boundaries.
4. Screen compiler layouts and audit all slots/protected sections before
   claiming a byte match. Do not replace the complete body with a broad
   instruction-patch batch. The caller's maximum-depth spill/address
   lifetime/scheduling match remains independently open.

The Game goal remains active with **2159 differing C functions**.
