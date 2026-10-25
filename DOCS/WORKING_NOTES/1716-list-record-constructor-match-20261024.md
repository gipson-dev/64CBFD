# List Record Constructor Direct C Match

2026-10-24. Production-qualified direct C recovery, adopted and freshly recounted.

## Recovered Routine

`func_1517E080` now has its complete semantic C constructor in
`conker/src/game/generated_1AB530.c`, replacing the zero-return placeholder.
Its entire 45-word/180-byte slot emits directly from the existing retail
O2/g3 compiler profile, with frame 0x20, no alignment tail and **zero new
guards**. The three original bindings remain intact: `D_800DDD64` HI16/LO16
at +0x04/+0x08 and `allocate_memory` R_MIPS_26 at +0x58.

- VA: `0x1517E080..0x1517E134`; VROM: `0x1AB530..0x1AB5E4`.
- Canonical C interface: `struct162 *func_1517E080(s32 first, s32 second)`.
- A private complete 0x34-byte view exposes only the two floats, next link,
  halfword, and three initialized bytes. The shared `struct162` is an older
  0x30-byte view; it and the opaque global declaration remain untouched.
- Walk the next links at +0x24 and capture the old terminal link address
  before calling `allocate_memory(0x34, 1, 0, 1)`.
- Return NULL on allocation failure without constructor publication or
  initialization writes; allocator-side mutations can still remain visible.
- Publish through the captured link before initializing next +0x24,
  halfword +0x28, byte +0x2E, float +0x10, float +0x0C and bytes +0x2F/+0x30.
  Reload the two full incoming argument homes late, then truncate to bytes.
- Preserve every other byte. This is not a whole-record zero fill, an
  allocator rewrite, or a capped/cycle-detecting list traversal.

## Caller And Allocator ABI

The whole-ROM encoded-call scan finds one JAL, VROM `0x36658` / VA
`0x150091A8`, word 22 of `func_15009150`. No literal target pointers occur
in the ROM scan; that does not rule out arbitrary computed calls.
The existing C caller in `conker/src/game/done/game_36600.c` now has a local
typed constructor prototype. Its complete 32-word retail slot/frame 24,
all bindings and the full production caller object remain byte-identical.
It passes `(0, 0xFF)` and unconditionally writes result byte +0x2E = 3.
The original NULL-result dereference is preserved and tested, not repaired.

The installed Init allocator wrapper returns `s32`, not `void *`. The recovery
uses that canonical declaration plus an explicit 32-bit address cast. This
corrects the old private screen's incompatible pointer-return declaration
without changing any emitted words. Both original and retained 11-word
`allocate_memory` wrappers are connected in guest tests, including their
frame 32, inserted fourth argument zero and fifth outgoing argument one.
Native probes use the actual wrapper C body with a bounded deeper allocator.

## Focused Qualification

Both independent tools copies passed **six fresh pre-install checks** with
zero errors, failures, skips or reused checks. Primary: 23.450 seconds;
older mirror: 15.679 seconds. Both existing shared tool checks also passed.

- 1,792 guest cases cover empty and multi-node lists, allocation failure,
  signed/high-bit arguments, head/existing-node aliases, incoming-home
  aliases, allocator head/tail mutations and late home mutations. All 45
  reachable original words are visited.
- 134 paired fault prefixes agree in complete guest state. These qualify
  emitted guest access order, not portable C fault semantics.
- 54 connected original/typed caller cases cover gate and table selection,
  nested frame/home behavior, arguments, publication and the final byte store.
- 192 actual allocator-wrapper connections verify the deeper five-argument
  call. The core allocator is a bounded provider, not a complete heap proof.
- Native32 O0/O2/O3 with trap UBSan pass 5,120 selected cases per profile,
  using heap-backed typeless fixtures, asserted 0x34-byte layout and correctly
  typed constructor function pointers. Five effective controls detect late
  publication, unwanted opaque-byte clearing, wrong first byte, missing next
  reset and wrong allocation size. Guest stack/global aliases are not claimed
  as portable native fixtures.
- Two compiled MIPS semantic controls are effective; all 45 raw-word corruptions,
  extent/binding changes, six independent GNU links in three layouts, and six
  strict-image corruption controls are checked. Global HI/LO and call bindings
  are independently rebased.

Whole-owner compilation preserves all seven neighbors, the one existing
GLOBAL_ASM routine, diagnostics, extents and normalized pools. The actual
five-command generated-GLOBAL_ASM Make route reproduces all eight compact
functions and the complete qualified padded object. Original assembly,
shared headers and the entire retail guard CSV are unchanged.

Initial validation needed two fixture corrections: a three-command Make
assertion did not describe this GLOBAL_ASM owner, and connected oracle bodies
must use flat address-to-word maps, not entry-to-list maps. The corrected
qualification and fresh suites pass; the failed fixture evidence is retained
separately in the ignored build directory and never counted as a passing gate.

## Production Image

Normal `make -C conker -j4 build/conker.us.elf progress.csv` passes in the
verified stdin/tar Linux cache without project DrvFS reads (137.325 seconds).
The production image reproduces the independent **127-byte exact prediction**:
126 code bytes and one symbol-size byte, with zero exclusions or symbol
permutations. All 6,054 other linked bodies and all addresses remain fixed.
Protected Game data is exact across 720 owners / 189,088 bytes:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Each tools copy passes **two fresh installed checks plus four fingerprinted
semantic reuses**, not six fresh installed checks. Reuse requires literal
installed source/caller/object/ELF equality and unchanged complete sealed
inputs, module fingerprints and qualified artifacts.

The tools were committed first as `7c3f57364d9782b241dc7d20345c8200ebf812f2`
(`Qualify direct list record constructor and typed caller`). The older mirror's
1,642 pre-existing dirty paths and HEAD are preserved; only two owned modules
are added there, without a mirror commit, reset or stash. Nothing is pushed.

## Measured Progress

Native adoption verifies all 16,030 captured inputs with exactly four explicit
source/caller/object/ELF overrides. The actual adopted Native ELF, streamed to
the GNU recount without DrvFS, is identical to the independent production image:

`d7f55e4df3b36403d433d98d12497133a35e74b135a9a944ddaef6247dd88f56`.

| Section | Byte-exact C functions | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,792 / 5,505 (68.88%) | 0 | 1,713 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,119 / 4,832 (64.55%) | 0 | 1,713 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Only `func_1517E080` leaves the remaining-function queue. The 75% threshold
remains 4,129 / 5,505, requiring **337 more matches**; the wider goal remains
active. The refreshed source-shape screen contains 1,584 placeholders, 120
semantic/other definitions and nine parser-unlocated entries. These are triage
classes, not additional ABI or C-matching qualifications. The root README
changes only its verification date and the two aggregate match rows.

Detailed local receipts remain in the ignored
`conker/build/game-list-record-constructor-match/` directory; private ROMs,
ELFs, packets and compiler outputs are not published.

## Next Target

Continue with ordinary placeholder `func_1519E818`. Its original 45-word
routine is the related identity callback plus a global clear after release.
Any isolated source screen remains private, uninstalled and uncredited until
caller/registry, ABI, guest/native, owner/Make, full-image and adoption gates
close. Keep existing-C `func_15014094` and parser-missed `Gfx *func_1510D8C0`
separate from ordinary placeholder recovery.

The deeper allocator, complete caller/gameplay paths, host-port behavior and
hardware acceptance remain outside this bounded C-matching checkpoint.
No host/Release, provider, package or global configuration changes are made.
