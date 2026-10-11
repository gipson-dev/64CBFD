# Animation Scratch Loop Shape Improvement

Verified 2026-10-11. Consumer baseline
3ca2cf9b4af0cf28bcb7074d6450f79f673fcde0; mounted tools baseline
ee484d736a1f52fc636ddd0263c8ee3742852e8f. New tools
995fcc30cad7d28512f4eb1a9ef6a397de6c02aa committed first. No push.
Single Codex writer, zero Claude calls; follow DOCS/AGENT_WORKFLOW.md.
This improves matching of the complete recovered routine; it is not byte-exact.

## Source Change

Continue full func_1502D824, VA 0x1502D824..0x1502DB20,
ROM 0x5ACD4..0x5AFD0, 191 words / 764 bytes, original 0x68 frame.
Preserve Note 1244's complete void(node,actor,scratch) semantics and typed
caller contract. Change only the loop shape: bank=0, banks>0 entry guard,
state=node inside that guard, then a do/while with bank/state increments and
bank!=banks termination. This recovers retail's opening loop schedule and
removes the extra initialization nop. Metadata strides, address widths,
float operations, callback packets and live post-copy reloads are unchanged.

Normal IDO O2/g3 now emits 187 words / 748 bytes, 0x50 frame, zero
diagnostics/pools and five relocation sites. Raw and linked word differences
drop 162 -> 102. These are position-by-position instruction differences,
not 60 recovered behavior bugs. No word guards, profile changes, unused local
arrays, fabricated padding or retail-body replacement were added.

Screen 29 complete source variants in the new shape experiment: explicit
entry guard, captured source address, named aligned pointer, split copy-offset
lifetimes, scratch pre-advance and float expression forms. Only the qualified
guarded-loop variant is installed. Named/captured variants can emit all 191
words but retain 0x50 frame and at least 123 differences; the matching word
count alone is not an acceptance criterion. Some float-expression probes
exceed the original slot. All other screened variants remain exploratory.

## Qualification

Ten final target tests pass after the linked rebuild. Reuse Note 1244's
independent reference/oracles and native32 harness, but keep a separate new
baseline and receipts under conker/build/game-animation-scratch-shape-test/.
Do not overwrite earlier snapshots or call their historical ELF audit current.

- 1,344 cases / 2,688 full retail/current executions: all length/stride byte
  values, finite frame/end boundaries, signed bank flags, actor/sentinel/NULL
  gates and all 16 scratch alignments; ordered public reference agrees.
  Reach 174 retail instruction words, not all 191.
- Seven alias/mutation cases; 652 fired public-access fault pairs / 1,304
  failed runs. Public partial memory/events/calls agree. Private frame/save
  accesses and private fault order remain explicitly excluded.
- Three independently rebased links / 54 cases / 108 runs qualify all five
  JAL sites. Four connected cases / eight runs execute actual byte-exact
  33-word actor refresh; its bzero remains a bounded callback.
- Seven effective fresh IDO negatives and one native negative. Native32
  O2/O0 each run 12,288 cases, 24,576 total, checking public node/actor/scratch
  storage and PI packets/generated copy bytes against an independent reference.
- Forty cases / 80 runs connect actual complete 66-word transform caller to
  the complete 191-word retail or 187-word current preparer. Safe length-zero
  NULL-temporary paths qualify; nonzero copy to NULL is not a hardware claim.
- Actual copied-owner postprocess/padder preserves all 37 neighbors' bytes,
  extents, relocation sites and normalized pools, with zero diagnostics.
  Current caller source/guards are unchanged and its 66-word fitted body
  stays byte-exact. Broader unchanged-neighbor behavior receipts from Note 1244
  are reused, not claimed as fresh runs here.
- Consumer make tools-check and mounted standalone python3
  check_project_tools.py pass. Standalone tools have no Makefile/tools-check
  target; an initial make invocation failed and the documented Python check
  was then used successfully.

PI is modeled by bounded deterministic callbacks, not actual ROM/hardware.
Finite in-range conversions only; no NaN/infinity/FCSR, private alias/fault
equivalence, full renderer, allocation lifetime or live gameplay acceptance.

## Linked Audit

Only the preparation slot and its ST_SIZE 752 -> 748 change: 504 ELF bytes;
all other ELF bytes exact. ELF 3,261,160 bytes, SHA-256
0f45792201cb49261cd4887aff3ac5f688515e38514a58963b6df355bbaeb423.
Protected data 189,088 bytes / 720 owners / zero differences, SHA-256
0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670.
Installed owner 42,125 bytes, SHA-256
c773916b3cd9e131e58429fa772fe687ef04ac2469a34bb7b706a1611207654b.
Caller owner, complete manifest including 298 historical CRLF lines, rodata,
tracked symbols, ignored undefined assignments and conversion CSV are all
byte-identical to the new baseline. Preserve their Note 1244 fingerprints.

Fresh matching totals unchanged: Game 2,778/4,821 (57.62%), total
3,451/5,494 (62.81%), zero drift / 2,043 different. No new matching or
converted credit. Root README aggregate rows verified correct and unchanged.
Converted total remains 5,494/6,043 (90.92%); already-converted Init 492/492
and Debugger 181/181 remain exact. Wider Game goal stays active.

```sh
python3 -m tools.experiments.game_animation_scratch_prepare_shape
python3 -m unittest tools.tests.test_game_animation_scratch_prepare_shape -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Existing duplicate generated_12D630 recipe warning remains. Native Graphify
update refuses unsafe shrink 39,618 -> 17,836 nodes, exit 1; retains 19,398
nodes from 2,972 existing excluded files. Preserve skill 0.9.20/package 0.9.26
and devcontainer.json zero-node warnings; no force, purge or install.
Require fresh post-commit hook growth/completion and zero actual workers.

Older standalone tools HEAD ddbdd16 remains untouched: 259 prior dirty entries
plus two absent-only byte-identical new mirrors = 261. Protected helper hashes
unchanged; existing submit copies not overwritten. No older commit/reset.
No OGL/Release, saves, editor state or private inputs changed.

## Next

Stay on this same routine. Recover original 0x68 frame and bank-count home
at SP+0x48 versus current 0x50 / SP+0x4C. Original 0x4C..0x67 is unwritten;
that does not justify inventing unused arrays to force frame capacity.
Retail also independently materializes 1.0 into F8 before frame+1, while
current C reuses F20. Resolve original source/aligned-pointer allocation,
first offset's A1-to-S2 lifetime and remaining independent schedules.
Qualify every full candidate before installation; any eventual normalization
needs a justified closed mapping and private-frame/fault qualification, not
a blanket retail-word replacement. Full 182-word func_15083AC8, timeline
matching and hardware/gameplay acceptance remain separate open work.
