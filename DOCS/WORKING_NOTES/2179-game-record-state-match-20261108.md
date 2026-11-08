# Record State and Viewer Update Match - 2026-11-08

`func_150A09D0` is byte-exact across all 209 words with its original 64-byte
frame. Total **4,248 / 5,513 (77.05%)**, Game **3,575 / 4,840 (73.86%)**,
Init **492 / 492**, Debugger **181 / 181**. Address drift is zero and 1,265
converted functions remain different. Another **163** exact functions reach
4,411 / 5,513 and the active 80% goal. Conversion totals are unchanged.

## Source and interfaces

Owner `conker/src/game/generated_CDE80.c`; VA 0x150A09D0..0x150A0D14,
ROM 0xCDE80..0xCE1C4, 836 bytes. The normal IDO 5.3 O2/g3/MIPS2/O32 profile
and Makefile remain fixed. The entry is `void func_150A09D0(s32 unused)`.
Retail stores its incoming word into its home at entry, then never reads it.
Tests vary the full word, preserve that store and restore saved registers.

The aligned scan of pristine `conker/conker.us.bin` finds **two** direct calls: ROM 0x462B8 in the restored
`func_15018DFC`, and ROM 0x1567B8 in the larger actor routine at 0x15129308.
The earlier assembly-only handoff missed the first because its assembly file
had already been replaced by C. Both load D_800BE9E4 in the JAL delay slot
and ignore V0 before the next call. No aligned entry/interior pointers or
interior J/JAL targets were found. Connected tests execute the original
5-word wrapper window and 44-word actor window, including the actual A0 LUI,
copies/stores, delay-slot load, return destination and post-call actor indexing.

A local `void func_150A09D0(s32)` declaration repairs the implicit C call in
`src/game_45B80.c`. Its complete 16-function owner is audited: all raw code,
relocations and pools are unchanged; three existing warning-712 diagnostics
are identical apart from source locations; no new diagnostics. Its actual
three-command Make recipe reproduces the entire original padded object byte
for byte. The compact object's debug/source metadata changes with the added
declaration; no debug metadata exclusions are used in the final ELF test.

The local 52-byte record exposes field20 as an unsigned state word. A private
9A0-byte viewer overlay names float radius/x/y/z at 938/93C/940/944 and bytes
948/949. No shared SDK header is changed. All 27 raw and padded neighbors in
the recovered owner remain fixed, including existing users of field20.

## Recovered behavior

The unsigned outer scan uses the live D_800D3094 count and D_800D3098 table,
with 0x34-byte records and class `flags >> 2`. Other classes skip the work.

- Class 2: state 1 becomes 2 through XOR 3. State 2 submits the upper half
  of field1C, signed origin coordinates and field18 to func_1000FC18, reloads
  the live record base, then clears state. Independently, gate byte
  D_800C35EA must equal 1; an accepted collision query on actor zero then
  invokes func_150A23E4 using a newly reloaded record address.
- Class 7: flags low bits 3 clear state; otherwise state 1 becomes 2.
  State 2 submits the subtype/zero/field18 command. Only success proceeds to
  subtype/100/field1C using a fresh record address. Only success again clears
  the state through another fresh address. Other states remain unchanged.
- Class 4: subtype 9 skips its countdown. For other subtypes, a nonzero low
  byte of field1C becomes zero when disabled, or decrements when enabled.
  Upper bits survive. Reaching zero reloads the record, clears the indexed
  byte in D_800DDF5C, rereads field1C through that retained pointer and retains
  its upper 16 bits. A fresh record/subtype lookup falls into class 0.
- Class 0 and the class-4 tail: enabled subtype 12 publishes signed origin
  coordinates and radius as floats, then enables the viewer and copies the
  low field18 byte. Viewer indices run from zero through the live signed
  D_80082FA0 bound, inclusively. Each iteration computes one viewer pointer
  from the live D_800DBFF0 base. The record base reloads before every field
  load; the field18 word is read before either output byte is written.

The count reloads at the same class exits. Provider changes to count, record
base, fields, gate and viewer state remain visible at their original boundaries.

## Audio width audit

The established SDK signature remains
`void func_1000FC18(u16, s16, s16, s16, u16)`. The correctly typed caller
already emits retail's complete word store into the fifth O32 argument home.
The actual 72-word SDK callee reads only the low half with LHU at its SP+4A.
Twenty-one connected SDK cases vary upper-word padding, all five comparison
fields, zero/nonzero sound handles and a handle callback that changes the
live SDK count. The complete fifth word survives the caller while only its
low 16 bits affect the SDK comparison. No Init source, prototype or body
is changed. Other audio/collision services remain bounded test hooks.

## Derived match and owner protection

Raw C SHA256:
`f067b4a5d4110bbcdfc595661697af370bddd20ec7cf15dfc6d7d6d1b8ba71b8`.
The source emits every semantic operation. Sixty fail-closed expected-word
and relocation guards normalize a closed S5/S6 role swap, viewer counter,
offset and temporary lifetimes, commutative equality/pointer-add operands,
and independent loop-register scheduling. The count-address LUI moves ahead
of the viewer block, and the two register increments move after its stores.
This is an instruction permutation and register reassignment; no new loads,
stores, arithmetic, calls or branch destinations are supplied by the guards.
All 25 bindings are checked and relocated with their owning instructions.

All 209 raw word corruptions, 25 altered bindings and an altered inherited
CSV prefix fail qualification. Every guarded position independently rejects
a stale instruction and unexpected relocation. The raw owner's pools and
24-byte register metadata remain identical. Production and strict padders
agree on all 28 functions and pools; all 31 original case labels are retained.

The frozen baseline contains 106 inputs. The actual five-command recovered
owner recipe and three-command caller recipe are executed in isolated output
directories. GNU links also verify original and rebased symbols, including
signed LO16 carries. The literal full-image predictor permits exactly **612
changed bytes**, comprising this restored function and its symbol size.
There are **zero exclusions**. All 6,053 function addresses, all other bodies,
720 protected data owners and 189,088 protected data bytes stay fixed.

## Execution and production evidence

Each tools configuration passes six focused checks. The mounted tools and
independent sibling configuration run sequentially against matching fingerprints.
The sibling's 2,434 inherited dirty paths and HEAD are preserved. Both copies
also pass a fresh shared-tool smoke check; three unchanged synthetic shared
regressions per copy are explicitly reused by exact source hashes.

- Guest model: **571 cases** on retail, normalized and
  raw C words; all **207 reachable words** execute. The two redundant words
  at 0x150A0B10/0x150A0BB8 follow unconditional branches and have no incoming
  branch targets. They are preserved and are not falsely counted as executed.
- Callers: **12 wrapper cases** and
  **8 actor-window cases**, plus
  **21 SDK cases**. Saved GPR/FPR lifetimes
  and both stack phases are checked.
- Fault prefixes: **353 executed memory cuts**
  compare complete literal states for retail and normalized words. Raw C is
  checked for public semantics, without claiming identical register scheduling.
- Native 32-bit: **372 cases** each at
  O0/O2/O3 with trapping UBSan and actual SDK record/view/pointer sizes.
  Callback streams and mutable-field digests agree with the independent model.
  Twelve semantic negative controls fail effectively, including stale base/count,
  unsigned coordinates, wrong transition, timer mask, gate, subtype exception,
  command selector, shared tail and exclusive viewer bound.

Production rebuilds exactly two C owners. The recovered owner has no C
diagnostics; the caller retains its three existing warnings. The actual ELF
equals the literal prediction. `make all` retains the existing whole-project
checksum failure while unmatched functions remain; its expected exit 2 is
recorded separately from the successful build and fresh matching recount.
`progress.csv`, compiler profiles, Makefile and all preceding guard bytes
are unchanged. README changes contain aggregate status rows only.

Production ELF: `e89916b8a4729061901753c9c5127be78c45c553ea5243e003d3d859f48c58aa`.
Binary: `569202041027ec2dc6d325528289a449030932e35608d1826e1c19e4dae7d071`.
Recovered owner: `741c968b594320ecf6c9987aa207670ef7fc6386f6d2f0addd300e1330355ad6`.
Guard CSV: `2458418c897988981b244e7d15fba669c3502d56ad2f3f84a40a32d10af856e2`.

WSL reproduction from the decomp root:
`python3 -m unittest tools.tests.test_game_record_state_150a09d0_match -v`.
Canonical receipts: `conker/build/game-record-state-150A09D0-match/`.
Tools are committed first, then consumer source/guards/docs/aggregate rows/pin
locally. No push. Graphify receives a scoped refresh with old-node retention;
this is not a full-corpus extraction. The full 80% goal remains active.

Next qualify `func_150A25D4`, the 110-word record-subtype dispatcher, including
its 11-entry protected jump table, six-word caller packet and SDK services.
No matching credit is assigned to that next target.
