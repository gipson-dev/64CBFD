# Two-Row Display-List Setup Guarded Match

Date: 2026-10-16. Consumer predecessor **472a12bf**, tools predecessor
**51ebd75**. Continue the adjacent recovery queued in
[Note 1453](1453-view-initialization-guarded-match-20261016.md). The separate
func_15019F20 timing match remains open at 141 slot-word differences.

## Recovered Contract

Replace func_1501A39C's zero-return stub and incorrect three-row commented
draft in conker/src/game_476D0.c with complete SDK-based C:

```c
void func_1501A39C(void);
```

Retail span **0x1501A39C..0x1501A490 / ROM 0x4784C..0x47940**: **61 words /
244 bytes**, leaf frame **0x18**, saved S0..S4 at SP+4..SP+0x14. The two
actual original caller cuts ignore the incidental V0 value; retain the
existing recovered driver's void interface rather than inventing a pointer
return from the old draft.

Read two command-buffer addresses from D_800BE9C8. For each row append:

1. Two separate segment-zero commands, both **DB060000 / 00000000**.
2. A display-list call, **DE000000 / address D_8002C930**.
3. A depth-image command, **FE000000 / live D_800BE9C4**.
4. A viewport command, **DC080008 / live D_800BE628 + row*0x10 + 0x40**.

Publish each resulting cursor to D_800BE9D8, stopping at the address of
D_800BE9E0 after **two rows**, not three. Reload the second input pointer,
depth word and view-base word in retail order; command buffers can alias
these tables/globals. Each buffer advances **40 bytes**, with no input-table
cursor writeback. The viewport address uses a wrapping unsigned word, not
the initializer's separate 0x180 allocation stride.

Use the actual gSPSegment, gSPDisplayList, gDPSetDepthImage and gSPViewport
SDK macros. Add only owner-local declarations for the existing input table
and shared list; retain existing output/depth/view storage and shared headers.
No new data pool, synthesized commands, padding or safety shortcut.

## Profile And Derived Guards

Twenty-four canonical complete-owner source/profile screens distinguish
pointer/word tables, input-update placement, signed/unsigned offsets, pointer
comparison forms and a returned-cursor hypothesis. The selected normal O2/g3
body unrolls to **126 words**, exceeding this slot. Disabling loop unrolling
gives **61 words / frame 0x18 / 38 raw differences**. Explicit returned-cursor
variants still have 62 words even without unrolling and are not installed.

Select **only func_1501A39C** from the no-unroll object using the existing
padder's --function-object support. The normal-profile object supplies all
ten neighbors, including the just-matched initializer. Do not change the
whole owner's optimization profile. Fresh complete-owner comparisons retain
all ten neighbors' raw words/bindings; all diagnostic streams are empty.

Thirty-eight relocation-aware guards derive only closed scratch-register
roles and independent scheduling from the fingerprint-locked 61-word object.
Raw-to-retail register roles:

| Raw | Retail | Role |
| --- | --- | --- |
| V0 | V1 | Input table |
| V1 | T3 | Output table |
| A0 | T2 | Viewport byte offset |
| A1 | V0 | Current command cursor |
| A2 / A3 / T0 | A0 / A1 / A2 | First three SDK packet temporaries |
| T1 | A3 | Shared list address |
| T2 / T3 | T0 / T1 | Last two SDK packet temporaries |

The routing permutation exchanges +0x1C/+0x20, then routes prologue targets
0x34/38/3C/40/44/48/4C/50 from raw 0x40/44/48/4C/38/50/34/3C respectively.
It also exchanges the independent input/cursor increments at +0xB4/+0xB8
and the offset increment/output publication at +0xCC/+0xD4. This places the
output store in the original branch delay slot. Move HI16/LO16 bindings
with their instructions. Preserve every opcode, arithmetic constant, branch
displacement, memory-access order, saved-register home and all seven epilogue
words. No instruction insertion or omission.

All **61 normalized words are literal retail**. Raw scratch registers differ
at boundaries; do not claim full raw private-register/fault-state identity.
Public/complete memory, preserved ABI state and the entire ordered memory
access sequence are independently qualified for raw C as well.

## Fresh Pre-Install Qualification

All **eight final focused pre-install tests pass in 49.201s**, run serially:

```sh
python3 -m unittest tools.tests.test_game_view_list_setup -v
```

- **688** three-way guest cases, 344 fixtures at two stack phases, compare
  retail, raw C and normalized instructions. All 61 words execute in every
  emitter. Complete memory/FPR state, preserved ABI registers and normalized
  full GPR state agree. Include overlapping/same buffers, live second-input,
  depth/view aliases and unsigned GPU-address wrapping.
- All **344** fixtures also compare the exact **38-access** load/store trace,
  including saved homes, both live row loads and both output publications.
  Complete runs are explicitly restricted to mapped word-memory stores.
- **344 native32 cases each at O2 and O0**, actual SDK macros in separate C
  units, UBSan, entry stack realignment and the existing no-strict-aliasing
  convention. Compare all **2,320 public words** and canaries across three
  arenas. No -fwrapv requirement; these are bounded native arenas, not an MMU.
- Seven native controls fail for measured output differences, all exit **21**:
  one row, wrong viewport stride, wrong segment, wrong shared-list address,
  wrong publication, cached depth and cached view base. No compile failure,
  sanitizer trap or signal counts as a successful negative control.
- Reject all **61** raw-word corruptions, **12** binding corruptions plus an
  extra binding, a private pool and **342** guard-field corruptions. The real
  padder rejects wrong expected words/bindings while using the alternate
  function object. Duplicate profile installation is also rejected.
- Three original-assembly links and three independently emitted normalized
  rebase links compare all 61 words, including moved HI/LO pairs and carry
  boundaries. Preserve the output-end label exactly eight bytes after its
  table start.
- Independently link **all 412 original func_1501878C words and all 239 original
  func_1501C880 words** against ROM. Exercise **48 actual call-cut cases**,
  including the former's post-call S0 flag clear and the latter's T1 stack
  store in the call delay slot. The current C func_1501C880 remains a stub;
  these cuts do not establish a complete linked caller/startup path.
- **456 normalized instruction-fault prefix pairs** agree with retail full
  state. Raw private-register fault equality and hardware exceptions are
  not emulated or claimed.

The native fixture initially failed to translate the alias-derived shared-list
symbol plus 0x40, which lies one-past its arena. Correct the specific 0x40/0x50
symbol-derived GPU addresses and one-past cursor translations, using integer
address arithmetic and rejecting ambiguous scalar seed values. A diagnostic
SSE store also exposed the freestanding entry's stack alignment; the final
serial run uses the established -mstackrealign option. No recovered C change
was needed for either harness issue. Imported TestCase discovery was narrowed
to the intended eight tests before the final serial receipt.

## Complete Image Gate

Before installation, reproduce the frozen predecessor with its old object,
then independently link the new normalized owner into the complete ELF.
The first prediction changes exactly **192 target code bytes and one target
symbol-size byte**, extent 12 -> 244: **193 ELF bytes**, zero metadata
permutations or exclusions. Predicted ELF SHA-256:
**3fa2606e9667487ba4196ca1cd897616c0dceea23fa7212cb5452d24315ac537**.

```sh
python3 -m tools.experiments.game_view_list_setup --prelink
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_view_list_setup \
    tools.tests.test_game_view_list_setup_installed -v
make -C conker match-progress NON_MATCHING=1
```

The production source, guard CSV and target-only Makefile rule are installed
with their exact first-prediction hashes. The normal build exits zero and
reproduces the **entire first predicted ELF**, all 3,257,636 bytes. All
**11 final focused/installed tests pass in 51.237s**, run serially. The installed
checks protect all **117** live inputs, the **113** unchanged inputs, exact
old guard prefix and all **189,088 protected bytes / 720 data owners**. Accept
only the exact four-input successor and reject source, caller, image, symbol,
binding and before/after fixture corruptions. No metadata or section exclusion.

Fresh official totals: Game **2,932/4,828 (60.73%)**, overall
**3,605/5,501 (65.53%)**, still different **1,896**, zero address drift. Init
remains 492/492 and Debugger 181/181 byte-exact among C functions. Conversion
stays 5,501/6,044 functions and 86.04% bytes overall; this stub already counted
as C. Root README changes only the Game/Total aggregate matching rows.

## Bank And Preservation

Tools **a83f3a412835b7695bfdf859f32c51d28e9f994c** banks the six new files
before the consumer pin. All six pairs are byte-identical in the active tools
checkout and older mirror; Windows AST passes for all 12 copies. Eleven shared
padder tests pass in each checkout (0.030s + 0.023s active; 0.031s + 0.020s
mirror); make tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **893** initial dirty-file
hashes and **899** final dirty paths. Do not commit/reset that mirror.
Zero Claude calls, no push, host-port change or frozen Release action.

Normal make reports the explicit game_476D0 recipe overriding the plain
static-pattern recipe, alongside the pre-existing generated_12D630 warning.
The selected recipe and complete output are qualified above. On the next
owner-build edit, exclude this owner from RETAIL_PAD_PLAIN_O_FILES to remove
the new advisory without changing its selected profile; recheck whole-image
identity rather than treating warning cleanup as a source match.

## Next Target

Continue adjacent **func_1501A490**, still a zero-return stub: **124 words /
496 bytes / frame 0x48**, VA **0x1501A490..0x1501A680**, ROM
**0x47940..0x47B30**. It emits pipe sync and a packed scissor command, returning
the advanced cursor. Preserve the six-word ABI and sign-extended s16 view;
the third/fourth words are homed but not used by the retained retail body.
View 0xFF uses the full-surface dimensions; normal views read the 0x180-stride
record and call the existing four-float func_1501AF44 clamp. The fifth word
selects the zero/default versus float minimum path; the sixth supplies the
two scissor mode bits. Audit float conversion/NaNs, live output/data aliases,
real helper behavior and consumed cursor-return sites before installation.
Keep timing's 141 differences, the remaining provider/additional-source queue
and full frame/startup/gameplay acceptance separate.

Follow-up completed in [Note 1455](1455-view-scissor-setup-direct-match-20261016.md):
func_1501A490 matches all 124 words directly from C, and the owner recipe
override advisory is removed. Continue the 87-word func_1501A764 wrapper;
the timing match and wider queue remain open.
