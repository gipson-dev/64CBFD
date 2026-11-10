# Angular spring and phase update restored to matching C

Date: 2026-11-10. `func_150C4D20` replaces a zero-return placeholder with
the complete angular-motion updater: **95 words / 380 bytes**, original
**0x48 stack frame**, and **six relocation-aware scheduling guards**. The
semantic C emits all 95 words; 89 match directly. The guards reorder existing
instructions in one post-helper block. No inserted or omitted instructions,
opaque assembly, profile change, shared-header change or new data pool.

Fresh production-ELF recount: **4,318 / 5,513 (78.32%)** total; Game
**3,645 / 4,840 (75.31%)**; Init **492/492**; Debugger **181/181**.
Zero address drift, **1,195** different, **93 more** accepted matches to
4,411/5,513 and the active 80% goal. Conversion CSV and converted-byte totals
remain fixed. Root README receives aggregate table changes only.

Baseline consumer `1b04d1694ed82e07832d86bd377dc31de10c2bab`; tools
`877567d5791e6676f83df5e184dd603fff52a345`, from
[Note 2248](2248-game-event-dispatcher-direct-match-20261110.md).
Bank eight proof files first in tools commit `07f41c42e2e6b526d233bc339d6b93c73c1eb9af`. Local commits only.

## Source, field view and arithmetic

Owner `conker/src/game/generated_F21D0.c`; complete original retained in
`conker/asm/F21D0.s`. Retail VA **0x150C4D20..0x150C4E9C**, ROM
**0xF21D0..0xF234C**. The old 12-byte stub differed in 91 retail-slot words.

The local `AnglePhaseRecord` names only the known 0x80-byte prefix of the
engine's 0xA0-byte script-object record. Angle is float +0, signed position
halves +0x10/+0x12/+0x14, flags byte +0x4F, angular velocity float +0x60 and
signed phase word +0x7C. Padding denotes unrecovered fields. Native static
assertions check every offset and prefix size. This introduces no shared
object-layout claim or rename of the retail function symbol.

The recovered interface is `void func_150C4D20(AnglePhaseRecord *state)`.
Actual callers supply the record pointer in A0 and ignore V0. This supports
a side-effect-only semantic interface; it does not prove the original C
return type. Callback fields +0x38/+0x78 and metadata byte +0x92 are owned
by the engine's separate registration paths.

The routine performs these operations in retail order:

1. Snapshot angle and velocity. If angle is greater than 180, subtract 360
   once for the restoring-force calculation. Add the signed phase and global
   `D_800BE9E4` as wrapping 32-bit words, preserving retail ADDU semantics.
2. Subtract angle times `D_800A03F0` from local velocity with single-precision
   rounding. If the rounded signed phase is at least 256, subtract 256 once,
   truncate, and submit positional sound `(15, 0x55F0, 0, 0, 0, x, y, z,
   500, 1000)` to `func_10010F88` using signed coordinate halves.
3. Restore captured phase and local velocity across audio, then publish phase.
   Call `func_15048A40((u8)phase)`. Multiply its result by live `D_800A03F4`,
   add to local velocity, and add that scale again when live flags bit 4 is set.
4. Multiply by live `D_800A03F8`, store velocity and add it to the live angle.
   Re-read angle; add 360 once when negative, otherwise subtract 360 once
   when at least 360. This is a single-step correction, not repeated modulo.

Retail constant values are approximately 0.009, 0.1 and 0.8. Helpers may
change record fields and constants: tests distinguish captured local velocity
and phase from live flags, angle and post-helper constants. The original
sound helper remains an effectful ABI model; this does not qualify audio
hardware or the full helper implementation.

All possible signed32 phase sums have defined truncation here: the largest
rounded float is 2^31; the taken path subtracts exactly 256, giving at most
2^31-256. The taken operand is nonnegative and below 2^31. No invalid
float-to-int prefix is reached by valid target inputs. Cases cover extrema,
rounding boundaries and wrapped sums. NaN/infinity angle and velocity cases
use IEEE float classes in the independent model; FCSR/trap/hardware behavior
is outside the claim. The SDK32 native ABI supplies the qualified two's
complement conversion from the wrapping unsigned word back to signed phase.

## Compiler shape and six guarded scheduling words

The initial complete C body emitted 95 words/frame0x48 with 26 differences.
An explicit phase load before the wrapping addition and normal typed argument
and local declarations recovered the retail register lifetimes and homes:
phase SP+0x38, local velocity SP+0x44, saved S0 SP+0x30 and RA SP+0x34.
The bounded source screens are retained as private experiments.

Selected raw target SHA256:
`6416ccd1d79276028d661eab8e2d1318805244810b71fa9f571b2892c9972982`.
The only remaining difference is the seven-word block 56..62. Its normalized
order takes old indices **58, 59, 60, 56, 62, 61, 57**; index 61 is unchanged,
so six expected-word guards are appended. The D_800A03F4 HI16/LO16 pair moves
with its instructions. Expected and replacement relocation sets are checked.

The address in AT is consumed before AT is reused for the 360 constant;
F12 is loaded before multiplication; F14 is not read until the final wrap.
The scale, flags and saved-velocity memory accesses retain their exact order.
The operation multiset, opcodes, operands, branches, frame and private homes
are fixed. Raw and normalized runs agree at completion; normalized code and
retail agree at every tested access cut, including intermediate registers.
Raw intermediate register state and FP exception timing are not equated.

The complete previous guard manifest is preserved byte for byte as a prefix.
Existing neighbor guards remain unchanged. Both independent padders and GNU
linking agree with the bound retail routine; no arithmetic replacement or
frame-offset normalization is used.

## Owner, complete image and qualification

Freeze **2,250 input fingerprints** and retain exact mutable pre-adoption
inputs privately. Three actual Make commands agree with independent complete
owner compilation using the existing O2/g3 flags. All **five other functions**,
their raw and padded bindings and all owner data pools remain fixed. IDO emits
zero diagnostics. The owner register masks grow to account for the recovered
GPR/FP use; independent and actual-Make masks agree. The merged linked image
has no unexplained register-information or non-target section change.

The strict complete-ELF prediction accounts for **325 changed bytes**, including
the target body, symbol extent **12 -> 380**, and two closed four-symbol/string
metadata permutations. Every named definition is checked. **Zero exclusions**;
all **6,050 function addresses** fixed. All **189,088 protected bytes / 720
data owners** remain exact, SHA256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Makefile, profiles, headers, layout and conversion CSV remain unchanged.

Fresh focused proof in each local tools environment:

- **844 cases / 2,532 guest executions**, independently rounded float model,
  helper clobbers and mutations, global/record aliases, all phase bytes and
  timer boundaries. All 94 reachable words are visited. Word 84 is a retained
  unreachable duplicate compare; it is still checked literally.
- **832 native cases** at each of `-O0`, `-O2`, `-O3`: **177,664 exact public
  and call bytes** per profile, actual SDK32 field types, strict aliasing and
  UBSan. Only global/record address-alias cases are guest-only.
- **14 effective compiled negative controls**, each with a normally completed
  counterexample and zero earlier execution errors.
- Both padders, **105 word/binding corruptions**, **16 GNU linker comparisons**
  over four independent low-half symbol sets, and **64 rebased executions**.
- **138 literal normalized/retail access-cut pairs**. These qualify emitted
  guest instruction order, not portable C fault semantics.
- **48 original registration windows** and **144 callback pairs** cover table
  entry 36, both +0x38 JALR sites and first/repeated group paths. **512 pairs**
  execute the actual 48-word trig helper chain and all 65 table floats over
  all 256 phase bytes and both flag states.
- Eight strict-image corruption probes plus live-input, historical-guard,
  protected-data and complete-address checks.

Each environment passes eight fresh pre-install methods, followed by two
fresh installed methods and six exact-fingerprint semantic reuses. Shared
tool smoke checks are fresh; three prior unchanged regression receipts per
environment are explicitly reused. The sibling has **2,434 pre-existing dirty
paths**: it is not edited. Its existing helpers run through a private target
overlay, with missing read-only fallbacks recorded; actual Make invokes the
mounted CLI. This is not a clean standalone-tools-clone claim.

Production Make matches the independent ELF and binary prediction. Existing
whole-ROM nonmatching behavior still returns checksum exit 2; expected
duplicate generated_12D630 warnings are unchanged. Fresh progress succeeds.
ELF SHA256: `f68ebad0d744f75913eedc038bcb523f72c29974854274116cdf6b174052352d`.
Binary SHA256: `86e814919255a2f444938a6970823cf3d5302145a07f533d1aa855cd4f1bba95`.

Codex is the sole writer; zero Claude calls. No push, tool installation,
account change, host-port edit, save change or Release build. Full callback
parents, audio hardware, complete gameplay and FCSR remain unqualified.

## Graph and continuation

Scoped Graphify refresh retains or relocates all 59704 old
nodes; resulting graph 59705 nodes / 113091
links. Definitions outside the declared scope remain fixed apart from
community metadata. All six C function positions are checked. Historical
excluded nodes remain; this is not full-corpus re-extraction. Post-commit
receipts separately check actual graph-worker completion and heading moves.

```sh
python3 -m unittest tools.tests.test_game_angle_phase_150c4d20_match -v
make -C conker match-progress NON_MATCHING=1
```

Reproduction needs the prepared PSBBN consumer and retained pre-adoption
mutable inputs in `conker/build/game-angle-phase-150C4D20-match/frozen/`.
No private ROM/ELF binary is committed.

Next: **`func_151103C8`**, 95 retail words/frame
0x28, in `conker/src/game/generated_13D350.c`. Its 12-byte
stub differs in 94 retail-slot words, is unchanged by
this adoption, and remains uncredited. Inspect the complete original, callers
and helper contracts before reconstructing it. Keep the wider 80% goal active.
