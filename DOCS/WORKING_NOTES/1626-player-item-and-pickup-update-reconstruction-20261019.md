# Player Item And Pickup Update Reconstruction

Date: 2026-10-19. Consumer predecessor: `16d14db1`; tools predecessor:
`27fb65e`. Tools checkpoint **e707d3e** is committed first. No push.
The previous goal turn completed an installed match; this turn makes progress
on the next function. The wider Game matching goal remains active.

## Scope And Source Evidence

Recover **func_1508DC24**, VA **1508DC24..1508E6C8**, ROM **BB0D4..BBB78**,
**681 words / 2,724 bytes / frame 0x118**. The installed definition at
[generated_B3020.c](../../conker/src/game/generated_B3020.c) remains its
three-word zero-return placeholder. **Nothing is installed and no new match
credit is claimed.** Preserve its original name when installation is qualified.

The complete [retail routine](../../conker/asm/B3020.s) and its direct
`func_1509DFC4` command-dispatch caller at 1509E108 establish a **void(void)**
interface: no incoming argument is used, and the caller ignores the result.
The old `s32 func_1508DC24()` placeholder is not ABI evidence. The routine
updates per-player item states/effects, then pickup timers, placement and
collection ownership. The candidate has meaningful locals and a short purpose
comment, not physical register bindings or handwritten executable assembly.

The separately audited donor `Another Source/CBFD-Recompiled/conker/conker/src/game/game_B3020.c`
was consulted as a control-flow reference, not imported. Its broad integer
casts misrepresent byte and halfword accesses, word-indexed tables, object
pointers and the event helper's integer player argument. Recover widths and
calls from retail assembly and the actual local provider definitions instead.

## Reconstructed C

[Candidate source](../../tools/experiments/game_pickup_state_update_candidates.py):
`INITIAL` is the complete readable array-indexed reconstruction; `SELECTED`
is its semantically equivalent byte-cursor tail. Both compile using the
prepared IDO 5.3 and existing O2/g3 owner profiles. No compiler/dependency,
Makefile, shared header, padding or word-guard changes.

| Complete Source | Words | Frame | Counted Differences |
| --- | --- | --- | --- |
| Initial array-indexed form | 682 | 288 | 666 |
| Selected byte-cursor form, either profile | 680 | 280 | 665 |
| Retail | 681 | 280 | 0 |

The 665 differences comprise **664 overlapped word differences and one missing
word**. Equal frame size and public behavior are not a byte match. The normal
and primary no-unroll profiles emit identical selected target bytes. Two
explicit actor-base controls also emit identical bytes to their corresponding
initial/byte-cursor forms; they are not additional source improvements.

Preserved details include:

- Signed halfword mode, byte current-state masking and distinct nausea bounds.
  Mode B9 can skip a player without refreshing the cached player count.
- The two animation queries, remove/start event order, paired 1D/1E behavior,
  full-width desired state arguments and mode-B8 byte/halfword updates.
- Different attached-effect preservation lists for mapped and unmapped states;
  the unmapped list additionally retains 2C/64. Stop cleanup at the first
  qualifying type-6E object, not every matching object.
- Signed-byte rotating selector, including 127 to -128 wrap; byte-3 pickup
  selector loads; cached opening table pointers with live global-state reloads.
- Separate grace/respawn countdowns, signed comparisons, saved coordinate
  narrowing and one cached floating random scale. Random placement rejects
  used target IDs before node lookup.
- Preserve the caller's **32-bit -1 node test**. Provider result 255 is not
  silently reinterpreted as signed-byte -1. The bounded coordinate provider
  writes all three outputs; this is not qualification of an invalid real
  node/coordinate chain that leaves original stack outputs uninitialized.
- Byte addition wraps before the charge clamp; owner writes use the pickup
  loop counter and the captured original owner table, even after a helper
  redirects the global state pointer.

## Focused Qualification

[Independent reference and bounded providers](../../tools/tests/game_pickup_state_update_oracle.py)
are separate from the candidate. The
[target suite](../../tools/tests/test_game_pickup_state_update_match.py)
passes **eight tests in each copy**, zero skips/errors/failures. Final harness
elapsed times are **34.378s primary**, **34.880s standalone mirror**.

- **234 cases**, both stack phases 0/8 and both actual compiled profiles:
  **936 completed candidate fixture/profile/phases**, plus 468 retail phases.
  Complete public memory, ordered public stores, canonical typed helper calls
  and all requested helper writes agree with the independent reference.
- **All 681 retail words** are visited. The earlier 14 uncovered words are
  closed by selected-B8, B8-leave-128 and same-state collection cases.
- All **936 ordered public-read sequences** match retail, with zero sequence
  differences. Private output-pointer addresses are canonicalized only for
  the list/coordinate helper contracts, not treated as proven equal homes.
- **234 native32 fixtures at O0/O2/O3**, with trap-mode UBSan, pass. Native
  fixtures translate pointer fields explicitly and preserve the big-endian
  byte-3 selector carrier; they compare the complete mapped public buffer.
- **Six independently compiled semantic negatives are effective**: missing
  current-state mask, wrong nausea threshold, wrong unmapped-44 preservation,
  wrong charge increment, uncached scale and conflating -1 with byte 255.
  Exit codes are 23/23/22/24/23/22. The actual installed placeholder is also
  an effective guest negative. The first test was observed failing on the
  empty stub before the complete implementation was written.
- Both complete owner profiles retain all **72 other raw bodies and pools**;
  the selected target bytes equal isolated compilation. All **seven production
  inputs** remain pinned and unchanged, including the installed ELF and guards.
- Both project-tools smoke checks pass. Three new task files match byte-for-
  byte between copies and all six Python copies parse.

This is bounded public-state qualification, **not** literal private/register
or fault-prefix equivalence, complete FCSR/MMU simulation, connected real
provider-chain acceptance or host gameplay qualification. In particular,
matching public access sequences in these fixtures does not establish all
possible alias/capture behavior or the original local-array capacity contract.

## Fingerprints And Artifacts

```text
Selected semantic C: 55aeddec4d8e8d2d354c9daa6defc8870e9d5bf86f6e308c1ebc87877fc6ec49
Selected raw target: 899a737e40358f6a0842007c5404d9040bed2c583f92ec155377121f6f3be5f7
Initial raw target:  89de8350df19981b80193065d06614a7e67fa27c24b207b48665abaf15498a09
Selected bindings:   77 relocation entries
Installed ELF:      40623350a4c531d2ef27a110ca30ea329b22e11c1dba97d8554907a674a20132
```

Ignored artifact root: `conker/build/game-pickup-state-update/`.
Retain primary/mirror final logs/run JSON, `test/test-receipt.json` and its
mirror counterpart, public-read differences, native executables/fixtures,
negative receipts, frozen inputs, selected bindings, owner profiles and
`final-audit.json`. `shape/diagnostic-shapes.json` is diagnostic only:
632 common normalized instruction shapes / 47 differing blocks, with register,
branch-target and private-displacement fields ignored as explicitly recorded.
It is not an origin recipe, matching gate or permission to copy missing words.

All **1,461 existing dirty standalone-mirror leaf hashes/statuses** and HEAD
`ddbdd16b` are preserved. Only three absent task files were added, leaving
**1,464 dirty paths**. No mirror commit/reset/clean/stash, host/frozen Release,
real save/configuration, dependency update, push or advisory call.

## Next Matching Work

1. Continue this same complete `SELECTED` C, not the 862-word other stub yet.
   Recover the missing functional word and original value lifetimes/schedule;
   keep the 280-byte frame, 77 bindings and complete public-state gates.
   Retail preloads constants 22/2A before the player loop and uses a separate
   skip continuation. The diagnostic first blocks locate these differences.
2. Recover real private homes and callee-saved role lifetimes. Add fired local-
   home/call-save aliases, complete modeled final state and first/last own-
   access cuts. Do not infer private parity from public reads or total length.
3. Qualify any eventual normalization using explicit C instruction origins,
   stale-input controls, independent GNU original-assembly rebases and actual
   owner padding/Make selection. No dummy storage, NOP padding or retail tail.
4. Require a strict declared first linked-image audit, installed target tests
   and fresh aggregate recount before production installation or match credit.
   Root README remains unchanged during this experiment. Its existing totals
   remain Game 3,019/4,832, overall 3,692/5,505, 1,813 different/zero drift because
   the installed ELF is byte-identical to Note 1625; no new build/recount is
   claimed here. Keep the wider Game goal open.
