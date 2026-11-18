# Randomized trail emitter guarded byte match - 2026-11-17

`void func_151AEAB4(f32 *position, s32 mode, s32 channel)` now replaces the
zero-return placeholder with the complete randomized trail emitter. Its
**123-word / 492-byte slot and 0x98-byte frame are byte-exact in production**.
Semantic C emits 120 words; **56 relocation-aware checked guards and three
instruction insertions** recover the original captures, byte argument views,
allocation and scheduling. No word is omitted or retail instruction range
embedded in the C source.

The independent actual-ELF recount is **4,537 / 5,514 (82.28%)**, Game
**3,864 / 4,841 (79.82%)**, Init 492/492 and Debugger 181/181, zero address drift
and 977 still different. The active 85% goal needs **150 further matches**.
Conversion counts and bytes remain unchanged. Root README changes are only
the two aggregate matching rows; function detail belongs in this note.

## Source and ABI

Owner `conker/src/game/generated_1D92F0.c`, VA151AEAB4..151AECA0,
ROM1DBF64..1DC150. Its sole direct caller is the complete 61-word effect router
`func_151AE890`. The caller ignores the result; the recovered interface has
three incoming words and no meaningful C return. The selector inputs remain
full words. Narrowing their declaration changed the already-exact caller and
was rejected; explicit byte consumption preserves that caller's original code.

The effect constructor's existing recovered definition establishes the complete
18-argument interface: position/velocity pointers, float scale, signed16
duration, byte mode, float time, request selector, opaque byte, two floats,
fade/selector bytes, extra size, two signed16 values, request value, channel
byte and context. Byte-valued incoming selectors are explicitly cast at this
call. IDO leaves their outgoing upper bits unspecified for byte formals; the
checked derivation restores retail's zero-extended byte loads.

Five integer draws, four trig lookups and three real draws preserve their
order and captured lifetimes. The direction uses two narrowed angle bytes;
speed and three velocity components retain the original FP operations and
negation. Unsigned modulo41/101/5 yields duration, mode and request selector.
The four global coefficients are read in their original provider epochs.
The real-draw routine is independently disassembled: it reads no input
arguments, so no stale F12 value is invented as an argument.

The local aggregate holds captured random values, trig results, angle bytes
and the velocity vector. The compiler allocates those aggregate fields four
bytes above retail's homes. The derivation moves only identified local stack
accesses and the submitted vector pointer down four bytes, preserves the
incoming full-word homes and RA slot, restores the two byte argument loads,
and inserts three neutral schedule slots. Both complete instruction streams
are related independently; this is not a mathematical commutativity shortcut.

## Complete relation, execution and controls

All **five final target checks pass fresh in both tools configurations**, with
zero failures, errors or skips: **118.14s primary /
119.991s sibling overlay**. Complete owner compilation retains
all 32 neighboring functions and normalized pools under unchanged O2/g3.

- The complete straight-line symbolic relation compares all **168 private and
  incoming-home bytes**, ordered public/FP/status events, read multisets,
  public byte state, all 13 provider calls and all 18 final arguments. The
  constructor receives exactly 12 exposed velocity bytes and may change them;
  opaque calls may mutate public state, caller-saved registers/status and
  four or 18 outgoing argument homes as appropriate. Unpassed private captures
  remain protected. Required GPR/FPR/RA/stack state is restored.
- An independent scratch-register allocation passes. Six effective controls
  reject wrong mode/channel byte loads, a wrong captured real home, incorrect
  velocity address, wrong 18th argument and broken frame restore.
- Retail/raw/derived each execute **928 guest cases** with the corrected,
  disjoint output fixture. Derived full RAM, provider/private boundaries,
  submitted packet and all **11,136 ordered FP observations** agree. All 123
  retail/derived words and all 120 raw words are visited. The matrix includes
  every azimuth byte, high-word noise, unsigned-remainder boundaries, signed
  zero, NaN/Inf real results and provider mutations.
- The complete 61-word original caller executes **320 cases per stream**,
  visiting every caller word. Early exit, primary emitter and alternate
  constructor paths pass, including 64 primary-emitter cases. Derived full
  RAM/private stack and ordered FP/boundaries agree. A wrong caller selector
  load rejects. The unchanged alternate constructor is an explicitly opaque
  six-argument boundary in this caller test.
- Native32 C is newly compiled at **O0/O2/O3**, each passing **592 finite or
  signed-zero cases**. All public regions, all 13 calls, all 18 final arguments
  and all three velocity words are checked. Four fresh controls reject wrong
  pitch masking, signed lifetime remainder, wrong Z velocity and incorrect
  final context. Native FP status/private stack and nonfinite payload behavior
  are not claimed; guest and symbolic checks establish the target FP order.

The initial native failure exposed a fixture overlap: the mock output address
was the guest stack address. The output was moved to 0x60000 and a disjointness
assertion added. Earlier overlapping-fixture results are not used for credit;
the full guest, caller and native matrices are rerun with disjoint buffers in
both final suites. Candidate C and production data were not changed by that
fixture repair.

The relation assumes ordinary mapped, disjoint public objects/private frame,
stable memory between calls/stores and nontrapping FP. The submitted private
velocity is the explicit alias/visibility exception. This does not establish
arbitrary aliases, literal fault-register state, cycle timing or gameplay.

## Objects, actual Make and linked-image gates

Both real padders produce the independent original body and all 21 bindings.
Twelve GNU links use four code/data layouts and HI/LO carry boundaries, with
the exact linked binding values checked. All previous CSV bytes remain intact;
56 new rows are appended and none is retired.

The object checks reject **141 raw/binding
corruptions, 224 stale-CSV changes and
62 replacement/insertion changes**.
All 120 bound source-word corruptions reject before derivation.

Five actual Make commands compile/pad the complete owner in the independent
shadow. Production Make rebuilds the source/object/ELF/progress; no prebuilt
object is installed. Strict full-image accounting has
**421 changed bytes and zero exclusions**.
Named definitions, any explicitly modeled metadata reorder groups and four
effective symbol/name/data/code corruptions are checked independently.

All other **6,050 function bodies and every function address** remain unchanged.
Exactly one of 698 frozen objects changes, retaining all 32 owner neighbors.
All **189,088 protected data bytes / 720 owners** remain exact. Production ELF
equals the independently predicted image:
`5ce80f63121ecffd6365636cf26773796d034e3ec2b717eaf2350c28a38eaa20`.

Fresh post-install source compilation agrees on all 33 compact owner functions;
the actual production instructions pass 928 guest and 320 original-caller cases,
visiting all 123 words. Prior source/padder/symbolic/native results are reused
at this final stage only with exact task/input/fixture hashes. Production
match-progress, tools-check and an independent actual-ELF recount pass. The
unchanged duplicate generated_12D630 Makefile recipe warning remains.

## Preservation and next work

The 1,573-input baseline links earlier immutable snapshots and copies changed
production inputs plus the ten previous tools additions, with zero live-tree
hardlinks. Exactly four frozen inputs change: source, guard CSV, owner object
and ELF. Classification, retail binary/data, all prior guards and the sibling's
2,434 dirty paths / 339 scoped dependencies remain unchanged. New task files
and actual module imports are separately fingerprinted. Claude calls are 0;
the local caller/ABI and instruction-driven evidence settle this routine.

The host sibling still contains only `.codex` and `recomp_scene`, without a
source/Git checkout to synchronize. It is untouched, including Release/saves.

Evidence is under `conker/build/game-next-151aeab4-private/adoption/`: paired
sealed suites/imports, both padders/GNU links, full relation/controls, corrected
guest/caller/native matrices, actual Make prediction, metadata corruption
controls, production audit/focus and recount. Native Graphify update fails
closed on the reduced scan; scoped AST merging retains all
65020 old IDs and the explicit target reference. This is
not full-corpus re-extraction. Commit tools before consumer source, guards,
notes, aggregate README rows and pin, locally only.

Next inspect **func_151AFEA4** in `generated_1DCA70.c`, a 107-word still-different
placeholder. The 85% goal stays active beyond this checkpoint.
