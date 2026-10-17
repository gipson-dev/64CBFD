# Movement Retail Extent Frame And Live Homes

Verified 2026-10-17. Consumer predecessor `c89577c1`; tools predecessor
`6f22514`. Both active trees began clean. This continues the complete
`func_150F34F4` recovery from
[Note1512](1512-actor-input-movement-recovery-and-fitting-boundary-20261017.md),
not a smaller substitute or a switch to the following function.

Target: owner `generated_11FF10`, VA `150F34F4..150F43F0`, ROM
`1209A4..1218A0`, 959 retail words / 3,836 bytes, frame `0x80`.
**The complete candidate now has exactly 959 words and frame `0x80`, with
restored live storage homes. It still differs at 744 words and is not installed.**
There are no new guards, profile changes or matching credit.

## Compiler Storage Evidence

`tools/experiments/game_actor_input_movement_frame.py` reuses the existing
owned-compiler observer through a scoped adapter. Prepared cc/CFE/UOPT/UGEN
fingerprints, source hashes, fired probes, complete producer/consumer/driver
exits and normal-object identity are mandatory. No compiler executable or
shared tracing helper is edited. The isolated procedure's complete words and
relative relocations must also equal the full owner's target.

Four fresh qualified traces in the full fitting run account for the storage:

| Complete Form | Frontend M Bytes | Optimizer M Bytes | UGEN Rounded Locals | Frame |
| --- | ---: | ---: | ---: | ---: |
| Previous recovery | 64 | 60 | 64 | `0x70` |
| Split independent values only | 80 | 60 | 64 | `0x70` |
| Split values plus ordered homes | 80 | 76 | 80 | `0x80` |
| Final heading/coercion form | 84 | 76 | 80 | `0x80` |

The observed UGEN frame sequence is **0 -> 16 -> 48 -> final frame**. Its
saved-area budget is 16 bytes, outgoing-area budget 32, and locals are rounded
to eight bytes. These budgets are not a count of literal register-save stores:
the actual S0/RA words remain at SP+`0x28` / SP+`0x2C`. The temporary list,
temporary size and temporary base stay empty/zero; there is no observed late
temporary-pool growth.

Each observation checks the exact native writer PC, raw M definitions,
source/procedure markers and operand widths/types. All four captures are
revalidated against the strengthened final checker, complete input hashes,
current compiler fingerprints and normal/traced object identity. The final
`--form heading-wide-cast` CLI invocation separately completes another owned
trace and passes the same checks. Host compiler PCs are not Conker guest PCs.

## Real Homes And Source Fitting

The accepted source separates four independently used values previously
stored in one reused C local: initial stick magnitude, nearest-distance result,
previous smoothed input and pitch calculation. Their declaration order restores
the live homes; none is an inert padding variable or fabricated parameter.

| Live Value | Previous Caller-Relative Home | Restored Home | Restored SP Offset |
| --- | ---: | ---: | ---: |
| Initial angle | -2 | -2 | `0x7E` |
| Input | -8 | -20 | `0x6C` |
| Speed / later saved velocity | -12 | -24 | `0x68` |
| Contact height | -16 | -40 | `0x58` |
| Nearest-scan index | -48 | -48 | `0x50` |
| Nearest distance | -20 | -56 | `0x48` |
| Scan record pointer | -60 | -76 | `0x34` |

Seven source homes are bound to the decoded frontend records. The initial
contact-height store, angle store and three live call-save stores are also
checked in actual emitted instructions against those caller-relative offsets.
The normal compiler output remains the authority; this is not proof of the
original local names or declarations.

Eleven complete source forms are freshly compiled and audited:

| Form | Words | Frame | Overlapping Unequal Words |
| --- | ---: | ---: | ---: |
| Previous recovery | 962 | `0x70` | 811 |
| Declaration ordering only | 962 | `0x70` | 811 |
| Independent value splits only | 962 | `0x70` | 811 |
| Splits plus ordered homes | 962 | `0x80` | 804 |
| Normal final animation u16 conversion | 960 | `0x80` | 804 |
| Separate 32-bit heading only | 961 | `0x80` | 758 |
| Heading plus animation conversion | **959** | **`0x80`** | **744** |

An explicit u16 cast and implicit prototype conversion produce identical
animation-call code. Keeping heading arithmetic as a separate unsigned 32-bit
value, narrowing only for the actual halfword store/call, removes the remaining
executable excess. The corresponding explicit/implicit final animation forms
also produce identical complete words. A typed link-address control leaves
the 960-word result unchanged.

Nine overflowing forms are genuinely rejected. The final raw and padded
959-word target are identical: no executable words are cut, inserted or replaced
to fit the slot. All eleven raw/padded owner neighbors and pools remain
unchanged, with no new guards or compiler-profile override.

```text
Final source form: heading-wide-cast
Raw SHA256: ee524ca5c671259f8ab349b7e6da08682ffc07fb09077428c8cdf659d5f50eb7
Words/frame/differences: 959 / 0x80 / 744
```

## Qualification And Remaining Private Boundary

The complete seven-test fitting run passes in **182.922s**. After strengthening
the pure storage checker and adding the alias screen, **two focused checks pass
in 25.191s**, including 49 effective fail-closed trace controls. Unchanged
emitted C/native bodies reuse the full-run evidence; this is not presented as a
second fresh full eight-test run.

Fresh full-run evidence for the new 959-word body includes:

- 2,496 complete core/width/filter/mutation cases and 20 additional modeled
  FP-edge cases, comparing retail MIPS, the complete candidate and the ordered
  independent model. All 256 stick-byte and cooldown values are retained.
- All 947 reachable retail words, with the twelve original unreachable
  duplicate words still retained in retail and required for later literal
  matching. Extent agreement alone does not prove those words already match.
- Two independent text rebases / twelve complete cases, actual 21-word curve
  execution, nine provider-mutation modes and complete public call snapshots.
- Native32 O2/O0 with UBSan, 130 cases per profile, complete actor/table/
  controller bytes, scalar globals and semantic call packets. Eight native
  controls fail real semantic gates, not crashes.
- Eight initial-state combinations across stack phases, byte patterns and
  input gates. The first ten modeled memory-fault boundaries agree in the
  compared register/stack/memory/call/PC state: **80 equal prefix states**.

The former cut-zero frame rejection is closed. The first remaining boundary is
**cut 10, guest PC `0x150F3544`**. Memory, FPRs and PC still agree, but retail
has the cached controller in **T2/GPR10**, while the candidate holds it in
**V1/GPR3**. All eight combinations reject there. This is not full private,
fault-prefix, general FCSR, opaque-provider or hardware/gameplay acceptance.

A complete global-controller alternative is measured and rejected as a fit:
959 words/frame `0x80`, but **763 differences** and cut 10 still fails. Twelve
additional guest cases alias the input packet with the controller global,
pressed-input global or pointer slot. Both source alternatives preserve public
behavior in those cases; that does not repair allocation or establish native
pointer-alias acceptance. The cached-controller 744-difference form is retained.

The first fully qualified-method-name selector hit Python's recursion limit in
the pre-existing long historical import chain. Module-level selection with
`-k effective -k global_controller` passes without editing dependencies or
changing the user's Python configuration. The failed launch is not counted as
passing qualification.

## Preserved Baseline And Reproduction

All **290 protected entries / 267 paths** are unchanged, including production
source/ELF, guards, profiles, conversion rows and prior immutable checkpoints.
The entire installed image remains
`245487b072c4daae7de2811ce7a50e749289a6adf7f28045c833523df36d7e60`.
All 6,057 bodies and 189,088 Game-data bytes / 720 owners are re-audited. No
normal production rebuild or installation is claimed for this research.

Fresh totals remain Game **2,965 / 4,828 (61.41%)**, total
**3,638 / 5,501 (66.13%)**, 1,863 different and zero drift. Init 492/492 and
Debugger 181/181 stay exact among converted functions. Root README is unchanged.

```sh
python3 -m tools.experiments.game_actor_input_movement_frame --screens
python3 -m tools.experiments.game_actor_input_movement_frame --fitting-screens
python3 -m tools.experiments.game_actor_input_movement_frame --form heading-wide-cast
python3 -m unittest tools.tests.test_game_actor_input_movement_fitting -v
python3 -m unittest tools.tests.test_game_actor_input_movement_fitting -k effective -k global_controller -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```

Owned receipts are under `conker/build/game-actor-input-movement-frame/` and
`conker/build/game-actor-input-movement-fitting-test/`, including the four
retained `traces/` captures, source screens, native/alias/private receipts and
protected-input audit. Earlier unchanged recovery/neighbor suites are prior
receipts, not fresh tests.

Tools **f0fadc5** is banked before the consumer docs/pin. Both local tools
copies freshly pass twelve shared tests and smoke checks, four ASCII/AST parses
and two identical task pairs. Both mirror destinations were absent; all 1,150
prior hashes and HEAD `ddbdd16b` survive, with 1,152 dirty paths afterward.
No mirror commit/reset, push, dependency installation, Claude call, host-port
change or frozen Release action.

## Continue Literal Matching

- [x] Explain the local area and bind real live homes with qualified traces.
- [x] Restore the complete 959-word extent, frame `0x80` and initial private prefixes.
- [x] Requalify the complete behavior and preserve all installed bytes/checkpoints.
- [ ] Continue the same `func_150F34F4`: recover controller-load allocation at
  cut 10 / `0x150F3544`, then the remaining register roles and scheduling.
  Do not treat the 744 differences as a broad patch list.
- [ ] Require literal agreement across all 959 words, full appropriate private/
  fault/rebase/caller gates and an exact complete first image before installing.
- [ ] Keep the gate, both fade lifetime gaps, full opaque-provider/runtime
  acceptance and the wider Game objective open; do not move to `func_150F43F0`.
