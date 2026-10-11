# Animation Child Cleanup Direct Match

Verified 2026-10-11. Consumer baseline
2c0f9f2fd4c3a273186dd7c5f6aa0776e4012942; mounted tools baseline
ed89891ded9155b6a743cdd231fb887b0f775279. New tools
71822b664ed9b10993bc6d86628445b1311a7df8 committed first. No push.
Single Codex writer, zero Claude calls; DOCS/AGENT_WORKFLOW.md applies.
Previous goal turn made progress by banking the complete allocation helper.
This finishes another complete routine; the wider Game goal remains open.

## Recovery And Direct Match

Recover func_150836CC, VA 0x150836CC..0x150837D4,
ROM 0xB0B7C..0xB0C84, in conker/src/game/generated_AEB40.c.
The complete 66 words / 264 bytes emit directly from C with the original
0x30 frame, seven relocations and no new guards, pools or compiler profiles.
Both nested and combined conditions compile identically; install the first
complete candidate, not a shortened body. Replace the 12-byte zero-return
placeholder with void (u8 *actor, s32 animation). Existing typed caller
func_150634E4 already declares a void two-argument interface.

- Save S0..S5 and RA with their complete original lifetimes. Call
  func_150302F0(actor, animation) before decrement or descriptor lookup.
- Decrement the animation selector and index the existing eight-byte
  AnimationDescriptor15083568 table. Preserve the unsigned index shift's
  emitted low-word behavior. Load the unsigned count before the records
  pointer, including the pointer read on an empty descriptor.
- Cache the records pointer, actor-base address and positive divisor 812.
  Walk 16-byte records. Only record type byte +3 equal to zero calls
  func_1505F0AC with the unsigned identity byte +0.
- Skip NULL lookup results. Otherwise compute the signed low-word actor
  difference /812, truncating toward zero, add one and compare against
  the unsigned child parent byte +0x65. Equality alone calls
  func_15060F28(child, 0); do not truncate the quotient to a byte.
- Reload descriptor count after each record/callback. Callback growth or
  shrink changes traversal, but callback replacement of descriptor->records
  does not replace the cached record cursor. Preserve branch-likely access
  order, loop increment/stride and the original restores/return delay slot.

Inspect direct retail call contexts in 50D80.s, 90840.s and C4DC0.s and
the existing C callers in game_981E0.c, game_A28B0.c and game_A9D90.c.
Actual complete 35-word func_150634E4 is connected below, including both
animation 29/30 invocations. This is not full execution of every caller.

## Fresh Qualification

Nine final tests pass after installation and rebuild (17.616 seconds).
Independent receipts and immutable baseline hashes are in
conker/build/game-animation-child-cleanup-test/. Consumer make tools-check
and mounted standalone check_project_tools.py both pass.

- 4,201 independent-reference cases / 8,402 original/C guest runs: every
  parent byte, type bytes 0/1/2/255, NULL/non-NULL results, two stack phases,
  signed quotient boundaries and extreme low-word differences. Include
  full animation words, wrapped descriptor indexing, count 0/1/2/128/255.
  Full memory, ordered accesses, calls and GP/FPR results agree; preserved
  registers are checked despite callback clobbers.
- Reach all 62 executable retail words. Four trap-scaffold words at
  offsets 0xA0, 0xB0, 0xB4 and 0xB8 cannot execute with constant positive
  divisor 812. They still match statically; no claim of dynamic coverage
  for impossible zero/-1-divisor branches.
- 36 callback/alias cases / 72 runs and 866 fired full-access fault pairs:
  reset changes count before lookup; lookup/cleanup changes live count;
  cleanup replaces the descriptor's records pointer and modifies a future
  cached record; parent aliases descriptor count; record storage aliases
  private argument-home space. Empty count accepts unmapped record data.
  Every fault gate fires; full partial memory/accesses/calls match. Deep
  callback bodies, real child lifetime and allocator behavior remain bounded.
- Three independent symbol sets / nine original/C/production-padded links,
  12 cases / 36 runs. Both address HI16/LO16 pairs and all three JAL sites
  are independently rebased across signed low-half carry boundaries.
- Actual before/after copied-owner preprocessing, IDO compilation and
  asm post-processing preserve all 30 neighbors' complete fingerprints,
  extents, relocations and normalized pools, with zero owner diagnostics.
  Both layout and generated-owner production padding routes preserve every
  existing guard fingerprint and all non-target padded text/relocations.
- Eleven freshly compiled effective negatives distinguish selector, type,
  identity, parent offset, slot formula, cleanup mode, stride, loop count,
  signed division, cached count and incorrectly reloaded record pointer.
  The unsigned-division negative uses a local bounded DIVU oracle extension;
  no shared oracle changes. One additional native parent-offset negative fails.
- Native32 O2/O0 each pass 4,096 cases, 8,192 total: every parent byte,
  signed -1 slot, types, NULL results, zero/max/live counts and callback
  record-pointer replacement. Pointer/integer/descriptor widths are checked.
  Wrapped descriptor addresses, signed selector overflow and private fault
  order are guest-only qualifications, not portable native-C claims.
- Connect the actual complete 35-word caller with original/C helpers in
  32 cases / 64 runs. Each form executes 64 helper invocations with ordered
  animations 29/30; complete memory/accesses/calls/GP/FPR agree. Check the
  caller's two state clears before calls and three final actor-byte clears.
  Deep reset/lookup/cleanup callbacks remain models, not gameplay acceptance.

Initial fixture corrections: replace guessed unreachable trap offsets with
the actual four-word scaffold, and add local unsigned DIVU execution so the
signedness negative is rejected for behavior rather than missing instruction
support. All initial remaining checks already passed; final suite is fresh.
Historical neighbor suites are reused only after freshly proved complete
fingerprint equality; they are not reported as freshly rerun suites.

## Linked Audit And Progress

Only 202 ELF bytes change, inside this function's 264-byte slot and the
12 -> 264 ST_SIZE field. Every other ELF byte and metadata field is exact.
ELF 3,261,160 bytes, SHA-256
dde2f1e83f6fa0c00e0a51f7c7e15b47652164b1b2e9d78a5b7dcf17e1e794a7.
Protected data: 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
New owner: 12,426 bytes, SHA-256
bc411af05714e86015d2bafaf015782ddebdbdd6e2bb77ebe78a8278b742cc5e.

Guard manifest stays byte-identical at 1,940,850 bytes, SHA-256
5e50f8952c0e5d4ba39b7e9054b7ac5727517d021ba8e92d3b10c8a2f07b2f19.
Conversion CSV stays 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Rodata, symbol addresses and ignored undefined assignments remain exact.
Linked rebuild succeeds with the existing duplicate generated_12D630 recipe
warnings. README changes two aggregate matching rows only.

Fresh Game matching 2,783/4,821 (57.73%), total 3,456/5,494 (62.90%),
zero drift / 2,038 different: +1 matching, no additional converted credit.
Converted remains 5,494/6,043 (90.92%); Init 492/492 and Debugger 181/181
already-converted functions remain exact.

```sh
python3 -m tools.experiments.game_animation_child_cleanup_candidates
python3 -m unittest tools.tests.test_game_animation_child_cleanup -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Older standalone tools HEAD ddbdd16 stays unchanged: 271 existing dirty
entries plus two absent-only byte-identical new mirrors = 273. Protected
older helpers remain exact; no existing paths overwritten or committed.
Native Graphify query found 42 nodes, showed 22 and truncated 20. Native
update exits 1, refusing unsafe shrink 39,666 -> 17,884 and retaining
19,398 nodes from 2,972 excluded-but-existing files. Preserve version and
devcontainer.json zero-node warnings; no force, purge or install. Require
fresh post-commit log growth/Rebuilt tail and zero actual workers before
reporting clean. No OGL/Release, saves, editor or private inputs changed.

## Next

Recover complete 33-word func_15083E0C in the same owner,
VA 0x15083E0C..0x15083E90, ROM 0xB12BC..0xB1340.
It is still a zero-return placeholder. Inspect its caller return use, byte
selector/zero sentinel, initial count gate, cached D_800D20FC record base,
0x30 stride, first-match index return and -1 not-found result. Preserve the
original argument home and all completed neighbors/guards. Broader timeline
matching and real reset/child/allocator/hardware/renderer/gameplay acceptance
remain separate open work; keep the wider Game goal active.
