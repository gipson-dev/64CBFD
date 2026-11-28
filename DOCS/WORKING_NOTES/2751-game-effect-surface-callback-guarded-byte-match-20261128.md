# Effect surface callback guarded byte match - 2026-11-28

`func_150F695C` in `conker/src/game/generated_1228D0.c` replaces a zero-return
placeholder with its complete semantic callback. Its body is **103 words /
412 bytes**, VA `0x150F695C..0x150F6AF8`, ROM `0x123E0C..0x123FA8`, frame
**176 /0xB0**. Its retail slot ends at VA `0x150F6B00` and ROM `0x123FB0`:
**105 words**, including two retained zero alignment words. The source emits
**91 same-index bound retail words**. Twelve expected-word guards recover the
optional-surface boolean register and branch layout; all twelve relocation
binding positions stay fixed. No instruction is inserted or omitted. This is
a guarded match; the raw compiler output is not byte-exact.

Production recount: **4,730 /5,528 (85.56%) total**, **4,057 /4,855 (83.56%)
Game**, Init 492/492, Debugger 181/181, zero drift and 798 different. One new match
is credited. Conversion rows and denominators are unchanged; **246 more** reach
90% at 4,976/5,528. The interpolation declaration earns no additional credit.
Tools `cbab6721528845fa21860faaeec8568b46f8405d` was committed before source installation; previous consumer
`60cf386ba3e1d47d6798a0b42522656bd1efd7f9`.

## Recovered callback and ABI

This is index 8 in the nine-entry `D_80089B38` callback table, at VA
`0x80089B58` /ROM `0x22E618`. A complete aligned ROM-word census finds this
one entry literal and no direct J/JAL; this does not rule out other indirect
call routes. Original parent `func_15134E48` supplies four vector pointers,
a stacked float fraction and an emitter pointer. It ignores the return value.
The current callback uses void; historical C spelling is unproven. The parent's
current C remains a placeholder and receives no matching credit.

The callback obtains three vectors, one scalar parameter, a signed 16-bit lifetime,
unsigned 8-bit alpha and float scale through the original thirteen-word interpolation
interface. It scales the result by `1 + RNG()*2`, selects an optional surface
using `D_800A1B74` (bits 0x3F19999A, approximately 0.6), and queries the emitter's
actor when selected. Otherwise it clears the surface metadata, flags, state
and value and sets height to `D_800A1B78` (bits 0xC61C4000, -10000). The nine
vertex halfwords and padding remain untouched on this default path.

An additional RNG call selects the alternate mode below 0.5 only when the
surface is enabled. The sixteen-word `func_151D9014` submission passes the
interpolated position and velocity, parameter/lifetime/alpha/scale, surface
selection, two copies of `D_800A1B7C` (bits 0x3FE66666, approximately 1.8), fixed
mode words, surface address, alternate mode and the emitter's group/context
bytes. Names retain the existing function/symbol identities; comments explain
the measured behavior without asserting unverified game terminology.

The shared SDK32 surface view has 36 bytes and matches the existing height-query
types. The emitter view is a 120-byte prefix of the full 472-byte record; context
is at +1, group +0xC, actor +0x1C and derivativeScale +0x74. Native fixtures allocate the
complete record. All thirteen interpolation words and all sixteen submission
words are checked through separately compiled SDK32 translation units with LTO.

`game_161520.c` receives only the corrected void thirteen-argument declaration
for `func_15137F30`. That routine remains original 97-word assembly. Its actual
six-command mixed-owner recipe is replayed before/after without an include shim:
all 64 main raw functions, the one separate dispatcher raw function, pools and
the complete padded owner are unchanged. Its SHA256 is
`f08cadd482db3dad367ea176789a0c2e0b307017e62b2b4304e26d3cb150aba7`.

The existing `func_151D9014` ABI represents argument 12 as a signed 32-bit surface
address word. Its assembly forwards that word into a pointer argument. The
new callback explicitly converts `&surface` at this established O32 boundary;
native fixtures assert 32-bit pointers and check the high-bit address roundtrip.
This does not establish a portable 64-bit pointer API. A private experiment to
change existing callers to void* altered `func_151AB9C8`'s register allocation,
and its old guard correctly rejected +0x100. No such source was installed and
no old guard was bypassed. Only the interpolation declaration repair remains.

## Qualification and exact production evidence

- Native SDK32: **400 cases at each O0/O2/O3**, strict aliasing, trapping UBSan,
  LTO type checks and nine effective semantic controls. Checks include valid
  input aliases, threshold ties, signed zero, lifetime sign boundaries, all 256
  metadata bytes, exposed outputs and public provider mutations. Original-guest
  vectors are generated freshly. Two additional controls reject an f64 callback
  fraction and a pointer in place of the signed 32-bit surface-address word through
  specific LTO type mismatches. Provider implementations remain opaque here.
- Literal MIPS: **960 cases per stream /1,920 executions**, all 103 body words,
  all three optional paths and all four rounding modes. Complete terminal
  memory, GPR/FPR, HI/LO and FCSR states agree. Ordered accesses, calls and
  defined packet values agree. **130 access-fault pairs** preserve complete
  memory, call/event records and access/trace prefixes. Raw scratch-GPR/EPC
  equality at faults is not claimed. Incoming-home mutations are guest-only.
- A closed decoded-opcode symbolic proof covers the entire 103-word function:
  three paths times two stack phases, symbolic public reads/call results,
  identical ordered FP operators and operands, ordered memory/call observations
  and complete terminal abstract states. Provider output extents and unexposed
  private bytes are constrained by the ABI; no arbitrary malicious private-frame
  provider mutations are claimed. Three effective instruction controls reject
  a wrong metadata offset, alternate result and live surface mask. Proof SHA256
  `861956408cb7c357fa6a59edd1ba9d175f9769be28879d3b17e4660a215d5d42`.
- Connected original caller: the 297-word parent is pinned. Four table-origin
  words, a 13-word argument/call/delay window and 46 post-call words execute over
  **288 fixtures /1,728 connected executions**, both loop and exit paths, four
  rounding modes and two stack phases. Three return-value poisons prove the
  ignored return through its first overwrite on each path. A 45-word static
  liveness walk checks no earlier V0 read. Two effective controls reject missing
  fraction/emitter home stores. This is not complete parent execution.
- Both complete owner padders recover all 105 retail slot words, preserving the
  two alignment words and all 23 other raw/padded functions and pools. The actual
  three-command target recipe equals an independent original-target assembly
  whole-owner reference. **16 actual GNU links** move four binding groups and
  cross signed HI16/LO16 seams. Four controls reject stale expected words and
  unexpected guard relocations. The old CSV bytes are retained exactly and only
  twelve rows are appended.
- Independent original-assembly reference, selected private image and actual
  production ELF agree literally: **335 changed bytes**, 303 target code bytes,
  **zero exclusions**. The remaining delta is qualified symbol/string metadata,
  including the target size 12 to 412 at its fixed address. All other definitions,
  addresses, extents, alignment bytes and data remain fixed. **720 protected
  data owners /189,088 bytes** are exact. Production's provider owner stays
  byte-identical. ELF SHA256
  `3b2aaa7e00cb57e89b17d49298ab2f33f1650d3eb67a9ba7528db9daf96a335a`.
- Five packaged tests pass against primary and closed-twin tools before and
  after installation: **20 fresh tests**. The twin has 2,534 frozen dependencies
  and 15 independent task files. Imports and 260 tool data inputs are audited to
  each selected root. Semantic report rows agree. Four raw interface objects
  differ only in `.mdebug`; retained section comparisons preserve every other
  section. The initial preinstall report equality check caught these hashes;
  an additional primary interface replay classified them. No executable or
  loaded metadata exclusion was introduced. Shared `make tools-check` passes.

The target owner retains ten pre-existing CFE Warning712 messages in neighboring
pointer/integer wrappers; no new warnings are introduced. Existing Make recipe
warnings remain documented separately. Zero Claude calls: Codex settled this
target with local evidence and remained the sole writer. No subagents or push.

## Documentation, graph, sibling applicability and continuation

The root README changes only two aggregate matching rows. Five concise indexes
link here. The retaining scoped Graphify AST refresh covers the two C owners
and fourteen Python task files, preserving old IDs and qualification metadata;
it is not full-corpus extraction. Actual hook-process terminal, graph-publication
and immutable accepted-bank receipts remain in
`conker/build/game-effect-surface-dispatcher-150f695c-private/`.

Read-only host applicability sampled
`64CBFDOGL/recomp_scene/intro_effect_dispatch_out/func_150F695C.c` and
`func_15137F30.c`. Both contain only unused initialized locals and a null
statement. Active host build selection remains unverified, so this is not
evidence of an active host implementation. No host changes, builds or launches;
Release stays frozen. The real dirty `64CBFD Tools` sibling is unchanged.

The 90% goal remains active. Next qualify the same-family `func_150F6178` from
the sealed N97 bank; its source remains a placeholder and receives no credit.
Keep `func_1514EECC` parked and preserve the mixed-boundary handoffs for
`func_150AE280` and `func_150A6760`. Every next candidate still needs its own
source/ABI, guest/native, owner/padder/rebase, actual Make, strict image,
production recount, documentation, graph and commit gates.
