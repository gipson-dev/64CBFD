# Complete Animation Node Constructor Byte Match

Verified locally: 2026-10-10. Continue the full Game matching goal; this is one
banked function checkpoint, not Game, hardware or live-gameplay completion.

## Result And Baseline

Recover complete func_15030AF4 in
[generated_5D2C0.c](../../conker/src/game/generated_5D2C0.c): VA
0x15030AF4..0x15030D54, ROM 0x5DFA4..0x5E204, 152 words / 608 bytes,
original 0x30 frame. The original assembly remains in conker/asm/5D2C0.s.
The semantic C replaces a false zero-return placeholder and the final linked
slot matches every retail word. Existing O2/g3 profile; no generated pool,
body insertion, omission, layout or symbol-assignment changes.

Baseline consumer 821d0ac77b5332c886f90f4dd17b6077e219a1b9; mounted tools
975e23b2b1c4109d238862495caca8dc5283bab2. Baseline source SHA-256
fc84ab6952dfb67df23c5a66c2bb302a8058b84429c8544dce6723af5d233640;
baseline ELF 5cbb958e352c5f4166a314ad84aa52dc04ffdfadcef7b9fcefb6d5fdfa78beb8.
Use [Note 1237](1237-game-complete-actor-animation-constructor-byte-match-20261010.md)
for the banked 89-word caller and the separate type-0 helper ABI correction.

Tools d2ad015add2fd9914aacbfcd05aed2410837d942 are committed first, then
consumer source/guards/docs/tools pin, no push. Single Codex writer; zero
Claude calls because compiler experiments and independent qualification settle
the assembly/ABI questions locally. No bridge, billing or token-cost claim.
Preserve OGL, frozen Release, saves/editor state and private reference inputs.

Older standalone tools HEAD ddbdd16b53ce60b054fb6e11bf0649a41f48375a stays
unchanged. Mirror only the three absent authored files: dirty entries
240 -> 243. Both protected pre-existing task-file fingerprints are unchanged,
all three mirrors byte-equal, all six parses and both tools checks pass.
No reset, clean or duplicate commit in that older checkout.

## Complete Contract

Thirteen O32 arguments agree with the actual constructor's existing declaration,
including byte-pointer payload argument nine. Keep kind, flags, mode and
duplicate key full-word until their explicit byte stores/comparisons; do not
narrow an incoming key to make a duplicate match.

1. Load the actor group at 0x3B; zero returns NULL. Flags bit 8 bypasses the
   duplicate scan. Otherwise walk D_800C3EE0, reading next at 0x54 before
   comparisons, and reject the first group/key/kind match.
2. Allocate 0x5C bytes with (1,0,2); NULL returns without payload access.
   Reload flags/key homes and the live list head after allocation. Link the
   old head's previous pointer at 0x58, then reload the head for the new next
   link. Publish the node and reload the actor group for initialization.
3. Initialize every recovered field and leave untouched gaps intact. Copy the
   three unsigned payload halfwords in order; preserve byte/halfword narrowing,
   scale 1.0f, priority 0xFF, nullable pointers and zero state words.
4. Allocate 0x80 transform bytes with (1,2,2) only when full-word mode == 4
   or flags bit 4 is set. Preserve NULL failure, private failure spill and
   signed/unsigned bit carriers. Duration zero becomes halfword 0xFFFF;
   nonzero durations retain their low 16 bits, even if those bits are zero.
5. If allocation did not fail, OR func_1502FFD8's complete returned word into
   the failure state. Any nonzero word, including the sign bit alone, submits
   func_15030158(node,1) and returns NULL. Otherwise execute the actual
   func_15031A50(node,actor) action setup and return the allocated node.

func_1502FFD8 and func_15030158 remain existing three-word zero stubs. The
factory's calls and failure decisions are recovered; those resource-loading
and cleanup bodies, freeing/unlinking behavior and runtime allocation
acceptance are not restored by this checkpoint.

## Source Fit And Guard Boundary

The first complete candidate already emits 152 words / frame 0x30; declaration,
source-order and typed/volatile-field alternatives were measured locally.
Unsigned duration storage recovers retail's 0xFFFF materialization directly.
The selected byte-pointer payload form emits identical code and agrees with
the existing caller prototype, without changing another owner.

Forty-seven expected-word guards apply only a checked initialization schedule
and closed t6/t7 temporary swap. The schedule is a bijective permutation of
existing emitted instructions; all 13 relocations remain untouched. The
complete 152-word raw fingerprint and relocation map must match before guard
generation; all 152 independent stale-word mutations reject. Stale and
duplicate guard publications reject, preserving the historical byte prefix.

This is not a claim that the raw compiler initialization access order equals
retail. Raw C is separately qualified for public behavior with valid, disjoint
fresh allocations and live actor/list payload aliases. Retail and fitted
forms have exact full-memory/event/call order, including private aliases and
fired fault prefixes. Guest fault timing is not portable C fault semantics.
One retail compiler-duplicated halfword store, word 130 at VA 0x15030CFC, is
unreachable on normal entry. Preserve it byte-exact, not as a coverage claim:
the other 151 words are reached.

## Fresh Qualification

[Target suite](../../tools/tests/test_game_animation_node_constructor_match.py)
passes all ten tests before installation (32.710s) and after the complete
rebuild (33.264s). Reuse existing candidate/compiler, MIPS oracle, native32,
padder and data-audit APIs; no shared helper changes.

- 18,480 ordered cases / 36,960 retail/fitted runs: all flag, mode, kind, key
  and group bytes, full-word boundaries, three list shapes, first/second NULL
  allocation, nonzero statuses, live post-allocator head/actor/home/payload
  mutations and clobbered caller GP/FPRs. Also 1,280 raw public cases.
- Fifteen alias/lazy-NULL cases, 948 fired fault pairs / 1,896 failed runs;
  compare full memory/events/calls/FPR prefix. NULL actor and reached NULL
  payload reject at the original required read. Private node/payload/spill/
  caller-home aliases are guest-only; live actor/list payload cases also
  compare raw public behavior.
- Nine independently linked forms across three entry/head/all-callback
  placements, 288 cases / 864 runs, including signed LO16 carries.
- Complete copied-owner compile/post-process/production padding: zero
  diagnostics, pools unchanged, all 39 other functions' bytes/extents and
  relocation sequences exact, both resource/cleanup stubs untouched.
- Eight effective fresh IDO negatives: narrowed mode/key/kind, wrong zero
  duration sentinel, wrong payload halfword, missing cleanup, signed-positive
  status gate and wrong allocation size. Two native negatives also fire.
- Native32 -O2/-O0: 264,192 cases each / 528,384 runs, typed thirteen-argument
  calls, exact complete node/untouched gaps, live head/group/payload changes,
  duplicate/nullable allocation and failure gates. No fresh-node overlap claim.
- Eight descriptor/record samples independently equal the retail ROM; 64
  connected cases / 128 runs use the actual 89-word caller, full factory,
  unchanged zero initializer/cleanup stubs and real 113-word action dispatcher
  with its original owned jump tables. 1,049 fired connected fault pairs /
  2,098 failed runs. External action/resource callbacks remain bounded.
- Separately execute all 256 action bytes: 2,048 connected cases / 4,096 runs,
  with an independent action reference for nullable state, counter wrap,
  actor flag masks and signed random boundary behavior.

The historical request/lookup/classifier suites are not rerun here. Their
unchanged linked bodies are covered by the complete ELF audit; do not label
their prior receipts fresh or claim complete deeper-helper/gameplay parity.

## Linked Audit And Progress

Permit only the target's 608-byte instruction slot and its ST_SIZE 12 -> 608.
Exactly 444 ELF bytes change; every other ELF byte is exact. ELF 3,261,160
bytes, SHA-256 cd907778bb225f56d0ab100345238ee72e9537a89e69bd2817407e6bf8210b8b.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Protected rodata, tracked symbols and ignored undefined assignments are exact.
Conversion CSV is byte-identical: 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Installed source 52,372 bytes, SHA-256
01abbb5db432fbdbfe965a558ee83b37a413cbc86fee8ea9d38db8c7ea11707a.

Guard history retains the entire 1,870,873-byte mixed-newline prefix and its
298 CRLF lines; append only 47 qualified LF rows. Working manifest 1,878,484
bytes, SHA-256 01a9103134bd89ae0e538d9cea84434c1b995dc7028715ef7992044f285fbfa9.
Git's existing LF-checkout warning remains; no unrelated normalization.

Fresh match-progress: Game 2,773/4,821 (57.52%), total 3,446/5,494 (62.72%),
zero drift / 2,048 different. Delta +1 matching / -1 different only. Converted
counts/bytes unchanged: total 5,494/6,043 (90.92%),
1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322 (90.59%),
1,769,624/2,072,880 bytes (85.37%). This was already a C placeholder.

```sh
python3 -m unittest tools.tests.test_game_animation_node_constructor_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

The manifest dependency triggered a broad successful rebuild. Retain existing
generated_12D630 duplicate-recipe and legacy pointer/type warnings; do not
claim a warning-free full build. Both tools checks pass. Native Graphify
update after final code changes refuses unsafe shrink 39,554 -> 17,772 nodes,
exit 1, retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve
skill 0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no
force/purge/install. Consumer commit hook needs fresh log growth/completion
and zero actual workers before reporting a clean checkpoint.

## Next

Full func_1502FFD8 in the same owner: VA 0x1502FFD8..0x15030158, ROM
0x5D488..0x5D608, 96 words / 384 bytes, original 0x40 frame. Restore the
signed selector sentinel, both seven-argument resource-loading paths, live
actor/node flags, resource-span arithmetic, paired copy allocation, partial
failure free and two bcopy submissions. Then qualify the real factory's
initializer connection, not just a success-return model. Full 102-word
func_15030158 cleanup and 182-word func_15083AC8 type-0 constructor remain
open too. Keep the broader Game goal active.
