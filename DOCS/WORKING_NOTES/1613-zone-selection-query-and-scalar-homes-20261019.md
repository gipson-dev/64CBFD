# Zone Selection Query And Scalar Homes

Date: 2026-10-19. Consumer predecessor: `f94e35ac`; tools predecessor: `7899ba5`.

## Result

Continue `func_1508B3F8`, following [Note 1612](1612-neighbor-row-builder-complete-match-20261019.md)
and its earlier [semantic recovery](1022-game-zone-neighbor-selection-recovery-20261006.md)
and [lifetime screen](1023-game-zone-neighbor-selection-lifetime-screen-20261006.md).
Retail occupies 369 words/1,476 bytes, VA 1508B3F8..1508B9BC, ROM B88A8..B8E6C,
with a 320-byte frame.

**Experimental home recovery, not an installed byte match.** A closed
permutation of the existing 23 local declarations recovers all four named
retail homes without changing any executable C statement or adding storage:

| Value | Installed C | Qualified Candidate | Retail |
| --- | ---: | ---: | ---: |
| 88-byte query | SP+0xE8 | SP+0xAC | SP+0xAC |
| Cached selections | SP+0xE0 | SP+0x124 | SP+0x124 |
| Cached zone cursor | SP+0xDC | SP+0x94 | SP+0x94 |
| Loop counter | SP+0xCC | SP+0x13C | SP+0x13C |

The complete candidate remains **369 words/frame 320**, with **277 raw word
differences**, down from the reproduced installed source's 282. The selected
body is `tools.experiments.game_zone_neighbor_selection_homes.SELECTED`.
This demonstrates those emitted homes, not the original declaration order.
No dummy field, query enlargement, volatile, register binding, instruction
array, padding fix, new guard or compiler-profile override is introduced.

Production C remains unchanged. Its official classifier still reports 281
differences; do not replace that production figure with the candidate's raw
277 or describe either as instruction-percentage completion.

## Source And Owner Evidence

[Home screen](../../tools/experiments/game_zone_neighbor_selection_homes.py)
adds 32 source controls. They include query positions, closed named-home
placement, byte winners, retained flags, guarded actor entry, cached
coordinates, deferred zones, direct fields and inline remainder variants.
All complete with empty compiler diagnostics. Non-selected controls are
screens, not individually qualified production bodies.

The typed-distance/byte-winner control still emits 370 words/frame 320/233
raw differences and remains oversized. Retained flags produce frame 328;
inlining the remainder expands the body to 374/375 words. None is installed
by deleting an arbitrary instruction or changing the slot limit.

[Owner qualification](../../tools/experiments/game_zone_neighbor_selection_home_integration.py)
compiles the complete owner before/after on both existing profiles. The
primary changes only 30 SP-relative immediate fields; the ordinary profile
changes only 32. Every opcode, register field, non-stack operand and all 32
relocation bindings are unchanged within each profile. The ordinary target
is 425 words/frame 328 and is not selected for production.

Both profiles preserve all 72 other raw functions and their pools. Actual
padding retains all 73 owner addresses/extents, all 72 neighbors, pools and
every non-target byte. It keeps the three existing normal-function overrides.
The mirror independently recompiles both owner profiles and reproduces the
same padded candidate. This is not a complete production Make/ELF install.

## Qualification

[Fourteen focused tests](../../tools/tests/test_game_zone_neighbor_selection_homes.py)
pass in **81.769s primary / 99.798s mirror**, with no skips. Mirror module paths
are checked before redirecting only the test input root to prepared consumer
inputs. Separate primary/mirror receipts remain ignored.

- 2,990 four-way guest cases compare retail, the candidate, the old retained-
  query source and the independent indexed recovery against the reference.
  They cover signed bounds, strict/equality/unordered gates, all candidate
  counts, ties, helper mutations and replaced globals/captured cursors.
- Dedicated cases visit all 369 retail-parent and 84 connected visitor words.
  Height/root lookup and bzero remain bounded opaque providers in these tests;
  this does not qualify their complete production chain or gameplay.
- 1,424 native32 fixtures pass at O0/O2/O3 with trap-mode UBSan, checking public
  memory footprints and ordered calls. A deliberate signed-overflow control
  fires SIGILL (-4), proving the sanitizer gate is active.
- Sixteen completed retail/candidate guest alias runs cover query threshold,
  counter, zone cursor and selections in both stack phases. The same eight
  aliases effectively reject the old homes. Query/visited pointer arguments
  agree at the real addresses. These deliberate frame aliases are not
  portable C calling contracts.
- Three compiled semantic negatives reject repeated queries, lost queue clear
  and inclusive candidate comparisons.

An initial native harness attempt required unavailable 32-bit CRT files. The
final harness reuses the repo's freestanding startup/compiler flags; no
dependency/configuration repair is needed. Direct defining-module imports
also avoid the newer experiment chain's unittest import-depth failure.

## Remaining Boundary

Two fired model store-cut probes keep the mismatch explicit. At the 18th
attempted store, retail requests counter SP+0x13C (caller SP-4), while the
candidate requests zone SP+0x94 (caller SP-172). Both stack phases reproduce
this difference. Equal final homes are not literal access-prefix or complete
private-state equivalence.

Retail retains query S7, visited pointer S6 and constant 255 in S8. The
candidate instead retains query S5 and ready S6, with node-global/minimum
addresses in S7/S8. Opening delay-slot/global-read scheduling, byte-winner
narrowing and remaining allocation/cursor scheduling still need recovery.
Full private/FCSR/hardware/caller/gameplay acceptance remains separate.

Continue this same routine. Close those saved-role/address lifetimes and the
fired store-order boundary, then qualify complete private/fault/alias behavior
and actual Make/strict linked-image gates before installation. Do not rotate
to a different function merely because this candidate is still unmatched.

## Banked State

Tools `743f234` is committed before consumer docs/pin. Only three absent task
files are copied into the independent mirror; all 1,427 older dirty leaf
hashes and HEAD `ddbdd16b` are preserved. Its 1,430 dirty entries include the
three new copies. No mirror commit/reset/stash/clean, push, advisory call,
host/frozen Release operation, save or dependency change.

All 19 pinned production/reference/compiler inputs remain byte-identical,
including source, guards, Makefile, progress CSV and linked ELF. The installed
baseline remains `f94e35ac`. Root README stays unchanged. Totals remain Game
3,016/4,832 (62.42%), overall 3,689/5,505 (67.01%), 1,816 different and zero
address drift; the owner remains 68/73 exact. `make tools-check` passes.

```text
Candidate C:     0a71c2d9f2487709f2009464c47c5cc532bd3a872edca5ce2a106f924b012941
Raw primary:     d2ba85071e0b0129b5be6aaf0d19fd40e4da20f88a9d4284e9aca81ffe3f79c0
Padded target:   c265fa820209550a6133de59bce0857901ae311a07825ec8f65aa5d221229d61
Production ELF:  0462d68d9fe12d04c2d747b1f8877305f84bce1ac7793e24024268e6e06e07c7
```

Receipts live under ignored `conker/build/game-zone-neighbor-homes/`: the
32-form screen, primary/mirror tests, immutable input copies, before/after
owner profiles, padding/pool checks, candidate fingerprints and Graphify
baseline/audit. Production is not rebuilt because no production input changes.
