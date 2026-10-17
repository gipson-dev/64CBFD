# Sequence Record Setup Certified Guarded Match Qualification

Date: 2026-10-16. Consumer predecessor **7e7871a5**, tools predecessor
**b9e0781**. Continue the same **func_1501D348** selected by
[Note 1466](1466-sequence-record-setup-frame-and-private-home-recovery-20261016.md).

## Qualified, Not Installed

The real generated-object padder and linker now reproduce **all 473 retail
words / 1,892 bytes** with **165 expected-word/relocation guards**. This is
a **guarded match, not direct compiler output**, and is **not installed**.
Production conker/src/game/generated_49D30.c retains its zero-return stub.
No matching credit, root README change or production rebuild this turn.

Retail: VA **0x1501D348..0x1501DAAC**, ROM **0x4A7F8..0x4AF5C**. The complete
semantic C remains Note 1466's **474-word PREHEADER** body, with its proper
**void(s32 scene, s32 sequence, s32 slot, s32 hook, s32 parameter)** API.
Keep frame **0x78**, original S0-S5/RA saves and lifetimes, eight private
homes, incoming homes and the established **O2/g3/no-unroll** profile.
No frame/home/argument repair, inserted instructions or truncated C body.

The qualification is tools/experiments/game_sequence_record_setup_matching.py.
Its SELECTED equals frame.PREHEADER; the six locals and typed resource,
descriptor, runtime and provider semantics remain unchanged. The original
recovery's SELECTED also remains INITIAL. All **56 raw and 56 padded owner
neighbors** are unchanged; this does not mean those other routines all match
retail. See Note 1465 for the full recovered semantic contract.

## Certified Normalization

The seven new source screens did not recover the preheader: unsigned cursor
and increment-placement variants retain 474 words, while index/pointer/byte-
base spellings shrink to 471. A lower difference score is not a match. Do
not repeat this or Note 1466's 58-screen sweep as new evidence.

Certify the remaining induction operation instead of patching it on score:

- Raw word **279 / +0x45C**, **sll t8,s3,3**, is omitted only after a complete
  CFG constant analysis proves **S3 = 1** on every incoming path.
- The scale result's only live use before redefinition/clobber is raw word
  **282 / +0x468**, **addu v0,a3,t8**. Derive **addiu v0,a3,8**, emitted word
  **281 / +0x464**, from that invariant. No memory operation changes.
- Reject an additional use of T8, a branch target into the omitted word,
  placement in a branch delay slot, a relocated arithmetic operand or an
  unexpected return-link read. The raw caller reads RA only for its entry
  save and restored return, at raw words **7 and 472**.
- Recompute conditional branch displacements through the one-word deletion.
  Preserve branch-likely annulment and delay execution on both successors.
  All **89 shifted relocation bindings** must equal the independently
  assembled original map before any register normalization is accepted.

The remaining differences are certified **scratch GPR allocation**, not
blindly accepted by masking registers. Compare the complete folded C and
original instruction streams with a relational fixed-point analysis:

- A state records must-equal register pairs plus actual known constants.
  Join by intersection. Relocatable immediates are unknown symbolic values,
  never the numeric zero temporarily present in an unlinked instruction.
- Check ordered operand equality before each instruction, including loads,
  stores, branches and indirect targets. Identical memory operands preserve
  memory equality inductively. Track value-preserving copies and redefine
  result pairs only after their inputs have passed.
- Only **AT/V0/V1/A0-A3/T0-T9** may change allocation. Zero, saved registers,
  GP/SP/FP/RA fields cannot be renamed. No commutative swap was needed.
- Execute delays according to the CFG. At every call, require identical ABI
  argument and nonvolatile roles, then discard caller-saved facts. Retain
  only a declared primary word result, not arbitrary post-call scratch
  equality. The shared-memory/provider contract remains explicit.
- Check final saved/return roles. The fixed point covers arbitrary loop
  iterations, not a bounded concrete unroll: **409 normal CFG nodes, all
  473 words, 32 call sites, one return**, **891 transfer steps** in this run.
  The raw cursor proof separately reaches all 474 words.

Export exactly **165 guards: 164 replacements and one omission**, no
insertions. Replacements include the derived address form, relocated branch
displacements and certified scratch fields. The actual assembler/padder
output, not a synthetic desired-word list, is linked and compared with ROM.

Opaque providers observe explicit ABI inputs/shared memory and preserve
nonvolatile state. This does not prove arbitrary raw-C helper behavior that
inspects its caller's return address. Original/guarded literal instruction
and fault parity is checked separately at the same entry; raw-C scratch/PC
fault equality is not claimed.

## Frozen Artifacts

All raw/original words, relocation maps and absence of private pools are
fail-closed inputs. Raw C remains:

```text
474-word raw text
7591a7e391b9c2d3a36cd1e86e8200e5794d8f5f1ef149f0ec1b20bc2708e2e8
89-binding raw relocation map
19aeaceffebfc1008e6faa7023b1bacc129f134af966962ced320d537e6cd331
473-word independently assembled original text
fed829450c08e9bb8a198c16a1d20d8e139a95b9b9f9c8aa437824e5e092fd4b
89-binding original relocation map
603e444031fa99b5f8e464abc59fd43134ffc586e38a814680354702f4608eb2
```

Preserve every old guard byte and its **298 CRLF lines**; append only the
certified target rows. These are **private qualification artifacts**, not
an installed CSV:

```text
Live predecessor guard manifest
2e182911b8f362b3dc5fcf8e690b2fdb3d69ea2aa9ce0c459beb95bbcad79302
Qualified complete guard manifest
bb20ecd3785ed2e3fe949d7c9a4bfa8f6648b78e5f9eb1712af941c38faf415b
Exact 165-row appended suffix
5b608c639774703df51abc471e893f1d9cc9e4058f03cfcb2275717176a7891c
```

## Fresh Qualification

All **eight final tests pass in 122.782s**, no skips. After comment-only proof
annotations, the focused proof-control test passes again in **2.537s**.
The initial run's sole failure was an off-by-one test expectation for the
first cursor-one initializer: actual words **89/95**, not 90/95; no candidate
or normalization logic was changed to address that fixture error.

- **484 three-way guest cases** execute original, complete raw C and actual
  guarded output against the independent ordered reference. Visit every
  **473/474/473 word**, check complete memory including private stack,
  ordered R/W events, all provider packets/snapshots and every call's saved
  roles/eight homes. All eight diagnostic provider gates fire positively.
  Original and guarded complete GPR/FPR/LO/event/PC/delay states agree.
- **60 native32 cases each at O2 and O0 with UBSan**, no fwrapv or LTO. Use
  the full actual C body, actual restored reset and separate typed caller/
  provider units. Check all **756 fields**, bank padding/canaries, used
  arena bytes/gaps/guards and protocol snapshots. Native tests qualify C,
  not execution of MIPS guard rewrites.
- All **eight native functional controls** compile/run and fail with
  **21/22**, not signals or sanitizer traps. Cover descriptor width, skipped
  group, capacity stride, stale runtime cell, process index, signed total,
  stale request status and callback parameter.
- **Nine effective symbolic controls** reject wrong cursor value, another
  live scale use, escaping return link, delay placement, direct branch
  target, wrong store input, wrong call argument, broken loop-carried role
  and changed non-register bits. These exercise the proof beyond hashes.
- Corrupt each of **474 raw and 473 original words**, **180 binding cases**
  including extra entries, raw/original pools, all **1,815 guard fields**
  and all **136 production inputs**. Every unknown is rejected.
- **Three independent original and guarded links each** compare every
  473-word body across HI16/LO16 carry boundaries. SDK and Game call symbols
  stay in the same MIPS jump region; this is not a hardware/runtime test.
- **417 positively fired original/guarded access-fault prefixes** compare
  literal memory, registers, events, provider state, PC/delay and access
  state. Bounded ABI-hook accesses are included; bulk provider/bzero bytes
  are not claimed as instruction-level SDK emulation.
- All seven new source screens receive two diagnostic witnesses only;
  the unselected alternatives do not inherit complete qualification.

Raw guest execution uses private **0x16010000** to avoid shadowing the next
provider with its extra word. Original/guarded use **0x1501D348**. Keep
Note 1466's valid-array, bounded allocation, actual-reset/opaque-provider,
NULL-failure, arbitrary-alias and gameplay/hardware limits. Complete caller
and real-helper-chain acceptance remain installation work.

## Bank And Install Handoff

Tools **c7c0d87** banks three new experiment/test files before the consumer
pin. Both copies have identical pairs and **six ASCII/AST checks**. All
eleven WSL padder tests pass per copy: active **0.032s + 0.022s**, mirror
**0.030s + 0.019s**; consumer tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **964 initial dirty-file
hashes** and its independent history; **967 final dirty paths**. No mirror
commit/reset, push, Claude call, REA reinstall, dependency/configuration
change or host/frozen Release action.

All **136 live inputs** remain unchanged: source/caller, guards, Makefile,
ELF, progress CSVs and root README. The ELF remains
**17e327a95fcf43c50ac2611a19461980ad1d44664a3c3a218d593f35e26cd4ab**.
Last installed measurements are still **Note 1464**, not new measurements:
Game **2,939/4,828 (60.87%)**, total **3,612/5,501 (65.66%)**, different
**1,889**, zero drift, converted **5,501/6,044 / 86.04% bytes**.

Prepared-checkout reproduction, sequentially:

```sh
python3 -m tools.experiments.game_sequence_record_setup_matching --guarded
python3 -m unittest tools.tests.test_game_sequence_record_setup_match -v
make tools-check
```

- [x] Qualify the cursor-one fold, dead scale omission, branch routing and complete scratch-role fixed point.
- [x] Produce all 473 retail words with the actual padder, preserving frame/homes and all neighbors.
- [x] Complete native/guest, effective controls, fault prefixes, rebases and fail-closed guards/inputs.
- [x] Bank tools first and update concise indexes without changing production or root README.
- [ ] Verify actual caller packets and narrow void-five-word declarations where needed; qualify required real-helper windows/chains without claiming full gameplay.
- [ ] Reproduce the predecessor and predict the entire first ELF/source/guard successor before installation, including exact metadata changes.
- [ ] Install only source.recovered_owner(before, SELECTED) and the certified guard append, preserving unrelated source and all old guard bytes.
- [ ] Run the normal build, target/affected tests, whole-image/function/data audit and fresh progress measurement; then update root README aggregate rows only and bank tools first.

Continue this same function's installation gates next. Do not reopen the
resolved preheader or switch to another stub. Wider Game matching, timing's
141 differences and full gameplay acceptance remain separate open work.
