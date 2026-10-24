# Paired Actor Child Teardown Direct C Match

Date: 2026-10-24. Consumer predecessor `1ef7137a`; tools predecessor
`c31f6b24`. Qualification tools committed before the consumer pin as
`a0858ab7d3d3d2e219d199bf8a9a4d11bda20fe4`. No push requested/performed.

## Recovered Routines

Owner: `conker/src/game/generated_11C2B0.c`.

| Function | VA Span | ROM Span | Release / Base Helpers |
| --- | --- | --- | --- |
| `func_150EF7B0` | `0x150EF7B0..0x150EF860` | `0x11CC60..0x11CD10` | `func_1516972C` / `func_1513CA6C` |
| `func_150EF860` | `0x150EF860..0x150EF910` | `0x11CD10..0x11CDC0` | `func_1516979C` / `func_1513CAA0` |

Each complete routine emits all 44 words directly from C, frame 40, five
bindings and no new guards/profile changes. Both symbol extents advance
from twelve to 176 bytes. The same raw words bind to the two helper families.

Raw C SHA-256, each:
`991bb68820e184ca876d69da751a407f878ce680f0f2e24c1203417db13cbbee`.
Resolved/retail SHA-256:
`func_150EF7B0`:
`0a3cdd60b59fdb41e462e60a8b0baad0e1caea5de7e6879726703d549ff88366`;
`func_150EF860`:
`96454209e43379cd34fcd73008c4935fedf1a98f96d35ebe85d630ebf788cbc0`.

The local `ChildReleaseState11C2B0` view starts at owner+0x110 and holds
five record pointers at relative +0x1C..+0x2C, absolute +0x12C..+0x13C.
Leave the preceding state bytes opaque. Loop over the first two entries,
then test the remaining three individually. Release every non-NULL entry
through the appropriate helper, then run base teardown on the owner.

Preserve live future-slot reads, repeated pointers, absence of pointer
clears, four saved-register lifetimes and the final incoming owner-home
reload. Do not cache all five pointers or deduplicate calls. The natural
two-entry C loop emits retail's offset counter/limit and branch-likely
update without a special compiler profile.

## Actual Caller Interfaces

The only aligned literal references are index seven in thirteen-entry tables:
`D_80089EF8`, ROM `0x22E9B8`, slot `0x80089F14` for the first;
`D_80089F2C`, ROM `0x22E9EC`, slot `0x80089F48` for the second.
There are no aligned direct target JALs.

Their actual dispatchers are `func_1513CB58` and `func_1513CBA4`,
each nineteen words/frame 24, in `conker/src/game_169510.c`.
Owner flag 0x400000 selects the owner byte at +0x19; otherwise choose slot
zero. There is no out-of-range selector check. Preserve that behavior rather
than inventing a safety clamp or claiming arbitrary selectors are safe.

Correct both C dispatchers from a no-argument call through a legacy
`void(void)` table declaration to a local `void(struct210 *)` cast and
explicit `arg0`. No shared header or unrelated table is edited.
The entire 59-function raw caller object and actual padded Make object are
byte-identical before/after this source-level ABI correction. Both dispatcher
bodies and tables match retail.

Native32 probes compile both actual corrected C caller bodies against full,
properly typed `struct210` owners and callback argument-capture boundaries.
They prove argument delivery and valid thirteen-slot selection, not a full
native caller/callee teardown closure. Selected-body native fixtures use a
separate complete typed child-state owner and full `struct102` children;
only pointer conversions, not incompatible header dereferences, cross that
boundary. Other callbacks and lower heap services remain bounded providers.

## Focused Qualification

Both tools copies pass eight fresh checks before and after installation,
zero errors/failures/skips, no reused checks. Pre-install primary/mirror:
16.206s / 16.016s; installed: 16.864s / 16.716s.
Both shared `check_project_tools.py` runs exit zero.

- 2,048 ordinary guest phases cover all 32 NULL masks, distinct/repeated
  pointers, future-slot mutations, late incoming-home changes and two stack
  phases. Every root word is visited. Compare literal GPR/FPR/HI/LO/RAM,
  event/call order, restored SP/RA and all saved GPRs.
- Native32 O0/O2/O3 with trap UBSan: 1,280 selected calls per optimization
  across both functions, typed storage, all surrounding/opaque bytes and
  eleven effective defined wrong-C controls per function.
- Both complete original dispatchers execute over 468 phases, including all
  thirteen valid slots and flag-clear/default selection. Both real tables
  and index-seven registrations are checked. Other callbacks are bounded.
- Native actual-caller boundary probes: 52 calls per optimization across
  both functions. Do not count these as full native teardown acceptance.
- Execute all 119 current-and-original retained helper words in 480 phases:
  both release dispatchers, signed-count scan, both default helpers and both
  base-teardown coordinators. Cover type-byte boundaries, empty/positive/
  negative scan counts, callbacks and default paths. Actual lower unlink,
  heap, base-state and auxiliary-resource work remains bounded.
- Eighteen independent GNU links compare original, qualified padded and
  actual Make objects. 288 cases independently rebase root/release/base
  addresses. All 648 root-access prefixes fire with equal state, PC and
  branch-delay origin. Fourteen image corruption/truncation controls fail.
  Guest private-home aliases/fault schedules are not portable C guarantees.

Earlier `func_1518C850` source/control-form experiments remain private,
unmatched and uncredited. The callback interface remains void; no integer
return was invented for register allocation. This checkpoint instead
qualifies the complete neighboring teardown pair.

## Production And Preservation

Preserve all 42 raw/padded neighboring functions and owner pools, including
the previously recovered owner-ray routine. The target's actual three-command
Make recipe and caller's five-command asm-processor/padder recipe both use
normal O2/g3 and emit their qualified padded objects exactly.

Target diagnostics are empty. The caller's 43 inherited warnings are
normalized for source filename only and are unchanged before/after; no
unrelated warning cleanup is included. Inherited duplicate Make recipes also
remain unchanged. Production Make exits zero in 0.699s.

Independent and production full links reproduce exactly 252 changed ELF
bytes: 250 target-code bytes plus two size bytes, zero exclusions. All other
6,053 function bodies and all 6,055 addresses remain fixed. The complete
guard manifest is byte-identical. Protected Game data remains exact across
720 owners / 189,088 bytes, SHA-256:
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Result ELF SHA-256:
`c67e436c20af22f763e2b2996d9c38fc501cbdd3ff408c6bc6a7f11fbcb387de`.
Target object SHA-256:
`a475992b5e72bb2022a038374b57de3b24a03da26f9b2a535086d28cf8505652`.

Seal 15,922 files / 30 focused inputs / all 1,454 linker objects. Verify
native capture, Linux cache and every static input/non-target object before
and after adoption. Stream via native stdin/checked tar without DrvFS
project reads. Only the two sources, target object and ELF differ.
Preserve all 1,588 pre-existing older-mirror dirty paths/statuses/hashes
and HEAD, adding only two task files. No host Release, save or config changes.

## Fresh Recount And Handoff

Capture actual adopted Windows ELF bytes and require identity with the
independent and production images. Standard matcher exits zero in 1.439s:

| Section | Exact C Functions | Address Drift | Still Different |
| --- | --- | --- | --- |
| Total | 3,761 / 5,505 (68.32%) | 0 | 1,744 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Game | 3,088 / 4,832 (63.91%) | 0 | 1,744 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

Denominator unchanged. Remove only the two qualified targets from the
ELF-pinned queue: 1,613 placeholders, 122 semantic/other and nine
parser-unlocated entries remain. The active 75% target is 4,129 exact
functions, 368 more.

Continue `func_1510D8C0` / `func_1518C850` triage without crediting
private screens; the former already has a `Gfx *` C body. The unconverted
five-argument owner-link helper `func_15169850` and remaining 44-word
candidates remain queued. Keep 862-word `func_1508CAD8` separate.

Commit only ten scoped consumer paths. Root README gets its two aggregate
rows only. Use the normal Graphify hook, then audit all 43,873 old nodes
for retention/unique relocation and all nine changed C/Markdown hashes,
mtimes and memberships. Never forge a missing stamp or equate excluded-old
retention with complete corpus re-extraction.
