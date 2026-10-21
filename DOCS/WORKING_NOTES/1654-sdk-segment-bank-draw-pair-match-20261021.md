# SDK Segment-Bank Draw Pair Direct C Match

Date: 2026-10-21

## Result

Restore `func_151D710C` in `conker/src/game/generated_203E20.c` as complete,
purpose-commented SDK-macro C. Normal O2/g3 emits the original **40 body
words, frame24 and six bindings** directly, without guards, raw emitters,
shared-header edits, profile changes or omitted logic. The queued 41-word
slot includes a separate four-byte alignment NOP. Correct Note 1653's static
handoff accordingly; do not add the alignment word to semantic body coverage.

Body VA 151D710C..151D71AC / ROM 2045BC..20465C, ends exclusive;
alignment at 151D71AC / ROM20465C; next slot begins 151D71B0.
Keep the reference `conker/asm/203E20.s`.

Unlinked C/GNU-original body SHA-256:
`81ab0b702d359aaf4bb1c0a7fed5f1a4ef3b188cde97a6fc40d307d2bfcec48c`.
All six relocations are checked, then independently linked to compare all
160 body bytes and the alignment tail against the frozen retail ROM.

## Recovered Contract

The interface is `Gfx *(Gfx *commands, u8 *descriptor, s32 unused2,
s32 unused3, u8 *changed)`. Save the full two unused words in entry-SP+8/+12.
Read descriptor byte+0x43 before any graphics stores. For values below 255,
emit SDK `gSPSegment` selecting bank `D_80083740`; for 255 select
`D_800838C0`. Both commands use segment 8 / DB060020.

Pass the advanced cursor to `func_15133EEC` with resource 0xC3, segment 6,
mode 3, then pass its returned cursor to the same helper with segment 7.
Reload the fifth-argument pointer from entry-SP+16 after both calls, write
one byte of value 1 through it and return the second helper's cursor.
Preserve all stores, helper ordering and return redirection. Word-form helper
arguments also emit the same body; the chosen u16/u8 types reflect the actual
helper's halfword/byte consumption, not uniquely proven historical spelling.

Bindings, relative to the body:

| Offset | Kind | Symbol |
| --- | --- | --- |
| 0x30 / 0x34 | HI16 / LO16 | `D_80083740` |
| 0x54 / 0x58 | HI16 / LO16 | `D_800838C0` |
| 0x6C / 0x80 | R_MIPS_26, twice | `func_15133EEC` |

## Caller And Helper

The complete 22-word/frame32 `func_150FB1E8` at VA 150FB1E8, ROM 128698,
matches retail in the current linked image. It calls this routine and forwards
the returned cursor plus its original remaining four arguments to
`func_15157F80`. Add a typed target declaration and explicit pointer/word
casts in `conker/src/game/generated_126F60.c`; preserve its existing public
word-based ABI. Execute all 22 original/current caller words over 24 phases,
including hostile volatile-register clobbers and redirected cursors.

All 18 caller-owner functions, pools and diagnostics remain unchanged. The
entire padded caller object remains byte-identical, SHA-256
`7fb6083d5edb715b1465ae005cc0d098919291cff0ed1c53aa1a5cc131fda3ed`.
No warning was added or removed; do not claim the warning fix from Note 1652.

Execute all 59 original helper words at 15133EEC / ROM 16139C in 64 connected
phases, covering both command-count paths and both end-offset choices.
Use controlled resource-table records and a bounded lower decoder that writes
the size output and returns a data address. Validate emitted command words,
wrapping end addresses, returned cursors, stack state and the final byte flag.
The decoder implementation, natural resource registration and rendering are
not qualified. The current helper still has a placeholder C body; do not
describe this as a working natural caller/helper chain or gameplay acceptance.
The follow-up caller helper is likewise an opaque provider boundary here.

## Qualification

Tools: `experiments/game_segment_bank_pair.py` and
`tests/test_game_segment_bank_pair.py`, identical in both local copies.

| Run | Active tools | Older mirror | Errors / failures / skips |
| --- | --- | --- | --- |
| Full pre-install suite | 8 tests, 55.303s | 8 tests, 72.737s | 0 / 0 / 0 |
| Fresh installed checks | 2 tests, 9.637s | 2 tests, 6.100s | 0 / 0 / 0 |

Explicitly reuse the other six checks per copy only under unchanged source,
raw/padded object, helper, input and complete-image identity. Those six are
not fresh installed executions. Shared project-tool checks also pass twice.

- 3,072 guest phases cover all 256 descriptor values, helper return redirection,
  store/read order and all 40 body words. Another 120 phases cover byte aliases,
  full unused homes and late fifth-pointer changes. Guest stack aliases are
  not represented as portable native C behavior.
- 16,384 native32 cases per optimization at O0/O2/O3 use actual SDK macros,
  the real C caller, trap UBSan, typed Gfx arrays, legal character aliases,
  complete memory/fence comparisons and all provider packets. Eight compiled
  wrong-C controls are effective.
- Six independent GNU links / 72 phases exercise every binding, independent
  bank/helper anchors and signed-low carries. There are 180 fired root-access
  fault prefixes, excluding provider accesses, and seven strict-image
  corruption controls. Keep portable faults and MMU behavior out of the claim.
- Pin 29 historical/current inputs, both old objects, SDK gbi.h, all relevant
  assembly/data references and the real caller source. Preserve six owner
  neighbors and the full guard manifest. Actual Make shadows execute six
  productive commands; caller object identity is a whole-file check.

The first probe incorrectly unpacked the body as 41 words and stopped before
installation; correct the body length to 40. The first full test run also
stopped four guest checks because the inherited oracle overwrote its generic
symbols field. Give this fixture its own anchor field, then pass both full
suites again. Do not count either failed attempt as a passing receipt.

## Production And Preservation

The live and Linux-local copies are sealed across 15,786 files, including the
complete 1,454-object linker closure. Rebase the prior qualified parabolic
source/object/ELF delta only after its committed-source and strict-adoption
proof; add only the four new task-file copies. No cache rebuild, dependency
installation, provider reconfiguration or host change is needed.

Actual production Make exits zero in 1.974s, rebuilding both owner objects,
linking the ELF and regenerating progress. Only the inherited duplicate-recipe
warning remains. The entire image equals the independent prediction:
**123 changed bytes = 122 instruction bytes + one symbol-size byte**, zero
metadata exclusions/permutations. The alignment tail remains original.

Installed ELF SHA-256:
`6e51b1a879d012d3b84bec32cce212f34ef9e08e302574a69afdfd74ecd21110`.
Installed target-owner object SHA-256:
`1e5adf4ce113247d4fc61970a96c9ce890885b67b570f65e0aad4ad668e22f9e`.

All other 6,055 bodies and all 6,056 addresses remain fixed. Protected Game
data remains exact: 189,088 bytes / 720 owners, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.
Recheck all 15,786 live files before/after adopting only the two objects, ELF,
generated linker script and progress CSV. Caller object bytes remain immutable.

Tools commit `fcaa532a5e8db70fb6f80e7e8bc386364ba2b076` precedes the
consumer source/docs/pin commit. Preserve all 1,520 pre-existing dirty statuses
and hashes in the older tools mirror; add only two task files, totaling 1,522
dirty paths. Do not commit/reset/stash/clean that mirror. No push, host build/
launch/change, shared-header edit, profile edit or Claude call. Release remains
frozen. Root README changes only its two aggregate rows. Refresh Graphify and
verify old-node retention after the consumer checkpoint.

## Measured Progress And Resume

The literal standard matcher exits zero against the adopted live ELF:

| Section | Byte-exact converted C | Address drift | Still different |
| --- | ---: | ---: | ---: |
| Total | 3,722 / 5,505 (67.61%) | 0 | 1,783 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,049 / 4,832 (63.10%) | 0 | 1,783 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold is 4,129; **407 more exact functions** are required. The
broader goal remains unfinished. The ELF-pinned source screen has 1,650
placeholders, 124 semantic/other definitions and nine unlocated entries.

Next: `func_150B3DD0`, 41 body words/frame40 in
`conker/src/game/generated_E1280.c`, reference `conker/asm/E1280.s`.
VA 150B3DD0..150B3E74 / ROM E1280..E1324, ends exclusive. Static inspection
shows an initial `(0,5)` helper call, followed by six command-0x18 calls
using the same local byte with values 0,2,4,1,3,5. Determine its actual caller/
return ABI, helper contracts, local lifetime and visible effects before any
draft or installation. No matching credit is claimed for it. Keep the larger
862-word `func_1508CAD8` owner stub queued.

Private receipts, snapshots, native/guest fixtures, Make shadows, linked
images, preservation proofs, literal matcher, queue and checkpoint audits live
under `conker/build/game-segment-bank-pair/qualified/`. No ROM, generated
fixture or build artifact is committed.
