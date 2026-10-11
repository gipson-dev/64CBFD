# Actor Definition Count Direct Conversion

Date: 2026-10-10

Continue [Note 1234](1234-game-actor-definition-lookup-direct-conversion-20261010.md).
Convert complete func_1507E968 from GLOBAL_ASM to directly byte-exact C and
extend actual channel-caller qualification through the count, lookup,
classifier and list helpers. The wider Game matching goal stays active.
This is not host or full-game acceptance.

## Scope And Baseline

- Consumer starts clean at 7b622f24, mounted tools clean at 6bc9c5a. Single
  Codex writer, zero Claude calls. Keep-committed authorization: tools first,
  consumer source/docs/tools pin second; no push.
- Owner conker/src/game/generated_AB760.c; VA 0x1507E968..0x1507E9E8,
  ROM 0xABE18..0xABE98, 32 words / 128 bytes, original 0x18 frame.
  Keep original assembly and nonmatchings copy. Local graph has no target
  node; read the complete routine and all three direct caller interfaces.
- Seven immutable before-* snapshots cover owner, ELF, guards, conversion
  CSV, protected rodata, tracked symbols and ignored undefined assignments.
  Before-source SHA-256
  2a54f461df2ce9a06698ed139c686598a9832d775aef7b51a40e97bed8dd0080;
  ELF bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
  Retain and recheck every hash; do not rewrite the baseline after installation.
- Older tools remains ddbdd16, independently dirty: 233 native Windows Git
  entries before, 235 after two absent-path authored mirrors. Both exact
  mirrored Python parses pass. Preserve tracked-dirty fingerprints
  game_owner_pool.py
  159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E and
  test_game_node_effect_registration_match.py
  C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input edits.

## Recovered Behavior And Match

Read unsigned actor byte +4. Special ID 150 bypasses func_150849A0 and selects
archive slot 150 directly; all other actor bytes call the classifier. Full-word
classifier result 255 returns zero. Otherwise read its live D_800D1C90 entry;
null archive returns zero. Move the cursor back eight bytes and return the
unsigned word at header +4 divided by ten. The maximum quotient 429,496,729
fits the existing signed-word return contract. No additional ID/count clamp.

The initial nested-if C emits 28 words with 26 positional differences. A
repeated-byte conditional expression and explicit sentinel early return
recover all 32 words. Special-first conditional emits 32 words with six
control-flow differences; invert it to put the classifier call first and emit
every retail word directly. Normal O2/g3, original 0x18 frame, no guards,
insertions, omissions, diagnostics or pools. Retain JAL at +0x18 and global
table HI16/LO16 at +0x44/+0x4C. No alternate profile or missing-body padding.

Retail restores RA before its table/header reads, including the sentinel
path. The initial actor byte decides whether the callback occurs; later
callback changes to actor +4 do not reselect the special path. The table and
header remain live after the callback. Compare scalar V0 and every private
read/write/call, not just final public state. All 32 words are emitted; 31 are
reachable. The original redundant MOVE at word 10 is unreachable and is not
credited as executed by the coverage gate.

Authored tools: [complete candidates](../../tools/experiments/game_actor_definition_count_candidates.py),
[qualification and linked audit](../../tools/tests/test_game_actor_definition_count_match.py).

## Fresh Qualification

- 16,352 cases / 32,704 original/C guest executions pass an independent full
  private-order reference. Cover every actor byte and classifier byte,
  special/sentinel/null paths, low/exact division boundaries, unsigned high
  words, wrapping full-word classifier carriers and two stack phases. Mutate
  live table/header/actor fields in the callback, clobber caller GP/FPR and
  verify saved registers, stack and return address. Reach all 31 reachable words.
- 380 alias/actual-classifier cases / 760 runs pass. Execute the actual
  banked 11-word classifier; all ten reachable words execute, dead word excluded.
  Include actor/header, actor/saved-RA, header/saved-RA and global-table/private
  stack aliases. Fire 100 strict access-fault pairs / 200 failed runs and
  compare prefix memory, events and calls. Missing or wrong faults reject.
  Synthetic alias faults qualify guest instructions, not portable C faults.
  High-word classifier addresses are emitted O32 probes, not native C or real
  asset-domain acceptance.
- Eight independently linked original/C binaries at four entry/classifier/table
  rebases pass 256 cases / 512 runs, including signed LO carry boundaries.
  Relocations remain original; no guards or replacement addresses.
- Complete production-profile copied-owner compile/post-process/actual padder
  has zero diagnostics. Target bytes, all 14 neighbors, extents, relocations
  and pools are exactly equal using the unchanged manifest.
- Six effective freshly compiled IDO negatives reject wrong special/sentinel
  IDs, signed header, eight-byte divisor, wrong header offset and narrowed
  full-word classifier carrier. Two native signed/special negatives also fail.
- Complete native32 C at O2/O0 passes 1,835,008 cases per profile, 3,670,016
  runs. Cover all 65,536 actor/classifier-byte pairs, nullable archives, live
  table/header mutations, unsigned high-bit sizes and every low-halfword size.
  Compare the full actor, global table and header; single-argument ABI,
  skipped special callback and scalar result qualify. Buffers/classes are
  synthetic; do not claim all class IDs exist in real assets.
- Execute actual banked 73-word func_1507E7E4, both 32-word count forms,
  24-word func_1507E908 and 11-word classifier in 1,344 cases / 2,688 runs.
  Independent nested-frame replay qualifies strict less-than count gate,
  sentinel/special/null branches and descriptor/list-present paths. Fire 276
  connected fault pairs / 552 failed runs. List/animation/finish callbacks in
  this first matrix are bounded, not actual-body acceptance.
- Additional actual-list connection: banked 19-word func_1507E9F8 and original
  D_8009D910 bytes 05 06 07 0A 0B execute with the complete channel/count/
  lookup/classifier chain in 432 cases / 864 runs. Fire 372 connected fault
  pairs / 744 failed runs. Qualify real list-null/default-list behavior and
  first/fifth animation selection; no fabricated list return. The caller
  supplies NULL output-count pointer, so nonnull list-output paths remain a
  separate gate. Actual animation and finish bodies are still bounded.
- Inspect func_1507E500 and func_15080430 interfaces: full signed-word count
  comparison in the former and signed positive-count gate in the latter.
  Their complete executions, real resources, hardware and gameplay stay open.

## Linked Audit And Progress

All ten final post-install tests pass in 33.038 seconds. Root tools-check,
older standalone tools check and both mirrored Python parses pass. Source-only
rebuild has no changed-owner compiler diagnostics; preserve the existing
duplicate generated_12D630 Makefile recipe warning.

Whole linked ELF is byte-identical: 3,261,160 bytes, SHA-256
bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
All addresses, extents, symbols, headers, sections and every instruction/data
byte remain exact. Guards, protected rodata, tracked symbols and ignored
assignments are also byte-identical. Protected data: 189,088 bytes / 720 owners /
zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Only the 128-byte target CSV row changes asm -> c; every other row and both
repeated section headers are exact. Current CSV SHA-256
be7d0a68b42aa93e75c17674b98c72f2c8a25699d18e484af9aaf4b010494c98;
installed source SHA-256
bb5309d25735e87d63fc76c7bd7be33d2a51e9eb1584bd3892591640f61fd180.

Fresh conversion: total 5,493/6,043 (90.90%), 1,940,940/2,256,728 bytes (86.01%);
Game 4,820/5,322 (90.57%), 1,769,504/2,072,880 bytes (85.36%). Init/debugger
and all denominators unchanged. Delta +1 converted function / +128 C bytes.
Fresh matching: Game 2,770/4,820 (57.47%), total 3,443/5,493 (62.68%), zero
drift / 2,050 different. Delta +1 matching credit; different count unchanged.

```sh
python3 -m unittest tools.tests.test_game_actor_definition_count_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Bank mounted tools 2c8eae2 before consumer source/docs/tools pin, no push.
Root README receives aggregate rows only. Earlier broad neighbor receipts
remain historical, not fresh tests; their linked bodies and guard/data history
are unchanged by this full audit. Eight added relative links pass, zero broken.
Native Graphify update after final code edits refuses unsafe shrink
39,524 -> 17,751 nodes, retaining 19,398 nodes from 2,972 excluded-but-existing
files. Preserve that refusal, skill 0.9.20/package 0.9.26 and devcontainer.json
zero-node warnings, no force/purge/install. The separate consumer hook requires
fresh log growth/completion and zero workers before reporting clean.

An intermediate fixture incorrectly borrowed a method containing a class-bound
super() for an unrelated caller subclass; fix the local unsigned-DIVU override.
The independent list replay also used return PC +0xD4 instead of retail +0xD0;
correct it from the actual JAL. Neither was a production defect or a reason to
weaken memory/order gates. Rerun the full ten-test suite after both fixes.

## Next And Boundaries

Next: complete 30-word func_1507EA44, still GLOBAL_ASM in the same owner.
VA 0x1507EA44..0x1507EABC, ROM 0xABEF4..0xABF6C, original 0x18 frame.
Preserve zero-index skip, nullable actual list helper, full-word one-based list
index, saved third integer argument, signed-word-to-single conversion and
global float multiplication before func_15083568(actor, animation, scale, 0).
Recover the mixed O32 argument contract and keep FCSR/nonfinite/native/runtime
acceptance separate. The existing 19-word list C is already byte-exact; do not
invent another matching credit for it. Other callers/deeper callbacks and
gameplay remain open. Zero Claude calls; no billing or goal-completion claim.
