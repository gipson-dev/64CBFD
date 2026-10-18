# Movement State Machine Installed

Verified 2026-10-18. Consumer predecessor `89a15c69`, tools predecessor
`cc0020c`; both active repositories began clean. The previous goal turn was
progress. Continue the full private qualification from
[Note1526](1526-movement-complete-private-byte-match-20261018.md).
Owner `generated_11FF10`, function `func_150F34F4`, VA
`150F34F4..150F43F0`, ROM `1209A4..1218A0`, 959 words / 3,836 bytes.

The production zero-return placeholder is replaced by complete C for
controller input, movement, linked-record updates and animation. Its typed
`MovementActor34F4 *actor` interface and descriptive comment are retained.
The installed ELF now matches **all 959 retail words**, with frame 0x80.
Raw C still differs in 134 words; the appended 134 production guards normalize
the qualified register roles and two independent address-setup words. This
is a guarded byte match, not unguarded compiler emission or a gameplay claim.

## Complete Successor

`tools/experiments/game_actor_input_movement_installation.py` captures 321
predecessor entries / 297 distinct paths and reproduces the original full
ELF before any production edit. The qualified owner is substituted into
the complete existing linker script, not measured only in isolation.

The first comparison rejects 567 unaccounted metadata bytes even though
canonical named definitions agree. The closed prediction then accounts for
22 explicit symbol/string serialization groups containing 54 unchanged
definitions. Each group locks its names, values, sizes, attributes, section
indices and string positions. No symbol section or metadata bytes are
excluded. The 44 effective group-order/definition controls reject corruptions.

| Complete ELF Change | Different Bytes |
| --- | ---: |
| Target retail instruction slot | 3,010 |
| Target symbol size 12 -> 3836 | 2 |
| Explicit symbol/string serialization | 567 |
| Total | 3,579 |

The real production link equals this complete first prediction byte for
byte. All 6,057 function bodies and every function address are audited:
only `func_150F34F4` changes. Every other named definition is preserved;
the target's declared size grows from 12 to 3,836. All 189,088 Game-data bytes
across 720 owners and callback slot `0x80086068 -> 0x150F34F4` remain exact.

The actual production object's target bytes **and all 167 relocation sites**
also equal the qualified padded object. This binds the independent-data
rebase tests to the production target, not merely equal final linked words.
Two actual-object corruption controls reject changed bytes or relocations.
Only the two intended LO16 records change position in the guard extension.

| Installed Member | SHA256 |
| --- | --- |
| Complete ELF | `db5587cb50d49f0ffc3de024bfc87c234d42e499667cc26d624839f4e3bff286` |
| Semantic owner | `0a7787b4ba8e2d190ee76e5adcd0eb23edd8ee5adbe8f2e44884f514cdd21c52` |
| Append-only guard manifest | `3f60679be81037a4035cd35f7b87a85db8764d0ccad1d68b3695bbce6a497e9b` |
| Normalized unlinked target | `48bbb4778e4843846a24a556baf564bd5634aad2ab19e9bb88648d24b98c88a0` |

## History And Tests

`tools/tests/movement_install_checkpoint.py` pins exactly three predecessor/
successor pairs: ELF, owner and guards. Its explicit serial historical view
returns predecessor bytes only for those exact known members. It rejects
unknown live bytes, corrupted before/after fixtures, mixed states and nested
views, and restores both readers even after exceptions. Other paths are
untouched. No previous recovery source, test, baseline hash or ten-member
older first-image fixture is rewritten or weakened.

Historical research runs only inside that view. The installed behavior
suite first extracts the actual 959 words through the unmodified reader,
requires equality with the qualified object, and binds the behavior oracles
to those installed words. Whole-image and production-input audits run outside
the view. Do not present historical predecessor checks as fresh reads of
the physical installed ELF. Use the installed-suite command below instead
of running an old pre-install recipe directly against the successor.

Fresh checks:

- Pre-install complete-image/history/serialization qualification: three
  tests pass in 58.192s before either production source edit.
- Installed suite: **25 tests pass in 292.679s**. The strengthened actual-object
  audit then passes its focused rerun in 10.694s, including both corruptions.
- The 21 behavior checks rerun the 2,496-case public corpus, twenty modeled
  FP edges, nine provider modes, 947 reachable retail words / twelve retained
  duplicates, and actual curve calls. Native32 O2/O0 UBSan retains 397 cases/
  profile and eight controls, with the existing text rebases and guest aliases.
- Complete private equality: 392 states / 30,629 fault prefixes, including all
  active, disabled, mode-zero and extra spawn/release paths. The old 46-row
  controls still reject at `0x150F3EE0` after 8,844 equal prefixes.
- Tail 325 controls, 324 poisoned tail cases and 24 independent bound-symbol
  rebases / 48 real links rerun. The actual counter reads exactly 1/3/24/25
  records under the rebases. Prior coefficient/physics kernels and their
  stale-word/relocation controls rerun as part of the installed suite.
- Fourteen exact-history controls, 44 symbol-serialization controls and the
  two actual-object controls pass. All 321 protected entries are accounted
  for: three declared production successors, all remaining paths unchanged.

The 32 unchanged source screens and completed 74-event/687-AS1 compiler
capture are explicitly reused, not recaptured. The selected C and normal
compiler profile are unchanged; normal production compilation uses existing
O2/g3/mips2/o32 flags. No dependency/compiler/REA setup change or Claude call.
No arbitrary caller-private/FCSR/hardware/full-game or host-port acceptance.

## Build And Progress

The source patch is applied only after the complete prediction is locked.
The generated guard extension preserves every prior byte, including its
physical CRLF endings. The existing Git LF-conversion warning does not
change the parsed rows; this task does not change line-ending configuration.

The real owner is compiled by its normal Make rule **with the new guards**.
Only afterward does `-o retail_word_patches.us.csv` suppress unrelated
owners' global CSV-timestamp rebuilds. This is justified by the exact old
guard prefix and final whole-ELF audit; it does not skip the target padder.

```sh
make -C conker -j4 build/src/game/generated_11FF10.c.o
make -C conker -o retail_word_patches.us.csv -j4 build/conker.us.elf progress.csv
python3 -m tools.tests.test_game_actor_input_movement_installation -v
make -C conker -o retail_word_patches.us.csv match-progress NON_MATCHING=1
make tools-check
```

The installation predictor (`python3 -m tools.experiments.game_actor_input_movement_installation`)
is a **pre-install** operation. It is frozen to the predecessor; do not relax it to accept the live
successor. Earlier private commands in Note1526 now require the historical
view. Current audits/tests use the immutable installation fixtures in
`conker/build/game-actor-input-movement-install/`.

| Linked Matching | Before | Installed |
| --- | ---: | ---: |
| Game | 2,965 / 4,828 (61.41%) | 2,966 / 4,828 (61.43%) |
| Total | 3,638 / 5,501 (66.13%) | 3,639 / 5,501 (66.15%) |
| Still different | 1,863 | 1,862 |
| Address drift | 0 | 0 |

Init 492/492 and Debugger 181/181 remain exact among converted functions.
Conversion counts/bytes are unchanged: the old placeholder already counted
as C. The main README changes only the snapshot date and two aggregate
matching rows; no function narrative or gallery change.

## Banked Continuation

Tools **ddd9d88** is committed before the consumer pin. Both copies pass
twelve shared tests and smoke checks, six ASCII/AST parses and three
byte-identical task pairs. All 1,178 prior mirror hashes and HEAD `ddbdd16b`
survive; the mirror has 1,181 dirty paths afterward. No duplicate mirror
history, reset/clean, push, host-port sync or frozen Release action.

- [x] Install the complete semantic movement body and 134 qualified guards.
- [x] Close the full first-image prediction and actual owner/ELF/data/callback
  audit with zero metadata exclusions, then pass installed behavior tests.
- [x] Update measured aggregate matching and bank coherent tools/source/docs.
- [ ] Continue Game matching. Fresh ranking's closest remaining body is
  `func_15095D34`: 346 words / 18 real differences. Read the rectangle native
  temporary/blocker handoff in Note1440 and the no-gain step screens in
  Note1441 before editing; do not substitute unsafe stack-lifetime guards.
- [ ] Keep the other gate, both fade lifetime gaps and complete caller/
  provider/hardware acceptance, plus the wider Game objective, open.

The scoped AST refresh completes with **42,360 nodes / 82,479 links / 3,945
communities**. The installed function is indexed at its actual source line307
and the new note is indexed. Only three shifted UPDATE_LOG heading IDs are
lost, with all three labels retained; no unrelated nodes disappear. All
19,398 existing excluded nodes from 2,972 still-present files survive without
a purge or full re-extraction. The new tools modules remain outside this
consumer graph's scan; no fresh helper indexing is claimed.
