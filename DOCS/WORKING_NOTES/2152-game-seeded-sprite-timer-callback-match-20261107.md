# Seeded sprite timer callback matched

Date: 2026-11-07. Continues [Note 2151](2151-game-below-height-effect-callback-match-20261107.md)
from consumer `d74c0ca3410a9a8e00944aeca674ebaed740ccc0` and tools
`463d686327e00ef999f1d83ee0a8a2fa66493833`. One fully qualified Game match
is added toward the active 80% total goal.

## Complete callback and live actor home

`func_15193390` in `conker/src/game/generated_1C0840.c` replaces its
zero-return placeholder with the complete **73-word / 292-byte** routine.
VA is `0x15193390..0x151934B4`, ROM `0x1C0840..0x1C0964`. Its recovered
interface is `void (u8 *volatile actor)`. The caller ignores the return.
The top-level qualifier is an explicit O32 argument-home carrier: it retains
the original incoming actor slot and three live reloads across providers.
It is not evidence that the original C declaration contained `volatile`.

The routine zeroes a real 168-byte `SeedSpriteDescriptor` whose first 128
bytes are eight SDK `Vtx` records. Its typed source record at actor+0x28
contains signed X/Y/Z/height halfwords and a variant byte. If the converted
height equals the live float `D_800A81B0`, initially bits `0xC61C4000`
(-10000), the output height becomes Y minus 200 and the input variant is
cleared. Otherwise the captured input height is copied. The subtraction
converts through `s32` before narrowing to the SDK halfword: Y minus 200
can be below -32768, while remaining safely inside the signed 32-bit range.

The descriptor receives the three coordinates, zero parameters at 0x92/94,
mode 15, texture index 0x45, parameter 0x86 = 10, the then-live variant,
flags 0x4880 and parameter 0xA4 = 128. Offset-based names are retained for
fields whose meaning is not established; parameter 0xA4 is not asserted to
be alpha. The initializer `func_1516865C` separately receives the proven
RGBA arguments 255/255/255/128. The constructor `func_15168800` then receives
the descriptor and live actor bytes at 0xC and 1. Its result is ignored,
including NULL. The integer RNG runs unconditionally afterward; a final
live actor-home reload selects the signed timer at +0xE, set to
`((u32)rng & 127) + 100`, range 100..227.

The descriptor, input and callback ABI are documented in the source with
local support types and provider declarations. No shared header changes
are needed. The other owner function remains its existing placeholder.

## Derived frame and branch guards

Normal O2/g3, MIPS2/O32 emits all 73 words in a 208-byte frame. Six exact
expected-word guards restore the original 216-byte frame and physical
incoming actor home:

| Offset | Raw C | Retail | Meaning |
| --- | --- | --- | --- |
|0x0|0x27BDFF30|0x27BDFF28|Allocate 216 rather than 208 bytes|
|0x8|0xAFA400D0|0xAFA400D8|Store actor in the incoming argument home|
|0x18|0x8FA200D0|0x8FA200D8|Reload actor after descriptor zeroing|
|0xE8|0x8FA200D0|0x8FA200D8|Reload actor after initialization|
|0x104|0x8FA900D0|0x8FA900D8|Reload actor after the RNG|
|0x118|0x27BD00D0|0x27BD00D8|Release the matching frame|

The descriptor remains `[SP+0x28,SP+0xD0)` with three address escapes:
zeroing, initialization and construction. It is disjoint from saved RA at
0x1C and the outgoing alpha argument at 0x10. Retail's last eight frame
bytes are unused. The incoming home remains physically caller SP+0 in
both layouts. The raw routine has 21 direct SP memory instructions,
including four home accesses and one unreachable private store; 17 are
private-frame accesses. No artificial padding object is introduced.

Sixteen further guards rotate the complete sentinel branch diamond,
words 21..36, joining at word 37. Raw C uses BC1FL with the unchanged
height store in its likely delay slot; retail uses BC1TL with the Y load
in its likely delay slot. Each executed path retains the same data-access
sequence. The conversion block, false-path store and variant clear are
derived from emitted instructions and moved as one closed transformation.
The raw unreachable duplicate store at word 36 becomes retail's unreachable
duplicate load at word 25. Neither is omitted. Branch targets, opcodes,
frame/home accesses and the exact raw body hash are checked before guards
can be generated. All six relocation bindings stay at their original
offsets; no GPR-allocation guard is needed.

Raw frame/PC identity is not claimed. Guarded instructions are literally
retail and their complete private state/access prefixes are independently
compared. Both raw and padded neighboring bodies remain fixed. Raw pool
changes are restricted to GPR mask 0x80000004 -> 0xA300FFFE and FPR mask
0 -> 0x000707F0, including the same fields in `.options` when present.
All other allocatable pools/relocations stay fixed; padded pools are literal.
The owner has zero inherited or new C diagnostics. Makefile and compiler
profiles are unchanged. Natural source/profile screens that moved the
neighbor or failed extent/lifetime gates remain private and uncredited.

## Focused qualification and limits

Seven checks pass both before and after installation in both tools
configurations. All new modules and imported helpers are fingerprinted;
the sibling executes its own available helpers through a disposable new-
module overlay. Its missing `alloc_pools`, `RngInstructions` and
`initialize` helpers use explicit, hashed mounted fallbacks read-only.
The 2,434 inherited sibling dirty paths are independently frozen and retained.

* 884 guest cases per body compare retail, guarded C and raw C with an
  independent byte-memory reference. Cases cover all 256 variant bytes,
  four source/heap overlap layouts, signed extrema, exceptional ordered
  comparisons, provider mutations and guest-only actor-home redirection.
  72 of 73 target words execute; the duplicate load is unreachable.
  Guarded full machine state and traces agree. Raw public effects and
  packets agree with private descriptor addresses canonicalized.
* 120 cases per body connect 387 original helper words: bzero's 40-word
  slot, the 105-word initializer, 28-word constructor, complete 196-word
  bcopy slot and 18-word integer RNG. Coverage is respectively
  33/94/28/55/18 words. The allocator stays bounded. Fixed descriptor flags
  do not cover every generic initializer branch; bcopy exercises the
  aligned forward 168-byte path. Allocation success and NULL both retain
  the unconditional RNG/timer update.
* The copy fixture initially used an incomplete 11-word prefix. It was
  corrected to the complete original 196-word window before all fresh
  receipts. Its signed ADD has a narrow, trapping emulator implementation
  with positive and overflow controls; no shared executor was changed.
* 256 cases execute all 45 words of the original `func_15149264` timer
  caller, ROM 0x176714..0x1767C8. The callback slot is
  `D_8008A4C0[1]`, address 0x8008A4C4, ROM 0x22EF84. The caller decrements
  enabled timers, optionally updates the actor, dispatches a negative timer,
  then checks whether cleanup remains necessary. Reseeding prevents cleanup
  of the original actor; guest-only home redirection can leave that actor
  negative and trigger cleanup. Other update/cleanup providers are bounded.
* 116 fired access cuts, including ten delay-slot cuts, compare complete
  guarded registers, private bytes, PC and access prefixes. Raw fault-PC
  identity and portable C stack-home poisoning are not claimed.
* O0/O2/O3 SDK native32 builds each pass 576 independently generated
  little-endian Python byte fixtures with layout assertions and UBSan traps.
  Five compiled negative controls fail: former stub, height rule, timer
  mask, initializer alpha and stale priority. A separately compiled guest
  nonvolatile actor-home control fails under home redirection. Native
  cases cover finite arithmetic and SDK short narrowing, not portable
  stack-home mutation.
* Two independent GNU links/rebases, including signed low16 carry, preserve
  complete instructions/bindings. Four header/body/symbol/string corruptions
  are rejected by the strict image gate.

FP exception flags, NaN payload propagation, hardware traps and gameplay
acceptance are outside these bounded models. Fresh shared smoke checks pass
in both tools copies. Three unchanged shared regression receipts per copy
are reused explicitly only after exact helper/test fingerprint checks
against Note 2151. Routine local evidence suffices; Claude calls: zero.

## Actual Make and full-image recount

The 113 frozen inputs include complete helper assembly, SDK headers, IDO
executables, ROM, linker, layout, guards, Makefile and predecessor ELF.
Actual Make recompiles only this owner with the normal O2/g3 profile and
equals the independently predicted full ELF: **267 changed bytes, zero
exclusions**. Besides the target body and its symbol extent 12 -> 292,
the prediction reconstructs two closed symbol/string serialization groups:
`(D_800A81B0,D_8009F640,D_80096240)` -> order (1,2,0) at ELF 0x2B7B6C,
and `(func_150F34A0,D_8009E480)` -> order (1,0) at 0x2C58AC.
The unequal string lengths and all `st_name` offsets are predicted;
named definitions otherwise agree. No metadata section is excluded.

All 6,052 function addresses remain fixed and only this body changes.
All 189,088 protected Game bytes across 720 owners remain exact. The
conversion CSV is byte-identical because the previous stub already counted
as converted C. Compile/link pass. `make all` reaches the expected
nonmatching image checksum, exit 2; it is not a compilation failure.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
|Total|4,222 / 5,512|76.60%|0|1290|
|Game|3,549 / 4,839|73.34%|0|1290|
|Init|492 / 492|100.00%|0|0|
|Debugger|181 / 181|100.00%|0|0|

The 80% threshold is 4,410 / 5,512: **188 additional exact functions**
remain. Root README receives aggregate rows only; this note contains the
function narrative and four current indexes receive a concise lead.
Refresh Graphify with old-node retention checks, retaining excluded-but-
existing legacy nodes fail-closed. This is not a fresh full-corpus
extraction. Commit tools before source/guards/docs and the exact consumer pin.

| Artifact | SHA-256 |
| --- | --- |
|Production ELF|`c1252d3127415b7cf315d97adee1d1a3a03255f07d9b40417755c8132e3015ad`|
|Production binary|`275845f3863d38b21958be7a1ae6c08fc6a6d77506a3fd3f10afe49a8ba3d1b1`|
|Padded owner|`6f86ce430d722b072d7d52ebe8a9c933f8e4c8e20a4a719e1abeb92151e9cad5`|
|Guard manifest|`66ad0ff1fb837b102250469a08f2fa8f7e862bde40868b3b8f0357346ca8571b`|

Separate qualification, pre/post focused suites, shared smoke/reuse,
production, graph retention and post-commit receipts remain ignored under
`conker/build/game-seeded-sprite-15193390-match/`.

Next: **func_15191400**, the 72-word active-entry reset loop in
`conker/src/game/generated_1BA1D0.c`, VA 0x15191400..0x15191520,
ROM 0x1BE8B0..0x1BE9D0. It remains a genuine zero-return placeholder:
69 retail word differences before qualification. Recover its 60-entry
scan, live actor-slot reads, unsigned random modulo, flags and final
720-byte clear with its complete owner/caller checks. Preserve established
handwritten/hidden-ABI boundaries, explicitly frozen 150A6FA0/150A76F0,
private inputs/saves, unrelated work and frozen host Release. The wider
80% goal stays active.
