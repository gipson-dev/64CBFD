# Animation Scratch Preparation Reconstruction

Verified 2026-10-11. Consumer baseline 491aa8fca5c90ff220e026c40ebe57b24a5e44ce;
mounted tools baseline e999db1be6bc16365da04fd967ff9e3b079a1c8e. New tools
ee484d736a1f52fc636ddd0263c8ee3742852e8f committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
This is complete semantic restoration, not a completed byte match.

## Recovery

Replace func_1502D824's false zero-return body in generated_58F80.c.
Retail VA 0x1502D824..0x1502DB20, ROM 0x5ACD4..0x5AFD0, 191 words /
764 bytes, original 0x68 frame. Both direct retail callers ignore V0.
Recover void (node,actor,scratch), not a fabricated status result.

When actor is non-NULL, test unsigned halfword +0x84 against 0xFFFF, call
actual actor refresh when equal, then reload the node pointer from actor+0x2D0.
A NULL resolved node returns without public work. Cache one bank by default,
two only for positive signed halfword node+0x3C. Loop index addresses bank
fields at node+index*4 but byte metadata at node+index*0x1D0.

Zero byte length +0x45 clears only node+0x38+index. A NULL bank source at
+0x28 skips copying and preserves that output byte. Otherwise capture frame
and end floats at bank fields +8/+0x18, align scratch upward to 16, truncate
frame, cap it at truncated end-1 when needed, and use unsigned byte +0x48
plus one as the frame stride. Preserve the special last-frame division and
ordinary signed integer division paths; do not replace them with floor math.

Compute the wrapping source address from length*frame index. Retain its low
two bits for the first copy, publish scratch+offset at fields+0x30, and select
direct small PI copy below 200 bytes or mode-1 DMA rounded to 16 otherwise.
For a final-frame wrap, copy one record first, reload source after the first
callback, align scratch again, retain the source's low one bit, and copy the
opening record. Reload the published output pointer after that callback to
derive byte-truncated offset node+0x38+index. Byte length is cached through
both callbacks; second-bank metadata and source/output pointers stay live.

All semantic operations emit from unguarded C. IDO O2/g3 emits 188 words /
752 bytes, 0x50 frame, zero diagnostics/pools. It still has 162 isolated and
linked word differences against the 191-word retail slot. No matching credit
is claimed. Preserve the production profile and original slot boundaries.

## Caller Contract

Change generated_6C960.c's stale s32 declaration to the recovered typed void
prototype. Its complete func_1503F4B0 now emits 66 words, original 0x48
frame, with only two private terminator-placement differences. The previously
guarded three-word V1-to-V0 base transfer now emits directly from C.

Retire only these three superseded guards at offsets 0x6C/0x70/0x74; retain
placement guards at 0x64/0x78 and every other manifest byte. A structured,
expected-word-checked retirement rejects stale, missing or duplicate rows.
All four routines in this caller owner remain exact: 66/29/99/17 words.
Update its complete raw fingerprint and tests for the new declaration, not
the fitted retail body. Notes 1243 and earlier remain historical checkpoints.

Second retail call: PC 0x1502DD94 / ROM 0x5B244 in func_1502DB84,
packet (NULL,actor,caller SP+0x98), delay 0x27A60098. That full renderer
is still a C placeholder and was not executed here. The other call is the
complete 66-word transform routine, packet (node,NULL,temporary); NULL
temporary is still passed after allocation failure, not silently skipped.

## Qualification

Ten final target tests pass after full rebuild. Ignored reproducible receipts
and immutable baseline snapshots live under
conker/build/game-animation-scratch-prepare-test/.

- 1,344 cases / 2,688 retail/current runs: all length/stride bytes, finite
  frame/end boundaries, signed bank flags, actor/sentinel/NULL gates and all
  16 scratch alignments. Independent ordered public memory/events/calls
  agree; 174 retail instruction words reached. No all-191-words claim.
- Seven alias/mutation cases; 652 fired public-access fault pairs / 1,304
  failed runs. Public partial memory/events/calls agree. Actor node reload,
  cached bank count/length, live second-bank metadata and post-copy source/
  output reloads qualify. Private frame/save/fault order is not equivalent
  yet and is explicitly excluded, not normalized into a matching claim.
- Three independently rebased links / 54 cases / 108 runs: all five JAL
  sites and three independent callbacks qualify.
- Execute actual 33-word retail/current byte-exact func_1505DFDC in four
  cases / eight runs. Actor sentinel, node clear, length-zero handling and
  no-copy outcome qualify; its bzero is a bounded callback.
- Seven effective fresh IDO negatives: length, signed bank flag, alignment,
  200-byte threshold, stride, wrap offset mask and output delta. One effective
  native negative; 24,576 native32 O2/O0 runs check PI packets, generated copy
  bytes and complete public node/actor/scratch storage against an independent
  reference. Finite in-range float-to-integer conversions only.
- Actual copied-owner postprocess/padder proves all 37 neighbors' bytes,
  extents/relocations and normalized pools unchanged; zero diagnostics.
- Forty connected cases / 80 runs execute the complete 66-word transform
  caller with full 191-word retail or 188-word current preparation, covering
  gate-off and safe length-zero NULL-temporary paths. Allocator, final
  emission/submission/timeline/free remain bounded callbacks.
- Nine current submit behavior regressions pass freshly after the rebuild.
  Exclude its historical test_09 whole-ELF checkpoint audit; preserve the
  saved snapshots. This target's new full-ELF audit is authoritative here.

PI callbacks generate deterministic bytes from the captured address; they
are not actual ROM reads, PI hardware or SDK allocation lifetimes. No invalid
float conversion, NaN/infinity/FCSR, private alias/fault-order, full renderer
or live gameplay acceptance is claimed. The complete retail function remains
the matching authority, not the public-only fixture.

## Linked Audit

Only preparation slot and its ST_SIZE 12 -> 752 change: 551 ELF bytes,
all other ELF bytes exact, including the requalified caller owner.
ELF 3,261,160 bytes, SHA-256
211396b55e4785e86a00a76c9718410d5441cd943a0a03a2426c45a8c6f653ab.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Rodata, tracked symbols and ignored undefined assignments byte-identical.

Installed owner 41,816 bytes, SHA-256
695b0323c40ff89ba071f1643254ddf0e44d9a43e0b11768e3e4257a23a4abd4.
Caller owner 3,342 bytes, SHA-256
0439ee4394ce5c8460feb73bb7b7f9a7af270e46cd180002d9ed16222751fc71.
Manifest 1,884,531 bytes, SHA-256
5434a4b101990faf7dafc142933515b4192a8924c0f4c5af27aef6354db596e5:
exactly three rows / 444 bytes retired; all other bytes and 298 historical
CRLF lines retained. No new guards for this preparation routine.
Conversion CSV unchanged, 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.

Fresh matching totals unchanged: Game 2,778/4,821 (57.62%), total
3,451/5,494 (62.81%), zero drift / 2,043 different. No new matching or
converted credit for restoring this already-counted C placeholder. Root
README aggregate rows were verified and need no change. Converted totals
remain 5,494/6,043 (90.92%), 1,941,060/2,256,728 bytes (86.01%).
Already-converted Init 492/492 and Debugger 181/181 remain exact.

```sh
python3 -m tools.experiments.game_animation_scratch_prepare_candidates
python3 -m unittest tools.tests.test_game_animation_scratch_prepare -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Guard retirement triggers the full padded-object rebuild; existing duplicate
generated_12D630 recipes and SDK/generated warnings remain. Both tools checks
pass. Older standalone tools HEAD ddbdd16 untouched: 257 prior dirty entries
plus two absent-only byte-identical new mirrors = 259. Existing three submit
tool copies and protected helper hashes stay untouched; no older commit,
reset or overwrite.

Native Graphify update refuses unsafe shrink 39,609 -> 17,827 nodes, exit 1,
retaining 19,398 nodes from 2,972 existing excluded files. Preserve skill
0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no force,
purge or install. Require fresh post-commit hook growth/completion and zero
actual workers before reporting a clean checkpoint. No OGL/Release, saves,
active editor or private inputs changed; wider Game goal remains open.

## Next

Finish this same routine's 191-word / 0x68 byte match, not another broad batch.
Recover original bank-count home at frame+0x48 versus current +0x4C,
24-byte frame difference, loop-entry schedule, source/temporary allocation and
retail's independent 1.0 constant materialization before frame+1 comparison.
Re-run complete ordered public checks for each candidate before considering
private-frame qualification or tightly justified scheduling guards.

Saved exploratory explicit-count/do-loop probe at
conker/build/game-animation-scratch-prepare/explicit.c emits 189 words,
0x50 frame, 124 isolated differences. It captures the source pointer before
the NULL gate, initializes bank=0, guards banks>0, then uses a do loop with
bank/state increments and bank!=banks termination. This probe is not yet
behavior-qualified and is not the installed source. Integer/double-literal
variants introduce an extra saved F22 or exceed the slot; no profile changes
or invented unused arrays/padding were installed. Full 182-word func_15083AC8,
current timeline matching and hardware/gameplay acceptance remain open.
