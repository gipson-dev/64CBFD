# Game owner-payload allocation wrapper byte match

Date: 2026-09-29

## Scope and behavior

`func_1514F3CC` in `conker/src/game/generated_179F30.c` occupies 32 words and
128 bytes at `0x1514F3CC..0x1514F44C`. It builds a 12-byte stack payload from
the incoming owner pointer, the owner's byte at offset `0x3B`, and a zero
floating-point parameter. It asks `func_15149130` to allocate an object with
type `0x12C`, subtype `0x3A`, property `0x2B`, payload size `0x0C`, and the
remaining fixed selector values. When allocation succeeds, the payload is
copied to offset `0x28` in the returned object.

## Source recovery

The previous body was a false zero-return placeholder. A typed local payload
recovers the owner, unique-id byte, three bytes of untouched padding, and
floating parameter at the retail stack offsets. The direct allocator call and
conditional `memcpy` restore the `0x40` frame, argument stores, branch shape,
and payload copy. All 32 words emit directly from C with no expected-word
guards.

## Verification

- The focused `generated_179F30` object reproduces all 32 retail words.
- The linked non-matching build succeeds.
- The authoritative matcher reports `3,035 / 5,463 (55.56%)` overall and
  `2,457 / 4,789 (51.31%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 128 linked bytes at
  Game offset `0x14F3CC` and retail ROM offset `0x17C87C`.
- Both spans share SHA-256
  `0d2c9ded4f628ae40ae053987cf654b78cdca2553954cee3a4d9433974a4cc92`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect Game `func_15152ABC`, the next ordinary short placeholder reported by
the matcher. Keep `func_15015F40`, `func_150A76F0`, `func_15106E78`, and Init
`func_1000FF90` parked at their documented special-case boundaries.
