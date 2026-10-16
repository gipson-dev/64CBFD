# View Render Provider Guarded Match

Date: 2026-10-16. Consumer predecessor **ee7d019f**, tools predecessor
**5f98c97**. Previous goal turn: **progress**, restoring the frame driver.
This checkpoint continues, but does not complete, the wider Game goal.

## Recovered Routine

```text
func_150195A0  VA 0x150195A0..0x150198FC  ROM 0x46A50..0x46DAC
215 retail words / 860 bytes / frame 0x30
```

Replace the false zero-return C placeholder in game_45B80.c. Retain the
address-based function name and add a semantic comment and typed Gfx * / s16
interface; existing references and symbol names remain compatible.

- Snapshot the selected 0x9A0-byte state record before the gates. Preserve
  its SP+0x2C lifetime and the original saved S0/S1/RA registers.
- Return the unchanged cursor for the global disabled byte, signed-halfword
  stop flag, per-view callback rejection or unsigned-halfword exclusion mask.
- For a positive live signed view maximum, run the two preparation helpers,
  select the view, emit the SDK viewport command and reset the render state.
  Read the current viewport base/page after the selection callback.
- Run the mode-sensitive scene passes, mode-6 pair, intermediate setup and
  SDK model-view matrix load. Read the live mode byte after the first pass.
- Read bit 0 at the previously selected state's +0x5F0 only after those
  callbacks. Execute 18E88/18F08 in the selected order with the intervening
  mode-zero pass. A changed global state pointer must not select a new record.
- Complete the two 15188D00 passes, mode-2 setup and mode-2 pair; return the
  final provider's cursor rather than the incoming or penultimate pointer.

The separately supplied source at
Another Source/CBFD-Recompiled/conker/conker/src/game_45B80.c still uses
GLOBAL_ASM for this target. This is a local retail reconstruction, not a
matching C donor transplant or host renderer repair.

## Interface Recovery

The caller already passes a cursor and signed-halfword view. Give its local
prototype the actual Gfx * first argument and remove the obsolete integer
argument cast. The freshly compiled 412-word caller, its existing guards,
and all other neighboring raw words/bindings remain unchanged.

func_15018E88 was declared void although retail callers consume V0. Return
its existing final func_15174AA4 result as s32. This corrects its source
contract without changing its 32 emitted words. The adjacent 30-word
func_15018F08 already returns its mutable pointer-out home. Execute both
actual helper bodies in 128 combined cases to check cursor returns, halfword
arguments, the disabled byte, private pointer-out lifetime and two stack
phases. SDK/helper implementations below those routines remain contracts.

No shared header, Makefile, compiler profile or conversion-row change.
Four pre-existing Warning 712 sites remain in the owner; compare exact
statement, column, physical source line and containing function against a
fresh predecessor compile. The target introduces no new warning.

## Source And Guards

The initial integer-address-plus-local-pointer form emits 219 words; reject
its extra argument home and mask operation. Passing the SDK pointer directly
recovers **215 words / frame 0x30**, with only five viewport temporary words
different. Unsigned view/base spellings emit the same object. The nested-base
source form worsens the fit to 26 words and is not installed.

Derive five expected-word guards from the frozen compiler object, not a
retail body copy. Exchange T8/T9 in the viewport base load and scaled-index
chain at offsets **0xE8, 0xF4, 0xF8, 0xFC and 0x100**. Keep both base-load
HI16/LO16 bindings. The unchanged commutative ADDU at +0x108 joins the two
values; neither temporary survives into a later use or ABI boundary.
No insertion, omission, branch retarget, save/home or frame rewrite.

```text
Raw target SHA-256
d3279403a00335487cb1c3451eca67956dcbb3028de51ce00f73ae93d7169422
Guarded retail slot SHA-256
fd2f7d19ffcc1cb0fd851d02f4c49595af84bb6a830108f8298ddbe0b6ae192a
```

## Focused Qualification

The pre-install six-test rerun passes in **23.971s** after correcting two fixture
errors: the viewport sum is +0x108, not +0x104, and a signed stop halfword
must be serialized as raw u16 bits in the native snapshot. The separate
actual-neighbor ABI test passes in **15.705s**. These are fixture fixes,
not production changes.

- **747** three-way retail/raw-C/guarded cases: all gates, both pass orders,
  negative/zero/positive view maxima including INT_MIN/INT_MAX, dirty high
  argument halves, unsigned page bytes, two stack phases and six fired live
  mutation sites. Visit all **215** root instructions dynamically.
- **119** fired memory-access fault prefixes over six representative paths.
  Compare retail and guarded complete modeled states. This qualifies emitted
  guest instruction order, not portable C fault semantics.
- Native32 separate translation units, O2 and O0 with UBSan, **400 cases each**,
  real selected C, full cursor-buffer comparisons and struct canaries. Active
  C cases use four allocated views; do not claim portable invalid-index or
  out-of-range-shift behavior from the guest's masked shift instruction.
- Seven compiled native controls fail observably: wrong flag/order, viewport
  stride, live instead of saved state pointer, cached mode, broad mode gate,
  and dropped final return. Exits are 21/26/23, not compile failures/signals.
- Reject every one of **215** object-word and **42** binding corruptions,
  an extra binding and unexpected pools. Preserve all **15** raw neighboring
  bodies and bindings, including the corrected return interface and caller.
- Three independent original-assembly and actually padded-source links check
  all 215 words across HI16/LO16 carry boundaries and J26 address rebases.

Unchanged broad neighbor suites are not claimed as fresh runs. These are
bounded ABI/guest/native contracts, not completed rendering or gameplay.

## First Whole-Image Prediction

Before installation, freeze the link script and original owner object and
reproduce the entire predecessor ELF. The independent prediction changes
only **678 code bytes** inside the existing target slot and **two symbol-size
bytes** (12 -> 860), for **680 changed ELF bytes**. No metadata reordering,
serialization adjustment or section exclusion is required.

```text
ELF    9ae138139ba63fab29b532ad2aa3c4303447629661226f9e7b375ba4b5018ef4
Owner  b43d27b1ad8040f7d91c92153377b687dac0884cbb3b0975d6d14390b5fcb248
Guards 0ecf98bd9a0098f3bc8b40ecdbf069b7f801f26b0dc326b1c5f5d098bbac23f3
```

The existing **2,225,548 guard bytes**, including mixed line endings, are an
exact prefix with five rows appended. Do not normalize unrelated history
or change Git's line-ending configuration. The successor adapter accepts
only these three new hashes and validates both before/after fixtures.

The normal shared-manifest rebuild exits 0 and equals the entire first
3,257,636-byte prediction. Existing warnings and the duplicate generated_12D630
recipe warning remain; this is not a warning-free build. All **ten final tests
pass in 66.748s**, including the installed whole-image audit, all **105** live
input corruption controls, targeted code/caller/helper/metadata corruptions
and exact three-input successor/before/after fixture controls. Preserve **102**
other inputs, every other function's body/address/extent and protected
**189,088 bytes / 720 owners**. No metadata section or symbol is excluded.

## Verified Checkpoint

| Section | Converted | Byte-exact | Drift | Still different |
| --- | ---: | ---: | ---: | ---: |
| Total | 5,501 / 6,044 (91.02%) | 3,601 / 5,501 (65.46%) | 0 | 1,900 |
| Init | 492 / 539 (91.28%) | 492 / 492 (100.00%) | 0 | 0 |
| Game | 4,828 / 5,323 (90.70%) | 2,928 / 4,828 (60.65%) | 0 | 1,900 |
| Debugger | 181 / 182 (99.45%) | 181 / 181 (100.00%) | 0 | 0 |

Conversion counts/bytes remain fixed because the former C stub already
counted as converted. The root README changes only its two aggregate match
rows. Mark the old provider item done and keep the remaining queue explicit.

Tools commit **dc4765f083ea0965c20f814d38c1326c9d3e026c** banks six focused
files before the consumer pin. Windows AST checks pass for all 12 files in
both copies; all six mirror copies are byte-identical. Eleven shared padder
tests pass in each checkout (0.070s consumer, 0.055s mirror), and make
tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **853** original dirty-file
hashes and **859** final dirty paths, without committing/resetting that
independent checkout. Prior unchanged broad suites are reused, not rerun.

## Resume Boundary

Next **func_150198FC**, 175 original words / 700 bytes / frame 0x28, ROM
0x46DAC..0x47068, still a 12-byte C stub directly called by the frame driver.
func_15019CC8 (102 words) and func_15019F20 (192 words), the adjacent
func_15094AB8, rectangle's 18-word fit and wider Game/additional-source
queue remain open. Do not describe the frame/render pipeline as complete.

Zero Claude calls. No push, account/auth retry, host-port edit/build/launch
or frozen Release action. Preserve the independent older tools mirror.
