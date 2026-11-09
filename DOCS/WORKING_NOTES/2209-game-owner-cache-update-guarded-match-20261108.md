# Owner Cache Update Guarded Match - 2026-11-08

`func_15188E48` replaces its false zero-return placeholder with the complete
matrix-history shift and last-slot owner capture. Semantic C emits all
**79 words / 316 bytes**, retail's **0x30-byte frame**, and unchanged saved
register roles. **28 checked word guards** normalize caller temporaries,
split a coalesced source argument, and share the destination calculation
at the copy call's delay slot. The fitted routine is byte-exact.

Production: Total **4,278 / 5,513 (77.60%)**, Game **3,605 / 4,840 (74.48%)**,
Init **492 / 492**, Debugger **181 / 181**, zero address drift. **1,235**
converted functions remain different. **133** more exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion rows remain unchanged.

## Recovered behavior and ABI

Owner `conker/src/game/generated_1B5CC0.c`, original `conker/asm/1B5CC0.s`.
VA **15188E48..15188F84**, ROM **1B62F8..1B6434**. Public interface:

```c
void func_15188E48(DescriptorDraw151897A4 *record);
```

Reuse the existing 20-byte descriptor view: kind/stride byte +1, filled
count byte +2, matrix buffer pointer +8, and owner pointer +0x10. No shared
type, neighbor declaration, allocation size or compiler profile changes.

Capture kind before calling `func_1502DB20(record->descriptor[4])`. Read
the live unsigned page byte `D_800BE9C0` after that call. With matrix count
`n` and captured kind `k`, compute `span=n*k`, current page `page*span`,
and other page `(page XOR 1)*span`. Preserve the complete byte domain;
XOR 1 cannot be replaced with one minus page for arbitrary input bytes.
The count helper reads an unsigned-halfword table and subtracts four for
fourteen owner types. Its canonical count range is -4..65535; `n*k` fits
signed 32 bits, while subsequent page arithmetic preserves low 32-bit results.
The copy byte length explicitly shifts unsigned 32 bits to avoid negative-shift UB.

For indices **1 through captured kind inclusive**, earlier iterations copy
history from `liveBuffer + (index*n + otherPage)*64` into
`liveBuffer + ((index-1)*n + currentPage)*64`. The **last** iteration reloads
the live owner pointer, then its matrix source pointer at +0x1D4. A null
final source resets the filled byte to zero and returns, retaining any
earlier history copies. A zero matrix count retains the helper/copy calls
with zero byte length; a null final source still follows its reset path.

The private initial handoff had misread the branch as selecting the owner
source on the first iteration. Direct examination of the literal BNE at
15188EC4 corrected this before qualification or installation: the owner
source is selected when **index equals captured kind**, on the last copy.
The first-iteration interpretation was never credited or installed.

The loop bound and computed page offsets stay captured across copies;
the owner and buffer pointer reloads remain live. Afterwards, including
zero-kind entry, reload filled then live kind: increment filled modulo256
when unequal, otherwise preserve it. This is an equality gate, not a clamp.
Original bcopy is overlap-safe; source/destination and call order matter.

## Closed code-generation certificate

Raw source and complete owner retain frame 48, RA at SP+0x2C, S0..S5 at
SP+0x14..0x28, all helper call sites, field access order and every neighbor.
The compiler coalesces the final source into A0 and duplicates destination
ADDU in the two branches. The checked normalization instead splits source
A1 into A0 at word 40 and shares those two equivalent ADDUs (raw 46/raw 58)
at the common call-delay word 60. It verifies that both renamed ADDUs are
identical before sharing them. One independent buffer load moves raw40 to
fitted42; the else-path shift moves 57 to 58 and the NOP 60 to 57. Page,
previous-index and intermediate caller-temporary assignments are closed
renames. There are no changes to frame, saved registers, helper bindings,
memory access order, arithmetic results or total emitted length.

Changed word indices: **14,15,17,18,23,34,35,39,40,42,43,44,46,50,51,52,53,
54,55,56,57,58,60,61,65,66,67,69**. The certificate pins every raw byte and
all four relocation records: the count call, paired page HI/LO and copy call. Every single-byte raw corruption, changed binding, or changed
guard expectation rejects. The 28 CSV rows append to the inherited bytes.

Raw comparisons establish memory, memory-access sequence, helper arguments,
call order and preserved register state. Caller-temporary identity is not
claimed. At a raw buffer-load fault, PC word 40 corresponds to fitted/retail
word 42; this explicit two-instruction fault-PC mapping is tested. Retail
and fitted code agree in full literal private state, including fault prefixes.
Portable C fault semantics and complete execution of the dispatcher are
not claimed.

## Qualification and bank

- **106 frozen inputs** pin source, object, compiler stages and headers,
  retail input, layout, guards, registry, caller and original helpers.
- **14 raw and padded neighbors** and pools are unchanged. Both whole-owner
  padders agree across 15 functions. The real three-command Make recipe
  reproduces the qualified owner under existing O2/g3 with **zero C diagnostics**.
- Independent prediction of the **entire ELF** permits only this function
  body and its extent changing 12 to 316 bytes: **215 changed ELF bytes,
  zero exclusions, no symbol-name reorder**. All **6,052 function addresses**,
  every other body, and **720 protected owners  / 189,088 data bytes** remain
  fixed. Progress CSV, Makefile and retail binding data remain unchanged.
- An aligned whole-ROM census finds no direct J/JAL into this function or
  its interior and one function pointer: **D_8008D580[0]**, ROM 232040.
  Paired slot 1 is func_15188F84. The original **nine-word indirect window**
  at 15188C00..15188C24 in func_15188B74 executes across **24 cases per body**,
  both callback indices, kind 0/2/3, filled 0/255 and live mutations. It passes
  the record in A0 and overwrites V0 from record+3 after return. The paired
  callback is bounded; this qualifies the one-argument void ABI, not the
  entire 99-word parent.
- **1,232 cases per body** cover all 256 kind, page, filled and owner-type
  byte values, zero/multiple matrices, live count/copy mutations, null final
  sources and counter wrap. All **79 words** are visited. **54 alias cases**
  cover overlapping forward/backward/identical copies. **115 fired fault
  prefix triples** include 9 delay cuts. **Six independent GNU links /39
  cases per body** qualify HI/LO carry and both R26 call bindings.
- **256 connected cases per body** execute the original count helper
  (25 words) and bcopy (196-word slot), with the exact 256-byte count jump
  table and both helper baselines verified against retail and the old ELF.
  All count instructions and 90 copy words are visited, including aligned
  and unaligned overlap paths. The borrowed ADD instruction model retains
  signed-overflow trapping rather than treating ADD as ADDU. This does not
  claim execution of every bcopy word or every theoretical matrix count.
- Native32 **O0/O2/O3 each pass 879 cases**, using the SDK 20-byte descriptor,
  the actual C count helper, all descriptor fields/pointers, **33,626 exact
  copy transactions**, and complete checksums of **two 65,536-byte banks**,
  with trap UBSan. Unaligned pointer cases stay in the guest checks. All
  **15 compiled incorrect implementations** fail observably in each native
  profile and in guest checks, including first-versus-last selection,
  cached live values, wrong page/index/length and clamped counters.

Target compile/link/progress and production recount pass. The existing
whole-ROM checksum mismatch still makes `make all` exit 2. The eight focused
checks run freshly in both tools environments before and after installation.
Shared smoke is fresh in both; three unchanged regressions per copy are
reused only by exact helper/test fingerprints, not reported as fresh runs.

Receipts: `conker/build/game-owner-cache-update-15188E48-match/`.
Sibling tools retain all 2,434 inherited dirty paths; host Release stays frozen.
Tools commit before the consumer pin. Scoped Graphify refresh retains old
unscanned nodes with evidence; it is not full-corpus extraction.

Next: **func_151B4EA4**, the next measured 79-word unmatched Game function
in generated_1E2180. Its source, ABI, callers and behavior still require
qualification before installation or credit. The 80% goal stays active.

Production ELF SHA-256: `b686e610b70dd8fe68d66280a8ced2641f823a18a43b332b0d9483abc73bf931`.

Guard SHA-256: `20c618695cd49515d11104e564bfa13e22edd36b5639203ee0368c9fb667e299`.
