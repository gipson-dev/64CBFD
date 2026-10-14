# Game Actor Burst Consumer Float Lifetimes And Angle Conversions

Verified locally: 2026-10-14. Continue the same consumer from
[Note 1353](1353-game-actor-burst-consumer-semantic-recovery-20261014.md).
This remains uninstalled research, not production matching or host acceptance.

Completed in [Note 1355](1355-game-actor-burst-consumer-guarded-match-20261014.md):
the315-word result is installed with ten guarded rows and closed image/fault/
alias/owner/link/producer gates. This page preserves the earlier research receipt.

## Target And Baseline

- `func_151A6F00`, owner `conker/src/game/generated_1D43B0.c:7`.
- VA `0x151A6F00..0x151A73EC`, ROM `0x1D43B0..0x1D489C`.
- Retail: 315 words, frame `0x168`. Previous candidate: 311 words / 274 raw
  positional differences, despite matching private aggregate locations.
- Starting consumer `f8308be0`; starting tools `ce205ae`.
- New tools `0e244d606faa2accfe40bbfc1a4a2a5e29a216b1`, committed first.
- Production owner/caller/ELF/guards/progress/Makefile/assembly stay unchanged.
  The original before snapshots and pinned manifest remain authoritative.

## Recovered Source Shape

Three natural source changes recover the entire routine except two independent
branch-delay scheduling sites:

1. Keep the kind-0 planar speed separate from the kind-1/3 short-lived speed.
   Reuse the existing radius temporary in kinds1/3. This restores all saved
   float roles and caches `15.0f` in F30 and `30.0f` in F28 before the first RNG
   call. It does not add a dummy local or force a register declaration.
2. Pass `angle0 - 64` and `angle1 - 64` through the existing `u8` trig prototype,
   instead of explicitly masking the expressions. The real implicit narrowing
   recovers both retail mask/move sequences and two missing words. Explicit
   `u8` casts produce the same measured result. No prototype is widened.
3. Assign duration before descriptor ID and read payload field0C alongside its
   other parameter fields. This recovers the retail initialization/read schedule.

Selected `initialization-duration1-payload1` emits **313 words / frame0x168 /
143 raw positional differences**. Keep all four private homes from Note1353:
descriptor E8, payload D4, retained scale D0 and animation8C. There are no new
guards, volatile fields, inline assembly, synthetic padding or profile changes.

The 143 positional differences are not 143 independent remaining code defects.
Instruction alignment changes after the two omitted idle slots. The complete
diagnostic below establishes the actual remaining boundary.

## Exact Scheduling Boundary

| Kind | Retail Sequence | Current Candidate |
| --- | --- | --- |
| 0 | Z store at0x151A71C0, branch at71C4, NOP at71C8 | Branch at candidate word176, Z store in its delay word177 |
| 1 | Z store at0x151A7208, branch at720C, NOP at7210 | Branch at candidate word193, Z store in its delay word194 |

`analyze_velocity_delay_schedule` is an **analysis-only** inverse, not a build
transform. It requires the two unique expected Z-store words and actual
unconditional branches, moves each store before its branch, restores one NOP
per site and rebases every internal BEQ/BNE through the explicit index map.
It rejects branches into moved delay stores or outside the available mapping.
It does not copy any retail word into the result.

The reconstructed diagnostic equals **every one of the 315 retail words**.
An unrelated opening-word corruption remains different, and a wrong Z-store
control is rejected. This closes the instruction-difference diagnosis; it does
not make the compiler's 313-word output exact or authorize production promotion.
Fault EPC/BD and instruction timing cannot be inferred from equal return states.

## Source And Profile Screens

Ignored measurements remain under `conker/build/game-actor-burst-consumer/`:

| Screen | Measured Result |
| --- | --- |
| Seven branch-scratch forms | Selected radial reuse:311/168/244; aggressive combined reuse can reduce frame to160 and is not selected |
| Nine angle-expression forms | Both implicit/cast narrowings:313/168/190 |
| Seven brace/goto/if forms | Brace/goto variants unchanged; if-chain314/168/230 |
| Four initialization forms | Both earlier reads selected:313/168/143 |
| Six comma/pointer store forms | All remain313/168/143; do not recover idle slots |
| Four initial lifetime profiles | O2/g3 remains313/168/190; O1 profiles change extent/frame |
| Five final profiles | O2/g3 and existing no-unroll profile are word-identical313/168/143; ordinary O2 is worse, O1 remains nonmatching |

The no-unroll profile reuses the repository's existing `-Wo,-loopunroll,0`
setting in a scoped experiment only. No production Makefile or shared compiler
profile is changed. Preserve `PRIVATE_SELECTED` as the previous candidate and
effective saved-float control, not as the new selection.

## Fresh Qualification

**15 checks pass in47.269s:** the expanded13 target checks plus two protected
text checks. Both tools copies pass project smoke checks and Windows byte
compilation, and the mirrored modules compare byte-for-byte.

- **960 guest domains:** every declared kind, count0..4, allocation outcome,
  callback mutation, SP phase and stack seed. Packet/copy bytes, all private
  homes and complete modeled return states agree. This includes memory, GPRs,
  FPRs, HI/LO, modeled condition, memory-event traces and access counts.
- **288 real-call domains:** every saved F20..F31 role and lifetime agrees at
  every reached RNG/trig/factory/animation/memcpy boundary. Verify F30=15 and
  F28=30 before the first RNG call. The prior candidate has equal bounded public
  semantics but fails these saved-role observations, an effective control.
- The prior **18 signed-count prefixes**, **four actual BREAK7 prefixes**,
  **32 raw direction domains**, and **108 native32 cases per O2/O0 profile**
  remain green. The effective bad-count, double-op and scalar-copy controls
  retain their documented meaning and coverage limits.
- Both scheduling sites execute with equal modeled return states. The complete
  inverse/rebase diagnostic matches all315 words, with effective corruptions.
- All seven pinned production inputs remain unchanged, including the whole ELF
  and the still-zero-return production placeholder.

The first12-check run failed two stale assertions expecting the previous
candidate's return-state inequality. The observed new states were equal.
Replace those expectations with positive equality checks and broaden to all960
domains; the repaired three-check run passes36.601s before the full15-check run.
The failed run is not an acceptance receipt or a production defect.

Keep instruction PC/BD, hardware FCSR/rounding, complete all-input semantics,
public/private aliases, fault prefixes, owner padding and independent relocation
carries separate. RNG/trig and allocation systems remain bounded hooks; memcpy
executes its original11 words. Diagnostic word identity is not a linked image.

## Banking And Next Work

The old standalone mirror remains at ddbdd16 with461 dirty paths. Only the two
previously owned research modules are updated after checking their prior
fingerprints. All459 unrelated dirty-file fingerprints remain fixed.

Fresh read-only progress remains Game2,832/4,823 (58.72%), total3,505/5,496
(63.77%), different1,991, drift0; Init492/492 and Debugger181/181 remain exact.
No root README change, push, host build/launch, dependency install or frozen
Release work is performed. Preserve the existing Graphify corpus protection;
root filters still exclude the new tools modules as noted in Note1353.

1. Finish the two actual schedule sites, not another broad semantic rewrite.
   A legitimate source-emission solution or narrowly guarded build transform
   must preserve explicit word/relocation expectations. Do not install this
   analysis helper as a production patch without qualification.
2. Before promotion, close target aliases/fault boundaries, complete owner and
   both padders, independent symbol/carry links and the unchanged producer ABI.
   A build transform would need to move relocation offsets as well as words.
3. Install only the qualified315-word result, rebuild and prove the complete
   linked-image/progress changes. Keep the wider Game goal active.

```sh
python3 -m tools.experiments.game_actor_burst_consumer_candidates --filter initialization
python3 -m tools.experiments.game_actor_burst_consumer_candidates --filter initialization-duration1-payload1 --profiles
python3 -m unittest tools.tests.test_game_actor_burst_consumer_recovery -v
```
