# Game two-angle trigonometric updater byte match

Date: 2026-09-29

## Scope and behavior

`func_150A0D14` in `conker/src/game/generated_CDE80.c` occupies 30 words and
120 bytes at `0x150A0D14..0x150A0D8C`. It scales the float at record offset
`0xC` by `D_8009F5A0`, stores its cosine and sine at offsets `0x24` and
`0x28`, then scales the float at offset `0x10` by `D_8009F5A4` and stores its
cosine and sine at offsets `0x2C` and `0x30`.

## Source recovery

The previous body was a false zero-return placeholder. A narrow typed record
view names only the two input angles and four outputs without changing the
existing `GeneratedCDE80Record` used elsewhere in the slice. Correct `f32`
prototypes for `func_150AD78C` and `func_150AD780` recover floating-point
returns instead of the implicit integer ABI.

IDO reproduces retail's 40-byte frame, saved record pointer, saved `$f20`,
constant and input load order, four calls and delay slots, output stores, and
epilogue directly from the semantic C body. No expected-word guards are used.

## Verification

- The focused `generated_CDE80` object reproduces all 30 retail words.
- The full replacement build, outer non-matching build, and ELF relink pass.
- The authoritative matcher reports `3,016 / 5,463 (55.21%)` overall and
  `2,438 / 4,789 (50.91%)` in Game, with zero address-drift rows.
- Direct comparison reports zero differences across all 120 linked bytes.
- Both spans share SHA-256
  `dac05049dfcc33eb162289598122317e867b460999b13b459c433af7ce230fc4`.
- `make tools-check` and all 10 tests under `tools/tests` pass.

## Resume boundary

Inspect `func_150B6D78` as the next ordinary 33-word Game candidate. Keep
`func_15015F40` parked behind unresolved indirect-table ownership and
`func_150A76F0` in the handwritten-assembly queue.
