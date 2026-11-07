# Below-height effect callback matched

Date: 2026-11-07. Continues [Note 2150](2150-game-owner-reference-command-handler-match-20261107.md)
from consumer `278850e0a597ba0ec3d4dba189c7385135348176` and tools
`d510ada034f4804d0bfba9410c966a3630d9faae`. This checkpoint adds one fully
qualified Game match toward the active 80% goal.

## Complete semantic callback and data lifetime

`func_15189EBC` in `conker/src/game/generated_1B6DB0.c` replaces its zero-return
placeholder with the complete **69-word / 276-byte** callback. VA is
`0x15189EBC..0x15189FD0`, ROM `0x1B736C..0x1B7480`; the interface is
`s32 (u8 *actor)`, always returning 1. The source defines a typed 20-byte
position record and declares the selector's recovered `u8 (void)` interface.

The position table at actor+0x94 and payload at actor+0x98 are captured before
the first comparison. The signed-byte index at actor+0x2D selects a position
record. An ordered comparison tests whether its Y is below the payload's
height at+0x48. False or unordered comparisons return without providers or
public stores. A true result calls the float RNG, then compares its result
as a double against the live `D_800A73A8` constant, bits
`0x3FE999999999999A` (0.8).

When the random threshold passes, X/Z are read from the retained table using
the live index, and the vector's Y comes from the retained payload's live
height. This vector is complete before calling the selector. Scale/alpha and
actor priority/owner bytes are read afterward, so selector mutations remain
visible. The seven-argument effect service receives selector low 8, scale
times 6, alpha, zero context, the vector, priority and owner. After the optional
effect, the captured payload is marked 4 and its height is reset from the
then-live `D_800A73B0`, initially `0xC61C4000` (-10000). A provider replacing
actor+0x98 must not redirect this final update.

## Closed frame/spill guards and owner audit

Normal O2/g3, MIPS2/O32 emits all 69 words with 65 already exact. Four expected
word guards recover the original 80-byte frame from the compiler's 72 bytes:

| Offset | Raw C | Retail | Meaning |
| --- | --- | --- | --- |
|0x0|0x27BDFFB8|0x27BDFFB0|Allocate 80 rather than 72 bytes|
|0x4C|0xAFA20044|0xAFA20040|Save the retained table pointer at SP+0x40|
|0x5C|0x8FA20044|0x8FA20040|Reload that same closed spill|
|0x110|0x27BD0048|0x27BD0050|Restore the matching 80-byte frame|

The complete SP audit accounts for 14 direct memory accesses, the balanced
prologue/epilogue and one escaping address. The sole escaping object is the
12-byte vector at `[SP+0x34,SP+0x40)`. Both the old spill `[0x44,0x48)` and
new spill `[0x40,0x44)` are disjoint from it, the outgoing arguments at
0x10/0x14/0x18, and the saved registers at 0x24/0x28/0x2C. There are no incoming
argument-home reads. The retail frame's last live byte is 0x43; its final 12
bytes are unused. All opcodes/register roles/branches/public accesses and
seven relocation bindings otherwise remain unchanged. No word is inserted
or omitted. Altered frame words, escaped vector addresses and bindings fail
closed.

Eleven natural source/aggregate screens were retained. A four-float array
extent control is explicitly non-adoptable; it is not used to fabricate the
retail frame. The installed source retains its real three-float vector.
Changing the selector declaration from an initial `s32` screen to its proper
`u8` return type leaves the emitted body unchanged.

All three raw/padded neighboring bodies stay fixed. The only raw pool change
is the expected GPR usage mask, `0xA001C1F6` to `0xA303FFFE`; all other mask
fields, pool bytes and relocations remain fixed. Padded pools are literally
unchanged. Both owner compiles have zero diagnostics, with no Makefile,
compiler-profile or shared-header changes.

## Fresh focused checks

Seven checks pass pre/post installation in both tools configurations. New
modules use a disposable sibling overlay, with its available helpers executed
directly. Missing mounted helper fallbacks are explicitly named and hashed;
all imported dependencies are fingerprinted. All 2,434 inherited sibling dirty
paths are independently fingerprinted and retained.

* 1033 guest cases per body compare retail, guarded C and raw C against an
 independent byte-memory reference. All 256 signed index representations,
 four overlap layouts, finite/exceptional ordered comparisons, provider
 pointer replacements and field mutations are exercised. All 69 target
 instructions are visited. Raw C public effects, vectors and calls agree
 under its distinct private frame; its private byte layout is not claimed
 identical to retail. Guarded C agrees with full retail state and traces.
* 113 fired access cuts, including 10 delay-slot cuts, preserve the complete
 guarded private memory, PC, registers and access prefix. Minimal mappings
 confirm that a rejected height gate does not touch provider-only state.
* 448 cases per body connect the original 25-word float RNG, 19-word selector
 and 113-word effect submitter. Coverage is 25/19/76 words respectively: this
 callback always passes zero context, so the submitter's nonzero-context
 branch is not reached. The lower effect provider remains bounded. The
 actual RNG unit `0x37800080` and all 768 palette bytes are checked against
 the frozen production image/retail input. The service reference preserves
 this caller's live alpha rather than assuming the previous caller's 255.
* 16 cases execute the original 17-word callback window at VA 0x15147F04,
 including disabled/blocked routes. Its slot is `D_8008A3F8[10]`, address
 `0x8008A420`, ROM 0x22EEE0. The target receives one actor argument; its return 1
 keeps the caller's block flag clear. The full dispatcher is not claimed.
* Three SDK native32 builds at O0/O2/O3 each pass 368 finite cases against
 independently generated little-endian Python byte fixtures, with UBSan
 traps and aligned backing. Native aliases cover separate storage, position
 storage and actor storage; the actor+0x80 overlap is guest-only. Five
 actually compiled controls fail: former stub, inclusive height comparison,
 reloaded table pointer, reloaded payload pointer and a float threshold.
* Two independent GNU links reproduce all instructions under separate code
 and constant rebases, including a signed low16 carry. Four deliberate
 header/body/symbol/string corruptions are rejected.

Floating exception flags, NaN payload propagation and hardware traps are not
claimed by the bounded numeric model. Original loaded instructions are
literally exact after the guards; no gameplay/hardware acceptance is inferred.
Fresh shared smoke checks pass in both tools copies. Three unchanged shared
regression receipts per copy are explicitly reused only after exact helper/
test fingerprint checks against Note 2150. No Claude call was needed.

## Actual Make, strict image and production recount

The 108 frozen inputs include original assembly/registry/constants, owner,
all SDK headers, IDO executables, ROM, linker, layout, guards, Makefile and
predecessor image. Actual Make recompiles only this owner under O2/g3 and
produces the independently predicted ELF exactly: **248 changed bytes,
zero exclusions**. The prediction replaces the 276-byte function slot, updates
its symbol extent from 12 to 276 bytes, and fully reconstructs two closed
GNU-ld symbol/string pair swaps: D_800A73B0/D_8009E640 and
D_800A73A8/D_8009E638. All named definitions otherwise remain identical;
neither metadata section is excluded.

All 6,052 function addresses stay fixed; only this function's body changes.
All 189,088 protected Game bytes across 720 owners remain exact. The conversion
CSV is byte-identical: this was already a C-classified placeholder. Compile/
link pass; `make all` reaches its expected nonmatching image checksum, exit 2.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
|Total|4,221 / 5,512|76.58%|0|1291|
|Game|3,548 / 4,839|73.32%|0|1291|
|Init|492 / 492|100.00%|0|0|
|Debugger|181 / 181|100.00%|0|0|

The 80% threshold is 4,410 / 5,512: **189 additional exact functions** remain.
The root README gets aggregate rows only; this note owns recovery details.
Four current indexes get a concise lead. Graphify is refreshed with old-node
retention checks, retaining excluded-but-existing legacy nodes fail-closed;
this is not a fresh full-corpus extraction. Commit tools first, then the
source/guards/docs and exact consumer pin.

| Artifact | SHA-256 |
| --- | --- |
|Production ELF|`652799e33cba0e843ac58ec6e3a2c6f81a3cd3383cca403a6c067af74e1dc165`|
|Production binary|`2209c027b5bf050bdae92b41c07e75de3372cef7ee5429d5d8a038a239267dbb`|
|Padded owner|`88a6d300f57fe9631bdc7d51d622d11b65fe05f0fcc6150a0c29d835ab13f98e`|
|Guard manifest|`4792e2d49631c53f8b7da7276d04153ea8133f2dc48ed5c8fdcbd63ee9b059cf`|

Receipts and transient screens remain ignored under
`conker/build/game-below-height-effect-15189EBC-match/`: qualification,
pre/post target suites, shared checks, production, graph retention and
post-commit audits each have separate JSON/log files.

Next: **func_15193390**, the 73-word zeroed sprite descriptor constructor in
`conker/src/game/generated_1C0840.c`, VA 0x15193390..0x151934B4,
ROM 0x1C0840..0x1C0964. Its sentinel height branch, five-argument initializer,
constructor and final randomized timer need complete qualification. Preserve
the eight established handwritten/hidden-ABI boundaries, explicitly frozen
150A6FA0/150A76F0, private inputs/saves, unrelated work and frozen host Release.
Keep the wider 80% goal active.
