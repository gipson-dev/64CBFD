# Sequence catch-up loop recovered as guarded C

Date: 2026-11-05. Target `func_1501E2F8`, owner `generated_49D30`.
Source `conker/src/game/generated_49D30.c`; original `conker/asm/49D30.s`.

## Outcome and live sequence behavior

All nine pre-install checks pass in **46.993 seconds**. The nine fresh
installed checks pass in **49.682 seconds**. Actual Make equals
the independently qualified owner and literal complete ELF prediction.

The complete **66-word / 264-byte** routine has no alignment tail and retains
its retail **56-byte frame**, fourteen bindings and all **56 owner neighbors**.
VA is `0x1501E2F8..0x1501E400`; ROM is `0x4B7A8..0x4B8B0`.
The established owner profile stays `-O2 -g3 -Wo,-loopunroll,0`.
Shared headers, compiler profiles and the Makefile are unchanged.

The recovered interface is `void func_1501E2F8(s32 slot)`. Each iteration
reads the live unsigned `D_800C35EA[slot]` status and requires exactly 1.
It compares the signed `D_800C35B0[slot]` timestamp with the signed
`D_800C3640[slot]` limit. A timestamp below the limit stops; equality is due.
If `D_800C3C8C` is nonzero, the routine stores 2 there and stops.

Otherwise it calls `func_1501E81C(0, slot)`, then rereads the original slot's
status. If that helper left status 1, it calls `func_1501E400(0)` and performs
the ordered passes `func_150242F8(1,0)`, `func_1501EC38(0)`,
`func_150242F8(0,0)`, `func_15020EC4(0)`. Subsequent iterations inspect
**slot zero**, regardless of the incoming slot. Timestamp, status and flag
values remain live across helpers; they are not cached or replaced with an
artificial iteration cap. Provider returns are ignored.

## Scheduling proof and original ABI

The semantic C already emits the correct length, frame, register roles,
all branch/call words and complete body from word 20 onward. Seventeen
checked manifest rows restore only the prologue schedule. The closed
15-word cycle and two-word exchange preserve every saved-register store,
constant, address instruction and binding; no instruction is synthesized,
omitted or duplicated. Raw target SHA and all fourteen bindings are checked
before this permutation. All 264 byte corruptions, fourteen binding corruptions
and seventeen actual padder preimage corruptions are rejected.

The simple rotating while form emits 68 words. Explicit header checks and
the recovered flag-zero arm recover 66. Pointer-local screens emit 64 words
and are not adopted. The canonical body is compiled and padded using the
existing no-unroll owner profile, with complete neighbor/pool identity.

A full aligned retail census finds one direct call, ROM `0x466A0`, VA
`0x150191F0`, in `func_15019130`. No aligned target literals or tail calls
are found. The frame coordinator passes 0 and ignores the return register.
Its source declaration is corrected from `s32(s32)` to `void(s32)`.
Both caller sources are compiled and padded independently: **all sixteen
functions, pools and the complete caller object remain byte-identical**.
Its padded SHA-256 is
`6f93d458b6a4991ee00a8d815534c58451aad5b9864fff79c9ceaf0c9533fafc`.

The original eight-word caller window `0x150191F0..0x15019210` is connected
to the target. Its following signed-byte `D_800D23A9` gate independently
controls `func_15087CC0`; poisoned target/helper returns do not control it.
There are 128 cases per body across all provider modes, zero/nonzero byte
patterns, both stack phases and two poisoned returns.

## Guest, native and connected-helper qualification

The focused suite supplies these distinct receipts:

* **576 cases per body** execute original, natural and fitted instructions
  against an independent live-state contract. Signed extremes and ties,
  inactive/non-one status, flag handling, helper deactivation/reactivation,
  three passes, live timestamp changes and the slot-zero restart all pass.
* **2,048 additional original/fitted cases** sweep every active and flag
  byte in both slots and stack phases. A nonzero flag becomes 2 only after
  the active and signed timestamp gates permit that store.
* **129 alias layouts** cover 120 private-frame layouts and nine overlapping
  global layouts. Original/fitted RAM, registers, calls and traces agree.
  Deliberately overwritten saved-register/return homes end at the same
  corruption boundary; a normal ABI return is not claimed for those inputs.
  One global alias stalls. It and a separate unchanged-provider case match
  bounded twelve-call prefixes, without claiming termination.
* **91 fired access-prefix cuts** compare complete state and ordered memory
  traces. Natural C private-stack/fault ordering is not claimed; the checked
  fitted instruction order supplies that qualification.
* The original **26-word `func_1501E81C` prefix** runs through its first
  `func_15169040` submission, verifying the 72-byte frame, local command byte
  and command 16. The original **28-word `func_1501E400` prefix** runs through
  `func_1501E1B4`, verifying its 40-byte frame, saturating countdown and
  slot-zero timestamp copy. Together 24 cases per body execute these prefixes.
  Complete callees and parents remain outside these bounded observations.
* **Nine independent GNU links** retain original, natural and fitted
  artifacts at three layouts. All fourteen bindings, HI/LO carry edges and
  fifteen cases per body pass.
* Native32 O0/O2/O3 pass **1,728 positive executions** through typed and
  direct calls, with UBSan and complete call/observation hashes checked
  against the guest-qualified contract. Eleven native and eleven separately
  compiled IDO controls reject wrong status, signedness, ties, flag values,
  post-call reload, slot reset, current-slot argument, phase, order and final
  helper. Native array inputs stay within the two-slot domain.

All **65 reachable words** are visited. The duplicate literal at `+0xD8`
follows the unconditional loop branch and is unreachable from the function
entry; it remains statically byte-exact and corruption-checked. The remaining
slot is not silently excluded from matching or progress.

Fixture corrections are separate from the recovered production body. The
native row initializer needs explicit nested-array braces under `-Werror`.
Private saved-register corruption is an expected boundary, and equal aliased
timestamp/limit storage can prevent progress. These are recorded as such;
no production iteration limit or shared oracle change is introduced.

The nineteen fresh padder, relocation, matcher and protected-layout checks
pass in **7.081 seconds**, and `make tools-check` passes. Unchanged suites
are reused through body/binding/pool identity rather than claimed freshly
executed. Routine work uses zero Claude calls. No FCSR, hardware or host
gameplay acceptance is added. IDO/GNU tools use the documented REA MIPS
adapter fallback without reinstalling or reconfiguring anything.

## Immutable inputs and production image

The snapshot freezes **95 files**, including all headers, target/caller
sources and objects, original target/caller assembly, retail input, ELF,
code binary, guard history, layout, progress, Makefile, linker and graph.
Private receipts are under
`conker/build/game-sequence-catchup-1501E2F8-match/`, with adjacent source
screens. The existing generated-owner and ordinary caller padders are used.

All **6,052 function addresses** remain fixed; only the target body changes.
All **189,088 protected Game bytes across 720 owners** remain exact.
The literal complete ELF prediction accounts for **207 changed bytes** in
the target and its 12-to-264 symbol extent, with **zero additional metadata
corrections or excluded bytes**. Five independent image corruptions cover the ELF header,
target, next slot, symbol extent and file tail. Actual Make follows the guard
manifest dependency through its broader rebuild. Frozen other inputs and
every prior manifest byte stay unchanged; exactly seventeen rows are appended.

| Artifact | SHA-256 |
| --- | --- |
| Natural target | `30cb1ad4e92e7bf5d44b9abc59fd6ea1799ea95ee187eb91c28d262ae1c462c5` |
| Retail target | `285bb3184d53468f915148446118bf0c9b799a8610842d9b44a51c6c3c8bd2fc` |
| Frozen predecessor ELF | `efd54ec9785d8510c55ccd84cde8d252ccd096f554733cef46b0d34f35de9ee7` |
| Production padded owner | `5f0ebeb715813f8d64cc4cae92f421b2f5a14f8c29ca4cd4c125149b99f69767` |
| Production complete ELF | `cb8850d1e353bf3ac38ebcc8ed36d7852472aa46f11eb6f1d98aaa53a6e36b90` |
| Production code binary | `88fdd1eab565f6c79b8821c0b33e034fb36dd40bc37f0ef78c006102ebac7a2f` |
| Appended guard manifest | `98c78a54647943d6bad989031ecb0256e24cf2247923f8fd992118dc7ba00810` |

The inherited duplicate `generated_12D630` recipe warning remains.
`make -C conker all` produces the binary and returns 2 at the expected
overall retail checksum mismatch for the incomplete decompilation.

## Baselines, progress and continuation

Main baseline is `79e847475a8dd408d8def74926d0146e5ef9c34e`;
mounted tools baseline is `629519a958dd186c12dcad8d9c4042ec2bddf3e8`.
Both start clean. The separate sibling tools checkout is untouched; its last
recorded checkpoint has six tracked edits and 2,428 untracked files at
`ddbdd16b53ce60b054fb6e11bf0649a41f48375a`. No fresh sibling qualification
is claimed. Host-port and frozen Release artifacts remain untouched.

The actual-ELF recount reports:

| Section | Byte-exact / converted | Match | Drift | Different |
| --- | --- | --- | --- | --- |
| Total | 4,172 / 5,512 | 75.69% | 0 | 1,340 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Game | 3,499 / 4,839 | 72.31% | 0 | 1,340 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

Converted inventory stays 5,512/6,046; root README changes aggregate rows
only. The 80% threshold is 4,410/5,512, leaving **238 more** exact functions.
Fresh ranking selects **func_150859AC** next. Keep `func_150A76F0`,
`func_151F8870`, `func_150A613C`, `func_150AE280`, `func_15115F68`,
`func_151AE2BC` and `func_150A6760` as separate documented boundary cases.
Keep the wider 80% goal open.

Mounted tools are committed first as
`21f0a0d0fc5646dd37f3028eca83a2b015fb4810`
(`test(game): qualify live sequence catch-up loop`). The consumer includes
that pointer, the guarded C, the void caller declaration and documentation.

The ordinary AST-only Graphify update refuses its smaller 24,947-node
replacement, preserving the existing 58,741-node graph. The nine-path scoped
refresh retains 58,738 old IDs, removes three relocated update-log IDs and
adds ten IDs, including seven note nodes. Each removed node has a unique
replacement with the same label and source path; **zero nodes outside changed
paths are lost**. The result is **58,748 nodes / 112,504 links / 5,132
communities**, SHA-256
`9f2d124a54261ffe77c3971a6321abbfb38e6a1749f9b02e89d56d82d07c4874`.
The 31,816 nodes retained from 3,754 files outside the current scan corpus are
preservation evidence, not a fresh full-corpus extraction. No force overwrite
is used. A final scoped receipt refresh verifies unchanged topology after
these paragraphs; they add no headings.
