# Sine Phase Update Restoration And Match

Date: 2026-10-17

Continue consumer **07cfa90b**, tools **39c4f4e**, after
[Note1496](1496-actor-counter-motion-direct-restoration-and-match-20261017.md).
Restore **func_150F2480**, owner **generated_11F780**, VA
**150F2480..150F2518**, ROM **11F930..11F9C8**: **38 words / frame0x20**.
The complete semantic C body replaces its12-byte zero-return placeholder.
One expected-word guard normalizes commutative integer ADDU operand order;
this is a guarded linked byte match, not a direct raw-C match.
Tools **931d6c2** banks qualification and exact fixture adapters first.

## Recovered Contract

Capture the float state pointer once from **actor + *(s32 *)(actor+0x50)
+0xF8**, retaining it in S0 across four float helper calls. Compute sine of
phase0 and phase1, multiply by the respective amplitudes at state4/state5,
and store outputs at state9/state10. Then independently advance phase0 and
phase1 by their respective rates at state2/state3 times **D_800BE9A4**,
wrap through **func_15144B68**, and return1.

Keep the amplitude loads after their sine calls and reload the clock for the
second phase after the first wrap call. Preserve retail's0x20 frame, S0 at
SP+0x18 and RA at SP+0x1C. Use the existing SDK declaration for sinf and a
correct float-to-float wrap prototype; do not invent actor-field names,
extra local storage, forced registers or compiler-profile changes.

The wrap helper's retail bound is **0x40C90FDB**, approximately2pi. Tests
connect all104 sine words and24 wrap words, including sine's real outgoing
argument-home store. Bounded finite phases, signed zero and NaNs are covered.
Infinite or sufficiently huge phases can fail to make progress in the retail
wrap loops; completion on those inputs is not claimed. The existing sine
reference is reused rather than replacing retail math with host math.sin.

## Source Shape And Guard

Raw target SHA-256:
`c28ce833e8d95a2cac321ac6dab4f9ee7b2f83da45f0ea6b7c15343781ce51db`.
Check all38 words and eight relocation sites: four float calls and two
independent clock HI16/LO16 pairs. Reversing the source float operand order
recovers all four retail floating-operation words; the remaining difference
is **+0x10:01C48021 ->008E8021**, ADDU S0,T6,A0 -> ADDU S0,A0,T6.
There is no relocation at this site. Addition modulo2^32 is commutative;
ADDU has no overflow trap or condition flags. No memory access, frame,
schedule, saved-register lifetime or result changes.

Reversed pointer operands, array-address and32-bit-address forms retain that
one difference. Introducing a separate offset local instead produces40 words
and frame0x30, so reject it. The conventional pointer body plus one narrow
guard preserves the actual contract. The original guard-file byte prefix is
unchanged, as are all seven existing matrix-callback guards and all eight
other raw/padded functions in this owner. Owner data/literal pools agree.

## Qualification

The initial pre-installation screen passes ten tests in23.323s. The final
installed suite, including the compatibility correction below, passes all
**ten tests in40.580s**:

- **384 three-way guest/reference cases**, signed state offsets, six float
  patterns, four clocks and two stack phases. Adversarial float providers
  clobber caller-saved registers and outgoing homes, mutate the actor's
  offset after pointer capture, and change amplitudes/clock/second-phase
  data across calls. Full private state and literal access order agree.
- **48 guest alias cases**, placing the clock over phases, rates, amplitudes
  and outputs. All38 target words execute.
- **144 cases with actual retail sine/wrap code**, not scripted math hooks,
  checked against the independent existing float32 sine reference.
- **456 three-way real-access fault prefixes**, both connected helpers and
  adversarial hooks, with no observer-created memory reads. These qualify
  emitted guest order, not portable C faults or hardware exceptions.
- **Nine independent original/raw/padded links**,48 three-way executions,
  all eight sites and signed-low carries. Thirty-six isolated ADDU controls
  supplement the modulo2^32 argument. Corrupting the expected object word
  makes the actual padder fail.
- Native32 **O2/O0 + UBSan**, a separately typed caller,256 cases per profile
  and four effective output/rate controls. Native providers are deliberately
  scripted float ABI probes, not retail sine approximations. Native objects
  are aligned/nonaliased; amplitude mutation is guest-only because portable
  C does not specify multiplication-operand evaluation order.
- Two effective compiled **IDO negatives** break the output offset and cache
  the clock across a mutating wrap call; their guest results positively differ.
- **144 executions of the complete41-word func_1513B798 caller** with actual
  sine/wrap helpers, timer on/off, signed counter edges, -1/3 selector and
  two stack phases. Table slot3 is **D_80089C18+12**, ROM22E6E4.
  Freeing remains a scripted boundary, not real heap/gameplay acceptance.
- **38 word / eight binding /468 live-and-frozen /18 checkpoint controls**.
  All **234 protected entries /216 distinct paths** remain fail-closed.

The float32 model is not hardware/FCSR or hardware NaN-payload acceptance.
Unchanged earlier math/neighbor semantic receipts are reused, not presented
as fresh full-suite runs.

## Complete Normal Image

Freeze the entire linked prediction before production edits:
`39f955fd7d2a506df706bb6581bef6b106ad20bab4edcdf6693a13a7070a2d54`.
The normal N64 build and timestamp-settling rebuild both exit0. Make's final
up-to-date check exits0. The entire normal ELF equals its first prediction:
**119 code bytes + one extent byte =120 changed bytes**, zero metadata
changes, permutations or exclusions.

All **6,057 disassembled function bodies** are compared; only this target
changes. Every function address agrees and every symbol definition agrees
except the target's12-to152-byte extent. All **189,088 Game-data bytes /
720 owners** remain exact, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Compiler flags, layouts, Makefile and nominal conversion rows are unchanged.
The changed owner has no CFE diagnostics; existing duplicate-recipe and other
unchanged broad-build warnings remain. Do not call the build warning-free.

Fresh official matching: **Game2,957/4,828 (61.25%)**, total
**3,630/5,501 (65.99%)**, **1,871 different**, zero address drift.
Init492/492 and Debugger181/181 remain exact. README changes only two
aggregate rows; no function narrative is added there.

## Historical Compatibility And Bank

Keep the original five-member first prediction unchanged: ELF, actor owner,
guard CSV and the two actor-counter-motion adapter files. A targeted legacy
run exposed an older reveal audit's direct live-versus-archived guard
comparison. Separately predict its one-file compatibility edit before
installation, pinning reveal_tests to
`50b93eabc654c9fad88404f04478d50820f2fc7786dc882ce32954dd1b0ee6d2`.
Do not rewrite the original ELF or five-member prediction. Exact inverse
adapters check both fixture stages; unknown bytes remain unrecognized.

Final affected checks: **seven pass in159.102s**: actor-counter-motion
emission/input/first-image checks, white-fade input/unchanged-production
check, reveal input/first-image checks and constructor compatibility check.
These are selected checks, not fresh full legacy suites. Archived audits
compare their own immutable images after validating current exact inverses;
the new installed suite supplies the current complete-image gate.

Twelve shared checks and one smoke check pass in each tools copy. All14 final
ASCII/AST parses and seven task pairs agree. Removing four extra EOF blank
lines preserves the full ASTs, including source attributes. Preserve
**1,093 unrelated mirror hashes**, **1,100 dirty paths**, and mirror HEAD
**ddbdd16b**. No standalone commit/reset, push, dependency/provider/account
change, Claude call, host-port operation or frozen Release action.

Tools931d6c2 first; the consumer checkpoint banks source, guard, pin and docs.
Verify the native post-commit Graphify receipt before closing, retaining
the19398 nodes /2972 existing files excluded from the current scan.

## Finish And Next

- [x] Recover and qualify the complete38-word/frame0x20 C body.
- [x] Validate the single expected-word ADDU guard and all raw/padded neighbors.
- [x] Freeze the complete first image before production edits, then require
  normal-build equality and all6,057 body/address/extent checks.
- [x] Pass ten final installed tests, seven affected checks and both tools-copy
  checks; preserve original predictions and the separate compatibility pin.
- [x] Refresh official progress and README aggregate rows only.
- [x] Bank tools931d6c2 before the consumer source/guard/docs/pin checkpoint.
- [x] Finish **func_150F23E0**, same owner,40 words/frame0x20, in
  [Note1498](1498-fixed-state-sine-update-direct-restoration-and-match-20261017.md).
  Its complete semantic C body matches directly with no new guards.
- [ ] Keep both fade S0/private-lifetime gaps and wider Game matching open.
  Handwritten func_150A76F0 remains in the separate assembly workstream.

```sh
python3 -m tools.experiments.game_sine_phase_update
python3 -m unittest tools.tests.test_game_sine_phase_update -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
