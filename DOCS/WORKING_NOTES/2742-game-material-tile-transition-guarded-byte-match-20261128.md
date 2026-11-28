# Material tile transition callback guarded byte match - 2026-11-28

`func_150D83D8` in `conker/src/game/generated_105760.c` now restores the
complete **110-word / 440-byte** callback, VA `0x150D83D8..0x150D8590`, ROM
`0x105888..0x105A40`. It has no stack frame or alignment tail. The previous
three-word zero-return placeholder supplied no matching credit. The recovered
interface is `s32 func_150D83D8(u8 *material, u8 *actor)`; no shared header changes.

Actual production: **4,721 / 5,528 (85.40%) total**, **4,048 / 4,855 (83.38%)
Game**, Init 492/492, Debugger 181/181. Zero drift, 807 still different.
Conversion rows/denominators are unchanged. The **90% goal remains active**:
**255 more matches** reach 4,976/5,528. Tools: `fba6d1b4fcbd2c231b6257f55f04b88c89aa4a8f`; previous consumer:
`c37ff676`. This adds exactly one guarded C match.

## Recovered behavior

The material's state/counter are words at +0x38/+0x3C. State zero resets the
counter to 50 and selects the low halfword of `D_80090298[27]`. Actor animation
0x18D at frame 46 or later changes state to one and selects table entry 28.
State one adds `D_800BE9E4`, clamps at 100, and enters state two. Animation
0x18E at frame 34 or later enters state three. State three subtracts four times
the tick count, then clamps nonpositive results to zero and enters state four.
Other states preserve the counter. Tick arithmetic wraps modulo 2^32 before
the signed comparisons; unsigned lvalue/arithmetic views avoid signed overflow.
Animation pointers are dereferenced only after the corresponding state/ID gate.

The counter is converted to binary32 and multiplied by the original coefficient
`D_800A0B14`: bits **0x3C23D70A**, verified against ROM 0x2455D4 and the frozen
ELF. The callback walks the material descriptor's eight-byte GBI commands to
the first opcode 0xF2. It truncates the ordered binary32 expression
`120.0f * fraction + 2.0f`, masks the low twelve bits and stores only word zero:
`0xF2002000 | (coordinate & 0xFFF)`. Word one and all other commands stay fixed.
The callback returns zero.

## Exact code and register certificate

Semantic C emits all 110 words under the existing O2/g3/mips2/o32 profile.
**94 bound words match directly; 16 expected-word guards** normalize closed
temporary GPR allocation cycles. There is no insertion, omission, private
frame change, memory-access rescheduling or floating-point algebra rewrite.
Eight HI16/LO16 bindings retain the three original external globals. Compiler
pools and all eight raw/padded neighboring functions and bindings stay fixed.
Both complete padders reproduce the frozen before object and agree on the
selected object. The existing Makefile and three-command owner recipe suffice.

An independent symbolic transfer proof checks four regions: entry (11 paths),
common update (2), sentinel-search step (2), and completion (1). These **16
inductive paths** preserve exact public read/write order, addresses, widths,
ordered FP operations/operands/numeric controls, saved registers, return and
stack. Ordinary mapped public RAM aliases are admitted. No floating algebra
or memory-commutation axiom is used. Two consistent GPR renamings pass; all 16
single-word broken allocation cycles and four semantic mutations reject.
The loop proof is inductive rather than a finite iteration screen.

Every new guard is effective: **32 removals visibly fail** and **32 stale
expected words reject**, across both padders. **16 independent GNU links**
cover four rebases with independent global addresses and signed HI16/LO16 carry
seams. The raw transfer proof is repeated at each rebase.

## Behavior, ABI and linked acceptance

- Actual SDK/native32 C: **1,732 cases each at O0/O2/O3**, separate translation
  units, strict aliasing, trapping UBSan and LTO type checking. Eight semantic
  controls exit 42. Checks include wrapping ticks, signed clamps, table low
  halfwords, frame equality/NaN gates, opcode search positions and every
  unwritten material/command byte. Other public objects remain fixed.
- Guest: **570 cases x four streams / 2,280 executions**, all **110 words**
  reached, three owner-pointer domains and both stack phases. Raw public
  access order matches retail. Both normalized streams have equal complete
  terminal states. **342 normalized memory-fault quadruples** preserve prefixes.
- Caller: original `D_800841C0[19]` at ROM 0x228CCC is the only registration;
  no direct calls are present. **488 connected executions** use the original
  17-word dispatch/result window in `func_15030468`, execute its 13 reachable
  words on the zero-return path and reach all 110 child words. Selector zero
  skips. The two pointers are material S1/actor S3. A forced nonzero return
  reaches the cleanup boundary. The complete 419-word parent is pinned, but
  its other paths/providers are **not qualified** by this focused window.
- Actual private and production Make output equals an independent frozen-
  before-C plus original-target-ASM full-image prediction: **358 changed bytes,
  zero exclusions**. All **720 data owners / 189,088 bytes**, other bodies,
  addresses, guard history and conversion rows remain fixed. Six existing
  unrelated duplicate-recipe warnings remain; there are no new diagnostics.
- Both tools copies passed five complete tests before installation and again
  after installation. Those **20 complete checks are retained with their exact
  fingerprints** after a comment-placement cleanup restored the unchanged
  neighbor. All tool code and the native target source body are identical;
  complete raw text, function extents and bindings also remain identical.
  **Two fresh focused checks**, one in each final tools copy, repeat the
  source/owner, inductive proof, actual Make and strict-image gates after the
  cleanup. Their four reports and closed import/data roots agree. The real
  dirty sibling checkout remains preserved. Shared `make tools-check` passes.
  Tools are committed before the consumer.

The behavioral C domain requires mapped/aligned objects, a reachable sentinel
within valid command storage, and a finite float result representable as s32.
Native tests exclude 228 out-of-range conversion cases, and the guest sample
excludes 30; no invalid-conversion or floating-trap gameplay claim is made.
FP exception flags are not emulated by the finite guest oracle. The separate
ordered-operation certificate supplies the stated normal-completion equivalence.
The N64 opcode is byte zero of a big-endian command; native fixtures model that
byte contract explicitly and check the numeric output word separately.

README changes are aggregate rows only. Graph refresh is scoped AST extraction
with old-ID and qualification retention, not full-corpus re-extraction. Final
hook, graph and immutable bank receipts are in
`conker/build/game-material-tile-transition-150d83d8-private/`. The host sibling
is inspected read-only for applicability; there are no host edits, builds,
launches or gameplay acceptance. Host Release remains frozen. No push or
subagent is used. N82 `func_1514EECC` remains parked separately.

Next: continue ordinary unmatched Game matching from the sealed N88 bank.
