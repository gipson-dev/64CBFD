# Complete Node Transform Submission Byte Match

Verified 2026-10-11. Consumer baseline 266c9db619f2034d20f8f409dbda40bd453ad44d;
mounted tools baseline 030412c0b57b8bf54374f5e2d27620db5120eb85. New tools
e999db1be6bc16365da04fd967ff9e3b079a1c8e committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.

## Recovery

Replace func_1503F4B0's false zero-return body in generated_6C960.c. Complete
66 words / 264 bytes, VA 0x1503F4B0..0x1503F5B8, ROM 0x6C960..0x6CA68,
original 0x48 frame. All three direct retail callers ignore V0; recover a
void outer routine, not an invented status result.

Gate on node+0x3E0 indexed by live selector byte D_800BE9C0. Allocate
0x320 bytes with packet (0x320,1,2,2), retain its private temporary home at
frame+0x44, and call preparation (node,0,temporary) even when allocation
returns NULL. Retain preparation's current s32 declaration and ignore its
result; its actual 191-word body remains a separate zero-stub recovery.

Reload selector after preparation; write the empty halfword adjustment-stream
terminator 0x1000. Capture indexed matrix/buffer, then pass the eight O32
arguments (private cursor pointer,matrix,node,source,count,terminator,0,0).
The transform helper's adjustment path reads the halfword terminator first;
no larger original local-array capacity is claimed. The C scalar is sufficient
for this empty stream. The helper may advance the private cursor; submission
instead reloads the selector/count/indexed buffer. Set node byte 0x3F6 to 1.

Unconditionally call the actual typed timeline interface
(struct197* node,f32 D_800BE9A4,NULL actor,0 mode), including the gate-off
path. Preserve the float wire bits in A1. Afterwards reload the private
temporary home and free only a non-NULL value. Callback mutations to that
home can change or skip the free. Required NULL node still faults in guest.

IDO O2/g3 emits all 66 semantic words and the original frame, zero diagnostics
and pools. Five raw word differences remain: halfword local placement at
frame+0x3E instead of retail +0x40 (store and argument address), and one
closed three-word V1-to-V0 indexed-base transfer. Guard the complete 66-word
fingerprint and all 14 relocations before the five substitutions. No inserts,
omissions, call/control-flow changes or compiler-profile changes. Fitted linked
body matches all retail words; do not claim raw private fault-order equivalence.

## Qualification

Ten final target tests pass after full rebuild. Reproducible ignored receipts
are under conker/build/game-node-transform-submit-test/. Immutable pre-change
snapshots are retained; do not rewrite historical neighbor checkpoints.

- 2,256 boundary cases / 6,768 retail/raw/fitted executions: every selector
  and count byte, NULL gate/temporary, both stack phases, signed zero,
  finite values, infinities, quiet/signaling NaNs and subnormal wire bits.
  All 66 words reached; caller GP/FPR clobbers qualify. Raw uses its own
  independent +0x3E marker reference; fitted follows full retail +0x40 order.
- 75 alias/live-mutation cases; 699 fired retail/fitted fault pairs / 1,398
  failed executions with exact partial memory/events/calls/FPR agreement.
  Selector, source/count, timeline step and temporary-home reloads qualify.
  Private cursor is not submission's source; global/public aliases and
  required NULL-node fault qualify. No raw private fault-order claim.
- Nine independently rebased links / 144 cases / 432 executions: all 14
  relocation sites, independently moved selector/float globals, signed HI/LO
  carries and six callback symbols. Reject 66 stale-word and 14 stale-reloc
  controls, stale manifest and duplicate publication.
- Actual copied-owner postprocess/padder preserves all three neighbors'
  bytes/extents/relocations, normalized pools and existing 24 alternate-loader
  guards; zero compiler diagnostics before and after.
- Eight effective fresh IDO semantic negatives: gate, allocation size,
  NULL preparation, terminator, count sign, cached cursor, flag and step.
  Invalid terminator 0x1001 is rejected after the emit callback actually fires.
  Two effective native negatives; 15,360 native32 O2/O0 runs, valid selectors
  0/1, all count bytes and float wire patterns. Private addresses normalized,
  but cursor and terminator values and eight-word packets checked. No native
  out-of-object cursor arithmetic or reads of unwritten private padding.
- 64 connected cases / 256 executions run the full 287-word retail timeline
  and current linked 287-word slot with both original/fitted outer routines.
  Finite steps/rates/frames, NULL actor, sequence 0/1, gates and allocation
  outcomes qualify; public outputs agree. Current timeline still has 237
  word differences, deliberately preserved. Not full FCSR/hardware acceptance.
- 48 cases / 96 executions exercise three authentic retail JAL/delay windows
  in synthetic save/restore wrappers, with independent complete target
  reference inside each window. Full callers were not executed.
- Nine scoped alternate-loader behavior regressions pass freshly. Exclude
  its historical test_09 whole-ELF checkpoint audit; retain that snapshot.
  This target's new whole-ELF audit is authoritative for this checkpoint.

Retail call windows: PC 0x150309EC / ROM 0x5DE9C (lw A0,0x48(S1));
PC 0x151573A4 / ROM 0x184854 (sw A1,0x20(SP), A0 previously loaded);
PC 0x151EDCD8 / ROM 0x21B188 (lw A0,0x24(S1)). All ignore returned V0.
Allocator/free, preparation, transform emission and final submission are
bounded callback receipts, not actual allocation lifetimes, complete resources,
graphics/hardware or live gameplay proof.

## Linked Audit

Only target slot and its ST_SIZE 12 -> 264 change: 215 different ELF bytes,
all other bytes exact. All four owner routines now match retail:
func_1503F4B0 (66), func_1503F5B8 (29), func_1503F62C (99),
func_1503F7B8 (17 words). No remaining zero placeholder in this owner.

ELF 3,261,160 bytes, SHA-256
c6ac65cbe5365504b283440c14e2b952d1485f1d681cc8615e3ac974237c93b1.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Rodata, tracked symbols and ignored undefined assignments byte-identical.
Installed source 3,325 bytes, SHA-256
9efd7bf0f8aebbda4a826737dba184b63a3d05f10bdcbeae0b09ea2a90089f49.

Guard manifest 1,884,975 bytes, SHA-256
a8da163d69e667661d5a0ed3dbe2a8c5d45df935d3a418f17a9a1fde80656664:
only five new rows; complete old byte prefix including 298 CRLF lines retained.
Conversion CSV unchanged, 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
No extra conversion credit for replacing an already-counted C stub.

Fresh match-progress: Game 2,778/4,821 (57.62%), total 3,451/5,494 (62.81%),
zero drift / 2,043 different. Delta +1 matching / -1 different only.
Converted counts/bytes unchanged: total 5,494/6,043 (90.92%),
1,941,060/2,256,728 bytes (86.01%); Game 4,821/5,322 (90.59%),
1,769,624/2,072,880 bytes (85.37%). Already-converted Init 492/492 and
Debugger 181/181 stay exact; unconverted routines remain open.

```sh
python3 -m tools.experiments.game_node_transform_submit_candidates
python3 -m unittest tools.tests.test_game_node_transform_submit_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

The guard change triggers full padded-object rebuild; existing duplicate
generated_12D630 recipes and SDK/generated warnings remain. Zero target
diagnostics is not a warning-free full-build claim. Both tools checks pass.
Older standalone tools HEAD ddbdd16 untouched: 254 prior dirty entries plus
three absent-only byte-identical mirrors = 257; protected helper hashes
unchanged, no older-checkout commit/reset/overwrite.

Native Graphify update refuses unsafe shrink 39,601 -> 17,819 nodes, exit 1,
retaining 19,398 nodes from 2,972 existing excluded files. Preserve skill
0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no
force/purge/install. Require fresh post-commit log growth/completion and zero
actual workers before reporting a clean checkpoint. No OGL/Release, saves,
active editor or private inputs changed; wider Game goal remains open.

## Next

Recover full 191-word func_1502D824 in generated_58F80.c: original VA
0x1502D824..0x1502DB20, ROM 0x5ACD4..0x5AFD0, 0x68 frame. Its current
zero-return placeholder is the preparation callback this routine needs.
Audit NULL actor/node/scratch gates, signed loop metadata, matrix outputs,
float math and complete caller contract before deciding types/profile.
Bank that scoped checkpoint before a broad batch. Full 182-word func_15083AC8,
current timeline matching and resource/allocator/hardware/gameplay stay open.
