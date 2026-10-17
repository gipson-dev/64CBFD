# Fixed State Sine Update Direct Restoration And Match

Date: 2026-10-17

Continue consumer **eafda31d**, tools **931d6c2**, after
[Note1497](1497-sine-phase-update-restoration-and-match-20261017.md).
Restore **func_150F23E0**, owner **generated_11F780**, VA
**150F23E0..150F2480**, ROM **11F890..11F930**: **40 words / frame0x20**.
The complete semantic C body emits every retail word directly, replacing its
12-byte zero-return placeholder. No new guards, declarations or compiler
profile changes. Tools **d698926** banks qualification and exact fixture
adapters before the consumer source/docs/pin checkpoint.

## Recovered Contract And Source Shape

Use fixed float state at **actor+0x170**. Compute sine of state0/state1,
multiply by amplitudes state4/state5, and write actor fields0x20/0x28.
Then advance state0/state1 by their respective rates state2/state3 times
**D_800BE9A4**, wrap each through **func_15144B68**, and return1.
Reload the clock after the first wrap call. Names remain conservative rather
than assigning an unverified gameplay meaning to these offsets.

The genuine pointer initializer at declaration is the discriminator:
`f32 *state = (f32 *)(actor + 0x170);`.
IDO naturally emits the real actor parameter home at SP+0x20, first sine
argument through T6, actor reload through V0, then delayed S0 state creation.
S0 remains live across the remaining three float calls. Retail saves S0 at
SP+0x18 and RA at SP+0x1C; all40 words, including delay slots, agree.

An explicit wave temporary plus later pointer assignment or declaration
instead produces39 words/frame0x28 and the wrong caller-saved pointer lifetime.
Adding volatile to the declared actor parameter retains40 words/frame0x20
but has seven real word differences and initializes S0 before the first
sine call. Reject it. No forced register, extra storage, inline assembly,
volatile qualifier or instruction-order guard is installed.

Raw SHA-256:
`846afc8acc047da0650dcba607e22f53fe7824e1f0b821177bf360824ba34f96`.
Eight relocation sites cover four calls and two clock HI16/LO16 pairs.
Raw and actual padded objects match all40 words. All eight other raw/padded
owner routines and all data/literal pools agree. The existing matrix guards
and func_150F2480's one ADDU guard remain untouched.

## Qualification

All **ten tests pass before installation in32.142s** and **after installation
in33.733s**:

- **96 three-way guest/reference cases**, six float patterns, four clocks,
  two stack phases and scripted caller-saved/home clobbers. Amplitude and
  clock/second-phase mutations demonstrate required reloads. Full private
  state, FPU condition and literal memory-access order agree.
- **48 guest aliases**, placing the clock over both actor outputs and all
  six state parameters. Every target instruction executes.
- **48 cases with actual104-word sine and24-word wrap routines**, including
  sine's outgoing argument-home store. Reuse the existing independent sine
  reference, not a new host approximation.
- **510 three-way real-access fault prefixes**, with actual helpers and
  scripted clobbers. Observers add no pseudo-instruction reads. This qualifies
  emitted guest order, not portable C faults or hardware exceptions.
- **Nine independent original/raw/padded links**,36 three-way executions,
  all eight sites and independent signed-low carries.
- Native32 **O2/O0 + UBSan**, separately typed caller,256 cases per profile
  and four effective output/rate negatives. Providers are scripted float ABI
  probes, not retail math. Only aligned, complete, nonaliased native objects
  are claimed; amplitude mutation remains guest-only because portable C does
  not specify multiplication-operand evaluation order.
- **Four extended guest private-home cases** mutate the real actor home
  after sine1 or sine2. All original/raw/padded states agree. The equal-length
  volatile negative has **four private and two public counterexamples**.
  This proves the emitted delayed-S0/home contract; it does not claim that
  arbitrary private stack mutation is portable C behavior.
- A separately compiled clock-cache negative positively changes guest output
  after the scripted first-wrap clock mutation.
- **360 bounded paths through the complete119-word func_151321D0 caller
  image**, using actual sine/wrap code, selector0/16, timer edges, flag clearing
  and two stack phases. Bounds/free are scripted boundaries; alternate,
  secondary and clamp paths, real heap and gameplay are not claimed.
  The real slot16 is **D_800898B0+0x40**, ROM22E3B0.
- **40 word / eight binding /478 live-and-frozen /12 checkpoint controls**.
  All **239 protected entries /220 distinct paths** stay fail-closed.
  Duplicate owner-path keys are covered by the same exact owned-path image,
  not silently excluded from input checks.

The float32 model does not establish hardware/FCSR or hardware NaN-payload
acceptance. Wrap completion is limited to bounded finite phases and NaNs;
retail infinity/huge-phase non-progress is not claimed away. Unchanged earlier
math and neighbor semantic receipts are reused, not reported as fresh suites.

## Complete Normal Image

Freeze all four successor pins, including the entire image, before production changes:
`73e16cc1c51f1ee12f996b964ad73d1c0864cc0d93f87dad2c40f609a44b9dee`.
The normal N64 build exits0 and its complete ELF equals this first prediction:
**128 code bytes + one extent byte =129 changed bytes**, zero metadata
changes, permutations or exclusions.

Compare all **6,057 disassembled function bodies**: only this target changes.
All function addresses agree; all symbol definitions agree except its
12-to160-byte extent. Every guard byte, compiler flag, layout, Makefile and
nominal conversion row stays unchanged. The restored placeholder was already
counted as C, so nominal conversion totals are not inflated by this recovery.
The owner has no CFE diagnostics; the pre-existing duplicate generated_12D630
recipe warning remains. This is not a warning-free build claim.

All **189,088 Game-data bytes /720 owners** stay exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Fresh official matching is **Game2,958/4,828 (61.27%)**, total
**3,631/5,501 (66.01%)**, **1,870 different**, zero address drift.
Init492/492 and Debugger181/181 remain exact. README changes only its two
aggregate rows; function narratives stay in the working documents.

## Fixture History And Bank

The four exact successor pins cover ELF, owner, prior sine checkpoint and
its live-input test adapter. Preserve both earlier first-image predictions
and the earlier separate reveal compatibility pin. Unknown current bytes
remain unknown; both archived fixture stages are checked before inversion.

Fresh affected checks: **three pass in53.531s**: the prior sine routine's
emission/actual-guard failure check, all live/frozen input corruptions and
immutable first-image/checkpoint audit. These are selected checks, not a
fresh full sine suite or a rerun of older reveal/white/constructor suites.
Those unchanged receipts remain in Note1497. Historical audits use their
own exact images after validating the current inverse; this target suite
supplies the current complete-image gate.

Twelve shared checks and one smoke check pass in each tools copy. Twelve
ASCII/AST parses and six task-file pairs pass. Verify exact old mirror
destinations before copying; preserve **1,098 unrelated hashes**,
**1,104 dirty paths**, and mirror HEAD **ddbdd16b**. No standalone commit/reset,
push, dependency/provider/account change, Claude call, host-port operation or
frozen Release action. Toolsd698926 first, then the consumer source/docs/pin.
Verify the native post-commit Graphify receipt and retain the19398 excluded
nodes /2972 existing files before closing.

## Finish And Next

- [x] Recover the complete40-word/frame0x20 body directly from semantic C.
- [x] Validate real actor home/S0 lifetime, actual helpers, private controls,
  aliases, faults, native32, independent links and bounded actual caller.
- [x] Freeze the entire first image before production edits and require exact
  normal-build equality, function/data/extent audit and ten installed tests.
- [x] Preserve fixture history; pass three affected checks and both tools-copy
  checks; bank toolsd698926 before the consumer source/docs/pin checkpoint.
- [x] Refresh official progress and README aggregate rows only.
- [x] Finish **func_150F22D0**, same owner,43 words, in
  [Note1499](1499-selector-point-transform-direct-restoration-and-match-20261017.md).
  Its full C switch matches with preserved retail-table binding and no new word guards.
- [ ] Keep both fade S0/private-lifetime gaps and wider Game matching open.
  Handwritten func_150A76F0 remains in the separate assembly workstream.

```sh
python3 -m tools.experiments.game_fixed_sine_update
python3 -m unittest tools.tests.test_game_fixed_sine_update -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
