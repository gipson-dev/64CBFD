# 1857: Descriptor-gated effect buffer constructor match

Date: 2026-10-30. Target `func_1518E3C4`, owner `generated_1BA1D0`.
VA `0x1518E3C4..0x1518E4A0`, ROM `0x1BB874..0x1BB950`:
**220 bytes /55 words**, all reachable, no alignment tail.

The former zero-return placeholder is now
`void *func_1518E3C4(void *descriptor,u8 priority)`. It reads the descriptor's
first pointer and rejects type byte150 at pointee+4. Otherwise it requests
`func_15167A68(33,1,2540,1,priority,1)`, returning NULL on allocation failure.
The descriptor is read again after allocation, preserving provider changes,
and its12 bytes are copied to created+0x18. The routine initializes the original
integer/byte/float fields, clears2,400 bytes at+0x48 and returns the captured
allocation pointer. It does not repeat the type gate after allocation.

All55 words and three call bindings emit directly from semantic C. There are
no guards, inserted/omitted instructions, frame repairs, compiler-profile,
shared-header, layout or conversion-CSV changes. Frame40 saves RA at+28;
the result pointer's retained local is+36. Outgoing arguments use24 bytes.
Incoming descriptor/priority homes are entrySP+0/+4, with the priority byte at+7.
Allocator and memcpy prototypes precede the new body; compatible existing
declarations later in this generated owner are retained. The SDK bzero type
is `void(void*,int)` as declared in `os_libc.h`.

Allocation size is0x9EC. The clear covers0x48..0x9A7. The90 untouched bytes
are the16-byte allocator header, bytes0x2E..0x2F,0x44..0x47 and the68-byte
tail0x9A8..0x9EB. Tests seed this backing explicitly and verify preservation;
the C routine does not initialize those bytes or promise allocator padding values.

- Eight focused methods pass freshly in both tools copies, plus shared tools
  checks. Production repeats two installed checks and reuses six semantic
  checks only under exact input/module/artifact fingerprints.
- Guest: **1,166 cases /3,498 original/raw/padded executions**, all55 words,
  literal register/private-memory/call equality,43 access prefixes and three
  relocated layouts /48 cases. Cases cover every type byte and priority byte,
  allocation failure/success, live descriptor changes, argument-home redirects
  and both stack phases. Home redirects remain guest-only claims.
- Native32 O0/O2/O3 each pass **846 cases with UBSan** and exact checks of all
  2,540 seeded output bytes and descriptor bytes. Guest scalar writes are
  translated to native little-endian expectations while untouched byte backing
  remains unchanged. Actual native pointers are checked separately. FNV checks
  are additional checks, not substitutes for byte equality. Nine controls reject
  wrong type, allocation kind/size, copy offset/length, clear offset/length,
  initial scale and a repeated type gate. Native excludes private home mutations
  and guest stack aliases. Allocator and SDK services are bounded providers;
  their original instructions, complete parent, hardware and gameplay are not claimed.
- All18 original call sites in `func_1518D1C0` are exercised with eight cases
  each. Sixteen windows are JAL plus the priority-byte load in its delay slot.
  Two three-word windows at VA0x1518D5C0 /ROM0x1BAA70 and VA0x1518D6B0 /
  ROM0x1BAB60 instead load priority first, call, and store a descriptor halfword
  in the delay slot. The actual T3/T9 signed-halfword entry precondition from
  callerSP+0x52 is checked against retail's earlier LH. A0 is the caller's
  descriptor at SP+0x3C. Earlier setup and later parent work remain preconditions.
- Full-owner compilation/padding preserves all60 neighbors and pools. Three
  actual Make commands reproduce the qualified object. Four inherited CFE712
  warnings remain: two calls each to `func_1518E4A0(arg0)` and
  `func_15190454(arg0)`. Exact diagnostic text and call counts are checked;
  only source line numbers shift. The isolated target has zero diagnostics.
  The inherited duplicate12D630 Make recipe warning also remains. All223
  raw-byte/binding controls and240 whole-image corruption controls reject.

The independent full-image prediction equals production with **162 changed
bytes =161 target code +one target extent byte**. Extent changes12 to220 bytes;
metadata changes and image exclusions are zero. All6,055 other linked bodies
and all addresses stay fixed. Protected Game data is exact across189,088 bytes /
720 owners. Guards and the C conversion inventory are unchanged.

Fresh adopted-ELF count: **3,934/5,506 (71.45%)**, Game **3,261/4,833 (67.47%)**,
Init492/492 and Debugger181/181; zero drift. **196** more to4,130.
Tools committed first: `27fd4f0b95442733f24d50556dd8e0d392f1edfe`. No push. Root README updates its aggregate
rows and snapshot date; detailed recovery evidence remains in this note.

The eleven-file scoped AST refresh retains or uniquely relocates all50,473
previous nodes and preserves104,628 valid old relationships. One obsolete s32
return edge retires for the recovered pointer return. The two-argument signature,
all18 direct caller windows and three helper bindings receive source evidence.
Outside-scope freshness/statistics remain historical; no full-corpus extraction
or reclustering claim.

Private `func_1518BBF4` remains uninstalled: the closest form restores its48-byte
frame and five saved roles but emits54 words against55. A55-word carried-depth
form changes loads/bindings and is rejected. Private `func_150A23E4` and all
other parked candidates remain uncredited. The mixed handwritten resume/C-entry
slot `func_150AE280` receives no ASM-as-C or denominator credit.

Artifacts: `conker/build/game-gated-effect-buffer-constructor-match/`.
Next screen `func_150843AC` requires all qualification gates. No host-port, frozen
Release, saves/editor, private-input or memory changes. Zero Claude calls.
The75% goal remains active.
