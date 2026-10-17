# Actor Counter Motion Direct Restoration And Match

Date: 2026-10-17

Continue consumer **811b042f**, tools **017c9c4**, after
[Note1495](1495-white-text-fade-candidate-and-private-lifetime-gap-20261017.md).
Restore **func_150B9560**, owner **generated_E5E90**, VA
**150B9560..150B95FC**, ROM **E6A10..E6AAC**: **39 words / frame0**.
The complete semantic C body emits every retail word directly, replacing the
12-byte zero-return placeholder. No new guards or compiler-profile change.
Tools **39c4f4e** banks the qualification and exact fixture adapters first;
the consumer checkpoint carries source, docs and the updated tools pin.

## Recovered Contract

Read the signed halfword counter at actor0x1C. Below80, increment the float
step at0x110 by **D_8009FDD4 * D_800BE9A4**, then subtract the updated step
from float field0x38. Retain the subsequent signed counter reload. At115
or above, multiply fields0x2C and0x30 by one cached **D_8009FDD8** value.
Otherwise, below65, add **D_8009FDDC** to0x30. Return1 on every path.

The exact existing data words are **0x3E99999A**, **0x3FACCCCD** and
**0x3F99999A**, approximately0.3,1.35 and1.2. Name the existing globals with
float declarations rather than creating new local literal-pool entries.
No constant/data pool changes and all seven other raw/padded owner functions
are unchanged. The actor-field names remain conservative; this checkpoint
does not infer a more specific gameplay role from the arithmetic alone.

The real locals are only the step pointer and cached scale. Assigning the
pointer inside the first conditional produces38 words, folding its address
into actor-relative loads/stores. Initializing it at declaration produces
retail's explicit V0 address, V1 counter, original float schedule and39 words.
An integer-address cast, byte pointer and register hint do not recover that
shape in the measured conditional-assignment forms. No dummy object, extra
stack storage, forced register or instruction-order guard.

## Qualification

Raw SHA-256:
`ca4fe8840677bb4a178792680924a963f940a18e218c82fe18ce025917422863`.
Eight relocation sites form four independently checked HI16/LO16 pairs.
Both raw and actual padded objects link to all39 retail words.

All **ten tests pass before installation in33.090s** and **after installation
in67.268s**, without skips:

- **14,784 three-way guest/reference cases**, all39 target words, signed
  boundaries, threshold edges, signed zero, NaN/infinities and two stack phases.
  Full private state and target read/write order agree. The float32 model is
  not hardware/FCSR or hardware NaN-payload acceptance.
- **1,280 guest alias cases**,20 placements across the clock/constants,
  counter and output fields. Preserve the post-store counter/step reloads
  and the single cached scale even when its source aliases the first output.
- **1,344 three-way target access-fault prefixes**. Observer snapshots create
  no counted pseudo-instructions. These qualify emitted guest order, not
  portable C faults or hardware exceptions.
- **Nine independent original/raw/padded links**,288 three-way cases, all
  eight sites and independent signed-low carry boundaries.
- Native32 **O2/O0 + UBSan**, all **65,536 signed-halfword values per profile**,
  separately typed caller and six effective sign/threshold/motion negatives.
  Native objects are complete, aligned and non-aliased; NaNs compare by
  category rather than payload. Extended guest aliases are not native proof.
- Two effective **IDO semantic negatives** separately break the threshold
  and reload the scale after an aliasing output store. Their guest results
  positively differ, not merely their fingerprints.
- **432 executions** of the complete195-word caller image, **func_1513CFE4**,
  selecting table slot3 at **D_80089CB8+12**. Exercise active/disabled and
  timer-decrement paths, callback absence/presence and successful return1.
  Animation and secondary callbacks are disabled; freeing is a scripted
  boundary. This is not all caller paths, the real heap or gameplay.
- **39 word / eight binding /446 live-and-frozen /18 checkpoint /14 metadata**
  corruption controls. All **223 protected entries /206 paths** stay checked.

## Complete Normal Image

Freeze the entire prediction before production edits:
`b62c85c1a8e02733790c827821229caaa487c0776bf87318a337c9f8142248eb`.
The normal N64 build exits0 and its entire ELF equals this first prediction:
**120 code bytes + one extent byte +51 metadata bytes =172 changed bytes**.
No metadata exclusions. The first strict prediction caught the51 metadata
bytes before installation. Permit only these exact adjacent ABS symbol/name
permutations, with all original definitions checked:

- **D_8009FDDC / D_800CC264 / D_800A0A0C**, order1,2,0.
- **D_8009FDD4 / D_800A0A04**, swapped.
- **D_8009FDD8 / D_800A0A08**, swapped.

Compare all **6,057 disassembled function bodies**: only this target changes.
Every function address agrees; every symbol definition agrees except the
target's12-to156-byte extent. Guards, compiler flags, Makefile, layouts,
nominal conversion rows and every other protected input are unchanged.
The changed owner has no CFE diagnostics; the existing duplicate
generated_12D630 recipe warning remains, so the build is not warning-free.

All **189,088 Game-data bytes /720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Fresh official matching is **Game2,956/4,828 (61.23%)**, total
**3,629/5,501 (65.97%)**, **1,872 different**, zero drift. Init492/492 and
Debugger181/181 remain exact. Root README changes only two aggregate rows.

## Fixture History And Bank

The six-member exact checkpoint covers the ELF, recovered actor owner,
reveal adapter, white-fade experiment and two affected test files. Unknown
bytes remain unrecognized and fail the caller's strict fingerprint check;
both before/after fixture corruptions fail closed. Preserve every earlier
first-image prediction and fixture rather than replacing them with this ELF.

Fresh affected checks: **21 pass in160.048s**, comprising the full ten-test
reveal suite, full eight-test white-fade suite and three constructor
input/installation/compatibility checks. This is not a fresh full eleven-test
constructor run; its unchanged core receipts remain in Note1494.
The reveal audit now explicitly compares its archived first image, after
validating the exact inverse of current bytes. Historical white-fade
"unchanged input" receipts similarly describe its canonical archived baseline,
not a claim that the current ELF lacks this actor change. The new installed
target suite supplies the current complete-image gate.

Twelve active and twelve standalone shared checks, both tool smoke checks,
sixteen ASCII/AST parses and all eight task-file pairs pass. The four modified
standalone files matched their exact predecessors before copying. Preserve
**1,088 unrelated hashes**, its **1,096 dirty paths** and HEAD **ddbdd16b**.
No standalone commit/reset, push, dependency/provider/account change, Claude
call, host-port operation or frozen Release action. Tools commit39c4f4e first;
verify the native code-only post-commit Graphify receipt before closing.

## Finish And Next

- [x] Recover and qualify the complete39-word semantic C body directly.
- [x] Freeze all six edits and the entire linked image before installation.
- [x] Install, finish the normal build, and require exact first-image equality.
- [x] Pass ten installed tests,21 affected checks, complete function/data audit,
  fresh official progress and both tools-copy checks.
- [x] Bank tools39c4f4e before the consumer source/docs/pin checkpoint.
- [x] Finish **func_150F2480**, owner **generated_11F780**, the38-word
  sine/phase update, in [Note1497](1497-sine-phase-update-restoration-and-match-20261017.md).
  The complete C body matches with one commutative ADDU operand guard.
- [ ] Keep both fade S0/private-lifetime issues and wider Game matching open.
  Handwritten func_150A76F0 remains in the separate assembly workstream.

```sh
python3 -m tools.experiments.game_actor_counter_motion
python3 -m unittest tools.tests.test_game_actor_counter_motion -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
