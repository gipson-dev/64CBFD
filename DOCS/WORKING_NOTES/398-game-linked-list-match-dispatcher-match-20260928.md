# Game linked-list match dispatcher byte match

Date: 2026-09-28

## Scope

This pass refined the existing semantic reconstruction of `func_150303E4` in
`conker/src/game/generated_5D2C0.c`. The retail slot spans 33 words and 132
bytes.

## Recovered behavior

The function rejects an input whose key byte at offset `0x3B` is zero. For a
nonzero key, it traverses the linked list rooted at `D_800C3EE0`. Every node
whose byte at offset zero matches the input key is passed to
`func_15030158(node, 0)`. The return value is one when any matching node was
handled and zero otherwise.

The node's link at offset `0x54` is loaded before the match handler is called.
That ordering preserves traversal even if the handler changes or releases the
current node.

## Compiler result

The prior C represented the broad behavior but made the current node the
saved-register lifetime and loaded its link after the comparison. An explicit
zero-key early return plus a preloaded `next` local makes IDO reproduce
retail's structure: current node in `a0`, next node in `s0`, result in `s1`,
and input in `s2`.

All 33 words now emit directly from semantic C, including both opening branch
paths, the branch-likely null-head return, the call delay slot, and the loop
backedge. No expected-word guards are required.

## Verification

- The focused `generated_5D2C0.c.o` build passed.
- Focused object disassembly matches all 33 retail instruction words.
- The full `wsl make -C conker NON_MATCHING=1` relink passed.
- `match_progress.py` classifies `func_150303E4` as byte-exact.
- The linked and retail 132-byte spans share SHA-256
  `5c1b5952bd66823179dfd610d3d9b5ba523126ca392c627190586bd569c251f3`.
- Fresh matcher totals are `2,900 / 5,466 (53.06%)` overall and
  `2,326 / 4,790 (48.56%)` in Game, with one address-drift row.

## Resume boundary

Resume the ordinary unparked queue with 27-word `func_1503A60C`, currently at
26 real differences. Keep the documented lower-difference compiler cases
parked. Also keep `func_151F3D78` parked behind the pre-existing audio-object
layout drift, keep the tied Init SDK cache routines in their ownership lane,
and keep address-drift row `func_10012588` parked.
