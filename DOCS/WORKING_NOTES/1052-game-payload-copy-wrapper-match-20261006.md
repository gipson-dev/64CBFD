# Game Payload-Copy Wrapper Match

Date: 2026-10-06. Starting checkpoint: `f4be4df3`.

Recover `func_151407D0` in
[game_16DC80.c](../../conker/src/game_16DC80.c): **53 words / 212 bytes**,
VA0x151407D0..0x151408A4, ROM0x16DC80..0x16DD54, frame **0x40**. Replace
its false no-argument zero-return C stub. Existing O2/g3 emits **43 slot words
directly**; ten expected-word guards normalize one closed success schedule,
its branch displacements and counter HI16 relocation. No inserted/omitted/
trampoline words, new profile/data/layout or broad conversion. Production
linking, full slot audit and the 92-test post-link regression pass.

## Recovered Contract

Ten arguments: source pointer, signed-word byte count, descriptor pointer,
unsigned-byte kind/mode/first/variant, signed-byte selector, unsigned-byte
channel and signed-word context. Register arguments retain retail home stores;
byte arguments retain their low byte with high incoming bits. Selector uses
the retail post-copy LB before its low-byte store. Recover the owner-local
prototype; no invented leading floats from old commented callers.

Before allocation, set descriptor byte+1 to3 and OR flags word+0x40 with
0x40400000. Forward descriptor/kind/mode/first/**setup=1**/variant/size/channel/
context to `func_1513D524`. Failure returns null, retaining descriptor and
callback mutations, with no payload copy or wrapper counter increment.

Success captures allocation+0x110 as payload and copies the live original
source/count arguments with `memcpy`. Reload payload and allocation from
separate stack slots after the call; memcpy's returned V0 is not the allocation.
Clear payload word+0x44, publish selector byte+0x59, conditionally increment
the **live** `D_800DC9F0` word and return allocation. Unsigned-word increment
preserves defined 32-bit native wrap. Retain clear-before-counter-read when
counter aliases payload+0x44. No count/bounds/overlap/safety clamp added.

Existing `func_1513D524`: **28 words / 112 bytes / frame0x38**,
VA0x1513D524..0x1513D594, ROM0x16A9D4..0x16AA44. False void/integer-descriptor
C ABI discarded the constructor pointer return although retail retains V0.
Recover void-pointer descriptor/return in
[functions.h](../../conker/include/functions.h) and owner definition; explicitly
cast the fixed table address to the constructor's existing word argument.
All28 instructions remain direct/unchanged, no guards. No other live C callers
found; old commented calls are not ABI authority.

## Compiler And Schedule Evidence

[Driver](../../tools/experiments/game_payload_copy_wrapper_candidates.py):
**six forms x four profiles plus four callee ABI forms x four profiles =40
controls**, real SDK layouts/fixed symbols, empty diagnostics. No installation
by the driver. Selected explicit success join: O2/g3 **53/0x40/10**
(words/frame/differences); O2:54/0x40/31; O1/g3:60/0x38/59; O1:60/0x38/60.
Structured success/failure gives54/0x40/19; early-null53/0x40/17;
captured selector53/0x40/12. Typed payload and volatile counter do not improve
the selected ten. Callee old-void, word-descriptor return, void-pointer and
byte-pointer forms all give **28/0x38/0** under O2/g3, equal to retail and
production; O2 has13 differences, O1 variants30 words/29 differences.
No alternate profile installed. Earlier ignored exploration:128 outer controls
plus16 callee controls under `game-list-key-sort/next-payload*`/`next-return-abi/`.

Tests derive normalized instructions from an explicit old-index to new-index
permutation, not pasted retail replacements:

`35->36, 36->37, 37->35, 38->39, 39->38, 40->41, 41->42, 42->43, 43->40`.

Other indices fixed. Recompute displacements to mapped original targets:
allocation branch27 maps40->41; branches38->42,40->49,42->48 become
39->43,41->49,43->48. Register fields/arithmetic/accesses/count unchanged.
Selector publication remains before success counter join; failure bypasses
payload accesses. Move **R_MIPS_HI16** raw+0xAC to retail+0xA0; **R_MIPS_LO16**
stays+0xB0. Guard both expected/replacement relocation lists explicitly.
Actual compact-object/padder/assembler/link test checks raw words, both
relocation positions, 212-byte symbol and all53 linked words. Single-function
section-alignment nops outside the symbol are checked zero, not slot content.

## Qualification

[Nine tests](../../tools/tests/test_game_payload_copy_wrapper_match.py):

- Raw shape, closed schedule/branch remapping, direct43 words, relocation move,
  complete independently padded/linked slot.
- **5376 ordinary guest cases/two raw bodies**: seven sizes0..128, four flags,
  six source/descriptor/payload/counter aliases, success/failure, callback
  mutations, two SP phases, four signed-byte boundaries/high incoming bits.
  Independent full external storage/call/return reference; ordered external
  traces agree. **All53 words** visited in each body; saved GPR/FPR/SP/RA and
  misleading memcpy V0/clobbers checked.
- **65536 kind/mode byte pairs/two bodies**, diagonal first/variant/selector/
  channel sweeps/high bits. Ten null-allocation size/phase boundary cases
  transport negative/near-overflow sizes without invalid native copies.
- **72 post-copy guest join cases** mutate saved allocation, selector home byte
  and counter: zero/original/alternate return, byte boundaries/wrap/two phases.
  Zero saved result suppresses increment but preserves payload stores; no
  assumption the redundant-looking branch is unreachable. Private-stack probes
  are instruction evidence, not native alias/allocator claims.
- All40 persistent compiler controls, empty diagnostics.
- **1440 actual wrapper->constructor guest cases/two outer bodies**: recovered
  28-word callee/114-word constructor instructions, failure/flags/phases/live
  callbacks/source-descriptor/source-actor aliases. Include88-byte payloads;
  distinguish constructor/payload copies by destination, not length. SDK and
  allocator leaves are bounded hooks, not every downstream/dispatch instruction.
- Ten compiled negatives: stub, descriptor byte, flag bit, setup, payload
  offset, copy length, clear offset, selector offset, early counter and payload
  pointer return. Each changes actual memory/call/return evidence; unsupported
  instructions are not negative detection.
- **132352 native whole-storage cases**:1280 size/flag/alias/failure/mutation
  cases plus131072 kind/mode/failure cases. Actual outer C, pointer-return callee
  and constructor compile together in freestanding 32-bit C with bounded SDK/
  allocator hooks. Independent expected descriptor, entire actor/source/counter
  storage, callback order, selectors, counter wrap, zero-length copies and
  allocation return checked. Counter may alias payload+0x44; source may alias
  descriptor, constructed actor header or counter storage. Native memcpy returns
  null deliberately to catch helper-return adoption.
- Production body/local prototype/callee definition/header, complete53/28-word
  slots, exactly ten guards with relocation metadata, total10695, no callee
  guards.

Boundary: ordinary nonoverlapping valid copies/allocation-backed payloads.
No arbitrary overlap, payload/private-frame/home-byte aliases, negative native
copy counts, corrupt pointers, all allocator/dispatcher paths, hardware
exceptions/FCSR, gameplay or sibling adoption claim. Local signed-LB/mapped
oracle extension isolated; previously qualified shared oracles unchanged.
Fixture import/MRO/section-padding/descriptor-span/unused-variable issues fixed
before final passes; production behavior was not changed to satisfy them.

## Linked Audit

Build/link/progress/audit pass. **6059 fixed slots**, only `func_151407D0`
changes; all addresses/sizes fixed. Target SHA-256:
`331875920d90b004baacb5509cafe36b193e9a8b9256cee369d040f741850704`.
Protected `.init`, `.init_data`, `.debugger`, `.game_data` unchanged;
**720 owners/189088 bytes** retail-exact. All **10685 existing guards**
preserved in order plus ten, total**10695**. Callee, constructor, sorter, both
quad builders, corner/attribute helpers, owner/buffer backend unchanged/exact.
Callee SHA-256:
`398493762222268ece48450d0d703784944e641a609effc573ece723bf5202d8`.

Compile baseline/current owners against their corresponding header snapshots:
`game_169510` **45->43 warnings**, exactly two false callee argument ABI warnings
removed; other normalized entries identical. `game_16DC80` **0->0**.
**Zero new warnings**. Shared-header dependency rebuild finished before audit;
no partially relinked ELF reused.

Converted unchanged:5464/6042, Game4791/5321, bytes85.57% total/84.89% Game;
false stub already counted as C. Exact **3330/5464 (60.94%)**, Game
**2657/4791 (55.46%)**, **2134 different**, zero drift; Init492/492 and
Debugger181/181 unchanged. README aggregate numbers only; details in docs.
Seven older tests advance only global guard count; own contracts unchanged.
All **92 post-link regression tests pass in 901.823 seconds**, no skips.
Tools/compileall/diff checks pass; **34 docs/3377 relative links/zero broken**.

Ignored receipts: `conker/build/game-payload-copy-wrapper/measurements.json`,
`build.log`, `audit.json`, `after.json`, baseline/current diagnostics;
behavior/relocation/native/negative objects under `game-payload-copy-wrapper-test/`.

## Cross-Project And Next Work

Read-only sibling `64CBFDOGL/recomp_out/.c` already contains retail-translated
`func_151407D0`, not a false zero-return placeholder; no src override found.
No mechanical guest C import/regeneration or executable/runtime adoption
inference. No sibling source/build/save/frozen Release change, runtime or push.

Next `func_151412BC`: **96 words/frame0x18**, VA0x151412BC..0x1514143C,
ROM0x16E76C..0x16E8EC. Scan four indexed buckets in each of two0x1A0 rows,
traverse next+8, flags+0x58 bit0x2000 clears halfwords+0x15C..0x162; bit0x10
enables per-channel signed X/Y bounds and live unsigned-halfword grid lookup.
Invalid coordinates store0x7FFF. Retain live channel bound, width capture for
row multiplication, byte wrap and short-circuit Y access. **96 ignored compiler
controls**: initial24, pointer/scope40, loop/result32; all completed with empty
diagnostics. Direct-fields O2/g3 **96/0x18/53**, ordinary payload97/0x18/79.
Explicit byte increment gives96/0x18/52 but changes backedge/branch-likely shape;
not selected as a claimed closed register rewrite. Pointer-row/register/for
variants do not improve direct53; result-type controls add words, not ABI proof.

`next-grid-behavior.py/json`: **1728 cases/two raw bodies**, complete external
storage and ordered accesses agree, **95 reachable words** in each; do not
artificially execute unreferenced instruction VA0x151413DC. Four channel bounds,
three widths/three heights, four flag patterns, ordinary/counter-field/grid-
field alias layouts, empty/nonempty lists and two SP phases. Strict mapping,
signed X/Y boundaries, live bound after stores, live grid overlap and saved
registers checked. Initial fixture incorrectly placed grid at emulator STACK;
move it to0x50000 before the completed receipt, not a production fix.
Important incomplete ABI evidence: raw void candidate ends **V0=0x800DD190**,
retail **V0=4**. The inspected caller `func_1501878C` immediately overwrites V0,
but that does not prove every caller or a recovered return type. No next native,
complete ABI/normalization/production qualification or installation. False
scalar table/pointer declarations need owner-local interpretation before any
header/data change. Ignored next scripts/receipts under this checkpoint's
`game-payload-copy-wrapper/next-grid*`.
Large adjacent `func_151408A4` also remains unrecovered; not owner completion.
