# Transition Burst Real Object Layout And Guarded Match

Date: 2026-10-17

Continue consumer **1dd59606**, tools **e12376f**, from
[Note 1487](1487-transition-burst-pointer-and-flag-lifetime-recovery-20261017.md).
Recover **func_150CF800**, VA **150CF800..150CFBEC**, ROM **FCCB0..FD09C**,
1,004 bytes / **251 words / frame 0x108**. The complete semantic C has the
real object homes and eleven remaining compiler scratch-register differences;
eleven explicit guards produce the complete retail word sequence. This is
guard-assisted, not a direct raw-compiler match or completion of the Game goal.

## Real Object Placement

Move the existing, genuinely used **f32 progress** declaration ahead of the
88-byte descriptor and 16-byte payload. Do not add storage, padding or fields.
The emitted descriptor/payload addresses become **SP+0xAC / SP+0x9C**, closing
every stack-displacement difference from Note 1487. Parent S4, payload-pointer
S3, transition home SP+0x84, first flag branch and full tail remain correct.

Owned compiler captures explain the placement rather than infer it from frame
size alone. The CFE automatic region remains **128 bytes**, but the descriptor's
LDA home moves **M-88 -> M-92**, and the payload **M-104 -> M-108**. The actual
text/function/binding/pool inventories remain identical between each normal
candidate compile and its fired CFE/UOPT/UGEN capture. All producer/consumer/
driver lifetimes finish and probes are removed.

Moving any of three other existing four-byte scalars ahead of the aggregates
produces the identical raw target and bindings. This establishes the storage
mechanism, not a unique reconstruction of original declaration order. A wrong-
home control is rejected by the raw identity gate, structural normalizer and
actual expected-word padder. No SP-displacement guard is introduced.

Raw target SHA-256:
`dd76d6be5742594b4c4445d30efda676e9ab249bbd0e5ed8743f8c37b1fbd8b7`.
All **31 bindings**, **24 raw/padded owner neighbors**, the original helper
interfaces and first-flag/loop branch-delay behavior remain qualified.

## Narrow Scratch Normalization

Only words **189, 190, 191, 192, 193, 194, 197, 198, 201, 208, 209** differ.
Over the bounded 189..209 interval, a bijective scratch-register relabeling
derives exactly those eleven expected/replacement pairs. Decode actual GPR
operand fields; do not touch jump target bits, immediates, memory offsets,
control flow, argument registers or callee-saved registers. The two completed
cycles cover T0/T2/T6/T7 and T5/T9/T8/T3; unused closing edges are inactive.

Flag-width variants emit identical words. Staging the flag expressions adds
instructions and is rejected. Keep the complete semantic routine, proper
one-pointer/success-result interface, byte reads, unsigned RNG remainders,
full descriptor/payload and live post-callback transition reload.

## Existing Constants

The six motion constants reproduce the existing 24 retail bytes at
**D_800A0860..D_800A0874**. Add only the established target-specific
`RETAIL_RODATA_SYMBOL := D_800A0860` mapping; compiler flags remain O2/g3.
Bind the raw pool references to the existing data, rather than emitting a new
pool. Its eight compiler alignment bytes are not retail constants and must
not overwrite the adjacent child-motion damping values at **D_800A0878/87C**.
The normal full-image/data audit is the acceptance gate for this mapping.

The alternate `Another Source/CBFD-Recompiled/conker/conker/src/game/game_FC5F0.c`
still labels itself auto-decompiled/non-matching and has incorrect word/float
reads and stack-object types for this function. It supplies no byte-exact
implementation to import; no alternate-source code or prototype is adopted.
Zero Claude calls, provider/account/model changes or dependency changes.

## Qualification

The focused checks cover:

- **2,688 three-way original/raw/guarded cases**, complete modeled memory
  including all inherited descriptor bytes, final registers, calls and ordered
  ISA accesses. Unlike the displaced predecessor, raw and original complete
  return state now agree too. All 249 reachable original words execute;
  the two divide-by-zero BREAK words remain unreachable with divisors 65/101.
- Actual **54-word factory**, eleven-word SDK copy and two three-word tag
  leaves. Script RNG, direction output, sine and lower allocation explicitly.
- Prepared native32 O2/O0 + UBSan, **1,728 cases per profile**, complete C and
  a separately compiled typed caller. Four effective source controls exit 22.
  Word-sized gate/slot controls pass little-endian native checks but fail their
  real big-endian MIPS guest checks; preserve this positive limitation.
- **4,654 paired access-fault prefixes / 9,308 positively fired instances**,
  across inactive, incomplete, full/null/alternating allocations, callback
  mutation, live padding and both stack phases. All actual factory/copy memory
  accesses participate; guarded/original complete modeled state and IO agree.
- **Nine independently linked targets / three symbol sets / 96 three-way
  cases**, with signed-low carries, all 31 bindings and an independently
  relocated actual factory. Rebind local raw pool references to the explicit
  retail anchor, never suppress them.
- The original eleven-word kind-12 dispatch window, **128 three-way cases**.
- **251 raw-word / 31 binding / eleven expected-guard corruption controls**.
- **198 protected entries / 182 paths / 396 live/frozen corruption controls**,
  plus exact before/after checkpoint fixtures for the five approved artifacts.

This is not full dispatcher, real allocator/RNG/direction/sine, portable C
padding or exception semantics, N64 MMU/FCSR/CP0, hardware or gameplay acceptance.
The native checks omit six representation bytes; the emitted-MIPS complete-
memory checks do not. Old frozen candidates retain their immutable baselines.

## First Complete Prediction

The first complete predictor reproduces the normal predecessor ELF exactly,
then verifies the full successor before any production edit. It predicts
**773 changed bytes: 759 code, two symbol-size, twelve metadata**. There are
zero metadata exclusions. The metadata is one explicitly checked ordering
permutation: **D_800A0860, D_800A0490, D_800A4990 -> D_800A0490,
D_800A4990, D_800A0860**, preserving all symbol values/sizes/types/sections.
An initial failed prediction identified exactly those twelve bytes before
the first accepted prediction was frozen; no arbitrary metadata is ignored.

Expected complete ELF SHA-256:
`3a166821cbf72bc1d0576277659ee0079e896cae66b7f33f1aa15a019a47308a`.
Owner source:
`0ed6b7d1ac20065bb63096427a011a389901654bc9f2ae99f369c399ea2314ca`.
Guard manifest:
`fc6e9c02547bebd537ab093029b210586e4e54e0342ce415845e37eb4cfbddf5`.
Makefile:
`ebd94346464987605699e4709194a11c08e248f02d94a400580690e0bdda7c69`.
The older child checkpoint gains only an exact approved-successor adapter,
with SHA-256 `4d7324b83d63ad1c814507f980783d6c3f70d29f2d63536326f9dd11aefe6190`.

- [x] Recover real object placement and qualify the guarded full function.
- [x] Freeze the complete independent prediction before production edits.
- [x] Verify the normal rebuild equals that prediction, all data and final installed tests.
- [x] Remeasure matching, bank tools first, then consumer source/guards/mapping/docs/pin.
- [ ] Continue broader Game matching; next nearby placeholder is func_150CF484.

No host-port/frozen Release action, push, mirror reset or unrelated cleanup.

## Installed Bank

All **twelve installed tests pass in 133.014s**, with no skips. Thirteen
archived predecessor/child behavior, compiler, caller and rebase checks pass
in **76.513s**. Their historical image/input-stage assertions are superseded
by the current full-image, 396-input and **fifteen exact checkpoint controls**;
do not describe those older stage gates as newly run against this image.
The normal rebuild finishes with the existing duplicate generated_12D630
recipe and pre-existing warnings in unchanged compilation units.

All five live artifacts equal the frozen prediction before approved after
fixtures are banked. The full Game-data audit passes: **189,088 bytes / 720
owners / zero differing bytes or owners**, retaining SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
A final unmocked freeze rechecks all 198 inputs after documentation edits.

Fresh official matching: Game **2,952/4,828 (61.14%)**, total **3,625/5,501
(65.90%)**, **1,876** different, zero address drift. Init **492/492** and
Debugger **181/181** remain exact. Nominal conversion rows stay unchanged
because this replaces an existing C placeholder. Root README changes only
the two aggregate matching rows; detailed narrative stays here.

Tools **e537123** commits the five new qualification files and exact prior-
checkpoint adapter first. Eleven shared padder tests pass in the active
checkout (0.050s) and mirror (six in 0.029s, five in 0.019s); tools-check and
all **twelve ASCII/AST parses** pass. Six task pairs match across both copies.
Preserve mirror HEAD **ddbdd16b**, all **1,066 unrelated initial dirty hashes**,
and all other work. The one approved predecessor edit plus five new files
yield **1,072 dirty paths**; no mirror commit, reset or push.

The consumer bank contains this function, eleven manifest rows, the existing-
constant anchor, tools pin and documentation only. Continue **func_150CF484**
next; broader Game, rendering and gameplay acceptance remain open.

Prepared-checkout commands:

```sh
python3 -m tools.experiments.game_transition_burst_match
python3 -m unittest tools.tests.test_game_transition_burst_match -v
make -C conker -j4 build/conker.us.elf progress.csv
make -C conker match-progress NON_MATCHING=1
make tools-check
```
