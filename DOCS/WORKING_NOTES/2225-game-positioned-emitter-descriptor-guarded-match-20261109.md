# Game positioned emitter descriptor guarded match - 2026-11-09

func_150E75A0 now matches all **76 words / 304 bytes** of retail. The complete
semantic descriptor builder remains C, with its natural **0x88-byte frame**
and one final submission call. **43 expected-word and relocation guards**
normalize private tag storage, temporary registers and independent store
scheduling. This is a guarded match, not an unmodified compiler byte match.

Fresh production totals are **4,293 / 5,513 (77.87%)** overall and
**3,620 / 4,840 (74.79%)** Game. Init remains 492/492, Debugger 181/181;
there is zero address drift and **1,220** different C functions. The existing
conversion inventory is unchanged. **118** further accepted matches are
needed to reach at least 80% (4,411/5,513).

## Source and ABI

Owner: conker/src/game/generated_113D60.c. Retail assembly: conker/asm/113D60.s.
VA 150E75A0..150E76D0, ROM 114A50..114B80. The semantic recovery in Note 925
already described the initialized fields and result forwarding.

Recover u8 duration/opacity and s16 size0/size1 parameter widths, matching
retail's byte/halfword loads from incoming argument homes. The one local
prototype is updated consistently. All 28 other complete-owner bodies and
relocations, including both callers, remain identical. The legacy fixture's
one literal call now states these four narrowing casts explicitly; its
expected field values and boundary assertions are unchanged.

Retain the sampled D_80088A64 byte in a one-byte local array across the
two-word position copy. This emits the observed store/reload lifetime without
adding volatility, invented padding or assembly emission. The chosen C stores
the private byte at SP+0x84; retail uses SP+0x28. Both place the 0x58-byte
descriptor at SP+0x2C, and both keep the tag outside that descriptor. Guards
normalize these private stack offsets and the independent instruction schedule.
The array is a source representation of the measured lifetime, not proof of
the original declaration.

The descriptor still leaves byte +0x11 and +0x42..+0x57 unwritten. Tests verify
that those **23 bytes** retain their initial storage contents. They are not
zero-filled or newly described as known data. Final func_1515548C receives
descriptor, zero, pair, mode, zero, narrowed slot and full context. Its V0
result passes through unchanged.

## Qualification

Six focused tests run before and after installation in both the mounted tools
checkout and a read-only overlay using the sibling tools environment. Every
receipt fingerprints task files and loaded helper modules. The sibling's
2,434 inherited dirty paths and seven relevant path states remain unchanged;
new modules are supplied by the overlay instead of copying over that work.
A final caller-report key was clarified to say raw function body rather than
whole owner object. That output-label-only correction received a fresh caller
replay in both environments; the original four full-suite receipts are retained
unchanged and the exact one-string delta is audited separately.

- Complete owner: 28 raw and padded neighbors unchanged, data pools and
  register-usage metadata unchanged. Both padders agree on all 29 functions.
- Actual unmodified Makefile in a disposable tree produces the exact predicted
  owner object using its ordinary -O2 -g3 profile. Both padders preserve the
  existing D_800A1350 compact-rodata binding required by this owner.
- Independent guest contract: **452 cases per body**, across raw C, normalized
  C and retail: **1,356 executions**, all 76 words visited in each body, plus
  **24 independent symbol/entry/stack rebases**. Cover every flag/slot byte,
  narrowing boundaries, distinct sizes, null pair, complete context and return,
  source mutation at submission, and twelve float-word patterns including
  signed zero, denormals, infinities and NaN payloads. These are word copies,
  not floating-point arithmetic claims. Saved registers, restored SP, argument
  home stores and caller storage beyond the four parameter homes are checked.
- Native32: five preserved contracts at O0/O2/O3 with UBSan, including the real
  recovered func_150E7290 dispatcher plus this builder and bounded final
  submission. Twelve compiled native negative controls are effective.
- Fourteen compiled IDO controls fail the independent guest contract, including
  writes to the unknown descriptor bytes. Both padders reject all 43 stale
  expected words and an independently stale relocation specification: 44
  rejections per padder. Payload/scope/binding and whole-image corruptions
  are independently rejected too.
- All six original descriptor tests pass freshly after installation in both
  environments, including their independent IDO footprint check. Shared tools
  smoke checks pass in both copies; three unchanged regression receipts are
  explicitly reused only after exact helper/test fingerprint verification.

The two retail JAL sites are ROM 0x1148EC and 0x115344, in func_150E7290 and
func_150E7C9C. The first caller remains non-matching: its linked JAL is one word
earlier than retail, a pre-existing difference. The census records the retail
and linked positions separately. Neither caller's body is modified. No complete
caller guest execution, real submission implementation, hardware or gameplay
acceptance is claimed.

## Linked and production audit

Strict whole-ELF prediction permits exactly this function's slot and its symbol
extent change from 296 to 304 bytes: **199 changed image bytes**, zero
unexplained bytes, zero exclusions and no symbol permutation. All **6,052**
function addresses stay fixed. Every other linked function stays unchanged.
All **189,088** protected Game-data bytes and their 720 owners remain exact;
the complete Init and Debugger images are covered by whole-image equality.
Four independent image corruptions are rejected.

The production Make rebuild invokes the compiler for this owner only, with no
new diagnostics. Its object and ELF equal the pre-install predictions. The
existing guard manifest is an exact prefix of the new manifest. Conversion CSV
and Makefile remain byte-identical. As at the inherited bank, ordinary make all
reaches the known whole-ROM checksum mismatch (exit 2); it is not a retail-ROM
completion claim. Fresh match-progress supplies the counts above.

Production fingerprints:

- ELF: `e0f6c5de19b01857c58e49f1624fad022cb4e9ea617ee28365613c10f19ccefe`
- Binary: `a38e9a00ea1b00cca5e014ac79e02548a2b03aa8814115622efa24cc0da5c5c2`
- Owner object: `6d1e875d68fed15b0ccfa1489cae85db122be7a9a584b5457d8b80b530c680b6`
- Guards: `157d6b0a1f5782e5ae6ea772fbbdcfa59a05e5426b6f53208319b285dbaf81c7`
- Makefile: `8e676e04318f8645e6b277ed60ed9f221d8901a5e6a02efd279d478d46a615f8`

Graphify refresh is scoped AST work on the touched paths, with fail-closed
retention of unscanned existing nodes. The retention receipt verifies no
removed nodes outside changed paths and the current source positions of all
26 C definitions. The three retained assembly functions are covered by the
owner audit. This is not a fresh full-corpus semantic extraction.

## Continuation

Next matching target: func_1504715C, the recovered 89-word actor-to-height-result
builder in generated_71820.c. Note 779 supplies its alias-sensitive metadata,
vertex and post-helper flag contract; re-query the current graph before edits.
It remains uncredited and needs the same source/ABI, guest/native, owner,
Make, strict image, installed recount, documentation and commit gates.

The separate func_1510D404 compiler investigation remains private and
non-matching. Owned CFE/UOPT/UGEN traces show the -65 mask survives optimizer
wire emission; UOPT considers it eligible for a register, then rejects its live
range for negative estimated saving. It does not recover retail's loop-limit
spill. Its new type/lifetime probes and detailed traces are retained under
conker/build/game-resource-maintenance-1510D404-match without new credit.
No wide-temporary frame fit or broad conversion batch is installed.

No host-port or frozen Release artifact was changed. Local tools commit
precedes the consumer pin commit; publication is not part of this checkpoint.
