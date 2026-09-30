# Game coordinate-query wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_150A32B4` in `conker/src/game/generated_CDE80.c` occupies 31 words and
124 bytes at `0x150A32B4..0x150A3330`. It builds a stack-local `struct127`
query from three signed integer coordinates, mirrors those coordinates into
the old-position fields, stores the vertical coordinate in `unk180`, submits
the query through `func_150A1DA0`, and returns whether that call returned zero.

## Source recovery

The previous body was a false zero-return placeholder. Retail's `0x350`-byte
frame contains exactly one `0x32C`-byte `struct127` at stack offset `0x24`.
Using that existing project type reproduces all integer-to-float conversions
and field offsets. Placing the independent `unk180` assignment before
`old_y_position` preserves retail's two-store order; the first semantic form
had only those two words reversed. The complete final routine emits directly
from C with no expected-word guards.

## Verification

- The focused `generated_CDE80` object reproduces all 31 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,029 / 5,463 (55.45%)` overall and
  `2,451 / 4,789 (51.18%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 124 linked bytes at
  Game offset `0xA32B4` and retail ROM offset `0xD0764`.
- Both spans share SHA-256
  `e14902f3383e5012a58c5da9916095a0fcfda96dd0709a830e73375e9fe79f5f`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_150B6754`, the next ordinary 35-word placeholder. Retail
uses two `func_150ADA20` results to derive bounded parameters, forwards the
incoming low byte and word, and calls `func_15182670` with fixed RGB values.
