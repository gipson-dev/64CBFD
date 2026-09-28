# Game per-entry cleanup loop byte match

Date: 2026-09-28

## Scope

This pass replaced the false zero-return placeholder for `func_15022754` in
`conker/src/game/generated_49D30.c` with its semantic Game routine. The retail
slot spans 26 words and 104 bytes.

## Recovered behavior

The function accepts an index into byte-count table `D_800C363A`. Starting at
entry zero, it calls `func_150226BC(entry, index)` once for every entry below
the current count.

The loop reloads `D_800C363A[index]` after every cleanup call. This is a
behavioral detail rather than redundant code: if the callee changes the count,
the next loop test observes the new bound. A zero initial count returns without
calling the helper.

## Compiler result

IDO emits all 26 retail words directly from the typed `do`/`while` loop. The
compiler reproduces the 40-byte frame; `s2`, `s1`, and `s0` lifetimes for the
index, count pointer, and loop counter; the opening zero-count gate; the
post-call byte reload; and the branch-likely loop with its argument-move delay
slot. No expected-word guards are required.

## Verification

- The focused `generated_49D30.c.o` build passed.
- Focused object disassembly matches all 26 retail instruction words.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_15022754` as byte-exact.
- The linked and retail 104-byte spans share SHA-256
  `37df4ff61f1705188a1a6f62ca49098bd2599db4c21f6962f81e7929ff52287b`.
- Fresh matcher totals are `2,899 / 5,466 (53.04%)` overall and
  `2,325 / 4,790 (48.54%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 33-word `func_150303E4`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
