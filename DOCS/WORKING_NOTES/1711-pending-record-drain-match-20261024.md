# Pending-Record Drain Match

2026-10-24. Fully qualified, installed, production-built, adopted and freshly
recounted. This is guarded semantic C, not a compiler-only match. The wider
75% exact-C goal remains active.

## Target And Baseline

- Function `func_1517CFC4`, owner `generated_1A89B0`.
- VA `0x1517CFC4..0x1517D074`; ROM `0x1AA474..0x1AA524`.
- All 176 bytes / 44 words; frame `0x30`, saved S0-S5/RA; no alignment tail.
- Consumer predecessor `c374ed477c1df8c4172957e884f5dafe800041f2`.
- Tools-first commit `ce0d707b639f103a2db6d1c215ab803c9af8133e`.
- Original assembly remains in `conker/asm/1A89B0.s`; no compiler profile change.

The preliminary typed/scalar-view and full-owner screens from Note 1710's
ignored handoff were reused as starting evidence, not as installed credit.
This checkpoint captured 42 focused immutable inputs and verified 16,010
native/cache files, including all 1,454 linker objects. WSL used the existing
PSBBN stdin/tar bridge; it did not read the project through DrvFS.

## Recovered Semantics

[The source](../../conker/src/game/generated_1A89B0.c) now has a complete
`void func_1517CFC4(void)` body. A private 16-byte record view exposes only
the pending pointer at offset eight; reserved bytes remain opaque.

Scan all 15 records beginning at `&D_800DDA90`. Empty pending entries do not
read a destination. For a nonempty entry, load the corresponding destination
from `&D_800DD478` at a 104-byte stride. A non-null destination receives
`func_10006240(pending, destination, D_8003809C)`, followed by
`func_10004074(record->pending)`. The latter reload is intentional: the first
helper may change the field. Read the scratch word for every processing call.
Clear every initially nonempty pending field, including a missing-destination
entry that skips both helpers. Advance the record cursor on every iteration.

Keep the shared header's existing scalar/opaque global declarations. The
private casts do not claim a recovered full shared table schema.
`func_10006240` retains its actual `s32` return type; `func_10004074` is void.
The local declaration in [the caller](../../conker/src/game_45B80.c) is now
void, matching its unused result. All 16 caller functions and the complete
caller object are unchanged after recompilation. No second matching credit
is assigned to the caller.

## Checked Normalization

Existing O2/g3 emits the complete 44-word body, frame and saved-register
lifetimes. Only raw words 11-13 differ: pending/destination/scratch low-address
setups appear in destination/scratch/pending order in retail. Cycle those
three independent existing words and their LO16 bindings. All other words,
branches, delays, calls and register lifetimes emit directly from C.

Three expected-word/relocation guard rows are appended, preserving the entire
old CSV prefix byte-for-byte. Fixed raw-body hash and all eight bindings are
checked before derivation. No instructions are inserted, omitted or invented.

- Raw 44-word C SHA-256:
  `e0657ab8cf6943b229007db402d1aa9466befb962e77122b7f4bb4b74697566d`.
- Retail target SHA-256:
  `34c6806c0435d8ee95970da3c6d50898842f67dc3743628b58a90dcba8063ac6`.
- Qualified padded object SHA-256:
  `8ea0922db7ea301c4bab8fa57ac2990b584fda1125cbe9ab1e95319bb779b8de`.

## Qualification

Permanent tools are `experiments/game_pending_record_drain.py` and
`tests/test_game_pending_record_drain.py`. Both local copies pass eight fresh
checks before and after installation, with no skips or reused tests.
Pre-install runs: 13.358s / 13.337s; installed runs: 59.060s / 66.585s.
Shared tools checks also pass in both copies.

- 3,780 guest cases cover all 15 positions, seven helper mutation modes,
  three alias layouts, and all 44 reachable words. Emitted raw C and fitted
  retail match complete private machine state, calls and public memory.
- 354 paired guest fault prefixes; empty records need no mapped destination
  table, and a missing scratch word faults at a processing call. A skipped
  reload is an effective negative control. This qualifies emitted guest
  access order, not portable C fault semantics.
- Ten independent GNU links across five layouts validate all six HI/LO and
  two call bindings, carry boundaries, a scratch/helper-home alias and
  overlapping pending/destination storage.
- Native32 O0/O2/O3 with trap UBSan: 225 positive cases and nine effective
  semantic controls per profile. Multi-record mutations detect cached
  scratch and pending values. Native backing unions are private fixture
  storage views, not changes to production headers.
- 84 connected executions of the original five-word retail caller boundary
  at `0x15018CD4` / ROM `0x46184`. The result is ignored and the next call
  receives `(0, 1)`. The aligned retail scan finds this one direct call and
  no literal function pointers. An actually compiled MIPS cached-pending
  negative is detected.
- All 44 raw-word perturbations, eight binding controls, extent/history
  controls, two real-padder corruptions and five full-image corruptions are
  rejected.

Helpers are bounded mutation/clobber contracts here, not full decompressor
or allocator executions. Whole-parent gameplay is not accepted by these tests.

## Production And Image Audit

The ordinary Make recipes use three commands for each owner. All 14 target
owner compact functions and all 16 caller functions match their qualified
counterparts; the complete target padded object agrees, and the complete
caller object remains identical. Preserve 13 target neighbors and all pools.

Independent full link and actual production Make agree on exactly 136 changed
ELF bytes: 135 inside the target slot, and one target symbol-size byte
(`12 -> 176`). No metadata exclusions or unaccounted symbol permutations.
Production Make exits zero in 7.392s. All 6,054 other linked bodies and all
addresses remain fixed. Protected Game data remains exact across 720 owners /
189,088 bytes, SHA-256
`0bbc00e1adfac5ffe6117f5be9c941575f87b341a77d808004603ac1cb87c670`.

Actual adopted native ELF SHA-256:
`902853b86424d6758316ec20095dec229d9c1bd98b334339f3b27d07b55be8c5`.
The native adoption audit verifies all 16,010 captured files with only five
qualified overrides: target source, caller source, guards, target object and
ELF. Preserve the older tools mirror's 1,632 existing path statuses/hashes and
HEAD; only the two owned modules are added there. Do not commit/reset that mirror.

## Fresh Progress And Next Work

The actual native ELF bytes were captured, streamed back and freshly recounted
with `match_progress.py`; only `func_1517CFC4` leaves the unmatched queue.

| Section | Byte-Exact C | Different | Address Drift |
| --- | ---: | ---: | ---: |
| Total | 3,787 / 5,505 (68.79%) | 1,718 | 0 |
| Game | 3,114 / 4,832 (64.45%) | 1,718 | 0 |
| Init | 492 / 492 (100.00%) | 0 | 0 |
| Debugger | 181 / 181 (100.00%) | 0 | 0 |

The 75% threshold is 4,129 / 5,505: 342 more matches. The queue has 1,589
placeholders, 120 semantic/other entries and nine parser-unlocated entries.
Next ordinary placeholder is `func_150C5D0C` in `generated_F2820`, 45 words.
Keep `func_15014094` as a separate existing-C task and `func_1510D8C0` as an
existing `Gfx *` body missed by the source parser; neither receives credit.

The root README receives aggregate rows only. Graphify is queried for the
target/caller/helpers and refreshed by the normal code-only commit hook.
The parent intentionally filters `tools/`; a separate zero-API-token AST
receipt covers these two tools files, without claiming parent membership.
Audit old-node retention separately; do not call the existing filtered-corpus
warning a clean full-corpus extraction or claim all old edges were preserved.
No push, host/Release, dependency/provider/configuration changes or Claude calls.
