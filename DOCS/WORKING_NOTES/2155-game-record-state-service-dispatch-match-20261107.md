# Record-state service dispatcher matched with register guards

Date: 2026-11-07. Continues [Note 2154](2154-game-callback-position-payload-factory-match-20261107.md)
from consumer `8a4159e8c5cdb6dae30575243b311a48e76c1eef` and mounted tools
`7bdf6ac3bf48128d0ec4f325ed36610155238fdc`. One additional qualified Game
function advances the active 80% total goal.

## Recovered record state and service packet

`func_150A24C0` in `conker/src/game/generated_CDE80.c` replaces its zero-return
placeholder with the complete **69-word / 276-byte** routine. VA is
`0x150A24C0..0x150A25D4`, ROM `0xCF970..0xCFA84`. Normal O2/g3, MIPS2/O32
produces the original 64-byte frame, saved S0/RA lifetime, incoming selector
home at caller SP+4, control flow, memory operation order and one JAL
relocation at body offset 0x9C. Twenty-five checked GPR allocation guards
reproduce the complete literal retail body. This is guarded matching,
not direct unguarded emission.

The recovered interface is `void (GeneratedCDE80Record *record, s32 selector)`.
Exact full-word selector 255 exits before reading any record field; the guest
NULL-record path is covered. Values -1, 256 and 0x100FF must not be truncated.
The guest stores selector into its incoming home before that early gate.

For other selectors, capture word +0x1C. If its low byte is zero or mode
byte +0x17 is nine, call `func_15183290` with these eleven values:

| Argument | Recovered value |
| --- | --- |
| 1 | Signed halfword +0x00 |
| 2 | Signed halfword +0x02 plus byte +0x1D shifted left four, full 32-bit sum |
| 3 | Signed halfword +0x04 |
| 4 | Full word +0x18 masked to its low byte |
| 5 | Mode byte +0x17 passed as a word |
| 6 | Signed halfword +0x06 |
| 7 | Full 32-bit selector |
| 8 | Signed halfword +0x18 |
| 9 | Byte +0x1A |
| 10 | Byte +0x1C |
| 11 | Full word +0x20 |

Overlapping word, halfword and byte views share one 52-byte record backing.
Explicit captures preserve the retail load-before-outgoing-store order.
Offset names avoid inventing semantic field meanings. The local service
prototype uses `u8` for argument four and `s32` for the others; the fourth
byte ABI is inferred from the original ingress store and `lbu` of home+3,
not claimed as recovered original source spelling.

Result -1 cancels the update. Otherwise reload live mode; nine cancels too.
Reload live word +0x1C and publish
`(live & 0xFFFF0000) | ((u32)result << 8) | 0xF0`. Do not narrow the result
to eight bits. Unsigned shifting avoids signed-shift UB. Service mutations
to mode and high state bits must remain visible. On the no-service branch,
preserve the captured upper 24 bits and floor its low phase byte at two.

## Closed allocation normalization

Raw SHA-256:
`ad30e0c1334440dc880b251fc5f6c9b945ac40bc46e3a48d56483a80a8fbbec0`.
All 25 differences are GPR fields. The derivation requires the complete
hash, 276-byte extent and exact sole relocation. It changes no opcode,
immediate, branch target, shift amount, memory width, instruction position,
frame size or relocation.

Zero-based word ranges are mode load 12 and call words 17..40, post-service
44..52, a new final-state lifetime 53..55, and phase-floor words 58..63.
Closed bijections are explicit in
`tools/experiments/game_record_state_dispatch_150a24c0_match.py` and all
expected/replacement pairs are frozen in the candidate. SP, RA, S0, A0,
zero and AT are never renamed. The first proof attempt incorrectly reused
the dead mode temporary's allocation for the new final-state destination;
two words rejected it. Separating those lifetimes gives the exact body.

Guarded execution matches retail in all tested GPR/FPR/HI/LO, private bytes,
PC and accesses, including fired fault cuts. Raw C independently matches
complete memory, calls, accesses, PC and callee-saved state. Caller-saved
temporaries and incidental V0 can differ; the sole observed caller ignores
the return, and no void-path V0 result is promised.

All **27 raw and padded neighbors** remain fixed. Allocatable pools and
options payloads are literal. Old/new owners compile with zero C diagnostics.
No header, Makefile or compiler profile changes. The duplicate generated_12D630
recipe warning remains. Old manifest bytes are an exact prefix, followed by
exactly 25 new expected-word rows.

## Independent qualification

Seven focused checks pass before and after installation in both tools
configurations. The 125 frozen inputs include complete target/service assembly,
relevant sources/objects, SDK/compiler inputs, linker/layout/registries, old
ELF, conversion CSV, guards and graph. Every imported helper and new module
is fingerprinted. The sibling uses its own available helpers through a
disposable new-module overlay; missing `alloc_pools` is an explicit hashed,
read-only mounted fallback. All 2,434 inherited sibling dirty paths remain
fingerprinted and unchanged.

* **4,339 guest cases per body** compare retail, guarded and raw instructions
  with an independent coherent byte model. All phase and mode byte values,
  full-word selector boundaries, signed coordinates, full-width Y sums,
  overlapping field views, arbitrary 32-bit results and service mutations
  are covered. Two guest-only aliases cover outgoing argument/home overlap
  and the incoming selector store over the record prefix. Record bytes
  remain explicitly observed even when inside the private stack region.
* **68 of 69 words execute.** Word 56 is the retained unreachable duplicate
  `slti` and still matches. No all-word execution claim is made.
* Twelve cases per body connect the complete retained **392-word** original
  service and execute its **27-word all-busy path**, with actual ingress
  homes, four busy-byte scans and result -1. Other service behavior remains
  bounded. Its production placeholder is unchanged and gets no new credit.
* The aligned retained-input census finds one target JAL at ROM 0xCEFF8
  and no entry/interior pointers. **216 cases per body** execute all five
  original caller-window words at 0x150A1B44, including the selector load
  from SP+0xC8 in the JAL delay slot and branch to 0x150A1CF8. The whole
  original parent and gameplay are not qualified by this window; its
  production placeholder is unchanged.
* **198 fired access cuts**, including **20 delay-slot cuts**, compare full
  guarded state and raw memory/PC/access/callee-saved prefixes, including
  NULL early exit, aliases and the connected busy-service path. These
  qualify guest instruction order, not portable C fault semantics.
* Native32 SDK O0/O2/O3 each pass **4,210** independently generated little-
  endian byte fixtures with structure-offset/size assertions and UBSan
  traps. Eight compiled negatives fail with exit one: former stub, selector
  truncation, wrong floor, stale high state, stale mode, narrowed result,
  narrowed Y sum and wrong property mask. Views share one coherent backing
  for that endianness; this does not assert little-endian field bytes equal
  retail big-endian bytes. Private stack/home aliases are guest-only.
* Two independent GNU links/rebases check the JAL. Four intentional
  header/body/symbol/string corruptions fail the complete-image predictor.

The initial native harness omitted freestanding `_start`; its linker warning
rejected the fixture before execution. It now uses the existing native
checks' explicit Linux exit pattern. An initial generic module name collided
with an older task: both tracked files were restored exactly and verified
clean, then all five new modules received the unique `150a24c0` suffix.
These fixture corrections change no production behavior or acceptance gates.

Shared smoke checks pass freshly in both copies. Three unchanged shared
regression receipts per copy are explicitly reused after exact helper/test
fingerprints against Note 2154. Claude calls: zero.

## Actual Make and production recount

Actual Make recompiles only this owner under normal O2/g3 and equals the
independent complete ELF prediction: **210 changed bytes, zero exclusions**.
Only the target's 276-byte slot and symbol extent 12 -> 276 change. No
metadata permutation or section exclusion is needed. All 6,052 function
addresses stay fixed; only this body changes. All 189,088 protected Game
bytes across 720 owners remain exact. Conversion CSV is byte-identical
because the former stub already counted as C. Compile/link pass with zero
owner C warnings; `make all` reaches the expected nonmatching image
checksum and exits two.

| Section | Exact / converted | Percent | Drift | Still different |
| --- | --- | --- | --- | --- |
| Total | 4,225 / 5,512 | 76.65% | 0 | 1287 |
| Game | 3,552 / 4,839 | 73.40% | 0 | 1287 |
| Init | 492 / 492 | 100.00% | 0 | 0 |
| Debugger | 181 / 181 | 100.00% | 0 | 0 |

The 80% threshold is 4,410 / 5,512: **185 additional exact functions** remain.
Root README gets aggregate rows only; four indexes get a concise lead with
historical text preserved. Graphify refresh retains old nodes outside changed
paths and excluded-but-existing legacy files fail-closed. This is a scoped
refresh, not fresh full-corpus extraction. Commit tools first, then consumer
source/guards/docs and exact tools pin, followed by fresh hook/preservation
audit.

| Artifact | SHA-256 |
| --- | --- |
| Production ELF | `7657d214413a1814ac0758fb4c4db76d19bb056776b7d9426b1c4cc7556eeb03` |
| Production binary | `d79a81b7b7007fa6d6f0736b69c9857c15299a2085788c6cb504b1703f157fa6` |
| Padded owner | `8651759bf2218cc52390416a9093116f4ce3b67673f2d844f1a35aabd5e4acc6` |
| Guard manifest | `f886325ab0671a847dd4dca4b976b063a225350f92043bc817aa56360b7b17bc` |

Qualification, pre/post suites, shared checks, production, graph retention and
post-commit receipts remain ignored under
`conker/build/game-record-state-dispatch-150A24C0-match/`.

Next: **func_150A25D4**, adjacent 110-word record updater, VA
0x150A25D4..0x150A278C, ROM 0xCFA84..0xCFC3C. Inspect complete state/mode
branches and the original caller before selecting a semantic candidate.
Preserve frozen handwritten/hidden-ABI boundaries, explicitly frozen
150A6FA0/150A76F0, private inputs/saves, unrelated work and frozen host Release.
Keep the wider 80% goal active.
