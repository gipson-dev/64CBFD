# All Remaining Byte-Exact Donor Recoveries

Date: 2026-10-14

## Scope And Result

The user requested all available matching C for missing, unfinished, unmatched,
or placeholder routines. Re-audit the linked executable C from the alternative
source against the active decomp, then install **all 19 remaining eligible
functions**. Together with [Note 1360](1360-first-byte-exact-donor-conversions-20261014.md),
all **22 applicable donors** are now adopted. The fresh individual-donor queue
is **zero**, not another partial batch.

This does not finish the wider Game decomp. Already-matched active routines
are left alone, and unlinked donor drafts, unmatched C, original assembly and
the donor's failed normal link do not receive C matching credit.

## Completed Steps

1. [x] Re-run the canonical retail-slot audit; identify exactly 19 remaining candidates.
2. [x] Recover all ten smaller Game routines using active headers and local layout views.
3. [x] Recover both streaming-driver routines and seven codec routines.
4. [x] Use the codec's retail `-g` profile only for its seven selected functions; keep its six established `-O2` neighbors unchanged.
5. [x] Verify all 4,117 raw and linked retail words with zero new expected-word guards.
6. [x] Preserve all 742 neighboring bodies, relative relocations, constant pools, old guard bytes and progress rows.
7. [x] Verify the complete linked transition, retained overflow bodies and all 720 protected data owners.
8. [x] Re-run existing history/corruption checks, fresh donor checks and the alternative-source audit.
9. [x] Refresh README aggregates and separate status/roadmap/index/update documents.
10. [x] Bank tools before the consumer source/docs pin; preserve unrelated mirror work and do not push.

## Installed Functions

| Function | Owner | Words | Recovered Role |
| --- | --- | ---: | --- |
| `func_15008870` | `game_35D20.c` | 48 | Clear the selected range in two 104-entry rows |
| `func_1501AF44` | `game_476D0.c` | 87 | Clamp rectangle edges to framebuffer bounds |
| `func_15042D94` | `game_70200.c` | 42 | Copy sixteen o32 variadic words and submit a text command |
| `func_1505D1C4` | `game_83300.c` | 61 | Initialize object slot 25 and restore the current index |
| `func_1506D74C` | `game_981E0.c` | 83 | Raise/reposition the actor and initialize movement state |
| `func_15074980` | `game_981E0.c` | 49 | Set nearby actors' chase timers |
| `func_15079228` | `game_A28B0.c` | 46 | Face a pointed-to path entry and decrement one movement step |
| `func_1509B764` | `game_C8950.c` | 43 | Unlink/free a doubly linked script node |
| `func_150C2FCC` | `game_EF410.c` | 48 | Damped extents and vertical acceleration |
| `func_15168F84` | `game_1944C0.c` | 47 | Select an inclusive group index range |
| `func_151F2E88` | `libultra/audio/game_21FC90.c` | 727 | Stream lifecycle and audio command generation |
| `func_151F39E4` | `libultra/audio/game_21FC90.c` | 142 | Volume/pan ramp and output mode overrides |
| `func_151F3DE0` | `game_221290.c` | 322 | Codec windows, x^(4/3) and gain lookup initialization |
| `func_151F42E8` | `game_221290.c` | 788 | Granule/channel spectrum requantization |
| `func_151F578C` | `game_221290.c` | 782 | MPEG-2 LSF scalefactors and intensity-stereo masks |
| `func_151F6970` | `game_221290.c` | 110 | Short-block reorder or long-block spectrum copy |
| `func_151F6B28` | `game_221290.c` | 298 | Long-block subband butterfly rotations |
| `func_151F8088` | `game_221290.c` | 335 | Frame synchronization, validation and side-info dispatch |
| `func_151F85C4` | `game_221290.c` | 59 | Fixed codec buffer initialization and first-frame validation |

## Names, Types And Build Integration

Retain address-keyed public `func_XXXXXXXX` symbols for layout, callback and
map identity. Add concise behavior comments and descriptive locals where the
role is established. Do not invent an upstream public name.

`ScriptNodeC8950` and `ScriptListC8950` are private views of the recovered
next/previous links and pointer-valued list endpoints. Do not globally merge
the alternative structs header. The codec similarly uses private band,
pre-emphasis and scalefactor-table views.

`func_15079228` now loads the pointer stored at `D_800D3098`, reads signed
halfword coordinates from its 52-byte entry, and decrements `unk218` by one,
not the old incorrect five. `func_15042D94` restores the original variadic
argument walk, rather than twenty fixed typed arguments.

Two owner-local integer-typed pointer parameters for `func_1505F188` and
`func_1505C7D8` caused `func_1505D1C4` to acquire an extra stack spill. Restore
their pointer arguments, including the existing placeholder definition's
argument type, without claiming that separate helper is recovered. The
61-word initializer then matches directly; all 88 neighbors remain unchanged
and three existing warnings disappear. The stream driver uses the codec
initializer's pointer return declaration and explicitly stores its o32 value
in the existing address-valued integer global.

The active codec owner contains six established O2 routines as well as seven
retail `-g` routines. Reuse `pad_c_object.py --function-object`, already used by
mixed-profile owners, to select only the seven `-g` bodies. No pad-tool behavior
change or instruction normalization is introduced. Exclude this owner from
the generic plain-object recipe to avoid adding a duplicate-recipe warning.
The pre-existing `generated_12D630` recipe warning remains unrelated.

## Qualification And Image Accounting

The first installed run passes **30 checks in 111.864 seconds**, covering new
donor qualification, all nine prior donor checks, four alternative-source
checks and prior actor/text history checks with effective corruption controls.
Three further compiled controls alter the clear range, movement decrement and
codec synchronization mask; all fail the byte gate, one check in 15.076 seconds.
The final five donor checks pass **27.386 seconds**, including the typed audio
declaration, all raw bodies/742 neighbors, linked transition, unchanged inputs,
19 installed-word corruption controls and three compiled source controls.

All 19 complete raw C bodies and full linked slots match: **4,117 words /
16,468 bytes**, no new guards, no omitted-slot exception. All **742** primary
owner neighbors retain their raw words, sizes, relative relocations and pools.

The `.game` section changes exactly **12,732 bytes**. Its only changes are
the 19 declared slots and jumps to retained overflow bodies after compaction.
Remove three obsolete overflow bodies for `func_15042D94`, `func_15079228`
and `func_151F2E88`, totaling **3,360 bytes**. The remaining **13** bodies
concatenate byte-for-byte into the compacted 3,072-byte overflow section.
All other executable/data section contents and addresses remain unchanged.

Close the canonical symbol differences: selected function sizes, removed
overflow symbols, retained overflow addresses, two obsolete object file labels,
and the resulting `__romPos`/debugger-overflow ROM start. The entire final ELF
serialization is also pinned; metadata is not blanket-excluded.

Historical fixtures are not reset. A bounded adapter recognizes only the
independently qualified, exact SHA256 post-checkpoint and projects it back
to the preserved prior fixture for old audits. Changed instructions, source,
guards, progress, symbol definitions or strings fail those gates. The new
transition test independently checks the actual installed image.

| Artifact | SHA256 |
| --- | --- |
| Before ELF | `294eba92c9b31ea335a560d67f8536a30993fc1fa429796df1c486fb532f7ddd` |
| Final ELF | `65a9c8e783574fbff76c11d3ab000af8015c604a17061f138f5d354e2a2e3968` |
| Guard CSV, unchanged | `59473e88b9a02be589d8c72465716753aa8802f1908cba79b771f2c8fbf952d0` |
| Progress CSV, unchanged | `c1fd11fe3c2891b50cd9c3f20ed9936e6d3c90a75b17e81c50ca45cad65526e6` |

Protected data remains **189,088 bytes / 720 owners / zero differences**.
All 801 archived source files are still unchanged. No host build, frozen
Release work, runtime audio acceptance claim or blanket donor import occurs.

## Fresh Progress And Next Work

- Legacy headline total: **3,531 / 5,499 (64.21%)** byte-exact.
- Game: **2,858 / 4,826 (59.22%)**, **1,968** still different, zero drift.
- Init: **492 / 492** converted C rows exact; Debugger legacy: **181 / 181**.
- Conversion totals remain **5,499 / 6,044**; these 19 already counted as C.
- Executable-function-only total: **3,391 / 5,359 (63.28%)**; Debugger is
  **41 / 41** after excluding 140 data labels. Keep the separate legacy-counter
  correction explicit rather than silently changing README denominators.
- Applicable byte-exact donor queue: **zero**. All 22 authorized donors have
  been integrated across Notes 1360 and 1361.

Resume original Game matching, not another donor import. The adjacent codec
`func_151F4F38` remains non-matching; its donor draft is not linked exact C and
requires independent register/scheduling recovery. It is a possible connected
next task, not completion credit or an accepted replacement. Host transfer and
audible/runtime qualification remain separate work.

Reproduce with `python3 -m tools.experiments.game_remaining_donor_candidates`,
`python3 -m unittest tools.tests.test_game_remaining_byte_exact_donors -v`,
`make -C conker build/conker.us.elf NON_MATCHING=1 -j8` and
`make -C conker match-progress NON_MATCHING=1`. Receipts are retained under
`conker/build/game-remaining-byte-exact-donors/` and the earlier audit directory.

## Bank And Preservation

Tools are banked first in `249f8c3e06442be6d3cc3338e7615ae25578c97b`.
Consumer `9eb367cfbea5284228f1fca8f9ec8a34a6ca4279` banks all source,
build selection, tools pin and documentation changes. The nine post-bank
donor/audit checks pass **39.383 seconds**; `make tools-check` also passes.
All ten owned files in the older mirror pass a fresh WSL syntax check.
The older tools mirror keeps HEAD `ddbdd16b53ce60b054fb6e11bf0649a41f48375a`.
Synchronize only ten owned paths: seven existing audit adapters and three new
qualification files. All **465 unrelated dirty fingerprints remain unchanged**;
the mirror's 472 dirty paths become 475 solely through the three new files.
Do not commit or reset that independently dirty mirror.

The final normal rebuild and incremental recheck pass with the pinned ELF
above. Root README changes only its aggregate matching rows; detailed recovery
updates stay in this note and the status/roadmap/index/update documents.
The source-bank graph hook completes at 40,742 nodes / 80,972 edges, preserving
19,398 nodes from 2,972 still-present files excluded by the current scan rules.
Do not force a smaller full refresh or treat the skipped large HTML graph
visualization as a failed source build. No push is performed.
