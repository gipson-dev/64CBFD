# Game record find-or-create updater byte match

Date: 2026-09-29

## Scope and behavior

`func_151557FC` in `conker/src/game/generated_182C30.c` spans 40 words and
160 bytes at `0x151557FC..0x1515589C`. Its recovered body:

- Searches for the keyed record through `func_15155FD4`.
- Falls back to `func_15155780(key, 0xFF)` when no record exists.
- Returns without updates if allocation also fails.
- Stores the incoming float at record offset `0x98`.
- Reads actor-table byte `0xAD` using the keyed `0x32C`-byte record stride.
- For a nonzero actor byte, clears record halfword `0xE` and state byte
  `0x11`; otherwise it sets state three and stores the incoming timer.

The function has no meaningful return value, so its recovered signature is
`void`. Retail leaves the last record pointer in `v0`, but no path constructs a
defined result for callers.

## Compiler shape

The source must spell the nonzero actor-byte case first. That ordering makes
IDO emit retail's `beql` into the state-three path, the state-three store in
its delay slot, and the two fallthrough clears before branching over the timer
case. Reversing the source condition preserves behavior but produces a
different nine-word branch block.

All 40 instructions emit directly from semantic C. The frame, argument homes,
lookup and fallback calls, both call delay slots, actor-table stride sequence,
`D_800CC37D` relocation pair, branch-likely delay slot, and epilogue need no
expected-word guards.

## Verification

- The focused `generated_182C30` object builds with all 40 retail words.
- The complete ELF relink passes.
- Direct linked comparison reports zero differences across all 160 bytes.
- Both spans share SHA-256
  `26ead8d1e4d9a93f6827eea92120b99ba1e86a29c5067c4de1de8169a17e2dec`.
- The authoritative matcher omits `func_151557FC` from its non-exact list and
  reports `2,990 / 5,465 (54.71%)` overall and `2,415 / 4,789 (50.43%)` in
  Game, with zero address-drift rows.

## Resume boundary

Continue with the next ordinary small Game placeholder. The adjacent
`func_1515589C` is a much larger 280-word state machine and should be treated
as a separate recovery, not folded into this wrapper commit.
