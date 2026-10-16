# Frame Timing State Semantic Restoration

Date: 2026-10-16. Consumer predecessor **5f4395d0**, tools predecessor
**52a9ed6**. The preceding goal turn made progress by matching func_15019CC8.
Continue the full Game matching goal after this checkpoint. This routine is
restored as **semantic C, not byte-exact**; its instruction match remains open.

## Recovered Routine

```text
func_15019F20  VA 0x15019F20..0x1501A220  ROM 0x473D0..0x476D0
191 body words / 764 bytes / frame 0x18 / one trailing slot NOP
141 actual slot-word differences / zero new guards
```

Replace the 12-byte zero-return placeholder with a complete timing/state
updater, retaining the address-based name and adding a semantic comment.
Recover its void, no-argument interface. The actual direct caller is
**func_1501905C**, not func_1501878C: its full 53-word body is freshly checked
against retail and remains unchanged. Source references show no other named C
caller; the alternate source still uses GLOBAL_ASM for the target. No donor C
is adopted and no broader indirect-caller or gameplay claim is made.

- Snapshot the old signed frame-step word before examining the byte divisor.
  Zero divisor uses the signed count's half-scale float value. Divisor one
  clears the step word, phase byte and scale. Larger divisors preserve the
  signed-to-float conversion, provisional truncated store, then half scale.
- Accumulate the residual and old count using wrapping u32 arithmetic. When
  the total reaches the divisor, store the unsigned quotient and preserve
  retail's unusual **total - quotient*total** update. Do not replace it with
  ordinary remainder arithmetic. The other arm stores the total and zero steps.
- Mask the phase to its low bit, add the step word with unsigned wrapping,
  narrow to a byte, then derive the half-phase byte. Keep the running counter
  as a wrapping word but interpret its modulo-30 operation as signed.
- Compute the current reciprocal, explicitly normalizing a zero current scale
  to positive zero. Cache the history index before the float store, then
  increment that original byte and reset only when it equals ten.
- Read the warm-up counter after the history write. Before ten samples, copy
  the live scale and reciprocal. Otherwise sum ten samples in ascending
  single-precision order and multiply by the existing factor D_800968D0,
  bits **0x3DCCCCCD**. A zero mean gets a positive-zero reciprocal without
  normalizing the mean itself; a negative-zero mean must remain negative zero.
- Call func_150A019C last. Its return is unused. Callback writes to timing
  fields must survive the provider return.

Add only owner-local declarations. The factor remains in its existing
23B390.rodata.s owner, including the complete 16-byte data slice; no private
float pool, shared-header edit or compiler-profile change is introduced.

The ten-sample history is indexed by an unchecked byte in retail. Other byte
encodings can overlap adjacent labels, including the residual, index/sample
counter word, reciprocal, running counter and frame-step word. Qualification
models those mapped addresses rather than pretending every byte is below ten.
This is bounded physical-memory evidence, not a claim that corrupt index states
occur during normal gameplay or that arbitrary portable C objects may overlap.

## Source Screens

Thirty complete-owner screens cover explicit index caching, signed/unsigned
counter views, known history extent, live/local divisors, scalar lifetimes,
signed total views and divisor widths. Reproduce through:

```sh
python3 -m tools.experiments.game_frame_timing_update --screens
python3 -m tools.experiments.game_frame_timing_update --arithmetic
python3 -m tools.experiments.game_frame_timing_update --lifetimes
python3 -m tools.experiments.game_frame_timing_update --divisors
python3 -m tools.experiments.game_frame_timing_update --byte-divisors
```

Only the selected source is semantically qualified. It uses an explicit cached
u8 index, u8 divisor, unsigned phase/counter arithmetic and signed modulo view.
The native proof needs neither -fwrapv nor overflow suppression. Do not adopt
an unqualified signed-overflow spelling merely because its register allocation
looks closer. The raw object emits **191 words / frame 0x18**, followed by the
padder's one zero word. All **15** neighbors retain their raw bytes/bindings;
all four old Warning 712 sites retain their statements, carets and containing
functions, with actual source lines checked against a fresh predecessor compile.

The screen's length-adjusted difference count is 142 because it counts the
unemitted padding word as missing. The actual padded 192-word slot differs
at **141 words**; the padding matches. Do not report 142 as the final mismatch
count or confuse equal length/frame with a byte-exact match.

```text
Raw C SHA-256
63fa053a2cb82cc69b8870e51fdf741b7816b2568aac8ea9cab272649282e67a
Unguarded 768-byte slot SHA-256
566c74650ae3a07c27a98ea23f11dd0eb39a80497abed2501541c1bf8376d95a
```

## Qualification

The corrected seven-test pre-install suite passes in **34.714s**. All **ten
final tests pass in 48.712s**:

- **6,860 retail/C guest cases**, covering 3,430 fixtures in two stack phases,
  all 256 divisor/phase/index/sample byte encodings, high signed/unsigned word
  boundaries, byte-index aliases, cancellation, subnormal rounding, negative
  zero, overflowed means and infinite reciprocals. Compare all public memory,
  ordered calls and a hash over the full 1,104-byte timing region at the callback.
- Visit all **186 legally reachable body words** in each emitter. Four
  unsigned-float correction words and the divide-zero trap are unreachable
  from the observed byte divisor and guards; one slot-padding word is outside
  the body. Do not claim dynamic coverage of all 192 words. Static corruption
  controls still protect every one of the 191 emitted words and 59 bindings.
- Native32, separate actual-C units at O2/O0 with UBSan, **3,430 cases each**.
  One real 1,104-byte memory union supplies the full history-index range and
  neighboring word/float labels. Byte labels use big-endian views within native
  words, so float writes and byte aliases agree without out-of-bounds objects.
  Check every word and all canaries. Ten compiled controls reject via exits
  22/23, not signals, UB or compilation failures.
- Reject all **191** raw-word corruptions, all **59** binding corruptions,
  an extra binding and unexpected pools. Three independently linked source
  images verify every word/binding and history addend carries **4, 8, 40**.
  These are relocation checks, not original/source word identity.
- **180** actual caller/provider cases use the fresh, fully checked 53-word
  func_1501905C and its real three-word cut at 0x15019088..0x15019094. Include
  the address load and previous helper result's publication to D_800BE728 in
  the JAL delay slot, including history index 80 aliasing that word. Verify the
  no-argument/ignored-return boundary and saved state, not the whole frame loop.
- Qualify signed/unsigned division HI/LO primitives and reject altered fields
  in every named metadata group, even when the initial image hash gate is
  deliberately bypassed to exercise the structured symbol guards.

The first caller fixture incorrectly began at the JAL and omitted the required
AT address setup/publication. Its unmapped delay-store failure is corrected by
including the preceding LUI and modeled previous result. The full rerun passes;
this is not a production defect.

Public access ordering still differs in **1,614** of the 6,860 guest cases.
In particular, the zero-reciprocal block reloads the current scale before its
reciprocal store, where retail stores first. Complete fault-prefix/private
register equivalence is not claimed. The floating model is bounded nearest
single precision, not hardware FCSR/exception timing or NaN-payload acceptance.
Prior unchanged broad suites are reused, not represented as fresh runs.

## Complete Image

Freeze the original owner object/link script and reproduce the entire
predecessor ELF before installation. The first structural prediction changes
only this 768-byte slot and the symbol extent **12 -> 764**. The independent
link exposes **173** additional serialized metadata bytes: six named symbol/
string bucket permutations, with all canonical symbol meanings unchanged:

- D_800BE9BC, D_800BE5EC, D_800A2FD8.
- D_800BE619, .L15098F6C_game_data, func_151279A0.
- D_800BE9B0 and D_800BE5E0.
- D_800DBE30 and D_80089730.
- osPiGetCmdQueue, D_800AA98C, D_800895B0.
- D_800C3D60 and D_8003C900.

The incomplete slot/extent-only prediction is rejected. Reuse the existing
structured serializer with exact names, fields, adjacency, string ranges and
permutations; preserve the structural image and its locked SHA-256. No generic
symbol-table, string-table or section exclusion is permitted. The complete
first prediction changes **755 bytes**: **580 code + two extent + 173 metadata**.

```text
Structural fa48acc7665ba6d768f591f5c1a8a4823a0351665cda2517f8c6cc9fd4f65657
ELF        44fa0f9f11ce36d6aad05a9214d8b025c687e54bb6dbf9e857386e2f47f3ebd3
Owner      d4884ed725cb96ba56e9a19ab0cb060682e527963579983a45b299a3e9383416
Guards     e09a6696c524fad38b6c2cbefdb4c8249e012efdd59b6a14cc51ac5958939239
```

The normal build exits 0; all **3,257,636 ELF bytes** and the installed source
equal that first prediction. Preserve all **107** other captured inputs,
unchanged guard bytes and protected **189,088 bytes / 720 owners**. Controls
reject alterations to all **109** live inputs and selected code/caller/factor/
metadata bytes; the exact two-input successor and both fixture stages pass.
Existing warnings remain in normal-build.log; this is not a warning-free build.

## Checkpoint And Resume

Fresh official numbers remain Game **2,930/4,828 (60.69%)**, total
**3,603/5,501 (65.50%)**, different **1,898**, zero drift. Init is 492/492 and
Debugger 181/181 exact among converted functions. Conversion counts/bytes also
remain fixed because the old stub already counted as C. Root README aggregates
are correct and untouched; keep function narratives in the working docs.

Tools commit **511d98a** banks six files before the consumer pin. Windows AST
passes for all 12 files across both copies, and all six new mirror files are
byte-identical. Eleven shared padder tests pass in each checkout (0.055s
consumer, 0.048s mirror), and make tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **877** initial dirty-file
hashes and **883** final dirty paths without committing/resetting that checkout.

Next finish **func_15019F20's instruction match** using these semantic/alias
fixtures. Investigate the retained D_800BE610 pointer versus retail branch
rematerialization, the zero-reciprocal access order, and history base/addend
folding into the existing D_800BE5EC/D_800BE5F0/D_800BE610 labels. Do not rerun
the same 30 screens or treat matched frame/body length as completed matching.
Keep adjacent func_15094AB8, rectangle's 18-word fit and the wider Game/
additional-source queue open. Zero Claude calls, no push, no host-port action
and no frozen Release build/modification/launch.
