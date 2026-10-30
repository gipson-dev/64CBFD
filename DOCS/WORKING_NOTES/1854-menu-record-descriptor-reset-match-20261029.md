# 1854: Menu record descriptor reset and factory return ABI

Date: 2026-10-29. Target `func_150B7484`, owner `generated_E4070`.
VA `0x150B7484..0x150B7560`, ROM `0xE4934..0xE4A10`: **220 bytes /55 words**.
All 55 words are reachable and fill the classifier slot; no alignment tail.

The zero-return placeholder becomes `void func_150B7484(void)`. It constructs
a fixed 60-byte descriptor, optionally releases the old first pointer in
`D_800D9898`, creates its replacement with `func_15169968`, stores the returned
pointer in the same slot, and finally sets byte `D_800D9890` to 3. The old
pointer is captured before descriptor stores and passed to the destructor
when nonnull. The descriptor remains live across that call. Factory failure
still stores NULL and selects state 3.

`MenuRecordDescriptorE4070` describes the recovered field widths and offsets.
Unknown field meanings retain offset-based names. Its asset pointer is
`D_800918DC`, fields+0x14/+0x16/+0x18 are zero halfwords, +0x1C/+0x20 are
60.0f, +0x24/+0x26 are zero halfwords, +0x28/+0x2A are 81, and +0x2C/+0x2E
are 88. Bytes+0x30..+0x39 are `6,1,255,0,0,255,7,21,1,0`.
These are **40 defined bytes**. The remaining **20 bytes** at +4..+0x13,
+0x1A..+0x1B and +0x3A..+0x3B are unwritten in retail; the source preserves
that behavior rather than zero-initializing the complete descriptor.

The initial byte-array view and the selected typed view both emit all55 raw
words and ten relocations exactly. No guards, insertions, omissions, profile
changes, frame adjustments or shared-header edits. The existing per-owner
O2/g3/no-unroll profile is retained. Frame0x58 saves only RA at+0x14; the
descriptor occupies +0x1C..+0x57 and there are16 outgoing bytes. All registers
and the literal stack bytes agree in guest tests, including the unwritten bytes.

The factory wrapper's existing C declaration incorrectly returned void, while
retail propagates the pointer from `func_15169900`. Its source is corrected to
`void *func_15169968(register void *arg0)` with an explicit returned call.
The complete `generated_196DB0` object stays **byte-identical**, preserving all
four functions and pools. Both the eight-word wrapper and 26-word constructor
already equal retail in the current ELF. This source/ABI repair receives
**zero additional matching credit**.

- Eight focused canonical methods pass freshly in both tools copies, plus
  shared tools checks. Production reruns two installed methods per copy;
  six semantic checks reuse only complete module/input/artifact fingerprints.
  The older tools mirror keeps2,000 inherited dirty paths and receives three
  new modules without a mirror commit. The actual no-unroll compiler adapter
  is fingerprinted, not an unused default-profile adapter.
- Guest: **3,184 cases /9,552 original/raw/padded executions**, all55 words,
  literal full-state and descriptor-byte agreement. Tests cover null/nonzero/
  full-word old/result values, all256 state bytes, destructor/factory global
  changes, live descriptor mutations, two stack phases, and seeded unwritten
  bytes. There are108 access-prefix comparisons, three layouts /96 relocated
  cases, and192 deliberate guest stack/global alias cases.
- Native32 O0/O2/O3 each pass **1,208 cases with UBSan**, using the actual
  pointer-return wrapper C body and an opaque constructor provider boundary.
  Size/offset assertions check the typed 60-byte descriptor. Native acceptance
  checks all40 defined bytes; it makes no claim about initial values of the
  unwritten bytes or a destructor reaching an unexposed local-stack pointer.
  Nine effective controls reject inverted release gating, wrong asset,
  wrong float, wrong size, wrong parameter, wrong state, discarded factory
  result, clearing the global before creation, and moving the state update
  before the factory call.
- The original **34-word factory chain** executes64 connected guest cases,
  including allocation success/failure and live packet/global changes. Its
  allocator arguments are `(0x5E,0,0x4C,0,255,1)`; successful allocation copies
  all60 bytes to record+0x10 and returns the allocation. Allocator and byte-copy
  operations are checked provider hooks; their complete implementations and
  the destructor implementation are not claimed dynamically qualified here.
- Original parent `func_150B6BC0` is verified from `asm/E4070.s`. Its JAL at
  VA0x150B6C28 /ROM0xE40D8 and nop delay execute32 cases with no arguments
  and ignored result. The parent C remains a stub. Switch dispatch and the
  remainder of the parent remain preconditions, not complete-parent credit.
- Complete target-owner compilation and production padding preserve20 neighbors
  and pools. Three actual Make commands reproduce its exact object; another
  three reproduce the byte-identical helper object and all four helper-owner
  functions. There are zero C diagnostics; the inherited duplicate12D630
  Make recipe warning remains. Initial default-profile owner padding overflowed
  a neighbor; using the existing production no-unroll profile resolves that
  diagnostic. The generic ASM preprocessor's rejection of a `-Wo` option was
  a wrapper limitation, not a failed IDO compiler profile. No build-rule change.
- All230 raw-byte/binding controls and240 whole-image corruption controls reject.
  Independent prediction equals production: **171 changed bytes =170 target
  code +one symbol-extent byte**, zero unrelated metadata changes or exclusions.
  All6,055 other linked bodies and all addresses are fixed, including both
  repaired-wrapper and constructor bodies. Protected Game data remains exact
  across189,088 bytes /720 owners. Guard manifest and conversion CSV unchanged.

Fresh adopted-ELF count: **3,931/5,506 (71.39%)**, Game **3,258/4,833 (67.41%)**,
Init492/492 and Debugger181/181, zero drift. **199** more to4,130.
Tools committed first: `c1c8fcb7ded49e0cb550b0ca751c1ff8319550ce`. No push. Root README gets only aggregate rows.

The scoped twelve-file AST refresh preserves all50,308 prior nodes or unique
relocations and104,265 valid old directed relationships. The obsolete s32
return edge for this void reset routine retires. The factory wrapper's
pointer-return signature, descriptor layout, original caller and factory-chain
evidence are attached. Outside-scope freshness and global analytics remain
historical; no full-corpus extraction or reclustering claim.

Artifacts: `conker/build/game-menu-record-descriptor-reset-match/`.
Next screen `func_150D8A34` still needs all qualification gates. `func_150AE280` remains
parked for a genuine entry-boundary audit: six handwritten stack-resume words,
two padding words and a separate47-word C entry at0x150AE2A0 share one current
classifier slot. Its private facts are preserved in
`conker/build/game-stack-resume-boundary-screen/HANDOFF.md`; no source/layout
change, ASM-as-C credit or inventory-denominator change was made for it.
Other private candidates, including `func_151A084C`, remain uncredited.
No host-port, frozen Release, save/editor, private-input or memory changes.
Zero Claude calls. The full75% goal remains active.
