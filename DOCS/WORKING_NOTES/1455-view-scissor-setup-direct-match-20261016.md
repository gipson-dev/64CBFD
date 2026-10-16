# View Scissor Setup Direct Match

Date: 2026-10-16. Consumer predecessor **255ae03a**, tools predecessor
**a83f3a4**. Continue the adjacent recovery queued in
[Note 1454](1454-two-row-display-list-setup-guarded-match-20261016.md).

## Direct C Recovery

func_1501A490 is restored in conker/src/game_476D0.c. All **124 words / 496
bytes**, VA **0x1501A490..0x1501A680**, ROM **0x47940..0x47B30**, emit directly
from semantic C with the existing **O2/g3 profile**, original **0x48 frame**,
S0 cursor lifetime, saved homes and four pointed float locals. **No new guards,
padding, private pools or compiler-profile change.**

```c
s32 func_1501A490(Gfx *commands, s16 view, s32 unused2, s32 unused3,
                 s32 bottomLimit, s32 mode);
```

Keep the six-word interface and cursor-address result. Owner-local hiding of
the old functions.h word-address declaration permits a correctly typed Gfx
cursor without changing legacy callers or shared headers. The existing
0x180-byte ViewProjection476D0 now names the four proven float fields:
top **+0x24**, bottom **+0x28**, left **+0x2C**, right **+0x30**. Preserve its
size, other offsets and data ownership; native checks verify these offsets.

Behavior recovered from the full retail body:

- Emit pipe sync first, then exactly one scissor command, returning the cursor
  advanced by **16 bytes**. Both SDK macros are the existing real definitions.
- Sign-extend the full **s16** view, not u8. View **0xFF** uses upper-left
  `(2, 0)` and full-surface bounds. Subtract two from the **width word before
  converting to float**, with defined unsigned wrapping and signed-word
  interpretation. This differs from subtracting after float conversion.
- Otherwise load the selected 0x180-stride record's edges in retail order.
  Zero bottomLimit uses the record value; nonzero uses the ordered float
  comparison/minimum path. Preserve equality, negative-zero and NaN behavior.
- Call the existing func_1501AF44 rectangle clamp through four actual local
  pointers, then pack float coordinates times four into 12-bit fields and
  the low two mode bits. Preserve the unused third/fourth argument homes.
- Do not cache dimensions or record values across earlier display-list writes:
  output can alias framebuffer globals and record fields.

The alternate-source game_476D0.c still has GLOBAL_ASM for this function.
No external C body is claimed imported or byte-matching. Its exact source
fingerprint is retained as reference provenance, not as implementation proof.

## Source Shape Evidence

The word-address parameter/local-cursor form emits 122 words and spills the
cursor, despite a superficially fitting frame. A typed cursor parameter
recovers all 124 words and the original S0 lifetime, leaving 23 differences.
Function-scope record temporaries shift the address-taken float homes.

Moving the four float values into their actual normal-view branch recovers
the retail scheduling but initially leaves 14 home differences. Inline record
accesses through the existing typed-array macro then recover every home and
instruction directly. No unused padding variables or frame/home guards are
introduced. A named temporary's eight-difference score is rejected because
its **0x50 frame** is wrong; O2-without-g3 and O1 controls do not improve the
retail shape. Source/profile screens alone are not functional qualification.

All ten other normal-profile owner functions retain their raw words/bindings.
The previous two-row initializer remains selected from its existing no-unroll
object, whose fingerprint is revalidated. All compiler diagnostics are empty.
Also remove game_476D0 from RETAIL_PAD_PLAIN_O_FILES, retaining its explicit
target-only rule: its recipe-override advisory is gone. The unrelated existing
generated_12D630 warning is not changed.

## Fresh Focused Qualification

All **seven focused pre-install tests pass in 22.983s**:

```sh
python3 -m unittest tools.tests.test_game_view_scissor_setup -v
```

- **2,996 completed three-way guest cases**, plus **928 invalid-conversion
  prefixes**, compare retail, direct raw C and final padded instructions at
  two stack phases. Compare complete public/private memory, GPRs, FPRs,
  ordered accesses, real clamp arguments and cursor result. Include full-word
  view encodings, signed ranges, framebuffer/record aliases and float edges.
- Connect the actual **87-word func_1501AF44**, also byte-exact. Dynamically
  visit all **124 root words and 83 reachable helper words**. Four duplicate
  mov.s words at **1501AFA0 / 1501AFF4 / 1501B044 / 1501B090** are statically
  unreachable: validate their exact bc1fl/delay/unconditional-branch patterns
  and the absence of incoming direct branches. All 87 helper words still
  receive literal byte comparison; do not claim the four dead words executed.
- Invalid float-to-word cases stop at the **first actual trunc.w.s**, before
  its result. Compare matching instruction/private-state prefixes, not an
  invented cast result or hardware FCSR behavior. Native C never executes an
  invalid float cast; zero/NaN/sign behavior is not hidden by broad masking.
- **1,252 native32 cases each at O2 and O0**, with UBSan, real SDK macros and
  the actual recovered clamp in separate C units. Verify the six-word ABI,
  field offsets, return cursor and all **864 public words/canaries**. Packed
  GPU coordinates are not translated as CPU pointers. No -fwrapv requirement.
- Seven compiled controls fail for measured differences: byte-view truncation,
  wrong record, reversed minimum, wrong border, missing cursor advance, wrong
  quantization and swapped clamp arguments. Six exit **21**, missing advance
  exits **22**. No compile failure, signal or sanitizer trap counts as success.
- Reject all **124** raw-word corruptions, all **seven** bindings plus an extra
  binding, a private pool and stale source/Makefile installation. Three
  original GNU links and three independently emitted C rebase links compare
  all 124 words, including HI/LO carries and the relocated real helper call.
- Independently assemble/link complete original callers **func_15019CC8 (102
  words)** and **func_1510FEA0 (267 words)** against ROM. **48 actual cut cases**
  check sign extension, fifth/sixth stack arguments, the delay store, preserved
  S0 and real commands written through the consumed return cursor.
- **402 three-way connected memory-fault prefixes** include executed accesses
  in both the root and actual clamp. Hardware exceptions, full original-caller
  execution, renderer output and gameplay acceptance are not claimed.

The initial coverage assertion exposed the helper's four dead words; the
final gate proves their control-flow pattern instead of subtracting arbitrary
uncovered instructions. No production fix was needed for this fixture issue.

## Whole Image Gate

The old typed zero-return stub is **28 bytes**, including four argument-home
stores, not the generic 12-byte stub. The independent pre-install relink
reproduces the frozen predecessor, then changes only **374 target code bytes
and two symbol-size bytes**, extent **28 -> 496**: **376 ELF bytes**, zero
metadata permutations/exclusions. The prediction is reproduced serially
before installation. Predicted full ELF SHA-256:
**e55313bd3b69da1c98f17c45778811d89858dd4a72de76472341e140607a164a**.

```sh
python3 -m tools.experiments.game_view_scissor_setup --prelink
make -C conker -j4 build/conker.us.elf progress.csv
python3 -m unittest tools.tests.test_game_view_scissor_setup \
    tools.tests.test_game_view_scissor_installed -v
make -C conker match-progress NON_MATCHING=1
```

Installed source and Makefile equal their first-prediction hashes, and all
guard CSV bytes remain unchanged. The normal build exits zero and reproduces
the **entire first predicted ELF**, all 3,257,636 bytes. All **10 final tests
pass in 45.415s**. Installed tests protect all **120** live inputs, the **117**
unchanged inputs, all guard bytes and **189,088 protected bytes / 720 data
owners**. Only the exact three-input successor is accepted; source, image,
caller, helper, dead-helper-word, symbol and before/after fixture corruptions
are rejected. No metadata or section exclusion.

Fresh official totals: Game **2,933/4,828 (60.75%)**, overall
**3,606/5,501 (65.55%)**, still different **1,895**, zero address drift. Init
remains 492/492 and Debugger 181/181 byte-exact among C functions. Conversion
stays 5,501/6,044 functions and 86.04% bytes overall; the old stub already
counted as C. Root README changes only the Game/Total matching rows.

## Bank And Preservation

Tools **e72f87b6f5941ba9c7ac2b0725e723944cd462b7** banks the six new files
before the consumer pin. All six pairs are byte-identical in the active tools
checkout and older mirror; Windows AST passes for all 12 copies. Eleven shared
padder tests pass in each checkout (0.031s + 0.023s active; 0.031s + 0.019s
mirror), and make tools-check passes. Preserve mirror HEAD
**ddbdd16b53ce60b054fb6e11bf0649a41f48375a**, all **899** initial dirty-file
hashes and **905** final dirty paths. Do not commit/reset that mirror.
Zero Claude calls, no push, host-port change or frozen Release action.

## Next Work

Continue adjacent **func_1501A764**, still a zero-return stub: **87 words /
348 bytes / frame 0x38**, VA **0x1501A764..0x1501A8C0**, ROM
**0x47C14..0x47D70**. It transforms a point, computes a reciprocal and writes
three projected outputs, reloading the live view base between output stores
and the page byte before the signed depth-halfword reads.

Audit the real func_150A7A00 tail-entry ABI rather than copying the old draft's
ordinary C prototype: the caller supplies matrix A0, mirrored F12/F14 and
A1/A2 coordinate words, A3, and four pointed stack outputs. Reuse the existing
triangle-transform tail-contract tests. Qualify seven-word input/output ABI,
signed view, page/table/output aliases, ordered arithmetic and zero/nonfinite
reciprocal behavior before installation. Keep timing's **141 differences**,
remaining view providers and the wider Game/additional-source queue separate.

Follow-up completed in [Note 1456](1456-view-point-projection-direct-match-20261016.md):
func_1501A764 matches all 87 words directly from C after actual transform-tail,
live alias and consumed-output qualification. Continue the 373-word
func_1501A8C0 initializer; timing and the wider queue remain open.
