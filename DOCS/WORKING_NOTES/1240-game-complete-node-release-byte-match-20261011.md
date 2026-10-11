# Complete Node Release Byte Match

Verified locally: 2026-10-11. One committed function checkpoint in the active
Game matching goal, not complete resource loading or hardware/live gameplay.

## Result And Baseline

Recover complete func_15030158 in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c): VA
0x15030158..0x150302F0, ROM 0x5D608..0x5D7A0, 102 words / 408 bytes,
original 0x20 frame. Replace the false zero-return placeholder with semantic
release/unlink code; every final linked word matches retail. Preserve original
assembly in conker/asm/5D2C0.s and existing O2/g3 profile. No pools, instruction
insertion/omission, layout or symbol-assignment changes.

Baseline consumer 0afcf493241018eac097f407e1f738758a34b266; mounted tools
8ec84847451503994e2dde7121892568c99d799b. Baseline source SHA-256
0ab470e18a81ccdb3dd435a55831a3e19cce4dac72fcaaa7a6f3b5aaf0943b85;
baseline ELF 9c8e1b09667b0fd9ee9aad0cd36bc44e98048c2388bc430d604093a4fdc46ebc.
See [Note 1239](1239-game-complete-node-resource-initializer-byte-match-20261011.md)
for the already banked 96-word initializer and its required loader outputs.

Tools 088efd42a4e25aae38a5f73e9f9859a43e9fccb9 are committed first, then
consumer source/guards/docs/tools pin, no push. Single Codex writer; zero
Claude calls because complete compiler experiments, independent references and
effective negative controls settle this routine locally. No bridge, account,
dependency or shared-helper changes; no token-cost claim. Preserve OGL, frozen
Release, saves/editor state and private inputs.

Older standalone tools HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a remains
unchanged. Mirror only three absent authored paths: dirty entries 246 -> 249.
All three mirrors byte-equal; six AST parses and both tools checks pass.
Protected game_owner_pool.py and node-effect-registration test hashes remain
unchanged. No overwrite, reset or duplicate old-checkout commit.

## Complete Contract

1. Recover void func_15030158(u8 *node, s32 immediate). The full 32-bit mode
   treats every nonzero value as immediate, including 256 and the sign bit.
   Mode zero first calls the already restored 134-word func_15031C14 action
   cleanup dispatcher. Reload node byte 9 after that call.
2. If byte 9 is nonzero, read byte 8 and the live mode home. Nonzero byte 8
   releases the two owned pointers at 0x28/0x2C: immediate func_10004074 or
   delayed func_100043B4(pointer,4). Do not suppress NULL owned-pair calls.
   Capture the mode for the pair, but reload the second pointer after the
   first callback. Release non-NULL attachment 0x48 through func_1503F7B8,
   then submit the live unsigned resource-kind byte 1 to func_1518CA04.
3. Nullable auxiliaries 0x34/0x4C/0x50 follow their separately reloaded live
   immediate mode. Auxiliary 0x44 always uses immediate free, even in delayed
   mode. Preserve retail reads of mode homes even when nullable fields are
   zero; callbacks may change public fields or escaped guest stack homes.
4. Compare the node with live D_800C3EE0; if it is the head, publish the live
   next pointer at 0x54. Capture live previous at 0x58, updating its 0x54;
   capture live next at 0x54, updating its 0x58. Preserve actual read/write
   order and callback-driven link mutations. No wrapper field clearing.
5. Always free the node last, after unlinking. Restore S0/RA/SP. The final
   callback's incidental V0 is not a status-return API. Both actual direct
   callers ignore it: the 33-word group walker owns its own result, and the
   152-word factory returns NULL on rollback. Their linked bodies stay exact.

The factory and initializer now execute this real release body on failure.
Deeper func_1502FE10/func_1503F62C still return zero without writing required
success outputs. Do not hide that gap with a zero-initialized source local or
claim complete resource restoration. Bounded free/queue receipts qualify
submission order, not actual allocator lifetime, attachment or resource work.

## Source Fit And Guard Boundary

The complete selected semantic body emits 102 words, original 0x20 frame,
zero pools and five differences with no compiler diagnostics. Register hints,
unsigned mode and additional local/evaluation forms do not improve the fit;
volatile mode emits 103 words. Narrowed byte mode is semantically invalid.

Five expected-word guards close the auxiliary-0x44 register transfer: three
loads use V0 instead of A0, the nullable branch tests V0, and the free-call
delay slot transfers V0 to A0. No memory/call reordering, inserted instructions
or omitted instructions. All fifteen JAL sites and the head's HI16/LO16 sites
retain their exact offsets and symbols. Require the entire 102-word raw body
and 17-site relocation fingerprint: 102 independent stale-word mutations and
17 stale-symbol mutations reject. Duplicate/stale publication rejects.

Raw compiler, retail and fitted bodies agree with the independent full
ordered reference, including memory accesses and calls. This is not just
final-state agreement. Guest-only private aliases and fired fault prefixes
qualify emitted code; do not claim portable C fault or freed-object semantics.

## Fresh Qualification

[Target suite](../../tools/tests/test_game_node_release_match.py) passes all
ten tests before installation (60.969s) and after the full rebuild (56.438s).
Reuse existing compiler, guest oracle, native32, production padder, owner-pool
and data-layout helpers; no shared helpers changed.

- 11,776 cases / 35,328 runs: all 256 initialized/copied/kind bytes, full-word
  nonzero modes, every seven-pointer NULL mask, isolated/head/middle/tail list
  shapes and two stack phases. Compare independent complete ordered reference
  with raw/retail/fitted forms; all 102 retail words fire. Clobber caller GP/FPRs.
- 136 mutation/alias cases, 401 fired fault triples / 1,203 failed runs:
  dispatch-driven flags, live pair second pointer, attachment-driven kind,
  resource-driven auxiliaries/head/links, escaped mode-home mutations, head
  overlapping node links and a private-stack node. Required NULL node read
  fails at byte 9. Every injected fault is checked to have actually fired.
- Nine independently linked forms at three placements, 672 cases / 2,016
  runs: all five callbacks/fifteen JAL sites and independent head HI16/LO16
  signed-carry placements. No hard-coded retail callback addresses in guards.
- Complete copied-owner compile/post-process/actual padder: zero diagnostics,
  pools unchanged, all 39 neighbors' bytes/extents/relocations exact. Corrected
  void interface leaves both direct callers and deeper zero stubs unchanged.
- Ten effective fresh IDO negatives: narrowed/exact-one mode, signed kind,
  suppressed dispatcher, wrong delayed queue mode, wrong owned-pair pointer,
  delayed 0x44, missing final free and wrong previous/next link fields.
- Native32 -O2/-O0: 48,640 cases each / 97,280 runs; independent release
  reference compares complete nodes/head/call packets, all flag/kind bytes,
  nullable masks, full-word modes and live callback changes. Three native
  negatives also fail. Free/queue callbacks are bounded, not real deallocation.
- 6,144 cases / 18,432 runs execute actual 134-word cleanup dispatcher and its
  ROM-verified 192-byte/48-entry owned table. All action bytes, cleanup keys,
  nullable actor and counter states compare independent cleanup public
  effects/calls. 222 fired connected fault triples / 666 failed runs.
- 48 cases / 144 runs execute actual 152-word factory, 96-word initializer,
  full release and 113-word success action consumer. Qualify node/matrix NULL,
  full nonzero loader status and first/second buffer NULL failures. Independent
  release memory/calls verify unlink-before-final-free on rollback. 427 fired
  connected fault triples / 1,281 failed runs. Deeper loaders, allocation/free,
  SDK copy and external action callbacks remain bounded valid-output fixtures.

Historical neighbor/factory/initializer/action suites are not rerun as
standalone suites. Their unchanged linked bodies are covered by the entire
ELF audit; relevant actual caller/helper connections execute in this new suite.
The group walker's retail body/interface is inspected and preserved, not newly
claimed as a connected semantic run. No emulator/live gameplay exercised.

## Linked Audit And Progress

Permit only target's 408-byte slot and ST_SIZE 12 -> 408. Exactly 270 ELF
bytes change; every other ELF byte is exact. ELF 3,261,160 bytes, SHA-256
21860452ad90029ea4130259bf0c92dad90765ba67dd4a9f71e68a40bdfb0a55.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Protected rodata, tracked symbols and ignored undefined assignments are exact.
Conversion CSV is byte-identical: 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Installed source 55,576 bytes, SHA-256
86ccba6353f361ca2682c9c47641e3758e26f6576232eb5a646524cca9ad577d.

Guard history retains the entire 1,880,308-byte mixed-newline prefix and all
298 CRLF lines. Append only five LF rows / 680 bytes: manifest 1,880,988 bytes,
SHA-256 97d736eeb70d54ea162326bffdfdd94d30d5c41ddec3a40c1dcf684815db6a64.
Preserve Git's existing LF-checkout warning; no unrelated normalization.

Fresh match-progress: Game 2,775/4,821 (57.56%), total 3,448/5,494 (62.76%),
zero drift / 2,046 different. Delta +1 matching / -1 different only; this was
already counted as a C placeholder. Converted counts/bytes unchanged: total
5,494/6,043 (90.92%), 1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322
(90.59%), 1,769,624/2,072,880 bytes (85.37%). Init 492/492 and Debugger 181/181
already-converted routines remain exact; their unconverted routines stay open.

```sh
python3 -m unittest tools.tests.test_game_node_release_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

The guard dependency triggered a broad successful rebuild. Preserve existing
generated_12D630 duplicate-recipe and legacy pointer/type/MIPS3 warnings; this
is not a warning-free full build. Both tools checks pass after final code.
Native Graphify refresh refuses unsafe shrink 39,574 -> 17,792 nodes, exit 1;
retains 19,398 nodes from 2,972 excluded-but-existing files. Preserve skill
0.9.20/package 0.9.26 and devcontainer.json zero-node warnings. No force,
purge or install. Consumer post-commit hook must show fresh log growth/final
completion and zero actual workers before reporting a clean checkpoint.

## Next

Recover complete 114-word func_1502FE10, VA 0x1502FE10..0x1502FFD8,
ROM 0x5D2C0..0x5D488, original 0x50 frame. Recover all seven O32 arguments,
cache miss/allocation failure, record-pointer relocation and live count loop,
reference-byte increment/rollover, required source output and nullable output
gates. Connect the initializer's selector-minus-one path with real outputs
before claiming that loader's success contract. Bank it before a broad batch.
Alternate func_1503F62C loader and full 182-word func_15083AC8 remain open,
as do actual allocator/resource work and hardware/live gameplay acceptance.
