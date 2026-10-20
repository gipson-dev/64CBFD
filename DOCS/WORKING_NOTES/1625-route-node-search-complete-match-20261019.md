# Route Node Search Complete Match

Date: 2026-10-19. Consumer predecessor: `817be19b`; tools predecessor:
`a7eba1d`. Tools checkpoint **27fb65e** was committed before production edits
and before the consumer pin/source/documentation commit. No push.

## Installed Result

Complete semantic **func_15086364** now replaces its zero-return placeholder in
[generated_B3020.c](../../conker/src/game/generated_B3020.c). Preserve its name,
five-argument interface, signed-byte list counts and short purpose comment.
VA **15086364..15086BD0**, ROM **B3814..B4080**, all **539 words/frame 1536**
are byte-exact in the actual rebuilt ELF.

This is a **guarded match**, not a compiler-only match. The complete normal
O2/g3 C still emits 535 words. The
[layout recipe](../../tools/experiments/game_route_node_search_layout.py)
recovers original value lifetimes and scheduling from that semantic body.
The [integration gates](../../tools/experiments/game_route_node_search_integration.py)
qualify actual owner selection, padding, Make commands and the first image.
Continue from [Note 1624](1624-route-search-start-home-extent-and-ordered-reads-20261019.md).

## Source Origins And Lifetimes

The initial instruction-shape alignment was diagnostic only: 511 of 539 words
agreed after ignoring register fields. It was not installed as a matcher or
used to import a retail executable tail. The final pure recipe has explicit
origins, scoped allocation cycles, typed operand fields and expected output.

- Keep **530 unique raw C instruction origins** and **nine derived forms**.
  The nine comprise the four already qualified start spill/reloads, an early
  edge-zero copy, split initial/relaxation next-value copies, the selected-
  current copy and the cached-table read in the unrolled-prefix delay slot.
- Coalesce **five raw origins**: the duplicate private frontier store, two
  redundant incoming goal-count reloads, a repeated edge-limit literal and
  the duplicate path-count decrement. No public access origin is omitted.
- Restore the C's selected+1/count-- condition rather than IDO's folded
  count-1 comparison. Restore common private-store blocks and ordinary versus
  likely-branch delays; all targets and entry points are explicitly owned.
- Preserve initial signed count/start roles and later reuse separately.
  For example, retail begins with start/goal-count/avoid-count/goals in
  S2/S3/S1/S6, then reuses those registers for different real values. This is
  not a global register substitution or a physical-register binding in C.
- Retain all **14 relocation entries**, with the correct moved origins.
  The entire unlinked output and binding map equal independently GNU-assembled
  original assembly, including HI16/LO16 and both helper calls.

Operand roles use the existing prepared **Rabbitizer** metadata. A test-entry
import exposed excessive recursion in the initially borrowed cross-experiment
decoder chain; using Rabbitizer removed that unrelated import chain. No
recursion-limit change, package install/upgrade or compiler change was used.
Rabbitizer is already declared by the pinned n64splat requirements.

The normalizer takes only raw C bytes and bindings. Full predecessor hashes,
source definitions/uses, origin ownership, operand-field checks and the output
SHA are enforced. It cannot consult the ROM or filesystem; a test forbids file
reads. The former SP+600 and table/avoid capture closures remain in place.

## Actual Build Integration

Only this function is added to the owner's existing normal-profile overlay.
The primary owner continues to use its established no-unroll profile, and the
other three normal overlays are unchanged. Both raw profiles preserve all
**72 other bodies and pools**. The unselected primary target is still 379
words/frame 1520; it is not silently treated as the selected 535-word input.

Append **535 expected-word rows**, preserving every preceding manifest byte.
There are **426 changed replacement rows and 109 identity fingerprint rows**.
Four actual start-home SW/LW instructions are inserted at output words
97/149/309/338. The exporter linearizes the independently qualified full
origin recipe; these four CSV insertions are not its nine conceptual derived
forms. No NOP padding or new shared-header/data changes.

Both copies execute the actual **seven-command expanded Make shadow**, with
profile flags [1,0], and reproduce the separately qualified padded code and
metadata. Omitting the function-specific normal overlay is an effective
negative: the primary target fails the expected-word gate.

The independent first full link predicts exactly **1,632 changed ELF bytes**:
**1,630 target-code bytes plus two target-symbol-size bytes**, 12 to 2,156.
There is no metadata-section exclusion or symbol-order exception. The actual
production build reproduces that complete first image byte-for-byte:

```text
40623350a4c531d2ef27a110ca30ea329b22e11c1dba97d8554907a674a20132
```

Every one of **6,056 other function bodies**, all **6,057 function addresses**,
and all **189,088 protected Game-data bytes / 720 owners** remain fixed.
The original assembly and ROM inputs are unchanged. Progress CSV is also
byte-identical: this replaces already-counted C, not a newly converted row.

## Fresh Qualification

**19 tests pass in each copy before and after installation**, with zero
skips/errors/failures. Final harness elapsed times:

| Stage | Primary | Standalone Tools Mirror |
| --- | --- | --- |
| Pre-install | 51.244s | 54.134s |
| Installed | 101.933s | 57.892s |

- **426 fixture/stack phases** agree with the independent route/frontier
  reference for output, helper calls/arguments, ordered public stores and
  public memory. Complete final modeled GPR/FPR/condition/private state also
  agrees literally at the same now-valid retail code base.
- **940 fired own-access cuts** compare full modeled state before attempted
  reads/writes: first and last execution per memory PC across four stated
  fixtures in both stack phases. Provider/constructor accesses cannot satisfy
  these gates. The old 426-difference allocation is an effective state
  negative despite agreeing on final RAM.
- A cached goal-count alias changes incoming SP+607 after the second executed
  GOALS-base read. Retail and the fitted routine retain the current scan's
  cached bound in both phases; the old layout reloads it and performs fewer
  public reads. Both requested mutations must fire.
- Two fired inner-flag aliases expose the previously unvisited likely-delay
  word at offset 0x7C8. Coverage is now **539/539 retail words**, not 538.
- **213 native32 C fixtures** pass O0/O2/O3 with trap-mode UBSan. Five compiled
  semantic negatives remain effective; the overflow control still fires
  SIGILL -4. These qualify the underlying actual C body, separately from
  execution of the reconstructed MIPS layout.
- All **213 ordered public-read lists**, 426 complete final memories/start-
  home histories and the existing table/avoid/start/cost/path/flag/F2 aliases
  remain qualified, with their effective old-source/layout controls.
- **Three independent GNU code/data rebases** exercise signed LO16 carries
  and both call bindings; **18 rebased fixture/phases** agree with the actual
  independently assembled original object, not an emitted copy of fitted code.
- **535 raw-word, 14 binding, 535 linked non-binding-field and 131 recipe-field
  controls** reject stale normalization. The guard exporter separately rejects
  all 535 raw-word mutations, and six wrong-image controls reject changes to
  code, neighbors, headers or symbol size.
- All four task files are byte-identical between copies, all eight Python
  copies parse, and both project-tools checks pass. Raw/padded owner neighbors,
  actual Make, guard prefix and full first-image/installed audits all pass.

The modeled condition is not a full hardware FCSR/MMU implementation. Full
connected-provider/gameplay and PC-port acceptance remain separate. Exact
retail instructions/relocations do not imply a fresh host-port qualification.
Older unchanged neighbor-suite receipts are reused through literal whole-ELF
preservation, not reported as newly rerun broad suites.

## Counts And Preservation

Fresh matcher: **Game 3,019/4,832 (62.48%)**, **overall 3,692/5,505 (67.07%)**,
**1,813 different / zero drift**. Init remains 492/492 and Debugger 181/181.
Owner progress is **71/73 exact**, up from 70/73. Converted totals and bytes
remain unchanged. Root README receives aggregate rows only.

All **1,457 pre-existing dirty mirror leaves/statuses** and HEAD `ddbdd16b`
are preserved. Only four absent task files were added: final dirty paths
**1,461**. No mirror commit/reset/stash/clean, push, host/frozen Release,
save/config, dependency/compiler or advisory changes.

```text
Raw normal C: c9cc61e01da4a0bf630aa5ff8a88a5f4b3c3a4a1709e2fd8142a56110fd5b9b7
Bindings:     d773bb14cc8b0e5c4f019c38b74b90010d7d46e5cc0dd2786ab3dd0e2e6d2161
Normalized:   65230441b56e2b5e7a8d7835537454d69ac450452e2268ffecc546a58f35fdf7
Installed C:  c70559485e1f832e727d1fcd19603b013d1ac3010cb357a1f5e171ef762d24e8
Live guards:  deb492afd7196d2c0109980a2b05634af1eacad9cb1fbfc33d84d0d17468a05c
Makefile:     54e393ef0f6c028cbfde10444ffff3581907a0647b0c3b16931ac93c8f3c85cf
```

Ignored receipts: `conker/build/game-route-node-search/loop/captures/qualified/start-home/layout/`.
Primary/mirror pre-install and installed logs/JSON, literal state and alias
receipts, independent originals/rebases, native builds, complete owner/padding/
Make/first-link snapshots, installed fingerprints/audit, mirror preservation
and graph baseline/audit remain there. Keep predecessor fixtures historical;
installed tests first audit the live image, then explicitly use those frozen
inputs. Do not update their old input hashes to silently accept new state.

## Next Target

Continue **func_1508DC24**, 681 words, VA 1508DC24..1508E6C8, still a zero-return
C stub. Read its original routine and direct caller/provider interfaces before
recovering types or importing donor semantics. The owner's other remaining
nonmatch is **func_1508CAD8**, 862 words, likewise still a zero-return stub.
Bank this completed restoration before another broad conversion batch.
The wider Game matching goal remains active and unfinished.
