# 1836: Record-key chain association match

Date: 2026-10-29. Target `func_15195D00`, owner `generated_1C2C60`.
VA `0x15195D00..0x15195DD4`, ROM `0x1C31B0..0x1C3284`,53 words.

The false zero-return placeholder is replaced by a complete void association
routine taking an owner pointer and three32-bit key/index/mode words. Owner
offset0x18 holds the chain. Record offset8 is a32-bit key, offset0xC an unsigned
16-bit index, offset0xE a mode byte, and offset0x10 the next-record pointer.
On a miss it requests20 bytes from `func_151957B0` using the global intrusive
pool heads `D_800E08E0/D_800E08E4`, links the new record, and initializes those
fields. The incoming index comparison retains its full32-bit width; truncation
occurs only at the halfword store.

Preserve the original look-ahead traversal: the head is tested, then a cursor
advances ahead of the tested record. On multi-record chains, a null look-ahead
exits before testing the tail. In a three-record witness, a tail match still
allocates another record.
The original v0 values for head/middle matches are diagnostic machine state,
not a C return contract. The only retained direct caller, `func_15195DD4`,
ignores v0 and immediately increments its loop counter. A complete aligned ROM
scan finds exactly its JAL at0x1C33FC and no full pointer words; computed/encoded
references are not excluded. The caller stays a C placeholder and gets no credit.

Pointer-return drafts emit55..58 words and add result-register copies. The
observed void interface recovers53 words. Moving the initial record assignment
inside the nonempty branch restores the opening v0/v1 roles. Register hints and
explicit mode-temporary layouts do not improve the remaining four words; the
mode-first48-byte-frame control is rejected.

Four expected-word/binding guards normalize the single paired record spill
from compiler SP+0x20 to retail SP+0x24 within the unchanged0x28 frame, and restore
the mode-load/next-clear order. Outgoing homes0..0xF, saved S0/S1/RA homes0x14/
0x18/0x1C and incoming owner/mode homes0x28/0x34 remain unchanged. The record
home occupies the remaining four bytes of the eight-byte local area. There
are zero frame-size adjustments, insertions or omissions; all ten bindings
and branch targets are preserved. This is guarded byte-exact matching.

Validation:

- 25,344 cases /76,032 executions compare original, normalized and raw C across
  chain lengths0..7, every possible match position, signed/high-bit keys, full
  index words, mode bytes, both pool states, provider mutations and stack phases.
  All53 original words are covered. Raw public memory/calls agree; normalized
  GPR/FPR/HI/LO, full RAM, events and access traces match the original.
- 35,712 actual provider-boundary checks verify the live record pointer at the
  literal retail SP+0x24 home. Provider clobbers cover caller-save registers,
  FP temporaries, HI/LO and all four outgoing homes. Incoming owner/mode-home
  mutations are guest-only probes, not portable native C behavior.
- 125 dispatched memory-access fault prefixes agree in full literal state.
  A sparse head match needs neither the next pointer, unused records, allocation
  output nor pool globals. Three GNU relocation layouts pass720 cases, including
  signed LO16 carries.
- The original11-word caller window0x15195F2C..0x15195F58 passes1,280 cases,
  including the signed clamp/store of owner byte0x14, four arguments, actual JAL
  and post-call counter increment. Earlier parent gates are preconditions;
  complete-parent/gameplay behavior is not claimed.
- Native32 O0/O2/O3 each pass8,448 cases with UBSan and reject eight effective
  controls, including an incorrect full-tail search. A valid non-null allocation
  is a native precondition; C behavior on allocation failure is not claimed.
- All212 raw-byte and ten binding corruptions reject; all four guard preimage
  controls reject. Changed C and unexpected-diagnostic controls reject.
- The complete compact/padded owner preserves68 neighbors and pools. Actual
  three-command Make output reproduces the qualified object. Selected and owner
  compilation emit zero diagnostics; the inherited duplicate-recipe Make warning
  remains. Eight fresh canonical checks run independently in both tools copies,
  plus each shared tools check. Installed checks rerun two methods per copy and
  reuse six only by complete input/module/artifact identity.
- The production ELF equals the independent literal prediction:168 changed bytes
  =167 target code +1 target extent, zero metadata changes/exclusions. All6,055
  other linked bodies and all addresses remain fixed;189,088 protected Game
  data bytes /720 owners remain exact.

Fresh adopted-ELF recount: **3,913/5,506 (71.07%)** total,
**3,240/4,833 (67.04%)** Game, Init492/492, Debugger181/181, zero drift.
The C inventory is unchanged. **217** more matches reach the4,130 threshold.

Tools commit first: `aa668dfc8729aee3737038a0d69984642db9d890`; consumer pins it. No push, host-port,
Release, save/editor or memory changes. The older tools mirror retains all
1,946 inherited dirty paths plus the three new tool files. Zero Claude calls:
retained caller evidence, source experiments and bounded oracles resolve the
routine. No provider/allocator conversion credit is added.

The constructor model is checked against the original29-word MIPS routine in
720 additional cases /2,160 executions, with540 checks of two-element pool
head/tail updates and actual allocator arguments(20,1,0,0). This caught reversed
head/tail updates in the first bounded model. The corrected model and native
fixture passed a fresh private suite and all eight methods again in both tools
copies before the unpublished tools commit was amended. Superseded evidence
is archived and is not used for acceptance. C source, object and ELF bytes were
unchanged by this model correction; successful allocation remains a precondition.

Graphify receives a scoped native AST refresh with all49,407 old nodes retained
or uniquely relocated and old relationships accounted for. The obsolete s32
return edge retires only against the source/caller-supported void signature.
Calls to the existing constructor and the original caller window are source/
binding-validated. Outside-scope manifest/community data stay historical; no
full-corpus extraction or complete allocator qualification is claimed.

Artifacts: `conker/build/game-record-key-chain-match/`. Next screened target:
`func_150A613C`; screening is not source/ABI qualification. Previously parked
candidates, including `func_15030310`, remain private and uncredited.
