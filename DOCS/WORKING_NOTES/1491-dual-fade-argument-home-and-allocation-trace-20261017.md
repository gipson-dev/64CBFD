# Dual Fade Argument Home And Allocation Trace

Date: 2026-10-17

Continue consumer **c65cb702**, tools **7960b37**, from
[Note 1490](1490-dual-buffer-fade-candidate-and-private-payload-gap-20261017.md).
Target **func_150D01A0**, VA **150D01A0..150D02B4**, ROM **FD650..FD764**,
**69 retail words / frame 0x30**. Recover and qualify the **record argument
home at SP+0x30**, with a complete **68-word / frame-0x30** candidate. It stays
**uninstalled**: no S0 save, old weight at SP+0x24, state pointer at SP+0x1C,
and **61 differing words across the full padded retail slot**. The one-word
extent gap is not a one-word matching gap. No guards or matching credit.

## Actual Compiler Captures

Reuse the prepared fingerprint-locked CFE/UOPT/UGEN and mode5 diagnostic
machinery with a target-owner adapter. All five newly owned compiler drivers
complete, including producers/consumers, required fired probes and cleanup.
Compare the complete emitted text/function/relocation/pool inventories with
each normal compile. Do not claim byte identity of unrelated debug metadata.
All three target raw fingerprints and both mode5 compiles retain their exact
normal code. Captures stay inside the ignored target build directory.

Select this procedure by its position in the **25-function owner inventory**,
then validate the complete ENT..END wire span and its one four-byte pointer
formal. Do not guess from a single VREG or from the frame size.

| Source form | Words | CFE automatic bytes | UOPT automatic bytes | Formal LDA records | UOPT P0 loads |
| --- | ---: | ---: | ---: | ---: | ---: |
| Original complete candidate | 65 | 20 | 12 | 0 | 0 |
| Explicit positive/else weight assignments | 64 | 20 | 12 | 0 | 0 |
| Addressed real argument object | 68 | 20 | 20 | 5 | 5 |

The first two forms promote the incoming pointer to **R16/S0**. The addressed
form retains loads from **P0**; UGEN merges them into three actual SP+0x30
loads. The unchanged 20-byte CFE automatic region and one pointer formal prove
that no padding, extra argument or dummy automatic object is introduced.

## Partial Source Recovery

The candidate explicitly reads the real parameter object through
`*(u8 **)&record` in the existing field expressions. This takes the address
of an existing pointer object of the same type. It keeps the one-pointer API,
unsigned wrapped clock subtraction, five real locals, original helper widths
and live buffer-index boundaries. It does not invent an argument-home array,
an opaque call, an extra parameter, a volatile qualifier or an SP-offset guard.

This is a qualified representation of the observed legacy argument home,
**not proof of the original C spelling or a unique source reconstruction**.
The original text wrapper really copies this caller-stack word. No source is
installed merely because the chosen expression influences the old compiler.

Raw candidate SHA-256:
`f061b64f4df1f19e93fc1570b41e99b88b5c873afbcba6a5feab50f202c89a8a`.
Clock HI16/LO16 bindings are at **+0x38/+0x48**, color JALs at
**+0x78/+0xCC**, and text JALs at **+0x9C/+0xF4**. All six are certified.
All **24 raw/padded neighbors** and owner pools/data remain unchanged.

Retail still requires old weight in **S0**, saved **S0 at SP+0x18**, saved
**RA at SP+0x1C**, and the second-window state pointer at **SP+0x20**. The
current form has no S0 use/save, saved **RA at SP+0x14**, old weight at
**SP+0x24**, and state at **SP+0x1C**. These are real outstanding contracts,
not interchangeable source homes or independent scheduling words.

## Allocation Evidence And Its Scope

Mode5 variable IDs are reused across procedures in the whole-owner log.
Joining all active records solely by identity includes unrelated functions.
First restrict the log to this function's **LOCAL OPTIMIZATION..REEMISSION**
markers, then match its procedure block, variable identity and expression.
Six boundary/poison controls ensure outside records and duplicate/missing
procedure markers cannot change or silently broaden the selected constraints.
The shared parser is unchanged; only this new consumer adds procedure scope.

For these fixed captures, match internal colors to the actual emitted code:

| Form | Variable | Internal color | Compiler marker | Evidence |
| --- | --- | ---: | --- | --- |
| Normal | P0 record | 14 | vreg true | Moves A0 into R16/S0 |
| Addressed | P0 record | -1 | vreg false | Keeps P0 loads, emits argument home |
| Normal | M-12 old weight | 8 | vreg true | T1, SP+0x24 call save; forbids color14 |
| Addressed | M-12 old weight | 8 | vreg true | T1, SP+0x24 call save; color14 no longer forbidden |

The internal vreg marker is **not** a recovered user register declaration.
Removing record promotion removes color14 from the weight's forbidden set,
but does not make the allocator select it. This isolates a second allocation
decision. Mode5's real-number printer remains suppressed: no numeric costs,
relative scores or printed compiler timings are inferred from this output.

Four committed source controls reject easy but unsupported shortcuts. An
array parameter produces the identical 65-word normal function; a register
weight hint produces the identical 68-word addressed function. A u16 weight
produces **69 words/frame0x30 but no S0 save**, so equal extent is insufficient.
The addressed explicit-branch form is 67 words and still lacks S0. Additional
ignored declaration-order and retained-temporary probes also fail the required
saved role; none is adopted as an original qualifier/profile recovery.

## Qualified Boundaries

All **ten tests pass in 66.689s**, without skips:

- **9,216 three-way public-memory/helper-call/return cases**, nine alias
  placements, four callback mutation modes, two stack phases and all 69
  original words. The new complete C and actual padding agree with each other.
- Prepared native32 **O2/O0 + UBSan**, **6,144 cases per profile**, separate
  body/typed caller and six effective signed-byte/factor/buffer controls.
- **Nine independent original/raw/padded links**, three symbol sets, signed-
  low carries, all six bindings and **144 three-way public cases**.
- The **complete 35-word original caller**, actual table slot and success
  contract across **256 three-way public cases**.
- Original **22-word color / 42-word text wrappers**, **eight cases** including
  both stack phases and the alpha-zero countdown. Actual copied payload word
  **8** now equals retail's record value **0x20000** on every text call. All
  sixteen words remain compared, and other private differences remain visible.
- **Two positively fired adversarial argument-home mutations**: replacing
  the real home after the first color call makes original/new use the alternate
  record's buffers, while the old S0-cached candidate demonstrably disagrees.
  This is an explicit emitted-ABI control, not evidence that the real color
  leaf mutates that home or a portable C callback contract.
- Three fresh CFE/UOPT/UGEN captures, two fresh owned mode5 drivers,
  **twelve fired capture-file hash controls**, six scoped-boundary controls,
  **68 raw-word / six binding controls**, **210 protected entries / 193 paths /
  420 live/frozen corruption controls**, and four negative source forms.

The first full run catches an alternate-record fixture clone extending beyond
its mapped tail. Copy only the valid 0x460-byte span, which still contains the
full byte-index table range; no accessed case or required test is removed.
Rerun all ten successfully. Complete private-state/access-fault parity, the
unfinished text consumer, final display, hardware and gameplay stay open.

## Bank And Next Step

Tools **0a0712a** commits the two new qualification files first. Eleven shared
tests pass in the active checkout (0.063s), and in the mirror (six in 0.028s,
five in 0.019s); tools-check and four ASCII/AST parses pass. Both task-file
pairs are exact. Preserve mirror HEAD **ddbdd16b** and **all 1,078 initial
dirty hashes**, yielding **1,080 dirty paths** after two new files. No mirror
commit, reset, push, provider/dependency change or additional Claude call.

Production C, guards, Makefile, normal ELF and progress CSV keep their exact
fingerprints. Fresh data audit: **189,088 bytes / 720 owners / zero differences**,
SHA-256 `0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Fresh official matching remains Game **2,953/4,828 (61.16%)**, total
**3,626/5,501 (65.92%)**, **1,875** different, zero drift. Init **492/492**,
Debugger **181/181** stay exact. Root README is unchanged, with no narrative.

- [x] Capture normal and branch formal/allocation behavior in owned compilers.
- [x] Recover and qualify the real record argument home without new storage.
- [x] Scope allocation identities by procedure and certify the partial ABI win.
- [x] Bank the candidate/tools/handoff without guards or matching credit.
- [x] Investigate old weight's caller-save versus callee-save decision after
  color14 is no longer forbidden in [Note1492](1492-dual-fade-native-caller-save-selection-20261017.md).
  Raw native costs/compare operands, actual flags and final colors establish
  caller cost2 versus S0 first-use cost4, not suppressed diagnostic numbers.
- [ ] Recover the source block/live-unit topology or establish the supported
  original compiler-profile cause of retail's different S0 selection.
- [ ] Recover S0, RA and state homes, close the full private/helper/fault gates
  and freeze a complete linked-image prediction before installation. The wider
  Game goal remains open. No host-port or frozen Release action.

```sh
python3 -m tools.experiments.game_dual_fade_argument_home
python3 -m tools.experiments.game_dual_fade_argument_home --trace
python3 -m unittest tools.tests.test_game_dual_fade_argument_home -v
make -C conker match-progress NON_MATCHING=1
make tools-check
```
