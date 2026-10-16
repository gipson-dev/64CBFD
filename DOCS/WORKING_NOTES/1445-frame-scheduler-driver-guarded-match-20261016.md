# Scheduler Frame Driver Guarded Match

Date: 2026-10-16. Consumer predecessor **386548f2**, tools predecessor
**c820bde**. Previous goal turn: **progress**, restoring the coordinator.
Continue the full Game matching goal; this checkpoint does not complete it.

## Recovered Routine

```text
func_1501878C  VA 0x1501878C..0x15018DFC  ROM 0x45C3C..0x462AC
412 retail words / 1,648 bytes / frame 0x68
```

Replace the false zero-return C placeholder in game_45B80.c. Receive one
blocking scheduler message into the original SP+0x64 home, reset the
housekeeping byte/halfword, and dispatch its signed halfword tag:

- Tag 1: honor both live stop checks, perform pending resets/view updates,
  call the restored coordinator when enabled, then run the original ordered
  display-list passes with inclusive live bounds and s16 cursors.
- Preserve each global cursor store, mapped view byte, signed-halfword or
  full-word helper argument, and the SP+0x44 saved cursor used for capacity
  rollback. Compare the current page's base and live signed command limit
  only after the render helper returns.
- Retain the single-view overlay loop, including live count changes after
  entry. Do not collapse it into one call merely because its entry test
  observes a zero maximum.
- Emit the actual SDK graphics commands: microcode load, geometry state,
  model-view matrix load, LookAt-X and **first-light** records, then final
  full sync/end. The second 16-byte record is DC08060A, not the standard
  SDK LookAt-Y DC08030A. This is a recovered destination, not a renderer fix.
- Preserve the hold-byte decrement/reset and independent requested/current
  audio-state transition, including provider-controlled pause/resume calls.
- Tag 2: run completion callbacks, decrement the signed-view halfword with
  16-bit storage, and free both current buffer pointers only at the original
  stop/count boundary. Clear the first pointer and return 0 after cleanup.
- Tag 4: drain func_151DCFD8(1), then enter the original permanent self-loop.
  Other returning paths return 1; do not turn the shutdown sink into a return.

The separately supplied source is nested at
Another Source/CBFD-Recompiled/conker/conker/src/game_45B80.c. Its target is
still GLOBAL_ASM, not a matching C donor. Recover from the complete local
retail routine; no donor C credit or host-port transplant is claimed.

## Local Interfaces

Retail consumes V0 from func_15019BB8 and func_15019E60, whose old C
definitions incorrectly said void. Return their existing final helper
results as 32-bit display-list addresses. Fresh interface-only and complete
owner compiles prove **all 15 neighboring raw bodies and relative bindings
unchanged**. These ABI corrections do not add matching credit.

Use an SDK pointer declaration for D_800BE9D0 in this owner only. Rename
the legacy integer declaration while including variables.h, then declare
the real label as Gfx *. The unused legacy declaration exports no symbol;
the complete linked symbol-name set remains fixed. Add an explicit cast
to the existing cursor initialization, with identical emitted instructions.
Do not change shared headers or reinterpret integer cursor arithmetic in
other owners.

Four existing Warning 712 sites remain in func_15018F08, func_15019BB8
(two sites), and func_15019E60. Validate warning kind, exact statement,
caret/column, real source line and containing function against a fresh
predecessor compile. The recovered return adds seven columns at the final
site, which is explicitly checked. The target adds no diagnostics.

## Source And Guards

| Source form | Words | Frame | Raw differences |
| --- | ---: | ---: | ---: |
| Initial pointer-view draft | 449 | 0x78 | 370 |
| Typed owner cursor | 407 | 0x70 | 235 |
| Correct SDK light pair | 407 | 0x70 | 234 |
| Explicit overflow boolean | 411 | 0x70 | 149 |
| Scoped snapshot and inline boolean, selected | 411 | 0x68 | 138 |
| Integer cursor control | 420 | 0x68 | 310 |
| Volatile cursor control | 416 | 0x68 | 301 |
| Volatile/no-boolean control | 412 | 0x68 | 216 |

Revalidate all nine reproducible base source screens against their physical
sources, objects, bindings and linked words. Equal length/frame is not a
match: the volatile 412-word control is rejected. The IDO assembly processor
rejects -O1/-g3 as an unsupported combination; record that profile rejection
rather than diagnosing it as a configuration failure. An interface-only
three-word leaf stub has frame 0, not the negated bits of its JR opcode.

The selected source emits **411 words**, not a direct match. Derive **55**
expected-word/binding guards without copying the retail body:

| Transformation | Guarded source words |
| --- | ---: |
| Closed V0/A0 temporary swap in two graphics-only ranges | 36 |
| Closed V0/V1 state-temporary swap | 9 |
| Retarget branches crossing the one inserted delay word | 8 |
| Exchange independent cursor store/call and restore its delay NOP | 2 |

The graphics temporaries are defined before use, dead at their ABI
boundaries, and never span an internal call. Preserve all other fields and
immediates. Keep the commutative equality operand order and **architectural
V0 = 1 in the likely delay slot** distinct from temporary roles. No branch
enters the exchanged store/call pair. Move that call's R_MIPS_26 binding
with it and insert exactly one NOP; there is no instruction omission,
frame rewrite, save-slot change or compiler-profile change.

The first schedule-only guard pass leaves nine state-role words. A broad
state swap then incorrectly changes the likely-delay return word; the
complete-word gate rejects it. Exclude that architectural return from the
temporary range and require its exact original word. Final classification
is checked independently and all 412 padded words match.

```text
Raw target SHA-256
891ed2b97a7d62cd4862c65ce530b933b33f3ebd8858baafd7df5dc0e5f3b178
Normalized retail slot SHA-256
5c3fb4784448084a751c6175b07270540a55247037a4e7ca820a708e35f276b9
```

## Qualification

Seven pre-install tests pass in **193.035s**; the additional guard-class/
branch-entry assertion passes in **3.154s**. All **ten final tests pass in
217.608s**. After the final native backing correction and concise byte-equality
failure-message changes, the four affected tests pass serially in
**72.725s**; unchanged semantic/core checks retain their full
post-install receipt:

- **1,624** three-way message/pass cases plus all **256** disabled-byte
  encodings, two stack phases and **24** fired mutation sites. Test raw C's
  public memory/callback protocol against the independent reference; compare
  original and guarded complete modeled states. Do not claim raw physical
  scratch-register identity.
- Dynamically visit **411** root words. The halt-loop delay NOP is not
  executed past the declared stop gate, but is included in the complete
  412-word static comparison. Shutdown drain results include unsigned
  nonzero values before zero, without hanging the test.
- **654** memory-access fault prefixes across seven representative paths.
  Use the actual eight-word first-loop increment cut to witness signed s16
  wrap at maxima 32767, 32768 and INT_MAX without clamping production or
  running tens of thousands of opaque callbacks.
- **32** connected cases execute the actual 185-word coordinator, 40-word
  matrix preparation, freshly qualified 46-word SDK conversion and original
  78-word product. Other callbacks and scheduler delivery remain explicit
  contracts, not recovered helper implementations or hardware scheduling.
- Separate-unit native32 O2/O0 with UBSan, **293 cases each**, using actual
  selected C, Python-generated expected packets/states and complete graphics
  buffers/canaries. Bind valid fixture storage for the page-pointer table
  and both buffers in one Gfx allocation at the original 0x8000 spacing.
  Use harness-only -mstackrealign and -fno-strict-aliasing. The permanent
  shutdown sink is guest-qualified, not a terminating native case.
- Seven effective compiled controls: cached stop/count, wrong rollback,
  wrong light destination, wrong halfword argument, return 0 and reversed
  completion-counter step. Their explicit failures are 21/22/23/25/26,
  never compiler failures, signals or unexplained timeouts.
- Reject all **411** raw-word and **125** binding corruptions, unexpected
  pools, every new guard's expected/structural fields, slot/metadata and all
  **104** frozen/live input corruptions. Check both fixture stages and
  independent HI16/LO16 carry/J26 rebases of the guarded target.

The native fixture initially used separate buffer rows, which did not
establish a defined cross-buffer C pointer difference or preserve the exact
0x8000 spacing. Final qualification uses one Gfx allocation covering both
buffers, their canaries and the intervening gap, checking the entire
allocation. This is a harness correction, not production.

The first broad run passed behavioral comparisons but missed five audio
branch words because fixture flags and provider results were correlated.
Decouple the requested/current flags and provider outcomes; rerun the full
suite and add independent transition cases to native qualification too.

An initial diagnostic command completed its 36-call semantic check, then
spent excessive time rebuilding public dictionaries inside a per-byte
print comprehension. Confirm its exact owned live PID, interrupt that
diagnostic, and cache the dictionaries for later comparisons. This was
not a stalled game, compiler failure or abandoned producer.

These are bounded ABI, guest instruction and native fixture results, not
portable C fault/alias guarantees, hardware FCSR, completed render-provider
semantics or full gameplay. Prior unchanged broad suites are not called
freshly rerun.

## Complete First Prediction

Freeze the link script and original owner object; reproduce the entire
predecessor. The first slot/size-only prediction rejects **111** extra bytes.
Canonical symbol meanings and names are identical. Explicitly account for
only these three adjacent symbol/string permutations:

```text
D_800D9B90, D_800D9F60, D_800D1890, D_80088B60  -> order 1,2,3,0
osPiGetCmdQueue, D_800AA98C, D_80089970          -> order 2,0,1
D_800BEB9C, func_1501A680                      -> order 1,0
```

Pin every original record, semantic field and string location; preserve
canonical definitions and require exactly 111 serialization changes.
No metadata section is excluded. The complete first accepted prediction
changes **1,301 ELF bytes**: 1,188 inside the target slot, two size bytes
(12 -> 1,648), and 111 metadata bytes.

```text
ELF    65e765cc9fdd7ae385522f739f4e4c8acc4d15b9a894ed68e0a968253eccf48a
Owner  759db490285d4b5ea0eaa9ed68fadcfe20401b9ab6b7e38b932deefd077fe8ed
Guards afb6b1c22543a1d74a309185ca4fe2978614bb43b1e288a4f7e844b4912a14ca
```

The normal shared-manifest rebuild completes and exactly matches the
entire 3,257,636-byte predicted ELF. Existing warnings and the duplicate
generated_12D630 recipe warning remain; this is not a warning-free build.
The existing **2,217,535 guard bytes**, including mixed line endings, are
preserved as an exact prefix, with only 55 derived rows appended. No line-
ending cleanup, Makefile, shared header or progress CSV change is needed.
All **101** other captured inputs and protected **189,088 bytes / 720
owners** stay fixed. The successor adapter accepts only the three hashes
above and validates saved before/after fixtures; unknown files are rejected.

## Verified Checkpoint

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,600 / 5,501 (65.44%) | 0 | 1,901 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,927 / 4,828 (60.63%) | 0 | 1,901 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes stay fixed: the old stub already counted as C.
Root README updates only its aggregate match rows; detail stays here.
Check off the old upstream item, keeping remaining render providers open.

Tools commit **5f98c97d05050af3cd1f0488874c1d924bc945e5** banks six task files before the consumer
pin. Windows AST passes for all 12 files in both copies, and all six mirror
copies are byte-identical. Eleven shared padder tests pass in each checkout
(0.056s consumer, 0.049s mirror), and make tools-check passes. Preserve old
mirror HEAD **ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **847** initial
dirty-file hashes and **853** final dirty paths, without committing/resetting
that independent checkout.

## Resume Boundary

Prioritize **func_150195A0**, 215 original words / 860 bytes, still a 12-byte
stub and directly called by the recovered driver. func_150198FC,
func_15019CC8 and func_15019F20 are also unfinished; do not describe this
checkpoint as a complete installed frame/gameplay pipeline. The adjacent
func_15094AB8, rectangle's 18-word fit and wider Game/additional-source work
remain active.

Zero Claude calls: local compiler/retail/ABI evidence settles this match.
No push, account/auth retry, host-port edit/build/launch or frozen Release
action. The broad Game matching goal remains active.
