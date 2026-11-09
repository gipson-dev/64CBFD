# Audio State Initializer Guarded Match - 2026-11-08

`func_15016170` replaces a false zero-return placeholder with the complete
audio-state clear, counted heap allocations, pan/gain initialization and
DMA callback registration. Semantic C emits **77 words  / 308 bytes**, retail's
**0x28-byte frame**, saved S0 at+0x20 and RA at+0x24. **19 checked guards**
normalize caller temporaries, one independent schedule, integer multiply
operand order and reverse-address lowering. All **80 slot words**, including
three trailing padding NOPs, are byte-exact.

Production: Total **4,280 / 5,513 (77.63%)**, Game **3,607 / 4,840 (74.52%)**,
Init **492 / 492**, Debugger **181 / 181**, zero drift. **1,233** converted
functions remain different. **131** more exact functions reach 4,411 / 5,513
and the active 80% goal. Conversion rows remain unchanged.

## Recovered behavior and ABI

Owner `conker/src/game_43620.c`; original
`conker/asm/nonmatchings/game_43620/func_15016170.s`.
VA **15016170..150162A4** body, slot through 150162B0;
ROM **43620..43760** slot. Interface:

```c
void func_15016170(s32 heapAddress);
```

The exact 17-word Init caller `func_10012588` passes this 32-bit address,
then creates its queue and registers func_10012560. It ignores the return.
An explicit matching void prototype is added only in `init_12560.c`;
all seven caller-owner functions, pools, register metadata and the complete
padded object remain identical. One inherited Warning 712 in the following
func_15043A00 call remains unchanged after line/path normalization. No shared
header or compiler profile changes are required.

Reuse the existing 160-byte `struct186` layout. Clear all 160 bytes at
D_800E0D80. Call SDK alHeapDBAlloc three times with file/line 0, the live
incoming heap home cast to ALHeap*, count 1, and sizes **80,1088,8**. Store
results at+8,+0x74,+0x5C, including null results. Continue after failures;
there is no rollback or early return. The SDK rounds those requests to
80/1088/16 bytes, advances cur only on success, and preserves count in the
release configuration. Private heap-home reloads are tested separately from
portable native providers.

Initialize the original pan, gain, limits, flags and counters with exact
byte/halfword/word stores and repeated reads. Signed pan+0xC and auxiliary
pan+0x96 become 64; copy the latter to+0x94. Signed gain+0xE becomes 32767.
The word limit+0x88 is stored through its corresponding unsigned 32-bit view,
preserving the shared signed field layout while recovering retail's two
distinct 7FFF literal loads. Multiply signed table samples by captured gain,
keep the low 32-bit result, arithmetic shift 15 and store the low halfword.

The data assembly proves **127 samples** under D_8002BC10 followed by a
**separate terminal sample** at D_8002BD0E. The reverse endpoint is a valid
one-past pointer, not a 128-element C object. Byte offset 128 from fixed pan 64
selects left entry 64 and right entry 63, both inside the 127-sample array.
The reverse expression converts the one-past pointer to u32, subtracts the
byte index, then converts the valid result back to s16*. The source explicitly
targets the N64/native32 address model; no negative array indexing is used.
The physical 256-byte span remains exact, SHA
`5342dc7ebdcab496ba88b4002bb6d50cfd9f2ad68a6323aea5aad3b8a504ec5c`.

Register func_151F3C4C's opaque 32-bit address through func_151F3C34. Its literal
setter consumes only A0; A1/A2 are leftovers from earlier calculations. The
historical three-argument comment is not adopted. The callback is registered,
not invoked here; its existing legacy header declaration remains untouched.
The setter's D_800E0DFC word is also state offset+0x7C. The following Init
callback word D_800E0E00 is offset+0x80. Both are cleared with the state;
registration repopulates+0x7C, and the complete caller later repopulates+0x80.
Native checks model this shared storage and normalize scalar endianness.

## Closed code-generation certificate

Changed indices: **36,37,38,39,44,49,52,53,54,55,56,57,63,64,65,66,68,69,71**.
The certificate pins all 308 raw bytes and all 13 relocation records; every
single-byte, binding and guard-expectation corruption rejects. The 19 rows
append to the inherited guard bytes without editing prior history.

Caller-temporary roles are closed over their actual lifetimes. Frame, saved
S0/RA, argument homes, memory-access sequence, five calls and side effects
remain fixed. The gain SH moves raw 38 to fitted 39 across an independent LI;
fault comparisons use this explicit PC correspondence. MULTU operand order
at 54 is commutative for the complete HI/LO result. Raw comparisons establish
memory, calls, access sequence, saved state and HI/LO; caller-temporary
identity is not claimed. Fitted and retail literal private state agree.

Raw 52/53 form the complete table-end address using LUI/ADDIU, raw 55 subtracts
the byte index and raw 63 uses LH offset 0. Fitted 52 NEGUs the index, fitted 53
holds the relocated HI, fitted 55 adds that HI address and the negated index,
and fitted 63 carries the original LO displacement 254. Move HI +208->212 and
LO +212->252 while retaining the parent symbol/addend. **24 modular address
equations** and independent GNU links qualify signed LO carry and effective
address identity. No ROM-word copying, inserted words or omitted words are
used in this normalization.

## Qualification and bank

- **112 frozen inputs** include both source owners/objects, caller, SDK
  allocator and alignment header, original clear/setter, data assembly,
  compiler/headers, ROM, layout, guard history and linker bindings.
- Both Game padders agree across the single-function owner. The real
  **three-command Game recipe** and **three-command Init caller recipe**
  reproduce their qualified objects under existing O2/g3. Game diagnostics 0;
  the caller's existing one warning is preserved. All seven Init functions
  and the caller object SHA remain fixed.
- Independent prediction of the **entire ELF** allows only this Game body
  and extent 12 to 308: **233 changed bytes, zero exclusions, no metadata/name
  exchanges**. All **6,052 function addresses**, every other body and all
  **720 protected owners  / 189,088 data bytes** remain fixed. The separate
  Init pan data is likewise checked byte-for-byte. Progress CSV, Makefile,
  shared headers and binding data remain unchanged.
- **1,149 cases per body** check all 160 state bytes, every provider snapshot,
  allocation failures/return bit patterns, three live heap homes, signed
  samples, width/truncation and release allocator boundaries. All 77 body
  words execute; all 80 slot words match literally.
- **12 alias cases per body**, **99 fired fault-prefix triples** with 3 delay
  cuts, and the explicit raw 38->retail39 fault-PC map qualify the schedule
  and address rewrite. Fitted-vs-retail full private state agrees. Guest
  global aliases/private home effects are not portable native C claims.
- **24 complete original Init caller cases per body** include its trailing
  queue creation and Init callback setup. **80 connected cases per body**
  execute original allocator 35 words, bzero 40-word slot and setter 6-word
  slot. All three helpers and the 17-word caller baselines are exact. The
  allocator visits 31 words across aligned allocation and exhaustion paths;
  full coverage of unreachable/padding instructions is not claimed.
- **Six independent GNU links /30 cases per body** qualify state/callback
  HI/LO pairs, the table-end addend/carry and all five R26 calls.
- Native32 **O0/O2/O3 each pass 575 cases**, with the actual C SDK allocator,
  struct186 size 160 and ALHeap size 16 assertions, every state byte and heap
  field, shared callback storage, and trap UBSan. All **16 compiled incorrect
  implementations** fail observably in every native profile and in guest
  checks. Unmapped/private-home/artificial global alias cases stay in guest
  checks. No shared tool helper implementation changes.

Fresh target checks run in both tools environments before/after installation.
Shared smoke is fresh in both; three unchanged regressions per copy are
reused by exact helper/test fingerprints, not reported as fresh runs. Actual
production Make/recount agrees with prediction. The existing whole-ROM
checksum mismatch still makes `make all` exit 2.

Receipts: `conker/build/game-audio-state-initialize-15016170-match/`.
Tools commit before consumer. Sibling tools retain all 2,434 inherited dirty
paths; host Release stays frozen. Scoped Graphify refresh retains existing
unscanned nodes with evidence; it is not full-corpus extraction.

Next: **func_1501E400**, measured 80-word unmatched Game slot in generated_49D30.
Its source, ABI/callers and matching shape require qualification before any
installation or credit. The 80% goal stays active.

Production ELF SHA-256: `8db9baee64ea34d6e1f084a23e247f83994faa3b950b284f05ab406a252cedc3`.

Guard SHA-256: `6a6094f04735cb3127833e50b21f98c3374916605acd7aa79ccdebd80d22dfe7`.
