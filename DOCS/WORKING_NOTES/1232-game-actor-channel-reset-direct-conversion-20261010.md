# Actor Channel Reset Direct Conversion

Date: 2026-10-10

Continue [Note 1231](1231-game-complete-actor-resource-transition-byte-match-20261010.md).
Convert full func_1507EABC from GLOBAL_ASM to direct byte-exact C. The wider
Game matching goal remains active; this is not whole-game/host acceptance.

## Scope And Baseline

- Consumer starts at clean d14f9a7d, mounted tools at clean 49e2558.
  Single Codex writer, zero Claude calls. User's keep-committed authorization
  applies: tools first, then consumer source/docs/tools pin; no push.
- VA 0x1507EABC..0x1507EB2C, ROM 0xABF6C..0xABFDC, 28 words / 112 bytes,
  original 0x20 frame. Owner conker/src/game/generated_AB760.c; original
  assembly and its nonmatchings copy are retained. Graph query finds no node
  for the assembly-only entry; complete assembly and live callers are read.
- Five immutable before-* snapshots: owner, ELF, guard manifest, conversion
  CSV and protected rodata. Every test run asserts their hashes. Before owner
  SHA-256 2c713dcb5e59d0947f0ccc62196fa5c5aea9d2102115ab631df9aae72c59f0ac.
  Before/current ELF SHA-256 72afd676886e434a8de725d4ab8d20662212e93ccea70527591982149137cee2.
- Older standalone tools stays at ddbdd16, independently dirty: native Windows
  entries 227 before, 229 after two new absent-path mirrors. The tracked-dirty
  game_owner_pool.py and test_game_node_effect_registration_match.py hashes
  remain 159B8C009AF7B2D26BA5DCE29F0C46CA0805CF14DBB27E5C682D107E551CA50E
  and C9195B44C4276E410CD6ABAB7F926E4C920363BF84505F5596681937397FBC71.
  No older-tools commit/reset, OGL/Release, editor, save or private-input changes.

## Recovered Behavior And Direct Match

Call func_1507E7E4(actor, actor[0x70], 3, 0xFFFF, 10). Channel and priority are
unsigned bytes, duration an unsigned halfword, and amount a signed word.
The fifth O32 argument occupies the outgoing +0x10 home. The actor pointer is
saved at incoming-argument home +0x20 and reloaded after the callback.

After the callback, clear byte +0x71 and the complete halfword +0x72. Read the
live unsigned byte +0x6C; if >=10, clear +0x6C then +0x6A. Read the live unsigned
byte +0x6D after those stores; if >=10, clear +0x6D then +0x6B. Neither comparison
is signed. Do not capture these bytes before the callback or clear state before
the callback observes it. The routine is void, not a false zero-return function.

Four source forms measured. An explicit u8/s32/u32 first-byte temporary emits
28 words and the original frame but changes five scheduling words. The inline
source emits all 28 retail words directly, zero differences/diagnostics/pool.
Normal O2/g3 is retained, with one JAL relocation and zero guards, insertions,
omissions or compiler-profile changes. No assembly bytes are supplied by padding.

Authored tools: [source candidates](../../tools/experiments/game_actor_channel_reset_candidates.py),
[complete qualification and linked audit](../../tools/tests/test_game_actor_channel_reset_match.py).

## Fresh Qualification

- 3,072 cases / 6,144 original/direct-C executions match an independent ordered
  reference including all private bytes and events. Every one of 28 retail
  words executes. Cover all first/second/channel byte domains, unsigned 9/10
  threshold boundaries, two stack phases, live callback mutations and callbacks
  overwriting the saved actor home. All caller GP/FPR are clobbered; callee-saved
  state, stack and return address are verified. Void V0 is not compared.
- Twelve private/public alias cases cover incoming actor-home and outgoing fifth
  argument-home overlap. Every selected access fires: 146 fault-prefix pairs /
  292 failed executions compare full prefix memory/events/calls. Missing faults
  fail. This qualifies emitted guest ordering, not portable C fault semantics.
- Six independent original/C links under three entry/callee address pairs pass
  108 cases / 216 executions. Distinct JAL targets and entries are checked.
- Execute actual banked 73-word func_1507E7E4 with both 28-word target forms in
  432 cases / 864 runs. An independent full private reference covers the
  reachable priority-3 context: equal-field early return, signed count gate,
  definition/list presence, live definition-byte reload, retained actor and
  argument-home mutations, and the fifth argument actually read from +0x40
  in the child's 0x30 frame. Forty additional connected fault-prefix pairs pass.
  Deeper callbacks remain bounded; priority !=3 branches are not exercised.
- Production-profile copied owner compiles/posts/pads with zero diagnostics.
  All actual padded owner bytes, function addresses/extents and relocations are
  identical, including the target and all 14 neighbors. Pools and callers are
  unchanged. This is a complete 112-byte C routine, not missing-body padding.
- Eight fresh complete IDO negatives and three native negatives are effective:
  threshold, signed byte, wrong channel/duration/fifth argument, truncated state
  clear, wrong reset pair and a pre-callback captured byte. The signed-byte
  negative needs LB; add its precise behavior only to this target's local oracle,
  leaving shared helpers unchanged. Rerun all ten tests after that fixture fix.
- Complete native32 C at O2/O0 passes 393,216 cases per profile, 786,432 runs.
  Cover all 65,536 first/second-byte pairs at two actual actor buffers and three
  mutation plans, all channel bytes, callback-before-reset ordering and actual
  typed five-argument ABI. Compare the full 812-byte actor to a separate
  little-endian reference. This is bounded-callback native acceptance.
- Actual banked func_1507EB4C's 13-word slot and both complete target forms
  execute in 72 cases / 144 runs. Full-word change gating remains distinct from
  the following low-byte store, including 256/511/0xFFFFFFFF inputs. Unchanged
  channels do not call or alter public state; changed channels submit all five
  expected arguments. Full private traces and ABI agree. Helper is bounded in
  this caller matrix; its separate actual 73-word connection is described above.

## Installation And Bank

Replace one GLOBAL_ASM entry with the qualified typed declaration and complete
C body. Source-only rebuild, link and progress generation succeed. Existing
duplicate generated_12D630 recipe warning remains; the target owner has no
diagnostics. All ten final post-install tests pass in 14.962s. Root tools-check,
older-copy standalone tools check and both exact mirrored Python parses pass.

Whole linked ELF is byte-identical to the baseline, including symbol/string
tables; no instruction, address or extent changes. The audit also compares
complete metadata/symbol/name multisets before any allowed ordering normalization.
No guard rows are added; all 1,867,291 guard bytes remain identical, SHA-256
0a07ccef5b121264c293ac66a93636dc39e34f84d8a186265c413172848fe989.
Protected rodata is byte-identical. Protected data: 189,088 bytes / 720 owners /
zero differences, SHA-256 0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.

Exactly one conversion row changes: func_1507EABC from asm to c, original 112-byte
length/address preserved. All other rows and repeated section headers remain
exact. Aggregate calculation filters real c/asm rows, not the two repeated
section headers. Current conversion CSV SHA-256
f8eefe41c2e47696cfad6041a56392db100e0c4b857c243ca3a2b72d76f4ed6e.

Fresh conversion: total 5,490/6,042 (90.86%), 1,940,424/2,256,728 bytes (85.98%);
Game 4,817/5,321 (90.53%), 1,768,988/2,072,880 bytes (85.34%). Init/debugger
unchanged. Delta +1 converted function / +112 converted bytes.
Fresh matching: Game 2,767/4,817 (57.44%), total 3,440/5,490 (62.66%), zero
address drift / 2,050 different. Delta +1 matching credit; different count is
unchanged because this routine was previously excluded from the C denominator.

Bank mounted tools 8355983 first, then consumer source/docs/tools pin. Root
README gets aggregate rows only. No push; older independently dirty tools stays
dirty. Prior resource/selector receipts remain historical, not called fresh;
their linked bodies and guard/data fingerprints are unchanged by the full audit.

```sh
python3 -m tools.experiments.game_actor_channel_reset_candidates
python3 -m unittest tools.tests.test_game_actor_channel_reset_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Native graphify update after code edits refuses unsafe shrink 39,493 -> 17,710
nodes, retaining 19,398 nodes from 2,972 excluded-but-existing files. Preserve
the refusal, skill 0.9.20/package 0.9.26 warning and devcontainer.json zero-node
warning; no force, purge or installation. The consumer's existing post-commit
hook runs separately; verify fresh log growth/completion and zero workers before
reporting the clean checkpoint.

## Next And Boundaries

Next decomp target: full 73-word func_1507E7E4, still GLOBAL_ASM in the same owner.
VA 0x1507E7E4..0x1507E908, ROM 0xABC94..0xABDB8, original 0x30 frame. Recover
all unsigned-byte/halfword arguments, equal-field return, priority arbitration
including priority !=3, signed returned-count gate, live definition/list reloads,
retained callback values and final five-argument amount consumption. Reuse this
actual-connection evidence only for its recorded priority-3 context, then broaden
qualification to the complete helper and its other callers before conversion.

Deeper callback bodies, real asset domains, hardware/live gameplay and OGL/frozen
Release remain separate open gates. No host changes or gameplay acceptance are
inferred from retail matching. Zero Claude calls attempted/completed: complete
local assembly, four source shapes and independent tests settle the routine.
No packet/model invocation, billing change or goal-completion claim.
