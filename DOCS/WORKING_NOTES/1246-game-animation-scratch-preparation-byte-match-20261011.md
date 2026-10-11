# Animation Scratch Preparation Byte Match

Verified 2026-10-11. Consumer baseline
713e1397411e23e377cb7cf8b320afc650dddfcb; mounted tools baseline
995fcc30cad7d28512f4eb1a9ef6a397de6c02aa. New tools
672c03d84c6a2d45abb7f8a2b33dca0ed94e2d50 committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
Complete semantic C plus checked normalization now matches the full retail slot.

## Complete Match

Finish func_1502D824, VA 0x1502D824..0x1502DB20,
ROM 0x5ACD4..0x5AFD0, all 191 words / 764 bytes and original 0x68 frame.
Notes 1244/1245 recovered its complete void(node,actor,scratch) semantics and
guarded loop. This checkpoint does not change that C or its typed callers.
Raw IDO O2/g3 still emits 187 words / 0x50 frame with 102 differences;
do not describe this as an unguarded compiler match.

The new explicit recipe changes 46 compiler words and inserts four, with no
omissions. All 187 raw words have expectation rows: 141 unchanged words are
identity checks, not replacement operations. Check all five R_MIPS_26 sites
and exact 748-byte raw extent. Recipe and production padder reject any stale
word or helper relocation. Preserve the existing profile and original slot.

- Increase frame reservation/return by 24 and move the six bank-count home
  accesses from SP+0x4C to SP+0x48. Save offsets are unchanged relative to SP.
  The original unwritten SP+0x4C..0x67 capacity is reproduced by normalization,
  not a fabricated C array or unused source padding.
- Preserve closed source A1->A2 allocation, aligned scratch T0/T1 lifetime,
  byte destination T9, stride-minus-one temporary, first offset A1->S2 and
  second offset S2/T6. Move only their complete producer/consumer schedules.
- Independently materialize the same 1.0 in F8 for frame+1 instead of reusing
  F20; preserve the associated float producer/compare and multiply-result
  schedule. Restore the first saved-offset move before helper calls.
- Normalize one commutative fields-pointer addition. Recompute branch
  displacements from the four insertions rather than copying target offsets.
  Keep all helper relocations, now at their retail instruction positions.

The recipe stores the complete compiler fingerprint, not a retail replacement
word array. Its transformed output is then independently compared with retail
and passed through the actual padding/assembly/linking path.

## Qualification

Thirteen final tests pass after the full rebuild. New immutable baseline
snapshots and reproducible receipts are under
conker/build/game-animation-scratch-match-test/. Earlier notes/tests retain
their historical whole-ELF checkpoints; do not overwrite those snapshots.

- 1,344 cases / 4,032 retail/raw/fitted executions: all byte lengths/strides,
  finite frame/end boundaries, signed bank flags, actor/sentinel/NULL gates
  and 16 alignments; independent ordered public reference agrees. Reach
  174 retail words dynamically; all 191 words match statically and linked.
- Seven public alias/mutation cases; 652 fired public-access fault triples /
  1,956 failed runs agree in public partial memory, events and call packets.
  Raw 0x50-frame private-fault equivalence is not inferred from public checks.
- Nine independent links at three entry/helper symbol sets, 54 cases / 162
  runs; independently assembled retail and fitted bodies match at all five
  call sites. Four cases / 12 runs execute actual 33-word actor refresh;
  its bzero is a bounded callback.
- Seven effective freshly compiled IDO negatives are rejected by both behavior
  and normalization. One effective native negative; native32 O2/O0 each run
  12,288 cases, 24,576 total, against an independent PI/public-storage reference.
- Forty connected caller cases / 160 paired runs: actual complete 66-word
  transform caller with complete retail/raw/fitted preparation. Retail repeats
  for two independent pairs. Gate-off and safe length-zero NULL temporary
  qualify; remaining emission/submission/timeline/allocation/free are bounded.
- Twenty-four private-layout cases; 912 fired full-access fault pairs / 1,824
  failed runs compare complete fitted/retail memory, events, calls, GP and FPR
  state. An independent save/home/restore contract verifies absolute original
  frame offsets, bank home reloads and untouched 28-byte capacity in zero-copy
  cases. Four scratch/node private aliases qualify at both stack phases.
- Two cases / four runs mutate the private bank-count home during a callback,
  extending one bank to two and proving the original home stays live. The first
  fixture assertion used an incorrect second aligned-pointer expectation;
  it was corrected from the packet arithmetic before publishing guards.
- Actual production padder rejects all 187 individually mutated raw words and
  five independently changed helper relocations, including identity rows.
- Actual copied-owner padding preserves all 37 neighbors' bytes, extents and
  relocations. Source/compiler pools are unchanged. Exact complete 66-word
  caller is requalified; broader unchanged-neighbor behavior receipts from
  Note 1244 are reused, not reported as fresh suites here.
- Consumer make tools-check and mounted standalone python3
  check_project_tools.py both pass. Existing duplicate generated_12D630 and
  SDK/generated warnings remain; the full rebuild is not warning-free.

Private qualification above is fitted versus retail, not portable C equivalence
for aliases into a different compiler frame. Native checks are finite/in-range
only. PI callbacks generate deterministic bytes, not actual ROM/hardware reads.
No NaN/infinity/FCSR runtime, full renderer, resource lifetime or live gameplay
acceptance is claimed. Final matching authority is the complete retail body.

## Linked Audit

Only target slot and ST_SIZE 748 -> 764 change: 323 ELF bytes, all other
ELF bytes exact. ELF 3,261,160 bytes, SHA-256
a73e5d25d64d9fbb7f7a56c843e186efdb3cba4a52e0762ee2be3c517a2fb139.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Source, caller, rodata, tracked symbols, ignored undefined assignments and
conversion CSV remain byte-identical to Note 1245's baseline.

Guard manifest appends only 187 rows / 28,059 bytes; complete old prefix and
298 historical CRLF lines are retained. New 1,912,590-byte SHA-256
2e564bf3b7c1985023c66211fda8079b8605f0bb1a1bb7c82f505dd93c4a5237.
Native Git's existing CRLF-to-LF checkout warning remains; the scoped diff
contains exactly 187 additions and zero deletions, not an EOL rewrite.
Unchanged conversion CSV 317,198 bytes, SHA-256
738f9596296f185524c6ee24932520ef68be00ed2c653eac6b3c5a4cc6ff102c.
Unchanged owner 42,125 bytes, SHA-256
c773916b3cd9e131e58429fa772fe687ef04ac2469a34bb7b706a1611207654b.

Fresh matching: Game 2,779/4,821 (57.64%), total 3,452/5,494 (62.83%),
zero drift / 2,042 different. Add one matching credit, no converted credit.
Root README aggregate rows updated only. Converted total stays 5,494/6,043
(90.92%); already-converted Init 492/492 and Debugger 181/181 stay exact.

```sh
python3 -m unittest tools.tests.test_game_animation_scratch_prepare_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Older standalone tools HEAD ddbdd16 is untouched: 261 prior dirty entries plus
two absent-only byte-identical new mirrors = 263. Existing submit copies and
protected helper hashes stay untouched; no older commit/reset/overwrite.
Native Graphify update refuses unsafe shrink 39,626 -> 17,852 nodes, exit 1;
retains 19,398 nodes from 2,972 existing excluded files. Preserve skill
0.9.20/package 0.9.26 and devcontainer.json zero-node warnings; no force,
purge or install. Require fresh consumer post-commit hook completion
and zero actual workers before reporting clean. N64 normalization only:
semantic C/caller contracts unchanged; no host/OGL change applicable here.
No Release, saves, editor state or private inputs changed. Wider Game goal open.

## Next

Bank this complete match before another conversion batch. Resume full
182-word func_15083AC8 in generated_AEB40.c: current typed nine-argument
constructor still returns zero. Original VA 0x15083AC8..0x15083DA0,
ROM 0xB0F78..0xB1250, 0x38 frame; inspect complete AEB40.s body and actual
caller before recovery. Timeline's current 237 differences, full renderer,
actual resource/PI/hardware and gameplay remain separate open work.
