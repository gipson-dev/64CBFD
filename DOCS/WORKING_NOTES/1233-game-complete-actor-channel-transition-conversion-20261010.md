# Complete Actor Channel Transition Conversion

Date: 2026-10-10

Continue [Note 1232](1232-game-actor-channel-reset-direct-conversion-20261010.md).
Convert full func_1507E7E4 from GLOBAL_ASM to byte-exact semantic C. The wider
Game matching goal remains active; this is not whole-game or host acceptance.

## Scope And Baseline

- Consumer starts clean at ecd19d39, mounted tools clean at 8355983. Single
  Codex writer; zero Claude calls. User's keep-committed authorization applies:
  tools first, then consumer source/guards/symbol declaration/docs/tools pin; no push.
- VA 0x1507E7E4..0x1507E908, ROM 0xABC94..0xABDB8, 73 words / 292 bytes,
  original 0x30 frame. Owner conker/src/game/generated_AB760.c. Retain original
  assembly and its nonmatchings copy. Graph query finds no assembly-only node;
  read complete retail assembly and all three direct caller interfaces.
- Five original immutable before-* snapshots retain owner, ELF, guards,
  conversion CSV and protected rodata. Baseline owner SHA-256
  d5111c1a9729f96e95cc57f4de4d7613d0a1cedc59607de4bc949e0a60b68572;
  ELF 72afd676886e434a8de725d4ab8d20662212e93ccea70527591982149137cee2.
  Add a separately hashed sixth linker snapshot before changing its assignment;
  do not overwrite the original snapshots or hashes after installation.
- Older standalone tools remains ddbdd16, independently dirty: 229 native
  Windows Git entries before, 231 after two absent-path authored mirrors.
  Later mirror replacements verify the exact prior authored fingerprint first.
  Preserve tracked-dirty game_owner_pool.py hash
  159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E and
  test_game_node_effect_registration_match.py hash
  C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input changes.

## Recovered Behavior And Match

Arguments: actor pointer, unsigned-byte channel and priority, unsigned-halfword
duration, signed-word amount in the fifth O32 home. Capture current actor byte
+0x6F once for arbitration. Return when requested channel, priority +0x71 and
duration +0x72 already match. Otherwise accept priority 3, current equal to
default byte +0x70, requested channel equal to current, expired duration, or a
strictly higher requested priority. Rejected arbitration calls nothing.

Call func_1507E968 and compare captured channel with its full-word signed
result using strict less-than. On acceptance, reread the live current channel
for func_1507E908. Read returned definition byte +4 unconditionally: do not
invent a null-definition compatibility guard. If nonzero, retain its pointer
across func_1507E9F8(actor, NULL), reread its live byte +4, and submit list[byte-1]
to func_150302F0 when the list is nonnull. Finally store requested channel,
duration and priority, then call func_1507E5C8(actor, amount). Zero definition
byte or null list skips animation submission, not the final state update.

The final declarations retain the existing full-word index contract of
func_1507E908 and signed-word func_150302F0 contract, explicitly casting the
actor address for the latter. No unrelated callee-source/type refactor.

Initial inline byte temporary emits 73 words with eight differences. A signed
word captured byte reduces this to seven; pointer-first local declarations
recover the retail +0x2C retained-pointer spill, leaving five differences.
Reversed comparisons, register/nested/gate forms and alternate widths do not
improve the selected complete source. No profile change or missing-body fill.

Five strict expected-word guards normalize only a closed t8/t9 load allocation
and symmetric equality operand ordering at +0x3C, +0x40, +0x48, +0x60 and +0x68.
Normal O2/g3, 73 words, 0x30 frame, five JAL relocations, zero diagnostics/pool,
zero inserted or omitted words. All producers and retail control-flow remain.
The raw and fitted forms have identical memory/call order, not just final state.

Authored tools: [complete candidates and guard recipe](../../tools/experiments/game_actor_channel_transition_candidates.py),
[qualification and linked audit](../../tools/tests/test_game_actor_channel_transition_match.py).

## Fresh Qualification

- 13,920 cases / 41,760 original/raw/fitted guest runs match an independent
  ordered reference, including every private byte/event. Execute all 73 retail
  words. Cover every priority-byte domain, arbitration/equal-field boundaries,
  duration equality/expiry, strict count boundaries, signed negative counts,
  descriptor-zero path and full amount bits. Clobber all caller GP/FPR; verify
  callee-saved registers, stack and return address. Void V0 is not compared.
- 144 public/private alias and live-callback cases; 972 fired fault triples /
  2,916 failed executions compare all prefix memory/events/calls. Missing faults
  fail. Include descriptor changing to zero before its live reread (list[-1]),
  retained-pointer overwrite, final argument-home mutations and two stack
  phases. This qualifies emitted guest fault order, not portable C faults.
- 64 additional high-word O32 carrier cases / 192 runs verify byte/halfword
  narrowing separately from typed callers and preserve signed amount bits.
- Nine independent raw/fitted/original links at three entry/callee rebases:
  135 cases / 405 runs pass. Guards do not alter JAL relocations. Execute the
  actual banked 28-word func_1507EABC caller with all three 73-word forms in
  144 cases / 432 runs against its separate full private reference.
- Complete production-profile owner compile/post-process/actual padding passes
  with zero diagnostics. Target and all 14 neighbors, function extents,
  relocations and pools remain exactly equal. Use old guards for the original
  assembly owner and appended guards only for the C owner; stale rejection of
  the unconverted owner is correct, not a reason to weaken the padder.
- Eight effective freshly compiled IDO semantic negatives: wrong priority,
  inclusive/unsigned count, signed priority byte, truncated duration store,
  wrong animation index/channel store, and cached pre-callback current channel.
  Isolate negative bodies at another entry because a wrong longer routine can
  overlap the retail callee address. Do not mistake this fixture overlap for
  a semantic control result. Six stale guard/length controls also reject.
- Complete native32 C at O2/O0 passes 2,097,152 cases per profile, 4,194,304
  runs: all 65,536 old/requested priority-byte pairs, eight channel/duration/
  descriptor/count scenarios and four callback plans. Compare all 812 actor
  bytes to an independent little-endian reference. Typed five-argument ABI and
  signed address-word animation call qualify; two native negatives are effective.
- Direct caller func_15079928 and Init func_1000CEAC interfaces are inspected,
  not fully executed here. Their code remains unchanged. Deeper callbacks are
  bounded models; real resources, hardware and gameplay are separate gates.

## Linker Boundary And Progress Correction

The first post-install audit correctly refuses an assumed asm-to-c row change:
the target has no original CSV row. conker/undefined_funcs_auto.txt still had
func_1507E7E4 = 0x1507E7E4; overriding its real FUNC symbol's section to ABS.
The link map omitted that boundary and assigned its 292 bytes to the preceding
assembly func_1507E73C, reporting a 460-byte extent instead of 168.

Remove only that assignment. Sixth snapshot SHA-256
cce90b4462b20a51f642784e0102349c28eb1e5c23f0677d92d1b3f5d49b0977;
after manifest SHA-256
deac423978a2c4e1336f0641725fd65445e0fd36e66167d77d73b98e208e7905.
Its other bytes are preserved. This *_auto.txt file is intentionally ignored
and is not committed. Append only the target's type:func defined:true line to
tracked conker/symbol_addrs.us.txt so future extraction does not recreate the
override. Preserve the entire previous symbol-file byte prefix (seventh
snapshot SHA-256 e6696d6c8784d00a6403a5416b82957bcaedd7ade657bb645782f6f06467bb68).
Actual local Splat parses the complete tracked symbol file, then its real
undefined-function writer excludes the referenced defined target while keeping
an unrelated unresolved canary. Changing only defined:true to defined:false
recreates the stale override: the negative is effective. No full extraction,
vendored parser change or dependency update. Makefile does not track this auto-assignment
file as a link dependency; ordinary make reports up-to-date. Force relink with
the existing linker-script dependency, not a broad build-system change:

```sh
make -C conker -W build/conker.ld -j4 build/conker.us.elf progress.csv
```

Final ELF differs only at file offsets 0x2C801E/0x2C801F: target symbol section
index 0xFFF1 (ABS) -> 5 (.game). Target value/type/292-byte size, all code/data,
all other symbols/addresses/extents, ELF headers and section layouts are exact.
Whole-file SHA-256
bf999834941dc6804caa011978298b58687ee6e9512c4649a766a49d2c57ec91.
Protected rodata is byte-identical. Protected data: 189,088 bytes / 720 owners /
zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Guard history retains all 1,867,291 old bytes; exactly five rows appended.
Current 1,868,051-byte SHA-256
69fa8d090a4d8a98e385fc77ad04c77f2a6d73b3c8ae13f3f441d6f2af1b27fa.
CSV changes only the explicit preceding asm extent 460 -> 168 and inserts the
target's 292-byte C row. Every other row and both repeated section headers are
exact. Current CSV SHA-256
b797f03d6cbb753f7d42b6049dd8e0f412da948efbb95759cb52258a6df8dab6.

Fresh conversion: total 5,491/6,043 (90.87%), 1,940,716/2,256,728 bytes (86.00%);
Game 4,818/5,322 (90.53%), 1,769,280/2,072,880 bytes (85.35%). The function
denominators rise by one for the recovered omitted boundary, not a new routine.
Init/debugger unchanged. Delta +1 counted/converted function / +292 C bytes.
Fresh matching: Game 2,768/4,818 (57.45%), total 3,441/5,491 (62.67%), zero
drift / 2,050 different. Delta +1 matching credit; different count unchanged.

## Validation And Bank

All nine final post-install tests pass in 22.241s. Root tools-check, older
standalone tools check and both exact mirrored Python parses pass. Full rebuild
has existing duplicate generated_12D630 recipe/compiler warnings; the target
owner and subsequent source-only rebuild have no compiler diagnostics.
An intermediate metadata fixture needed immutable bytes rather than bytearray
for its symbol Counter; fix the fixture and rerun the complete suite, not skip it.

```sh
python3 -m unittest tools.tests.test_game_actor_channel_transition_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker -W build/conker.ld -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Bank mounted tools 26d2236 (complete qualification), then 4da6c0b (durable Splat
definition proof), before consumer source/guards/symbol declaration/docs/pin.
No push; older independently dirty tools remains dirty. Root README receives
aggregate rows only. Prior selector/resource/reset broad receipts remain
historical, not described as fresh; their linked bodies and guard/data history
are unchanged by the full audit. Final target suite freshly executes the actual
reset caller and covers the helper's previously unqualified priority !=3 paths.

After final code edits, native graphify update refuses unsafe shrink
39,503 -> 17,731 nodes, retaining 19,398 nodes from 2,972 excluded-but-existing
files. Preserve that refusal, skill 0.9.20/package 0.9.26 warning and the
devcontainer.json zero-node warning; no force/purge/install. The existing
consumer post-commit hook runs separately; verify fresh log growth/completion
and zero workers before reporting the clean checkpoint.

## Next And Boundaries

Next: full 24-word func_1507E908, still GLOBAL_ASM in this owner. VA
0x1507E908..0x1507E968, ROM 0xABDB8..0xABE18, original 0x18 frame. Preserve the
full-word saved index across func_150849A0, nullable archive/data pointers,
ten-byte record stride and return-zero paths; do not narrow its index to u8.
Qualify actual count/definition/list/finish callbacks and the other script/Init
callers separately. No host or live-gameplay acceptance follows from this match.
Zero Claude calls attempted/completed: local assembly and independent evidence
settle the routine. No model/billing invocation or goal-completion claim.
