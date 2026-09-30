# Game randomized effect-parameter wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_150B6754` in `conker/src/game/generated_E2DA0.c` occupies 35 words and
140 bytes at `0x150B6754..0x150B67E0` including the function's three trailing
alignment words. It calls `func_150ADA20` twice, derives an unsigned
`200..255` parameter and an unsigned `15..25` parameter, and forwards them to
`func_15182670` with fixed RGB values, the incoming byte, and the incoming
32-bit context.

## Source recovery

The previous body was a false zero-return placeholder. The sole caller and
callee argument reloads establish a byte first parameter, 32-bit second
parameter, and the eight-argument effect ABI. Unsigned remainder expressions
reproduce retail's two `divu` operations. Keeping both PRNG calls directly in
the final call expression is essential: IDO then spills the first result to
retail stack offset `0x28`; a named local used `0x2C` instead. The complete
routine emits directly from C with no expected-word guards.

## Verification

- The focused `generated_E2DA0` object reproduces all 35 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,030 / 5,463 (55.46%)` overall and
  `2,452 / 4,789 (51.20%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 140 linked bytes at
  Game offset `0xB6754` and retail ROM offset `0xE3C04`.
- Both spans share SHA-256
  `fb70b61aec9a52557abb3566fc9c99564e9583ec845ef8e730bcde9ce3ec9209`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_150CC638`, the next ordinary 32-word placeholder. Retail
gates on a flag at offset `0x58`, advances a byte threshold from a signed
halfword, and conditionally adds a scaled record value to two float fields.
