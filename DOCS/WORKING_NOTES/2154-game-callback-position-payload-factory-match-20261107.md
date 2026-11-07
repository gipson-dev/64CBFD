# Callback-position payload factory matched directly

Date: 2026-11-07. Continues [Note 2153](2153-game-active-entry-reset-loop-match-20261107.md)
from consumer `ccdf86f57a0da06d6b2dc53a3c943d58d312a39a` and tools
`f1c457d7cdad54327ae89a8e97452e51097b6b93`. One additional qualified
Game function advances the active 80% total goal.

## Captured payload and live callback state

`func_151D0F60` in `conker/src/game/generated_1FA770.c` replaces its
zero-return placeholder with the complete **69-word / 276-byte** factory.
VA is `0x151D0F60..0x151D1074`, ROM `0x1FE410..0x1FE524`. Normal O2/g3,
MIPS2/O32 emits every original word directly, with **zero guards**, the
112-byte frame and all eight bindings intact. Its recovered interface is
`void (u8 *owner, u8 selector, u8 priority, s32 context)`; all three observed
call sites ignore the result. An incidental memcpy return in V0 is not
treated as a promised return value or proof of the original declaration.

The real 56-byte `PositionPayload151D0F60` starts at SP+0x34. Owner pointer,
owner byte +0x3B and a zero word are captured before calling
`D_8008FC30[selector](owner,&payload.second)`. A zero callback status
replaces second with the then-live default `D_800A5480`. First copies second,
and third reads the default again. The remaining float becomes positive
zero; the selector byte is reloaded from its live O32 home after the callback.
Generic vector names avoid inventing meanings for the three payload vectors.

The creator receives `(300,-1,95,-1,0,72,56,priority,context)`, with live
priority/context reloads after the callback. A non-NULL result receives all
56 payload bytes at created+0x28 through memcpy; a NULL result skips the copy.
The default is initially three positive-zero float words, but remains a
mutable symbol. Its callback-time changes must be visible. Owner/id remain
captured even if the callback or creator changes the original owner memory.

Payload offsets 0x05..07 and 0x35..37 are implicit SDK/C padding. The guest
checks every emitted byte, using a seeded private frame. Native fixtures
explicitly exclude those six bytes and do not assert portable padding values
or initialized values for partial callback writes.

## Callback ABI repairs without neighboring code changes

The table's first three retail entries are 0x151D1074, 0x151D10A4 and
0x151D10C4. The latter two wrappers were incorrectly declared void with
integer pointer parameters. Their original instructions preserve the status
from `func_151D10E4`, which this factory tests. The source now returns that
status explicitly and uses compatible owner/vector pointers. The first
callback uses the same vector type, and the common query uses real output/
matrix pointers instead of integer carriers. Both null and non-null matrix
paths retain their original status behavior.

All **51 raw and padded neighboring instruction streams** remain literally
fixed, including those four repaired definitions. Native compilation assigns
the actual callback functions to the exact table type without casts, and
executes 18 return/output checks per optimization level. The transform below
the common callback remains a bounded provider; full matrix math is not
claimed. Two precise pointer warnings disappear from the wrapper calls to
`func_151D10E4`. A closed diagnostic gate permits only those two removals:
eight warnings before, six after, no new warnings. The other six remain
unrelated. The duplicate generated_12D630 Makefile recipe warning remains.

Raw and padded allocatable pools and options payloads are literal; no
register-mask allowance is needed. No shared header, Makefile, compiler
profile or guard-manifest change occurs.

## Independent focused qualification

Seven checks pass before and after installation in both tools
configurations. The 120 frozen inputs include source/object/complete owner
assembly, caller assembly/source, original factory source, SDK headers,
IDO executables, retained retail input, linker/layout/registry, guards,
conversion CSV, predecessor ELF and graph. Imported helper files and every
new module are fingerprinted. The sibling executes its own available helpers
through a disposable new-module overlay; its missing `alloc_pools` uses an
explicit hashed mounted fallback read-only. All 2,434 inherited sibling dirty
paths are independently fingerprinted and retained.

* 733 guest cases per body compare the complete memory effects, calls and
  both creator/copy packet observations with an independent byte reference.
  Every target word executes. Cases cover all 256 selector/identity bytes,
  all eight partial-output masks, zero/nonzero/negative callback statuses,
  default/owner/private-packet mutations, live argument homes, allocation
  success/failure and five overlap layouts. Stack destinations use an
  explicitly bounded factory that avoids corrupting its caller's saved RA;
  these are guest-only provider scenarios, not claims about real allocation.
* 254 cases per body connect 149 original helper words: callback/query slots
  12/8/8/21, creator 49, bzero 40 and memcpy 11. Coverage is respectively
  12/8/8/21/47/22/11 words. This caller passes creator flags zero, so the
  creator's two-word alternate flag-class path is not reached. The clear
  is 16 aligned bytes; all 56 payload bytes pass through the real forward
  copy loop. Allocator and lower transform remain bounded. The complete
  retained helper bytes, actual table entries and default bytes are checked.
* The aligned retained-input census finds exactly three direct target JALs,
  ROM 0x17B11C/0x17C660/0x17C674, and no entry/interior pointers. 384 cases
  execute both complete original callers: ten words at 0x1514DC5C and
  93 words at 0x1514F194. All 103 caller words execute, including both
  conditional branches in the larger parent. Other parent services are
  bounded. The smaller caller is exact in production; the larger caller is
  still its existing zero-return production placeholder. Executing its
  retained retail instructions proves this call interface, not recovery or
  gameplay acceptance of that parent. Its production slot stays unchanged.
* 138 fired access cuts, including eight delay-slot cuts, preserve complete
  private memory, GPR/FPR/HI/LO, PC and access prefixes.
* O0/O2/O3 SDK native32 builds each pass 688 independently generated little-
  endian byte fixtures, plus the 18 actual callback checks, with layout
  assertions and UBSan traps. Six compiled negatives fail with exit 11:
  former stub, late owner identity, stale default, unconditional default,
  52-byte copy and wrong creator kind. Native checks verify initialized
  packet fields, pointer identity, copy length and call order while excluding
  implicit padding. Partial uninitialized outputs, incoming-home poisoning,
  private-packet mutation and forward-overlapping copies remain guest-only.
* Two independent GNU links/rebases include signed low16 carry for both
  table/default symbols. Four header/body/symbol/string corruptions fail.

The initial draft incorrectly required full coverage of the creator's unused
flag branch and assumed the larger caller was already restored in production.
Those assumptions were corrected from measured instructions and current
source, without changing either routine's production bytes. Exact retained
windows and explicit coverage boundaries replace those incorrect claims.
Floating exception flags, hardware traps and full transform/gameplay behavior
are outside these bounded tests. Shared smoke checks pass freshly in both
copies. Three unchanged shared regression receipts per copy are explicitly
reused after exact helper/test fingerprints against Note 2153. Claude calls:
zero; local evidence settled the implementation and ABI audit.

## Actual Make and production recount

Actual Make recompiles only this owner under normal O2/g3 and equals the
independently predicted complete ELF: **213 changed bytes, zero exclusions**.
The only allowed changes are the 276-byte target slot and its symbol extent
12 -> 276. No symbol/string permutation or section exclusion is needed.
All 6,052 function addresses remain fixed; only this body changes. All
189,088 protected Game data bytes across 720 owners remain exact. The
conversion CSV is byte-identical because the former stub already counted
as C. Compile/link pass; `make all` reaches the expected nonmatching image
checksum, exit 2. The four callback source repairs add no matching credit.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
|Total|4,224 / 5,512|76.63%|0|1288|
|Game|3,551 / 4,839|73.38%|0|1288|
|Init|492 / 492|100.00%|0|0|
|Debugger|181 / 181|100.00%|0|0|

The 80% threshold is 4,410 / 5,512: **186 additional exact functions**
remain. Root README receives aggregate rows only and four current indexes
receive a concise lead. Graphify refresh retains old nodes outside changed
paths and excluded-but-existing legacy files fail-closed; this is not a
fresh full-corpus extraction. Commit tools first, then consumer source/docs
and the exact tools pin, followed by the fresh hook and preservation audit.

| Artifact | SHA-256 |
| --- | --- |
|Production ELF|`5a4db0738d916beba355845ed0eeb8927617d0e590505c956a90cafaf2c4ecd7`|
|Production binary|`7cd6efd82436154d1636c98775ee1943686c69b10a5c76ce5ceb87178a146a9b`|
|Padded owner|`cd707a020cf3d561eed8a1a7de7ee13bffe05d4259f4ca058343e84fffe21030`|
|Unchanged guard manifest|`66ad0ff1fb837b102250469a08f2fa8f7e862bde40868b3b8f0357346ca8571b`|

Separate qualification, pre/post suites, shared checks, production, graph
retention and post-commit receipts remain ignored under
`conker/build/game-position-payload-151D0F60-match/`.

Next: **func_150A24C0**, a 69-word record-state dispatcher in
`conker/src/game/generated_CDE80.c`, VA 0x150A24C0..0x150A25D4,
ROM 0xCF970..0xCFA84. The measured live queue shows 68 retail word
differences in its existing zero-return slot. Recover the full-word 255
argument gate, state/mode branches, eleven-argument service packet and
post-service state update with complete qualification. Preserve frozen
handwritten/hidden-ABI boundaries, explicitly frozen 150A6FA0/150A76F0,
private inputs/saves, unrelated work and frozen host Release. Keep the
wider 80% goal active.
