# Movement Complete Private Byte Match

Verified 2026-10-18. Consumer predecessor `b2f239dc`, tools predecessor
`d5406cd`; both active repositories began clean. The previous goal turn was
progress. Continue complete `func_150F34F4` from
[Note1525](1525-movement-physics-call-register-roles-20261018.md).
Owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM `1209A4..1218A0`.

The isolated, guarded candidate now matches **all 959 retail words**. Its
complete C and raw object are unchanged at **134 raw differences**. The
private table grows from 46 to 134 rows: 86 tail GPR-field changes and two
independent ADDIU scheduling words. No production guards, installation or
matching credit yet. The production source still has its zero-return stub.

| Measurement | Raw C | Previous 46 Rows | Complete Private Match |
| --- | ---: | ---: | ---: |
| Words | 959 | 959 | 959 |
| Frame | 128 | 128 | 128 |
| Different words | 134 | 88 | 0 |
| Exact opening words | 361 | 633 | 959 |
| First unequal PC | `0x150F3A98` | `0x150F3ED8` | None |

## Tail Proof

`tools/experiments/game_actor_input_movement_tail_match.py` protects 319
predecessor entries / 295 distinct paths. The ignored run directory is
`conker/build/game-actor-input-movement-tail-match/`. It reuses the selected
`dataflow-423` source, original owner compiler, parsers, padders and oracles.

The 327-word region is words 627..953 inclusive, PC
`0x150F3EC0..0x150F43D8`, through the final animation call/delay slot.
Its source-to-retail roles form a closed permutation:

```text
11 -> 14, 12 -> 10, 13 -> 24, 8 -> 9, 9 -> 8,
10 -> 15, 14 -> 25, 15 -> 11, 24 -> 12, 25 -> 13
```

The complete control scan rejects incoming interior/computed entries,
control in delay slots and branches leaving the region or entering delay
slots. The only backward edge is the actual counter loop 756->749. Branch
outcomes and likely-slot annulment are overapproximated. All ten mapped
roles must be defined before every read at entry **and after each call**:
calls invalidate the entire role-definition set instead of assuming that
opaque callees return physically permuted scratch values.

All nine call sites and 55 region relocation bindings are locked. The
local analysis has 1,860 states; all ten mapped roles are dead on entry and
none are read by the four-state epilogue continuation. There
is no mapped target/identity collision. O32 argument registers 4..7, stack
addresses and FP fields are unchanged. Unpassed private callee registers
remain outside the ABI qualification.

Four unreachable duplicates 815/842/864/892 are retained and checked
literally. The static analysis visits 323 of 327 tail words; dynamic coverage
is recorded separately. No instruction is inserted, removed or synthesized
from a desired ROM word. All 86 role changes derive from the permutation.

The two other words at `0x150F4098/9C` are independent nontrapping ADDIU
definitions of V0 and A1. Their GP read/write sets are disjoint. No branch
may split the pair or skip into its following word, and neither is a delay
slot. The rewrite swaps both instructions **and** their two LO16 relocation
records for `D_800CC5FC` / `D_800D121C`; all other relocation metadata remains
identical. It does not assume their original high halves will stay equal.

The real padder/link equals the derived 959-word retail sequence. All 134
rows change 163 target bytes, preserving eleven padded neighbors, owner
pools, 959-word extent and frame 0x80. The 46-row research table remains an
exact byte prefix. This is guarded-object matching, not direct C emission.

| Artifact | SHA256 |
| --- | --- |
| Raw target | `4a4c3574716a6ab788981a28d6af57e8bd46c6c01d6a92aed2c100edfc38b5a7` |
| Fully normalized target | `48bbb4778e4843846a24a556baf564bd5634aad2ab19e9bb88648d24b98c88a0` |
| Unchanged isolated source | `0b89776bd3c14abb3f18407fb0f45af318c1803add086c3b60960fdce1b52980` |

## Qualification

The final full sweep passes **21 tests in 231.809 seconds**. Focused tail
controls, kernel and rebases also pass three tests in 37.120s. The first
21-test sweep passed 19 tests and found
two test-fixture expectations: a newly inserted branch made an existing
target a delay slot before the intended backedge test, and provider mode 3
does not fire in this tail. The controls now mutate an existing branch and
use the actual tail modes 6/7. Live-out controls change the compared literal
as well, so a literal mismatch cannot mask the intended dataflow rejection.
Use the documented direct module invocation below; the deeper `unittest`
loader invocation reaches the existing import-chain recursion limit. No
global recursion limit, environment, package or compiler was changed.

- 325 effective tail controls: all 88 changed words, missing/wrong bindings
  at all 55 sites, invalid maps, frame/extent/call/entry/control/boundaries,
  ten source live-ins, 80 reads after the eight intermediate calls, and ten
  physical live-outs. The prior 89 physics-window controls also rerun.
- 324 poisoned tail-kernel cases vary stack phase, RAM pattern, scratch
  GPR seed and provider mode across nine contact/held/release/spawn scenarios.
  Each callee return poisons all ten mapped physical registers independently.
  All six unique callees are exercised; the CFG proof locks nine static call
  sites. Retail, old 46-row and complete-normalized images agree on
  RAM/GP/FP/events/LO/condition,
  public call packets and pre-call RAM/FP boundaries. The kernel visits 313
  words; it does not claim all 327 were dynamically covered.
- 24 actual independent bound-symbol rebase cases / 48 links cover three
  bases, signed-low/high-carry behavior, 1/3/24/25 records and two stack phases.
  Raw and normalized actual objects agree on exact record reads, count,
  final cursor/end and access events. These are real metadata-driven links,
  not patched literal addresses or a full data/hardware rebase claim.
- All 392 selected private paths now complete: 100 active states / 11,276
  equal access-fault prefixes, 80 disabled / 2,700, 160 mode-zero / 8,320, and 52
  extra spawn/release states / 8,333. Total 30,629 equal prefixes. All 100 old
  46-row controls fail at `0x150F3EE0`, after 8,844 equal prefixes. There is no new
  frontier in the selected normalized cases; arbitrary FCSR/hardware/private
  caller contracts are not claimed.

The unchanged compiler capture and 32 source screens are explicitly reused,
not rerun. Fresh qualification still requires source/normal/observed/raw
identity, 74 emitter events / 687 AS1 records, unchanged homes/layout and five
pitch-site controls. The final sweep freshly passes the complete 2,496-case
public corpus, twenty modeled FP edges, nine provider modes, 947 reachable
retail words and twelve retained duplicates. Native32 O2/O0 UBSan passes
397 cases/profile and eight controls, two text rebases/twelve cases and
twelve established guest aliases. The prior release/speed/signed-Y/clamp,
counter, surface, 640 coefficient and 576 physics-kernel cases also rerun.
These checks complement, rather than substitute for, the new tail gates.
Zero Claude calls: existing bounded proof tools answer this routine question.

## Checkpoint And Installation

Tools **cc0020c** is committed first. Both tools copies pass twelve shared
tests and smoke checks, four ASCII/AST parses and two byte-identical task
pairs. All 319 protected entries / 295 paths, 6,057 installed bodies,
189,088 Game-data bytes / 720 owners, callback slot `0x80086068` and ten
immutable first-image members remain unchanged.

Both mirror destinations were absent before copying. All **1,176** prior
hashes and HEAD `ddbdd16b` survive, with **1,178** dirty mirror paths afterward.
No duplicate mirror commit/reset/clean, host-port or frozen Release action,
dependency update or push. Main README is unchanged.

Production ELF remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
Fresh production totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different, zero drift; Init 492/492 and
Debugger 181/181 among converted functions. No production build is claimed.

The next operation is **production installation**, not another register
window. Live ELF preflight confirms the existing symbol row at file offset
`2833936`, entry `0x150F34F4`, size 12, section 5. The qualified routine is
3,836 bytes. Before changing production:

1. Predict the complete successor from the frozen first image: recovered
   semantic owner/typed actor argument/comment, append-only 134-row production
   guard extension including the two moved LO16 records, target slot and
   declared symbol-size change. Account for any named symbol serialization
   explicitly; do not blanket-exclude metadata or relax frozen hashes.
2. Archive the immutable predecessor/successor fixtures and qualify exact
   historical adapters needed by existing movement/burst research. Preserve
   all current protected inputs and unrelated owner routines.
3. Install the qualified source/guards, build/link the real ELF and CSV,
   audit every function/address/extent plus all Game data and callback slot,
   then rerun focused target/adapter/shared checks on installed artifacts.
4. Only after that audit, advance matching totals and README aggregate rows,
   bank coherent tools/consumer commits and continue the wider Game goal.

```sh
python3 -m tools.experiments.game_actor_input_movement_tail_match
python3 -m tools.tests.test_game_actor_input_movement_tail_match -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

- [x] Close all 88 remaining private differences with a proved permutation
  and independent symbolic address schedule; match all 959 words.
- [x] Pass the complete 21-test sweep and bank this research checkpoint.
- [ ] Install and audit the actual production successor before taking credit.
- [ ] Keep caller/provider/hardware acceptance, the other gate and both fade
  lifetime gaps, and the wider Game matching objective open.

The scoped AST graph refresh completes with **42,351 nodes / 82,471 links /
3,968 communities**. The new note is indexed. Only three shifted UPDATE_LOG
heading IDs disappear, with all labels retained at new locations; no
unrelated nodes are lost. All 19,398 existing excluded nodes from 2,972
still-present files survive without a purge or full re-extraction. The new
tools modules have no nodes in this consumer graph; no newly indexed helper
ASTs or changed scan settings are claimed.
