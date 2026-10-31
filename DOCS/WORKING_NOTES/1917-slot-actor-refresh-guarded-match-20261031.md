# 1917 - Slot actor refresh restored from guarded C

Date: 2026-10-31. Function `func_1501DE18`, generated owner `49D30`.
VA `0x1501DE18..0x1501DF04`, ROM `0x4B2C8..0x4B3B4`.
Tools checkpoint: `1c4dc2103d833d2edcadf04dc04cc818416d2a7a`.

The zero-return placeholder is replaced with the semantic slot refresh.
All 59 words are byte-exact after three checked setup/relocation guards.
The original 48-byte frame, saved S0-S4/RA lifetime, 17 relocation bindings,
call order, actor stride and branch delay slots are preserved. No words are
inserted or omitted, and no alignment padding is added.

## Recovered behavior

The signature is `void func_1501DE18(s32 slot)`. The selected destination
timestamp becomes the source timestamp plus `D_800BEA08` before the first
helper call. Unsigned casts preserve retail's wrapping 32-bit addition
without introducing signed-overflow behavior into C.

The setup order is `func_150242F8(1, 0)`, `func_1501EC38(0)`,
`func_150242F8(0, 0)`, then `func_15020EC4(0)`. The routine subsequently
scans all 25 `struct127` records in `D_800CC2D0` at stride `0x32C`.
For an occupied record it publishes the index to `D_800C3E78`, calls
`func_150229E4(actor)`, and applies `func_1502178C(actor, slot, -1)` for any
nonzero result. It finishes with `func_1501E81C(1, slot)`.

The actor state is read as the scan advances; helper changes to future
records remain visible. The current record's occupancy is not checked again
after eligibility returns. Current-index and timestamp changes made by
helpers remain intact. The caller ignores the result register, so the
recovered function returns void.

The donor source was only a hypothesis. Retail instructions correct its
array indexing, byte counter and erroneous word-pointer stride. The source
uses the existing `struct127` definition and an explicit word counter.

## Compiler and guard scope

This owner uses the retail `-O2 -g3 -Wo,-loopunroll,0` profile. Qualification
uses the existing active-record compiler adapter and fingerprints that
adapter in both tools copies. The actual Make commands confirm the same
profile; the owner is not compiled under a generic unroll policy.

Only words 30, 31 and 32 differ before normalization. The compiler's actor
address completion, counter initialization and current-index address
completion rotate into retail order `[32, 30, 31]`. The two LO16 bindings
move with their instructions; both HI16 preimages remain unchanged.
`schedule_proof` verifies this closed rotation across all words and bindings.
Complete raw-body/hash/binding checks and six actual padder negative controls
reject stale inputs. Control flow and memory accesses do not change.

## Qualification evidence

- Eight fresh target checks pass independently in each tools copy, plus
  both shared tool checks. Each installed copy runs two fresh source/image
  checks and reuses six unchanged checks only by complete input, module and
  qualified artifact fingerprints.
- Guest qualification passes 918 cases / 2,754 original, normalized and raw
  executions. All target instructions are exercised. Tests cover both valid
  slots, every actor position, empty/full/sparse/high-bit occupied records,
  zero/one/high-bit/alternate eligibility results, live helper mutations,
  timestamp wrap and helper-entry observations. Complete machine state and
  trace agree even for raw C. All 161 access cuts, including 41 delay cuts,
  agree. Six independent-rebase cases cross signed LO16 carry boundaries;
  six synthetic aliases qualify guest instructions without a portable C
  alias or hardware claim.
- Both JAL sites at ROM `0x4B414` and `0x4B438` execute through the original
  19-word `func_1501DF04` repeat window in 144 cases. The tests distinguish
  its latched flag from its live stop flag, exercise the branch-likely loop,
  and run up to three complete refresh invocations. The aligned retail
  census finds those two sites and no literal function pointers. The full
  parent and gameplay remain outside this bounded caller claim.
- The original 73-word eligibility routine is connected in 48 cases /
  144 executions, reaching 66 words. Tests cover direct/linked actor
  identities, empty pointers, type/identity filters and results zero, one
  and two. Other helpers remain ABI hooks with explicit side effects.
- Native SDK32 O0/O2/O3 with UBSan trapping pass 12,288 cases per profile.
  They verify the 804-byte actor layout, all 25 positions, complete actor
  pool contents, both timestamp slots, ordered helper observations and live
  mutations. Thirteen separately compiled IDO/native controls fail by
  explicit semantic comparison; compiler/interpreter/sanitizer failures
  are rejected. The void result is not read.
- Full raw/padded owner compilation preserves 56 neighbors and all pools
  with zero diagnostics. The actual three Make commands produce exactly
  the qualified object under the no-unroll profile.
- Independent full-image prediction equals first link and production ELF:
  195 changed bytes = 194 target code bytes + one target symbol extent byte.
  There are no metadata permutations or excluded ranges. All 6,055 other
  bodies and all 6,056 addresses remain fixed. Protected Game data is exact
  across 189,088 bytes and 720 owners.

Production ELF SHA-256:
`95b69ba2d22a64d2b1ca04937ad0d64c09d0e61f7ec35602123f35c883ee1edf`.
The map and C inventory CSV remain unchanged. Receipts and frozen inputs:
`conker/build/game-slot-actor-refresh-1501DE18-match/`.

## Progress and continuation

The actual adopted ELF recount is **3,994 / 5,506 (72.54%)** exact C,
Game **3,321 / 4,833 (68.72%)**, Init 492/492, Debugger 181/181, with zero
address drift. The threshold remains 4,130; **136** more verified functions
are needed for 75%. Conversion inventory totals do not change.

Next screen: `func_150B76BC`. Tools are committed before consumer source/guards/pin/
docs. The eleven-file graph update preserves prior nodes and valid directed
relationships and retires the one obsolete signed placeholder return edge.
No full-corpus extraction, global clustering, push, host-port or Release
work is claimed.
