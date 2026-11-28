# Resource slot initializer guarded byte match - 2026-11-28

`func_1500AC14` in `conker/src/game_36680.c` replaces its zero-return placeholder
with the complete **92-word / 368-byte** resource initializer. VA
`0x1500AC14..0x1500AD84`, ROM `0x380C4..0x38234`, frame **104 / 0x68**.
The semantic C has **35 same-index bound retail words**; **57 expected-word
guards**, including nine changed relocation positions, recover the closed
register/control-flow layout. No instruction is inserted or omitted. Both
complete owner padders match, preserving all **81 other functions** and pools.
This is a guarded match. The raw compiler output is not byte-exact.

Actual production: **4,729 / 5,528 (85.55%) total**, **4,056 / 4,855 (83.54%)
Game**, Init 492/492, Debugger 181/181, zero address drift and 799 different.
Conversion rows and denominators stay fixed. One new match is credited;
**247 more** reach 90% at 4,976/5,528. The shared types, related consumer and
caller declaration receive no additional credit. Tools `7e0da27ee4fb8d14254647aa39a9cfa8902d50ed` was committed
before installation; previous consumer was `dc2f82e5`.

## Recovered behavior and compatible object views

The initializer visits fifteen 16-byte resource slots and fifteen 4-byte presets.
It loads the unsigned 16-bit ID before clearing address+0, pending pointer+8,
aligned size+4 and state byte+C. Bytes+D..F remain untouched. ID255 skips
processing. Otherwise the enable halfword selects the request, with ID59
forcing it even when disabled. Skipped dimension pairs remain untouched.

The existing provider definition is `u32 func_1502B020(u32 *size,u32 depth,...)`.
The call passes the four O32 words `&size,2,0,id`; its result is a ROM address
word, not a native pointer. The initializer retains the raw size for its zero
test and writes `(size+15U)&~15U` with 32-bit unsigned wrapping. It reads the
descriptor's unsigned 16-bit span+2 and divisor byte+8 after the provider.
Zero size or span clears the address and numerator while retaining the aligned
size. The two halfword outputs are `(divisor<<5)-1` and
`(((span/divisor)<<6)/5)-1`, truncated to 16 bits. Their exact retail meanings
remain unnamed; no invented asset-format interpretation is required.

`resource_slots.h` replaces the false scalar declarations of `D_800DDA90` and
`D_800BE4A0` with shared fifteen-entry `ResourceSlot` and `ResourcePreset`
arrays. ResourceSlot contains two 32-bit words, a pending pointer, state byte
and three retained bytes. The native SDK32 layout is 16 bytes. The related
`func_1517CFC4` consumer now uses the same pending pointer field; all 14 raw
functions and its complete padded owner stay fixed. `game_3B920.c` declares
the initializer as `void func_1500AC14(void)`; its one raw function and whole
padded owner also stay fixed. The complete original caller discards the result.
The historical C return spelling is unproven.

The final dimensions cursor is derived from the complete fifteen-entry array
object, preserving valid character-pointer traversal. This refinement changes
none of the 82 raw functions, bindings or pools. Native checks and the actual
main-owner recipe were rerun on that final source. All six proposal files are
required together; installing only the initializer would leave incompatible
global declarations.

## Qualification and limits

- Native SDK32: **384 cases at each O0/O2/O3**, ten effective semantic controls,
  strict aliasing, trapping UBSan and LTO type checks. Every byte of slots240,
  presets60, enables30, dimensions60 and synthetic descriptors65,5360 is checked.
  Eight provider-mutation modes cover post-call reads, stable aligned output
  pointer, unsigned ID/span boundaries and alignment wrap. The synthetic65,536
  descriptor capacity is not a claim about retail capacity. Native divisor zero
  is explicitly excluded.
- A separate17-case link uses the actual provider source definition across
  native32 translation units. It qualifies the size pointer, varargs and ROM
  word return. A wrong integer size parameter fails specifically at LTO type
  checking. The lower resource lookup remains opaque; whole native provider
  owner execution is not claimed.
- Guest: **1,068 executions** of original and raw streams, all92words exercised,
  complete normal memory/ordered accesses/calls equal, callee-saved ABI intact.
  **3,766 access-fault pairs** compare complete memory, calls and access traces.
  Literal raw fault GPR/EPC equality and the void residual V0 are not claimed.
- The zero-divisor path performs both halfword stores before `BREAK 7`.
  An arithmetic-region proof decodes both instruction streams into canonical
  32-bit expressions and qualifies every nonzero numerator/divisor and every
  shared arbitrary32-bit zero quotient, ten output binding/zero combinations,
  final HI/LO, two intervening MFLO-to-DIVU instructions and three structural
  controls. This is a scoped arithmetic proof, not a whole-function symbolic
  proof or hardware-timing test. The [NEC VR4300 manual, page417](https://hack64.net/docs/VR43XX.pdf#page=417)
  leaves divide-by-zero results unspecified. No device-specific quotient is
  assumed. Finite guest fixtures additionally exercise five quotient choices.
- Complete original 84-word startup caller: **256 fixtures /1,536 connected runs**,
  every parent word exercised, zero arguments and three residual V0 poisons.
  Complete terminal registers, memory, calls and events agree. The aligned
  full-ROM census finds the sole direct JAL at ROM 0x3BA24 / VA 0x1500E574 and no entry
  word literals. This does not establish the absence of all indirect calls.
  Larger startup providers remain opaque; the 24-byte bzero is modeled.
- The changed shared header has **206 compiled direct users**, no transitive
  header users. All recipes were audited: **199 whole objects identical** and
  seven completely classified metadata exceptions. All code/data, pools and
  named relocations stay fixed in those seven; only undefined table sizes
  change to 240/60, with compiler path metadata and symbol-index permutations.
  Complete independent before/after header-only links both equal the frozen
  baseline. No linked dependent is excluded. The large audit is reused only
  after checking every pinned input, driver, receipt and2,715 cached output files.
- Both complete padders, the actual 5-command main recipe (including retained
  GLOBAL_ASM preprocessing/postprocessing), both 3-command related/caller recipes,
  original target GNU assembly/link and independent whole-owner assembly
  reference agree. The owner retains `func_15009334` assembly. **16 actual GNU
  links** cover four independently moved binding groups and signed HI/LO seams;
  four fail-closed controls reject wrong expected words and relocation names.
- Independent original-assembly reference, selected private image and actual
  production ELF are identical: **316 changed bytes**,275 target code bytes,
  **zero exclusions**. The remaining delta is fully qualified symbol/string
  metadata and the target's definition size 12 to 368. All other code/data,
  addresses and extents remain fixed. **720 protected owners /189,088 bytes**
  are exact. Production also rebuilds and classifies all seven metadata owners.
  ELF SHA256 `7a807c6a9c3bf19567712d8a651f9a98a081e4a15f83a3da411f4f7e1bad0f70`.
- Six packaged tests pass freshly against primary and closed-twin tools roots
  before and after installation: **24 fresh tests** with equal reports and
  audited import/data closure. The twin has 2,519 frozen dependencies and 15
  independent task copies. The original failed package/log is retained: its
  extracted helper lacked a sys import. The revised helper and tools-root
  routing are requalified. Shared `make tools-check` passes.

One prior packet-only Claude Pro advisory was reconciled without accepting a
source correction; it suggested a form already present in the supplied C.
Codex remains sole writer. No new Claude call was needed in this completion.

## Documentation, graph and continuation

Only aggregate matching rows change in the root README. Five current indexes
link here. The scoped Graphify AST refresh covers the three C owners, two
headers and tools packet, retaining previous IDs and qualification metadata;
it is not a full-corpus extraction. Actual hook-terminal, graph and immutable
bank receipts are retained in
`conker/build/game-resource-slot-initializer-1500ac14-private/`.

Read-only sibling audit: the local host snapshot's
`recomp_scene/visibility_init_out/func_1500AC14.c` is empty; a generated entry
also appears in `out_1500E470/.c`. This does not establish an active host build
implementation or warrant copying these decomp declarations into the distinct
context ABI. No host changes/build/launch occur; Release remains frozen.
The dirty real `64CBFD Tools` sibling is preserved. No push or subagent.

The 90% goal remains active. Next qualify `func_150F695C` from this sealed
bank (103 body words plus two alignment words in its 105-word slot, frame 176). Its read-only handoff is
`NEXT_TARGET.md`; no next source or match is credited.
Keep `func_1514EECC` parked and preserve the mixed-boundary handoffs for
`func_150AE280` and `func_150A6760`. The next private candidate earns no credit
before its complete qualification and production recount.
