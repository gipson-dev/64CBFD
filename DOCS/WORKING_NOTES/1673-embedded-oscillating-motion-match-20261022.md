# Embedded Oscillating Motion Direct C Match

Date: 2026-10-22

## Result

Recover `func_151B8C54` in `conker/src/game/generated_1E5FF0.c` from
its twelve-byte zero-return placeholder. All **42 words / 168 bytes,
frame 32 and six bindings** emit directly from complete typed C under the
normal O2/g3 profile. No guards, frame patches or profile overrides.

VA 151B8C54..151B8CFC / ROM 1E6104..1E61AC, ends exclusive.
Preserve the original routine in `conker/asm/1E5FF0.s`, the existing
OscillatingMotionRecord type and all three neighboring routines.
Keep the address-based name and add a purpose comment plus one private
44-byte EmbeddedOscillatingMotion type. Conversion rows and denominators
remain unchanged.

## Recovered Contract

The callback accepts a byte actor pointer and returns integer 1. Its motion
block begins at actor+0x120; the oscillation output is a separate field at
actor+0x58. Do not conflate this layout with func_151B8B40's smaller record.

| Actor Offset | Meaning |
| --- | --- |
| +0x58 | Separate oscillation output |
| +0x120 / +0x128 | X / Z coordinates |
| +0x124..+0x127 / +0x12C..+0x12F / +0x140..+0x143 | Reserved bytes |
| +0x130 | Phase |
| +0x134 | Oscillation base |
| +0x138 | Phase rate |
| +0x13C / +0x144 | X / Z velocities |
| +0x148 | Oscillation amplitude |

Call sinf with the old phase. After the call, read the live amplitude and
base and write sine*amplitude+base to actor+0x58. Advance phase by
phaseRate*D_800BE9A4, store it, call func_15144B68 with that updated value
and store the returned phase. Then advance X and Z in order using their
live velocities and separate live clock reads. Preserve separate float32
multiply/add operations, late helper effects and all untouched bytes.

The actor pointer is saved in its incoming home at current SP+0x20;
the motion pointer is saved at current SP+0x18 across phase normalization.
The real integer-1 callback result controls the caller's removal flag.
Do not retain the old zero return or make the routine void.

## Exact Emission

Raw unlinked body SHA-256:
`124c16bcaeeacbd886b8c4939afc89955d4103c546be9a5276ef9bd2a6dd654f`.

| Offset | Binding |
| --- | --- |
| +0x0C | R_MIPS_26 sinf |
| +0x18 / +0x34 | R_MIPS_HI16 / R_MIPS_LO16 D_800BE9A4 |
| +0x50 | R_MIPS_26 func_15144B68 |
| +0x5C / +0x60 | R_MIPS_HI16 / R_MIPS_LO16 D_800BE9A4 |

Independent original GNU assembly, fresh isolated C and full raw owner agree
on complete words and bindings. The ordinary generated-owner three-command
Make recipe reproduces raw code, padded code and metadata. Preserve all
three raw/padded neighbors and pools, including the already-matching
func_151B8B40. The entire guard manifest remains byte-identical.

## Qualification

Identical task tools in both copies:
`experiments/game_embedded_oscillating_motion.py` and
`tests/test_game_embedded_oscillating_motion.py`.
Reuse the established oscillating-motion oracle, native32 runner, padder,
GNU link and strict image gates, replacing the target layout and caller
fixture. Routine Codex work uses zero Claude calls.

Full pre-install suites pass eight tests each in 6.779s / 6.972s with zero
errors, failures or skips. Shared tools checks pass in 0.176s / 0.107s.
Fresh installed checks pass two tests per copy in 2.548s / 2.527s. Explicitly
reuse the other six pre-install checks only under strict source, raw/padded
object, guard, helper/input and complete-image identity; they are not fresh
installed runs.

- 443 cases produce 886 guest phases, including 112 guest clock-alias
  phases, post-helper mutation, zero/sign/large values and unusual float
  representations. All 42 target words execute. Check complete register,
  private stack and public-memory agreement against original emitted code.
- Native32 O0/O2/O3 each pass 366 finite disjoint cases, with trap UBSan,
  separate float operations, actual private-tail and actor offset/size
  checks and whole actor/fence comparison. Twelve effective defined wrong-C
  controls cover the separate output, base, amplitude, phase rate, wrap
  argument/result, X/Z velocities, accumulation, return, cached clock and
  reserved-byte clear. Native aliases are not claimed.
- Connect the original 104-word sine and 24-word normalizer across 72 phases.
  Visit 124 helper words, including all 24 normalizer words. Scripted native
  helper results are not claimed as native libm validation. Huge/infinite
  normalizer completion and general FCSR/hardware parity remain unclaimed.
- Nine independent original/C/padded GNU links cover 72 rebase phases,
  all six bindings and signed-low HI16 carry. Check 192 fired target-access
  fault prefixes, 32 frozen/live inputs and seven strict image corruptions.
  Instruction-fault agreement is not portable C fault/MMU semantics.

## Caller Bounds

The aligned retail scan finds no direct JAL references and one literal
target pointer, ROM 22F858 / VA 8008AD98: slot 2 of D_8008AD90.
This does not exclude constructed targets.

Qualify the actual func_151572D0 dispatcher window 1515731C..15157358,
fifteen executed words, across sixteen phases. Signed selector -1 skips the
callback; selector 2 loads the real table entry and transfers the actor
pointer. The return value 1 preserves A2's clear removal flag, with actor
reloaded into A1. An effective old-stub execution returns zero and incorrectly
sets the removal flag, demonstrating why the return type/value matters.

The first caller-fixture run stopped at an unsupported LB instruction.
Add its standard signed-byte semantics only to this local test class;
the -1/2 paths then pass. No shared emulator or production change is needed.
Retain the full 84-word parent's unchanged twelve-byte production placeholder.
Timer eligibility, later callback tables, removal helpers, full-parent
execution and natural gameplay remain outside these bounded windows.

## Production

The independent complete-ELF prediction permits exactly
**138 changed bytes = 137 code bytes + 1 function-size metadata byte**,
with zero exclusions.
ELF SHA-256:
`87b1175d6d301c17ae6db273c2c866d7fab43237bfba0794aa2e94912f658a09`.

Commit tools first: `b6ea02b4c41afa8c870c5cd4c24cb792f9cd62b4`. No push.
Preserve all 1,558 prior older-mirror dirty paths, statuses, hashes and HEAD;
add only two task files, leaving 1,560 dirty paths. Do not reset or commit it.

Seal 15,862 files and all 1,454 linker objects. Normal Make completes in
0.481s in the verified Linux copy. Mark only the verified unchanged guard
manifest old to avoid unrelated historical-object rebuilds. Existing
generated_12D630 duplicate-recipe warnings remain; isolated diagnostics are
empty and full-owner diagnostics are unchanged.

The installed linked audit preserves all other 6,054 bodies, all 6,055
addresses and all 720 protected Game-data owners / 189,088 bytes.
Protected-data SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Live adoption audit passes in 72.375s. Verify every static input and
non-target object before and after promoting only the target owner object,
ELF, linker script and progress CSV. Linker-script and conversion-CSV bytes
remain identical. The complete live image reproduces the independent
138-byte prediction.
Padded owner SHA-256:
`bab75054f2d6dff8ee64d5b045be8bdd7e843bafdba560d5cf2168aeacdddc2a`.

## Handoff

The standard matcher against the actual live ELF completes in 34.401s:
total **3,742/5,505 (67.97%)**, Game **3,069/4,832 (63.51%)**,
Init 492/492 and Debugger 181/181 exact. Zero address drift; 1,763 different.
The 75% threshold remains 4,129 exact, requiring **387 more matches**.
Queue shapes: 1,632 placeholders, 122 semantic/other and nine unlocated.
Next func_151749F8 is screened only, unmodified and uncredited.
Keep func_1508CAD8's 862-word stub queued.

Root README changes only its two aggregate rows. Detailed updates belong here
and in concise indexes. Post-commit graph-worker and every-old-node audits
remain private receipts. Preserve excluded-corpus/large-HTML caveats without
claiming full re-extraction or a fresh corpus-membership recount.
Host Release remains untouched.
